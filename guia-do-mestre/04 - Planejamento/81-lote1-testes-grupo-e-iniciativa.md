# L1 — testes, trabalho em grupo e iniciativa

26 de outubro de 2026. Continuação do primeiro lote da auditoria 80. Entrega: [Testes, trabalho em grupo e iniciativa](<../06 - Redacao do Guia/82-testes-trabalho-em-grupo-e-iniciativa.md>), com integração às seções 04/05/80. Os três procedimentos já existem na R53. Esta etapa acrescenta explicação e demonstração; não pede adoção de uma regra nova.

## O que o leitor recebeu

- Uma escolha de sucesso com custo: descobrir o destino de uma caixa com atraso, ou recusar esse tempo adicional e conservar a tentativa malsucedida. O custo tem consequência concreta no transporte.
- Uma comparação entre Ajudar, teste coletivo e ocultação individual em combate, com dados e limiares. Contribuição Decisiva aparece como exceção publicada, com seus requisitos e limite.
- Um empate de cinco participantes que percorre todas as prioridades da iniciativa: total, Destreza, jogador/inimigo e escolhas dentro de cada lado.
- Um lembrete de seleção de CD, ligado à escala e ao procedimento ambiental já escrito.

Os exemplos são originais e independentes dos pilotos. Seus recortes não são fichas completas ou um encontro pronto. O calendário do arquivo, o percurso e a percepção do vigia são escolhas locais para demonstrar as regras. Não foram acrescentados pontos de energia, ações, punições, surpresa ou parâmetros gerais de inimigos.

## Conferência da R53

Fonte: Livro do Jogador R53 editável, com a mesma cópia de referência usada nas etapas anteriores. Ambos conservaram SHA256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

| Fonte e linhas do texto editável | Aplicação |
|---|---|
| Testes, 150–180 | CD fixa/criador, igualdade como sucesso, margem de sucesso com custo e preservação de consequências fechadas. |
| Testes de grupo, 212–214 | Pelo menos metade; cinco participantes precisam de três sucessos; ocultação em combate é individual. |
| Turnos, 251–275 | Iniciativa e desempates; ordem conservada; Reação no começo do próprio turno. |
| Ajudar, 323–343 | Padrão, vantagem, contribuição concreta, prazo, um ajudante e requisitos. |
| Esconder, 1085–1112 | Observadores e sinais, CD de Percepção, total guardado, localização após falha e travessia coletiva fora de combate. |
| Contribuição Decisiva, 3065–3071 | Treino, sucesso próprio, uma vez por cena, momento e uma aplicação por teste, sem refazer dados. |
| Tarefas e testes, 7080–7130 | Atributo, tempo, repetição e distinção entre trabalho de um responsável e tarefa de todos. |
| Criação de entidades, 14690–14705 | Exceção da ajuda, aplicável também a reconstrução e transferência. |

As linhas não são páginas do PDF. Os [trechos conferidos](apoio-lote1/fontes-conferidas.md) preservam a identificação. O inventário M010/M014/M128 foi consultado na extração guardada pela auditoria anterior. Não houve pesquisa externa nesta etapa: os procedimentos necessários estavam publicados na R53.

## Casos conferidos

| Caso | Resultado e limite |
|---|---|
| Arquivo, sucesso normal | 17h40 + 10 minutos = 17h50; dado 10 + 4 alcança CD14. Não cobrar o custo alternativo de uma falha. |
| Arquivo, falha e custo aceito | 9 + 4 = 13; mais vinte minutos depois da tentativa terminam às 18h10. O transporte das 18h00 foi perdido; o arquivo segue aberto até 18h30. |
| Arquivo, custo recusado | Conserva a falta de resposta e os dez minutos já gastos; os vinte adicionais não são cobrados. |
| Ajuda antes do teste | Maior entre 9/15, somado a +4 = 19. Um teste com vantagem; não somar a ficha do ajudante nem reduzir o tempo automaticamente. |
| Cinco participantes | Totais 16, 12, 14, 8 e 14: três sucessos, limiar três. O resultado é coletivo para a travessia fora de combate. |
| Quatro participantes | Sem Emi, dois sucessos entre quatro ainda bastam. Esse caso confere a diferença entre metade e maioria absoluta. |
| Ramo de dois sucessos | Emi tira 9 e totaliza 13. Falha coletiva; uma Contribuição Decisiva válida acrescenta um sucesso à contagem e alcança três. Não muda as rolagens pessoais. |
| Ocultação individual | Durante combate, os mesmos totais localizam Nao e Tomo para o vigia. Cada tentativa consome a ação pertinente; não há resultado coletivo. |
| Iniciativa | Todos totalizam 14. Haste tem Destreza 3; demais, 2. Após as escolhas declaradas: Haste, Aoi, Nao, Trinco, Dobra. Não muda a cada rodada. |

As contas foram reproduzidas pelo [conferidor](apoio-lote1/conferir.py), com leitura das tabelas do manuscrito e [resultados salvos](apoio-lote1/resultados.json). O programa confere aritmética, referências e atualização dos estados editoriais. Não substitui a leitura da regra nem executa uma sessão.

## Revisão de clareza e integração

| Antes | Depois | Motivo |
|---|---|---|
| A seção 04 dizia para interpretar a falha quando a regra deixasse margem, sem acompanhar uma oferta completa. | A seção 82 mostra anúncio, falha, aceitação/recusa, calendário e resultado que não admite essa substituição. A seção 04 aponta diretamente para o caso. | O leitor consegue distinguir consequência, escolha e gasto efetivo. |
| Ajudar estava explicado, mas o teste coletivo não tinha demonstração completa. | Uma tentativa com vantagem é comparada a cinco rolagens e a um limiar de três. Combate individual e Contribuição Decisiva ficam em blocos próprios. | Evita somar bônus, exigir maioria absoluta ou apagar resultados individuais indevidamente. |
| A condução mandava organizar iniciativa, sem resolver um empate completo entre vários lados. | Quadro com total 14 para todos, inimigo de Destreza maior e escolhas fixas entre pares. | Mostra por que jogador não vem automaticamente antes de todo inimigo empatado no total. |
| A folha de condução não tinha os três lembretes. | Inclui resultado com custo, ajuda/grupo e sequência de desempate; o índice de ferramentas aponta para os casos. | A consulta pode ser feita durante a sessão sem abrir outro formulário. |

A revisão manteve a orientação da skill de redação acessível já aplicada ao projeto: procedimento antes de exceção, números completos e decisão visível. Os nomes e bônus do recorte foram conferidos para evitar tratar os exemplos como uma ficha inteira ou como mudanças nos personagens dos pilotos.

## Cobertura atual

| Ponto | Antes | Agora | Evidência principal |
|---|---|---|---|
| M010 — falha e sucesso com custo | P | E | Seção 82: arquivo e resultado fechado. |
| M014 — Ajudar e tarefas coletivas | P | E | Seção 82: ajuda, travessia, capacidade própria e contraste com combate. |
| M128 — empates entre inimigos | L | E | Seção 82: cinco totais iguais e ordem registrada. |

E significa base operacional demonstrada neste recorte, não certificação de aprendizagem. A atualização passa de **93 E/35 P/2 L para 96 E/33 P/1 L**. Restam **34 pontos** a complementar, com pesos diferentes. A lacuna L restante é M066, arma improvisada. Os casos de percepção de L3 ainda precisam de seus próprios complementos: a comparação de Esconder aqui não encerra todos os observadores, sentidos e usos informativos previstos.

As **20 competências conservam 16 E/4 P**. P08/P11/P18 recebem mais apoio, sem mudança de classificação. Não houve reclassificação dos outros 127 pontos nem nova auditoria integral do manuscrito. A [cobertura atualizada](apoio-lote1/cobertura-atualizada.json) conserva os IDs/naturezas e relocaliza as evidências nos textos integrados. A auditoria 80 e seu JSON são retratos anteriores, preservados; o aviso na abertura aponta para esta atualização.

## Preservação

Os 312 arquivos do manifesto inicial estavam íntegros. Treze arquivos receberam integração ou atualização de planejamento/navegação; suas versões anteriores foram copiadas para `apoio-lote1/historico/`. As fontes, decisões autorais, fichas de inimigos, Pactos, projetos e cálculos anteriores permanecem preservados. Os textos 04/05/80 mudaram somente para conectar os procedimentos e a consulta.

O [registro de verificação](apoio-lote1/verificacao.json) delimita as conferências do pacote. O programa desta etapa, sem `--salvar`, é somente leitura; com essa opção, grava exclusivamente `resultados.json` em sua própria pasta. Não altera o manifesto. Para a integridade atual de todo o salvamento, usar `CONFERIR-SALVAMENTO.py`, na raiz. Verificadores de etapas históricas com hashes de textos antigos não substituem essa conferência atual.

Não houve sessão humana, nova simulação de combate, pesquisa externa ou envio ao GitHub. Treinamentos mecânicos, Bestiário completo e os desenvolvimentos de Pactos já adiados conservam seus destinos.

**Próxima tarefa:** L3 — percepção e informação: Esconder, Ler o Ambiente, Intuição e lembranças, busca energética com interferência e sinais/assinaturas. **GPT-6 Astra, esforço extra alto**, para regras e casos; **GPT-6.1 Sol, esforço alto**, para clareza e integração.

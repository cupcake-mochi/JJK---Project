# Primeira missão reunida e comentada — registro 100

28 de outubro de 2026. Entrega da etapa 2 do [plano 98](98-plano-de-melhoria-e-validacao-do-guia.md), usando a [estrutura 99](99-sumario-comentado-e-caminhos-de-leitura.md).

## Resultado

O capítulo **Sua primeira missão** foi escrito como nova entrada do Guia. Reúne contexto, acordos, cotidiano, preparo, NPCs, planta, ficha completa do Amontoado, investigação comentada, confronto com socorro, alternativas e fechamento. A folha preenchida de preparação fica no fim da amostra para consulta durante a sessão.

- [Texto editável do capítulo](<../06 - Redacao do Guia/revisao-98/01-sua-primeira-missao.md>).
- [Amostra de leitura em HTML](apoio-primeira-missao-100/capitulo-1.html).
- [PDF da amostra](apoio-primeira-missao-100/output/pdf/Ciclo-Maldito-Sua-Primeira-Missao-Amostra.pdf).
- [Trechos do Livro de Regras e conversões para consulta](apoio-primeira-missao-100/consulta-de-regras.html).

A amostra é isolada: a edição integrada de 357 páginas permanece como referência anterior até a integração dos demais capítulos. A nova fonte está na subpasta `revisao-98`, fora da lista antiga de 104 fontes. Isso evita misturar a entrada nova com os mesmos pilotos ainda presentes no livro atual.

## O que mudou na maneira de ensinar

A missão antes exigia procurar preparo, exemplo e inimigo em partes distantes. Agora apresenta primeiro o que o leitor precisa para acompanhar a situação, e depois mostra as escolhas de condução. A estrutura distingue descrição, fala de jogador e comentário do mestre. O acesso a contexto de mundo mais amplo fica opcional; a entrada não exige conhecimento da trama de Jujutsu Kaisen.

As falas mostram informação disponível sendo obtida por conversa, uma pergunta pertinente de posição, a leitura dos sinais e a passagem para o combate. As alternativas incluem conversar com a criatura, usar outro acesso, sair do confronto e encaminhar o chamado. O fechamento diferencia ameaça resolvida, riscos do lugar, atendimento e pendência assumida por um contato.

A guilda continua como referência do sistema. A mesma ocorrência oferece uma ligação para campanha fechada. O texto usa os nomes Livro de Regras 1.0, PV, PE e CD, explicando as abreviações antes de usá-las nas contas. Dados escolhidos ensinam o funcionamento; não determinam o resultado de uma sessão real.

## Confronto simplificado

O exemplo antigo de três rodadas e duas quedas continua preservado nas fontes anteriores. A entrada usa **duas rodadas e uma queda**, com os mesmos máximos e capacidades da base experimental. O crítico inicial demonstra Insistir; uma cura de 5 não completa o requisito de 8. Na volta ao ponto da queda, o prazo cai de três para duas rodadas. A cura seguinte de 3 completa o atendimento. A frente termina com 8 PV, 2 PE e uma Sequela.

O Amontoado gasta 6 PE em duas tentativas; a segunda erra. Os quatro acertos dos personagens causam 12, 14, 12 e 11 de dano, derrotando seus 48 PV. O apoio termina com 4 PE e a conjuradora com 6. Não há dano de Alma ou perda de Integridade no roteiro. A ficha do inimigo foi mantida, com seus valores e capacidades experimentais, sem recorrer ao Bestiário antigo.

A [conferência executável](apoio-primeira-missao-100/CONFERIR-EXEMPLO.py) verifica as contas, o uso de recursos, o requisito de cura e posições possíveis dentro da sala. O [resultado](apoio-primeira-missao-100/verificacao-do-exemplo.json) registra a sequência. Trata-se de conferência do exemplo escrito, não de previsão de dificuldade ou simulação de decisões livres.

## Planta do anexo

A [planta vetorial](apoio-primeira-missao-100/planta-do-anexo.svg) usa as dimensões do preparo existente: pátio 6 × 6 m, corredor 9 × 3 m, depósito 6 × 6 m e portas de 1,5 m. Mantém os dois acessos ao mesmo corredor, a única porta do depósito e a posição inicial do Amontoado a 4,5 m dela. A recepção aparece indicada fora do desenho.

Foram escolhidos cômodos desenhados como áreas e portas visíveis, com as cotas separadas, para evitar a ambiguidade de um fluxograma de rotas. Na primeira prova, a cota vertical interferia com os rótulos do depósito e das caixas; foi reposicionada antes da entrega. A planta é um recurso original em vetor, construído para esta missão; não foi inserida uma ilustração decorativa sem função.

## Revisões e limites

A primeira passagem textual conferiu sequência, linguagem, fatos do preparo e regras. A segunda leitura da prova conferiu abreviações, referências, contas, condições de Estabilizar, passagem entre cenas e leitura de colunas. Foram acrescentadas definições curtas de PV, PE e CD, explicitados os requisitos de estabilização e ajustada uma referência ao fechamento.

A primeira prova visual tinha 11 páginas com quebras fixas por tópico. A condução passou a fluir entre páginas, reduzindo a amostra para **10 páginas**, sem diminuir as fontes. O padrão usa A4, margens de 19 mm, corpo Spectral 10,25/13,2 pt, intervalo de 7 mm entre colunas e títulos Barlow Condensed/Bree Serif. Mapa, tabelas e quadro da criatura recebem composição adequada à largura necessária.

As dez páginas da prova final foram renderizadas e examinadas para conferir colunas, parágrafos, tabelas, mapa e espaços. Depois do último ajuste, as páginas 8–9 foram examinadas novamente: o título e a introdução do estado do grupo agora ficam junto da tabela. As outras oito páginas permaneceram idênticas à prova já examinada. A inspeção está registrada em [revisão da amostra](apoio-primeira-missao-100/revisao-final.json). Os espaços restantes serão considerados também na integração ao livro, quando os capítulos seguintes participarem do mesmo fluxo.

As consultas de regras foram extraídas da referência mecânica e têm acesso separado em HTML. As conversões experimentais para Doma vêm da mesma base pequena autorizada. A regra completa de entidades continua necessária quando uma ficha puder adquirir a maldição; a simples derrota não realiza essa aquisição. As fichas parciais da demonstração não são personagens prontos para distribuição.

**Leitura externa e mesa ainda não foram realizadas nesta entrega.** A avaliação interna verifica se os elementos estão acessíveis e coerentes; não afirma aprendizado observado, equilíbrio ou equivalência já alcançada com os outros guias. O alvo inicial de 12–16 páginas do registro 99 era uma referência editorial flexível: a amostra ficou mais curta ao reunir o conteúdo e rever as quebras, preservando os elementos exigidos.

## Continuidade

Etapa 2 entregue como texto de trabalho e amostra. A incorporação ao livro completo ocorrerá com a revisão e integração previstas no plano 98. Preservar esta versão para comparar as mudanças e receber sugestões enquanto a redação prossegue.

**Próxima tarefa recomendada:** etapa 3, revisar o núcleo de ensino, começando por **O mundo dos feiticeiros** e **Preparar aventuras**, com contexto opcional, preparo mínimo e orientação para criar outra missão. **GPT-6.1 Sol, esforço alto.** Questões mecânicas que exijam comparação ampla continuam na frente própria, com GPT-6 Astra, esforço extra alto.

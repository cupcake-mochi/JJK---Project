# Primeira régua experimental de inimigos

26 de outubro de 2026. Continuação de C04 após o ensaio guiado. Entregue a [seção 74 — Escolher os números de um inimigo](<../06 - Redacao do Guia/74-regua-inicial-de-inimigos.md>). O trabalho oferece pontos de partida nos níveis 2 e 6, separa campos determinados pela R53 de parâmetros propostos e mede o efeito das escolhas. **Não atualiza as fichas existentes nem estabelece uma escala geral aprovada.**

## Direção recomendada

Usar um rascunho central de **24 PV / 12 de Integridade no nível 2** e **72 / 36 no nível 6**, com uma aplicação ofensiva na Padrão e Defesa 13 sustentada por componentes legais. Comparar vida menor e maior e Defesa 11/15, antes de escolher a ficha final. Ataque +4/CD12 e +5/CD13 vêm de atributo 3/4 com Maestria 1; não são bônus impostos somente pelo nível.

Essa é uma **proposta editorial do assistente**, sem aprovação autoral atribuída. A coluna central organiza a primeira tentativa de criação, não define encontro moderado. Os dois níveis não geram fórmula de interpolação, multiplicador de chefes ou equivalência de criaturas por personagem.

Uma régua baseada apenas em PV por nível seria insuficiente: o recorte misto muda mais no nível 6 porque o feitiço puro chega a 6d8 enquanto a espada de uma mão permanece em 1d8, com modificadores. O efeito das ações, do repertório e dos recursos aparece antes de uma possível escala universal.

## Fontes e método

R53 atual conferida com a [cópia preservada](apoio-carregador/fontes/LIVRO-COMPLETO-R53.md), SHA-256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`. Consultados: Maestria, Defesa/Bloquear, ataques, TRs, progressão, Caminhos, dano/crítico, Integridade, cura e queda, montagem de Classe 1/2 e Refino. As fichas locais usadas são Carregador e Sineiro; o Bestiário desatualizado continua excluído dos números.

A camada curada de inimigos e o relatório 05 do acervo **Pesquisa de Campo — Inimigos, Itens e Técnicas** serviram de orientação para a leitura dirigida. A conferência externa de 26/10 foi feita nas fontes abaixo:

- [Pathfinder 2e, GM Core — Building Creatures](https://2e.aonprd.com/Rules.aspx?ID=2874): conceito e função precedem o conjunto numérico; vida, defesa e capacidades precisam ser examinadas juntas. O uso dessa organização no Guia é uma adaptação editorial. Nenhuma estatística, escala de nível ou orçamento de encontro foi transportado.
- [D&D 2024 — How to Use a Monster](https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster): ficha distingue ações e limitações de uso, incluindo recarga e recuperação por descanso. Sustenta a comparação de procedimentos, não uma obrigação de recarga no Ciclo Maldito.

O cálculo é por **enumeração de distribuições**, não por dados sorteados, mesa humana ou simulação integral. [Programa](apoio-regua-inicial/calcular.py), [resultados](apoio-regua-inicial/resultados.json), [estado anterior](apoio-regua-inicial/estado-inicial.json) e [verificação](apoio-regua-inicial/verificacao.json). O programa reutiliza as funções de dados, ataques e Bloquear do apoio à etapa 73, sem alterar seus arquivos. `--salvar` escreve somente resultados.json.

## Perfis usados

São recortes parciais de Bastião, Emanador e Guia, nessa ordem. Não foram preenchidas ou ativadas todas as capacidades de Origem e Trilha. Traje1 e Destreza2 dão Defesa13; não se acrescenta a proteção passiva de Refino sobre o Traje. O nível6 conserva o recorte já conferido, com marco Corpo.

| Nível / Caminho | Força / Destreza / Constituição / Inteligência / Essência | PV | PE | Integridade | TR Físico |
|---|---|---:|---:|---:|---:|
| 2 / Bastião | 3 / 2 / 2 / 1 / 1 | 23 | 8 | 26 | +4 treinado |
| 2 / Emanador | 0 / 2 / 2 / 3 / 2 | 14 | 12 | 27 | +3 treinado |
| 2 / Guia | 0 / 2 / 2 / 2 / 3 | 17 | 10 | 28 | +2 sem treino |
| 6 / Bastião | 4 / 2 / 3 / 1 / 1 | 65 | 24 | 50 | +5 treinado |
| 6 / Emanador | 0 / 2 / 3 / 4 / 2 | 44 | 36 | 55 | +3 treinado |
| 6 / Guia | 0 / 2 / 3 / 2 / 4 | 51 | 30 | 65 | +2 sem treino |

Nível2: nove pontos de atributo, Refino1, Classe1. Nível6: onze pontos após progressão e Corpo, Refino2, Classe2. Constituição aplicada a todos os níveis. As reservas vêm do Caminho; a vida inimiga não usa essas fórmulas automaticamente.

Feitiços puros de Concussão: Classe1/3PE/3d8/+4 ou Classe2/6PE/6d8/+5, sem Melhorias ou Restrições. Bastião usa Toque com Selo verbal e mão livre; os outros, Projétil, com suas mãos disponíveis. A devolução de Toque não cria dados adicionais onde não há pontos pagos para devolver. O atributo da técnica acompanha o atributo ofensivo de cada recorte, e sua Regra precisa comportar a aplicação. Cada personagem pode pagar duas dessas conjurações na reserva cheia:6 ou12PE.

No recorte misto, Bastião substitui suas conjurações por Espada Longa em uma mão, 1d8 + Força +1d4 de Canalizar. Crítico dobra apenas o d8 básico. Não são executados Kokusen, efeitos de arma ou respostas de Caminho. A alternativa não representa o dano máximo do Bastião.

## Resultados e interpretação

Há **72 curvas**, combinando dois níveis, três reservas, três Defesas, Defesa estática ou Bloquear e sequência de feitiços ou mista. Cada curva acompanha até seis declarações no grupo, duas por pessoa. Todas incluem erros e críticos. Não incluem dano recebido pelos jogadores, perdas de ação, concentração, cura, deslocamento, controle ou resultado da missão.

As tabelas principais estão na seção74. Destaques que orientam a proposta:

- No nível2, 24PV/Defesa13 permanecem acima de zero após três declarações em 43,4% com feitiços e 50,1% no misto. Essa reserva pode ser curta contra três ofensivas disponíveis; não serve como promessa de chefe duradouro.
- No nível6, 72PV/Defesa13 produzem 70,1% e 88,0%, respectivamente. A coluna central não significa a mesma duração nos dois níveis. Essa assimetria fica explícita, em vez de ser apagada por um nome de dificuldade.
- Com108PV, subir a Defesa de11 para15 muda a sobrevivência após seis declarações mistas de55,3% para81,4%. A análise apoia conferir o conjunto e preservar a Defesa11 do Sineiro, sem promover essa escolha a regra universal.
- O valor32PV do Carregador é comparável a outras reservas, mas sua Pancada é **1d4 +3**, não4d4 +3 nem um golpe energético. Seu dano pequeno combina com uma função de contenção; não foi corrigido para maior dano por estar abaixo de um feitiço de Classe1.

Bloquear foi enumerado com duplo10, duplo1 e prioridade de20 natural. Seus possíveis revides não são executados. Por isso, comparar apenas a sobrevivência da reserva não esgota o valor dessa defesa. Os testes analíticos conferem médias conhecidas, acerto estático, normalização, monotonicidade e coincidência com a curva108PV da etapa73.

## Pressão de dano e controle

A alternativa ofensiva de nível2, 1d8 +3 com ataque+4, fica como proposta para comparar com a Pancada do Carregador, e não como dano obrigatório. Contra Defesa13, as médias por declaração são4,73 e3,43. O crítico da alternativa chega a19 e pode levar uma personagem de14PV a zero em uma aplicação:1,64% no recorte sem proteção adicional. A Pancada comum do Carregador não chega a14 em um golpe.

Em duas declarações, contra14PV cheios, a chance de chegar a zero muda de4,9% para27,0%. Com7PV iniciais, muda de50,3% para67,3%. Contra o perfil de23PV, duas declarações da alternativa dão1,45% a partir da vida cheia e33,42% começando com12PV. Acompanhantes e concentração de golpes merecem conferência antes de atribuir um segundo ataque.

No nível6, uma Pancada2d6 +4/+5 contra Defesa13 tem média7,50. Duas declarações contra44PV chegam a zero em aproximadamente0,0153% com vida cheia, mas26,62% começando com22PV. Isso não inclui o impacto5d8, já avaliado na etapa73, nem significa que uma ameaça deva receber mais dano para derrubar personagens cheios.

CD12 versus Físico+4/+3/+2: falha35/40/45%. CD13 versus+5/+3/+2:35/45/50%. Manobra substituindo o único ataque disputa dano; substituindo um de dois, conserva outro golpe. O procedimento de saída, o acesso ao alvo e o custo de ação continuam necessários à avaliação.

## Propostas, regras e pendências

**Regras preservadas:** fórmulas comuns, atributos, treinos, ações, recursos efetivos, estados, aquisição e derrota. ZeroPV de jogador não é derrota automática; zeroPV/Integridade do inimigo encerra sua atuação, salvo regra própria. Vida e Integridade da Doma são construídas pela rota de aquisição.

**Propostas novas:** valores centrais24/72, comparação16/24/32 e48/72/108, organização por função e uso de uma aplicação ofensiva como rascunho inicial. Defesas11/13/15 são sensibilidades com exigência de componentes válidos. Nenhum campo foi aprovado pelo autor nesta etapa.

**Ainda não coberto:** níveis intermediários ou altos; perfis resistentes, evasivos, apoiadores e conjuradores completos; múltiplos inimigos com iniciativa; área contra vários alvos; dano de Alma e acesso específico; efeitos de defesa combinados; rotinas com PE; classes de dificuldade e orçamento de encontros. A condição de fraqueza não compra um bônus em pontos; não foi inventado esse sistema de orçamento.

As fichas existentes de Carregador, Sineiro e respectivas Domas ficam intactas. P75/G74 iniciam o construtor geral; não encerram M124 ou C04. Não há nova pergunta obrigatória antes de aplicar a proposta: a continuação autoriza desenvolver e conferir exemplos, mantendo os números como candidatos.

**Próxima tarefa recomendada:** aplicar a régua a dois rascunhos completos de nível6 com funções diferentes — um atacante e um apoio — e conferir uma composição com ambos contra o trio de referência. Isso deve avaliar foco de ataques, interação entre capacidades, perda de pressão quando um cai e gasto real de recursos antes de propor dificuldade. **GPT-6 Astra, esforço extra alto**; revisão de clareza com **GPT-6.1 Sol, esforço alto**. Bestiário integral e treinamentos continuam adiados.

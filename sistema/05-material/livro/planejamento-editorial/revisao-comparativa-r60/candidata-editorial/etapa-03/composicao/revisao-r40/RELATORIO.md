# R40 — Sumário, hierarquia e ordem de níveis

Entrega de 08/10/2026. 373 páginas. Base R39 preservada, com todos os arquivos comparados por SHA-256. Sem commit nem push.

## O que mudou

- Sumário ampliado de uma para três páginas: 21 capítulos e 156 seções, com links conferidos. Inclui Lapidação, Restrição Celestial e sua criação sem energia, Sem Técnica como Origem e como rota, os seis Caminhos, todas as Trilhas e as três rotas do Batedor.
- Marcadores do PDF seguem essa hierarquia. O índice distingue os destinos de Restrição Celestial e Sem Técnica.
- Habilidades dos seis Caminhos usam nome em título de entrada e nível em linha própria. Agrupadores, detalhes e exemplos conservam funções visuais distintas.
- Tabelas de progressão acrescentadas às três Trilhas do Guia, usando exclusivamente os nomes e níveis já existentes. Demais tabelas padronizadas; o Batedor mantém sua tabela conjunta de três rotas.
- Assassino: todas as habilidades de nível 2 precedem as duas de nível 11. Golpe Cirúrgico aparece na sequência inicial.
- Pugilista: Rajada Marcial passa a aparecer após as habilidades de nível 2; a primeira frase explica que é a melhoria de Corpo Treinado recebida no nível 7.
- Evocador: Dificultar a Resistência, nível 7, aparece após todas as intervenções iniciais de nível 2.
- Tratar e Retomar e outras capacidades antes apresentadas como marcadores receberam a hierarquia de habilidade.
- Aberturas de Trilhas sem arte e introduções de listas receberam proteção contra separação prematura. Leitura segue a coluna esquerda inteira e depois a direita.
- Espaçamento vertical das entradas do índice reduzido em 0,4 pt por linha, mantendo fonte e tamanho; isso evitou uma página adicional com apenas duas entradas.

## Preservação do conteúdo

São 91 blocos com antes/depois em `ALTERACOES-TEXTO.json`. A comparação com a R39 não encontrou diferenças textuais fora desses registros. As mudanças são de títulos, metadados, tabelas de consulta, ordenação e explicitação da Rajada; não houve alteração de custo, efeito ou nível de aquisição.

As regras, exemplos e contas foram preservados. O exemplo de Escolher a Próxima Vítima foi deslocado junto da habilidade, sem reescrita; seu destaque foi relocalizado no catálogo. Nenhum exemplo foi recalculado. Os custos de Resposta Coordenada e a frequência de Todos no Mesmo Plano foram separados do parágrafo, sem retirada de conteúdo. Fontes, tamanhos, arte, capa e créditos mantidos.

## Conferência individual de níveis

A coluna abaixo mostra a sequência de aquisição; repetições de um mesmo nível foram resumidas. Batedor possui uma tabela conjunta e três rotas conferidas separadamente. Referências a evoluções futuras dentro de uma regra não foram confundidas com novas habilidades.

| Caminho, Trilha ou rota | Início na R40 | Sequência |
|---|---:|---|
| Bastião | 86 | 2 → 7 → 15 → 23 → 30 |
| Muro | 89 | 2 → 11 → 19 → 27 |
| Punho | 90 | 2 → 11 → 19 → 27 |
| Combatente Amaldiçoado | 92 | 2 → 11 → 19 → 27 |
| Vanguarda | 94 | 2 → 7 → 15 → 23 → 30 |
| Estocada | 98 | 2 → 11 → 19 → 27 |
| Batedor | 100 | Tabela conjunta; conferir as três rotas abaixo. |
| Batedor: Yumi | 100 | 2 → 11 → 19 → 27 |
| Batedor: Besta | 102 | 2 → 11 → 19 → 27 |
| Batedor: Arma de Fogo | 104 | 2 → 11 → 19 → 27 |
| Executor | 106 | 2 → 11 → 19 → 27 |
| Guia | 108 | 2 → 7 → 15 → 23 → 30 |
| Arquiteto | 112 | 2 → 11 → 19 → 27 |
| Analista | 115 | 2 → 11 → 19 → 27 |
| Socorrista | 116 | 2 → 11 → 19 → 27 |
| Emanador | 119 | 2 → 7 → 15 → 23 → 30 |
| Condutor Armado | 124 | 2 → 11 → 19 → 27 |
| Ressonante | 127 | 2 → 11 → 19 → 27 |
| Catalisador | 129 | 2 → 11 → 19 → 27 |
| Evocador | 131 | 2 → 7 → 15 → 23 → 30 |
| Invocação Principal | 138 | 2 → 11 → 19 → 27 |
| Parceria | 141 | 2 → 11 → 19 → 27 |
| Múltiplas Invocações | 146 | 2 → 11 → 19 → 27 |
| Incursor | 152 | 2 → 7 → 15 → 23 → 30 |
| Assassino | 156 | 2 → 11 → 19 → 27 |
| Pugilista | 161 | 2 → 7 → 11 → 19 → 27 |
| Malabarista | 166 | 2 → 11 → 19 → 27 |

Fluidez no nível 15 e Obras maiores foram conferidos como evoluções das capacidades existentes, na sequência correta. As escolhas internas de uma mesma capacidade permanecem juntas; os nomes de todas as entradas verificadas estão em `SEQUENCIAS-DE-NIVEL.json`.

## Validação final

- 117.400 verificações automáticas; zero problemas detectados. Cobertura: conteúdo dos 500 blocos, extração do PDF, fontes, margens, sobreposições, destinos e numeração.
- 2432 links internos e 184 marcadores conferidos; 177 linhas clicáveis do sumário verificadas individualmente.
- Nenhuma sequência descendente de níveis no inventário e nenhum par de títulos adjacentes com a mesma apresentação detectado.
- Inspeção visual das 86 páginas do capítulo Caminhos e Trilhas (86–171), das três páginas do sumário, das quatro do índice e das três páginas externas recompostas (265, 283 e 322).
- Os outros 16 capítulos preservam a composição da R39, descontada a mudança na numeração das páginas.
- As folgas antes de aberturas ilustradas foram preservadas; esta rodada prioriza a hierarquia e a continuidade, sem reduzir o tamanho da letra.

O livro passou de 367 para 373 páginas: duas adicionais no sumário e quatro na recomposição de Caminhos e Trilhas. O índice permaneceu com quatro páginas.

## Registros

- `ALTERACOES-TEXTO.json`: antes/depois dos 91 blocos.
- `ALTERACOES-HIERARQUIA.json`: classificação dos títulos alterados.
- `ALTERACOES-DIAGRAMACAO.json`: todos os blocos com diferenças de posição, composição ou página, inclusive elementos gerados.
- `DECISOES-DE-COMPOSICAO.json`: decisões de navegação e continuidade.
- `CONFERENCIA.json`, `REVISAO-VISUAL.json` e `COMPARACAO-COMPOSICAO.json`: evidências da revisão.

## Próxima etapa

Leitura e aceite do autor sobre a R40. Para analisar retornos que envolvam entendimento e cruzamento de regras, recomendação editorial: GPT-6 Astra, esforço alto. A recomendação considera o tipo de trabalho, não uma comparação medida entre modelos.

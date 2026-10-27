# L2 — espaço, objetos e capacidades do cenário

26 de outubro de 2026. Entrega dos complementos de M019, M020, M021, M022, M054, M064 e M066. O material foi dividido em [Percursos, apoios e quedas](<../06 - Redacao do Guia/84-percursos-apoios-e-quedas.md>) e [Trajetórias, ferramentas e improvisação](<../06 - Redacao do Guia/85-trajetorias-ferramentas-e-improvisacao.md>), com integração às consultas existentes.

## O que foi completado

| Ponto | Caso e resultado de ensino |
|---|---|
| M019 | Natação de 4,5 m com correnteza: custo da modalidade, teste único, sucesso e posição anunciada na falha. |
| M020 | Salto de 6 m com esforço e risco de piso: uma rolagem contra CD 18, movimento reservado e chegada definida nos dois resultados. |
| M021 | Duto com maleta incompatível; queda sobre criatura com divisão antes das defesas, alvo evitando o corpo e diferença de tamanho fora da faixa. |
| M022 | Ricochete chega pela lateral da cobertura, alterando a Defesa de 16 para 14 no exemplo. |
| M054 | Passarela de Obras de Apoio, percurso de Parkour e Ricochete, com apoios, custos, limites e uso da capacidade. |
| M064 | Instalação de corda e kit; fechadura com falha anunciada; contenção compatível e formas de soltura. |
| M066 | Cabo comparado a Bastão e garrafa pelo perfil genérico: treino, mãos, ação, acerto, dano, alcance, crítico e quebra. |

As regras vêm da R53. As posições, os riscos ambientais e os perfis locais de objetos foram apresentados como exemplos, sem atribuir ao autor aprovação de uma tabela nova. Os recortes não são encontros completos nem fichas de personagens prontas. Os exemplos antigos da passarela e do Carregador conservam seus parâmetros e seu estado experimental.

## Fonte conferida

O Livro do Jogador R53 editável e sua cópia preservada conservaram SHA256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`. Os [trechos de referência](apoio-lote2/fontes-conferidas.md) guardam linhas da fonte editável, não páginas do PDF, e as entradas correspondentes do inventário.

Foram consultados Movimento e terreno; Espaço e posição; Saltos; Quedas sobre criaturas; Rastejar e passagens estreitas; Ataques, Dano e crítico; Defesa e cobertura; Abrir Caminho e Obras de Apoio; Movimento Acrobático, Parkour, Fluidez e Ricochete; Sacar e guardar; catálogos de Porrete e Arremesso; Exploração e ferramentas; Fechaduras e contenção; Armas improvisadas. Não foi necessária nova pesquisa externa para aplicar esses procedimentos publicados.

## Conferência dos casos

| Caso | Contas e limites conferidos |
|---|---|
| Canal | 4,5 m custam 9 m na natação comum regular; variantes custam 4,5/13,5/9 m. Atletismo 9 + 5 = 14 passa; 8 + 5 = 13 falha. A grade e o gasto reservado na falha pertencem ao cenário anunciado. |
| Salto | Força 1: 4,5 m com impulso; esforço amplia a 6 m. Impulso 3 + salto 6 = 9 m. CD maior entre 14 e 18 = 18. Treino e especialização: 1 + 2 + 1 = +4; dados 14/13 produzem 18/17. Queda real de 3 m: 1d6. |
| Duto | 1,5 + 1,5 + 1,5 = 4,5 m; com terreno difícil, 6 m. A bagagem incompatível fica fora. Rastejar não levanta automaticamente. |
| Impacto | 3d6 = 11; alvo recebe 5 e Ema recebe 6 antes das defesas. Resistência de Ema reduz sua parte a 3. Se o alvo evitar, ela recebe a queda inteira reduzida a 6. Médio/Grande está na faixa; Médio/Imenso não reparte dano. |
| Obra | Nível 2, atributo 3, Maestria 1: limite 3, duração 30 minutos, Vida 27, Defesa 11, carga 300 kg. Bônus e 2 PE ao todo; Abertura e obra têm prazos distintos. |
| Parkour | Movimento 12; limite acrobático 6. Parede 3 + salto 4,5 = 7,5 m; restam 4,5 m de movimento e 3 m de limite. Mão ocupada no apoio; risco CD 14 conserva dificuldade ao trocar Atletismo por Acrobacia. |
| Ricochete | 6 + 6 = 12 m, faixas ampliadas 12/24. Cinco percursos contrastam o primeiro trecho e o total. Ataque 9 + 5 = 14; dano 3 + 2 = 5. Última direção remove somente a cobertura que não protege daquele lado. |
| Kit e fechadura | Um minuto e duas mãos na instalação; descida de 6 m custa 12 m. Folga de 1,5 m não causa dano de altura. Fechadura reforçada CD 18: 12 + 5 = 17 falha às 16h01; nova tentativa possível exige outro minuto, com 13 + 5 = 18. |
| Algema | Instalação em um minuto com alvo elegível; romper exige Atletismo CD 24. Totais 23/24 falham/passam. Sem supressão automática de energia ou de ações independentes das mãos. |
| Cabo e garrafa | Referência Bastão: ataque +3, 1d6 + 2, alcance 1,5 m, sem propriedades incompatíveis. Perfil genérico: corpo a corpo +3, arremesso +5, 1d4 + 2, faixas 6/18. A 9 m, duas fontes de desvantagem mantêm dois d20; menor entre 17/9, +5 = 14; dano 5. Crítico seria 2d4 + 2. |

O [conferidor](apoio-lote2/conferir.py) reproduz contas e limites e confere as referências de cobertura; os [resultados](apoio-lote2/resultados.json) ficam preservados. Não houve simulação integral de combate, resgate ou aprendizagem com pessoas.

## Clareza e integração

| Antes | Depois | Motivo |
|---|---|---|
| Havia escalada e salto simples, mas não risco combinado ou correnteza resolvida. | Canal e salto mostram custo, um teste e posição final na falha. | Evita testes por quadrado e a escolha tardia da consequência. |
| Queda sobre criatura e passagem estreita tinham referência geral. | Duto distingue corpo de bagagem; impacto separa faixa de tamanho, TR, divisão e defesa. | Permite conduzir a chegada sem inventar passagem ou dano adicional. |
| A cobertura era calculada para uma direção direta. | Mapa de pontos e cinco percursos verificam Ricochete. | Mostra o efeito do último trecho e os dois limites de distância. |
| Ferramentas apareciam como requisitos. | Instalação, folga, mãos e fechadura têm execução completa. | Evita kit sem conexão, ação duplicada ou gazua quebrada automaticamente. |
| Não havia perfil completo de arma improvisada. | Um objeto semelhante e outro genérico recebem requisitos, ataque, dano e destino após o uso. | Ensina a comparação local sem copiar todas as propriedades do catálogo. |

As seções 05, 11, 34, 64 e 80 receberam lembretes ou remissões. Navegação, referências e planejamento foram atualizados. Nenhum novo formulário geral foi criado.

## Cobertura e preservação

Somente os sete pontos do lote mudam de estado: seis passam de P para E, e M066 passa de L para E. A cobertura atual fica em **108 E/22 P/0 L**. E significa base operacional demonstrada, sem certificar uso ou aprendizado. Não restam entradas classificadas como procedimento não localizado, mas **22 pontos ainda precisam de complemento**, além das quatro competências parciais. Isso não equivale a conclusão da pré-1.0.

As competências conservam **16 E/4 P**. A [cobertura atualizada](apoio-lote2/cobertura-atualizada.json) mantém o escopo e relocaliza evidências dos textos integrados; não é uma nova auditoria integral dos outros 123 pontos. L1, L3 e L2 estão entregues. As fotografias de cobertura anteriores e seus verificadores continuam históricos.

Os 328 arquivos iniciais estavam íntegros. Quinze arquivos recebem integração, com cópias anteriores em `apoio-lote2/historico/`; nove arquivos entram no manifesto, totalizando 337. O [registro de verificação](apoio-lote2/verificacao.json) delimita a conferência. Para a integridade atual, use `CONFERIR-SALVAMENTO.py` na raiz. O conferidor local é somente leitura por padrão; `--salvar` grava exclusivamente seu `resultados.json`.

R53, decisões autorais, fichas de inimigos, Pactos, projetos e resultados anteriores foram preservados. Surpresa/Instinto permanece separado; treinamentos mecânicos e Bestiário integral continuam adiados. Salvamento local, sem envio ao GitHub.

**Próxima tarefa:** L8 — mundo para consulta: sociedade, funções institucionais, diferentes modos de vida, aprofundamentos sinalizados e índice de termos. Usar o acervo e conferir fontes primárias quando necessário, distinguindo obra, R53 e campanha. **GPT-6.1 Sol, esforço alto**, para curadoria e redação; **GPT-6 Astra, esforço alto**, se houver interpretação autoral em disputa. A entrada essencial deve continuar utilizável sem ler revelações da trama.

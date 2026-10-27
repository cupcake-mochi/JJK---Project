# Ensaio guiado do Sineiro

26 de outubro de 2026. Continuação autorizada do registro 73. Entregue a [seção 73 — Retirar a caixa, proteger a equipe](<../06 - Redacao do Guia/73-ensaio-guiado-do-sineiro.md>), com mapa, capacidades usadas, dois percursos de iniciativa e estados finais. **A ficha continua na versão 2 experimental: 108 PV / 54 de Integridade.** Nenhum valor, capacidade ou procedimento de Doma foi aprovado novamente ou alterado nesta etapa.

## Método e limites

O trabalho é um **ensaio escrito com resultados escolhidos**, conferido com a R53 e reproduzido por um programa parcial. Não houve sessão humana, sorteio de combates, avaliação estatística de vitória nem escolha automática de estratégia ótima. Um exemplo resolvido demonstra que aquele percurso cabe nas regras; não demonstra que seja frequente, fácil ou equilibrado.

A referência de regras é a cópia local [LIVRO-COMPLETO-R53.md](apoio-carregador/fontes/LIVRO-COMPLETO-R53.md), conferida contra o arquivo atual de origem. SHA-256: `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

[Estado anterior](apoio-ensaio-sineiro/estado-inicial.json), [reprodução](apoio-ensaio-sineiro/reproduzir.py), [resultados e eventos](apoio-ensaio-sineiro/resultados.json) e [verificação da entrega](apoio-ensaio-sineiro/verificacao.json). O comando `python3 reproduzir.py --salvar` escreve somente resultados.json, sem regenerar o manifesto. Dez arquivos que receberam atualização de continuidade têm cópia em `apoio-ensaio-sineiro/historico-anterior/`.

O programa confere a aritmética dos dados escolhidos, trajetos, ocupação, passagem pela porta, distâncias, recursos declarados, gasto de ações e Reações, término do agarrão por separação e acúmulo de cura. As permissões das capacidades, a interpretação dos estados, a escolha de defesa antes do ataque e os motivos para não executar outras ações recebem **revisão documental**. O programa não implementa todo o sistema nem verifica todas as combinações possíveis de uma ficha.

## O que os percursos acrescentam

| Questão | Primeiro percurso | Segundo percurso |
|---|---|---|
| Objetivo | Retirar a caixa e sair. | O mesmo, resolvendo o socorro antes de encerrar a sequência. |
| Estado inicial | Todos com vida cheia. | Mei com 18/44 PV; demais estados iguais. |
| Primeira interrupção | Empurrão acerta; um passo lateral cancela o sino e separa a presa. | Erra depois de Mei se aproximar; o impacto permanece disponível. |
| Proteção | Rina intercepta uma Pancada e precisa esperar o próprio turno para usar outra abertura. | Rina usa Resguardar para escapar; sua retirada não tira Mei da zona. |
| Gasto ofensivo | Uma espada e dois feitiços de Mei. Akira usa duas aberturas. | Uma espada, uma tentativa de controle e um feitiço com Passo. Akira usa uma abertura e duas curas. |
| Encerramento | Todos fora; Sineiro com 52 PV. | Todos fora; Mei com 18 PV e uma Sequela; Sineiro com 74 PV. |

O percurso principal atende à conferência de **menor uso de feitiços ofensivos** prevista no registro anterior. Usa apenas duas conjurações, em vez das seis declarações ofensivas daquela comparação. Não é uma segunda simulação de combate até a derrota nem representa um grupo incapaz de conjurar. A disponibilidade de controle e movimento faz diferença; não extrapolar o resultado para fichas sem essas capacidades.

| Recursos ao fechar o percurso | Rina | Mei | Akira | Sineiro |
|---|---|---|---|---|
| Principal — PV / PE | 53 / 24 | 44 / 23 | 51 / 28 | 52 / 0 |
| Ferida — PV / PE | 59 / 24 | 18 / 21 | 51 / 17 | 74 / 0 |
| Integridade, nos dois | 50 | 55 | 65 | 54 |
| Sequelas | Nenhuma. | Uma somente no segundo. | Nenhuma. | Não usa o procedimento de jogador. |

O grupo gasta **15 PE** no primeiro percurso e **28 PE** no segundo. A diferença não isola uma causa: o segundo começa com vida menor, usa outros deslocamentos, falha no controle e precisa curar. Não é uma comparação de eficiência entre Insistir e Aguentar.

## Conferência das interações

**Captura.** A manobra substitui um dos dois ataques do Sineiro, exige mão livre e usa CD 13. A condução mantém a presa ao alcance e cobra movimento do chefe. Rina e seus itens somam 7,3 Volume para esse transporte. O Empurrão desloca o agarrador; não ganha transporte gratuito da vítima. Ao passar de 1,5 m, a separação encerra o agarrão. Dano sozinho não o encerra.

**Ações do chefe.** Atacar e impacto disputam a Padrão. Preparar o sino ocupa a Bônus; convertê-la em movimento impediria essa preparação naquele turno. Interrupção perde o preparo, sem repor a ação. Depois de impactar, Guarda Aberta impede Bloquear e outra preparação enquanto durar, mas não suprime os demais recursos. Não foram acrescentados PE, recarga aleatória, imunidade a controle ou ações fora do turno.

**Proteção.** Olhos Em Mim intercepta o ataque rolado declarado contra Mei, não o Agarrar por TR ou o impacto em área. A Reação é paga antes do ataque. Esquivar passa a afetar a rolagem contra Rina; Bloquear é escolhido antes dela e não exige segunda Reação. Alicerce já estava escolhido no descanso anterior. A interceptação e Cobrir-se não reutilizam a mesma Reação.

**Aberturas.** Avançar fora do turno cobra Reação. Depois de interceptar, Rina recebe outra abertura, mas só a usa no turno dela. Esse turno ocorre antes da expiração no começo do turno seguinte de Akira. Resguardar dá vantagem à fuga no segundo percurso; não concede deslocamento nem desfaz Agarrado automaticamente.

**Feitiços.** O Arremesso tem seis pontos, usa um em Empurrão e conserva 5d8. Remodelar troca essa Melhoria por Passo pelo mesmo preço; Classe 2 acrescenta 1 PE, total 7. Impulso Técnico só aparece depois da aplicação alterada paga com Padrão; seu prazo é mantido, sem ação extra. Uma conjuração Projétil não recebe a desvantagem geral de armas de projétil por proximidade nem o crítico físico de Guarda Aberta. Não houve dado 20 escolhido, Aparar ou Brecha a resolver.

**Espaço.** A segunda preparação usa D7:E8, com Mei em D6: a escolha deixa o alvo claramente dentro do raio, sem depender da interpretação de uma célula na borda. As trajetórias de entrada e saída preservam corpos, porta e movimento diagonal. Passo protege seu trecho contra oportunidade; andar voluntariamente depois de escapar de Agarrar, sem outra proteção, continua provocando. O segundo percurso resolve essa oportunidade antes da saída do alcance.

**Socorro.** A primeira escolha de Insistir com máximo 44 e Classe 2 exige 15. Os 10 da primeira cura não levantam Mei; os oito seguintes somam 18 e viram vida por inteiro, com uma Sequela. O prazo perde uma rodada no retorno ao ponto da queda, antes do segundo atendimento. Sair do recinto não reinicia ou suspende esse relógio. Cuidado Preparado exige vida positiva e não substitui a cura; as permissões de níveis 11 e 19 não estão disponíveis.

**Aguentar.** A comparação é delimitada: pede 11, mas deixa Mei Inconsciente e Derrubada em C11. Ela não executaria a própria fuga, e Akira em C0 estaria a 16,5 m, fora de sua cura de 9 m. O material explica que essa escolha exige reposicionamento ou transporte; não atribui ao ramo um resgate completo que não foi desenvolvido.

## Clareza e alterações

Aplicada a orientação local de redação acessível: regra próxima do uso, decisões com nomes e contas, diferença entre consulta de ficha e exemplo comentado. A seção nova não substitui os procedimentos gerais de combate e socorro.

| Antes desta etapa | Agora | O que resolve |
|---|---|---|
| A comparação parava na primeira chegada a zero de vida. | Um percurso acompanha Insistir, duas curas, prazo e Sequela. | Evita tratar zero como morte ou cura pequena como recuperação imediata. |
| Alcance, posição e disponibilidade eram condições dos recortes numéricos. | Percursos anotam coordenadas, trajeto e recursos. | Permite conferir se as respostas cabem no encontro. |
| Sobrevivência a várias conjurações dominava a comparação. | O objetivo é resolvido com espada, controle, proteção e retirada. | Separa concluir a missão de esvaziar os PV do chefe. |
| O texto explicava a economia de ações como orientação geral. | A Reação gasta impede uma saída imediata; a abertura é usada no turno seguinte. | Mostra uma consequência concreta sem inventar penalidade. |

## Encaminhamento

**Manter 108/54 como candidata experimental.** Não há evidência nova para elevar dano, CD ou vida, nem para retirar respostas que funcionaram no exemplo. Tampouco há base para declarar equilíbrio: os dados foram selecionados, o mapa é favorável à retirada e o chefe tem um limite de perseguição conhecido.

O Sineiro já tem função, ficha, sinais, respostas, aquisição separada, comparação numérica e exemplo de condução. A próxima etapa deve avançar o método geral de C04, em vez de prolongar indefinidamente este único protótipo.

**Próxima tarefa recomendada:** montar a primeira régua experimental de criação de inimigos, usando Carregador e Sineiro como referências locais; separar papel, precisão, defesas, reservas, dano e frequência das capacidades, declarando onde faltam comparações. Começar pelas faixas já trabalhadas, sem estender uma fórmula a todos os níveis ou reutilizar o Bestiário antigo. **GPT-6 Astra, esforço extra alto**, para a construção e as contas; **GPT-6.1 Sol, esforço alto**, para o texto de consulta. Treinamentos e atualização integral do Bestiário continuam adiados.

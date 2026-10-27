# Perigos ambientais, exposição e efeitos persistentes

26 de outubro de 2026. Continuação autorizada da integração de C04. Entrega: [procedimento de perigos ambientais](<../06 - Redacao do Guia/78-preparar-perigos-ambientais.md>) e [O pó na sala de conservação](<../06 - Redacao do Guia/79-o-po-na-sala-de-conservacao.md>). O desenvolvimento amplia M017/M129 além da queda e da mudança de acesso, sem declarar uma escala geral de dano ou doenças concluída.

## Resultado e alcance

A seção 78 ensina a definir exposição, escolher a regra e a escala de CD, separar dano/condição/alteração do lugar, fixar frequência, oferecer intervenções e acompanhar efeitos após a retirada. Também orienta a preparação de uma doença fictícia: transmissão, latência, sinais, intervalo, consequências, tratamento e término. Não cria um catálogo de doenças ou concede remoção de sintomas sem a capacidade correspondente.

A seção 79 desenvolve um caso completo sem inimigos: a equipe interrompe a alimentação de um pó material, liga a extração, acompanha duas fases de limpeza e registra a interdição. O caso distingue interromper a fonte, eliminar a nuvem, curar vida, remover Envenenado e encerrar Morrendo.

O cenário e o reagente são criações editoriais para a ocorrência. Não são informação canônica de Jujutsu Kaisen ou descrição de uma substância real. O uso principal continua sendo a guilda; a mesma ocorrência atende campanhas fechadas por meio de um contato do grupo.

## O que veio da R53

Fonte: Livro do Jogador R53 atual, em `/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md`, e cópia preservada em `apoio-carregador/fontes/LIVRO-COMPLETO-R53.md`. Hash de referência: `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

| Fonte dirigida | Aplicação nesta etapa |
|---|---|
| Testes e TRs, linhas 150–251 | Escala fixa 6/10/14/18/22/26, escala do criador, bônus, sucesso e resultados próprios do efeito. |
| Turnos e ações, a partir de 253 | Rodadas de seis segundos, deslocamento, Bônus convertida e Padrão para operar comandos. |
| Concentração, 433–450 | Um teste após cada aplicação de dano enquanto o efeito continuar ativo; CD ambiental preparada; dano zerado e vida temporária. |
| Percepção, 1057–1078 | Nuvem leve prejudica Percepção visual, sem bloquear visão ou conceder cobertura. |
| Dano, 1344–1416 | Resistência, imunidade, redução, arredondamento e separação entre tipo de dano e condição. |
| Condições, 1468–1608 | Saídas de condições Pesadas, Envenenado e ausência de desvantagem automática em Vigor. |
| Vida a zero e socorro, 1665–1785 | Insistir, tratamento acumulado, janela, dano posterior, saída da queda e Sequela. |
| Corpo Amaldiçoado Autônomo, 2827–2829 | Dispensa de respiração e imunidade à condição não equivalem a imunidade ao dano de Veneno ou ao contato material. |
| Corpo Debilitado, 3137–3151 | Exemplo de exposição recorrente já publicada: pele ao sol/luar, 1d4 Radiante e cobertura adequada. |
| Objetos, 8093–8127 | Pino de cerâmica, Defesa 12, pequena peça frágil de 2 PV e efeito de deixar de funcionar. |

Os recortes de Mei e Akira vêm da seção 73. Vigor +3 sem treino de Mei é um complemento explícito para este ensaio; não altera seu TR Físico nem concede uma capacidade adicional de Caminho.

## Escolhas experimentais do caso

| Parâmetro | Proposta preparada |
|---|---|
| Área | Sala 3 × 18 m, faixas A/B e linhas internas 1–12; vestíbulo na linha 0. |
| Exposição | Uma verificação de quem estiver dentro na fase após todos os turnos e efeitos de fim de turno. Travessia sem permanência não recebe outra cobrança. |
| Intensidade | TR de Vigor CD 14; sucesso evita tudo; falha causa 1d6 Veneno e pode aplicar Envenenado. |
| Contato | Material que afeta também corpos construídos; respirar não é requisito. Proteção compatível pode impedir a exposição. |
| Reaplicação | Enquanto a aplicação desta fonte estiver ativa, outra falha causa dano, mas não soma nem renova a condição. É uma escolha própria, em vez de produzir várias aplicações separadas. |
| Prazo | Máximo de dez rodadas, expiração antes da exposição correspondente; TR de saída CD 14 ao fim de cada turno. |
| Limpeza | Alimentação fechada + exaustor ligado por duas fases; exposição antes do avanço, retirada da nuvem depois do segundo. A primeira fase pode ser a da operação. |
| Fonte e intervenção | Pino compatível com impacto de pressão libera uma mola ao quebrar e fecha a alimentação. Essa função é uma propriedade local do dispositivo. |

A escala fixa permite escolher CD 14, mas não aprova automaticamente sua adequação a qualquer grupo. O 1d6 e os prazos são propostas do exemplo, não valores publicados para todo veneno. A autorização de continuidade não foi registrada como aprovação autoral desses parâmetros. Não há nova decisão a acrescentar ao registro 06.

## Percursos e contas

O principal usa dados escolhidos e termina com Mei **44 PV/36 PE/55 Integridade**, sem Envenenado e sem Sequelas; Akira **51 PV/24 PE/65 Integridade**. A máquina permanece interditada. A nuvem termina na fase 2; a condição de Mei termina no fim de seu turno na rodada 3.

O ramo ferido muda apenas a entrada de Mei para 3 PV. A exposição causa 4 e inicia a queda. Insistir pela primeira vez exige **15 de tratamento**, pois ⌈44/3⌉ = 15, abaixo do teto 30 de Classe 2. O deslocamento de retirada continua disponível. Sutura de 15 encerra Morrendo antes da fase seguinte, com 15 PV e uma Sequela. O TR de saída de Envenenado é resolvido separadamente, antes da ação de Akira.

Se a pessoa permanecer dentro, a volta ao ponto da queda pode consumir uma rodada da janela e o dano posterior positivo, outra: **3 → 2 → 1**. O perigo não transforma a janela em rodadas garantidas de combate nem concede socorro retroativo após o prazo.

O apoio `apoio-perigos-recorrentes` guarda `calcular.py` e `resultados.json`. O programa confere aritmética e cronologia e enumera o dano de um a três testes de exposição, com Vigor +3 contra CD 14, sem proteção ou cura entre eles. As médias por uma, duas e três exposições são **1,75; 3,5; 5,25**. São aplicações condicionadas à permanência, não rodadas de missão ou chances de vitória. Não se incluiu estratégia, decisão humana ou motor completo de capacidades.

`--salvar` grava apenas o resultado do próprio apoio; não reconstitui o manifesto. Para a integridade do projeto, usar `CONFERIR-SALVAMENTO.py`.

## Revisão independente e ajustes

Uma revisão independente, somente de leitura, conferiu a proposta com os trechos da R53. Não se tratou de leitor de teste ou sessão humana.

| Antes da revisão final | Ajuste incorporado |
|---|---|
| Dez rodadas tinham ponto de expiração, mas a ordem frente à nova exposição podia gerar dúvida. | Expirar a aplicação antes da verificação daquela fase; nova falha pode reaplicar. |
| O ramo de queda preservava Envenenado depois da cura sem repetir seu teste de saída. | Declarado o TR 9 + 3 = 12 ao fim de Mei 2, antes da Sutura de Akira. |
| Uma limpeza por duas fases poderia ser entendida como duas rodadas completas adicionais. | Mostrada a contagem na rodada da operação e na seguinte; exposição antes de cada avanço. |

## Preservação e cobertura

Os 293 arquivos do manifesto anterior estavam íntegros na abertura. O estado anterior e as cópias dos 11 arquivos atualizados estão em `apoio-perigos-recorrentes`. Fichas, Domas, ensaios e cálculos anteriores foram preservados. O acervo da pesquisa paralela não foi editado.

M017/M129 recebem procedimento geral e um exemplo de exposição recorrente, imunidades, condição persistente e socorro. Permanecem abertos o catálogo e os exemplos específicos de outros perigos, incluindo doença com desenvolvimento prolongado, e eventual referência numérica geral. M124 continua parcial quanto a outros níveis, perfis, chefes e dificuldade. A cobertura da matriz não foi promovida a completa.

O índice, o plano, a pauta e a retomada apontam os dois novos textos. A conferência final verifica remissões locais novas/alteradas, matriz dos 130 identificadores, R53, arquivos preservados e resultados copiados. Não houve teste humano ou validação de dificuldade. O salvamento desta etapa é local.

## Próxima tarefa recomendada

Consolidar as ferramentas de C10: inventariar as folhas existentes, organizar sua escolha por situação, conectar preparação, condução, fechamento e passagem entre mestres e montar um exemplo de entrega de missão. Não duplicar os formulários que já cumprem sua função. Em seguida, auditar as lacunas do manuscrito como conjunto, incluindo o restante de C04.

**GPT-6.1 Sol, esforço alto**, para a consolidação e a clareza. **GPT-6 Astra, esforço extra alto**, para a auditoria posterior dos 130 pontos e das interações mecânicas. Bestiário integral e mecânica de treinamentos continuam adiados.

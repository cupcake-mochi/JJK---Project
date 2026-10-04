# Integração ao livro — v0.331

Data: 02/10/2026. Pedido autorizado: implementar Evocador, Incursor, Invocações e os cinco ajustes do Bastião; guardar a revisão ampla de nomes e outras pequenas mudanças na fila.

## O que entrou

- Seis Caminhos e dezoito Trilhas no capítulo 8. Evocador: Invocação Principal, Parceria e Múltiplas Invocações. Incursor: Assassino, Pugilista e Malabarista.
- Invocações no capítulo 17, com os catálogos comuns do Fundamento e as tabelas reduzidas aprovadas; perícias treinadas iguais a 4 + metade da Inteligência da entidade, arredondada para baixo, e ofícios por permissão expressa.
- Bastião: reação antes da rolagem para assumir o ataque, com Defesa/Bloquear próprios; Duro de Matar sem limite por rodada; Nem Um Arranhão passivo; Arrastão com custo variável; Mão Pesada com escolha de agarrar ou derrubar; Contra a Parede no primeiro ou segundo ataque, sem crítico do feitiço e sem Canalizar em Golpe no ataque escolhido.
- Casca Grossa, Trocação Franca e Retaliação agora dependem de o ataque assumido realmente acertar. A redução de Casca Grossa não concede outro Bloquear. Mão Pesada explicita alcance, mão livre e CD 8 + Força + maestria; a alteração resolve a omissão do texto anterior sem exigir Atletismo.
- Índice, criação, glossário, referências dos capítulos, fontes mecânicas e catálogo do gerador local atualizados. As fichas em trabalho no outro ambiente não foram editadas.

## Fontes e limites

As habilidades novas foram comparadas integralmente com os textos aprovados. As adaptações são hierarquia de títulos, quadro de características compatível com o livro, referência ao capítulo 17, nome Malabarista e espaçamento de três listas do Incursor para que os itens não saiam como texto corrido. As referências aprovadas têm hash e estão preservadas. A coleção v0.4 e seu manifesto não foram modificados; a edição atual está em caminhos/05-Edicao-Integrada/.

Os validadores de Invocações e do catálogo conservam as verificações históricas e as identificam como históricas. A verificação da edição atual confere suas fontes, fidelidade integral, calendário, treinamentos, contratos do Bastião e custos de Arrastão. Não se usa a matemática antiga de Servo/Matilha/Coro para afirmar que as Trilhas atuais estão equilibradas.

A média de inimigos conserva os quatro Caminhos de referência publicados na v0.330. Disponibilizar seis Caminhos não recalibra automaticamente o bestiário. Rever a média é trabalho futuro registrado na fila.

## Cenários conferidos

| Situação | Resolução da edição integrada |
|---|---|
| Aliado é alvo de um ataque | Bastião decide antes do d20; gasta sua Reação; rolagem normal compara com sua Defesa ou seu Bloquear |
| Bastião bloqueia ataque assumido e falha | Duro de Matar pode reduzir; se Muro 19, Casca Grossa também se aplica ao acerto |
| Bastião sofre vários ataques e bloqueia mal | Duro de Matar pode ser usado em cada falha; assumir ataques ainda depende de sua única Reação disponível |
| Ataque pede TR Físico e atacante está na área | Nem Um Arranhão concede vantagem, sem gastar Reação; fora da área não concede |
| Arrastão ampliado tenta 1 / 2 / 3 / 5 / 6 alvos | 0 / 2 / 4 / 8 / 10 PE; errar não devolve o custo |
| Mão Pesada empurra para fora do alcance | Não mantém o alvo Agarrado; Derrubado continua sendo uma escolha válida |
| Contra a Parede acompanha o segundo ataque | O feitiço resolve após esse ataque, paga PE normal e não crita; esse ataque não usa Canalizar em Golpe |

## Testes negativos

Dezessete perturbações deliberadas em cópia isolada foram detectadas. Incluem alteração somente no livro e alteração simultânea de fonte e cópia, custo de Arrastão, limite de Duro de Matar, momento de Assumir, reação de Nem Um Arranhão, opção de agarrar, Canalizar em Contra a Parede, alcance do Evocador, acúmulo de Fluidez, nome Malabarista, teto de entidades, treino, CD, tabelas de consulta, calendário e presença dos Caminhos nas frases de treino do capítulo de equipamentos. A base isolada passa antes das perturbações. Evidência em perturbacoes.json.

## O que continua na fila

Revisão textual integral, revisão ampla de nomes e outras mudanças pequenas, capítulo piloto de diagramação e arte, conciliação de Origens e fichas, definições pendentes de invocações e playtests de economia/ritmo. As notas recebidas foram preservadas nesta pasta como histórico. A fila atual no ESTADO-ATUAL.md prevalece sobre a indicação antiga de que o pacote ainda não havia sido integrado.

As pendências de kit inicial, troca de Trilha, repertório após alteração permanente de atributo, corpos excedentes e procedimentos gerais de ações não receberam regras inventadas. As regras específicas já aprovadas continuam disponíveis.

## Exportação e regressão

Os 30 validadores passam, sem verificação pulada. O catálogo local de fichas também passou na conferência de sintaxe. O verificador de voz encontra 117 termos recorrentes com destino definido e nenhuma referência a título ausente; seus achados editoriais permitidos permanecem para a revisão textual.

O Word de revisão foi renderizado em 358 páginas. Houve inspeção geral das páginas em folhas de contato e inspeção em tamanho original dos trechos alterados de Bastião, Evocador, Incursor, Malabarista, equipamentos e Invocações. A última correção de listas afetou visualmente apenas as páginas 164 a 167, comparadas por hash de imagem; as quatro foram inspecionadas novamente. Esta conferência verifica a integração, não substitui a futura revisão editorial e de diagramação de todo o livro.

Os arquivos finais têm 380 páginas no PDF de uma coluna, 240 no PDF de duas colunas e 358 no Word de revisão. O texto de consulta também foi atualizado. A paginação do PDF de uma coluna estabilizou na sétima passagem, preservando as verificações de títulos e tabelas; as duas exceções de paginação já existentes continuam identificadas pelo construtor para a futura revisão de diagramação.

O PDF de duas colunas teve inspeção geral das 90 páginas afetadas pela última mudança de paginação em folhas de contato, além de inspeção em tamanho original dos trechos críticos desta integração. No PDF de uma coluna, foram inspecionadas em tamanho original treze páginas de Bastião, Evocador, Incursor, equipamentos e Invocações. Não houve corte ou sobreposição nos trechos conferidos. Esta amostragem não equivale à inspeção individual de todas as páginas em tamanho original.

A entrega em finalizado foi sincronizada com as fontes e os arquivos finais. O pacote v0.331 reúne o livro, as fontes, as notas, a fila e as evidências de validação; seu manifesto permite conferir a integridade dos arquivos. A revisão textual e artística integral ainda não foi executada nesta integração.

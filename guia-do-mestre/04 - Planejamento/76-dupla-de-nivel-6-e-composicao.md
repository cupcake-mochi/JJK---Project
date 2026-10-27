# Atacante, apoio e composição de nível 6

26 de outubro de 2026. Continuação autorizada da primeira régua. Entregues [Ren e Sora — fichas](<../06 - Redacao do Guia/75-ren-e-sora-atacante-e-apoio.md>) e [Escolher quem enfrentar primeiro — confronto](<../06 - Redacao do Guia/76-confronto-de-ren-e-sora.md>). São dois inimigos humanos com funções diferentes, um percurso conjunto e comparações condicionais de pressão e prioridade de alvo. **Não foi atribuída dificuldade nem aprovação autoral dos números.**

## A construção proposta

Ren usa a reserva central de nível6 da régua:72PV/36 de Integridade, Defesa13 e ataque+5. Sora usa a menor:48/24, Defesa13, com apoio automático e pouca ofensiva física. Cada um tem sua iniciativa e uma aplicação na Padrão. Não há ataque extra de chefe, bônus ofensivo gratuito ou turno compartilhado.

As reservas próprias **8PE para Ren e12PE para Sora** são propostas editoriais de inimigos. Não são derivadas de Caminho de jogador, e a ficha não recebe capacidades de Caminho/Trilha por ser humana. A separação está declarada no texto. Atributos, ataque, Defesa/Bloquear, TRs, Refino, manobras, carga, feitiços e capacidades usadas conservam seus procedimentos da R53. Não é uma proposta de reduzir os PE dos personagens jogadores.

Escolher humanos amplia a variedade do Guia e evita tratar todo inimigo como maldição adquirível. Não se aplica Doma às duas fichas. A derrota preparada é incapacitação; as fichas de inimigos não recebem Insistir ou Socorro de jogador. Não há transformação dessas fichas em personagens jogadores sem reconstrução pela criação correspondente.

Carregador, Sineiro, Amontoado e suas conversões permanecem intactos.

## Montagens conferidas

| Capacidade | Conta | Resultado e custo |
|---|---|---|
| Espada de Ren | Espada Longa em uma mão, Força4, Maestria1, Canalizar com Refino2. | +5;1d8+4+1d4, crítico2d8+4+1d4; Padrão, sem PE. |
| Fenda em marcha | Classe1:3 pontos − Passo1. | 2d8, Projétil18m, ataque+5; Padrão/3PE; Passo até6m antes ou depois. |
| Fio de impulso | Classe1:3 − base Leve de vida temporária1 − Impulso1. | Impulso e3 temporários; benefício individual9m, Padrão/3PE. |
| Remendo | Classe2:6 − base Média de cura2. | 4d8, dentro do teto individual;9m, Padrão/6PE. |
| Cobrir-se | Refino2 ×1,5 =3 de redução. | Reação e2PE, mantendo proteção do Traje. |

**Correção durante a montagem:** Impulso pertence a Auxiliares, e sua aplicação individual não cobra base Média. A base de Fio é Leve porque a aplicação também concede vida temporária individual. Amparo Livre e Auxiliares Livre foram registradas em Sora; a base não recebe desconto. A ficha oferece três temporários, não cura ou uma segunda reserva cumulativa.

Passo não depende de acerto, não transporta o parceiro e não liberta Agarrado. Fio não exige Concentração ou manutenção; portanto, derrota da fonte impede novas conjurações, mas não cancela automaticamente um benefício já concedido. Remendo não restaura Integridade ou PE e não reabre a participação de um inimigo Derrotado por uma permissão que a montagem não possui.

Impulso, Executar e a provocação comum podem gerar situações de vantagem, mas vantagens não se empilham. A abertura de Executar é usada antes de expirar no começo do turno seguinte de Akira. Avançar não é usado fora do turno por Rina depois de ela gastar a Reação em interceptar; ela espera o próprio turno.

## Pressão e prioridade de alvo

[Cálculo reproduzível](apoio-dupla-n6/calcular.py) e [resultados](apoio-dupla-n6/resultados.json). As distribuições de dados e ataque reutilizam o apoio da etapa73, sem modificá-lo. Não há IA, sorteios de combate, taxa de vitória ou reprodução de todas as capacidades das fichas.

**Uma espada de Ren, contra Defesa13:**65% de acerto sem vantagem ou87,75% com Impulso. Média por declaração7,39 ou10,12, incluindo o primeiro teste possível de Kokusen, com limite4 e bônus acumulado0. Contra Alicerce/Cortante,3,86 ou5,28. O cálculo aplica a resistência antes do acréscimo de Kokusen, conforme a R53. Não inclui Bloquear ou outra redução.

O Kokusen corresponde a0,20% ou0,39% dessas declarações. As médias não presumem que todo turno conserva esse limite: uma falha anterior no d100 o aumenta. No percurso escrito não há crítico; o contador permanece zero. Nenhum teste obrigatório foi omitido de um ataque20 escolhido.

**Duas conjurações restantes na rodada1:** o ponto de comparação começa após Ren agir, com Ren67PV/6PE e Sora48PV/9PE. Mei usa5d8, Akira6d8, ambos+5 contra Defesa13. O alvo tem uma Reação disponível, pode pagar2PE e usa Cobrir-se no primeiro dano positivo. Como o menor acerto produz pelo menos5 ou6, a redução de3 pode ser descontada da soma dessas duas aplicações neste recorte específico. Não há vida temporária restante em Ren nesse ponto.

| Foco | Derrotado antes de Sora2 | Alvo sobrevive até metade da máxima; Sora escolhe curar | Alvo sobrevive acima da metade; Sora escolhe Fio |
|---|---:|---:|---:|
| Sora | 23,9% | 37,7% | 38,4% |
| Ren | 4,5% | 43,4% | 52,0% |

As três colunas de cada linha partilham o mesmo denominador e somam100% antes do arredondamento. A política depende de alvo ativo, alcance, Selo e recursos. A cura é sobre o alvo atacado; Fio vai para Ren. Se Ren cair, Sora procura retirada, sem conceder benefício a um parceiro Derrotado. Se o primeiro feitiço já derrotar o alvo, a segunda ação pode mudar de destino; isso não altera o evento de o alvo escolhido já ter sido derrotado.

Na alternativa de foco em Sora, se ela usar Cobrir-se e depois Remendo, terá1PE: perde acesso a outro Fio e à própria redução. No foco em Ren, é ele quem paga a redução; Sora conserva9PE antes da escolha. Curar Ren por6 deixa3, ainda suficientes para um Fio posterior. Assim, atacar o apoio pode afetar o orçamento mesmo sem derrubá-lo. Isso não prova que seja sempre a prioridade correta.

O texto não transforma o reforço em dano gratuito: Sora investe uma Padrão e3PE para melhorar uma tentativa e oferecer3 temporários. Curar ocupa essa Padrão. Quando Ren já possui vantagem, Impulso não amplia o acerto; a decisão deve considerar os temporários ou outra ação. A combinação foi mantida simples para testar duas iniciativas e um apoio, sem acrescentar controle duro, áreas ou múltiplos ataques.

## Percurso conjunto

[Reprodução parcial](apoio-dupla-n6/reproduzir.py) e [registro de eventos](apoio-dupla-n6/resultados-ensaio.json). A seção76 fixa dados e acompanha três rodadas até a perda da função de apoio, retirada escolhida do atacante e obtenção do estojo. Coordenadas, trajetos, ações, PE, Reações, cura e reservas foram conferidos. A permissão das capacidades, a decisão de não perseguir e as interpretações de estado recebem revisão documental.

Estado final: **Rina52PV/24PE**, **Mei44/24**, **Akira51/16**, sem quedas ou Sequelas; **Ren46/1**, fora do recinto; **Sora0/1**, incapacitada. Integridade preservada em todos. O grupo gastou26PE e a dupla18. Akira recolhe o estojo do espaço adjacente, sem ocupar o corpo de Sora. A saída com documentos, atendimento e eventual transporte posterior não foram concedidos como ações gratuitas.

O resultado favorece uma formação capaz de proteger a equipe: Rina tem resistência prévia aos dois tipos usados por Ren e consegue interceptar dentro de6m; Mei desloca a fonte de apoio; Akira tem alcance para completar o foco. Não extrapolar esse resultado para um grupo sem essas respostas. O erro de Akira na primeira rodada e os demais dados foram escolhidos para mostrar decisões, não para representar a frequência calculada do encontro inteiro.

**A retirada de Ren não encerra compulsoriamente a iniciativa.** Mei e Akira ainda podem agir e, no exemplo, decidem não perseguir. Desengajar protege o movimento do turno; a porta não o protege de disparos posteriores. A outra decisão exigiria continuar a sequência.

## Fonte e verificação

R53 atual conferida contra a [cópia preservada](apoio-carregador/fontes/LIVRO-COMPLETO-R53.md), SHA-256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`. Leitura dirigida: ataque/alcance, vantagem e crítico, manobras, Defesa/Bloquear, ações/reações, movimento/corpos/carga, reservas temporárias, derrota, Integridade, progressão, Fundamento/mesclas/alcance, Impulso/Auxiliares, Passo/Alcance, Amparo, Canalizar, Cobrir-se e Kokusen; Olhos Em Mim/Alicerce e aberturas do Guia. Não foi necessária nova referência externa para montar essas aplicações.

[Estado inicial](apoio-dupla-n6/estado-inicial.json), nove cópias históricas em `apoio-dupla-n6/historico-anterior/` e [verificação da entrega](apoio-dupla-n6/verificacao.json). Os dois programas só escrevem seus respectivos resultados com `--salvar`; não reconstroem o manifesto. Nenhum salvamento remoto foi feito nesta etapa.

## Alcance da entrega e próximo passo

Há agora dois rascunhos de inimigos completos para a ocorrência, com funções, reservas próprias, montagem de capacidades, rotina de decisão, estados e uma composição conferida. Não são personagens jogadores completos. As propostas de8/12PE, as vidas, a política de alvo/cura e o desfecho de incapacitação são editoriais. As regras das peças existentes permanecem identificadas; nenhum “pode seguir” foi registrado como aprovação dos novos parâmetros.

C04/M124 continua parcial. Ainda faltam outras quantidades de participantes, famílias de defesa, níveis intermediários/altos, áreas sobre vários alvos, dano de Alma com acesso válido e uma escala de dificuldade sustentada. Não há razão nesta etapa para alterar Carregador ou Sineiro, multiplicar o dano para garantir quedas ou impor PE a todos os inimigos.

**Próxima tarefa recomendada:** fazer uma revisão integrada do método de criação e avaliação nas seções56–76, separar regras da R53 de propostas, eliminar repetição e preparar uma ficha única de construção preenchida com Ren/Sora e remissões aos exemplos. A finalidade é transformar os estudos acumulados em um percurso de consulta utilizável antes de expandir os níveis. **GPT-6.1 Sol, esforço alto**, para organização e clareza; **GPT-6 Astra, esforço extra alto**, para divergências mecânicas que a revisão revelar. Bestiário integral e treinamentos continuam adiados.

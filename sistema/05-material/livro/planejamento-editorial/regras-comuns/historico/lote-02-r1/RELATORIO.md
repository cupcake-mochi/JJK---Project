# Revisão do lote 2: saltos, apoios e quedas

**02/10/2026. Candidato sobre a v0.331, sem integração ao livro jogável.**

## Entrega e alcance

A [amostra de sete páginas](output/pdf/Projeto-M-Movimento-Saltos-e-Quedas-Proposta-02.pdf) reúne saltos horizontais e verticais, chegada a bordas, falhas, descidas apoiadas, dano e controle de queda, empurrões e compatibilidade com Movimento Acrobático. Inclui três percursos resolvidos, sete marcadores de consulta e um esquema vetorial. Preserva a paleta. Nenhuma imagem gerada por IA foi usada.

O [registro M07–M22](02-DECISOES.md) identifica os números novos e as interpretações que afetam habilidades. Não são correções apenas de estilo. Custo de salto, resultado de falha, dano por altura, controle de queda, restrição a destinos no ar, limite acrobático por ciclo e momento de medir Recuperar a Base precisam ser avaliados antes de integrar.

## Como o texto foi examinado

Três agentes trabalharam em frentes distintas: interações com habilidades, referências primárias e escala matemática. Depois da minuta, dois deles fizeram leituras críticas separadas, uma de regras e outra editorial. Os pareceres estão em `evidencias/`; descrevem o texto anterior às correções finais. Não são testes com jogadores nem garantias de compreensão humana.

A pesquisa retoma D&D 2024, Pathfinder Player Core e Cairn e aprofunda bordas, quedas e movimento forçado. A comparação matemática examinou três perfis: 1d6 por 3 m, 1d6 por 1,5 m e 3 pontos por 1,5 m. O terceiro foi adotado para esta primeira amostra. Os limites e as hipóteses estão documentados, incluindo diferenças entre a sonda inicial e as tabelas finais de salto. Os números propostos não são atribuídos ao cânone de Jujutsu Kaisen.

O autor deste lote aplicou as correções, conferiu as contas da versão entregue e inspecionou visualmente as sete páginas renderizadas. Não houve nova leitura integral dos agentes após a última correção.

## Achados tratados

| Achado | Correção aplicada |
|---|---|
| A falha dizia “no máximo”, permitindo escolher a própria posição depois da rolagem | Distância final passa a ser a menor entre o declarado e o salto curto; obstáculo sólido ainda pode interromper. |
| A ordem de resolução parecia guardar uma resposta imediata durante uma queda de vários turnos | Resolver primeiro o trecho imediato; a janela de resposta termina ali, sem ser transferida ao impacto futuro. |
| Redução do deslocamento proibia apenas iniciar um novo trecho acrobático | O trecho atual também termina quando o limite recalculado já estiver consumido. |
| Derrubado podia diminuir retroativamente o gatilho de Recuperar a Base | Medir o limiar antes do efeito que empurrou; o retorno continua usando as condições atuais. |
| Subir de uma borda ignorava terreno difícil | A subida conta como 1,5 m de escalada, com os quatro custos explicitados. |
| A renovação do limite só estava definida em combate | Fora de combate, usar percurso contínuo entre apoios permitidos; cenas com controle de tempo usam turnos. |
| O exemplo de nível 11 mencionava Passo Guardado, recebido no nível 15 | Retirada a referência do exemplo; conservado o caso de Recuperar a Base. |
| Uma remissão usava linguagem de bastidor no procedimento do jogador | Nomeada a regra de movimento/terreno a consultar. A integração futura deve transformar a referência em link definitivo. |

Além dos pareceres, a redação final explicitou consciência e ausência de Agarrado/Impedido como requisitos do controle de queda. Isso é uma escolha nova, registrada como M15, e não uma afirmação de que as condições já tenham esse efeito no livro atual.

## Conferência final

[CONFERENCIA.json](CONFERENCIA.json) registra os resultados da última execução: valores da tabela de queda, fronteiras de altura, percentuais de testes, contas dos exemplos, preservação das fontes, texto presente em cada página, marcadores, limites da área impressa e links locais deste lote. As sondas de distribuição estão preservadas e podem ser executadas sem depender dos caminhos temporários de trabalho.

Na inspeção visual, as sete páginas ficaram legíveis, sem cortes encontrados, cabeçalhos soltos ou tabelas atravessando páginas. O esquema do Assassino distingue parede, salto e movimento restante. O texto extraído foi cotejado com a fonte para detectar omissão no PDF; esse teste não substitui a inspeção visual.

A comparação de integridade abrange as 22 fontes e os cinco artefatos publicados do inventário, além do retrato de 137 arquivos de mecânica, edições integradas e pilotos. As contagens se sobrepõem; não são conjuntos a somar. O resultado exato consta da conferência. Não foram usados comandos Git.

## O que ainda precisa ser avaliado

Dano fixo facilita a consulta, mas cria degraus nas alturas e pode ser severo em quedas repetidas. O limite acrobático por ciclo restringe travessias fora do próprio turno depois de consumido. A restrição vertical muda uma leitura permissiva de empurrões e projeções. Esses efeitos estão expostos como decisões, sem declaração de equilíbrio comprovado.

A amostra não encerra afogamento, cargas, voo, objetos em queda nem todas as combinações de condições. Também não substitui o teste humano planejado. Antes da publicação, é preciso escolher as propostas, conciliá-las com o primeiro lote e atualizar as remissões das Trilhas.

**Continuação da fila:** percepção, esconder e detectar. A abertura conserva o retorno do usuário para uma rodada própria; nomes e pequenas alterações de classes seguem na pauta.

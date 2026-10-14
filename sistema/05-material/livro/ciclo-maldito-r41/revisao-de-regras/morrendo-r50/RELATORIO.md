# R50 — integração de Morrendo e revisão do livro

Entrega sobre uma cópia da R49, com **397 páginas**. A candidata aprovada v0.17 foi incorporada ao livro, incluindo as decisões finais sobre Sequelas, teto de Insistir e ordem de recuperação no descanso longo. Não foi feita uma nova rodada de balanceamento.

## Entrega

- [PDF final](../output/pdf/Ciclo-Maldito-R50.pdf).
- [Texto integral gerado](../LIVRO-COMPLETO.md).
- [29 alterações de texto, com antes e depois completos](../ALTERACOES-R49-para-R50.json).
- [Registro de geração e composição](../ALTERACOES-COMPOSICAO-R49-para-R50.json).
- [25 frentes de interação conferidas](INTERACOES.md).
- [Escopo e resultados da revisão textual](REVISAO-TEXTUAL.md).
- [Cobertura visual das 397 páginas](REVISAO-VISUAL-PAGINAS.json).

## Mecânica integrada

Morrendo é uma condição própria. Aguentar exige 1/4 da vida máxima de referência, arredondado para cima e sem teto. Insistir exige 1/3 na primeira escolha da cena e 1/2 nas seguintes, com teto direto de 15 × a maior Classe. Escolher Insistir não gasta Ação Padrão, vida máxima nem uma rodada imediata; conservar a ação permite autocura conforme a fonte usada.

A vida permanece em zero enquanto o tratamento se acumula. Ao completar o requisito, todo o tratamento vira vida, limitado ao máximo atual. Tempo e dano posterior reduzem a janela de socorro, sem apagar tratamento nem aumentar o requisito. Estabilizar suspende o tempo, sem curar. Uma nova ocorrência de dano encerra a estabilidade e consome uma rodada.

A janela usa as Sequelas que já existiam: três, duas ou uma rodada; com três Sequelas, a próxima queda causa derrota imediata. Sair da queda deixa uma Sequela. No descanso longo, primeiro resolve-se a recuperação e registra-se a Sequela da saída; depois removem-se todas, inclusive essa. Cura depois de Derrotado não devolve a participação na mesma cena.

Levanta e Ainda Há Tempo conservam suas permissões expressas de resgate. Limpa Fundo não encerra Morrendo. Segundo Fôlego troca o requisito de Insistir por 1/4 naquela queda, uma vez por descanso longo. Recomposição recupera 3 × a maior Classe, conservando Ação Padrão e uma vez por descanso curto. Invocações, Integridade, concentração e domínios conservam suas regras próprias.

## Exemplos e ajustes de compreensão

Foram refeitos os exemplos de dano posterior, de socorro da Mei com 23 PV, do Insistir com máximo 93/Classe 3 e da próxima queda após uma Sequela. Foi acrescentado o exemplo do teto com máximo 395/Classe 7: 99 para Aguentar; 105 para ambos os requisitos de Insistir. Os demais exemplos numéricos preservados não foram reequilibrados.

A revisão também incorporou pendências anteriores autorizadas que ainda estavam fora da R49: polimento dos Legados de história, suas remissões nas Origens e Pactos, a concessão específica de Categoria de Efeito 4 e a definição aprovada de visão noturna do Olho adicional. O rascunho sobre a R46 foi aplicado apenas nas passagens correspondentes, preservando as mudanças posteriores, incluindo Ataque sem Prenúncio.

Negativas ambíguas foram esclarecidas em Socorro, Regeneração Orgânica e Amparo Interior. Cura e vida temporária passaram a remeter explicitamente ao tratamento de Morrendo. Cada diferença textual está no registro; são **29 blocos alterados e 482 preservados**, num total de 511.

## Revisão visual

Houve duas passagens integrais por painéis sequenciais, cobrindo as 397 páginas, e inspeções individuais ampliadas nas páginas novas e nos pontos de risco. Foram produzidas quatro composições durante a revisão. As páginas 52–59, 78, 83–85, 134, 279–280, 285 e 307 foram abertas individualmente na composição final.

O fechamento começou na segunda composição para as páginas 1–80 e prosseguiu na terceira para 81–397. A comparação dos PNGs com o PDF final confirmou identidade nas páginas não recompostas. As diferenças finais foram a página 55, pelo subtítulo, e as páginas 84–85, pela lista reunida; todas foram inspecionadas novamente em ampliação. Essa cobertura e os hashes estão registrados por página. O nome “final” em algumas legendas de painéis intermediários corresponde ao nome da pasta no momento da renderização; o registro distingue as composições pelo arquivo e pelo hash.

Correções feitas:

1. **Aguentar:** a primeira composição deixava apenas o começo na página 53. A entrada curta agora fica inteira na página 54.
2. **Resgates expressos:** o novo subtópico recebeu o mesmo tratamento visual de Estabilizar. A classificação foi aplicada depois da revisão que a reconstruía, para sobreviver a uma nova geração.
3. **Locomoção Adaptada:** a lista deixava uma opção após a tabela e as outras na página seguinte. As três opções agora ficam juntas na página 84.

Foram reconferidas as correções anteriores de Leitura a Dois, das famílias de Melhorias e das apresentações de Trilhas. A leitura mantém a coluna esquerda antes da direita. Elementos largos são tratados como faixas próprias; tabelas longas conservam o cabeçalho quando continuam. Não foram vistos títulos sem o primeiro conteúdo, texto cortado ou elementos sobrepostos na passagem final. A triagem geométrica adicional examinou 1.482 títulos H1–H3 e não apontou separação entre título e primeiro conteúdo.

## Aproveitamento e branco remanescente

A quantidade de páginas permanece igual à R49. Pela medição aproximada do branco abaixo do último elemento de cada coluna, a R49 tinha 55,65 páginas equivalentes; a R50 tem 54,52. Em páginas de meio de capítulo, o valor passou de 44,66 para 43,59. Essa medida não inclui todo o branco do livro, margens ou entrelinhas e não deve ser confundida com páginas que poderiam simplesmente ser eliminadas.

Ainda há mais de um terço dessa área vazio nas páginas **7, 9, 77, 81, 83, 84, 85, 111, 137, 143, 163, 175, 180, 188, 206, 210, 219, 223, 309, 326 e 338**. O aproveitamento não é uniforme:

- 7 e 9 pertencem às apresentações iniciais; 81, 85, 223 e 309 antecedem aberturas de seção com tratamento próprio.
- 77 preserva Leitura a Dois inteira na 78; 83 antecede a tabela larga de Armamento Orgânico; 84 preserva a lista curta de Locomoção inteira após essa tabela.
- 143 e 163 antecedem apresentações de Trilha com introdução e progressão; 210 antecede as tabelas largas de armas.
- 111, 137, 175, 180, 188 e 206 conservam a composição vigente de procedimentos/habilidades e seus primeiros conteúdos. Não se comprimiram fontes ou espaçamentos para preencher o rodapé.
- 219, 326 e 338 terminam conjuntos de explicações antes das próximas seções. Não foram classificados como interrupções de leitura na inspeção, embora conservem espaço aproveitável numa eventual rodada específica de compactação.

As medições detalhadas estão em [METRICAS-final.json](METRICAS-final.json). Não se afirma que esta é a compactação máxima possível; a prioridade foi a sequência de leitura e a integridade dos assuntos.

## Validação e limites

- **118.348 verificações automáticas**, sem problemas no PDF final: presença do conteúdo, margens, sobreposições, glifos, imagens, remissões e extração real.
- **2.541 links internos e 192 marcadores** conferidos.
- **81 verificações de integração** aprovadas; o registro reconstrói exatamente os 511 blocos usados pelo gerador.
- **16 cenários determinísticos** do estudo reexecutados, além da conferência dos exemplos 23/93/395 PV. As simulações extensas anteriores foram preservadas e não são apresentadas como um novo teste.
- **4.098 arquivos da R49** conferidos contra o inventário anterior, sem alteração.
- Capa, artes, créditos, famílias tipográficas e tamanhos de letra preservados. Nenhum commit ou push.

A revisão textual combinou varredura do livro inteiro por termos/remissões e leitura dirigida das partes novas, recentes e relacionadas. Ela não equivale a reler palavra por palavra todos os capítulos antigos. A revisão de interações foi feita por leitura cruzada e cenários definidos; não há um motor completo de todas as capacidades nem um teste com jogadores nesta rodada. Nenhuma nova decisão de regra ficou pendente.

PDF validado: `c0be8892248e80bc97720502317e1f2745ae194b0e2704923f00d93151d308e4`.

# Fundamento — candidata do lote 01

Este lote desenvolve **R06: Fundamento e criação/uso de feitiços**, com interfaces necessárias à revisão de Técnica Máxima. É material de revisão: não substitui o livro publicado nem encerra o catálogo R07 ou os poderes avançados R08.

## Arquivos

- [FUNDAMENTO.md](FUNDAMENTO.md): texto destinado ao jogador, com criação guiada, exemplos, consulta de procedimentos e ficha.
- [PDF da proposta](output/pdf/Projeto-M-Fundamento-Proposta-01.pdf): versão diagramada gerada do manuscrito. Quantidade de páginas, estrutura e estado da conferência: consultar `evidencias` e os resultados do conferidor.
- [ALTERACOES.md](ALTERACOES.md): registro de 56 decisões com antes, candidata, motivo e destinos; 28 delas identificadas como mecânicas ou fechamento de lacuna.
- [REVISAO-E-FONTES.md](REVISAO-E-FONTES.md): decisões, motivos, fontes consultadas, alcance das validações e pendências.
- [MATRIZ-AUDITADA.json](MATRIZ-AUDITADA.json): combinações examinadas e respectivas recomendações. Recomendações ainda dependentes de R07 não são permissões publicadas.
- [sincronizacoes](sincronizacoes): substituições candidatas para Técnica Marcial, Sem Técnica, Invocações e Progressão, com trechos anteriores, trechos propostos e motivos.
- [evidencias](evidencias): auditorias de compatibilidade, rotas, didática, Técnica Máxima, modelos numéricos e conferências. As auditorias de trabalho conservam os achados da versão examinada; o manuscrito e a validação vinculada ao seu hash identificam a versão atual.

## O que foi trabalhado

A redação separa **espaços conhecidos**, **pontos de montagem** e **PE por uso**. O primeiro feitiço aparece cedo, com ideia, conta, ficha e resolução. Outros exemplos mostram movimento, controle, apoio e efeitos fora de combate.

A troca de um espaço por entidade aparece no Fundamento e nas sincronizações de Manejo e Kata. Classe 0 e benefícios gratuitos fora da lista não fornecem espaços para essa troca. A candidata adota uma revisão compartilhada por subida de nível: refazer a troca disputa a mesma revisão usada para reescrever um feitiço; preencher um espaço novo não a consome.

Toque, alcance, área, Restrições embutidas, devolução de pontos, resolução por ataque/TR e repetições de dano receberam esclarecimentos e decisões registradas. Técnica Máxima passa a separar explicitamente seus dados e seu orçamento; o orçamento candidato foi revisto para **8/12/16**, evitando que montagens antes válidas deixem de caber apenas pela subida de faixa.

## Estado da validação

Foram feitas auditorias documentais, leituras críticas por modelos, comparações dirigidas com regras de outros RPGs e verificações numéricas. **Não houve playtest nem teste com leitores humanos.** Não interpretar aprovação de cálculo como prova de equilíbrio ou de compreensão por iniciantes.

Para o resultado final do PDF, das contas e dos testes de regressão, consulte os arquivos atuais em `evidencias` e a conferência deste lote. Este README não fixa totais de páginas ou de verificações, pois esses resultados precisam corresponder ao hash final do manuscrito e do PDF.

## Continuidade

- **R07:** revisar e consolidar o catálogo completo de Famílias, Formas, Melhorias, Restrições e Passivas. Resolver destinos de consulta, pares ainda abertos e cópias das regras em Invocações.
- **R08:** concluir poderes avançados, incluindo domínio, confrontos e avaliação comparativa das Máximas ofensivas, de cura e utilidade. Os procedimentos e exemplos deste lote não substituem essa revisão.
- **Rotas e integração:** aplicar as sincronizações somente junto da revisão correspondente, preservando números próprios de entidades e requisitos de cada rota.
- **Morrendo e Integridade:** revisão conjunta futura, conforme pedido do usuário. Cura, socorro a zero, dano de alma, estados, morte do invocador e permanência de efeitos precisarão ser reavaliados depois dela.

O tema rosa/roxo é preservado. Nenhuma imagem gerada por IA faz parte deste lote. Exemplos de técnicas e personagens são originais do Projeto M; seus números não são afirmações sobre o cânone de Jujutsu Kaisen.

## Resultado desta exportação

29 páginas, cinco grupos principais recolhidos no painel de navegação, fontes incorporadas e remissões internas verificadas. As 233 conferências do PDF passaram; todas as páginas foram inspecionadas visualmente. A auditoria do modelo aprovou 68 verificações de texto/conta e 53 casos funcionais, com 39.032 estados de orçamento. A análise de Certeiro tem 63 cenários de custo; a progressão da Máxima usa 840 perfis de preço. Essas contagens têm escopos diferentes e não devem ser somadas como se fossem testes de mesa.

Reproduzir com o Python do ambiente: `python auditar.py`, `python verificar_sincronizacoes.py`, `python gerar_pdf.py`, renderizar e inspecionar se houver mudança, então `python conferir.py`. Os geradores exigem o registro editorial atualizado; não mudar hashes para aprovar uma versão que não foi lida. `CONFERENCIA.json` e `evidencias/inspecao-visual.json` vinculam a aprovação aos arquivos atuais.

## Atualização de 03/10 — acesso e catálogo

Invocação por espaço exige Descrição e Regra que prevejam criar, chamar ou controlar entidades; o requisito também aparece nas rotas de Manejo/Kata e nos patches. O exemplo positivo usa animais de papel, e o negativo uma técnica que apenas corta fios. FU-51 registra o pedido. FU-52 fecha Armado/Segura na Técnica Máxima, em continuidade com R07.

## Estado após catálogo R07

R07 está escrito em 30 páginas, com 106 entradas conferidas. A matriz atual está em `../../catalogo/lote-01/evidencias/MATRIZ-R06-R07.json`: 53 combinações consolidadas e uma interface com Condições. As contagens anteriores da matriz neste relatório documentam a etapa R06 antes desse fechamento. FU-51 a FU-55 registram requisito de invocações, Máxima adiada, Sem Volta/Vazio, títulos e novo exemplo de Passiva Livre. A candidata final tem 56 decisões, das quais 28 mecânicas/lacunas.

FU-56 acrescenta remissão à exceção de Energia Reversa em Ferir maldições, sem reproduzir seu procedimento.

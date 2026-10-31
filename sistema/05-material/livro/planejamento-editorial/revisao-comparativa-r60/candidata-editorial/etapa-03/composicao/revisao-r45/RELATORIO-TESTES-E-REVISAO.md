# R45 — relatório de testes e revisão

13/10/2026. Integração das Origens v178 sobre a R44, preservada integralmente. As decisões adicionais I001 e I002 estão registradas literalmente. Não houve commit, push ou publicação do livro.

## Integrado

Sete núcleos, dois ramos alternativos de Restrição Celestial, base + uma marcante + duas menores elegíveis. Sem Técnica separado. 52 blocos no registro antes/depois: 38 de Origens (12 novos) e 14 dependências. Outros 459 blocos permanecem idênticos. Um modelo suplementar de ficha foi atualizado com registro próprio.

O mapa decisão → texto → ficha reúne 146 entradas/títulos, com referências documentais. As fontes selecionadas estão copiadas em fontes-de-decisao, com hashes. Histórico e justificativa não entram no texto do jogador. Exemplos finais e suas diferenças estão no mesmo registro de blocos.

## Testes executados

- 68 casos determinísticos em TESTES-CALCULOS.json: todos aprovados, com entradas, gabarito e resultado. Incluem recuperação, arredondamentos, faixas, limites e contagens.
- Duplas elegíveis enumeradas por perfil, preservando restrições e repetições específicas; não se tratam de simulações de combate.
- Quatro fichas comparadas nos níveis 2, 10, 18 e 26, sob premissas idênticas de Caminho/atributos explicitadas em FICHAS-COMPARADAS.json. Não representam todos os Caminhos e Trilhas.
- Seis sequências de consumo de recursos em TESTES-DE-CONSUMO.json: todas aprovadas. Cenários modelados, sem dados humanos de mesa.
- 19 cenários de leitura/interação em CENARIOS-DE-LEITURA.json, examinados em autorrevisão mecânica e editorial.
- 11 casos executados na cópia nativa da ficha: entrada/saída da faixa de 30%, mudança do máximo, vida zero, usos, turno, Ação Bônus, impedimento, PE e outra Origem. Todos aprovados; dados de ensaio removidos e fórmulas restauradas.
- Validação do PDF (script conferir_livro.py --strict): 122.552 verificações, 2.502 links internos, 192 marcadores, 511 blocos, 388 páginas, zero problemas apontados.
- Comparação dos 2.637 arquivos fotografados da R44: nenhuma divergência. Cada diferença do livro consolidado corresponde ao registro antes/depois da R45.

## Leitura e prova visual

Autorrevisão do texto final, comparação com aprovações e correção de seis achados de redação/remissão. Prova final de 69 páginas renderizadas, incluindo as 32 páginas do capítulo de Origens (66–97), dependências, sumário e índice. Cinco achados de composição/ordenação foram corrigidos e reconferidos. Páginas e critérios em REVISAO-VISUAL.json; imagens em prova/.

A verificação automática abrange o PDF inteiro; a inspeção visual abrange as 69 páginas indicadas. Não houve playtest humano, leitor externo, segunda revisão independente ou certificação de acessibilidade. Os testes não demonstram equilíbrio definitivo.

## Ficha

Foi criada uma cópia da ficha acessível, sem alterar a original. A aba ORIGENS R45 recebe escolhas e um alerta de regeneração do Híbrido; a vida na aba FICHA também recebe destaque quando entra na faixa. O alerta separa limiar de vida das demais condições de uso. O painel foi inspecionado visualmente no navegador. As demais automações antigas permanecem e precisam de conferência manual: esta entrega não é uma conversão completa do motor da ficha.

## Exportações

PDF, LIVRO-COMPLETO.md, FICHAS-COMPLETAS-R45.md, fontes/camadas editáveis e registros. DOCX não integra o fluxo efetivo da base; não foi fabricada uma exportação alternativa. O ZIP conserva os insumos de geração e os relatórios pertinentes, sem duplicar os PDFs e provas históricas pesadas.

## Reprodução do pacote

O ZIP foi extraído em uma pasta temporária e gerou novamente 388 páginas com sucesso. Markdown consolidado, páginas, âncoras, capítulos, marcadores e geometria de todos os eventos idênticos à entrega. Resultado detalhado em REPRODUCAO-DO-PACOTE.json.

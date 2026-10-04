# Referências e fundamento das escolhas editoriais

Levantamento inicial de 02/10/2026 para o planejamento da revisão do Projeto - M v0.331.

**Complementado nesta data:** [estudo dos nove arquivos enviados](ESTUDO-DOS-LIVROS.md), [diagnóstico a partir do feedback](DIAGNOSTICO-DO-LEITOR.md), [auditoria dos PDFs atuais](AUDITORIA-DO-PDF.md) e [metodologia e testes com leitores](METODO-E-TESTES-COM-LEITORES.md). A tabela abaixo conserva o recorte inicial, inclusive Pathfinder, que não faz parte dos nove ZIPs da remessa posterior.

## O que foi consultado

Foram extraídas as páginas iniciais dos quatro PDFs locais abaixo. O sumário e as passagens relevantes foram lidos, e uma página representativa de cada referência foi inspecionada visualmente. Este é um levantamento de arquitetura, não uma revisão integral desses livros nem uma pesquisa de equilíbrio de suas regras.

Os números “PDF” indicam a posição física no arquivo local, contando a primeira página como 1. Quando há paginação impressa legível, ela aparece separadamente.

| Referência e localização | Observação confirmada | Aplicação proposta no Projeto - M | Custo ou limite da aplicação |
|---|---|---|---|
| D&D, Livro do Jogador 2024. PDF 9, sumário; PDF 11, página impressa 5. [Arquivo local](../../../../PDFs%20-%20Sistemas%20Extras/PDF_Sistemas/Player_Hand_Book_DnD_2024.pdf) | A apresentação encaminha de fundamentos para criação, depois opções e catálogos. O glossário fica no apêndice. A própria introdução explica que o índice encaminha nomes antigos aos novos. | Antecipar a criação, deixar o glossário completo como consulta e preservar a busca pelos nomes anteriores. | O Projeto - M exige construir técnicas e entidades; a sequência de um catálogo de magias pronto não cobre essa necessidade. |
| GURPS, Módulo Básico, edição de luxo. PDF 3 e 4, sumário; PDF 7, página impressa 7. [Arquivo local](../../../../PDFs%20-%20Sistemas%20Extras/PDF_Sistemas/gurps---gurps-4ed.---edicao-de-luxo.pdf) | Um glossário resumido aparece antes da criação, com conceitos e referências para a explicação completa. O sumário distingue criação, vantagens e modificadores. | Quadro curto de termos indispensáveis e procedimentos que apresentam o orçamento antes de combinar escolhas. | O quadro pode virar outro catálogo na abertura se tentar cobrir todo o sistema. A montagem por pontos também precisa de exemplos locais. |
| Pathfinder, Livro Básico, segunda edição, arquivo local anterior ao Remaster. PDF 3 e 4, sumário. [Arquivo local](../../../../PDFs%20-%20Sistemas%20Extras/PDF_Sistemas/pathfinder---livro-basico-2-edicao.pdf) | A introdução inclui criação. Catálogos de personagem vêm antes do capítulo detalhado de regras; mestragem tem seu próprio capítulo. Condições e índice encerram o livro. | Distinguir entrada do leitor, opções de personagem e consulta detalhada. É uma referência de organização diferente de pôr todas as regras completas no início. | Leitura linear exige mais saltos. O Projeto - M precisa compensar com rotas de leitura, referências e marcadores digitais. |
| 3D&T Alpha, Manual Revisado. PDF 5, página marcada “1d+4”, sumário. [Arquivo local](../../../../PDFs%20-%20Sistemas%20Extras/PDF_Sistemas/3dt-alpha-manual-revisado-biblioteca-elfica.pdf) | O Herói precede Os Números e os catálogos. Combate e magia têm partes próprias; O Mestre fica no fim. A amostra combina desenho, espaço em branco e hierarquia legível. | Dar entrada pelo personagem e preservar uma fronteira para conteúdo de mestre. Usar ilustração com função de apresentação e orientação. | A menor complexidade das entradas não deve ser tomada como licença para omitir custos e exceções do Projeto - M. |

As colunas de aplicação e custo são análise editorial deste planejamento. Elas não são resultados de testes com leitores nem afirmações dos autores dos livros.

## O que já existe no projeto

- [Regra de voz](../REGRA-DE-VOZ.md): convenções aprovadas, distinção entre texto de mesa e argumento de design, catálogo e termos com destino.
- [Método de passada de texto](../METODO-passada-de-texto.md): conferir números e ler os casos que uma medida aponta; não usar contagem como ordem automática de corte.
- [Material de mestre removido](../REMOCOES-material-de-mestre.md): destinos já decididos, incluindo PvP.
- [Relatório da integração](../../../01-pesquisa/integracao-v0.331/RELATORIO.md): fidelidade, ajustes do Bastião, novas fontes e limites das validações.
- [Retomada vigente](../../../ESTADO-ATUAL.md): fila atual e precedência sobre o histórico.
- [Pesquisa anterior de arquitetura](../build/skills/arq/arquitetura-de-manual-rpg/references/anatomia-comparada.md): contexto útil, com amostragem e fontes secundárias explicitadas.

As referências secundárias da pesquisa anterior não foram usadas para sustentar contagens ou estrutura dos livros nesta proposta. As escolhas centrais acima foram confrontadas com os PDFs locais.

## Como foram obtidas as medidas do diagnóstico

As 22 fontes da pasta manual foram lidas como texto. A contagem lexical inclui sequências de letras e números, títulos e tabelas. Com esse método, o conjunto tem 109.263 palavras ou sequências numéricas. O inventário JSON registra os resultados por arquivo, seus títulos e hashes.

Caminhos e Trilhas, Fundamento e Invocações somam 62.553 dessas unidades, ou 57,2% do conjunto. Isso mostra concentração de material; não mede qualidade nem quantidade de texto dispensável.

O capítulo dos Caminhos foi separado pelas seis seções de nível 2:

| Caminho, com suas Trilhas | Contagem lexical |
|---|---:|
| Bastião | 1.622 |
| Vanguarda | 5.724 |
| Guia | 4.435 |
| Emanador | 3.612 |
| Evocador | 8.291 |
| Incursor | 7.701 |

A diferença sugere que os lotes exigirão esforços distintos. Não se propõe igualar seus tamanhos: parte da diferença vem de quantidade de opções e parte pode vir de estilo. Cada caso precisa de leitura.

O inventário de títulos ajuda a localizar os blocos. A análise de conteúdo foi direcionada à abertura, criação, procedimentos, Caminhos e interfaces dos construtores. Este planejamento não declara uma revisão linha a linha de todas as regras.

## Uso de novos livros de referência

Quando o Mizuki acrescentar outros livros, registrar que problema cada amostra ajuda a resolver: explicação inicial, catálogo, habilidade, construção de poder, consulta ou direção visual. Ler sumário e páginas representativas antes de mudar o plano.

Uma referência nova não exige copiar seu vocabulário, diagramação ou ordem inteira. A decisão continua dependente do público e das regras do Projeto - M.

Os PDFs de terceiros não fazem parte do pacote de planejamento. O pacote contém a análise e a identificação das fontes; os arquivos locais permanecem em sua pasta de referência.

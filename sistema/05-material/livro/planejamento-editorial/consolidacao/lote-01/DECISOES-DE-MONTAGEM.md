# Decisões de montagem

## Fluxo e hierarquia

Antes, cada bloco das provas começava em uma página. Agora somente capítulos, Caminhos e modelos imprimíveis iniciam página. Os demais títulos participam do fluxo normal, unidos ao parágrafo ou à tabela seguinte. Tabelas podem continuar na página seguinte com cabeçalho repetido. Quadros de exemplo permanecem inteiros.

Desde 04/10/2026, uma tabela que continua na página seguinte deixa pelo menos duas linhas em cada página. Ela não termina a página só com o cabeçalho e uma linha, nem deixa uma linha sozinha sob o cabeçalho repetido. Uma tabela de até três linhas não quebra.

Um título seguido de até quatro linhas e de uma tabela vai junto com o cabeçalho e as duas primeiras linhas dela. Um título seguido de uma linha só, como a linha de uso de uma habilidade, vai junto com o começo do texto seguinte. Antes, o livro tinha 10 tabelas com uma linha sozinha e 12 títulos sozinhos no pé da página, com até quatro linhas e a tabela ou o texto na página seguinte. O `conferir_livro.py` confere as duas coisas no PDF, sem depender do gerador.

A regra usa a mesma conta do quadro de página do ReportLab. A alternativa de mandar o grupo inteiro para a página seguinte sempre que a tabela não cabe inteira foi testada e deixou o livro com 388 páginas, em vez de 382.

Foi mantida uma coluna para esta prova. Os catálogos têm tabelas largas e fórmulas que se beneficiam da mesma área de leitura. O corpo usa Spectral, os títulos Barlow Condensed, com a paleta #251727, #BC2A6E e #FDF0F6. Não houve redução geral de fonte para comprimir o livro.

Um primeiro cabeçalho idêntico ao título do capítulo é apresentado uma só vez. Sua âncora continua apontando para esse cabeçalho. O mapa registra quais cabeçalhos foram unidos; nenhum texto de regra é removido por essa operação.

## Painel e remissões

O painel tem cinco partes recolhidas, capítulos no nível seguinte e seis Caminhos dentro de Caminhos e Trilhas. Os demais títulos têm destinos internos, sem gerar centenas de entradas no painel.

Cada âncora recebe o prefixo do documento de origem. Assim, dois capítulos podem usar um identificador como `cura` sem colidir. Links locais são convertidos para o destino qualificado. Glossário e índice usam o mapa estruturado de Consulta, por termo, arquivo e âncora. O gerador não adivinha a equivalência de títulos nem conserva a página de uma prova antiga.

A paginação é calculada em passagens até convergir. Os números impressos nas remissões e no sumário pertencem à prova atual. A conferência precisa ser reexecutada sempre que uma fonte mudar.

## Cobertura e preservação

ORDEM.json seleciona blocos inteiros. Cada bloco deve aparecer exatamente uma vez. O gerador recusa blocos duplicados ou omitidos, incluindo novos blocos acrescentados depois. O seletor de Referências e fichas exclui prefixos de índice e glossário, para que seu crescimento não gere duplicação.

O manuscrito único é derivado, com rastreio de cada bloco e hash das fontes. Os donos permanecem editáveis e são relidos a cada execução. A conferência compara também o texto de cada bloco ao intervalo correspondente do PDF, permitindo cabeçalhos repetidos de tabela.

## Revisão visual inicial

A primeira amostra identificou uma quebra inconveniente na palavra Volume no cabeçalho das tabelas de armas. A largura dessa coluna foi ampliada no gerador, preservando o tamanho da fonte e os dados. A inspeção integral da prova final permanece pendente.

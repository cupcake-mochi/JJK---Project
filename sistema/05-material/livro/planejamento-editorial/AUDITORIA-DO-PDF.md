# Auditoria de navegação e diagramação — Projeto - M v0.331

Data da conferência: 2 de outubro de 2026. Leitura somente; nenhum PDF, fonte ou gerador do projeto foi alterado.

## Escopo e limites

Foram examinados os dois PDFs atuais, seu HTML intermediário e os arquivos `build.py`, `manual.css` e `duas-colunas.css`. A contagem de marcadores foi feita na árvore real `/Outlines` dos PDFs com pypdf; o texto foi extraído com Poppler. A inspeção visual cobriu 40 páginas em folhas de contato (20 de cada edição), com ampliação dos exemplos críticos descritos abaixo. Isso é uma amostra editorial, não uma validação visual integral das 620 páginas somadas. Não foi executado novo build: os artefatos auditados são exatamente os publicados na pasta.

Fontes locais:
- `sistema/05-material/livro/Projeto-M-Manual-da-Guilda.pdf`
- `sistema/05-material/livro/Projeto-M-Manual-da-Guilda-C-duas-colunas.pdf`
- `sistema/05-material/livro/build/manual.html`
- `sistema/05-material/livro/build/build.py`
- `sistema/05-material/livro/build/manual.css`
- `sistema/05-material/livro/build/duas-colunas.css`

Os cinco prints da leitora Caramelo são evidência de experiência de leitura. A numeração citada neles não equivale automaticamente à paginação atual: a edição atual ganhou capa artística, por exemplo. As observações foram confrontadas com os arquivos atuais, sem adotar seus conselhos como regras absolutas.

## Navegação: a reclamação tem causa objetiva

| Medida | Uma coluna | Duas colunas |
|---|---:|---:|
| Páginas | 380 | 240 |
| Marcadores no PDF | 827 | 827 |
| Nível 1 | 26 | 26 |
| Nível 2 | 195 | 195 |
| Nível 3 | 345 | 345 |
| Nível 4 | 182 | 182 |
| Nível 5 | 75 | 75 |
| Nível 6 | 4 | 4 |
| Nós com descendentes | 199 | 199 |
| Nós com descendentes abertos no arquivo | 199 | 199 |
| Nós com descendentes fechados no arquivo | 0 | 0 |
| Folhas | 628 | 628 |

O `/Count` da raiz do outline é 827. O leitor de PDF pode recordar o estado de uma sessão anterior; a informação medida aqui é o estado gravado no próprio arquivo.

O HTML contém exatamente 827 títulos `h1` a `h6`, na mesma distribuição de níveis. Não existe política explícita de `bookmark-level`, `bookmark-state` ou seleção editorial de marcadores nos CSS examinados. O documento está expondo a hierarquia inteira de títulos como navegação lateral, inclusive subtítulos que servem apenas para organizar uma regra na página.

Não são 827 capítulos: são 19 capítulos numerados mais material de abertura, índice e centenas de subdivisões. Essa diferença precisa aparecer na explicação ao usuário.

São 704 títulos distintos, com 123 ocorrências adicionais de títulos repetidos. Exemplos: “Efeito na ficha”, “Destranca” e “Ajusta” aparecem 8 vezes cada; “Limites”, 7; “Catálogo” e “Progressão da Trilha”, 6; “Exemplo”, 5. Repetição sob um pai claro pode ser legítima, mas esses rótulos têm pouco valor quando a árvore inteira está aberta.

Concentração de descendentes:

| Capítulo | Marcadores abaixo dele |
|---|---:|
| Caminhos e Trilhas | 232 |
| Origens e Legados | 93 |
| Fundamento | 77 |
| Invocações | 61 |

O sumário impresso tem 216 entradas, derivadas dos títulos `h2` mais aberturas/índice. Ocupa as páginas 4–7 na edição de uma coluna e 4–5 na de duas. O algoritmo copia cada `h2` para o sumário (`md_para_html`, linhas 568–578; construção do sumário, linhas 962–982). Assim, a escolha tipográfica de um título está decidindo sua presença no sumário, e a escolha editorial de navegação fica implícita.

### Mudança proposta

Separar três produtos editoriais: sumário geral, marcadores laterais e índices locais de catálogo. Preservar as âncoras e os links úteis mesmo quando um título deixa de aparecer na lateral.

- Sumário geral: partes, capítulos e apenas as entradas de leitura mais úteis. O detalhe dos catálogos passa a um índice local no começo de cada catálogo.
- Lateral: capítulos e seções úteis à consulta; Caminhos e Trilhas devem ter acesso direto aos seis Caminhos e às dezoito Trilhas. Níveis e habilidades podem ser alcançados pelas tabelas de progressão clicáveis na página da respectiva Trilha.
- Estado inicial: ramos recolhidos abaixo do primeiro nível escolhido. Não abrir centenas de entradas ao carregar o arquivo.
- Rótulos específicos: uma entrada geral “Exemplo” vira, quando necessária à navegação, “Exemplo de criação”, “Exemplo de descanso”, etc.
- Metadados editoriais explícitos decidem o que entra na navegação. Não rebaixar o título semântico do texto apenas para escondê-lo do PDF.
- Evitar um teto arbitrário de entradas totais. O teste importante é encontrar rapidamente uma regra comum sem percorrer uma árvore já expandida de centenas de itens.

## Páginas verificadas e achados visuais

| Exemplo atual | Constatação | Encaminhamento |
|---|---|---|
| P. 1 nas duas edições | Capa artística ainda mostra “v0.1”. O livro auditado é v0.331. | Conferir se é uma versão intencional da arte; para o leitor, corrigir ou remover o rótulo ambíguo na futura capa. Isso não prova que o conteúdo está velho. |
| P. 2 nas duas edições | Capa tipográfica reserva 42 mm no alto; símbolo é um bloco isolado de 26 mm, seguido de 14 mm de margem. Uma segunda lista de capítulos repete a função do sumário. Nota de guilda fica no rodapé a 8,4 pt e em cinza, contra 10,6 pt do corpo principal. | Tratar como folha de rosto/abertura com função definida. Reorganizar o símbolo; tirar a lista duplicada; introduzir a proposta de jogo em texto legível, em vez de delegá-la à nota discreta. |
| P. 3 nas duas edições | Créditos reiteram guilda/personagem persistente antes da introdução. | Créditos ficam nos créditos; a apresentação do jogo e da guilda recebe um lugar principal. |
| P. 4–7, uma coluna | Sumário longo, com continuação de capítulo no topo de outra coluna/página e muitos subtítulos. P. 7 ocupa só uma parte superior pequena. | Enxugar a navegação geral. Manter juntos os pequenos grupos do sumário e sinalizar continuação quando necessária. Não bloquear todo o capítulo para caber na mesma página. |
| P. 8–10, uma coluna; p. 6–7, duas | A introdução passa rapidamente de dois parágrafos para material de mesa e uma tabela de capítulos. Na edição de uma coluna, a tabela começa no fim da p. 8, continua na 9 e deixa poucas linhas de orientação sozinhas na p. 10. Nas duas colunas, o grupo “O jogo” fica no fundo esquerdo da p. 6, separado das entradas que começam no topo direito; o capítulo termina com grande sobra na p. 7. | Reescrever e diagramar a entrada como percurso de leitura com apresentação do mundo e do tipo de personagem. Reduzir a duplicação sumário/tabela. Não corrigir o vazio inflando o texto. |
| P. 8, uma coluna; p. 6, duas | Texto ainda abre com “Você vai criar um feiticeiro”, depois já presume maldições, clãs e instituição. A identidade e os conflitos desse mundo recebem muito pouca apresentação antes dos termos de regra. | A futura abertura precisa acolher quem não domina JJK e apresentar possibilidades reais do sistema. Isso requer trabalho editorial e temático; não se resolve só com CSS. |
| P. 187–188, uma coluna; p. 126–127, duas | A Trilha Assassino começa junto do fim do Incursor. Na edição de uma coluna, “Alvo Estudado” abre na p. 187, suas oportunidades começam na 188; “Golpe Cirúrgico” começa no fim da 188 e segue na próxima página. As letras estão legíveis, mas a unidade de consulta se fragmenta. | Dar às Trilhas entradas reconhecíveis; manter juntos nome, ativação, custo e núcleo da habilidade quando couberem. Textos longos podem continuar, com contexto explícito. |
| P. 198–199, uma coluna; p. 136–137, duas | Malabarista compartilha a abertura de página com o fim da Trilha anterior. Tabelas de progressão e continuação são úteis, mas a página é quase toda regra e exceção, sem elemento visual que diferencie a identidade da Trilha. | Projetar modelo de abertura de Caminho/Trilha com apresentação, função, progressão e ilustração funcional. Não acrescentar caixas vazias nem transformar todo parágrafo em card. |
| P. 325–326, uma coluna; p. 208–209, duas | Catálogo de Melhorias tem cabeçalhos de colunas repetidos na continuação. Na edição dupla, “Melhorias de Área” começa embaixo à esquerda na p. 208 e continua no topo direito com o cabeçalho genérico “Melhoria / Custo / O que faz”, sem repetir o nome da categoria. | Aceitar a quebra da tabela longa, mas repetir o nome da categoria ou “continuação”. Evitar separar o pequeno título do primeiro conjunto útil de linhas. |
| P. 336–337, uma coluna; p. 218–219, duas | Exemplos e procedimentos de entidade misturam narrativa, números, fórmulas e exceções em blocos densos. Há espaço para fluxos e ficha anotada, sem haver necessidade de mais ornamentação. | Usar um exemplo progressivo, uma ficha visual e sequência “declarar → pagar → resolver → encerrar”. Manter regra completa disponível junto da explicação. |

Na amostra examinada não foi identificada sobreposição catastrófica de texto, corte de borda ou caractere ausente que permita chamar o PDF inteiro de ilegível. Os problemas confirmados foram densidade, perda da unidade de consulta, fragmentação de grupos e desperdício causado pelo fluxo. A ausência desses erros graves na amostra não é certificado para todo o documento.

## Causas que o gerador ajuda a explicar

1. **Navegação automática sem seleção.** Todo título vira marcador e todos os ramos ficam abertos.
2. **Conteúdo antes de composição.** A abertura tem uma lista de capítulos, o sumário tem outra, a introdução traz uma tabela de capítulos e o glossário precede a primeira explicação de jogo. O leitor atravessa várias estruturas de orientação antes de jogar.
3. **Restrições globais de paginação.** `.capitulo { break-before: page; }`, blocos `.par` e destaques com `break-inside: avoid`, títulos com `break-after: avoid`, além de tabelas grandes com página própria. Essas regras são úteis individualmente, mas empurram conjuntos e podem deixar sobras; não podem ser substituídas por “nada nunca quebra”.
4. **Duas colunas dependem de segmentação.** `segmenta_colunas` separa blocos `.c2` de tabelas `.plena`, e `column-fill: balance` redistribui cada segmento. O gerador usa limiares por quantidade de colunas e linhas da tabela. Um parágrafo ou linha adicionada pode atravessar esses limiares e mudar o fluxo.
5. **A correção automática de órfãs só roda em uma coluna.** Em `desenha_sem_tabela_orfa`, linha 768, a variante diferente de `unica` retorna um render direto. Logo, o PDF de duas colunas precisa de inspeção própria das fronteiras entre colunas, mesmo que o render de uma coluna passe.
6. **As heurísticas aceitam compromissos.** O limite de buraco é 0,65 da altura, há até oito passadas e os títulos com até duas linhas recebem tratamento especial. O relatório da integração registra duas exceções antigas. O gerador avisa quando preserva uma separação para evitar um buraco pior; aviso não equivale a resolução editorial.
7. **Arte quase ausente do miolo.** O HTML contém zero elementos `<img>`; a única imagem identificada neste fluxo é a capa em CSS. Os kanjis e bordas dão identidade gráfica, mas não explicam personagem, espaço, combate ou construção de técnica.

## O que preservar das cores

Paleta atual, chamada “Neve Saturado” no CSS:

| Função/token | Cor |
|---|---|
| tinta | `#251727` |
| selo | `#2B1B2E` |
| selo-fraco | `#9A6F87` |
| acento | `#BC2A6E` |
| acento-claro | `#ECC3D6` |
| washi | `#FDF0F6` |
| zebra | `#FADDEA` |
| linha | `#F8C7DC` |
| cinza | `#847B86` |

O fundo de fallback da capa é `#22202C`. O requisito do usuário permite redesenhar hierarquia, grades, fontes e usos, conservando as cores do tema. Não se precisa manter todo texto pequeno no cinza ou no “selo-fraco”: usar tinta escura para leitura e deixar os tons claros como suporte preserva a paleta e pode melhorar o contraste.

As famílias atuais são Spectral no corpo, Barlow Condensed nos títulos e navegação, IBM Plex Mono nas expressões marcadas como código e Noto Serif CJK JP nos kanjis. Usar mais de uma família não é, por si só, inconsistência. A padronização deve definir papéis estáveis e legíveis, em vez de impor uma única fonte a todo o livro.

## Como transformar as opiniões em critérios de aceitação

- **Espaço vazio:** pode ser intencional em uma abertura. Defeito é uma regra ou pequeno grupo empurrado que deixa página quase vazia sem função. Toda ocorrência sinalizada precisa de classificação humana; não preencher automaticamente.
- **Quebra de texto:** parágrafos e tabelas longos podem atravessar páginas. Proibir título sem conteúdo útil; preservar as partes que precisam ser vistas juntas; repetir cabeçalho/categoria quando uma tabela continuar.
- **Nomenclatura em destaque:** escolher uma convenção por papel, sem itálico obrigatório em todo termo mecânico. O uso excessivo de negrito, itálico e fundo de código pode reduzir a hierarquia.
- **Tabela mais estreita:** nem toda tabela precisa ocupar a largura da página. Medir legibilidade, alinhamento e função; tabelas de duas colunas podem ficar estreitas legitimamente. A largura não deve oscilar sem propósito entre blocos equivalentes.
- **Quantidade de capítulos:** a dificuldade lateral vem da exposição de 827 títulos, não apenas de haver 19 capítulos. É possível reorganizar em mais capítulos e ainda entregar navegação muito mais simples.

## QA proposta para cada lote editorial

### Conferência automática

- Destinos do sumário e dos marcadores existem, apontam para a seção certa e continuam coerentes após repaginar.
- Estado inicial dos ramos e presença das entradas essenciais são testados no PDF exportado, não somente no CSS.
- Nenhum título decorativo/administrativo ou subtítulo genérico entra na lateral por acidente.
- Detectar texto fora da área útil, cortes de tabelas, páginas quase vazias e títulos isolados; gerar lista com página e motivo para revisão visual, sem consertos cegos.
- Verificar fontes incorporadas e substituições; tabelas e texto permanecem selecionáveis.
- Checagens de regras comparam custos, gatilhos, alvos, limites, duração e exceções antes/depois. A revisão gráfica não aprova mudanças mecânicas implícitas.

### Conferência visual

- Folhas de contato de todas as páginas do lote; ampliação de toda página sinalizada e das páginas anterior/seguinte.
- Inspecionar aberturas, habilidades curtas e longas, listas, exemplos com fórmulas, tabelas extensas, fichas e continuação de categorias.
- Conferir os dois PDFs separadamente enquanto ambos forem entregues. Uma variante passando não valida a outra.
- Para o piloto, comparar a leitura real em tela comum e em tela estreita antes de decidir que duas colunas resolvem a edição.

### Testes de uso com leitores

Dar tarefas concretas: localizar Bloquear; descobrir custo e momento de Golpe Cirúrgico; achar a Trilha Malabarista; encontrar uma condição; montar uma entidade com o catálogo. Registrar caminho usado, tempo, erro, releitura e ajuda solicitada. Medir também a capacidade de explicar a regra com as próprias palavras. Um teste externo real não pode ser substituído por concordância entre modelos.

Os resultados de leitores devem ser separados das inspeções por IA. As cinco imagens já fornecem uma opinião externa válida; não equivalem, sozinhas, a uma amostra representativa de jogadores ou a uma regra de diagramação universal.

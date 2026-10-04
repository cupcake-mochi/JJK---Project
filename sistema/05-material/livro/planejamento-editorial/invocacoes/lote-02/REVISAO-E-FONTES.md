# Revisão da construção de Invocações

Esta é uma candidata de construção e aquisição. `CONSTRUIR-INVOCACOES.md` não altera o manual publicado. O resultado depende de Fundamento revisado, Catálogo de criação, Invocações em campo e dos procedimentos de fabricação ainda em sua fila própria.

## Fontes e precedência

O capítulo atual `manual/60-invocacoes.md` foi lido integralmente. Sua cópia em `invocacoes/05-Edicao-Integrada/60-invocacoes.md` é idêntica, byte a byte. Os hashes estão em `evidencias/fontes-preservadas.json`. As decisões autorais posteriores ao §46 foram consultadas de forma dirigida para aquisição, níveis, corpo, construtor, Famílias, redução de efeitos, passivas, fabricação e domação.

A peça histórica `03-mecanica/15-invocacoes.md` foi identificada pelo próprio aviso como arquitetura anterior. Sua Matilha, orçamento de Traços, 18 m de amarra e dano por grupo **não foram incorporados**. O deslocamento-base de 9 m preenche uma omissão pela regra geral de movimento, e está registrado como fechamento mecânico, não como reativação da arquitetura antiga.

Fundamento R06 e Catálogo R07 são donos de preços, compatibilidades e efeitos comuns revisados. As sincronizações de Invocações dos dois lotes foram lidas. As tabelas próprias de entidade prevalecem para orçamento, dados, progressão, desconto Livre, intensidade reduzida e acesso às treze Passivas.

## Comparação editorial com livros locais

Foi feita leitura **dirigida**, não integral, dos PDFs fornecidos pelo usuário. No Player’s Handbook 2024 local, foram relidas as páginas de PDF 10, 241, 243 e 245: apresentação de jogo, aquisição de magias, campos da conjuração e exemplos de entradas. No Dungeon Master’s Guide 2024, foram relidas as páginas de PDF 62 e 63, sobre criação de itens e de magias. As extrações locais são `/tmp/r07-phb.txt` e `/tmp/r07-dmg.txt`.

Padrões aplicados: apresentar primeiro a aquisição, separar o custo para conhecer do custo para usar, manter campos de referência previsíveis, comparar uma proposta a opções já existentes e explicar limites de alcance/duração junto do efeito. As tabelas pessoais desses livros não foram transplantadas para o sistema. Os exemplos, nomes de personagens e capacidades desta candidata foram redigidos para o Projeto M.

A referência editorial principal é D&D, como o usuário pediu. A leitura destes trechos sustenta decisões de organização e consulta. Não demonstra que pessoas compreenderão o capítulo sem dificuldades.

## Comparação de força

A tabela reduzida preservada é **2/4/6/9/11/13/16 pontos** nas especiais. O dano-base das básicas permanece **1/2/2/2/3/3/3d6**. A auditoria recalcula a média de especial mais básica de outra entidade e a compara com o feitiço pessoal de mesma Classe. A diferença de granularidade nas Classes baixas permanece declarada, sem corrigir os dados aprovados para perseguir uma porcentagem ideal.

Essas médias supõem acertos e aplicação integral. Elas não simulam distribuição de Defesa, cobertura, baixas, custo de comando, cura, posições, equipamentos, talentos ou composições de Caminho. Portanto, não são uma certificação de equilíbrio do conjunto em jogo.

**Onda:** na fonte anterior, Restrição só recuperava gasto em Melhorias. O teto útil era orçamento reduzido menos o custo da Forma Pesada. A candidata permite reembolsar Forma por sincronização com R06, mas conserva explicitamente o teto antigo da Onda: **0/1/1/3/3/4/5**. Sem isso, uma entidade de Classe 1 poderia recuperar até 2d8 por aliado, superando até a Onda pessoal limitada a 1d8. O perfil útil de Classe 1 foi mantido: Onda + Impulso + Gesto concede o benefício de Impulso na área por 3 PE, com zero dados. A proposta não aumenta sua cura e exige benefício aplicável numa montagem de saldo zero.

**Cura comum:** a mesma análise vale para a Forma Média. Seu teto próprio fica em orçamento reduzido menos preço Médio: **1/2/3/5/6/7/9d8**. A primeira sincronização candidata usava o teto pessoal de 2 × Classe e recuperava a Forma, produzindo um aumento não autorizado. Isso foi corrigido antes de entregar o lote. A cura da Técnica Máxima continua usando seus dados fixos, como exceção expressa.

**Família Livre:** o desconto próprio da entidade usa metade para baixo, mínimo 1. Comparar apenas com o desconto pessoal para cima daria descontos indevidos nas Classes 3, 5 e 7. Os preços completos são calculados pela Classe real, enquanto sete efeitos e tamanhos de área usam uma Classe abaixo, mínimo 1.

**Domada:** importar uma ficha de Chefe com ações adicionais e vida de encontro invalidaria a economia aprovada. A conversão deve ser apresentada antes da tentativa. Por exemplo, um inimigo de nível 5 com Constituição 2, 120 PV e três ataques por turno passa a usar a escala da entidade: 27 PV, uma atuação básica e os limites de especial. Sua capacidade de lançar espinhos pode continuar como função, mas precisa da montagem e dos valores disponíveis. Este é um exemplo hipotético de fronteira, não uma alteração aplicada a um monstro existente. Registre os cortes de cada ficha real.

**Passivas:** escolher uma CP inferior à máxima do marco foi aceito para ampliar opções sem aumentar o teto. Não promove escolhas anteriores. As treze entradas permitidas continuam fechadas. Passiva Própria não dá acesso automático a mais ações, percepção irrestrita ou Famílias Fechadas.

## Cânone e criação original

O capítulo apresenta regras do Projeto M. Não faz afirmações novas de que os valores, testes de domação, reservas ou formas de aquisição sejam regras universais da obra. Cão de sombra, Vigia de papel e Registro de cena são exemplos originais. A divisão entre corpo autônomo com alma e corpo sem alma é preservada como regra do sistema, com interface no dono de campo, sem alegar uma verificação integral do mangá nesta rodada.

Não foi usado Feiticeiros & Maldições como autoridade de cânone. Não foram produzidas imagens de IA.

## Evidências e limites

`INVENTARIO.json` atribui todas as seções da fonte a R11 ou R12. `COBERTURA-CATALOGO.json` registra cada entrada copiada na fonte e seu destino. `REVISAO-EDITORIAL.json` contém leitura contextual por seção. `regras-verificadas.json` contém pares de casos positivos e negativos **raciocinados**, sem alegar execução com jogadores.

`auditar.py` confere tabelas donas, exemplos, limites, marcos e restituições. Seu resultado fica em `AUDITORIA.json`. A auditoria editorial automática tem exceções documentadas somente para requisitos e remissões necessários. Ela não mede naturalidade nem substitui a leitura contextual.

V12 foi concluído por revisor diferente do autor, com três achados corrigidos e conciliação posterior da reserva total de corpos. V13 e V14 incluem exportação e inspeção visual das 27 páginas. A revisão final corrigiu uma palavra dividida na tabela de áreas e a largura da tabela de ampliação. A conferência automática fica em `CONFERENCIA.json`. Não houve teste humano ou playtest. O relatório não usa métricas de PDF ainda inexistente.

A integração final deve reavaliar remissões e paginação entre os capítulos. Morrendo e Integridade continuam reservados para revisão conjunta. A fabricação física de entidades é dependência real de outra etapa e não foi simulada como procedimento já completo.

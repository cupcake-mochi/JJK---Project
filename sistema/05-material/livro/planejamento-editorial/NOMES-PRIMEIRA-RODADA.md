# Primeira pauta de nomes centrais

Base examinada: v0.331. Estado: propostas para discussão; nenhum renome aplicado. Esta pauta trata de três conceitos, não abre uma lista geral de nomes. A prioridade é conseguir explicar a mesma regra com menos esforço e preservar a identidade jujutsu.

## O tamanho real da mudança

Contagem nas **22 fontes registradas em INVENTARIO-BASE.json**, incluindo o início rápido. Os 22 conteúdos coincidem com seus SHA-256 registrados. Nenhum dos 22 arquivos Markdown da pasta manual ficou fora desta contagem.

Método: leitura UTF-8, normalização Unicode NFC e busca de palavras inteiras, sem distinguir maiúsculas de minúsculas. Singular e plural separados; títulos, tabelas, exemplos e referências do próprio texto entram. Não entram nomes de arquivos, PDFs exportados, histórico ou planejamento. É contagem lexical para estimar alcance, não classificação semântica de cada ocorrência. O [resultado por fonte](evidencias/contagem-nomes.json) acompanha a pauta.

| Termo | Ocorrências | Fontes com ocorrências |
|---|---:|---:|
| Fundamento | 73 | 15 |
| Fundamentos | 4 | 3 |
| Classe | 593 | 19 |
| Classes | 16 | 5 |
| Classe Passiva | 92 | 9 |
| Classes Passivas | 0 | 0 |
| Refino | 166 | 15 |
| Refinos | 0 | 0 |

**As 92 ocorrências de Classe Passiva já estão dentro das 593 de Classe.** Não somar as duas linhas. Há também usos abreviados como “Passiva de Classe 2”; portanto, subtrair 92 não produz automaticamente uma lista de todas as Classes de feitiço.

## 1. Fundamento: podemos falar mais diretamente em técnica?

**O conceito atual:** a descrição e as escolhas que definem a técnica e orientam suas aplicações: Regra, Famílias, Selo e Passivas. Seus feitiços são aplicações concretas dessa base.

A abertura do construtor e o glossário chamam isso de técnica inata. Mas a rota **Sem Técnica também escreve um Fundamento**, construído a partir de uma aptidão. Isso consta nas fontes vigentes: [Fundamento, abertura](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/40-fundamento.md:5>), [Origens, Sem Técnica](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/25-origens.md:451>) e [Sem Técnica, abertura](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/43-sem-tecnica.md:3>).

| Opção | O que ganha | Custo ou risco |
|---|---|---|
| **Técnica** | Aproxima a ficha do que o jogador imagina e reduz um nome intermediário. A própria rota Sem Técnica explica que a técnica foi construída, em vez de nascer com a pessoa. | Exige distinguir a técnica inteira de cada feitiço e dos nomes Técnica Marcial/Técnica Máxima. Há muitas ocorrências genéricas da palavra; a migração deve ser por sentido, não substituição global. |
| **Fundamento da Técnica** | Explicita que é a base usada para construir as aplicações, preservando o nome atual reconhecível. | Continua relativamente abstrato e aumenta o comprimento de títulos e campos. Funciona melhor como título explicativo do que como palavra repetida na conversa. |
| **Técnica Inata** | É reconhecível para a rota que efetivamente tem esse dom. | **Não serve como renome global:** atribuiria uma técnica inata à rota Sem Técnica. Usá-lo seletivamente exige separar o nome da ficção do nome do procedimento de construção. |

**Minha preferência para o primeiro teste é Técnica**, sempre reservando “feitiço” para uma aplicação concreta. A decisão inclui conferir como a rota Sem Técnica será apresentada após a conciliação das Origens. Se a intenção for manter um nome próprio para o construtor, “Fundamento da Técnica” é a alternativa conservadora. Trocar tudo por “Técnica Inata” não é recomendado.

O nome atual pode continuar no piloto, explicado uma vez. Não precisamos inventar um conceito novo para substituir uma palavra difícil.

## 2. Classe e Classe Passiva: são duas escalas diferentes

**O conceito atual:** Classe, de 0 a 7, governa orçamento, custo e limites de feitiços e aplicações equivalentes. Classe Passiva usa outra escala, Livre/1/2/3; classifica Passivas, mas também aptidões e Bênçãos. Nestas últimas, o número não é seu preço: aquisição e requisitos seguem regras próprias. Fontes: [Classe](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/40-fundamento.md:9>), [Passivas](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/40-fundamento.md:280>), [aptidões](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/45-aptidoes-e-refino.md:96>) e [Bênçãos](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/47-bencaos-e-lapidacao.md:45>).

O problema não é somente sonoridade: alguém pode ler “Classe Passiva 3” e concluir que o efeito nunca exige ativação, ou confundir classe com o papel de personagem. D&D usa “class” para Bárbaro, Guerreiro etc.; isso confirma uma associação possível para leitores vindos desse sistema, sem provar que todos os nossos leitores a terão. [Regra oficial de classes](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes).

| Par de nomes | O que ganha | Custo ou risco |
|---|---|---|
| **Potência / Categoria de Efeito** | Distingue o orçamento crescente da classificação Livre/1/2/3. “Categoria de Efeito” funciona em Passivas, aptidões e Bênçãos, sem afirmar que todos são efeitos passivos. | Potência já foi um nome provisório e foi aposentado. Voltar a ele exige decisão explícita de nomenclatura. Também precisa de um exemplo de efeito sem dano, para potência não parecer sinônimo de dano. “Categoria” sozinho já é usado para armas; manter o complemento nos contextos ambíguos. |
| **Círculo / Categoria de Efeito** | Fornece um nome curto, distinto de nível e Grau, para a escala 0–7. | Evoca organização mágica. Precisa ser testado também na Técnica Marcial e nas habilidades de entidades; pode combinar menos com essas rotas. Não considero automaticamente melhor só por lembrar outro RPG. |
| **Classe / Categoria de Efeito** | Corrige a sugestão enganosa de que tudo na segunda escala é passivo, com uma migração menor. | Conserva “Classe” e sua associação externa com tipos de personagem. Depende de a explicação local realmente resolver essa dúvida. |

**Minha preferência de teste é Potência / Categoria de Efeito**, comparada com a opção conservadora Classe / Categoria de Efeito. A primeira descreve melhor os dois papéis; a segunda permite medir se a mudança maior traz ganho real. Nenhuma delas muda escalas, custos ou requisitos.

No uso comum, potência pode significar força e capacidade de produzir um efeito; isso sustenta a possibilidade de uso, mas não demonstra que jogadores entenderão a escala sem explicação. [Priberam: potência](https://dicionario.priberam.org/pot%C3%AAncia).

**Não propor Grau ou Nível nesta rodada.** Grau já identifica patente e ferramentas. Nível já acompanha o personagem. O histórico registra que Grau do feitiço virou Classe precisamente para resolver a primeira colisão. D&D também precisa explicar que nível de magia e nível de personagem não coincidem; importar essa duplicidade não oferece uma solução gratuita. [Histórico local, v0.20](</media/mizuki/HD Externo II/Claude/Claude 2/logs/CHANGELOG.md:22186>), [regra oficial de nível de magia](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/spellcasting#SpellLevel).

## 3. Refino: o nome pode mostrar o que o número representa

**O conceito atual:** um valor de 1 a 10 associado ao controle de energia amaldiçoada, aos requisitos e efeitos de aptidões e a entregas específicas. Sobe nos marcos; a escolha de progressão Refino concede um aumento adicional e aptidão, respeitando o teto. Fontes: [Refino](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/45-aptidoes-e-refino.md:13>) e [progressão](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/80-experiencia-e-progressao.md:309>).

| Opção | O que ganha | Custo ou risco |
|---|---|---|
| **Controle de Energia** | Liga imediatamente o campo da ficha à prática do personagem. Ajuda a distinguir controle da quantidade de PE disponível. | É mais longo. A Família Controle já existe; não abreviar simplesmente para Controle no texto de montagem. A ferramenta acusa essa proximidade corretamente, mas os conceitos podem ser distinguidos pelo nome completo. |
| **Refino** | Preserva uma palavra curta, já presente nas fichas e falas, que combina com aperfeiçoamento. | Precisa apresentar o objeto: refino de quê? O leitor pode imaginar melhoria de equipamento. O dicionário também registra sentidos de purificação e refinamento; isso é uma possibilidade de associação, não uma medida de familiaridade do público. |
| **Domínio da Energia** | Comunica domínio de uma prática e tem uma formulação ligada à ficção. | “Domínio” já é central em Expansão, Domínio Simples e outras regras. O verificador declara o composto livre, mas a colisão de associação é relevante. Não é minha preferência. |

**Minha preferência é Controle de Energia**, mantendo o nome completo onde “Controle” possa significar a Família. Se o grupo já associa Refino corretamente, manter Refino com uma boa definição é uma escolha válida; a revisão não precisa eliminar todo termo evocativo. [Priberam: refino](https://dicionario.priberam.org/refino).

Uma eventual decisão deve abranger o número da ficha e a escolha de progressão do mesmo nome. Lapidação continua fora desta rodada: é uma rota distinta e não deve ser arrastada para o novo nome automaticamente.

## Triagem executada e leitura humana

Executei `sistema/03-mecanica/conferir-nomes.py --candidatos` com os termos discutidos e alternativas de descarte. Duas execuções terminaram com código 0 e 44 avisos não bloqueantes nas checagens gerais; a triagem de candidatos informa riscos, não os transforma em reprovação do comando.

| Retorno da ferramenta | Interpretação para esta pauta |
|---|---|
| Fundamento e Refino: **OCUPADO** | Esperado: são os nomes atuais. Não constitui argumento para mantê-los nem para proibir uma revisão. |
| Técnica: **DENTRO**; Fundamento da Técnica: **DENTRO** | Técnica aparece em nomes compostos; Fundamento da Técnica contém o termo atual. É preciso preservar a distinção dos conceitos e revisar as frases. |
| Técnica Inata: **LIVRE** | Há ocorrências em prosa e, sobretudo, o problema semântico da rota Sem Técnica. Livre no catálogo não equivale a adequado. |
| Potência: **MORTO** | Nome provisório do tamanho do feitiço, substituído por Classe na v0.6. A presente pauta permite discutir sua retomada; não o reintroduz silenciosamente. |
| Círculo e Categoria: **LIVRE**; Categoria de Efeito: **DENTRO** | O composto contém “Efeito”, nome de Forma. A classificação proposta não é aquela Forma; ainda assim, deve aparecer inteira na explicação e nas tabelas relevantes. |
| Controle de Energia: **DENTRO** | Contém a Família Controle. A diferença de significado é clara quando o nome completo permanece; verificar o uso abreviado na mesa. |
| Domínio da Energia: **LIVRE** | A ausência de coincidência inteira não elimina o conflito de associação com Domínios. |
| Patamar: **LIVRE** | **Falso conforto:** a leitura complementar do livro encontrou Patamar como obra do Arquiteto. Descartado para esta pauta. [Fonte](</media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/manual/35-caminhos-e-trilhas.md:909>) |

Também foram sondados Escala (aviso de proximidade com Escama), Potência Passiva (contém Passiva) e Controle Amaldiçoado (contém Controle); não se tornaram opções finais. A cobertura do script inclui listas e documentos históricos; a checagem manual nas fontes vigentes é indispensável antes de publicar qualquer renome.

## O piloto pode avançar com os termos atuais

**Sim.** O primeiro piloto de abertura, mundo e funcionamento da mesa pode usar os nomes publicados, com uma definição concreta na primeira aparição. Exemplos de formulação para testar, sem trocar nomes:

- **Fundamento:** descreve a técnica e reúne as escolhas que orientam seus feitiços. Na rota Sem Técnica, essa base é construída a partir de uma aptidão.
- **Classe:** a escala de 0 a 7 que define pontos, custo e limites das aplicações. O nível do personagem determina quais Classes estão disponíveis.
- **Classe Passiva:** uma classificação separada, Livre/1/2/3, usada pelas Passivas e como referência para aptidões e Bênçãos; os custos e requisitos pertencem à regra de cada tipo.
- **Refino:** mede o controle da energia amaldiçoada. É um valor de 1 a 10 usado em requisitos e efeitos; PE registra a energia disponível.

Depois de o leitor entender o trecho, testar as alternativas de nome na mesma regra. Pedir que ele explique o que o campo representa e que escolha faria com ele. Registrar primeiro o entendimento espontâneo, depois o resultado após a explicação. Isso distingue um nome enganoso de uma explicação ruim.

O piloto não deve criar alias permanentes como “Classe/Potência” em toda linha: essa duplicação apenas transferiria a decisão ao leitor. Manter uma versão com nomes atuais e provas curtas separadas das alternativas. Após a escolha, revisar concordância, fórmulas, tabelas, índices, fichas e busca por nomes antigos em uma migração própria.

## Feedback de 03/10/2026

Leitor do usuário prefere chamar Passiva Livre de Fundamento. A sugestão foi registrada, sem substituição nesta rodada: Fundamento já nomeia a estrutura inteira da técnica. A revisão autônoma deve comparar os usos, escolher nomes inequívocos e registrar o mapa antes/depois. Incursor, Pugilista e Malabarista permanecem aprovados. Mão Firme tem colisão entre Aptidão e Passiva; Aviso entre Melhoria e Passiva.

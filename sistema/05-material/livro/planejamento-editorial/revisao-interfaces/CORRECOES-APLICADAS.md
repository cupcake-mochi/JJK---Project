# Correções aplicadas — antes, depois e motivo

Correções feitas em 04/10/2026 a partir da revisão das interfaces (`ACHADOS.md`). Só entrou o que diverge de um nome, custo ou remissão já aprovado em outro capítulo. Nenhuma regra nova, nenhum número de balanceamento mudou.

O mesmo conteúdo, com o hash de cada fonte antes e depois, está em `CORRECOES-APLICADAS.json`. Caminhos relativos ao planejamento editorial.

## Como foi conferido

- **Fontes editadas:** só as declaradas em `../consolidacao/lote-01/ORDEM.json`. O `LIVRO-COMPLETO.md`, o PDF e as evidências da consolidação foram regerados pelo `gerar_livro.py --strict`, não editados à mão.
- **Estrutura:** `conferir_livro.py` passou com as 3492 checagens e os 508 links internos. O PDF continua com 383 páginas, 21 capítulos e seis Caminhos.
- **PDF:** antes `44dfa941…`, depois `89f9057b…` (sha256 completo em `../consolidacao/lote-01/evidencias/GERACAO.json`).
- **Páginas:** a comparação por pixel entre o PDF anterior e o novo mudou 35 páginas: 10, 59, 87, 96, 97, 113, 116, 117, 152, 175 a 189, 214, 218, 257, 263, 281, 283, 284, 340, 360, 376 e 378. As 35 foram olhadas uma a uma: nenhum corte de texto, sobreposição ou título órfão no pé da página. As outras 348 são idênticas em pixel ao PDF anterior. A faixa 175 a 189 é o capítulo de Equipamento: as trocas C04b, C07, C11 e C12 mudaram o comprimento de algumas linhas e o texto seguinte andou junto.
- **Texto do PDF:** os termos removidos ("Restringido", "Restrição Único", "Montagem de entidades") não aparecem mais, e cada "depois" abaixo aparece no texto extraído.
- **Links:** os destinos internos do PDF foram conferidos pelo `conferir_livro.py`; nenhum destino ficou pendente.
- **Validador editorial:** `testar_editorial.py` passou nos 70 testes. O `conferir_editorial.py` sobre os 11 manuscritos alterados: ver a seção no fim.
- **Prova visual completa (V14):** `../consolidacao/lote-01/evidencias/FINAL-V14.json` continua apontando para o PDF anterior. A inspeção desta rodada cobriu só as 35 páginas que mudaram.

## As correções

### C01 · caminhos/emanador/lote-01/EMANADOR.md

Achados: G1-01, G4-08. Integridade é a reserva de alma das criaturas (Dano e recuperação). O estado de dano de um objeto é a Vida do objeto, em Equipamento.

- Antes: A arma continua sendo um item: munição, Integridade, propriedades e efeitos precisam ser registrados.
- Depois: A arma continua sendo um item: munição, Vida do objeto, propriedades e efeitos precisam ser registrados.

- Antes: Conserve Grau, Integridade e efeitos próprios compatíveis.
- Depois: Conserve Grau, Vida do objeto e efeitos próprios compatíveis.

- Antes: Cada uma mantém munição, Integridade e efeitos próprios separados.
- Depois: Cada uma mantém munição, Vida do objeto e efeitos próprios separados.

### C02 · caminhos/incursor/lote-01/INCURSOR.md

Achados: G3-01. "Restringido" não aparece em nenhuma outra fonte; Rotas, glossário e índice chamam esse personagem de Restrição Celestial sem energia.

- Antes: **Restringido.** Aplique o reforço
- Depois: **Restrição Celestial sem energia.** Aplique o reforço

### C03 · consulta/lote-01/CONSULTA.md

Achados: G3-08, G4-12. O índice já registra Leve como propriedade de arma, exigida por habilidades do Assassino; o glossário não acompanhou a sincronização R05.

- Antes: **Leve, Média e Pesada.** Nomes de faixas de preço e também de categorias de Condição. Consulte a tabela correspondente; pontos de montagem e PE não são a mesma conta. **Consulta:** Pontos e preços.
- Depois: **Leve, Média e Pesada.** Nomes de faixas de preço e também de categorias de Condição. Consulte a tabela correspondente; pontos de montagem e PE não são a mesma conta. Leve também é uma propriedade de arma, explicada em Propriedades, no capítulo Equipamento. **Consulta:** Pontos e preços.

### C04 · regras-gerais/lote-final/REGRAS-GERAIS.md

Achados: G2-01, G4-14. Sete capítulos usam Ação Completa (46 ocorrências) e o glossário e o índice mandam procurar esse nome em Turnos, onde só aparecia Rodada inteira. O glossário mantém Rodada inteira como nome anterior.

- Antes: Um custo de **Rodada inteira** consome Ação Padrão
- Depois: Um custo de **Ação Completa** consome Ação Padrão

### C04b · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-14. Mesmo motivo de C04.

- Antes: cada **Rodada inteira** dedicada a vestir
- Depois: cada **Ação Completa** dedicada a vestir

### C05 · consulta/lote-01/CONSULTA.md

Achados: G2-09. O capítulo se chama Construir invocações (ORDEM.json); Montagem de entidades não é título de nenhuma fonte.

- Antes: | Domar | Montagem de entidades: Domar uma maldição |
- Depois: | Domar | Construir invocações: Domar uma maldição |

- Antes: | Entidade | Montagem de entidades: Criar uma invocação |
- Depois: | Entidade | Construir invocações: Criar uma invocação |

- Antes: | Invocação | Montagem de entidades: Adquirir entidades |
- Depois: | Invocação | Construir invocações: Adquirir entidades |

### C06 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achados: G4-02. Equipamento trocou o contador X pela capacidade (Ataques por carga) e pelo gatilho de esvaziar; a Vanguarda ainda usava X. A regra não muda.

- Antes: O limite **X de disparos antes da recarga aumenta em um**.
- Depois: A **capacidade da arma** (os ataques por carga, em Munição) **aumenta em um**.

- Antes: Recupere **metade de X, arredondada para baixo**, sem ultrapassar o limite.
- Depois: Recupere **metade da capacidade, arredondada para baixo**, sem ultrapassar o limite.

- Antes: recuperando **uma unidade de munição**, até a capacidade X.
- Depois: recuperando **uma unidade de munição**, até a capacidade da arma.

- Antes: resolve a necessidade normal de recarga por X ou pelo gatilho natural.
- Depois: resolve a necessidade normal de recarga por esvaziar a arma ou pelo gatilho natural.

### C07 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-03. Guia, Emanador, Evocador e a criação oferecem treino numa arma específica; lida ao pé da letra, a regra de Equipamento impunha desvantagem a esse treino.

- Antes: **Sem treino na categoria**, você tem desvantagem nos ataques com aquela arma.
- Depois: **Sem treino na categoria ou naquela arma específica**, você tem desvantagem nos ataques com aquela arma.

### C08 · caminhos/vanguarda/lote-01/VANGUARDA.md

Achados: G4-04, G5-03, G5-04. Não existe seção Compras e equipamento inicial; a regra está em Equipamento inicial.

- Antes: Compre seu equipamento conforme **Compras e equipamento inicial**.
- Depois: Compre seu equipamento conforme **Equipamento inicial**, em Equipamento.

### C08b · progressao/lote-01/PROGRESSAO.md

Achados: G4-04. Mesmo motivo de C08.

- Antes: conforme **Compras e equipamento inicial**.
- Depois: conforme **Equipamento inicial**, em Equipamento.

### C08c · rotas/lote-01/ROTAS.md

Achados: G4-04, G5-03. Os destinos não existem; as seções são Sacar e guardar, Equipamento amaldiçoado e Talento Próprio.

- Antes: Sacar uma arma de reserva segue **Ações — Interagir com objetos**.
- Depois: Sacar uma arma de reserva segue **Sacar e guardar**, em Equipamento.

- Antes: Efeitos especiais de graus maiores seguem **Equipamentos amaldiçoados**.
- Depois: Efeitos especiais de graus maiores seguem **Equipamento amaldiçoado**.

- Antes: deve seguir **Catálogo de criação — Criar Talentos**,
- Depois: deve seguir **Catálogo de criação — Talento Próprio**,

### C08d · abertura/lote-01/ABERTURA-E-CRIACAO.md

Achados: G4-04. Carga é seção própria de Regras gerais; Equipamento já corrigiu a mesma remissão (EQ23).

- Antes: Modos diferentes de movimento, terreno e excesso de carga seguem Movimento.
- Depois: Modos diferentes de movimento e terreno seguem Movimento; excesso de carga segue Carga, em Regras gerais.

### C08e · catalogo/lote-01/CATALOGO.md

Achados: G5-04. Criar um efeito e Descanso e recuperação não são títulos das fontes vigentes.

- Antes: estão em **Criar um efeito**, no Fundamento.
- Depois: estão em **Efeitos próprios**, no Fundamento.

- Antes: Recuperar os pontos segue **Descanso e recuperação**.
- Depois: Recuperar os pontos segue **Descansos**, em Dano e recuperação.

### C09 · rotas/lote-01/ROTAS.md

Achados: G4-05. Equipamento organiza armas em 13 categorias e 3 listas; "grupo" não é termo dele. A peça 20 diz "três das treze categorias de arma".

- Antes: selecione **três grupos de armas diferentes** entre os grupos de Equipamento. Você recebe uma arma de cada grupo, todas de **grau 4**, e fica treinado nos três grupos,
- Depois: selecione **três categorias de armas diferentes** entre as categorias de Equipamento. Você recebe uma arma de cada categoria, todas de **grau 4**, e fica treinado nas três categorias,

- Antes: qualquer **arma amaldiçoada de um desses grupos**,
- Depois: qualquer **arma amaldiçoada de uma dessas categorias**,

- Antes: Assim, é possível escolher um grupo de Força e outro de Destreza.
- Depois: Assim, é possível escolher uma categoria de Força e outra de Destreza.

- Antes: Começa com uma arma de grau 4 de cada grupo.
- Depois: Começa com uma arma de grau 4 de cada categoria.

- Antes: | Selo | Usar uma arma amaldiçoada de um dos três grupos. |
- Depois: | Selo | Usar uma arma amaldiçoada de uma das três categorias. |

### C10 · invocacoes/lote-02/CONSTRUIR-INVOCACOES.md

Achados: G4-09. Equipamento define teto de Destreza zero para Revestimentos; a fórmula da entidade somava a Destreza inteira.

- Antes: a Defesa usa **10 + Destreza da entidade + proteção do equipamento**.
- Depois: a Defesa usa **10 + Destreza da entidade permitida pelo teto da peça + proteção do equipamento**.

### C11 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-15. No mesmo capítulo Rina tem Força 0, e o escudo Médio exige Força 3; pela regra de requisitos ela não receberia a proteção.

- Antes: Sua Defesa é 10 + 4 + 2 = **16**. Com um escudo Médio, recebe mais 2 de proteção, mas só pode contar 3 de Destreza: 10 + 3 + 2 + 2 = **17**.
- Depois: Sua Defesa é 10 + 4 + 2 = **16**. Com um Broquel, recebe mais 1 de proteção: 10 + 4 + 2 + 1 = **17**. Um escudo Médio exigiria Força 3; com ele, ela só poderia contar 3 de Destreza.

### C12 · equipamento/lote-final/EQUIPAMENTO.md

Achados: G4-13. Duas propriedades das tabelas de armas são explicadas fora da página Propriedades.

- Antes: | Propriedades | Benefícios e restrições, explicados em [Propriedades](#eq-propriedades). |
- Depois: | Propriedades | Benefícios e restrições, explicados em [Propriedades](#eq-propriedades); Volumosa e Embainhada estão em Armas escondidas. |

### C13 · caminhos/emanador/lote-01/EMANADOR.md

Achados: G5-01. Nenhuma fonte define Restrição Único; a Restrição de frequência do Catálogo é Uma Vez.

- Antes: como a Restrição Único.
- Depois: como a Restrição Uma Vez.

### C14 · progressao/lote-01/PROGRESSAO.md

Achados: G5-06. Fundamento diz que trocar função, Forma ou peças da Técnica Máxima usa a revisão ao subir de nível (FU-44), mas a lista de Progressão não a incluía.

- Antes: Você pode reescrever **um feitiço conhecido**, incluindo uma Liberação Máxima, ou rever
- Depois: Você pode reescrever **um feitiço conhecido**, incluindo uma Liberação Máxima, a **Técnica Máxima**, ou rever

## Validador editorial

| Situação (saída em `evidencias/`) | Achados do `conferir_editorial.py` nos 11 manuscritos |
|---|---|
| `main`, antes das correções | 5 (Incursor 2, Construir invocações 3) |
| Logo depois das correções | 60 |
| Depois de renovar a revisão de localização dos 6 manuscritos afetados | 5, os mesmos da `main` |

Os 55 achados novos não vinham do texto novo. Cada manuscrito tem um LOCALIZACAO-EDITORIAL.json, na pasta de evidências da unidade, com as citações de nomes de outros capítulos já revisadas, e essa revisão só vale para o hash exato do texto. Ao mudar uma palavra, o hash muda e as 55 exceções já aprovadas voltam a acusar. Todas as 55 coincidem, em termo e trecho, com exceções já revisadas.

Nos 6 manuscritos que estavam em dia na `main` (Abertura, Emanador, Vanguarda, Consulta, Progressão e Rotas), os trechos trocados foram relidos: só nomes e remissões ao capítulo dono, nenhuma regra de outro capítulo copiada e nenhum título mudado. A revisão foi renovada com o hash novo e um registro `revisao_delta_2026_10_04` em cada arquivo, que diz o hash anterior, as correções e que é revisão por modelo.

Os outros 5 (Incursor, Catálogo, Equipamento, Construir invocações e Regras gerais) **já estavam com a revisão desatualizada na `main`**: o hash registrado não batia com o texto antes desta rodada, e o modo de exportação (`require_review`) acusa E004 e E006 neles nas duas versões. Eles não foram renovados aqui, porque renovar pede releitura do capítulo inteiro e não só dos trechos trocados. Fica como pendência anterior a esta rodada.

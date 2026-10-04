# Fundamento — última leitura da Técnica Máxima

Data: 2026-10-03. Auditoria localizada, sem alteração de arquivos do projeto.

## Versão conferida

Diretório: `sistema/05-material/livro/planejamento-editorial/fundamento/lote-01`.

- `FUNDAMENTO.md`: SHA-256 `01ce58f4da94c1b9b92d85dd455e2c86593e93679ac57834408fc39426a1f195`.
- `CONTRATO.json`: SHA-256 `9de4b2d2feec18d49f4ea6af0446edee1fe5e729b15c24f87c6d47d8dff15a1e`.
- `auditar.py`: SHA-256 `28858c09d119fe187bc73f06fe0d63e1eaa7d43ab2e5318fed16b99dcde564c4`.
- `sincronizacoes/40-CATALOGO.md`: SHA-256 `eea4e32024b441f45a0b0674bb8b9b1406664b6b9016a13e0bb16b513be45b45`.
- Fonte publicada `sistema/05-material/livro/manual/40-fundamento.md`: SHA-256 `8ec6cd54f8fbb0cc7e98874a5242890a3b3392a792ec1cdef959abcec4b70d96`.

O hash do manuscrito permaneceu o mesmo entre a leitura inicial e a conferência final. O contrato contém esse hash e o hash correto da fonte de custos.

## Resultado

Não encontrei bloqueador de uso nas seções Técnica Máxima, Ataque/cura/utilidade, Melhorias da Técnica Máxima, Passagem de Papel e Retirada de Emergência. A divergência encontrada no modelo de validação foi corrigida pelo agente principal e a correção foi reconferida. **Não resta bloqueador concreto identificado neste escopo.**

### B1 — corrigido: auditor rejeitava Precisão com TR

- Na primeira leitura, `auditar.py:116` rejeitava resolução por TR quando as peças incluem `Precisão`, junto de Rajada, Certeiro e De Novo.
- A fonte `manual/40-fundamento.md:639` permite Precisão como **+2 na rolagem de acerto ou +2 na CD do TR**.
- `FUNDAMENTO.md:774` conserva Precisão pelos próprios requisitos. A seção Conjurar permite registrar uma versão por TR.
- `sincronizacoes/40-CATALOGO.md` não revoga a alternativa de CD de Precisão.

**Contraexemplo reproduzível:** Máxima de nível 17, Forma Projétil, resolução por TR, Precisão neutra. Custo de montagem 0 + 3 = 3 dos 8 pontos, uma Melhoria. É uma montagem permitida pela regra, mas o auditor original retornava `False` para `valid('Projétil', ['Precisão'], mode='maxima', resolution='TR')`.

**Correção confirmada:** o agente principal retirou somente `Precisão` da exclusão de peças para TR e acrescentou um caso positivo de Precisão modificando CD. A reexecução independente em memória retorna `True` para o contraexemplo de Máxima acima. Rajada, Certeiro e De Novo conservam seus requisitos de ataque. Não foi alterada a regra de Precisão nem o manuscrito.


## Conferências sem contradição encontrada

- **Tabela e contas:** 24/28/32d8, orçamento 8/12/16, PE 25/30/35. O custo do Efeito Próprio Pesado é 8/9/11 e cabe em todas as faixas. Pontos e dados são separados.
- **Monotonicidade:** enumeração de 840 perfis de preço preserva os 68 perfis acessíveis na Classe 5 ao passar para 6 e os 133 acessíveis na Classe 6 ao passar para 7. Perdas zero em ambas as transições. Os orçamentos 12 e 16 são os mínimos desse modelo para preservar todas essas escolhas. Isso é aumento de largura nas faixas altas, não prova de equilíbrio global.
- **Fenda de Arrasto:** Projétil + Passo Livre + Empurrão Livre custa 0 + 1 + 1 = 2; conserva 24d8 e 25 PE. O deslocamento específico de Passo não devolve a Ação de Movimento. A regra de Lento reduz a distância específica também.
- **Dano e repetições:** vedações de Salto, Queima, Estilhaço, Acúmulo, Remate, Quebra Coisa, Fica e Inescapável são expressas. Rajada/Mais Um repartem dados, áreas aplicam a mesma quantidade uma vez a cada alvo, e críticos/defesas permanecem gerais.
- **Certeiro:** exige ataque; metade dos dados do ataque que efetivamente errou, arredondada para baixo, sem efeitos de acerto ou crítico. De Novo antecede esse desfecho. Não foi reintroduzido dano automático sem ataque.
- **Junto:** somente repartição de cura ou benefício quantitativo compatível, sem copiar bônus/condições. O limite próprio de seis criaturas da Retirada continua explícito; Junto não remove esse limite.
- **Fica e duração:** Fica indisponível na Máxima. Concentrada/Duradoura não repetem dano nem reaplicam condição encerrada. A duração própria da Passagem é expressa e a Retirada é instantânea.
- **Passagem:** preparação e ativação distintas, duas marcas, limites de dimensões/distância/visão, concentração, interrupção, saída bloqueada e término antes do primeiro turno do combate. Não utiliza seus dados como cura nem compra mais efeitos com o saldo descartado.
- **Retirada:** seis aliados dispostos, seleção e destinos fixados no início, 18 m por trajeto, obstáculos e terreno cobrados, sem concessão de voo/escalada/teleporte, sem ações/ataques extras, sem desfazer contenção. Lento reduz o orçamento específico a 9 m; proteção contra ataques de oportunidade permanece. Longe altera a seleção, não cada percurso. Não há repetição por concentração.
- **Recarga e progressão:** uso na rodada 1, três turnos seguintes completados, novo uso na rodada 5 no exemplo normal. Atualizar orçamento não aumenta por si só as medidas das fichas próprias, nem permite reescolher montagem a cada uso.

## Execução do auditor sem escrita

O script foi carregado em memória com AST. Somente a função `dump`, que escreve JSON, foi substituída por armazenamento num dicionário em memória. O restante do auditor foi executado com seu `__file__` original para ler as mesmas fontes. Não foram executadas as gravações de evidências nem de CONTRATO.json.

Resultado: **65 verificações numéricas/textuais, 39.032 estados de orçamento e 41 casos funcionais passaram**. Após normalizar a serialização JSON (chaves numéricas viram texto), o CONTRATO gerado em memória coincide integralmente com o arquivo existente. Na primeira execução, os 40 casos existentes não detectavam B1. A revisão acrescentou o caso positivo ausente; os 41 casos da versão corrigida passaram. Isso evidencia por que o resultado automatizado precisa ser lido dentro do conjunto de casos efetivamente coberto.

## Limites

- Leitura localizada dessas cinco seções, com consulta aos procedimentos comuns, preços, requisitos e patches necessários à comparação. Não é revisão completa do catálogo, do livro ou da folha diagramada.
- Não executei combate, Bloquear, fichas completas, mapas reais ou sessões com jogadores. Passagem e Retirada continuam efeitos candidatos que precisam de teste de mesa.
- Os perfis de custo são um superconjunto de preços; não equivalem a 840 feitiços semanticamente válidos nem avaliam valor tático.
- O modelo `valid()` cobre um subconjunto deliberado de compatibilidades. Passar nele não autoriza uma peça a ignorar seus requisitos nem certifica qualquer combinação restante.
- Não fiz nova verificação de cânone: as duas fichas de utilidade se apresentam como criações originais do projeto.
- Nenhuma nova proposta de design ou balanceamento foi introduzida nesta leitura. A correção B1 apenas fez o auditor corresponder à regra existente.

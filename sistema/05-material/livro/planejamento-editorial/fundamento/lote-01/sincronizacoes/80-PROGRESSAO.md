# Sincronização candidata — 80-experiencia-e-progressao.md

**Estado:** revisão para aplicação futura junto de Fundamento, lote 01. A fonte publicada permanece intacta. Os números de linha são da fonte inspecionada; a âncora e o trecho anterior devem ser conferidos antes da integração.

Fonte: `sistema/05-material/livro/manual/80-experiencia-e-progressao.md`.
SHA-256 da fonte: `11943325cbd9887c2fb6d312df0ec52f70eab50440d9f9bb12a080a9d2e8e24e`.

A autorização atual permite a troca de espaço por entidade nas três rotas, somente quando seu funcionamento prevê invocações. Os nomes atuais Manejo/Kata são preservados; revisão geral de nomes pertence à fila própria. Os trechos de Máxima dependem da versão consolidada do novo procedimento em Fundamento e não devem ser aplicados isoladamente.

## PR-01 — ### Colunas de progressão, entrada espaços de feitiço

- **Fonte:** linha 281.
- **Tipo:** Sincronização da contabilidade.
- **Motivo:** A antiga lista não incluía entidades e sugeria que cada espaço sempre era um feitiço..

**Antes**

```markdown
- **espaços de feitiço** é o tamanho da sua lista de feitiços conhecidos, e é a coluna que responde "quantos feitiços eu tenho agora?". Passiva é paga com espaço, e a Expansão de Domínio também. Liberação Máxima não ocupa.
```

**Depois**

```markdown
- **espaços de feitiço** é a capacidade da sua lista de criações conhecidas. Feitiços, Passivas pagas, Expansão de Domínio e entidades adquiridas por espaço dividem essa capacidade. Manejos e Katas usam a mesma conta. Classe 0, Liberação Máxima e Técnica Máxima ficam fora dela.
```

## PR-02 — ### Feitiços por nível, parágrafo após explicação dos marcos

- **Fonte:** linha 293.
- **Tipo:** Sincronização da aquisição e decisão conservadora de revisão.
- **Motivo:** Inclui entidades sem alterar a fórmula nem a progressão. Remete aos donos para preservar uma regra única e explicita que espaços dos marcos não são separados..

**Antes**

```markdown
Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também: as três saem desta mesma coluna.
```

**Depois**

```markdown
**Requisito:** invocações precisam estar previstas no funcionamento declarado da técnica ou do estilo. A Descrição e a Regra, ou a semente e o equipamento da rota, devem explicar como a entidade é criada, chamada ou controlada. Sem essa capacidade, a troca não está disponível; possuir um espaço não concede invocações por si só.

Todos os espaços desta conta, inclusive os recebidos nos marcos, pertencem à mesma lista. Eles podem ser ocupados por feitiços, Passivas pagas, Expansão de Domínio ou entidades, com os custos de cada opção. **Na regra comum, um espaço permite obter uma entidade**, conforme **Invocações — Aquisição**; a opção também vale para Manejo e Kata.

Ao subir de nível, você pode revisar **um espaço já ocupado**, reescrevendo seu feitiço ou refazendo a troca por entidade. Preencher um espaço novo não gasta essa revisão. Os procedimentos completos estão em **Fundamento — Feitiços conhecidos** e **Invocações — Aquisição**.
```

## Verificação de integração

- Conferir que cada trecho anterior ocorre uma única vez na fonte indicada.
- Aplicar junto da regra central equivalente de Fundamento e conferir as remissões.
- Conservar as exceções expressas nos seus capítulos; não reproduzir habilidades de Trilha aqui.
- Revalidar a contabilidade de espaços e os exemplos após a integração.
- Os custos e os dados reduzidos da entidade não passam a usar automaticamente a tabela do jogador.

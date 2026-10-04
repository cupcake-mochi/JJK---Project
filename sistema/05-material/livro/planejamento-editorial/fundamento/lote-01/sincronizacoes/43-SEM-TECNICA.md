# Sincronização candidata — 43-sem-tecnica.md

**Estado:** revisão para aplicação futura junto de Fundamento, lote 01. A fonte publicada permanece intacta. Os números de linha são da fonte inspecionada; a âncora e o trecho anterior devem ser conferidos antes da integração.

Fonte: `sistema/05-material/livro/manual/43-sem-tecnica.md`.
SHA-256 da fonte: `bf4296c61b167717bffc98459ba26bce8c1b0a46fc8de1230df833486b8c70b7`.

A autorização atual permite a troca de espaço por entidade nas três rotas, somente quando seu funcionamento prevê invocações. Os nomes atuais Manejo/Kata são preservados; revisão geral de nomes pertence à fila própria. Os trechos de Máxima dependem da versão consolidada do novo procedimento em Fundamento e não devem ser aplicados isoladamente.

## ST-01 — Inserir antes de ### `Auge`

- **Fonte:** linha 23.
- **Tipo:** Sincronização da aquisição.
- **Motivo:** Manejo herda feitiço em qualquer capítulo, mas a opção por entidade está invisível na criação. A regra completa permanece em Invocações..

**Antes**

```markdown
### `Auge`
```

**Depois**

```markdown
### Invocações

**Requisito:** invocações precisam estar previstas no funcionamento declarado da técnica ou do estilo. A Descrição e a Regra, ou a semente e o equipamento da rota, devem explicar como a entidade é criada, chamada ou controlada. Sem essa capacidade, a troca não está disponível; possuir um espaço não concede invocações por si só.

Você pode ocupar **um espaço de Manejo com uma entidade**, em vez de um Manejo conhecido. A aquisição, a progressão da entidade e a troca ao subir de nível seguem **Invocações — Aquisição**. A entidade precisa ser coerente com sua semente e sua Regra; entrada e habilidades conservam seus próprios custos.

### `Auge`
```

## ST-02 — ### `Auge`, primeiro parágrafo

- **Fonte:** linha 25.
- **Tipo:** Sincronização do procedimento e clareza.
- **Motivo:** Substitui definição exclusivamente ofensiva por remissão ao procedimento completo revisado, sem repetir sua tabela..

**Antes**

```markdown
**`Auge`** — o golpe de dano fixo, do nível 17 em diante. **Dano pela faixa de nível, orçamento de montagem à parte, `5 × maior Classe` de PE**, e não aceita Restrição.
```

**Depois**

```markdown
**`Auge`** — a aplicação máxima do seu Manejo, disponível a partir do nível 17. Crie e use seu Auge pelo procedimento de **Fundamento — Técnica Máxima**, escolhendo um resultado compatível com sua semente e sua Regra. A mesma seção define orçamento, custos, limites e recuperação.
```

## ST-03 — ### `Energia Reversa`, aviso posterior à apresentação

- **Fonte:** linha 74.
- **Tipo:** Correção de sincronização de regra já registrada.
- **Motivo:** A peça 25, linhas 185–187 e 284, registra desde v0.194 que o bloqueio é da aptidão inicial. Manejo com Forma Cura pode curar terceiro. Evita exigir Trilha específica para toda cura e retirar a função de Amparo..

**Antes**

```markdown
> **Curar os outros não entra na criação.** É o degrau raro do material, e ele mora numa Trilha do Guia, no capítulo 8, *Caminhos e Trilhas*. Quem quiser isso paga uma Trilha inteira, como qualquer um.
```

**Depois**

```markdown
> **A aptidão inicial cura você.** Para curar outra pessoa, você pode criar um Manejo com a Forma `Cura`, se sua Regra permitir e Amparo estiver disponível. Esse Manejo ocupa espaço na lista e paga os custos normais. Curar terceiros diretamente pela aptidão exige a permissão específica das regras de Energia Reversa.
```

## ST-04 — ### Sutura Fria, parágrafo final

- **Fonte:** linha 142.
- **Tipo:** Correção de sincronização de regra já registrada.
- **Motivo:** O exemplo repetia o bloqueio incorreto. Distinguir bônus da semente em cura própria, Manejo Cura em terceiro e acesso separado pela aptidão..

**Antes**

```markdown
A cura dele soma `1/3 do refino`, pela seção *Cura*. Curar os outros ele não faz: para isso ele precisaria do Guia e da Trilha que entrega aquilo, como qualquer um.
```

**Depois**

```markdown
Nas curas que recebe por suas próprias habilidades, ele soma o bônus da seção **Cura**, respeitando as regras dessa seção. Com Amparo disponível, pode criar um Manejo de `Cura` para outra pessoa e pagar seu espaço, ação e PE normalmente. O bônus da semente não se aplica a essa cura em terceiro.
```

## Verificação de integração

- Conferir que cada trecho anterior ocorre uma única vez na fonte indicada.
- Aplicar junto da regra central equivalente de Fundamento e conferir as remissões.
- Conservar as exceções expressas nos seus capítulos; não reproduzir habilidades de Trilha aqui.
- Revalidar a contabilidade de espaços e os exemplos após a integração.
- Os custos e os dados reduzidos da entidade não passam a usar automaticamente a tabela do jogador.

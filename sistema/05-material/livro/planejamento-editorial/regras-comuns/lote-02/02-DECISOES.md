# Movimento: revisão 3

02/10/2026, sobre a v0.331. O usuário aprovou a escrita e pediu uma base mais simples, inspirada em D&D, adaptada ao sistema, sem distribuir os apoios de Parkour e com distâncias em múltiplos de 1,5 m. Esta revisão aplica essa direção na amostra; não altera o livro jogável.

A [versão anterior](../historico/lote-02-r1/LEIA-ME.md) está preservada. Seus M07–M22 não são a lista de decisões ativa: os itens abaixo substituem o desenho, inclusive onde uma compatibilidade foi mantida. [Texto atual](02-SALTOS-E-QUEDAS.md).

## Revisão funcional de 02/10/2026

A revisão 2 foi preservada em `../historico/lote-02-r2/`. R01–R10 continuam vigentes nesta candidata, com dois complementos: **R11**, saltos curtos dentro de terreno difícil mantêm seu custo; só ultrapassar inteiramente um obstáculo rente ao chão e aterrissar em piso regular evita aquele obstáculo; **R12**, uma Ação de Movimento parcialmente usada para andar não pode pagar uma tarefa que exija a ação inteira. O contraexemplo de R11 era atravessar 9 m de entulho com seis saltos de 1,5 m, pagando metade do custo de caminhar. A correção conserva o salto que efetivamente passa por cima de um obstáculo isolado.

A unidade de 1,5 m continua proposta para a integração, sem alterar retroativamente alcances de habilidades nas fontes preservadas. A revisão integral de distâncias existentes é uma dependência da publicação.

## Antes e depois

| Antes | Agora | O que resolve |
|---|---|---|
| CD diferente a cada distância, inclusive saltos rotineiros | Capacidade por Força; teste só para extensão ou risco real | Permite decidir o percurso sem consultar uma escada de CDs. |
| Alturas de 0,5 m, 1 m, 2 m e 2,5 m | Distâncias em unidades de 1,5 m | Atende à escala solicitada para mapa e ficha. |
| Borda geral, alcance dos braços, custo de subir e Reação para segurar | Retirados; apoios especiais remetem ao Parkour | Preserva a identidade da habilidade e reduz procedimentos gerais. |
| Dano fixo e Acrobacia universal para amortecer | Dados de dano por altura, sem amortecimento geral em solo | Retoma a base simples de D&D e reduz rolagens sobre a mesma queda. |
| Sete páginas só de saltos/apoios/quedas | Quatro páginas incluindo movimento e terreno | Reúne a consulta básica; os bastidores ficam aqui. |

## Escolhas desta amostra

| ID | Regra candidata | Origem e consequência |
|---|---|---|
| R01 | Unidade de 1,5 m; distâncias calculadas arredondadas para baixo após modificadores | Direção do usuário; o critério de arredondar para baixo é nossa implementação. Não altera arredondamento de dano ou PE. Ainda será necessário varrer distâncias do livro na integração. |
| R02 | Custo 1,5/3/4,5 m por unidade conforme terreno/modalidade | Retoma o primeiro lote e a composição da referência. Deslocamento especial elimina o custo da modalidade, conservando terreno. |
| R03 | Impulso 3 m; salto horizontal 3 + 1,5 × Força; parado metade | Estrutura inspirada em D&D, fórmula própria para atributos 0–6. É mais generosa que uma conversão literal e valoriza cada ponto de Força. Não usar valor de atributo de D&D como se fosse nosso modificador. |
| R04 | Salto vertical com impulso 1,5 m (Força 0–4) ou 3 m (5–6); parado, 1,5 m automático apenas no segundo grupo | Conversão grossa para o mapa. Saltinhos no piso não são proibidos; superar o desnível inteiro pode exigir esforço. |
| R05 | Extensão única de até 1,5 m em um eixo, Atletismo CD 14; uma rolagem para o salto | Adaptação nossa. Mantém utilidade da troca por Acrobacia do Parkour sem alterar a Trilha. Distâncias acima disso exigem habilidade. Falha da extensão fica na capacidade normal. |
| R06 | Salto paga a maior distância entre horizontal/subida, com saldo antes da tentativa | Simplifica a soma de eixos anterior; não acrescenta Ação Padrão ou Bônus para rolar. Movimento disponível continua limitando o salto. |
| R07 | Queda 1d6 por 3 m completos, até 20d6; Derrubado se houver dano | Base D&D. A altura de 4,5 m dá 1d6. O teto permite que personagens avançados com Vida cheia sobrevivam a qualquer altura; isso é consequência assumida da proposta, não equilíbrio demonstrado. |
| R08 | Água profunda (3 m), Reação, Atletismo ou Acrobacia CD 14, metade do dano para cima | Adapta o procedimento 2024 à CD local e explicita profundidade. Não é mitigação universal em solo. |
| R09 | Deslocamento forçado e queda usam cenário real; sem fabricar ponto no ar; trecho imediato de 150 m em quedas longas | Compatibilidades mantidas da proposta anterior. O passo de queda longa é convenção local nesta amostra; não atribuído ao glossário de D&D consultado. |
| R10 | Limite acrobático por ciclo, momento de medir Recuperar a Base, dano da Projeção separado | Mantém interpretações candidatas do lote anterior. Não foram promovidas a regras aprovadas por estarem nesta revisão. Apoios do Parkour permanecem específicos. |

## Pesquisa e conferência

[Referências primárias](../lote-03/evidencias/referencias-dnd.md), [dúvidas públicas de leitores](../lote-03/evidencias/retorno-de-leitores-publicos.md) e [análise de escala](../lote-03/evidencias/escala-saltos-quedas.md). A prosa é própria. A direção usa a estrutura de D&D; outros livros não são uma razão para acrescentar subsistemas que o usuário pediu para simplificar.

O salto de Força 3 alcança 7,5 m com impulso, mais que a conversão conservadora da referência. Custa 10,5 m com a aproximação: não concede movimento gratuito. Parkour com Força 0 alcança 3 m sem teste e pode tentar 4,5 m com Acrobacia CD 14; +4 dá 55%, +7 dá 70%, +10 dá 85%.

Queda de 9 m causa 3d6: chance exata de zerar 14 de Vida = 35/216, cerca de 16,2%. O teto é 120 de dano, menor que os 182 de Vida do Incursor de nível 30 e Constituição 2. Essa tolerância no topo é visível e ficará para avaliação da mesa; não foi escondida elevando a CD com o nível.

Os benefícios existentes do Assassino e do Pugilista não foram reescritos nas fontes integradas. O teste humano continua pendente. A edição jogável permanece na v0.331.

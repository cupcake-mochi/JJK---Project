# Compatibilidades finais da Técnica Máxima

Revisão de 03/10/2026 para o procedimento candidato de Fundamento. Não modifica o manuscrito principal. A sincronização IN-03 foi atualizada separadamente em `sincronizacoes/60-INVOCACOES.md`.

## Critério adotado

A Máxima conserva os dados-base de sua faixa. Seu orçamento ampliado compra entrega e efeitos compatíveis, sem comprar dano adicional, cópia de dano ou multiplicação do dano. Este é um limite mecânico explícito da candidata; o publicado fixava dados-base, mas não esclarecia todas as interações abaixo.

Isso não remove os modificadores gerais de crítico, resistência, vulnerabilidade e Redução de Dano. Também não transforma a quantidade-base de uma Forma de área num reservatório global repartido entre todas as criaturas: o exemplo publicado da Linha aplica os dados a cada atingido. As peças de divisão têm uma instrução diferente e a obedecem.

## Matriz para o texto e o validador

| Peça ou grupo | Resultado na candidata | Limite que precisa ficar explícito |
|---|---|---|
| Salto | não entra na Máxima ofensiva | o original copia metade dos dados depois da primeira aplicação; não criar uma exceção de divisão nesta rodada |
| Queima | não entra na Máxima ofensiva | reaplica metade dos dados em outro turno |
| Estilhaço | não entra na Máxima ofensiva | cria dano adicional em outro alvo |
| Acúmulo | não entra na Máxima ofensiva | acrescenta dados e ainda pressupõe usos em rodadas consecutivas incompatíveis com a recarga normal |
| Remate | não entra na Máxima ofensiva | multiplica o dano contra alvo machucado |
| Quebra Coisa | não entra na Máxima ofensiva | multiplica dano contra objetos/estruturas; registrar que este limite também reduz essa especialização, não apenas dano contra criaturas |
| Fica de dano | não entra na Máxima ofensiva | permite aplicações persistentes e por entrada; a base alta não pode ser repetida |
| Inescapável | não entra na Máxima | não recebe a quantidade-base inteira sem ataque nem defesa; é vedação expressa nova, não inferência de que a peça já proibia Máxima |
| Rajada | permitida quando a entrega de ataque for compatível | divide os dados entre os tiros antes das rolagens; tiro sem dados não leva efeitos de acerto |
| Mais Um | permitido em uma montagem de alvos compatível | divide os dados disponíveis entre os alvos antes de resolver; não multiplica a base |
| Junto | permitido para cura ou benefício quantitativo que possa ser dividido | não entrega cura inteira a cada alvo nem multiplica bônus/efeitos indivisíveis; ver seção específica |
| Certeiro | permitido em uma ficha de ataque | **continua havendo ataque**; no erro final contra alvo válido, aplica metade dos dados atribuídos àquele ataque, arredondada para baixo; nenhum outro efeito, crítico ou reembolso de dados |
| Precisão, Fura, Corrói, De Novo, Rasga Escudo e Sem Cura | permitidos, com seus requisitos | não adicionam dados; melhorar confiabilidade/atravessar defesa não equivale a ignorar o preço ou os limites dessas peças |
| Toca a Alma | permitido com requisito de tema e demais regras próprias | metade dos dados, arredondada para baixo; não devolve orçamento. Integridade permanece pendente de revisão |
| Condições e Controle | permitidos conforme a montagem | oposição e término preservados, uma Pesada por ficha; nenhum bônus de Controle comum concedido automaticamente por renunciar aos dados fixos |
| Passo e outros movimentos específicos | permitidos | fornecem apenas seu movimento definido, mesmo após consumir Ação Completa; não devolvem ação de movimento nem concedem locomoção ausente |
| Rápido e Reação | não substituem a Ação Completa | Máxima não muda sua economia de ação por essas peças |
| Restrições, inclusive Corpo a Corpo embutida | nenhuma devolução | Toque/Aura preservam a entrega, sem recuperar pontos |

## Junto: a autorização da fonte é limitada

Fonte: `sistema/05-material/livro/manual/40-fundamento.md`, linha 799. Junto acrescenta um aliado à **cura ou ao apoio**, dividindo o efeito, e permite duas compras. Não afirma que duplica automaticamente qualquer estado aplicado a um aliado.

**Caso autorizado e suficiente para o livro:** Máxima de Cura de 24d8 com Junto pode distribuir os 24d8 entre dois aliados, por exemplo 12d8 e 12d8. Duas compras podem chegar a três aliados, com 8d8 para cada um. As divisões são declaradas antes das rolagens. Um aliado não recebe o total novamente porque outro não precisava de tanta cura.

**Apoio na candidata:** Apoio da Máxima não cria PV temporários a partir de dados nem de pontos restantes. Portanto, usar Apoio + Guarda + Junto não fornece automaticamente +2 de Defesa aos dois aliados. Não inventar divisão de condição, duração ou bônus sem que a montagem tenha um procedimento para ela. Se um Efeito Próprio estabelece uma quantidade compartilhável de proteção, Junto só se aplica quando a compatibilidade estiver expressamente definida; ele divide essa quantidade e nunca copia.

**Não aplicar Junto para multiplicar o pacote de Retirada de Emergência.** A retirada tem limite próprio de seis criaturas e trajetos definidos; não é uma quantidade de cura/PV a repartir. Onda também não precisa de Junto para alcançar mais um aliado já contido na área. Uma compra sem função não deve ser vendida ao jogador.

## Fica sem dano: não conceder permanência universal

Há dois usos diferentes na fonte:

1. A entrada de Área (`40-fundamento.md:624`) mantém uma área e entrega metade do dano a quem entra ou começa ali. A candidata corrigiu a sequência, mas continua dizendo que os outros efeitos não se reaplicam por Fica. **Com zero dano, essa entrada não compra uma série de aplicações gratuitas de Controle.**
2. Em Forma Efeito fora de combate (`40-fundamento.md:929`), Fica estende a duração para o próximo degrau da tabela. A linha Máxima já era a última e usava “até alguém desfazer”. **Não existe um próximo degrau publicado acima da Máxima.** Na candidata o encerramento passa a ser definido na própria ficha, também sem um degrau numérico superior automático.

Recomendação: **Fica não tem uso genérico na Máxima sem dano apresentada neste lote.** Retirada de Emergência é instantânea, logo não pode ser repetida ou sustentada por Fica. Passagem de Papel já possui duração e encerramento próprios; Fica não os substitui. Uma Máxima futura que mantenha uma área sem dano deve trazer esse funcionamento em seu Efeito Próprio e passar por aprovação, sem alegar que a entrada antiga concedeu gratuitamente a permanência.

Isso evita uma proibição temática abstrata de “efeitos duradouros”, mas impede usar a palavra Fica para reaplicar estados, repetir movimento ou prolongar indefinidamente a passagem. O validador deve responder **“sem aplicação compatível nesta montagem”**, em vez de aprovar a compra e descobrir o resultado durante a sessão.

## Certeiro e distribuição de dados

A decisão vigente da candidata muda a peça antiga, que removia o ataque e trocava por TR. No novo procedimento:

- Ataque válido é feito normalmente. Só seu resultado final decide se houve acerto ou erro.
- De Novo, quando permitido e gasto, oferece nova rolagem após errar; não causar a parcela de Certeiro antes da nova tentativa. Dois erros do mesmo ataque não aplicam metade duas vezes.
- No erro, arredonde para baixo **a quantidade de dados**, não o resultado já rolado do dano. Numa Máxima comum de 24d8, o erro de um ataque único causa 12d8; numa domada de 19d8, causa 9d8.
- Se Rajada dividiu 24d8 em seis tiros de 4d8, o erro de um deles com Certeiro aplica 2d8 daquele tiro. Não aplica 12d8 pela faixa da Máxima nem devolve os outros dados a outro tiro.
- Certeiro não aplica condição, movimento hostil, marca de acerto ou outros efeitos no erro. Não faz um alvo inexistente, fora de alcance, oculto por obstáculo total ou incompatível receber dano.
- Em uma montagem com TR, Certeiro não se aplica. O sucesso no TR da Máxima segue seu resultado próprio de **três quartos do dano recebido**, com o arredondamento do capítulo de Dano. Não substituir por metade dos dados de Certeiro.

## Toca a Alma e críticos

Toca a Alma troca o conjunto inicial pelo conjunto reduzido. Se uma domada tem 19d8, a montagem fica com 9d8 na alma antes de outros procedimentos. O erro de Certeiro sobre esse conjunto, se os requisitos de ambos forem satisfeitos, usaria 4d8. Não fazer a metade voltar a 19 ou 24 por consultar outra tabela no meio da resolução.

Um ataque que erra não é crítico. Ataques que acertam e são críticos seguem a regra geral vigente; a proibição de comprar dados por Melhorias não remove crítico por omissão. Toca a Alma continua exigindo o tema apropriado e respeitando as suas regras de Integridade. A revisão futura de Integridade/Morrendo pode alterar efeitos, resistências e consequências, portanto este lote não certifica sua letalidade final.

## Texto enxuto pronto para o capítulo

> **Peças da Máxima.** A quantidade de dados vem da tabela. Pontos e Melhorias não compram dados adicionais, multiplicam o dano nem o aplicam novamente. Salto, Queima, Estilhaço, Acúmulo, Remate, Quebra Coisa e Fica de dano não entram nesta montagem. Inescapável também não entra.
>
> Rajada e Mais Um repartem os dados antes da resolução. Junto reparte a cura ou outro benefício quantitativo expressamente compatível; não duplica condições ou bônus. Dados que não forem aplicados não passam para outro ataque ou alvo.
>
> Certeiro mantém a rolagem de ataque. Num erro final contra um alvo válido, causa metade dos dados daquele ataque, arredondada para baixo, sem os demais efeitos e sem crítico. As peças de acerto, defesa e movimento continuam obedecendo a seus requisitos. Toca a Alma reduz os dados pela metade. Críticos e as defesas do alvo seguem suas regras normais.
>
> Uma Máxima sem dano precisa ter a duração de seu efeito definida. Fica não repete seus estados ou movimentos nem prolonga automaticamente uma duração própria.

Se for necessário reduzir o bloco, mover a lista detalhada para uma tabela de compatibilidade. Não abreviar “metade dos dados” para “metade do dano”, pois isso produziria uma regra diferente.

## Casos mínimos de validação

| Entrada | Esperado |
|---|---|
| Máxima24d8 + Queima/Salto/Estilhaço | rejeitada |
| Máxima24d8 + Remate/Quebra Coisa | rejeitada sob a política candidata |
| Máxima32d8 + Inescapável | rejeitada |
| Máxima24d8, Rajada em seis tiros de4d8 | aceita quanto à conta; soma24 |
| Dois tiros erram e tentam reaproveitar8d8 | rejeitada a redistribuição |
| Rajada4d8 com Certeiro, erro final |2d8, sem efeitos adicionais |
| Ataque24d8 com Certeiro e De Novo: erro, depois erro |12d8 uma única vez |
| Domada19d8 com Certeiro, erro |9d8 |
| Domada19d8 + Toca a Alma |9d8 na alma; com Certeiro no erro,4d8 |
| Cura24d8 + Junto:12d8/12d8 | aceita |
| Cura24d8 + duas compras Junto:8/8/8 | aceita quanto à conta e quantidade |
| Cura24d8 + Junto:24/24 | rejeitada por duplicação |
| Apoio sem PV + Guarda + Junto: +2Defesa para dois | não autorizado por Junto; precisa de outra montagem |
| Retirada + Junto: sete participantes | rejeitada |
| Retirada + Fica:18m por turno | rejeitada |
| Passagem de Papel + Fica: dura até ser desfeita | rejeitada a extensão automática |
| Máxima de controle sem dano + Fica: condição nova a cada entrada | rejeitada a reaplicação |
| Passo6m junto de Ação Completa | movimento específico permitido, sem devolver ação |
| TR da Máxima bem-sucedido |3/4do dano segundo procedimento de Dano, não Certeiro |
| Linha24d8 atinge três criaturas | base por alvo da Forma, conforme política declarada; não é Mais Um |

## Sincronização IN-03 concluída

Foi conferido o SHA-256 da fonte `60-invocacoes.md`: `4df82e672d063b4d4bfe3394d93bb75052ec3e07d44d90b83c0ea32f10439f82`.

A fonte mantém **19d8/22d8/26d8** nas faixas17–20/21–25/26–30. A candidata de sincronização agora declara orçamento **8/12/16**, usa o nível da domada e remete as incompatibilidades ao procedimento central. Preserva PE25/30/35, divisão com reserva e Ação Completa do invocador. A identidade da domada e a regra de conservar seu nível permanecem com seu capítulo.

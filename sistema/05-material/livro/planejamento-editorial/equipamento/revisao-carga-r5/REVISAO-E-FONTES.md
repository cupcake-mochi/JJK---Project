# Calibração de proteção, itens comuns e corpos

03/10/2026. Complemento após o catálogo amaldiçoado. Candidatas novas, sem modificar fontes anteriores ou o livro v0.331. Examinaram-se todas as nove proteções e treze linhas de itens comuns; foram alterados três Volumes.

| Peça | Antes | Agora | Motivo |
|---|---|---|---|
| Traje 1 | 0,1 | 0,3 | Uniforme completo deixa de equivaler a um acessório mínimo. Compatível com roupas comuns completas do novo catálogo. |
| Broquel | 0,1 | 0,5 | Escudo de uma mão exige espaço e transporte próprios; continua mais portátil que Médio/Torre. |
| Cantil, 1,5 L | 0,2 | 0,3 | Água cheia precisa de carga relevante, sem tornar suprimento básico impraticável. Vazio mantém o valor por simplicidade. |

Mantidos Trajes 2/3 em 1/2; Revestimentos 1/2/3 em 2/3/4; escudos Médio/Torre em 1/2. Proteção, requisitos de Força, limites de Destreza, ações e preços não mudaram. Os Trajes mais caros continuam ocupando carga maior; não se presumiu aumento de Defesa universal, pois há teto e defesa por energia a comparar.

Mantidos corda, pé de cabra, kit de escalada e ferramentas de ofício em 0,5: representam objetos compridos/enrolados ou conjuntos, não pequenas peças isoladas. Lanterna, algema e mochila em 0,2; pilhas, gazuas, ração, telefone e bateria em 0,1. A mochila não reduz carga do conteúdo. Ração por pessoa/dia é simplificação de inventário, não equivalência em quilogramas. Esses limites merecem mesa, mas não surgiu motivo suficiente para aumentar todas as linhas.

## Pesquisa física e escolha de jogo

Um broquel de Wrexham no Met mede 36,2 cm e pesa 2,27 kg. É uma peça histórica específica, não uma média universal; confirma que um escudo pequeno não precisa ocupar o mesmo espaço de um telefone. [Met, broquel](https://www.metmuseum.org/art/collection/search/27942).

A Nalgene informa 134,75 g para seu recipiente de 48 oz vazio. Com água, um cantil desse porte transporta aproximadamente 1,5 a 1,7 kg, dependendo da capacidade e do recipiente. Isso orienta a revisão de 0,2 para 0,3; não fornece uma taxa universal de kg/Volume. [Nalgene, recipiente](https://nalgene.com/product/48oz-wide-mouth-ultralite-bottle/).

A corda Mambo 10,1 mm da Petzl tem 65 g/m; 15 m desse exemplo correspondem a 975 g, sem acessórios. A corda conserva Volume maior que o cantil por porte e transporte do rolo. Trata-se de âncora comparativa: a corda fictícia do catálogo não recebe especificações de segurança desse produto. [Petzl, Mambo](https://www.petzl.co.jp/professional/mambo-101/).

A diferença entre massa e Volume é deliberada. A calibração anterior de armas e munição permanece; uma arma não volta a pesar 7 Volume por aplicação de uma taxa física. Metralhadora em 4 e reserva em 0,5 continuam cobrando carga e manejo. Não houve pesquisa de campo presencial, teste de equipamento ou coleta com jogadores nesta rodada.

## Corpos

Mantidos 5 + Força para carregar e o dobro para arrastar/erguer. **12 kg por Volume passa a ser convenção exclusiva para o corpo de uma criatura.** Equipamento do carregado usa sua própria tabela e se soma ao do portador. Objetos sem valor usam comparação com o catálogo e avaliação do mestre; não recebem uma conversão geral disfarçada.

Com Força 0 e sem equipamento, corpo de 60 kg cabe; 61 kg não cabe. Força 2, dois Volumes próprios, corpo de 60 kg e mais um de equipamento somam oito: precisa redistribuir um. Um corpo de 72 kg com dois Volumes de equipamento total pede Força 3. Não arredondar na fronteira evita que frações virem capacidade gratuita. Transportar coletivamente, montaria e arrasto pesado ainda exigem seu procedimento próprio; esta rodada não os inventa.

## Conjuntos e regressões

| Inventário | Volume novo | Observação |
|---|---|---|
| Katana + Broquel + Traje 1 | 1,8 | Força 0 atende manejo e carga. |
| Hankyū + 20 flechas + Traje 1 | 1,8 | Força 0 atende. |
| Naginata + Traje 1 | 2,3 | Ainda exige Força 3 pelo manejo. |
| Pistola carregada + duas reservas + Traje 1 | 1,2 | Ainda exige autorização de aquisição. |
| Mochila + corda + lanterna + pilhas + cantil | 1,3 | ¥13.000; com ração, 1,4. |
| Katana + Broquel + Traje 1 + conjunto de exploração | 3,1 | ¥73.000, mantendo ¥77.000 do fundo padrão. |
| Metralhadora + duas reservas + Traje 1 + exploração | 6,6 | Força 3 dá capacidade 8; Força 0 não atende. |

O script lê tabelas e catálogo de armas, verifica preservação dos atributos de proteção e enumera 71.344 cenários de uma arma/proteção/escudo, Força/Destreza 0..6 e conjunto de exploração. Há 26.278 combinações utilizáveis nessa matriz, sem reservas adicionais de munição. A proporção **não é nota de equilíbrio**: muitos casos deliberadamente violam mãos ou requisitos. O resultado útil é identificar fronteiras, não garantir que qualquer escolha funcione em Força 0.

Broquel/Médio/Torre preservam trocas entre proteção, teto de Destreza, carga e Força; nenhum é melhor em todas as fichas. Não se atribuiu “eficiência de Defesa por Volume” universal a trajes e revestimentos: ignoraria custo, energia e situação do Traje. A dominância anterior de Revólver sobre Pistola no alcance continua pendente e separada.

`validar_carga.py` inclui casos de fronteira, inventário transferido, contas de exemplos e perturbações negativas. O PDF reúne somente os quatro blocos revisados, em 17 páginas com quatro grupos recolhidos. Não é uma nova exportação integral do livro. Armas, munição e seus preços mantêm os arquivos correntes registrados na fila.

## Próximo trabalho

**Perícias e Ofícios.** Conferir treino, escolha de atributo, tentativas repetidas, ajuda e ferramentas; depois fabricação/reparo, incluindo ferramentas amaldiçoadas. Continuam para conciliação final: Volumosa, Par com classes, situação de Traje, perda temporária de requisitos, preço/logística em mesa, alma e as decisões mecânicas listadas na fila. Morrendo permanece adiado.

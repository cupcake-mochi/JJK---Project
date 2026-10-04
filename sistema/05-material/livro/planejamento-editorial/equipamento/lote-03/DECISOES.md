# Decisões de Munição

Esta é uma proposta de regras e preços do Projeto M. Não representa preços de mercado, dimensões de fabricantes, legislação real ou capacidades reais de armas. A exigência de estoque, capacidade, preço e carga veio do usuário; os valores e procedimentos abaixo são escolhas desta candidata, não aprovação antecipada do usuário.

| ID | Escolha | Motivo e limite |
|---|---|---|
| M01 | Capacidade da carga em ataques: 1 para bestas; 2, 3 ou 4 para armas de fogo, conforme o X publicado. | Preserva o ritmo de recargas da base. Cartucho individual e unidade abstrata de disparo são distintos. Usar capacidades reais exigiria revisar o ritmo e fica fora desta escrita. |
| M02 | Uma unidade consumida em cada ataque, acertando ou errando. | Evita munição infinita, inclusive em ataques fora do turno. Arco usa uma flecha, besta um virote. |
| M03 | 1 ou 2 no dado mantido exige recarga, mas conserva unidades restantes. | Substitui a marca antiga de descarregada por precisa recarregar quando há sobra. Preserva o custo de ação. A regra não declara pane real, falha automática ou perda do ataque. |
| M04 | Ação Bônus completa ou prepara a arma; repõe apenas o transferido da reserva. | Mesmo sem reserva, pode preparar a sobra após 1/2. Uma arma vazia não passa a disparar sem munição. Recarga parcial tem só o número de disparos inseridos. |
| M05 | Carga instalada incluída no Volume da arma; reservas e recipientes extras contados separadamente. | Evita dupla contagem. Recipiente vazio mantém Volume por simplicidade. A régua é Volume, sem inventar pesos físicos em kg. |
| M06 | Cargas de fogo: ¥1.000/¥1.500/¥2.000/¥4.000 e 0,1 ou 0,2 Volume; flechas/virotes: 20 por ¥3.000 e 0,1. | Propostas ligadas à economia do livro: munição comum custa ¥500 por ataque; precisão/pesada, ¥1.000; flecha/virote ¥150. Não são preços reais. Não prova equilíbrio entre armas. |
| M07 | Compatibilidade por linha, sem trocar munição entre modelos só porque têm capacidade igual. | Arcos compartilham flechas, bestas compartilham virotes como convenção do jogo. Calibres/modelos especiais não estão definidos. |
| M08 | Transferência entre armas: Bônus para retirar, Bônus para colocar. | Não usar uma segunda arma como reserva com transferência gratuita. A recarga comum já cobre retirar/guardar a carga da própria arma; retirar de outra é etapa adicional. |
| M09 | Compra inicial inclui três cargas de fogo ou vinte flechas/virotes. | A Espingarda custa todo o fundo inicial de ¥150.000; sem provisão inicial, passaria a ser uma compra inutilizável. O fornecimento é único, na criação, finito e precisa de autorização da arma. Demais compras não renovam o benefício. |
| M10 | Recuperação de metade das flechas/virotes acessíveis, por tipo, uma vez para o grupo, após 1 minuto. | Procedimento inspirado na referência D&D; exclui munição de fogo, projéteis destruídos e inacessíveis. Sem segunda busca multiplicando a recuperação. |
| M11 | Quantidade restante substitui o antigo contador. | Não manter dois contadores redundantes. Com reserva suficiente e recarga completa, o ritmo de ações permanece; com reserva insuficiente ou recarga parcial, a arma pode esvaziar antes. |

## Interfaces para a integração

A candidata de Equipamento em jogo passou a lote-01-r3, sem a página antiga de recarga. As propriedades, categorias, dano, mãos, alcance, treino e preços das armas não mudaram. Munição de fogo usa o acesso da arma, sem criar nova afirmação jurídica sobre o Japão.

Catálogo de armas, compras e kit devem remeter a esta unidade. Sincronizar a ficha com quantidade na arma, reserva e estado precisa recarregar. Os procedimentos de manipulação, Ação Bônus e escudo continuam aplicáveis; não há exceção nova para Caminhos ou Trilhas. Testar interfaces específicas nos relatórios de seus donos.

## Referência efetivamente consultada

D&D Basic Rules 2024, Equipment, propriedades Ammunition/Loading e tabela Ammunition, página oficial consultada em 03/10/2026: https://www.dndbeyond.com/sources/dnd/br-2024/equipment . A referência organiza tipo, quantidade, recipiente, peso e preço, e cobra munição por ataque. Foi usada como exemplo de procedimento e consulta. Aqui o recipiente simples está incluído no item, os preços são em ienes fictícios, a recarga é a do Projeto M e o controle de fogo continua abstrato. Não se importou a restrição Loading de um ataque por ação, nem as capacidades de armas de D&D.

## Pendências e riscos

Preços, estoque inicial, logística e recuperação são candidatos a teste. Ainda não há evidência de que o custo mensal ou por missão seja adequado. Não existe taxa de missões/disparos estável para concluir isso. A vantagem dos Trajes foi revisada em unidade própria; não atribuir essa mudança ao lote de munição. Morrendo permanece adiado.

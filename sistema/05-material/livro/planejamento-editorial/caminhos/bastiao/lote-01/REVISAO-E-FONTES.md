# Revisão do Bastião

Candidata de 11 páginas, com todas as 19 habilidades do Caminho e das três Trilhas. Nomes preservados. Fontes publicadas não alteradas. O destino, o motivo e o tipo das 25 decisões estão em `ALTERACOES.json`; `COBERTURA.json` aponta cada entrega da fonte.

## Regras e funcionamento

A leitura comparou o integrado v0.331 com os contratos e o manual35. A publicação ainda passa em `conferir-catalogo.py`; esse resultado prova integridade da fonte antiga, não valida sozinho a candidata. O verificador local testa a candidata e os procedimentos necessários para executá-la.

Assumir ocorre antes do acerto, Bloquear depois, sem segunda Reação. Dano no erro não se torna acerto: Retaliação, Trocação e Casca não disparam por ele. Duro usa os dados que falharam, sem o modificador da Defesa. Casca usa dados próprios depois de um golpe interceptado que acertou. Não há novo Bloquear para o mesmo ataque.

Passa Pra Mim preserva1 depois das proteções do aliado. A transferência conserva tipos, não produz outro ataque e não reutiliza uma redução já aplicada em favor do aliado. Benefícios próprios ainda precisam proteger dano transferido; os que exigem ser alvo/acertado ou Bloquear o ataque original não entram. Dois exemplos, inclusive misto, acompanham casos executáveis. A ordem de consumo das parcelas mistas é esclarecimento geral novo, aprovado pelo root para sincronizar R03, sem atribuí-lo à publicação histórica.

Arrastão não recebe AtaqueExtra. O controle de Mão Pesada é reservado e pago antes dos ataques; o alcance excepcional da área não amplia o alcance de agarrar nem do golpe Bônus. Contra a Parede não ignora preparação, requisito, energia nem limite de conjuração do turno.

## Ensaio numérico

A enumeração cobre 216 perfis defensivos e 2.000 resultados de acerto/Bloquear por perfil, com convolução exata dos 100 resultados de Casca quando aplicável. Escolher Bloquear depois de conhecer o ataque importa: o modelo mantém Defesa estática contra um ataque que já erraria e bloqueia quando seria acertado. Duro é condicionado às falhas; sua média não é simplesmente11+Con em todos os ataques.

No perfil Defesa21, atacante+7, Constituição3 e dano já rolado40, a Defesa estática sozinha recebe média14 por ataque declarado. Bloquear com Duro reduz essa média para7,4575. Com Alicerce, fica2,0125. Somar Casca num ataque interceptado do tipo resistido deixa0,10492. A chance de terminar sem dano nessa última combinação é96,515%. Para dano80, Alicerce+Duro+Casca recebem média3,915655. Estes números pressupõem que o Bastião pode interceptar esse ataque; Casca não se estende aos demais ataques recebidos.

Essa proteção é forte contra golpes moderados, e a retirada humana do limite de Duro aumenta a resistência a vários atacantes. Não a reverti silenciosamente. Há custos de posição, seleção de tipos e Reação para interceptar, mas eles não anulam a força identificada. O modelo não inclui o dano adicional de Brecha nem atribui ao adversário dano crítico aleatório: a entrada já é o dano determinado. Também não mede objetivos da cena ou a capacidade do inimigo de atacar outra reserva. A comparação final deve usar inimigos e equipamentos do livro, sem presumir que toda defesa é excedente.

A possibilidade de escolher Bloquear depois do acerto favorece qualquer personagem do sistema; é decisão de R02, não benefício criado aqui. Duro torna essa escolha especialmente vantajosa. Contra efeitos automáticos ou TR não há Bloquear, e Duro não reduz dano apenas por ser recebido.

## Ações, recursos e controle

Um turno comum de Punho7 pode ter dois ataques da Padrão e um Bônus após acerto. Uma Padrão adicional não repete AtaqueExtra naquela rodada. Um ataque que acerta não ativa Minha Vez; um Bloquear que evita o acerto não ativa Trocação. Minha Vez pode acontecer em outro ataque, paga2PE e tem seu limite próprio. Não afirmamos um máximo absoluto de ataques por rodada: a Reação renova no começo do próprio turno e pode ser usada antes e depois dele na mesma rodada.

Arrastão com Força6 tenta seis alvos distintos. Com ampliação custa10PE, mesmo se errar. O Bônus pode atingir novamente um alvo ao alcance normal, mas não dá um segundo Arrastão. Mão Pesada empurra sem TR adicional, 4,5m por alvo por rodada, enquanto agarrar/derrubar exige TR e respeita seu uso. O potencial de controle em área no nível27 é intencionalmente elevado; múltiplos agarrões continuam limitados por mãos e alcance. Uma comparação de dano por alvo não mede o valor de retirar inimigos de uma passagem ou precipício.

Em Provocar+6 contra Espírito+4, cada alvo falha57,25% das vezes. Com o mesmo teste para quatro alvos, a chance de todos falharem é27,5833%, e não a quarta potência da probabilidade marginal: a rolagem de Provocar é compartilhada. Empates resistem. A vantagem de Nem Um Arranhão depende da posição do atacante, sem gastar Reação. Embalo pode repor energia depois que ela for gasta, mas nunca acumula reservas repetidas.

Ainda de Pé cura média7,5 no nível7 e19,5 no30. Com Constituição6 constante, a vida no30 é395; a média recuperada é cerca de4,94% do máximo. A cura não é um motivo para enfraquecer o restante do kit, e não substitui a revisão futura de Morrendo.

## Referências de organização

[D&D Beyond — Character Classes](https://www.dndbeyond.com/sources/dnd/br-2024/character-classes), consultado em03/10/2026: a apresentação separa identidade, características, progressão e habilidades nomeadas por nível. Usei essa lógica de consulta: tabelas curtas e regras locais com custos e gatilhos. O texto da candidata não copia a prosa, os números ou a progressão das classes de D&D. A comparação avalia organização e precisão, não equivalência de poder.

[D&D Beyond — Playing the Game](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game), consultado em03/10/2026: os procedimentos de jogo distinguem resolução, dano e proteções. A candidata aplica a mesma necessidade de sequência explícita, mas conserva os procedimentos próprios do ProjetoM, inclusive Bloquear e arredondamento do dano recebido. Não importei a ordem de reduções ou as condições de D&D.

## Parecer editorial por seção

`evidencias/REVISAO-POR-SECAO.json` registra clareza, suficiência, números, compatibilidade e voz em cada uma das 11 páginas. O texto dá ao leitor o procedimento necessário para usar a habilidade e remete ao dono para a condição inteira. A incompatibilidade nominal com Canalizar é necessária para a regra de Contra a Parede; não reproduz a aptidão. Títulos diretos e nomes aprovados foram mantidos.

Não houve teste com jogadores nem comparação cega de preferência textual. A revisão por agente não demonstra por si só que um iniciante compreenderá o livro. Em mesa, testar uma interceptação com crítico, Mão Pesada após empurrão, Arrastão com dois erros e Passa Pra Mim com dano misto; pedir ao leitor que resolva sem orientação do autor.

## Pendências de fechamento

Revisão independente, PDF e inspeção de todas as páginas estão com o root. No fechamento, sincronizar Provocar, ordem de dano misto e retirar a reprodução de Duro/Casca de R03. Quando Morrendo/Integridade forem redesenhados, rever Ainda de Pé e a transferência de Alma. Não existem alegações de cânone de JJK nesta unidade: as habilidades são regras originais do ProjetoM.

## Revisão independente e BAS26

Revisão integral por /root/rotas_didatica em `evidencias/REVISAO-INDEPENDENTE.md`. A redação de Nem Um Arranhão passou a incluir efeitos ofensivos sem teste de acerto, exigindo origem em criatura hostil dentro da área. Auditoria atual: 113 verificações e 52 casos, todos aprovados. Nenhum teste com leitores ou playtest foi realizado. A sincronização de dano misto no R03 continua necessária antes da integração final.


## Fechamento da prova

Prova de 11 páginas inspecionada integralmente pelo agente principal. Conferência automática: 96 verificações aprovadas. Os resultados substituem a pendência de PDF/visual desta versão, sem encerrar sincronizações globais de Dano/Provocar nem alegar playtest humano.

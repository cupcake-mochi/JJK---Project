import sys;sys.path.insert(0,'/tmp');from revisar_guia94 import *
headings(21,[('# Acompanhar recursos e consequências','# Vida, energia e outros recursos'),('## Separe máximos e valores atuais','## Máximo e valor atual'),('## Resolva o dano antes de alterar reservas','## Como descontar o dano'),('## Integridade e penalidades','## Perder Integridade'),('## Recupere usos pelo prazo certo','## Quando recuperar os usos'),('## Faça uma passagem que outro mestre consiga usar','## Registre para continuar depois')])
edit(source(21),[
('confira o estado dos personagens','confira como estão os personagens'),
('Na saída, atualize apenas o que as regras de recuperação e os acontecimentos realmente permitirem.','Ao terminar a missão, confira o que cada personagem recupera pelas regras e o que ainda precisa de cuidado.'),
('Use esta seção para organizar o acompanhamento.','Use os campos abaixo para acompanhar o que cada personagem ainda tem.'),
('desenvolve vida a zero e derrota','explica o que acontece ao chegar a zero de vida ou ficar Derrotado'),
('forma de saída','condição para voltar ao normal'),
('em vez de preencher todos os campos por analogia','antes de usar os mesmos campos para todos'),
('Resistência, Redução de Dano e vida temporária não são o mesmo procedimento.','Resistência, Redução de Dano e vida temporária entram em momentos diferentes da conta.'),
('salvo exceção expressa','a menos que uma regra diga o contrário'),
('a nova concessão','a quantidade recebida'),
('aplique o estágio mais alto alcançado, conservando os efeitos anteriores','aplique as penalidades de todos os estágios que a perda atingiu'),
('mantêm seus próprios procedimentos','seguem suas próprias regras'),
('Use o procedimento de dúvidas de','Siga as orientações de dúvidas de regra em'),
('dias ficcionais','dias da história'),
('O nível de detalhe depende do que precisa ser retomado, sem apagar o que ainda produz efeito.','Anote o que será necessário para continuar, incluindo os efeitos que ainda estão ativos.')
])
headings(22,[('## Confira a causa e a janela','## Quanto tempo resta para o socorro'),('## Registre os dados da queda','## O que anotar quando alguém cai'),('## Explique a escolha sem decidir pelo jogador','## Aguentar ou Insistir'),('## Conte o tempo pelo ponto da queda','## Como contar as rodadas'),('## Dano posterior também consome janela','## Receber dano enquanto está Morrendo'),('## Acumule cura válida','## Quanto falta para se recuperar'),('## Estabilize quando a cura não for a resposta disponível','## Estabilizar'),('## Duas quedas no confronto do piloto','## Exemplo: duas quedas no mesmo combate')])
edit(source(22),[
('O estado, as opções de participação e o prazo de socorro dependem das regras daquele personagem. Registre a escolha e acompanhe tratamento e tempo separadamente.','Confira se ele pode continuar agindo e quanto tempo resta para o socorro. Anote a escolha do jogador. Depois, conte separadamente a cura recebida e o tempo que ainda resta.'),
('Esta seção ensina o procedimento para personagens jogadores do Livro de Regras 1.0.','Esta seção explica as regras de queda dos personagens dos jogadores, conforme o Livro de Regras 1.0.'),
('seu desfecho conforme esse procedimento','o resultado conforme essas regras'),
('mostra o procedimento numa sequência','mostra essas regras numa sequência'),
('a janela começa com **3 rodadas menos 1 por Sequela**','o prazo para receber socorro, chamado de **janela**, começa com **3 rodadas menos 1 por Sequela**'),
('Uma capacidade disparada pela queda','Uma habilidade ativada pela queda'),
('capacidades disparadas pela própria queda','habilidades ativadas pela própria queda'),
('A vida atual permanece zero durante Morrendo.','Enquanto o personagem está Morrendo, sua vida atual permanece zero.'),
('**Classe**, aqui, é a escala das aplicações do sistema, não o nível do personagem. Consulte a rota da ficha para seu uso.','**Classe** é a categoria usada para feitiços e outras aplicações do sistema. Não é o nível do personagem. Confira na ficha qual é sua maior Classe.'),
('se cumprir os requisitos da fonte','se cumprir os requisitos da habilidade ou do recurso de cura'),
('Não pode voltar a Insistir nessa ocorrência.','Não pode voltar a Insistir nessa mesma queda.'),
('no ponto da iniciativa','no ponto da iniciativa'),
('uma ação de socorro que só começaria naquele ponto não antecede o prazo','uma ação de socorro que só começaria naquele ponto chega tarde demais'),
] if False else [
('O estado, as opções de participação e o prazo de socorro dependem das regras daquele personagem. Registre a escolha e acompanhe tratamento e tempo separadamente.','Confira se ele pode continuar agindo e quanto tempo resta para o socorro. Anote a escolha do jogador. Depois, conte separadamente a cura recebida e o tempo que ainda resta.'),
('Esta seção ensina o procedimento para personagens jogadores do Livro de Regras 1.0.','Esta seção explica as regras de queda dos personagens dos jogadores, conforme o Livro de Regras 1.0.'),
('seu desfecho conforme esse procedimento','o resultado conforme essas regras'),
('mostra o procedimento numa sequência','mostra essas regras numa sequência'),
('a janela começa com **3 rodadas menos 1 por Sequela**','o prazo para receber socorro, chamado de **janela**, começa com **3 rodadas menos 1 por Sequela**'),
('Uma capacidade disparada pela queda','Uma habilidade ativada pela queda'),
('capacidades disparadas pela própria queda','habilidades ativadas pela própria queda'),
('A vida atual permanece zero durante Morrendo.','Enquanto o personagem está Morrendo, sua vida atual permanece zero.'),
('**Classe**, aqui, é a escala das aplicações do sistema, não o nível do personagem. Consulte a rota da ficha para seu uso.','**Classe** é a categoria usada para feitiços e outras aplicações do sistema. Não é o nível do personagem. Confira na ficha qual é sua maior Classe.'),
('se cumprir os requisitos da fonte','se cumprir os requisitos da habilidade ou do recurso de cura'),
('Não pode voltar a Insistir nessa ocorrência.','Não pode voltar a Insistir nessa mesma queda.'),
('Uma ação de socorro que só começaria naquele ponto não antecede o prazo.','Uma ação de socorro que só começaria naquele ponto chega tarde demais.'),
('aproximação da cura','avanço do tratamento'),
('Confira fonte, ação, alcance, alvo e compatibilidade com o corpo.','Confira de onde vem a cura, a ação que ela exige, seu alcance, seus alvos e se funciona naquele corpo.'),
('Remoção genérica de condições não encerra Morrendo.','Uma habilidade que remove condições só encerra Morrendo se disser isso expressamente.'),
('para a contagem temporal','para contar as rodadas'),
('No ramo principal','Na sequência principal'),
('No ramo alternativo do roteiro','Na outra versão do exemplo'),

])
headings(23,[('## Torne a saída compreensível','## Mostre os caminhos de saída'),('## Resolva movimento e respostas','## Movimento e ataques de oportunidade'),('## Transporte quem não consegue sair','## Carregar um aliado'),('## Se o socorro continua, conserve o prazo','## Socorro durante a retirada'),('## Recupere depois de Derrotado','## Recuperar-se da derrota'),('## Confirme o descanso pela situação','## Quando o grupo pode descansar'),('## Confira as exceções da ficha','## Corpos e cuidados diferentes'),('## Dê destino às consequências da missão','## O que acontece depois da derrota'),('## Prepare a retomada','## Antes da próxima missão')])
edit(source(23),[
('Uma retirada precisa dizer quem sai, por onde e com quais meios.','Para organizar uma retirada, confira quem precisa sair, por onde pode passar e como chegar até lá.'),
('Parar a descrição do combate não resolve essas etapas sozinho.','Encerrar a narração do combate não faz o grupo sair do perigo nem receber atendimento.'),
('retomada','próxima sessão'),
('essas etapas','esses passos'),
] if False else [
('Uma retirada precisa dizer quem sai, por onde e com quais meios.','Para organizar uma retirada, confira quem precisa sair, por onde pode passar e como chegar até lá.'),
('Parar a descrição do combate não resolve essas etapas sozinho.','Encerrar a narração do combate não faz o grupo sair do perigo nem receber atendimento.'),
('seus momentos de agir','sua vez de agir'),
('têm seus tratamentos próprios','seguem suas próprias regras'),
('quem se move e quais gatilhos realmente foram atendidos','quem se move e se esse movimento permite uma oportunidade'),
('capacidade de cada participante','limite de carga de cada participante'),
('precisa de procedimento diferente','segue outras regras de socorro'),
('no ramo alternativo do piloto','na outra versão do combate do anexo'),
('pelo procedimento do Livro de Regras 1.0','pelas regras do Livro de Regras 1.0'),
('Os procedimentos gerais abaixo podem ser modificados','As regras gerais abaixo podem ser modificadas'),
('conservam seus procedimentos','seguem suas próprias regras'),
('para a resolução','para conferir suas regras'),
('A decisão sobre a ocorrência e seu esforço deve ser explicável pelo que aconteceu.','Explique por que o esforço daquele confronto conta como luta, usando o que aconteceu na cena.'),
('Essa margem não acrescenta um gatilho novo de ganho de Exaustão.','Essa possibilidade serve para remover um degrau. Ela não cria uma nova causa de Exaustão.'),
('A tabela apresenta o procedimento geral','A tabela apresenta as regras gerais'),
('metade é um piso após a pausa','metade é o mínimo que deve restar depois da pausa'),
('Use as regras pertinentes e os procedimentos compartilhados para o que afetar fichas.','Para alterar uma ficha, siga as regras e os acordos da comunidade.'),
('mantenha o jogador informado do procedimento','explique ao jogador como será o socorro'),
('comunique o estado aos jogadores','diga aos jogadores como suas fichas ficaram')
])
print('C04: primeira leitura das três fontes concluída.')

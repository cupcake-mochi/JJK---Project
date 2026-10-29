"""Documenta a estrutura proposta; não altera fontes nem gera a edição de leitura."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

APOIO = Path(__file__).resolve().parent
RAIZ = APOIO.parents[1]

DESTINOS = """ENT|Como usar este livro
N01.1|1.1 O que faz o mestre
N01.2|1.2 Antes de começar
N01.3|1.3 Uma cena do cotidiano
N01.4|1.4 Prepare As batidas no anexo
N01.5|1.5 Jogue a missão
N01.6|1.6 Se o grupo escolher outro caminho
N01.7|1.7 Depois da missão
N02.1|2.1 Maldições na vida comum
N02.2|2.2 Feiticeiros, energia e técnicas
N02.3|2.3 Escolas, famílias e contatos
N02.4|2.4 Diferentes formas de viver
N02.5|2.5 Trabalho, estudo e relações
N02.6|2.6 A época e o lugar da sua campanha
N03.1|3.1 O preparo necessário
N03.2|3.2 Pessoas que dão vida à aventura
N03.3|3.3 Lugares e caminhos
N03.4|3.4 Pistas e investigações
N03.5|3.5 Perigos e consequências
N03.6|3.6 Ideias para sua próxima missão
N03.7|3.7 Quando há pouco tempo
N04.1|4.1 Descrever, ouvir e responder
N04.2|4.2 Quando pedir um teste
N04.3|4.3 Interpretar e negociar
N04.4|4.4 Conduzir uma investigação
N04.5|4.5 As ideias dos jogadores e o cenário
N04.6|4.6 Atenção, ritmo e mudança de cena
N04.7|4.7 Combate, socorro e retirada
N04.8|4.8 Dúvidas e fim da sessão
N05.1|5.1 A sessão zero
N05.2|5.2 Vínculos e interesses dos personagens
N05.3|5.3 De uma missão à próxima
N05.4|5.4 Facções
N05.5|5.5 Antagonistas
N05.6|5.6 Arcos, finais e epílogos
N06.1|6.1 Objetivos e papéis no encontro
N06.2|6.2 Escolher, adaptar e criar uma ficha
N06.3|6.3 Habilidades, energia e recarga
N06.4|6.4 Escolher os números
N06.5|6.5 Grupo, terreno e composição
N06.6|6.6 Chefes e confrontos maiores
N06.7|6.7 Perigos ambientais
N06.8|6.8 Conferir antes e depois de jogar
N07.1|7.1 Conferir uma ficha
N07.2|7.2 Convivências e cuidados
N07.3|7.3 Escolhas próprias do personagem
N07.4|7.4 Avaliar uma criação
N07.5|7.5 Poderes avançados
N07.6|7.6 Registrar e rever uma decisão
N08.1|8.1 Rotina, descanso e compromissos
N08.2|8.2 Trabalho, dedicação e espera
N08.3|8.3 Ofícios, fabricação e reparos
N08.4|8.4 Comprar, emprestar e contratar
N08.5|8.5 Ferramentas e objetos amaldiçoados
N08.6|8.6 Recompensas e progressão
N09.1|9.1 Preço e benefício de um Pacto
N09.2|9.2 Desenvolver e avaliar uma troca
N09.3|9.3 Promessas entre pessoas
N09.4|9.4 Obter e criar entidades
N09.5|9.5 Trabalho, materiais e novas tentativas
N09.6|9.6 Evolução, transferência e continuidade
N10.1|10.1 Mesas diferentes, mundo compartilhado
N10.2|10.2 Calendário e atividades
N10.3|10.3 Passar uma missão para outro mestre
N10.4|10.4 Fichas, decisões e registros
N10.5|10.5 Ouvir o grupo e dividir o trabalho
A1|A1 Preparo de missão
A2|A2 Lembretes de condução
A3|A3 Estado e socorro
A4|A4 Resumo para continuar depois
A5.1|A5 Acordos do grupo
A5.2|A5 Descobertas
A5.3|A5 Facção
A5.4|A5 Convivência
A5.5|A5 Avaliação de capacidade
A5.6|A5 Projeto e entrega
A5.7|A5 Dedicação por ficha
A5.8|A5 Pactos e Promessas
A5.9|A5 Aquisição e estado de entidade
A5.10|A5 Inimigo e encontro
A5.11|A5 Habilidade de inimigo
A5.12|A5 Chefe
B1|B1 Testes, percepção e movimento
B2|B2 Confrontos e perigos
B3|B3 Personagens e técnicas
B4|B4 Objetos e recompensas
B5|B5 Pactos e entidades
C1|C1 Termos do mundo
C2|C2 Onde encontrar as dúvidas mais comuns
D1|D Inspirações da obra — contém revelações"""

# Uma linha por fonte integrada. O destino complementar indica reaproveitamento
# de uma parte ou remissão; não manda copiar o texto inteiro em dois lugares.
MAPA = """s001|complementar|N03.1|N03.2,N03.3,N03.5,N03.7|Conservar o método; preencher o preparo mínimo e separar as instruções do comentário longo do anexo.
s002|condensar|A1|N03.1,N10.3|Reduzir a folha ao preparo de uma missão; campos especializados remetem aos registros próprios, sem duplicar o formulário inteiro.
s003|mover|N01.4|N01.7|Unir o preparo preenchido à demonstração e ao mapa; manter uma única versão dos fatos da missão.
s004|complementar|N04.1|N01.1,N04.2,N04.3,N04.6,N04.7,N04.8|Distribuir as orientações por decisão; ampliar conversas e ritmo; aproveitar somente o essencial na entrada.
s005|condensar|A2|N04.2,N04.4,N04.7,N04.8|Fazer a folha curta; transferir explicações e exceções para o corpo ou para casos já existentes.
s006|condensar|N02.1|N01.1,N02.2,N02.4,N02.6,N08.1|Mundo como contexto jogável; fornecer somente o vocabulário da primeira missão na entrada e evitar repetir instruções de teste.
s007|condensar|N05.1|N01.2,N10.1|Preservar a sessão zero completa; extrair acordos essenciais para começar e administração de várias mesas para a guilda.
s008|manter|A5.1|N05.1,N01.2|Manter o registro de acordos e apontar quais perguntas bastam à primeira missão.
s009|condensar|N05.1|N01.2|Reaproveitar o exemplo de campanha junto dos acordos; evitar repetir instruções já explicadas.
s010|condensar|N04.4|N03.4|Manter condução da descoberta, falha e mudança de abordagem; preparo da investigação é explicado em 3.4.
s011|complementar|N04.5|N03.3,B1|Conservar a leitura de posições e meios; mostrar soluções funcionais e remeter cálculos especializados aos casos.
s012|manter|A5.2|N04.4,N10.3|Conservar fontes, descobertas e hipóteses; usar quando uma nota curta já não for suficiente.
s013|condensar|N03.4|N04.4|Conservar o método de construir a investigação e as fontes alternativas; distinguir preparo de condução.
s014|mover|B1|N03.4,N04.3,N04.4|Usar um trecho como exemplo breve de investigação e negociação; manter o preparo completo consultável.
s015|condensar|N05.3|N10.1,N10.3|Ensinar consequências e próximos assuntos; as particularidades da passagem entre mestres ficam no capítulo 10.
s016|condensar|A4|N05.3,N10.3,N10.5|Criar o resumo de retomada a partir dos campos; concentrar instruções de entrega e retorno nos capítulos pertinentes.
s017|complementar|N05.4|N03.2,A5.3|Conservar objetivos e reações das facções; tornar os exemplos mais variados ao desenvolver o conjunto de inspiração.
s018|condensar|N05.5|N06.1|Conservar criação, apresentação e reação do antagonista; concentrar limites mecânicos nas consultas de encontro.
s019|manter|N05.6|N01.7|Manter desfechos e epílogos abertos às escolhas; aproveitar um fechamento breve no fim da primeira missão.
s020|manter|A5.3|N05.4|Manter a ficha e um preenchimento breve; não exigir facção para todo contato.
s021|condensar|N04.7|N01.5,A3|Preservar máximos, valores atuais, temporários, Integridade e duração; fornecer lembretes só dos recursos usados no piloto.
s022|condensar|N04.7|N01.5,A3,B1|Preservar no corpo o passo a passo de queda e socorro; o exemplo extenso de duas quedas vira caso consultável.
s023|condensar|N04.7|N08.1,N01.6,B1|Preservar retirada, recuperação e descansos; aproximar descanso do cotidiano e deixar cálculos extensos em consulta.
s024|manter|A3|N04.7,N10.3|Conservar janela, tratamento, iniciativa e estado necessários à continuidade do socorro.
s025|condensar|N07.1|N01.2,N07.6|Conservar conferência e evolução da ficha; extrair somente o necessário antes da primeira missão.
s026|mover|N05.2|N02.4,N07.2|Vínculos gerais passam à campanha; particularidades de Encarnado e Corpo Amaldiçoado continuam junto dos personagens.
s027|manter|N07.2|N05.2,A5.4|Conservar acordo de vozes, participação e modalidades; recomendação de voz do mestre continua dependente do acordo.
s028|manter|A5.4|N07.2|Conservar modelo de convivência e exemplo; não exigir essa folha de outras Origens.
s029|condensar|N07.4|N07.6,A5.5|Preservar avaliação passo a passo, um uso e um limite; aproximar a decisão de seu registro e revisão.
s030|condensar|N07.4|B3|Manter um exemplo acompanhado no método; os outros pareceres ficam localizáveis por problema em B3.
s031|condensar|N07.5|B3|Conservar a orientação de Liberação, Máxima, Domínio e CE4; montagens e usos completos permanecem em B3.
s032|manter|A5.5|N07.4,N07.6|Manter proposta, decisão, alcance e revisão; vínculo direto com o método de avaliação.
s033|mover|B3|N07.3,N07.4,N07.5|Organizar casos específicos por dúvida; levar ao corpo as conclusões necessárias para entender o método.
s034|condensar|N08.3|N08.2,B4|Conservar projeto, materiais, teste e falha; usar um trabalho acompanhado e evitar duplicação dos casos completos.
s035|manter|N08.4|A5.6|Preservar compra, reposição, empréstimo, serviço e venda; apresentar escolhas e relações antes da conferência de custos.
s036|condensar|N08.5|N08.3,B4|Manter uso, identificação, Desgaste, criação e objeto perigoso; casos próprios ficam em B4.
s037|condensar|N08.6|N01.7,N10.4|Preservar XP semanal por jogador, resultados parciais e remuneração opcional; o capítulo 10 referencia sem criar política distinta.
s038|manter|A5.6|N08.3,N08.4|Manter campos e exemplo de projeto; empréstimo curto continua alternativa adequada a operações simples.
s039|condensar|N08.2|N08.1,N10.2|Conservar integralmente as condições da política; concentrar sua exposição em 8.2 e manter adaptação de campanha fechada ao lado.
s040|manter|A5.7|N08.2,N10.2|Conservar saldo, origem, acesso e exemplos por ficha; não confundir com o controle de XP por jogador.
s041|condensar|N09.1|N09.2,N09.3,A5.8|Conservar categorias e funcionamento publicados; Overtime ou outro exemplo publicado da própria fonte introduz a troca.
s042|manter|A5.8|N09.1,N09.3|Manter obrigações, prazos e exemplos de registro, com remissão aos acordos completos.
s043|condensar|N09.4|N09.6,B5|Conservar todas as formas e passos de aquisição no capítulo; ilustrações longas ficam nos casos completos.
s044|manter|A5.9|N09.4,N09.5,N09.6|Preservar requisitos, projeto, estado e passagem; exemplos completos por tipo ficam em B5.
s045|condensar|N09.5|B5,N08.2|Manter tabela de trabalho, orçamento por projeto, falha e detalhamento opcional; exemplo longo alimenta B5.
s046|condensar|N09.6|B5|Manter cálculo de reconstrução e transferência, requisitos e falha; os acompanhamentos completos ficam em B5.
s047|condensar|N09.2|B5|Preservar método e recorte das sete ideias; apontar para os dois modelos sem desenvolver os três adiados.
s048|mover|B5|N09.2|Preservar o Pacifismo completo, benefício particular e saídas aprovadas; só a lição da avaliação aparece no método.
s049|mover|B5|N09.2|Preservar Liberação irregular e Refluxo completos; exemplo permanece experimental e consultável.
s050|condensar|N09.3|B5|Conservar termos, reparação e consequência completa da Promessa no capítulo; desfechos adicionais e contas ficam no caso.
s051|mover|B5|N09.4|Conservar prova de ritual, mapa, ficha e resultados; usar no método um resumo suficiente da forma de aquisição.
s052|mover|B5|N09.4,N09.6|Conservar Doma, condições e ficha convertida; explicar seus passos no método e citar este estudo como aplicação.
s053|mover|B5|N09.4,N09.6|Conservar construção e evolução do Escriba; extrair um exemplo curto para ensinar as escolhas da criação.
s054|mover|B5|N09.6,N04.7|Conservar transporte, estados e consequências para passageiros; levar os cuidados gerais ao método correspondente.
s055|mover|B5|N09.5,N09.6|Manter fabricação e evolução completas; usar como aplicação das tabelas de trabalho e reconstrução.
s056|condensar|N06.1|N06.2,N06.5,N06.8|Preservar o construtor e o preparo do encontro no corpo; organizar as etapas e concentrar ressalvas repetidas.
s057|mover|B2|N06.5,N06.8|Preservar análise e limites da simulação; levar conclusões didáticas ao método sem prometer risco previsto para qualquer mesa.
s058|manter|A5.10|N06.2,N06.8|Manter ficha específica de ameaça e encontro, acionada quando esse detalhe for necessário.
s059|manter|N06.3|B2|Manter a escolha entre PE, recarga e condições no método; cada modelo explica sua função e interações.
s060|condensar|N06.2|N06.3,B2|Conservar construção e classificação da habilidade; manter um caso acompanhado e encaminhar detalhes dos demais.
s061|condensar|A5.11|N06.2,N06.8|Conservar perguntas para conferir interações sem exigir transcrição da mesma habilidade em várias folhas.
s062|mover|B2|N06.5|Conservar cenário, mapa e escolhas do corredor; método de composição aproveita uma leitura breve do caso.
s063|mover|B2|N06.2,N09.4|Conservar ficha do Carregador e conversão de Doma; nenhuma dessas fichas é substituída por resumo.
s064|mover|B2|N06.7|Conservar o perigo e seu cronograma completos; apresentar no método uma sequência curta de preparação/intervenção.
s065|condensar|N06.5|B2|Manter a combinação de inimigos e ambiente no método; comparação extensa acompanha seus casos em B2.
s066|mover|B2|N06.5|Conservar mapa, fechamento do portão e caminhos de resposta; citar como variação com objetivo.
s067|condensar|N06.6|B2|Manter o método de chefes; comportamentos, ações e sinais continuam explicados antes das aplicações extensas.
s068|condensar|A5.12|N06.6,B2|Manter ferramenta de chefe; reorganizar crítica histórica do Carregador como exemplo útil, preservando contexto de proposta.
s071|mover|B2|N06.6|Conservar ficha, cenário e exemplo de chefe; referenciar a função de suas respostas no método.
s072|mover|B2|N09.4,N09.6|Manter ficha do Sineiro após Doma junto do caso e remeter a ela na aquisição de entidades.
s073|mover|B2|N06.6,N04.7|Conservar rodadas e socorro; resumir a lição de objetivo e resposta no capítulo de chefes.
s074|condensar|N06.4|B2|Conservar referências de números e seu alcance no corpo; contas completas e premissas ficam no estudo.
s075|mover|B2|N06.2,N06.3|Preservar as duas fichas completas; um resumo pode ilustrar atacante e apoio no método.
s076|mover|B2|N06.5|Manter confronto e comparação de alvos; usar a conclusão sobre apoio como exemplo de composição.
s077|mover|B2|A5.10,N06.8|Manter o preenchimento junto de Ren e Sora; o formulário em branco continua acessível em A5.
s078|condensar|N06.7|B2|Conservar preparação do perigo, exposição, resolução, sinais e formas de terminar; aplicações extensas vão a B2.
s079|mover|B2|N06.7,N10.3|Conservar poeira, condições e saída; a passagem entre mestres referencia o estado resultante.
s080|condensar|N10.4|N10.5,C2,A4|Usar a seleção de folhas por necessidade; reduzir repetição de instruções de cada formulário e extrair a consulta por problema.
s081|condensar|N10.3|B1,A4|Manter uma passagem curta e suficiente no capítulo; preservar a retomada detalhada com socorro em B1.
s082|condensar|N04.2|N04.7,B1|Manter teste, custo, ajuda e grupo no método; cinco empates e aplicações longas passam a B1.
s083|mover|B1|N04.4|Preservar todos os casos de percepção; o método mantém a distinção indispensável entre informação, alcance e meios.
s084|mover|B1|N04.5|Preservar medidas, contas e consequências de percursos e quedas; o corpo ensina como apresentar a situação e escolher a regra.
s085|mover|B1|N04.5|Preservar trajetórias, instalação e armas improvisadas; levar as decisões gerais para o corpo da condução.
s086|complementar|N02.3|N02.4,N02.5,N02.6,N03.2|Dar destaque à vida e às relações; variar exemplos e remeter conferências de ficha a seus capítulos.
s087|manter|D1|N02.6|Preservar os casos e avisos; a referência no mundo essencial não revela o conteúdo nem o coloca na busca geral.
s088|condensar|C1|N02.1,N02.2,N02.3|Manter os termos e suas relações; definições essenciais aparecem no ponto de uso sem exigir o apêndice primeiro.
s089|mover|B3|N07.3|Preservar opções e família Arata; extrair orientação de personalização. A CD 16 permanece questão de conferência, sem alteração aqui.
s090|condensar|N07.2|N08.3,B3|Conservar cuidado e diferença entre reparar e descansar; caso completo de atendimento fica em B3.
s091|condensar|N07.2|N02.4,B3|Conservar participação e cuidados no corpo; ficha de Nilo e casos específicos completos vão a B3.
s092|manter|N07.3|A5.5|Manter só a habilidade publicada e seu acordo por personagem; histórico de depósitos e retiradas segue fora da leitura.
s093|mover|B3|N07.4,N07.5|Conservar montagem, Ampliação e troca de Forma de Yara; remeter a partir da dúvida específica.
s094|mover|B3|N07.4|Conservar repetição de Melhorias, Condicional e Restrição Própria; extrair critérios necessários ao método geral.
s095|mover|B3|N07.5,N04.5|Conservar efeito de cena e cancelamento completos, com referências junto da orientação geral.
s096|mover|B4|N08.3,N08.5|Conservar Anel, identificação e projeto; um trecho acompanha o ensino de fabricar sem duplicar o caso.
s097|mover|B4|N08.4|Manter empréstimo e negociação como aplicação; o método conserva critérios de acesso e acordo.
s098|mover|B4|N08.5|Preservar objeto, selo, escolhas e consequências; não usar seu efeito como regra geral de todo objeto selado.
s099|mover|B4|N08.6|Conservar feito e promoção completos; explicar no capítulo como conferir requisitos e não confundir os controles de recompensa.
s100|mover|B2|N06.4|Conservar comparação por faixa e suas limitações; levar a advertência útil ao método sem criar escala geral validada.
s101|mover|B2|N06.3,N06.5|Preservar fichas, custos e Reações dos guardas; apresentar no método a função de suas escolhas.
s102|mover|B2|N06.5,N06.8|Conservar o arquivo e a economia de ações; uma conclusão curta ajuda a avaliar terreno e controle.
s103|mover|B2|N06.7,N08.1|Preservar doença, evolução e tratamento completos; o método mantém o acompanhamento de efeitos prolongados.
x001|condensar|N01.5|N01.4,N01.6,N01.7|Unir conversa, preparo, confronto e alternativas à missão; eliminar duplicação de fatos com s003, mantendo requisitos do socorro.
x002|mover|N01.5|N06.2,N09.4|Amontoado completo no ponto de uso; Rastejante e Vigia ficam como exemplos do construtor; conversões permanecem acessíveis na aquisição.
x003|condensar|N01.3|N03.2,N04.1,N04.3,N04.6|Usar uma cena breve de cotidiano na entrada; o comentário de decisão alimenta os métodos, sem repetir o episódio inteiro."""

# Recortes obrigatórios para fontes que cruzam funções. Os demais casos ficam
# identificados pelos títulos da fonte e pelo destino principal/complementar.
RECORTES = [
    ("s006", "Feiticeiros e técnicas", "N02.2"),
    ("s006", "As Origens no dia a dia", "N02.4"),
    ("s006", "Entre uma missão e outra", "N08.1"),
    ("s007", "Proponha a campanha", "N05.1"),
    ("s007", "Organize os encontros", "N10.1"),
    ("s004", "Quando pedir um teste", "N04.2"),
    ("s004", "Interprete as outras pessoas", "N04.3"),
    ("s004", "Dê espaço a todos", "N04.6"),
    ("s004", "Quando passar à próxima cena", "N04.6"),
    ("s004", "Quando começa o combate", "N04.7"),
    ("s004", "Dúvidas de regra", "N04.8"),
    ("s005", "Em combate", "N04.7"),
    ("s015", "Quando muda o mestre", "N10.3"),
    ("s022", "Exemplo: duas quedas no mesmo combate", "B1"),
    ("s023", "Descanso curto", "N08.1"),
    ("s023", "Descanso longo", "N08.1"),
    ("s026", "Encarnado: a vida de outra pessoa", "N07.2"),
    ("s026", "Corpo Amaldiçoado: consciência e cuidado", "N07.2"),
    ("s041", "Promessas: combine as obrigações", "N09.3"),
    ("s043", "Reconstruir", "N09.6"),
    ("s043", "Transferir ou herdar", "N09.6"),
    ("s043", "Quando o invocador deixa de agir", "N09.6"),
    ("s050", "Três exemplos de desfecho", "B5"),
    ("s080", "Ouça o grupo e divida as tarefas", "N10.5"),
    ("s081", "O socorro de Mei", "B1"),
    ("s082", "Cinco participantes, todos com total 14", "B1"),
    ("s090", "O atendimento de Ena", "B3"),
    ("s091", "A ficha de Nilo", "B3"),
    ("s091", "Cuidados com cada condição", "B3"),
    ("x002", "Rastejante", "N06.2"),
    ("x002", "Vigia das farpas", "N06.2"),
    ("x002", "Conversões conhecidas para maldições domadas", "N09.4"),
]

COMPETENCIAS = """P01|Começar a mestrar|N01.1,N01.2,N01.4,N01.5,N01.7|A1,A2|Reunir a primeira missão e conferir o acesso ao necessário; não há avaliação externa nova.
P02|Consultar o mundo|N01.1,N02.1,N02.2,N02.3,N02.6|C1,C2|Explicar termos no ponto de uso e manter aprofundamento opcional sem revelações inesperadas.
P03|Transformar cotidiano em jogo|N01.3,N02.4,N02.5,N03.6,N08.1|A1|Ampliar variedade e demonstrar convivência que não precise virar tarefa ou perigo.
P04|Combinar grupo e campanha|N01.2,N05.1,N10.1|A5.1|Mostrar acordos essenciais e completos; a campanha fechada precisa de caminho próprio.
P05|Preparar com esforço viável|N01.4,N03.1,N03.7|A1|Preencher o preparo mínimo e demonstrar a redução para pouco tempo.
P06|Criar missão com caminhos possíveis|N03.1,N03.2,N03.3,N03.5,N03.6|A1|Permitir criar outro caso, com escolhas e consequências diferentes do anexo.
P07|Investigar sem depender de pista única|N03.4,N04.4,N01.6|A5.2,B1|Conferir uma pista perdida, uma hipótese alternativa e outra via de informação.
P08|Descrever para decisões informadas|N01.5,N04.1,N04.4,N04.5|A2,B1|Distinguir o evidente, a tentativa possível e o inacessível em exemplos curtos.
P09|Abrir e encerrar cenas com ritmo|N01.3,N01.7,N04.6|A2|Complementar cena repetitiva, grupo pensando, pausa e encerramento no horário.
P10|Distribuir atenção|N04.6,N07.2|A2|Mostrar participação discreta, grupo separado e convites sem obrigar atuação.
P11|Improvisar com consistência|N01.6,N04.2,N04.5,N04.8|A2,B1|Mostrar propostas que funcionam e decisões explicadas, preservando as regras.
P12|Interpretar NPCs e negociar|N03.2,N04.3|A1,B1|Complementar traços memoráveis e conversa com resistência e acordos diferentes.
P13|Fazer facções e antagonistas reagirem|N05.4,N05.5|A5.3|Variar aplicações e ligar objetivos, meios e consequências sem desfecho imposto.
P14|Criar inimigos e preparar encontros|N06.1,N06.2,N06.3,N06.4,N06.5,N06.6,N06.8|A5.10,A5.11,A5.12,B2|Manter o construtor no corpo; referências numéricas ainda experimentais e avaliação geral pendente.
P15|Preparar perigos claros|N06.7,N06.8|A5.10,B2|Manter exposição, tempo, regras e intervenção no método e verificar os casos completos.
P16|Acompanhar recursos e derrota|N04.7,N08.1,N10.3|A3,B1|Preservar socorro no corpo, dados de continuidade e distinção entre descanso e troca de sessão.
P17|Conectar missões e encerrar campanhas|N05.2,N05.3,N05.6|A4|Mostrar resultado de escolhas, relações e encerramentos que não exijam luta final.
P18|Manter continuidade entre mesas|N10.1,N10.2,N10.3,N10.4|A3,A4,A5.7|Conferir retomada sem explicação oral e adaptação com menos registros para mestre único.
P19|Receber retorno e dividir trabalho|N04.8,N10.5|A4|Preparar registro breve e aproveitar sugestões durante a redação; leitores ainda não recrutados.
P20|Avaliar personagens e criações|N07.1,N07.3,N07.4,N07.5,N07.6,N08.3,N09.1,N09.2,N09.3,N09.4,N09.5,N09.6|A5.5,A5.6,A5.8,A5.9,B3,B4,B5|Preservar método e decisões existentes; aprofundamentos localizáveis e limites experimentais identificados."""


def main():
    destinos = dict(line.split("|", 1) for line in DESTINOS.splitlines())
    anterior = json.loads((RAIZ / "07 - Edicao de Leitura/mapa-editorial.json").read_text())
    composicao = json.loads((RAIZ / "08 - Diagramacao do Guia/revisao/composicao.json").read_text())
    fontes = {f["id"]: f for f in anterior["fontes"]}
    capitulos = {s: c["titulo"] for c in anterior["capitulos"] for s in c["consultas"]}
    regras = {}
    for line in MAPA.splitlines():
        ident, acao, destino, extra, motivo = line.split("|", 4)
        assert ident not in regras, ident
        assert acao in {"manter", "condensar", "mover", "complementar"}
        usos = [x for x in extra.split(",") if x]
        assert all(x in destinos for x in [destino, *usos]), ident
        regras[ident] = {"acao": acao, "destino_principal": destino,
                         "usos_complementares": usos, "orientacao": motivo}
    assert set(regras) == set(fontes), {"sem_destino": list(set(fontes) - set(regras)),
                                       "ids_extras": list(set(regras) - set(fontes))}
    assert len(fontes) == 104
    resultado = []
    for ident, fonte in fontes.items():
        p = RAIZ / fonte["fonte"]
        texto = p.read_text()
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        assert digest == fonte["sha256"], (ident, "fonte alterada desde a edição")
        resultado.append({"id": ident, "fonte": fonte["fonte"], "sha256": digest,
                          "titulo_atual": fonte["titulo"], "capitulo_atual": capitulos[ident],
                          "pagina_inicial_atual": composicao["secoes"][ident]["pagina"],
                          "secoes_atuais": re.findall(r"^#{2,3} (.+)$", texto, re.M),
                          **regras[ident]})
    por_id = {x["id"]: x for x in resultado}
    recortes = []
    for ident, secao, destino in RECORTES:
        assert secao in por_id[ident]["secoes_atuais"], (ident, secao)
        assert destino in destinos
        recortes.append({"fonte_id": ident, "secao_atual": secao, "destino": destino})
    competencias = []
    for line in COMPETENCIAS.splitlines():
        ident, titulo, corpo, ferramentas, pendencia = line.split("|", 4)
        lista = corpo.split(",")
        apoio = ferramentas.split(",")
        assert all(x in destinos for x in [*lista, *apoio]), ident
        competencias.append({"id": ident, "competencia_resumida": titulo,
                             "destinos": lista, "ferramentas_e_casos": apoio,
                             "melhoria_pendente": pendencia,
                             "evidencia_nesta_etapa": "mapeamento documental; sem novo teste externo"})
    assert {c["id"] for c in competencias} == {f"P{x:02d}" for x in range(1, 21)}
    historicos = []
    for f in anterior["historicos_excluidos"]:
        assert hashlib.sha256((RAIZ / f["fonte"]).read_bytes()).hexdigest() == f["sha256"]
        historicos.append({**f, "destino": "histórico de produção, fora da leitura"})
    pdf = RAIZ / "08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf"
    pdf_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert pdf_hash == composicao["sha256_pdf"]
    dados = {"registro": 99, "data": "2026-10-28", "estado": "estrutura proposta; não aplicada ao livro",
             "pdf_base": {"paginas": composicao["paginas"], "sha256": pdf_hash},
             "destinos": destinos, "fontes": resultado, "recortes": recortes,
             "competencias": competencias, "historicos_excluidos": historicos,
             "cortes_editoriais_preservar": anterior["cortes_editoriais"],
             "limites": ["Ações são instruções para a próxima redação, não mudanças já executadas.",
                         "Usos complementares não mandam duplicar texto integral.",
                         "As âncoras antigas devem ter destino ou alias na integração futura.",
                         "O documento 99 não migra regras nem valida aprendizado ou equilíbrio."]}
    (APOIO / "estrutura-e-fontes.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n")
    linhas = ["# Mapa de reaproveitamento das 104 fontes", "",
              "Registro 99, 28/10/2026. Destinos propostos para a próxima redação. Nada desta tabela foi aplicado ao PDF atual.", "",
              "A página é a inicial da fonte no PDF atual de 357 páginas. A ação é a intervenção predominante; os usos complementares especificam recortes ou referências, sem duplicar o texto inteiro. Condensar preserva requisitos, custos, prazos e exceções. N01–N10 são os novos capítulos; A–D são os apêndices do sumário proposto.", "",
              "[Sumário comentado e quatro caminhos](../99-sumario-comentado-e-caminhos-de-leitura.md) · [Dados técnicos](estrutura-e-fontes.json)", "",
              "| Fonte e título atuais | Página atual | Ação | Destino principal | Reaproveitamento complementar e motivo |",
              "|---|---:|---|---|---|"]
    for f in resultado:
        outros = "; ".join(destinos[x] for x in f["usos_complementares"])
        linhas.append(f"| [{f['id']} · {f['titulo_atual']}](<../../{f['fonte']}>) | {f['pagina_inicial_atual']} | {f['acao']} | {destinos[f['destino_principal']]} | {outros}. {f['orientacao']} |")
    linhas += ["", "## Recortes que precisam ser preservados", "",
               "Estas subseções têm destino específico. As outras partes seguem o destino e as orientações da linha da fonte.", "",
               "| Fonte | Seção atual | Destino |", "|---|---|---|"]
    linhas += [f"| {x['fonte_id']} | {x['secao_atual']} | {destinos[x['destino']]} |" for x in recortes]
    linhas += ["", "## Histórico fora da leitura", ""]
    linhas += [f"- [{f['fonte']}](<../../{f['fonte']}>): {f['motivo']}" for f in historicos]
    linhas += ["- Manter também os cortes editoriais já identificados no mapa da edição atual, especialmente o detalhamento descartado de Reserva Condensada e as notas de produção dos pilotos.", "",
               "Não há fonte integrada inteira sem destino ou destinada ao descarte. Os cortes serão de repetição, notas de produção e aprofundamentos redistribuídos, com histórico preservado. Isso não obriga manter cada parágrafo no PDF: a seleção final precisa preservar a explicação, a aplicação necessária e as condições mecânicas.", ""]
    (APOIO / "mapa-de-reaproveitamento.md").write_text("\n".join(linhas))
    linhas = ["# Competências e melhorias pendentes", "", "Registro 99, 28/10/2026. Reutiliza os IDs P01–P20 da matriz existente. Esta tabela liga conteúdo e tarefas; não certifica aprendizagem.", "",
              "[Matriz original](../04-competencias-que-o-livro-deve-ensinar.md) · [Sumário comentado](../99-sumario-comentado-e-caminhos-de-leitura.md)", "",
              "| Competência | Onde será ensinada | Ferramentas e casos | O que ainda precisa melhorar ou ser avaliado |", "|---|---|---|---|"]
    for c in competencias:
        locais = "; ".join(destinos[x] for x in c["destinos"])
        apoios = "; ".join(destinos[x] for x in c["ferramentas_e_casos"])
        linhas.append(f"| {c['id']} · {c['competencia_resumida']} | {locais} | {apoios} | {c['melhoria_pendente']} |")
    linhas += ["", "## Lacunas e limites mantidos visíveis", "",
               "- P01/P05: a missão reunida e o preparo mínimo serão redigidos nas etapas 2–3; esta estrutura ainda não os substitui.",
               "- P03/P06/P12: variedade, combinações de ideias e negociação precisam dos complementos previstos, não apenas da mudança de ordem.",
               "- P09/P10/P11: desenvolver e conferir ritmo, participação e propostas inesperadas nas situações indicadas no plano 98.",
               "- P14: números e dificuldade continuam experimentais. A construção geral de encontros exige uma frente própria de avaliação; não há nova validação nesta entrega.",
               "- P18: a aplicação por outro mestre e o uso em campanha fechada ainda precisam ser observados quando houver participantes.",
               "- P20: manter decisões e o alcance das propostas; não reintroduzir detalhamento descartado de Reserva Condensada nem novos treinamentos.",
               "- A matriz dos 130 pontos permanece como inventário mecânico e será conferida novamente na integração. O mapa das 104 fontes evita fonte esquecida, mas sozinho não demonstra preservação semântica de cada ponto.", ""]
    (APOIO / "competencias-e-lacunas.md").write_text("\n".join(linhas))
    verificacao = {"registro": 99, "fontes_integradas": len(resultado),
                   "fontes_sem_destino": [], "ids_duplicados": [], "destinos_invalidos": [],
                   "recortes_com_titulo_conferido": len(recortes), "competencias_mapeadas": len(competencias),
                   "historicos_excluidos": len(historicos), "fontes_inalteradas": True,
                   "pdf_inalterado": True, "pdf_sha256": pdf_hash,
                   "acoes_planejadas": dict(Counter(x["acao"] for x in resultado)),
                   "etapa_1": "entregue; reorganização do livro ainda pendente"}
    (APOIO / "verificacao.json").write_text(json.dumps(verificacao, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(verificacao, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

# Pressão e sobrevivência do Sineiro

26 de outubro de 2026. Continuação da reconstrução do chefe. **Recomendação do assistente: ensaiar 108 PV e 54 de Integridade, mantendo as demais capacidades da versão 1.** Essa passa a ser a versão 2 experimental nas seções 71/72. Não é uma regra de vida por nível nem uma aprovação autoral de equilíbrio.

A análise encontrou pouco tempo de atuação contra um trio que concentra feitiços ofensivos, mas também mostrou que dano, controle e desgaste precisam ser avaliados separadamente. Aumentar dano agora agravaria o risco para pessoas já feridas. Aumentar CD ou impedir controles enfraqueceria as respostas que dão sentido ao encontro.

## O que foi calculado

[Resultados completos](apoio-pressao-sineiro/resultados.json) e [cálculo reproduzível](apoio-pressao-sineiro/calcular.py). Foram enumerados os resultados possíveis dos dados e acumuladas suas probabilidades, com arredondamento na apresentação. **Não houve sorteio de milhares de combates ou simulação integral de mesa.**

Há três recortes: dano e controle de uma ação; sobrevivência a uma sequência declarada de ações ofensivas; e a janela entre o começo do confronto e a primeira oportunidade de impacto. Alcance, percepção, recursos e oportunidade de agir são condições desses recortes. Não se calcula uma taxa de vitória da missão.

Os ataques com Bloquear incluem duplo 10, duplo 1 e prevalência do 20 natural. Seus revides pagos por Reação **não são executados**. Por ataque normal bloqueado, Aparar oferece um gatilho de resposta em 0,95% dos resultados e Brecha em 1%; ainda seriam necessários Reação, alcance e requisitos. As tabelas de defesa isolam o ataque inicial, sem afirmar equivalência de valor entre Defesa estática e Bloquear.

## Perfis de referência

São **recortes de personagens**, não fichas completas nem representantes de todas as montagens de cada Caminho. Nível 6, Maestria 1, Refino 2, marco Corpo. Cada um soma 11 pontos: nove iniciais, um do marco e um de Corpo. O atributo ofensivo e Constituição aumentaram em um. Traje 1, Destreza 2, Defesa 13; nenhuma situação favorável do Traje foi presumida.

| Referência | Força / Destreza / Constituição / Inteligência / Essência | PV | PE | Integridade | TR Físico |
|---|---|---:|---:|---:|---:|
| Bastião | 4 / 2 / 3 / 1 / 1 | 65 | 24 | 50 | +5, Força treinada |
| Emanador | 0 / 2 / 3 / 4 / 2 | 44 | 36 | 55 | +3, Destreza treinada |
| Guia | 0 / 2 / 3 / 2 / 4 | 51 | 30 | 65 | +2, Destreza sem treino |

Os demais TRs treinados devem ser escolhidos ao completar as fichas. Constituição foi recalculada em todos os níveis. Integridade de jogador usa **20 + (Essência + 5) × 5**, não metade dos PV. O Bastião ainda não tem Ataque Extra, adquirido no nível 7.

**Ataque de comparação:** Classe 2, Padrão, 6 PE, ataque +5, 6d8 de Concussão. Base de dano zero, seis pontos, sem Melhorias ou Restrições. O Bastião usa Toque a 1,5 m, palavra como Selo e uma mão livre; os outros usam Projétil a 18 m, com seus Selos e mãos disponíveis. Cada técnica precisa comportar esse dano e sua aplicação. O recorte não concede efeitos além da montagem.

A sequência de seis declarações usa dois feitiços por pessoa: 12 PE por personagem. Isso cabe nas reservas cheias, mas não numa ficha que já tenha gasto esse recurso em outras atividades. Sobras de Padrão, Bônus ou espaço de repertório não viram feitiços adicionais automaticamente.

**Comparação mista:** Bastião usa uma Espada Longa em uma mão, +5, 1d8 + 4 + 1d4 de Canalizar; os outros continuam com feitiços. O crítico dobra apenas o d8 da arma. Esse recorte não executa Kokusen, efeitos específicos da arma ou respostas de Caminho; não representa o teto de dano de um combatente. Tampouco soma Trocação Franca e Alicerce, que pertencem a Trilhas diferentes.

Origens, Trilhas, demais aptidões, cura e habilidades situacionais não estão integralmente preenchidas. Quando uma capacidade importante é discutida abaixo, ela é uma sensibilidade separada, não um benefício oculto na tabela.

## Sobreviver às ações do grupo

Cada linha conserva ataque, dano e Defesa do Sineiro; muda apenas sua reserva de vida e a Integridade derivada. O dano desta comparação não é de Alma. A sequência é Bastião → Emanador → Guia, repetida uma vez. O Sineiro usa Defesa 11 nesta tabela.

| PV / Integridade | Vivo após 3 feitiços | Vivo após 4 feitiços | Vivo após 6 feitiços | Vivo após 4 ações no recorte misto |
|---|---:|---:|---:|---:|
| 72 / 36 | 58,4% | 29,3% | 5,2% | 67,6% |
| 108 / 54 | 95,5% | 75,5% | 26,8% | 98,2% |
| 144 / 72 | 99,9% | 97,4% | 65,1% | 99,98% |

**Uma declaração pode errar.** Esses números incluem erros e críticos; não são a chance de sobreviver a quatro acertos garantidos. Também não dividem PV por dano médio para adivinhar rodadas. As ações do Sineiro, deslocamentos, respostas e eventuais ações perdidas dos personagens ficam fora dessa sequência.

Um feitiço +5 contra Defesa 11 acerta em **75%**, incluindo 5% de críticos, e produz **21,60 de dano médio por declaração**. Contra Bloquear 2d10, acerta em **73,75%** e produz **21,26**, antes dos revides. Trocar a defesa, sozinho, muda pouco esta pressão inicial.

A diferença entre as últimas colunas mostra por que 72 PV não é um erro universal. Com menos gasto ofensivo, essa reserva já dura mais. **108 PV é a candidata para o próximo ensaio**, especialmente contra três personagens que consigam concentrar Classe 2; não se recomenda aplicar o valor a todo grupo apenas pelo nível. A opção 144 resiste mais, mas traz risco de alongar muito um confronto de baixa produção de dano.

## A primeira preparação do sino

Ordem fixa: **Bastião → Sineiro → Emanador → Guia**. O Bastião age antes do chefe; este tenta Agarrar, usa uma Pancada e prepara o sino. Emanador, Guia e Bastião agem antes do próximo turno do Sineiro. Portanto, são quatro ações de personagem antes da primeira oportunidade de impacto.

Neste recorte, eles permanecem aptos a agir e escolhem as ações da tabela. O alvo de uma única Pancada não cai a partir dos PV cheios desses perfis. A captura não impede, por si, conjurar. Alcance, Selos, visão e trajeto das aplicações precisam estar disponíveis; não se teleporta ninguém para cumprir a hipótese.

| Escolha ofensiva na janela | Vivo e com preparo, 72 PV | Vivo e com preparo, 108 PV | Vivo e com preparo, 144 PV |
|---|---:|---:|---:|
| Todos priorizam 6d8 | 29,3% | 75,5% | 97,4% |
| Emanador usa 5d8 + Empurrão | 14,6% | 23,9% | 25,0% |
| Guia usa 5d8 + Guarda Aberta, CD 13 | 19,9% | 40,7% | 44,8% |
| Guia usa Guarda Aberta sem dano, CD 15 | 20,5% | 33,4% | 34,9% |

A tabela mostra **poder tentar o impacto**, não a probabilidade de atingir alguém. A zona pode estar vazia, a presa pode ter escapado ou o Sineiro pode desistir. As escolhas de controle são alternativas: não foram todas realizadas juntas.

**Empurrão:** Classe 2, Projétil, Melhoria Leve de Alcance por 1 ponto, saldo 5d8 e 6 PE. Depois de acertar, pode mover até 6 m por percurso válido, cancelando o preparo corporal. Não exige TR adicional e não usa o limite de tamanho da manobra comum. Sua função e o espaço continuam obrigatórios. Na tabela, pode mover pelo menos um passo.

**Guarda Aberta:** Classe 2, Projétil, Condição Leve por 1 ponto. Uma aplicação cuja Regra justifique pressão sobre o espírito foi registrada por **TR Espírito CD 13**, 5d8 e metade no sucesso. Falha aplica a condição por uma rodada. Uma segunda versão, conhecida separadamente, descarta o dano e usa o reforço de Controle: **CD 15 e duas rodadas**. Cada versão custa Padrão e 6 PE. Não se troca a opção de reforço durante o uso. A condição cancela o preparo e solta a presa; não remove todas as ações do chefe.

Com 144 PV, um Empurrão ainda deixa só cerca de um quarto dos resultados com preparação disponível. **Mais vida sustenta a presença do chefe; a interrupção continua oferecendo uma vitória aos jogadores.** Não acrescentar imunidade apenas para garantir o impacto roteirizado.

## Captura, fuga e exposição

Agarrar CD 13 contra os TRs Físicos +5, +3 e +2 captura em **35%, 45% e 50%** das tentativas. Se a pessoa capturada gastar a Padrão para tentar escapar, a chance de a sequência “capturar e resistir à fuga” se completar, sem outros modificadores, é **12,25%, 20,25% e 25%**, respectivamente. São duas rolagens, não a duração completa de um agarrão. Sair do alcance do chefe depois da fuga pode provocar oportunidade; esse ataque não permite um novo Agarrar.

Escapar também custa ao grupo a ação que poderia causar dano. A comparação ofensiva anterior não cobra ao jogador uma fuga e um feitiço na mesma Padrão. Resgatar, deslocar ou abrir a guarda pode ser mais vantajoso que insistir em testes pessoais, dependendo da ficha e do espaço.

Uma manobra comum de Força 4 e Maestria 1 tem CD 13: contra o Físico +5 do Sineiro, funciona em **35%**. Exige corpo, tamanho e alcance válidos. Estágio 3 de Integridade impõe desvantagem ao TR do inimigo, elevando a chance de ele falhar para **57,75%**. Agarrá-lo restringe movimento, mas não cancela sozinho sua preparação.

A exposição depois do impacto favorece ataques físicos próximos. A Espada Longa do recorte passa de **8,48 para 11,63 de dano médio por declaração** contra Defesa 11, sem Kokusen. **Feitiço de Toque continua sendo conjuração:** não ganha crítico automático por Guarda Aberta. Para um grupo que use sobretudo feitiços, o ganho dessa exposição pode ser bem menor. Bloquear fica indisponível, mas a Defesa estática permanece.

## Pressão sobre personagens

Uma Pancada +5, 2d6 + 4 contra Defesa 13 causa **7,50 em média por declaração**; duas produzem 15 antes de outras defesas. Contra Defesa 16, cada uma cai para **5,85**. Defesa 16 é possível, por exemplo, com Revestimento 1 e escudo Médio, respeitando Força, preparo, mãos e carga; não foi concedida de graça aos três perfis.

Se o impacto ocorrer com alguém na zona, os danos médios são **15,35** contra TR +5, **16,45** contra +3 e **17,00** contra +2. Bloquear não substitui esses TRs. A chance de sucesso reduz dano, mas não elimina toda a ameaça.

Uma aplicação isolada de 5d8 não derruba esses perfis a partir dos PV cheios: seu máximo é 40 e o menor máximo de vida é 44. O resultado muda com ferimentos anteriores. **Condicionando à exposição a uma declaração de Pancada e depois ao impacto concluído**, sem proteção adicional:

| Perfil | PV cheios: chance de chegar a zero | Começando ferido | Chance de chegar a zero nessa sequência |
|---|---:|---:|---:|
| Bastião | Menos de 0,01% | 32 PV | 16,6% |
| Emanador | 1,7% | 22 PV | 60,6% |
| Guia | 0,2% | 25 PV | 47,8% |

Isso não é a chance de queda no encontro: a preparação ainda precisa ocorrer e o alvo continuar exposto. **Zero de vida não foi contado como morte ou derrota automática de jogador.** A análise termina nessa primeira queda; Insistir, Aguentar, socorro e Sequelas continuam necessários numa simulação integral.

Sensibilidades importantes:

- **Bastião/Muro:** se escolheu resistência a Concussão no descanso longo e ativou Olhos Em Mim, o impacto contra TR +5 cai para **7,93 em média**. Não supor essa escolha retroativamente. A resistência não exige interceptar, mas a área ofensiva e Agarrar por TR não podem ser assumidos pela interceptação de ataque rolado.
- **Cobrir-se de Energia:** Refino 2 permite reduzir 3 de um golpe por Reação e 2 PE. Não reduz de graça cada Pancada e o impacto. Com Traje, não perde sua proteção de equipamento.
- **Guia:** Executar pode dar vantagem a um ataque, levando +5 contra Defesa 11 a **93,75% de acerto**, com 9,75% de crítico; custa Bônus, 1 PE, aliado elegível e uso antes da expiração. Resguardar ajuda um TR; a mesma Abertura não faz as duas coisas.

Não aumentar o dano apenas porque pessoas descansadas suportam uma aplicação. A missão já pode impor captura, perda de posição e gasto de ações; feridos precisam de uma leitura diferente de risco.

## Integridade e acesso a Alma

| PV / Integridade máxima | Perda para estágio 1 | Para estágio 2 | Para estágio 3 | Para derrota por Integridade |
|---|---:|---:|---:|---:|
| 72 / 36 | 9 | 18 | 27 | 36 |
| 108 / 54 | 14 | 27 | 41 | 54 |
| 144 / 72 | 18 | 36 | 54 | 72 |

As frações são comparadas antes de arredondar os limiares para quantidades inteiras de dano. No candidato 108/54, perder 13 ainda não alcança um quarto. Dano de Alma legal reduz PV e Integridade, salvo regra específica; pode diminuir o movimento e depois prejudicar ataques e TRs antes de zerar a vida. O Sineiro não ganha cobranças de PE em suas ações corporais por isso.

**Não foi usado 6d8 de Alma como ataque normal de nível 6.** A entrada [Toca a Alma](apoio-carregador/fontes/LIVRO-COMPLETO-R53.md#catalogo--melhoria-toca-a-alma) exige Classe 3, Regra sobre alma e redução dos dados pela metade. Ela não está disponível por Classe 2. A escolha geral de tipos no Fundamento precisa ser distinguida de uma permissão específica ou de uma conversão por essa peça antes de preparar um perfil com Alma. Esta análise não resolve essa questão autoral por suposição nem altera o livro-base. Os limiares acima permitem avaliar um efeito cuja legalidade já esteja estabelecida.

## Alteração entregue

Nas seções 71/72, a segunda versão usa **108 PV / 54 de Integridade**, sem aumentar Defesa, CD, dano, ataques, alcance ou resistências. Atualizados estágios e limiares de destruição. A Doma conserva **38 PV / 19 de Integridade**, porque seu resultado usa a construção da R53, não uma proporção da vida inimiga. A aquisição ainda não cura.

Excedente para destruição agora precisa superar 54, ou uma ocorrência direta alcançar os 108 PV máximos. A partir de 5 PV, dano direto 59 deixa excedente 54 e não satisfaz esse critério; 60 deixa 55 e destrói. Dano em área mantém sua regra própria.

O texto de consulta explica o motivo do ajuste, preserva 72 como referência da versão anterior e remete a esta comparação. Nenhum número virou escala universal. O dano ficou igual porque a análise já mostra risco relevante para pessoas feridas; o controle continua funcionando porque é parte do objetivo de desenho.

## Fontes, revisão e preservação

R53 local conferida em 26/10/2026; livro atual e cópia de apoio com SHA-256 **7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d**. Leitura dirigida: progressão e marcos; características de Bastião/Emanador/Guia; ataque, crítico, Bloquear/Aparar/Brecha; manobras; Controle, Empurrão, Condição, Toca a Alma; Integridade, resistência e derrota; Traje, Revestimento, escudo; Canalizar e Cobrir-se. A comparação externa permanece no registro 71; não houve nova coleta externa.

A skill de redação acessível orientou a revisão: “29% de sucesso do chefe” foi evitado em favor de **“29% de permanecer vivo e com preparação nessa sequência declarada”**, pois sobrevivência não garante alvo ou dano. “Dano de uma rodada” foi substituído por **“dano por declaração ou sequência”**, evitando omitir ações e tempo. Ficha inimiga e ficha domada conservam valores separados e explicados.

Dezoito verificações nomeadas de probabilidades, dados, limiares e destruição, mais invariantes de sobrevivência e preparação. Incluem reprodução independente da chance de 59,85% publicada no piloto para ataque +4 contra Defesa 13 com Bloquear. O cálculo não executa nem altera o verificador antigo do piloto. Limites do modelo acompanham os resultados.

Estado inicial: **263 arquivos íntegros**. [Estado anterior](apoio-pressao-sineiro/estado-inicial.json), cópias dos dez arquivos atualizados e [verificação final](apoio-pressao-sineiro/verificacao.json). Registro 06, P72, dados anteriores, livro-base e coleções de pesquisa preservados. Plano 63, pauta 57, planejamento até 73; manuscrito continua até 72, com revisão das duas fichas. Salvamento local, sem publicação no GitHub nesta etapa.

**Próxima tarefa recomendada:** conduzir um ensaio guiado da versão 2, com três perfis de nível 6, posições, recursos e escolhas de captura, interrupção, resgate e retirada; incluir as capacidades de Caminho usadas e a passagem de zero de vida para socorro. Conferir também um grupo com menor uso de feitiços antes de fixar a referência. **GPT-6 Astra, esforço extra alto**, para mecânica; **GPT-6.1 Sol, esforço alto**, para clareza. Bestiário integral e treinamentos continuam adiados.

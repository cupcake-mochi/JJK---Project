# Projeto M — Manual da Guilda

*RPG de mesa de Jujutsu Kaisen. Texto corrido para revisão: sem diagramação, na mesma ordem do PDF.*

*As seções “Notas de revisão” dos arquivos-fonte não entram aqui, igual não entram no PDF.*


---


# Bem-vindo à Guilda

*fonte: `manual/05-introducao.md`*

Você vai criar um feiticeiro. Alguém que nasceu com energia amaldiçoada, ou que aprendeu a lidar com quem tem, e que agora anda entre o mundo comum e o mundo jujutsu: o das maldições, dos clãs, da instituição que treina quem sobrevive aos dois.

Este é um sistema de mesa feito para um servidor de guilda. Várias pessoas mestrando, e personagem que atravessa mesas diferentes com o mesmo dono. A ficha que você monta aqui pode sentar em mais de uma mesa, com mestres diferentes, e continuar sendo a mesma pessoa.

## Material da mesa

- **Um mestre.** Quem prepara a cena, interpreta todo mundo que não é personagem de jogador, e decide o que as regras não cobrem.
- **Um grupo.** De cinco a sete jogadores é o tamanho que este sistema pressupõe, mas qualquer grupo funciona.
- **Dados.** Um d20 e um punhado de d8 resolvem quase tudo. Aparecem também d4, d6, d10 e d12, quase sempre como dado de dano de arma.
- **Uma ficha.** Papel, planilha ou o que a sua mesa usar.

## Organização do manual

Nem todo capítulo é para ler do começo ao fim. Metade dos capítulos é catálogo, e catálogo se abre quando você está montando alguma coisa. A coluna *Para quê* diz qual é qual.

**Capítulos**
| | Capítulo | Para quê |
|---|---|---|
| | **O vocabulário do sistema** | *consulta* · toda palavra que este manual usa com significado próprio, em uma linha |
| | **Antes da primeira sessão** | *cena pronta* · uma ficha e um combate guiados, para jogar hoje sem ter lido o resto |
| | **O JOGO** | |
| **1** | Como Jogar | *ler* · o dado, o teste, o acerto, a defesa, e o que acontece quando a vida acaba |
| **2** | O Turno | *ler* · a iniciativa e as doze ações |
| **3** | Perícias e Ofícios | *ler, depois consultar* · as vinte e três perícias e os onze ofícios |
| **4** | Dano, Condições e Cobertura | *consulta* · os catorze tipos de dano, as catorze condições, e a mureta no meio do caminho |
| **5** | Descanso e Recuperação | *ler* · o que volta entre uma luta e a seguinte |
| | **O PERSONAGEM** | |
| **6** | Criação de Personagem | *ler, com a ficha na mão* · oito passos, de vinte a quarenta minutos |
| **7** | Origens e Legados | *consulta* · de onde vem o seu poder, e o que você já trazia |
| **8** | Caminhos e Trilhas | *consulta* · o seu lugar numa equipe |
| **9** | Fundamento | *ler uma vez, depois consultar* · a sua técnica, e como se monta feitiço com ela |
| **10** | Aptidões e Refino | *consulta* · o que qualquer feiticeiro pode aprender, técnica à parte |
| **11** a **13** | Equipamento · Ferramenta Amaldiçoada · Invocações | *consulta* · o que você carrega e o que você põe em campo |
| | **A CAMPANHA** | |
| **14** | Experiência e Progressão | *consulta* · o que cada nível entrega, do 1 ao 30 |
| **15** | Apêndice · Bloquear | *decisão de mesa* · Defesa parada ou rolar `2d10` pra se defender — os dois são regra do sistema |
| | **Índice remissivo** | no fim: termo, e em que página ele aparece |

**Grupo novo, sem ninguém ter lido nada?** Vá direto para *Antes da primeira sessão*, logo depois desta introdução. É uma cena pronta, com ficha e tudo, para jogar antes de estudar o resto.

**Leia Como Jogar antes de qualquer outra coisa.** É o capítulo dono do vocabulário que todos os outros usam sem parar para explicar de novo. Depois dele, pular direto para o que te interessa funciona.

**E se esbarrar num nome que ninguém te apresentou**, ele está no vocabulário, logo na página seguinte, com o número do capítulo que trata dele por extenso.

---


# O vocabulário do sistema

*fonte: `manual/07-glossario.md`*

Cada termo vem com uma linha de explicação e o número do capítulo que trata dele por extenso. Nada aqui é regra completa.

## Rolagens

**Rolagens**
| Termo | O que é | Cap. |
|---|---|---|
| **Teste** | `d20` + atributo, comparado com uma CD. Igualou ou passou, você conseguiu | 1 |
| **CD** | O número que a tarefa pede. Quem diz qual é o mestre, numa escada de 10 a 26 | 1 |
| **Vantagem** | Role dois `d20` e fique com o melhor | 1 |
| **Desvantagem** | Role dois `d20` e fique com o pior | 1 |
| **Maestria** | Bônus que mede tempo de estrada. Começa em 1 e sobe a cada oito níveis. Entra em toda rolagem de ataque, na CD dos seus feitiços, e no que você treinou — perícia, ofício e Teste de Resistência | 1 |
| **Teste de Resistência** | O que **você** rola quando algo acontece com você. São quatro: Físico, Vigor, Intelecto e Espírito | 1 |
| **Defesa** | `10` + Destreza + proteção. O número que o inimigo precisa alcançar para te acertar | 1 |
| **Crítico** | `20` natural numa rolagem de acerto. Dobra os dados da arma ou da Classe, e nada mais | 1 |
| **`Bloquear`** | Regra opcional: role `2d10 + (Defesa − 11)` e use no lugar da Defesa parada. A mesa escolhe se usa | 17 |
| **`Aparar`** | O duplo 10 no `Bloquear`. O ataque não acerta, e você pode gastar a Reação para revidar com `+3` de dano | 17 |
| **Arredondamento** | Sempre para o lado que não te favorece. O que você paga sobe, o que você ganha desce | 1 |
| **Rotina** | O dano que um personagem entrega numa rodada comum, sem gastar recurso guardado | 15 |

## Números da ficha

**Números da ficha**
| Termo | O que é | Cap. |
|---|---|---|
| **Atributo** | Cinco, de 0 a 6: Força, Destreza, Constituição, Inteligência, Essência. O número **é** o modificador | 1 |
| **Pontos de vida** | O corpo. Vêm do Caminho mais a sua Constituição, a cada nível | 1 |
| **Pontos de energia** (`PE`) | O combustível dos feitiços. PE por nível do Caminho × o seu nível. Numa ficha sem energia amaldiçoada a mesma sigla se lê **Pontos de Esforço**, e nenhuma regra pergunta qual das duas você tem | 1 |
| **Integridade** | A vida da alma. `20 + 8 × (nível − 1)`, igual para todo mundo. Só volta com descanso longo | 1 |
| **`Vida temporária`** | Anteparo, não vida. Gasta antes da vida real, não acumula, teto de metade da vida máxima, some no fim da cena | 1 |
| **Proteção** | O que soma na Defesa: o uniforme que você veste, ou a energia com que você se cobre | 13 |
| **Redução de Dano** | Desconto no dano que já passou pela Defesa. Não é a mesma coisa que proteção | 9 |
| **Perícia** | Uma das vinte e três. Cada uma tem um atributo fixo. Sem treino você ainda tenta | 3 |
| **Ofício** | Um dos onze. Não tem atributo fixo, e sem treino você **não** tenta | 3 |
| **Condição** | Estado nomeado que muda o que você consegue fazer. São catorze, em três níveis: `Leve`, `Média` e `Pesada` | 4 |
| **`Leve`** [Nível] | O menor dos três níveis. Como preço de Melhoria, custa metade da Classe; como condição, sai por `1` ponto de energia | 4 |
| **`Média`** [Nível] | O nível do meio. Como preço, custa a Classe; como condição, sai por `2` pontos de energia | 4 |
| **`Pesada`** [Nível] | O maior. Como preço, custa Classe e meia; como condição, sai por `3` pontos de energia. Dá Teste de Resistência no fim de cada turno do alvo | 4 |
| **Exaustão** | Relógio de descanso, em três degraus. **Não é condição neste sistema** | 5 |
| **Sequela** | O que você ganha ao levantar de uma queda. Encurta em uma rodada a janela da queda seguinte | 1 |
| **Cicatriz** | Permanente, ganha na segunda queda. Não sai no descanso | 1 |

## Personagem

**Personagem**
| Termo | O que é | Cap. |
|---|---|---|
| **Caminho** | O seu lugar numa equipe. Cinco: Bastião, Vanguarda, Guia, Emanador, Evocador. Escolhido na criação, para sempre | 8 |
| **Trilha** | Quem você é dentro do Caminho. Três por Caminho, quinze no total | 8 |
| **Origem** | De onde vem o seu poder. Sete, mais a sub-origem Sem Técnica | 7 |
| **Legado** | O que você já trazia, das listas da sua Origem. Dois por ficha | 7 |
| **Traço** | Marca de história vinda da Origem, sem número | 7 |
| **Pacto** | O que você trocou por poder. Opcional. Três das quatro formas dele são `Restrição`, `Regra Própria` ou Legado; a quarta, o trato entre dois personagens, não entra na criação | 6 |
| **Patente** | O seu reconhecimento na instituição, de Grau 4 a Grau 1. Todo personagem começa **Grau 4** | 7 |

> **Cuidado com a palavra `Grau`.** Ela nomeia duas escadas de cinco casas que não se encostam: a **patente** de um feiticeiro e o **grau** de uma ferramenta amaldiçoada. Patente é reconhecimento; grau de ferramenta é a energia que a peça carrega. O capítulo 14 abre a diferença.
## Técnica

**Técnica**
| Termo | O que é | Cap. |
|---|---|---|
| **Fundamento** | A sua técnica inata, escrita por você na criação. Nunca muda. Descrição, Regra, Famílias, Selo e Passivas | 9 |
| **Regra** | A frase única que resume a técnica. Todo feitiço seu precisa caber nela | 9 |
| **Feitiço** | Uma aplicação concreta da técnica, com nome próprio, montada por você com pontos | 9 |
| **Classe** | O tamanho do feitiço, de 0 a 7. Define pontos, PE, teto e limites | 9 |
| **Pontos** | O orçamento do feitiço: `3 × Classe`. Cada ponto que sobra vira `1d8` de dano | 9 |
| **Teto** | O máximo de dados de dano, somando alvos e repetições: `4 × Classe` | 9 |
| **Forma** | Como o feitiço sai: `Projétil`, `Toque`, `Explosão`, `Aura`, `Cone`, `Linha`, `Cura`, `Apoio`, `Onda`, `Efeito` | 9 |
| **Melhoria** | O que você compra com ponto. Custa `Leve`, `Média` ou `Pesada` | 9 |
| **Restrição** | O que você vende para recuperar ponto. Paga Melhoria, **nunca vira dano** | 9 |
| **Família** | Um dos nove grupos de Melhoria. Na criação você fecha duas como Livres e três como Fechadas | 9 |
| **Selo** | O que você sempre faz para conjurar. Não custa nem devolve ponto | 9 |
| **Classe 0** | O feitiço grátis: não gasta PE, não ocupa espaço na lista e não se monta | 9 |
| **Passiva** | Efeito que fica ligado sozinho. Custa espaço de feitiço | 9 |
| **Classe Passiva** | A altura de uma Passiva, de Livre a 3. Diz quantos espaços ela cobra e em que nível abre | 9 |
| **Espaço de feitiço** | `2 + (nível ÷ 2)`, arredondando para baixo, mais um por marco. É a moeda que Passiva e Expansão de Domínio também gastam | 16 |
| **Ampliar** | Lançar um feitiço que você conhece numa Classe maior, pagando o PE da Classe nova | 9 |
| **Liberação Máxima** | Feitiço à parte, escrito antes da sessão, de Classe 3 ou mais. Rompe o limite de dano num alvo só. Nos níveis 10, 20 e 30 | 9 |
| **Técnica Máxima** | O golpe de dano fixo que carrega o nome da técnica. Do nível 17 em diante | 9 |
| **Uso Livre** | O que a sua técnica faz de graça fora de combate, sem rolagem e sem montagem | 9 |
| **Expansão de Domínio** | O espaço fechado onde a sua técnica manda. Custa espaço de feitiço | 9 |
| **Dano na alma** | Tira vida, Integridade e vida máxima no mesmo tanto. Entra cheio, e tem quatro estágios | 4 |

## Técnica Marcial

Quem não escreve Fundamento monta o poder aqui. A máquina é a mesma; três nomes mudam.

**Técnica Marcial**
| Termo | O que é | Cap. |
|---|---|---|
| **Técnica Marcial** | O Fundamento com o corpo no lugar da energia. Mesmo orçamento, mesma montagem, e o equipamento no lugar do Selo | 10 |
| **`Kata`** | O feitiço desta rota: mesma Classe, mesmos pontos, mesmo custo | 10 |
| **`Ruptura`** | A Liberação Máxima desta rota. Nos níveis 10, 20 e 30 | 10 |
| **`Ōgi`** | A Técnica Máxima desta rota. Do nível 17 em diante | 10 |

## Bênçãos e Lapidação

O eixo de controle de quem não tem energia amaldiçoada nenhuma, no lugar do refino e das aptidões.

**Bênçãos e Lapidação**
| Termo | O que é | Cap. |
|---|---|---|
| **Lapidação** | Quanto do que o corpo tem chega até o fim do movimento. Começa em 1, teto 10. Sobe `+1` de graça em cada marco | 12 |
| **Bênção** | O que um corpo sem energia aprende a fazer. Catorze, e custa marco | 12 |
| **`Defesa sem Armadura`** | Bênção de graça: proteção `1/3 da Lapidação + 1`, e barreira de energia não segura você | 12 |
| **`Estímulo Muscular`** | Bênção de graça: vantagem numa perícia e num Teste de Resistência escolhidos, `1×` por cena | 12 |

## Progressão

**Progressão**
| Termo | O que é | Cap. |
|---|---|---|
| **Marco** | Um dos sete níveis em que a ficha muda de forma: **6, 10, 14, 18, 22, 26 e 30** | 16 |
| **Refino** | Quanto da sua energia você não desperdiça. Começa em 1, teto 10. Sobe `+1` de graça em cada marco | 11 |
| **Aptidão** | O que qualquer feiticeiro pode aprender, independente da técnica. Custa marco, e só marco | 11 |
| **Corpo**, **Refino**, **Leque** | As três escolhas que um marco oferece: mais atributo; mais refino e uma aptidão; ou mais feitiço e uma Passiva. Numa ficha sem energia, o eixo do meio é **Lapidação** e entrega Bênção | 16 |

## Turno

**Turno**
| Termo | O que é | Cap. |
|---|---|---|
| **Rodada** | Todo mundo teve o seu turno. 6 segundos | 2 |
| **Ação de Movimento** | Uma por turno. Compra até 9 metros de deslocamento, e o segundo saque do turno | 2 |
| **Ação Padrão** | Uma por turno. Atacar, conjurar, a maior parte das coisas | 2 |
| **Ação Bônus** | Uma por turno, e só o que a regra disser com todas as letras que é Ação Bônus | 2 |
| **Reação** | Uma por turno, responde a um gatilho e vale fora do seu turno | 2 |
| **Rodada inteira** | Custa a Ação de Movimento, a Ação Padrão e a Ação Bônus de uma vez. A Reação continua sua | 2 |
| **Concentração** | Manter um efeito de pé. Um por vez, e tomar dano pede Teste de Resistência de Vigor | 2 |
| **`Estudar`** | Ação Padrão: um teste sobre uma criatura ou objeto que você enxerga, para saber o que ele é e o que ele vai fazer | 2 |
| **Cobertura** | O que está entre você e quem atira. Três degraus: Parcial, Boa e Total | 4 |
| **`Agarrar`** | Opção do `Atacar`. Aplica a condição `Agarrado` | 2 |

## Condições

Catorze estados nomeados, em três níveis. `Leve`, `Média` e `Pesada` também nomeiam custo de
Melhoria — são escadas diferentes que usam as mesmas três palavras. O capítulo 4 separa as duas.

**Condições**
| Termo | O que é | Cap. |
|---|---|---|
| **`Agarrado`** | Seu deslocamento é `0`. Acaba se quem agarrou ficar `Incapacitado`, ou se algo tirar você do alcance dele | 4 |
| **`Amedrontado`** | Desvantagem em ataque e em teste enquanto você enxergar a fonte do medo, e você não se aproxima dela de vontade própria | 4 |
| **`Atordoado`** | Você perde a Ação Padrão e não usa reação | 4 |
| **`Cego`** | Você não enxerga. Falha automática em teste que precise de vista, desvantagem nos seus ataques, e quem ataca você tem vantagem | 4 |
| **`Derrubado`** | Está no chão, de pé no medidor. Vantagem a quem ataca de perto | 1 |
| **`Desarmado`** | A sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta | 4 |
| **`Enfeitiçado`** | Você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você | 4 |
| **`Lento`** | Seu deslocamento cai pela metade e você não usa Ação Bônus | 4 |

## Equipamento

**Equipamento**
| Termo | O que é | Cap. |
|---|---|---|
| **Ferramenta amaldiçoada** | Arma forjada para ferir maldição. Tem grau, de 4 a especial | 14 |
| **`Estigma`** | O efeito que uma ferramenta carrega. O grau dela decide o formato | 14 |
| **`Desgaste`** | Ferramenta usada demais antes de chegar em você: cada uso derruba o grau dela em um | 14 |
| **Invocação** | O que você põe em campo e comanda. Tem ficha própria, montada com orçamento | 15 |
| **Amarra** | A invocação tem de ficar a até 18 metros de você, ou não pode ser comandada | 15 |
| **`Emaranha`** | Propriedade de arma: você pode `Agarrar` sem largar a arma | 13 |
| **`Fineza`** | Propriedade de arma: no corpo a corpo, troca Força por Destreza no acerto e no dano | 13 |
| **`Longo Alcance`** | Propriedade de arma: ela alcança à distância, em metros | 13 |
| **`Oculta`** | Propriedade de arma: dá para esconder no corpo, com um teste de `Prestidigitação` | 13 |
| **`Par`** | Propriedade de arma: role dois dados de dano e fique com o melhor | 13 |
| **`Rompe`** | Propriedade de arma: vantagem contra objeto e estrutura | 13 |
| **`Talha`** | Propriedade de arma: `−1` no `Bloquear` de quem se defende | 13 |
| **`Versátil`** | Propriedade de arma: nas duas mãos, o dado sobe um passo | 13 |
| **`Vestida`** | Propriedade de arma: não ocupa a mão | 13 |
| **`Volumosa`** | Propriedade de arma: não dá para esconder, e atrapalha em espaço apertado | 13 |
| **`Remoto`** | Traço de invocação: funciona além dos 18 metros da amarra | 15 |
| **`Vigia`** | Traço de invocação: o que ela vê e ouve, você vê e ouve | 15 |
| **`Voo`** | Traço de invocação: voa, e o terreno para de valer para ela | 15 |

## Formas, Melhorias e Restrições do Fundamento

**Fundamento**
| Termo | O que é | Cap. |
|---|---|---|
| **`Projétil`** | Forma: 18 m, um alvo, rolagem de acerto | 9 |
| **`Toque`** | Forma: 1,5 m, um alvo. `Projétil` com `Corpo a Corpo` embutida | 9 |
| **`Explosão`** | Forma: esfera de raio 3 m, num ponto a até 18 m, Teste de Resistência | 9 |
| **`Cone`** | Forma: 4,5 m saindo de você, Teste de Resistência | 9 |
| **`Linha`** | Forma: 18 m por 1,5 m, Teste de Resistência | 9 |
| **`Apoio`** | Forma: um aliado a até 9 m, sem dano; o que sobra vira vida temporária | 9 |
| **`Onda`** | Forma: esfera de raio 3 m centrada em você, pega todos os aliados dentro | 9 |
| **`Efeito`** | Forma: fora de combate, sem dano | 9 |
| **`Corpo a Corpo`** | Restrição: `Projétil` vira `Toque`, `Explosão` vira `Aura`. `Cone` e `Linha` não pegam | 9 |
| **`Condicional`** | Restrição: só funciona quando uma condição de cena ou de alvo é verdadeira | 9 |
| **`Gesto`** | Restrição: precisa das duas mãos livres e de falar em voz audível | 9 |
| **`Parado`** | Restrição: você não se move no turno em que conjura | 9 |
| **`Uma Vez`** | Restrição: uma vez por cena | 9 |
| **`Fura`** | Melhoria: ignora até `3 × Classe` de Redução de Dano | 9 |
| **`Longe`** | Melhoria: sobe um degrau na escada de alcance. Pode comprar duas vezes | 9 |
| **`Maior`** | Melhoria: sobe um degrau de tamanho de área. Pode comprar duas vezes | 9 |
| **`Precisão`** | Melhoria: `+2` na rolagem de acerto, ou `+2` na CD do Teste de Resistência | 9 |

## Caminhos e Trilhas

**Trilhas**
| Termo | O que é | Cap. |
|---|---|---|
| **`Elo`** | Trilha do Guia: o que outra pessoa fez chega mais longe | 8 |
| **`Sutura`** | Trilha do Guia: Energia Reversa cedo, e nos outros | 8 |
| **`Torrente`** | Trilha do Emanador: mais de um feitiço na rodada, e a energia acaba | 8 |
| **`Explosivo`** | Trilha do Emanador: um feitiço só, e ele sai maior | 8 |
| **`Arremate`** | Trilha do Emanador: o feitiço acontece onde a mão chega | 8 |

## Palavras com sentido próprio

Estas palavras têm sentido próprio neste sistema.

**Palavras com sentido próprio**
| Palavra | Aqui ela quer dizer | E **não** quer dizer |
|---|---|---|
| **Classe** | o tamanho de um feitiço | a profissão do personagem |
| **Grau** | patente na instituição, **ou** a força de uma ferramenta | nada além disso |
| **Restrição** | o que você vende para recuperar pontos num feitiço | limite de movimento no turno |
| **`Incapacitado`** | você age, mas não se protege | você perde o turno — isso é `Atordoado` |
| **`Inconsciente`** | você chegou a 0 de vida | uma condição comprável — não é |
| **Exaustão** | relógio de descanso | condição — não é, e não se compra com a Melhoria `Condição` |
| **Essência** | perceber energia, trato social, hierarquia | força de vontade sozinha |
| **Refino** | quanto da sua energia não se perde | melhorar um item |

> **`Paralisado` não existe neste sistema.** O que outros jogos chamam assim se chama `Atordoado` aqui.


---


# Antes da primeira sessão

*fonte: `manual/08-inicio-rapido.md`*

Uma cena pronta para jogar hoje, sem ninguém ter lido o livro. Alguém lê em voz alta, ou
com as próprias palavras, e a mesa roda a cena com a Kaori — a ficha pronta que vem logo
abaixo.

## Regras da cena

> **Role um `d20`, some o seu bônus, compare com a CD.** Igualou ou passou, você conseguiu.
>
> **Vantagem:** role dois `d20` e fique com o melhor. **Desvantagem:** fique com o pior.
>
> **O seu turno tem quatro coisas:** uma Ação de Movimento, uma Ação Padrão, uma Ação Bônus
> (só se alguma coisa na ficha disser isso com todas as letras) e uma Reação.
>
> **Atacar** = `d20` + maestria + Força (corpo a corpo), Destreza (à distância) ou o
> atributo da sua técnica (conjuração), contra a **Defesa** do alvo.
>
> **Teste de Resistência** = `d20` + o atributo daquele Teste, mais a maestria se você for
> treinado nele. É o que **você** rola quando alguma coisa acontece com você.

Todo termo aqui tem explicação completa no capítulo 1 e no vocabulário do sistema, logo
atrás.

## Kaori

Feiticeira de nível 2, a mesma ficha de exemplo do capítulo 6.

**Quem ela é.** O clã da Kaori perdeu o nome faz três gerações, e ela cresceu ouvindo a
história de quem perdeu. A avó era a única que ainda sabia alguma coisa de valor — ervas,
principalmente — e fez questão de ensinar. Kaori entrou na instituição querendo provar que
o sobrenome ainda vale alguma coisa. Ninguém perguntou se ela queria.

**O que ela quer nesta cena:** sair sem que ninguém se machuque, inclusive ela. Kaori não
procura briga; ela entra na frente de quem procura.

**A técnica.** *"Tudo que eu prendo entre as minhas mãos fica mais pesado."* O Selo dela é
físico: as duas mãos precisam se tocar antes de qualquer feitiço sair.

**Kaori, nível 2**
| | |
|---|---|
| **Vida** | 23 |
| **Integridade** | 28 |
| **PE** | 8 |
| **Defesa** | 13 |
| **Iniciativa** | `d20 + 2` |
| **Ataque corpo a corpo (soco)** | `d20 + 4`, dano `d4 + 3` |
| **Ataque de conjuração** | `d20 + 4` — a técnica dela usa **Força** |
| **CD dos feitiços dela** | 12 |

> **`Peso nas Mãos`** · Classe 1 · Toque
> Ela toca o alvo com as duas mãos. **`d20 + 4` contra a Defesa dele.** Acertando: **3d8 de
> dano de concussão**, e o alvo fica `Derrubado` (condição).

> **`Corpo Duro`** · Reação, do Caminho Bastião
> Ao ser atingida, ela reduz o dano em **`2` (o nível dela) `+ 1d6`**. Ela pode fazer isso
> **duas vezes** (a Constituição dela) antes de precisar descansar.

> **`Alicerce`** · Ação Bônus, da Trilha Muro
> Ela se firma no lugar. Enquanto estiver firme, o dano `Cortante` e o dano `Concussão`
> caem pela metade contra ela, e o deslocamento dela também cai pela metade. Sair dali não
> custa nada.

## Corredor da ala oeste

Leia (ou narre) isto para o grupo:

> *A escola mandou vocês verificarem uma sala trancada na ala oeste, desativada desde o ano
> passado. O corredor está escuro cedo demais para o horário. No fim dele, encostada na
> porta que vocês precisam abrir, tem uma coisa do tamanho de um cachorro grande, toda
> pernas, sem cabeça que dê para apontar.*

Isso é uma **Maldição Menor**: Vida 14, Defesa 12, ataque `d20 + 3` por `1d6 + 2` de dano
`Cortante`.

**1 — Iniciativa.** Todo mundo rola `d20 + Destreza`. Kaori tem Destreza 2: ela tira 11 no
dado, soma 2, fica com 13. A maldição, mais rápida, tira 16 com Destreza 3: age primeiro.

**2 — O turno da maldição.** Ela avança e ataca: `d20 + 3` contra a Defesa 13 de Kaori. Sai
17: acertou. `1d6 + 2` de dano: sai 5. **Kaori pode gastar a Reação `Corpo Duro` agora.**
Ela gasta um dos dois usos: reduz `2 + 1d6`, tira 4 no d6, reduz 6. O dano de 5 cai para
zero. *O `Corpo Duro` reduz o dano depois que o golpe já acertou; ele não faz o inimigo errar.*

**3 — O turno de Kaori.** Três escolhas fazem sentido:

- **Gastar a Ação Bônus em `Alicerce`.** Se ela sabe que a luta vai continuar, plantar os
  pés agora corta o próximo golpe `Cortante` pela metade — e a maldição ataca com garra.
- **Gastar a Ação Padrão em `Peso nas Mãos`.** Precisa estar a `1,5 m`: ela anda até lá com
  o movimento e toca. Rola `d20 + 4` contra a Defesa 12 da maldição: tira 12, soma 4, fica
  16. Acertou. `3d8` de dano: sai 14. **A maldição, com 14 de vida, cai.**
- **Recuar e negociar.** Nem toda cena precisa terminar em dano. Se o grupo tiver outra
  ideia, ela vale tanto quanto as duas de cima.

**Se a maldição tivesse sobrevivido**, o turno dela viria de novo, e a cena continuaria
até alguém desistir, fugir ou cair. **Se Kaori chegasse a `0` de vida**, ela escolheria
entre `Aguentar` e `Insistir`. A regra está no capítulo 1, na seção *Vida a 0*.

## Depois da cena

- **Quer entender por que cada número é aquele?** Capítulo 1, *Como Jogar*.
- **Quer montar o seu próprio personagem?** Capítulo 6, *Criação de Personagem*, os oito
  passos — a Kaori acima é o exemplo completo de lá.
- **Esbarrou numa palavra que não foi explicada?** O vocabulário do sistema, logo atrás
  desta página, tem uma linha para cada termo e o capítulo que o explica por extenso.

---


# Capítulo 1 · Como Jogar

*fonte: `manual/10-como-jogar.md`*

## Teste

Na maior parte do tempo o jogo é conversa. Alguém descreve o que o personagem faz, o mestre descreve o que acontece, e a cena anda. O dado entra num momento específico: quando a coisa é difícil **e** o fracasso muda alguma coisa. Empurrar uma porta emperrada com uma maldição arranhando o outro lado pede rolagem. Empurrar a mesma porta com a tarde inteira pela frente, não; o mestre deixa acontecer e segue.

> **Role um d20, some o seu bônus e compare com a CD. Igualou ou passou, você conseguiu.**

A **CD** é o número que a tarefa pede. Quem diz qual é o mestre, e ele tira de uma escada de cinco degraus.

**Escada de CD**
| CD | dificuldade | como isso aparece na cena |
|---|---|---|
| 10 | rotina | pular o muro do colégio, lembrar de que família é aquele brasão |
| 14 | fácil | passar por dois vigias distraídos, convencer um funcionário cansado |
| 18 | média | escalar a fachada de um prédio na chuva, mentir para quem já desconfia |
| 22 | difícil | reconhecer uma técnica que só aparece em três registros |
| 26 | quase impossível | sair inteiro de uma coisa que não devia deixar ninguém sair |

Por exemplo, numa CD 14 você precisa tirar 14 ou mais no d20 depois de somar o bônus: com bônus 3, um 11 no dado já basta.

O bônus muda conforme o tipo de rolagem. As seções seguintes dizem o que entra em cada um.

### Teste de perícia

> **Perícia = d20 + atributo + maestria, se você for treinado.**
> **Sem treino, é d20 + atributo.**

Cada perícia tem um atributo fixo, e o quadro completo (vinte e três perícias e onze ofícios) está no capítulo 3, *Perícias e Ofícios*. Você é **treinado** naquilo que a sua Origem e o seu Caminho te deram na criação: o Caminho dá duas perícias fixas, mais quatro à sua escolha e dois ofícios livres, e a Origem dá mais duas perícias. Oito perícias de vinte e três. O resto você ainda pode tentar; só tenta sem a maestria.

> **Exemplo.** Rin precisa passar por um corredor com dois vigias. Dá para contornar por fora (Furtividade, CD 14) ou subir pela lateral do prédio (Atletismo, CD 18). Ela é treinada em Furtividade e não em Atletismo, e escolhe contornar. Destreza 3, maestria 1: rola 11 no d20, soma 4, dá 15. Passou.

### Vantagem e desvantagem

> **Vantagem: role dois d20 e fique com o melhor.**
> **Desvantagem: role dois d20 e fique com o pior.**
> O bônus é somado normalmente ao dado que ficou.

Qualquer coisa pode ligar um dos dois: um Legado, uma condição, um aliado te ajudando, a posição em que você está. Nenhum dos dois mexe em número da ficha — os dois mexem em quantos dados você joga.

> **Exemplo.** Sousuke ataca alguém que está `Derrubado`, a um metro de distância. A condição dá vantagem a quem ataca de perto: ele rola dois d20, tira 6 e 17, e usa o 17.

### Ajudar

> Um personagem que possa contribuir de verdade dá **vantagem** ao teste de outro. Um ajudante por teste: dois ajudando não dão vantagem duas vezes.

Contribuir de verdade quer dizer estar em condição de fazer diferença naquela tarefa específica: segurar a escada, apontar a lanterna, distrair o segurança enquanto o outro passa. Alguém torcendo do outro lado da sala não conta.

`Ajudar` custa a sua Ação Padrão. A economia de ações está no capítulo 2, *O Turno*.

### Teste de grupo

> Quando o grupo inteiro precisa passar por alguma coisa (atravessar sem ser notado, aguentar o frio), **metade do grupo passando resolve**.

### Falha

Toda falha empurra a cena para algum lugar. O mestre pediu a rolagem porque o resultado importava, então o dado ruim tem que mudar a situação tanto quanto o dado bom mudaria. Uma falha entrega uma destas três coisas:

- **Custo.** Você consegue, e paga: tempo, barulho, um ferimento, um recurso.
- **Complicação.** Você consegue, e alguma coisa piora junto.
- **Informação indesejada.** Você não consegue, descobre por quê, e isso abre outro caminho.

> **Exemplo.** Rin falha na Furtividade por dois pontos. O mestre escolhe **custo**: ela passa pelos vigias, mas derruba um cone de sinalização, e agora os dois estão andando na direção do corredor. Ela conseguiu o que queria e o relógio da missão encurtou.

## Atributos

**Força · Destreza · Constituição · Inteligência · Essência**

O número **é** o modificador, numa escala de 0 a 6. Um personagem com Força 4 soma 4 no ataque corpo a corpo, e ponto. Não existe valor separado, tabela de conversão nem coluna extra na ficha.

**Atributos**
| Atributo | O que governa |
|---|---|
| **Força** | ataque corpo a corpo, agarrar, quebrar, carregar |
| **Destreza** | ataque à distância, Defesa, iniciativa, furtividade |
| **Constituição** | pontos de vida |
| **Inteligência** | conhecimento, investigação, reconhecer uma técnica pelo catálogo |
| **Essência** | perceber energia amaldiçoada, trato social, hierarquia, negociar Pactos |

Essência é a sua energia amaldiçoada como sentido: o que ela capta do ar de uma sala é da mesma natureza do que ela capta da voz de alguém. A divisória entre ela e Inteligência: **Inteligência sabe, Essência percebe**. Sentir Energia e Percepção rolam com Essência.

Inteligência não concede perícias extras. O que você é treinado vem da Origem e do Caminho, e de mais nada.

## Maestria

> **Maestria começa em 1 e sobe um ponto a cada oito níveis.**

**Maestria por nível**
| nível | 2–9 | 10–17 | 18–25 | 26–30 |
|---|---|---|---|---|
| maestria | 1 | 2 | 3 | 4 |

Maestria é o bônus que mede o tempo de estrada do personagem. Ela entra em toda rolagem de ataque, na CD dos seus feitiços, e no que você treinou: perícia, ofício e Teste de Resistência. Por exemplo, no nível 6 a sua maestria é 1, e no nível 10 ela vira 2. Ela fica fora da Defesa.

A ficha começa no **nível 2**, já com um feitiço. O nível 1 fica como opção de campanha, para quando a mesa quiser jogar o personagem de antes de ele ser feiticeiro.

## Acertar

Três rolagens, uma para cada jeito de machucar alguém. Todas comparam com a **Defesa** do alvo, e todas seguem a mesma regra do teste: igualou ou passou, acertou.

> **Ataque corpo a corpo = d20 + Força + maestria**
> **Ataque à distância = d20 + Destreza + maestria**
> **Ataque de conjuração = d20 + o atributo da sua técnica + maestria**

As três têm a mesma forma: **um atributo, mais a maestria.** O atributo do corpo a corpo é a Força e o do tiro é a Destreza; o da conjuração é aquele que você escolheu quando escreveu a técnica, e ele pode ser qualquer um dos cinco.

Nem todo feitiço rola acerto. Um feitiço resolve de três jeitos, e o capítulo 9, *Fundamento*, diz qual é o de cada um:

**Resolução de feitiço**
| como resolve | o que acontece |
|---|---|
| **Acerto** | você rola o ataque de conjuração contra a Defesa do alvo |
| **Teste de Resistência** | o alvo rola contra a CD do seu feitiço |
| **Automático** | acontece, sem rolagem de nenhum dos dois lados |

> **CD de feitiço = 8 + o atributo da sua técnica + maestria.**

> **Exemplo.** Mei está no nível 10, então a maestria dela é 2, e a técnica dela usa Essência, que ela tem em 4. O ataque de conjuração dela é `d20 + 6` e a CD de qualquer feitiço dela é 14. Ela tem duas versões da mesma técnica na ficha: uma que pede acerto e uma que pede Teste de Resistência. O alvo é um mestre-maldição com Defesa 17 e Teste de Resistência de Espírito alto. Ela escolhe a de acerto, porque 17 contra `d20 + 6` é uma aposta melhor do que a CD 14 contra a resistência daquele bicho.

### Crítico

> **20 natural numa rolagem de acerto é crítico. Você dobra os dados.**
> Dobra os dados da arma, se for arma; os dados da Classe, se for feitiço ou feitiço de Toque.
> **Nada mais dobra**: nem Força, nem dados que vieram de Melhoria, nem dano fixo.

Crítico só existe onde existe rolagem de acerto. Feitiço que resolve por Teste de Resistência ou por Automático nunca crita, e isso vale também para as Melhorias que compram precisão tirando a rolagem de ataque.

> **Exemplo.** Sousuke acerta com uma lâmina de 2d6 e Força 4. No 20 natural ele rola 4d6 e soma 4. A Força continua entrando uma vez só.

## Defesa

> **Defesa = 10 + Destreza + proteção**

Defesa é o número que o inimigo precisa igualar ou passar para te acertar. Ele rola contra ela; você não rola nada. Por exemplo, com Destreza 3 e um Traje de degrau 2, a sua Defesa é 15.

**Proteção** é o que você veste ou o que você cobre. Cobrir-se de energia amaldiçoada dá proteção sem equipamento nenhum, e é aptidão básica de todo feiticeiro.

Defesa evita ser acertado. Reduzir o dano que já passou é outra coisa, chamada **Redução de Dano**, e ela aparece no capítulo 9, *Fundamento*.

### Cobertura

Estar atrás de alguma coisa sobe a sua Defesa, e a cobertura Total tira você da lista de alvos possíveis. Os três degraus, com os números de cada um, estão no capítulo 4, *Dano, Condições e Cobertura*.

## Testes de Resistência

**Você rola um Teste de Resistência** quando alguma coisa acontece com você e você tenta segurar a barra. O ataque parte do outro lado; a rolagem é sua. São quatro.

> **Teste de Resistência = d20 + atributo do TR + maestria, e a maestria só entra se você for treinado nele.**

**Testes de Resistência**
| Teste de Resistência | Usa | Serve para |
|---|---|---|
| **Físico** | Força **ou** Destreza, declarado na criação e travado | reagir, esquivar, aguentar impacto |
| **Vigor** | Constituição | veneno, doença, exaustão |
| **Intelecto** | Inteligência | controle mental, ilusão, dissociação |
| **Espírito** | Essência | vontade, determinação, não se dobrar |

**Só o TR Físico escolhe entre dois atributos**, e essa escolha é feita uma vez na criação. Ela diz como o seu personagem sai da frente de uma explosão: quem travou em Força planta o pé e absorve, quem travou em Destreza salta.

Você é treinado em **dois dos quatro**: a sua Origem treina um, o seu Caminho treina outro. **No Teste de Resistência que você treinou, você soma a maestria; nos outros dois, só o atributo.** É a mesma marca de treino da perícia e do ofício.

> Nos dois Testes de Resistência que você não treinou, você não soma a maestria — e a distância entre eles e os treinados só cresce conforme a campanha anda. É por ali que um chefe vai entrar.

> **Exemplo.** Kaito travou o TR Físico em Destreza, que é 4, e a Origem dele treinou justamente esse. Um feitiço de área de CD 15 explode do lado dele: ele rola 9 no d20, soma 4 de Destreza e 2 de treino, dá 15. Igualou, então resistiu.

## Vida, energia e alma

Três reservas, e cada uma tem uma conta diferente. Vida é o corpo, energia é o combustível, Integridade é a alma. O **Caminho** define os números abaixo, e você escolhe ele na criação; o capítulo 6, *Criação de Personagem*, explica o que cada Caminho é.

### Pontos de vida

> **No nível 1 você recebe a vida inicial do seu Caminho, mais a sua Constituição.**
> **Em cada nível depois, você recebe a vida por nível do seu Caminho, mais a sua Constituição de novo.**

**Vida e PE por Caminho**
| Caminho | dado | vida no nível 1 | por nível | PE por nível |
|---|---|---|---|---|
| **Bastião** | d12 | 12 | 7 | 4 |
| **Vanguarda** | d8 | 8 | 5 | 5 |
| **Guia** | d8 | 8 | 5 | 5 |
| **Evocador** | d6 | 6 | 4 | 6 |
| **Emanador** | d6 | 6 | 4 | 6 |

> **Exemplo.** Mei é Vanguarda, Constituição 3, nível 4. Nível 1: 8 + 3 = 11. Cada um dos três níveis seguintes: 5 + 3 = 8. Total: 11 + 24 = **35 de vida**.

> **Variante: rolar a vida.** Se a sua mesa preferir, role o dado do Caminho a cada nível em vez de pegar o valor fixo da tabela. Na média isso rende um pouco menos.
### Vida temporária

Algumas coisas dão **vida temporária**: a Forma `Apoio`, a Passiva `Fluxo`, e habilidades de Trilha como o `Aprumo` e a `Crosta`.

> **Vida temporária é anteparo, e não vida.** Ela é **gasta antes** da vida real, **não acumula** — duas fontes, você fica com a maior, nunca com a soma —, tem **teto de metade da sua vida máxima**, e **some no fim da cena**.

Por exemplo, com 40 de vida máxima o seu teto é 20: um efeito que daria 27 te deixa em 20, e um segundo efeito que daria 12 não soma nada, porque 20 é maior.

**O mestre pode deixar ela atravessar para a cena seguinte** quando a preparação foi deliberada — quem se cobre antes de entrar no prédio não perde o que gastou porque a cena mudou de nome.

Ela não sobe a sua vida máxima, não conta para `Insistir`, e não é cura: quem está a `0` de vida e recebe vida temporária continua a `0`.

### Pontos de energia

**Pontos de energia** são o combustível dos seus feitiços, e o manual chama de **PE** nas tabelas. É o que acaba primeiro numa missão longa.

> **Pontos de energia = PE por nível do seu Caminho × o seu nível.**

Sem atributo e sem valor inicial: no nível 1 você tem o PE de um nível.

> **Exemplo.** Mei, Vanguarda de nível 4: 5 × 4 = **20 de PE**. Nenhum atributo entra nessa conta.

### Integridade

> **Integridade = 20 + 8 × (nível − 1).** Plana, igual para todo mundo.

Integridade é a sua alma, e a alma é igual para todo mundo: nem o Caminho nem a Constituição mexem nela. Dano de alma passa por cima de corpo duro. Por exemplo, no nível 2 a sua Integridade é 28, e no nível 10 ela é 92.

Dano de alma tem quatro estágios, e eles estão no capítulo 4, *Dano, Condições e Cobertura*, na seção *Dano na alma*. O quarto é o fim da linha: *"você não é mais você, e o que sobra é decisão do mestre"*.

## Arredondamento

Boa parte das contas do sistema cai em fração. Uma frase resolve todas.

> **Arredonde sempre para o lado que não te favorece.**
> O que você **paga** sobe. O que você **ganha** desce. E o que você ganha nunca fica abaixo de 1.

> **Exemplo.** Você recupera 2,5 de PE num descanso curto: recupera 2. Um efeito te cobra 2,5 de PE: você paga 3.

A regra vale para a conta que cai na sua mão na mesa. Número que já está impresso numa tabela você copia e segue: a vida por nível do Caminho, por exemplo, já vem arredondada no quadro acima.

O piso de 1 é sobre arredondamento. Quando uma regra diz que você recupera **nada**, ela diz nada, e o piso não desfaz um zero escrito.

## Vida a 0

O personagem levou o golpe que zerou a barra, a mesa para, e quem escolhe o que acontece é você.

> **Você chega a 0 de vida. Escolha uma das duas, na hora:**
>
> **Aguentar** — você apaga. Tem uma janela de **3 rodadas**. Qualquer cura de 1 ou mais te põe de pé. Se a janela acabar sem socorro, você chega ao **estágio 4 de dano de alma**.
>
> **Insistir** — você fica de pé a 0 de vida e age normalmente. Cada rodada custa um pedaço da sua **vida máxima**, e ele dobra: **1/8, depois 1/4, depois 1/2**. Na quarta rodada você desaba.

Quem desaba pelo Insistir não levanta com um ponto de cura. Só acorda com uma cura de **metade da sua vida máxima original, de uma vez só**.

**Aguentar e Insistir**
| | ganha | custa |
|---|---|---|
| **Aguentar** | janela de 3 rodadas, e acorda com 1 de cura | fora da luta desde já, 1 Sequela |
| **Insistir** | 3 rodadas agindo | 7/8 da vida máxima, 1 Sequela, e só acorda com metade da máxima original |

O custo do Insistir usa o arredondamento de sempre: ele é uma coisa que você paga, então ele sobe.

> **Exemplo.** Kaito tem 80 de vida máxima e chega a 0 com o chefe quase morto. Ele escolhe Insistir. Na primeira rodada paga 10 (1/8 de 80), na segunda 20, na terceira 40. Se o chefe não cair até lá, Kaito desaba na quarta.

### Sequela e Cicatriz

> Toda vez que você levanta de uma queda, ganha uma **Sequela**. Cada Sequela tira uma rodada da janela da sua próxima queda.
>
> **Na segunda queda você também ganha uma Cicatriz**, que é permanente e não sai no descanso.
>
> Sequela some no descanso longo. Vida máxima e Integridade voltam junto, como sempre.

Sequela deixa as suas rolagens exatamente como estavam. O que encurta é a próxima queda: onde antes havia três rodadas de janela, agora há duas.

### Inconsciente

Chegar a 0 de vida tem nome próprio: `Inconsciente`, o estado descrito nesta seção. Duas condições parecidas costumam ser confundidas com ele, e as duas moram no capítulo 4, *Dano, Condições e Cobertura*:

**Inconsciente, Incapacitado e Derrubado**
| | o que é |
|---|---|
| `Inconsciente` | você chegou a 0 de vida, e está nesta seção |
| `Incapacitado` | condição, e quem está `Incapacitado` continua com vida |
| `Derrubado` | condição, e quem está `Derrubado` está no chão, de pé no medidor |

## Condições

**Condição** é um estado nomeado que muda o que você consegue fazer enquanto durar. Ficar `Cego` no meio de uma briga, levar um golpe que te deixa `Atordoado`, ser agarrado e não sair mais do lugar: tudo isso é condição. Cada uma tem um nível, e o nível é o que ela custa quando alguém monta um feitiço para aplicá-la.

São catorze, e elas têm capítulo próprio: o capítulo 4, *Dano, Condições e Cobertura*. Lá está o efeito de cada uma por extenso, o nível de cada uma, o que não conta como condição neste sistema, e como se tira uma condição de alguém.

## Notação e nomes

Ao longo do manual, o que aparece `assim` é nome de mecânica: uma condição, uma perícia, uma ação, uma Melhoria. Quando você vir uma palavra nesse formato, ela tem regra escrita em algum lugar, e o nome dela é exatamente aquele.

---


# Capítulo 2 · O Turno

*fonte: `manual/11-o-turno.md`*

O combate é contado em rodadas. Todo mundo rola Iniciativa, e essa rolagem decide a ordem em que as pessoas agem. Cada um tem o seu **turno**; quando todo mundo já teve o seu, a rodada fecha e começa outra, na mesma ordem.

Uma rodada são 6 segundos. Tudo que acontece nela está acontecendo mais ou menos ao mesmo tempo; a ordem existe para a mesa conseguir narrar.

## Iniciativa

> **Iniciativa = `d20` + Destreza. Quem tirar mais age primeiro.**
>
> Empate se resolve pela maior Destreza. Se as Destrezas também forem iguais, o jogador age antes do inimigo.

A ordem sai uma vez e vale enquanto a cena durar. Ninguém rola de novo a cada rodada.

> **Exemplo.** A Rina tem Destreza 4. Ela rola o d20, tira 11, e a iniciativa dela é 15. A maldição do outro lado do galpão tem Destreza 3 e tira 16: iniciativa 19. A maldição age antes dela, nesta rodada e em todas as próximas.

## Recursos do turno

**Recursos do turno**
| Recurso | Quanto | O que faz |
|---|---|---|
| Ação de Movimento | uma | compra até 9 metros de deslocamento, e o segundo saque do turno |
| Ação Padrão | uma | atacar, conjurar, a maior parte das coisas |
| Ação Bônus | uma | só o que a regra disser, com todas as letras, que é Ação Bônus |
| Reação | uma | responde a um gatilho, vale fora do seu turno, e volta no começo do seu turno |

Os quatro são independentes. Você tem os quatro em todo turno seu, e gastar um não mexe nos outros. Também não dá para trocar: abrir mão da Ação Padrão não compra movimento nem uma segunda Ação Bônus.

O slot de Ação Bônus fica vazio na maioria dos turnos da maioria das fichas, e isso é normal. Ele só acende quando alguma coisa escrita na sua ficha diz **Ação Bônus** com todas as letras.

### Deslocamento

**Ação de Movimento** é o slot do turno; **deslocamento** é a distância que ele compra. Onde a sua ficha disser `+3 m`, `metade do deslocamento` ou `perde o deslocamento do próximo turno`, está falando de metros.

O seu deslocamento base é 9 metros, e você corta esse total em quantos pedaços quiser dentro do turno. Dá para andar 3 metros, atacar, e andar os 6 que sobraram. É assim que alguém sai de trás de uma coluna, dá o golpe e volta para trás dela no mesmo turno.

### Sacar e guardar

> **Sacar ou guardar um item — inclusive arma — não custa nada. Uma vez por turno.**
>
> **Do segundo em diante, sacar ou guardar custa a sua Ação de Movimento inteira.** Não meia, não 3 metros: a Ação de Movimento do turno.

**Trocar de arma é sacar e guardar, então é dois.** Guardar a que está na mão é o primeiro e sai de graça; sacar a outra é o segundo, e custa a Ação de Movimento.

**Largar no chão não é guardar.** Largar é de graça e é sempre. É por isso que *soltar e sacar* sai mais rápido que *trocar*, ao preço de deixar a arma no chão.

### Rodada inteira

Algumas coisas custam a rodada inteira: Ação de Movimento, Ação Padrão e Ação Bônus de uma vez só. A Reação continua sua.

> **Exemplo.** A Rina abre o turno andando 6 metros até a porta do depósito. Gasta a Ação Padrão em `Atacar` a maldição que estava esperando atrás dela, e ainda tem 3 metros sobrando, que usa para sair do vão da porta. A Ação Bônus dela fica parada: nada na ficha da Rina diz que é Ação Bônus, e sem isso o slot não faz nada.

## Ações de Ação Padrão

Doze ações têm regra escrita. Você continua podendo tentar o que não está aqui; é aqui que o mestre não precisa arbitrar nada.

**Ações de Ação Padrão**
| Ação | O que ela faz |
|---|---|
| **Atacar** | um ataque com arma ou desarmado, e os ataques a mais que a sua regra de ataque extra der. `Agarrar` e `Derrubar` são opções desta ação |
| **Conjurar** | um feitiço, pelo Fundamento |
| **Correr** | ganhe deslocamento igual ao seu, pelo resto do turno |
| **Desengajar** | o seu movimento não provoca ataque de oportunidade pelo resto do turno |
| **Esquivar** | ataques contra você têm desvantagem, e os seus Testes de Resistência de Destreza têm vantagem, até o começo do seu próximo turno |
| **Esconder** | um teste de `Furtividade` |
| **Ajudar** | dá vantagem ao próximo teste ou ataque de um aliado |
| **Influenciar** | um teste de Essência para mudar a atitude de alguém |
| **Preparar** | escolha uma ação e um gatilho visível. Quando o gatilho acontecer, você gasta a Reação para fazer a ação |
| **Vasculhar** | um teste de `Percepção` ou `Investigação` sobre uma coisa ou uma criatura ao seu alcance |
| **Estudar** | um teste de `Sentir Energia`, `Ocultismo`, `Medicina` ou `História` sobre uma criatura ou objeto que você enxerga |
| **Usar objeto** | usar um objeto não mágico |


### Agarrar e Derrubar

As duas são opções do `Atacar`, e cada uma ocupa um dos seus ataques. Quem tem ataque extra agarra com um golpe e bate com o outro, no mesmo turno. Cada uma aplica a condição de mesmo nome, e o efeito delas está no capítulo 4, *Dano, Condições e Cobertura*.

### Ajudar

Um ajudante por teste. Dois aliados ajudando não dão vantagem duas vezes, e o segundo perde a Ação Padrão dele à toa. A regra completa de `Ajudar`, com o que conta como ajuda de verdade, está no capítulo 1, *Como Jogar*.

### Influenciar

O teste é de Essência, e a perícia depende do jeito que você escolher: `Persuasão`, `Enganação`, `Intimidação` ou `Atuação`. Serve tanto para o negociador do outro lado da barreira quanto para a maldição que ainda tem alguma coisa de gente dentro. O que muda é a CD que o mestre põe.

### Preparar

`Preparar` cobra duas coisas por uma. Você gasta a Ação Padrão agora, e a Reação depois, quando o gatilho acontecer. Se o gatilho não acontecer até o começo do seu próximo turno, a ação se perde e você não recebe nada de volta.

> **A Reação não fica reservada.** Até o gatilho acontecer, ela continua sua para qualquer outro uso — e gastar ela em outra coisa faz a ação preparada se perder. Usar a ação preparada gasta a Reação.

O gatilho precisa ser visível e verificável pela mesa: *"quando ela sair da fumaça"*, *"quando ele encostar na porta"*. Um gatilho que só o jogador consegue julgar trava a cena.

Preparar uma conjuração continua exigindo a Melhoria `Reação`. O slot não muda o que a Reação permite.

> **Exemplo.** O Kaito prepara: *"se aquela coisa passar da linha das prateleiras, eu ataco."* Gastou a Ação Padrão dele agora. A maldição passa da linha ainda na rodada, e ele gasta a Reação para dar o golpe. Se ela tivesse ficado parada até a vez dele de novo, ele teria perdido o turno inteiro esperando.

### Vasculhar e Estudar

As duas gastam a Ação Padrão para trocar informação por tempo, e a diferença é a distância. `Vasculhar` é mão no objeto: revistar o corpo, abrir a gaveta, apalpar a parede atrás de um vão. `Estudar` é olhar com atenção de longe: ler a energia de uma maldição, reconhecer o formato de um selo, avaliar quanto sangue aquele ferido ainda aguenta perder.

## Ações de Ação Bônus

São duas.

> **`Provocar`** — Ação Bônus. Teste de `Provocar` contra o Teste de Resistência de Espírito do alvo. Se ele falhar, até o começo do seu próximo turno ele ataca com desvantagem qualquer alvo que não seja você, e com vantagem contra você.

> **`Ler o Ambiente`** — Ação Bônus, uma vez por cena. Teste de `Percepção` ou `Intuição` contra a dificuldade que o mestre puser. Num sucesso, o mestre te diz uma coisa daquele lugar que dê para usar: um objeto, um caminho, uma posição, um risco. Se não houver nada, ele diz isso e a ação não é gasta.

`Provocar` puxa o golpe para você: enquanto durar, você é o alvo mais fácil da sala, e quem foi provocado erra mais em qualquer outro. É a ação de quem tem couro para receber no lugar de quem não tem.

`Ler o Ambiente` fala do lugar e só do lugar. Ela nunca diz nada sobre uma criatura. Quem quer saber do inimigo usa `Estudar`; quem quer revistar alguém usa `Vasculhar`; e as duas custam a Ação Padrão.

> **Exemplo.** O Kaito está encurralado num estacionamento. Ele gasta a Ação Bônus em `Ler o Ambiente` e tira 17 num teste de `Percepção`. O mestre diz que o carro ao lado dele está com o tanque aberto e cheirando a gasolina. Se ele tivesse perguntado *"o que essa maldição está prestes a fazer?"*, a resposta seria outra: isso é `Estudar`, e custa a Ação Padrão.

## Ataque de oportunidade

> **Quando alguém sai do seu alcance de corpo a corpo sem tomar cuidado, você pode gastar a sua Reação para atacar essa pessoa.**

É o que impede um inimigo de passar correndo pelo meio do grupo como se ninguém estivesse ali. É um ataque físico, rolado como qualquer outro ataque, com soco ou com arma. Conjurador faz um normalmente. Conjurar na Reação, em vez de socar, exige a Melhoria `Reação`.

Duas coisas passam livre: quem usou `Desengajar` naquele turno, e qualquer movimento cujo texto diga **sem provocar**.

> **Exemplo.** A maldição está encostada na Rina e resolve correr atrás do Kaito. Ela não usou `Desengajar`, então a Rina gasta a Reação dela e ataca a maldição saindo. A Reação da Rina só volta no começo do próximo turno dela, e até lá ela não tem com o que responder a mais nada.

## Concentração

Alguns efeitos exigem que você mantenha a atenção neles enquanto duram: a barreira que continua de pé, a coisa que você está segurando no lugar do outro lado da sala. Você concentra em um por vez; começar um segundo derruba o primeiro.

> **Quando você toma dano concentrando, faça um Teste de Resistência de Vigor. A CD é 10, ou metade do dano que você tomou, o que for maior. Se falhar, o efeito cai.**

> **Exemplo.** O Kaito está concentrando num efeito e leva 26 de dano. Metade de 26 é 13, e 13 é maior que 10: a CD é 13. Se o golpe tivesse tirado 12, a metade daria 6, e a CD seria 10 mesmo.

### Concentração e Carregar

As duas seguram alguma coisa contra o dano, em momentos diferentes da vida de um feitiço.

**Concentração e Carregar**
| | O que você segura | Teste | Falhar custa |
|---|---|---|---|
| **Concentração** | o efeito que já está no ar | Vigor | o efeito cai |
| **Carregar** | o feitiço que ainda não saiu | Espírito | o feitiço, e o que você pagou por ele |

Quem usa a Restrição `Carregar` mantém o movimento e a Ação Bônus no turno de carga. Só a Ação Padrão daquele turno vai embora.

## Limites

> **Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.**

É a trava que impede dois feitiços grandes no mesmo turno. Por exemplo, se você conjurou um feitiço de Classe 3 na Ação Bônus, o que ainda cabe na Ação Padrão é um Classe 0, e nada maior.

Você tem **uma Reação só**, e três coisas disputam ela: ataque de oportunidade, a ação `Preparar` e conjurar pela Melhoria `Reação`. Gastar a Reação com uma delas é abrir mão das outras até o seu próximo turno começar.

---


# Capítulo 3 · Perícias e Ofícios

*fonte: `manual/12-pericias-e-oficios.md`*

O seu personagem tem duas listas de coisas que sabe fazer fora da técnica: **perícias** e **ofícios**. Elas se parecem na ficha e funcionam diferente.

**Perícia** é uma capacidade do corpo ou da cabeça. Ela pertence a um atributo e só a esse atributo. Correr é `Atletismo`, e `Atletismo` é sempre Força.

**Ofício** é uma prática que alguém te ensinou. Ele vive solto no quadro de atributos: o atributo muda conforme o que você está fazendo com ele.

**Perícia e ofício**
| É perícia | É ofício |
|---|---|
| Escalar um muro | Dirigir a van até o muro |
| Saber que aquilo é uma maldição de segundo grau | Desenhar o talismã que segura ela |
| Convencer o clã a te receber | Preencher a requisição que abre a porta |
| Notar o cheiro de sangue na sala | Fazer o chá que faz o ferido dormir |

A regra prática: se é uma ferramenta ou um procedimento que alguém te ensinou passo a passo, é ofício. A ferramenta pode ser a chave de fenda, o papel de talismã ou o formulário certo. `Burocracia` é ofício pelo mesmo motivo que `Forja` é.

## Rolagem de perícia e ofício

> **Perícia = `d20` + o atributo dela + maestria, se você for treinado.**
> Sem treino, é só `d20` + o atributo.

> **Ofício = `d20` + o atributo que a situação pede + maestria, se você for treinado.**
> Sem treino, você normalmente não consegue tentar.

Ser **treinado** quer dizer ter aquela perícia ou aquele ofício marcado na ficha; a seção *Treino* diz de onde vêm as marcas. **Maestria** é o bônus que cresce com o nível, e a escada dela está no capítulo 1, *Como Jogar*. O mestre põe uma **CD**, o número que a sua rolagem precisa alcançar para você conseguir o que queria. Por exemplo, com Destreza 3 e maestria 1, uma `Furtividade` treinada rola `d20 + 4`; sem treino, `d20 + 3`.

### Atributo fixo ou variável

Forjar uma lâmina é Força. Falsificar uma assinatura é Destreza. Saber qual selo o papel pede é Inteligência. As três coisas são o mesmo ofício, `Caligrafia` ou `Forja`, e o mestre escolhe o atributo na hora, do mesmo jeito que escolhe a dificuldade.

Um ofício rende diferente na mão de cada personagem. O mesmo `Arrombamento` é uma coisa para quem tem Destreza 4 e outra para quem tem Inteligência 4, e as duas fichas passam por portas diferentes.

### Sem treino

Qualquer um pode tentar escalar e falhar. Ninguém forja uma lâmina por tentativa. Quando o mestre achar que dá para improvisar, tipo dirigir um carro automático em linha reta ou fazer um curativo torto, ele libera a rolagem sem a maestria.

> **Exemplo.** A Rina joga de Vanguarda, no nível 6. Destreza 4, Inteligência 2, maestria 1. Ela é treinada em `Furtividade` e no ofício `Arrombamento`.
>
> Para entrar no depósito sem ser vista ela rola `Furtividade`, que é Destreza: `d20 + 4 + 1`, ou seja `d20 + 5`.
>
> Chegando na porta, ela usa `Arrombamento`. O mestre decide que forçar aquela tranca é trabalho de mão e cobra Destreza: `d20 + 4 + 1` de novo. Se a tranca fosse eletrônica ele teria cobrado Inteligência, e o mesmo ofício sairia `d20 + 2 + 1`. Três a menos, porque a Rina é boa com as mãos e não com o sistema.

## Perícias

### Inteligência e Essência

**Inteligência sabe, Essência percebe.** Inteligência é o que você estudou: o catálogo de maldições, o que aconteceu, como o corpo funciona, quem manda em quem. Essência é o que você capta: a energia no ar, o barulho no corredor, a mentira na voz de alguém.

**Perícias por atributo**
| Atributo | Perícias | Quantas |
|---|---|---|
| **Força** | Atletismo | 1 |
| **Destreza** | Acrobacia · Furtividade · Pontaria · Prestidigitação | 4 |
| **Inteligência** | Investigação · Intuição · Ocultismo · Religião · História · Hierarquia · Medicina · Sobrevivência · Natureza · Lidar com Animais · Tecnologia | 11 |
| **Essência** | Sentir Energia · Percepção · Persuasão · Enganação · Intimidação · Atuação · Provocar | 7 |
| **Constituição** | — | 0 |

Nenhuma perícia mora em Constituição. Constituição governa os pontos de vida e o Teste de Resistência de Vigor.

### Catálogo

#### Força

**Atletismo** — correr, escalar, nadar, saltar, carregar alguém que não consegue andar. É a perícia das cenas em que o obstáculo é o terreno: a grade que precisa ser vencida antes da maldição chegar, o companheiro desmaiado que alguém tem que tirar dali, os três andares de escada que separam o grupo do telhado.

#### Destreza

**Acrobacia** — equilíbrio, cair sem se machucar, escapar de um agarrão, passar por espaço apertado. Aparece quando o chão trai: viga estreita, telhado molhado, o corredor desabando enquanto vocês correm. Também é o que tira você de um `Agarrado`, no capítulo 4, *Dano, Condições e Cobertura*.

**Furtividade** — mover-se sem ser visto nem ouvido. É a perícia de infiltração e de emboscada, e a que decide se a cena começa com o grupo escolhendo o momento ou com o inimigo escolhendo por ele.

**Pontaria** — acertar o que é pequeno, o que está longe ou o que se mexe, fora de uma rolagem de ataque. Serve para o arremesso que resolve a cena sem virar combate: a chave jogada pela grade, o talismã colado na testa da coisa antes que ela vire, a pedra que acerta o interruptor no fim do corredor.

**Prestidigitação** — mão rápida: esconder um objeto, tirar do bolso alheio, trocar uma coisa por outra na frente de quem está olhando. É a perícia da cena com plateia, em que a dificuldade é fazer sem ninguém ver.

#### Inteligência

**Investigação** — vasculhar, deduzir, ligar duas pistas que ninguém tinha ligado. É a perícia de cena de local: o apartamento onde alguém sumiu, a sala onde a barreira foi montada, o padrão que se repete nos três desaparecimentos.

**Intuição** — ler a pessoa pelo que ela faz: a inconsistência na história, o detalhe que não fecha, a motivação atrás do pedido. É dedução sobre gente, e por isso é Inteligência. Aparece na cena de negociação e de interrogatório, quando o grupo precisa decidir se o informante está entregando ou vendendo. Perceber que alguém está nervoso é `Percepção`.

**Ocultismo** — maldições, técnicas conhecidas, barreiras, o funcionamento da energia amaldiçoada. O lado técnico. É o que você rola quando a coisa na sua frente já foi catalogada por alguém e você quer saber o nome dela, o grau dela e o que costuma matá-la.

**Religião** — xintoísmo, budismo, exorcismo, templo, ritual, o que os selos querem dizer. O lado sagrado, que é de onde o jujutsu veio antes de virar instituição. Resolve cena de lugar antigo: o santuário que ninguém cuida há quarenta anos, o rito que precisa ser feito na ordem certa, a inscrição na pedra que explica por que aquilo está preso ali.

**História** — o que aconteceu e quem estava lá, no mundo comum e no registro das famílias. É a perícia da cena de arquivo e da cena de conversa longa: entender por que este clã odeia aquele, saber que já houve uma missão neste endereço em 1974.

**Hierarquia** — os clãs, a política, quem manda em quem e quem deve o quê a quem. Diz o que você pode pedir, a quem, e o que vai custar. Resolve a cena política: a sala de reunião, o superior que precisa autorizar, o favor que alguém pode cobrar de volta depois.

**Medicina** — ferimento, veneno, doença, corpo. É o saber: olhar um corpo e dizer o que aconteceu, quanto tempo aquela pessoa tem, o que aquele veneno faz. A prática de campo é o ofício `Herbalismo`.

**Sobrevivência** — aguentar o ambiente, achar água e abrigo, se orientar, e seguir um rastro, seja pegada ou resíduo de energia. É a perícia da missão fora da cidade e da perseguição longa, quando a pergunta da cena é *"para onde foi?"*.

**Natureza** — planta, bicho, clima, terreno. O que é o quê, o que é venenoso, quando a chuva vem. Aparece antes da cena dar errado: saber que aquele vale enche, que aquela fruta mata, que o cheiro no ar é de queimada e não de maldição.

**Lidar com Animais** — acalmar, montar, conduzir, mandar num bicho. Vale para o que não é bicho mas se comporta como um: uma invocação que ainda não te obedece direito responde a essa perícia.

**Tecnologia** — computador, câmera, rede, equipamento moderno. Resolve a cena de prédio moderno: a câmera que precisa ser desligada antes de a equipe entrar, o celular da vítima, o registro de acesso que diz quem passou pela porta.

#### Essência

**Sentir Energia** — perceber energia amaldiçoada. Notar o feiticeiro escondido, medir o tamanho de uma maldição antes de encostar nela, sacar que alguém está prestes a conjurar. Quase toda cena do jogo tem energia amaldiçoada em algum lugar, e é esta perícia que diz se o grupo entra na sala ou dá meia-volta.

**Percepção** — notar o mundano: som, cheiro, movimento, a coisa que está fora do lugar, a pessoa suando frio. É a perícia de entrar num lugar novo e reparar em alguma coisa antes de ela virar problema.

**Persuasão** — convencer, negociar, conseguir que façam o que você quer porque querem. A cena dela termina com as duas partes de pé e sem rancor.

**Enganação** — mentir, blefar, se passar por outro. A cena dela termina com alguém acreditando em alguma coisa que não é verdade, e com o relógio contando até ele descobrir.

**Intimidação** — ameaçar, dominar pela presença, fazer alguém **recuar**. Resolve a cena em que o grupo quer que aquilo pare sem precisar bater: o capanga que abre a porta, a testemunha que decide falar, a coisa que resolve procurar comida em outro bairro.

**Atuação** — representar, cantar, tocar para uma plateia, sustentar um personagem que não é você. É a perícia da infiltração longa, em que você não mente uma frase e sim vive um disfarce por uma noite inteira.

**Provocar** — tirar alguém do sério, fazer perder a linha, forçar a vir para cima de você. É o oposto de `Intimidação`: uma faz recuar, a outra faz **avançar**. Em combate ela tem ação própria, `Provocar`, no capítulo 2, *O Turno*.

### Técnica do inimigo

Não existe perícia para isso, porque são duas perguntas diferentes e cada uma já tem casa.

**Ocultismo e Sentir Energia**
| `Ocultismo` reconhece o que você está vendo | `Sentir Energia` lê como a energia se move |
|---|---|
| *"Isso é uma técnica de troca, e troca sempre tem um custo."* | *"Ela gasta muito no começo de cada golpe. Se eu forçar três seguidos, ela seca."* |
| Você conhece o catálogo | Você não precisa saber o nome do que está acontecendo |

O Nanami faz a primeira. O Todo faz a segunda.

## Ofícios

Ofício é o que o personagem sabe fazer porque alguém sentou com ele e ensinou. Cada entrada diz o que ele cobre e onde ele aparece numa missão.

**Condução** — carro, moto, van, o que estiver na garagem. É a cena de chegar a tempo e a cena de sair inteiro: a perseguição pela marginal, o recuo com dois feridos no banco de trás.

**Arrombamento** — tranca, alarme, cofre, janela que não devia abrir. É o ofício que decide se o grupo entra pela porta escolhida por ele ou pela porta que o inimigo deixou aberta de propósito.

**Herbalismo** — planta que cura, planta que mata, chá, unguento, e o que dá para fazer no mato quando não tem hospital. Aparece no acampamento e na volta da missão, quando alguém está mal e o hospital fica a três horas dali.

**Forja** — fazer, afiar e manter arma, e cuidar de ferramenta amaldiçoada sem estragar o que tem dentro. É o ofício do tempo entre missões, e o que evita que o equipamento do grupo vire sucata ao longo da campanha.

**Caligrafia** — talismã, papel de barreira, documento oficial. E documento oficial que não é oficial. Serve tanto para preparar a missão quanto para atravessar uma recepção com um crachá que ninguém deveria ter.

**Burocracia** — a máquina jujutsu por dentro: relatório, requisição, quem assina o quê, como se pede uma janela e como se encobre o que não devia ter sido visto. É o ofício da cena que acontece depois da luta, quando alguém tem que explicar o prédio destruído.

**Entalhador** — madeira, pedra, osso. Fazer o corpo que vai receber alguma coisa. Aparece quando o grupo precisa de um recipiente, um selo físico ou um boneco que aguente o que vai ser posto dentro dele.

**Alfaiate** — tecido, corte, remendo. O uniforme que aguenta energia amaldiçoada sai daqui, e o traje sob medida também. O de prateleira veste todo mundo e ninguém.

**Culinária** — cozinhar de verdade, para gente ou para o que aceitar comida. É o ofício das cenas de descanso, e o de quem negocia com coisa que quer ser agradada antes de ser convencida.

**Instrumento** — um instrumento, escolhido no treino. Toca numa festa, num velório, num templo, ou para segurar a atenção de uma sala inteira enquanto os outros trabalham.

**Jogatina** — carta, dado, aposta, e ler a mesa enquanto joga. Serve para entrar em ambiente fechado pela porta social: a sala de mahjong nos fundos, o cara que só conversa se você sentar e perder algum dinheiro primeiro.

> **Não existe Primeiros Socorros, e `Herbalismo` não cobre o mesmo.** Estancar sangue no meio da missão vira cena em vez de rolagem: ou alguém tem cura de verdade, ou a consequência acontece.

## Treino

> **O Caminho dá duas perícias fixas e mais quatro à sua escolha, de qualquer lugar do quadro.**
> **Mais dois ofícios à sua escolha.**
> **A Origem dá mais duas perícias.**

As duas fixas são a assinatura do Caminho, o que qualquer um daquele Caminho sabe fazer. As quatro livres são suas.

**Perícias fixas por Caminho**
| Caminho | Perícias fixas |
|---|---|
| **Bastião** | Atletismo · Intimidação |
| **Vanguarda** | Acrobacia · Percepção |
| **Guia** | Persuasão · Medicina |
| **Emanador** | Ocultismo · Investigação |
| **Evocador** | Religião · Lidar com Animais |

Ofício o Caminho não trava. Os dois que ele dá são livres, e você escolhe os dois.

`Sentir Energia` fica fora das fixas de todos os cinco Caminhos. Qualquer um pode treinar, e ninguém ganha de graça.

### Perícias da Origem

Uma perícia da lista de quatro da sua Origem, e uma perícia livre que a sua história justifique, com aprovação do mestre. Foi filho de médico, tem `Medicina`. Batia carteira antes de saber o que era energia amaldiçoada, tem `Prestidigitação`.

Além dessas duas, você escolhe um extra: um ofício livre, ou mais uma perícia no lugar dele.

**Extra da Origem**
| Se o extra for | Perícias treinadas | Ofícios treinados |
|---|---|---|
| um ofício | 8 | 3 |
| mais uma perícia | 9 | 2 |

> **Exemplo.** O Kaito é Guia. Ele já entra com as fixas `Persuasão` e `Medicina`. Nas quatro livres do Caminho ele pega `Sentir Energia`, `Ocultismo`, `Percepção` e `Atletismo`, e nos dois ofícios livres pega `Herbalismo` e `Caligrafia`. A Origem dele dá mais duas perícias. No extra ele escolhe a perícia em vez do ofício, e fecha a ficha com 9 perícias e 2 ofícios: ele lê talismã, mas não tem quem arrombe uma porta no grupo.

### Testes de Resistência

A Origem treina um Teste de Resistência, o Caminho treina outro. Ser treinado num Teste de Resistência vale **a maestria**, igual à perícia e ao ofício, e a lista dos quatro está no capítulo 1, *Como Jogar*.

---


# Capítulo 4 · Dano, Condições e Cobertura

*fonte: `manual/15-dano-e-condicoes.md`*

## Tipos de dano

Todo dano deste sistema tem um tipo, e os catorze tipos se dividem em três grupos. O grupo importa porque várias habilidades resistem a um grupo inteiro em vez de a um tipo só.

> **Catorze tipos, em três grupos.**
>
> | grupo | tipos |
> |---|---|
> | **Físicos** | `Cortante` · `Perfurante` · `Concussão` |
> | **Elementais** | `Fogo` · `Frio` · `Elétrico` · `Ácido` · `Trovejante` · `Veneno` |
> | **Especiais** | `Radiante` · `Necrótico` · `Psíquico` · `Energia Reversa` · `Alma` |

A lista é fechada. Quando uma arma, um feitiço ou uma habilidade disser de que tipo é o dano, ou a que tipo ela resiste, o nome sai daqui.

### Catálogo

O número do dano vem da arma ou do feitiço. O tipo diz quem resiste a ele e como a mesa descreve o golpe.

#### Físicos

**`Cortante`** — lâmina, fio, borda. Abre o corpo e sangra. É o dano que deixa o rastro mais visível numa cena: chão molhado, uniforme rasgado, alguém segurando o braço.

**`Perfurante`** — ponta, agulha, projétil. Entra fundo num ponto pequeno. Machuca por dentro sem estragar muito por fora, e é o tipo que atravessa uma guarda que estava bem fechada contra um golpe largo.

**`Concussão`** — soco, queda, coisa pesada. Quebra osso e sacode o que está dentro da caixa. Quem toma sai do lugar, perde o ar e demora um segundo a mais para reagir.

#### Elementais

**`Fogo`** — queima, cozinha, pega no que estiver por perto. A cena continua queimando depois do golpe.

**`Frio`** — tira o calor e trava a articulação. O corpo endurece antes de doer, e a mão demora a fechar de novo.

**`Elétrico`** — passa pelo corpo e faz o músculo obedecer a outra pessoa. Contrai tudo de uma vez, arremessa, e cheira a queimado no ponto de entrada.

**`Ácido`** — come. Continua comendo o que encostou, e estraga equipamento junto com pele.

**`Trovejante`** — pressão e som. Bate no ar antes de bater na pessoa: empurra, estoura ouvido, quebra vidro na sala inteira.

**`Veneno`** — entra e trabalha por dentro. É o dano que dá tempo de alguém perceber que está mal antes de cair.

#### Especiais

**`Radiante`** — luz que queima de dentro para fora. Cega antes de ferir, e costuma vir de coisa que se considera com algum direito de julgar.

**`Necrótico`** — apodrece o vivo. O ferimento não fecha direito e a pele em volta escurece.

**`Psíquico`** — não encosta no corpo. Bate direto na cabeça: a dor vem sem ferimento, e a pessoa continua inteira por fora enquanto sangra pelo nariz.

**`Energia Reversa`** — a energia que conserta gente, usada para o contrário. Num corpo comum ela é ferimento em cima do que já existe; é o dano que mais desmonta quem confiava na própria recuperação.

**`Alma`** — passa por couro, armadura e barreira, e bate na coisa que você é. Ele gasta Integridade em vez de vida, tem quatro estágios próprios, e não se resiste com músculo. Quem toma dano de `Alma` continua de pé e volta menos do que era. Os quatro estágios estão logo abaixo.

### Nomes repetidos

Seis desses nomes você já viu em outro lugar, e ali eles querem dizer outra coisa.

**Nomes repetidos**
| onde o nome aparece | o que ele é ali |
|---|---|
| `Fogo`, `Ácido`, `Veneno` como **Tema** do Fundamento | rótulo de sabor pendurado numa técnica, sem efeito próprio |
| `Cortante`, `Trovejante`, `Alma` dentro de `Passo Cortante`, `Palma Trovejante`, `Toca a Alma` | pedaço do nome de um feitiço pronto |
| os catorze desta seção | o tipo do dano na hora que ele cai |

Um não puxa o outro. Um feitiço com o Tema `Fogo` só causa dano do tipo `Fogo` se o texto dele disser isso.

> **Exemplo.** A Mei tem uma habilidade que dá resistência a `Fogo`. O inimigo acerta ela com `Palma Trovejante`, que causa dano `Trovejante`. Os dois são Elementais, e isso não basta: a resistência dela nomeia um tipo, e `Trovejante` não é `Fogo`. Ela toma o dano inteiro.

### Dano na alma

**Integridade é a vida da alma**, e a fórmula dela é `20 + 8 × (nível − 1)`, do capítulo 1, *Como Jogar*. Por exemplo, 6 de dano na alma tiram 6 de vida, 6 de Integridade, e derrubam a sua vida máxima em 6 até o próximo descanso longo.

> **Cada ponto de dano na alma tira 1 de vida, 1 de Integridade, e derruba a sua vida máxima em 1** até o próximo descanso longo.
>
> **Dano na alma entra cheio**, sem redução pela metade.
>
> Ao receber, faça um **Teste de Resistência de Integridade** contra a CD do atacante. Numa falha, você também avança um estágio na hora, mesmo que a fração ainda não tenha fechado.

**Estágios de dano na alma**
| Integridade perdida | Estágio | O que pega |
|---|---|---|
| 1/4 | **1** | Desvantagem em testes de perícia. |
| 1/2 | **2** | Deslocamento pela metade, e todo feitiço custa +1 PE por Classe. |
| 3/4 | **3** | Desvantagem em ataques e Testes de Resistência. Você não conjura acima de metade da sua Classe máxima. |
| Toda | **4** | Você não é mais você. O que sobra é decisão do mestre. |

**Cura comum não devolve o que a alma perdeu.** Só descanso longo, ou a Melhoria `Remenda`, no capítulo 9, *Fundamento*. O descanso longo devolve toda a Integridade e a vida máxima, e limpa os estágios.

**Nenhum feitiço passa de 2 × Classe em dados na alma.**

## Condições

**Condição** é um estado nomeado que muda o que você consegue fazer enquanto durar. São catorze, e cada uma tem um **nível**: `Leve`, `Média` ou `Pesada`.

> **O nível faz duas coisas, e são as duas contas que a condição pede.**
> É o que ela **custa para comprar** dentro de um feitiço.
> É o que ela **custa para tirar** de alguém, em pontos de energia.

### Como ler

Cada condição abre dizendo **quando** ela vale. Depois vem um parágrafo por efeito, e cada
efeito tem nome próprio: `Deslocamento`, `Seus ataques`, `Contra você`, `Ação`, `Testes` e
`Sai quando`. Os mesmos seis nomes aparecem em todas as catorze, então quem aprende um
reconhece nas outras.

No fim do capítulo, a tabela `Condições em uma linha` traz as catorze resumidas, para
consulta na mesa.

### Nível `Leve`

#### `Lento`

Enquanto está `Lento`, você sofre os seguintes efeitos.

**Deslocamento.** Cai pela metade.

**Ação.** Você não usa Ação Bônus.

*As pernas pesam e o turno rende menos; você chega, só que atrasado.*

#### `Incapacitado`

Enquanto está `Incapacitado`, você sofre os seguintes efeitos.

**Ação.** Você não pode `Bloquear`.

**Contra você.** Todo ataque corpo a corpo é crítico.

*A guarda abriu e você não consegue fechar de volta; quem chegar perto acerta onde quiser.*

#### `Derrubado`

Você está no chão. Enquanto está `Derrubado`, você sofre os seguintes efeitos.

**Deslocamento.** Só se move rastejando.

**Seus ataques.** Desvantagem.

**Contra você.** Vantagem a até **1,5 m**, desvantagem de mais longe.

*Você está de costas no chão olhando para cima, e a prioridade do turno vira levantar.*

#### `Agarrado`

Enquanto está `Agarrado`, você sofre os seguintes efeitos.

**Deslocamento.** É `0`.

**Sai quando.** Quem agarrou ficar `Incapacitado`, ou alguma coisa tirar você do alcance dele.

*Tem uma mão fechada em você; dá para bater, dá para conjurar, e não dá para sair.*

#### `Desarmado`

A sua arma está no chão ou na mão de outro. Enquanto está `Desarmado`, você sofre o seguinte
efeito.

**Seus ataques.** Você bate desarmado até pegar a arma de volta.

*O barulho da lâmina caindo no concreto, e a decisão de gastar o turno pegando.*

#### `Surdo`

Você não ouve. Enquanto está `Surdo`, você sofre os seguintes efeitos.

**Testes.** Falha automática no que precise de audição.

**Iniciativa.** `−2`.

*Zumbido, e tudo que chega por trás chega sem aviso.*

### Nível `Média`

#### `Calado`

Enquanto está `Calado`, você sofre o seguinte efeito.

**Conjuração.** Você não conjura. Nada que precise de voz, gesto ou Selo sai.

*Você tenta e não sai nada; o resto da luta você vira alguém com as mãos e mais nada.*

#### `Enfeitiçado`

Enquanto está `Enfeitiçado`, você sofre os seguintes efeitos.

**Seus ataques.** Você não ataca quem enfeitiçou, nem mira efeito nocivo nele.

**Contra você.** Ele tem vantagem em teste social contra você.

*Você continua você, e aquela pessoa passou a ter razão sobre tudo.*

### Nível `Pesada`

> **Só as de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo.**
> **E só cabe uma delas por feitiço.**

#### `Petrificado`

Você virou pedra. Enquanto está `Petrificado`, você sofre os seguintes efeitos.

**Ação.** Você fica `Incapacitado`.

**Deslocamento.** É `0`.

**Testes.** Você não percebe nada em volta.

**Contra você.** Vantagem.

**Resistência.** A todo dano.

*Você sai da luta inteiro e sem saber o que aconteceu enquanto isso.*

#### `Impedido`

Enquanto está `Impedido`, você sofre os seguintes efeitos.

**Deslocamento.** É `0`.

**Seus ataques.** Desvantagem.

**Testes.** Desvantagem no Teste de Resistência Físico.

**Contra você.** Vantagem.

*Alguma coisa te prendeu no lugar: teia, corrente, o chão fechando em cima do pé.*

#### `Cego`

Você não enxerga. Enquanto está `Cego`, você sofre os seguintes efeitos.

**Testes.** Falha automática no que precise de vista.

**Seus ataques.** Desvantagem.

**Contra você.** Vantagem.

*Você ataca na direção do barulho, e o grupo passa a te narrar a sala.*

#### `Amedrontado`

Enquanto está `Amedrontado`, você sofre os seguintes efeitos.

**Seus ataques.** Desvantagem, enquanto você enxergar a fonte do medo.

**Testes.** Desvantagem, enquanto você enxergar a fonte do medo.

**Deslocamento.** Você não se aproxima dela de vontade própria.

*Você sabe o que precisa ser feito e o corpo não avança.*

#### `Envenenado`

Enquanto está `Envenenado`, você sofre os seguintes efeitos.

**Seus ataques.** Desvantagem.

**Testes.** Desvantagem em todo teste de perícia.

*Suor frio, mão tremendo, e tudo saindo pela metade.*

#### `Atordoado`

Enquanto está `Atordoado`, você sofre os seguintes efeitos.

**Ação.** Você perde a Ação Padrão e não usa reação. Quem tem mais de uma Ação Padrão no
turno — um chefe, um capanga grande — perde **uma**, e não todas.

*O mundo demora a voltar; a rodada passa por cima de você.*

> **Exemplo.** A Rina fica `Atordoada`. Ela perde a Ação Padrão daquele turno e não usa reação, então ninguém leva ataque de oportunidade dela. A Defesa continua a mesma: `Atordoado` não abre a guarda de ninguém. No fim do turno dela, como é uma condição `Pesada`, ela faz o Teste de Resistência e pode sair sozinha.

### Condições em uma linha

Para consulta na mesa. O efeito inteiro de cada uma está acima, na entrada dela.

**Condições em uma linha**
| condição | nível | o que faz |
|---|---|---|
| `Lento` | `Leve` | deslocamento pela metade, sem Ação Bônus |
| `Incapacitado` | `Leve` | não `Bloqueia`, e todo ataque corpo a corpo contra você é crítico |
| `Derrubado` | `Leve` | rasteja; desvantagem nos seus ataques; vantagem a quem ataca de perto |
| `Agarrado` | `Leve` | deslocamento `0` |
| `Desarmado` | `Leve` | bate desarmado até pegar a arma de volta |
| `Surdo` | `Leve` | falha no que precise de audição, `−2` na iniciativa |
| `Calado` | `Média` | não conjura |
| `Enfeitiçado` | `Média` | não ataca quem enfeitiçou; ele tem vantagem social contra você |
| `Petrificado` | `Pesada` | `Incapacitado`, deslocamento `0`, resistência a todo dano |
| `Impedido` | `Pesada` | deslocamento `0`, desvantagem nos ataques e no Físico |
| `Cego` | `Pesada` | falha no que precise de vista, desvantagem nos ataques |
| `Amedrontado` | `Pesada` | desvantagem enquanto vir a fonte, e não se aproxima dela |
| `Envenenado` | `Pesada` | desvantagem nos ataques e em todo teste de perícia |
| `Atordoado` | `Pesada` | perde a Ação Padrão e a reação |

### `Atordoado` e `Incapacitado`

Nenhuma das duas contém a outra. Escolher uma para aplicar é escolher o que você quer tirar do alvo:

**`Atordoado` e `Incapacitado`**
| | o eixo que ela ataca |
|---|---|
| `Atordoado` | tira **parte do turno**: uma Ação Padrão e a reação. Você continua se defendendo |
| `Incapacitado` | tira a **defesa**: você age e não se protege |

`Paralisado` não existe neste sistema. O que outros jogos chamam assim se chama `Atordoado` aqui, e não há um terceiro degrau que some os dois.

> **Metade do `Incapacitado` só aparece se a sua mesa usa `Bloquear`.** A outra metade — todo ataque corpo a corpo contra você é crítico — vale sempre, com `Bloquear` ligado ou não.
### `Inconsciente`, `Exaustão` e `Invisível`

Estas três não são condição.

**`Inconsciente`, `Exaustão` e `Invisível`**
| não é condição | onde ela está |
|---|---|
| `Inconsciente` | é cair a 0 de vida, com regra própria no capítulo 1, *Como Jogar* |
| `Exaustão` | é relógio de descanso, e mora no capítulo 5, *Descanso e Recuperação* |
| `Invisível` | é benefício, e as condições são compradas para aplicar num alvo |

A `Exaustão` engana: em outros jogos ela é condição, aqui não. Quem for escrever feitiço que canse alguém não alcança a exaustão pela Melhoria `Condição`.

### Comprar uma condição

> **Existe uma Melhoria `Condição`, uma só, e o preço dela é o nível da condição que você escolheu.**
> Escolher `Derrubado` custa `Leve`. Escolher `Petrificado` custa `Pesada`.

Você aponta a condição nas tabelas acima, lê o nível dela, e esse é o preço. Não existe pacote nem grupo de compra.

> **Exemplo.** O Kaito está montando um feitiço de Classe 2 que derruba quem for acertado. Ele compra a Melhoria `Condição` e escolhe `Derrubado`, que é `Leve`. Numa Classe 2 isso custa `1` ponto, e ele fica com o resto do orçamento em dados de dano. Se ele quisesse `Impedido`, que é `Pesada`, o mesmo feitiço pagaria `3` e sairia bem menor.

### Tirar uma condição

> **Tirar uma condição de alguém custa `1` ponto de energia por nível: `1` para `Leve`, `2` para `Média`, `3` para `Pesada`.**

Você só faz isso se tiver uma habilidade que tire condição, e cada habilidade dessas tem um teto de quanta energia ela gasta por uso. O teto é que decide o que você alcança: com teto `2` você limpa `Leve` e `Média`, e a `Pesada` fica fora até o teto subir.

> **Exemplo.** A Mei tem uma habilidade de tirar condição com teto de `2` pontos de energia por uso. O aliado dela está `Calado`, que é `Média`: ela gasta `2` e limpa. No turno seguinte o mesmo aliado fica `Cego`, que é `Pesada`: ela precisaria de `3`, e não consegue até a habilidade dela crescer.

## Cobertura

Cobertura é o que está entre você e quem está atirando. São três degraus, e você lê o que enxerga do alvo para saber em qual deles ele está. A pergunta que o mestre faz é sempre a mesma: daqui, quanto do corpo dele dá para acertar?

**Degraus de cobertura**
| cobertura | o que ela dá | exemplo |
|---|---|---|
| **Parcial** | **`+2` de Defesa e `+2` no Teste de Resistência Físico** | mureta, tronco, uma criatura no caminho |
| **Boa** | **`+5` de Defesa e `+5` no Teste de Resistência Físico** | seteira, olhando por cima de uma parede, metade do corpo atrás de um canto |
| **Total** | **você não pode ser escolhido como alvo** | parede inteira, do outro lado da porta |

> **Vale contra o que vem do outro lado da cobertura, e só.** Quem está atrás de uma mureta não ganha nada contra quem já está do lado de cá dela.
>
> **Só a maior conta.** Duas coberturas parciais não viram uma boa.

O Teste de Resistência que a cobertura ajuda é o **Físico**, seja qual for o atributo em que você o travou na criação. Quem travou em Força também se abaixa atrás de uma mureta.

A **Total** tira você da lista de alvos possíveis, e não dá número nenhum. Um efeito que pega área continua alcançando quem está atrás dela, se o efeito não precisar de linha até o alvo.

> **Exemplo.** O Sousuke está agachado atrás do capô de um carro, com meio corpo de fora. Isso é cobertura **Boa**: a Defesa dele sobe `5` contra quem atira do outro lado do estacionamento. Ele decide se jogar inteiro para trás do carro e passa a ter cobertura **Total**, então ninguém do outro lado consegue escolher ele como alvo. Mas um feitiço de área que estoura embaixo do carro não precisa de linha até ele, e alcança do mesmo jeito. Como a **Total** não dá número, o Teste de Resistência Físico dele sai limpo, sem os `5` que ele tinha um segundo antes.

---


# Capítulo 5 · Descanso e Recuperação

*fonte: `manual/70-descanso-e-recuperacao.md`*

O combustível volta em dois momentos, e os dois são de ficção.

> **Descanso curto: você parou entre uma luta e outra.** Ninguém está te caçando agora.
>
> **Descanso longo: a missão acabou.** Você parou de trabalhar.

Não existe contagem de horas em lugar nenhum deste capítulo. O gatilho é o que aconteceu na história, e é isso que faz dois mestres diferentes chamarem o mesmo momento de descanso.

## Cena

`Por cena` é o relógio mais usado do manual, então a palavra precisa de definição própria.

> **Quem conta é o mestre.** Uma cena pode ser uma sala, um segmento de salas, ou um combate. **Ela acaba quando a pressão daquele pedaço acaba**: o inimigo caiu, a porta fechou, o grupo saiu dali.

É a mesma forma da contagem de luta, mais adiante, e pelo mesmo motivo: *"isso foi uma cena?"* é pergunta sobre o pedaço de jogo que aquele mestre acabou de dirigir.

## Ambiente propício

Quase tudo neste capítulo depende de uma pergunta só: o lugar onde você parou tem recursos?

> **Ambiente propício é um lugar com gente, suprimento e teto.** Talismã, kit, comida, alguém que sabe costurar um corte. É a diferença entre voltar para a escola e dormir no mato.

Contam como propício:

- a escola, e qualquer campus da instituição
- um posto oficial ou barreira montada da instituição
- a casa de um clã que te recebe
- um hospital, jujutsu ou comum
- um veículo de apoio, com o kit dentro

> **O mestre tem a palavra final, sempre.** A lista existe para ele não precisar decidir do zero, não para amarrá-lo. Um santuário abandonado com um velho que já foi feiticeiro pode ser propício; a escola sob ataque pode não ser.

Quando der para declarar isso na abertura da missão, declare: vira informação tática, e o grupo planeja em cima dela em vez de descobrir na hora.

## Recuperação

O PE é o que você tem para a missão inteira. Só o descanso longo devolve tudo.

### PE

Os pontos de energia amaldiçoada que você gasta para conjurar.

### Descanso curto

**Descanso curto**
| | devolve |
|---|---|
| **PE** | **25% do seu máximo** |
| **Vida** | nada |
| **Usos `por descanso curto`** | recarregam |

Os 25% valem em qualquer lugar. O que o ambiente propício faz é **proteger esse número da exaustão**: fora dele, cada degrau de exaustão corta um pedaço, até sobrar nada.

Vida não volta sozinha no respiro entre lutas, porque quem conserta gente neste mundo é a Energia Reversa. O que já cura no descanso curto, como a Passiva `Reversão`, continua valendo o que vale.

### Descanso longo

**Descanso longo**
| | em ambiente propício | fora dele |
|---|---|---|
| **PE** | **cheio** | **metade do seu máximo** |
| **Vida** | **cheia** | **metade do seu máximo** |
| **Exaustão** | **zera** | **não zera** |
| **Integridade** | **cheia**, e os estágios limpam | **cheia**, e os estágios limpam |

A metade é sempre metade do **máximo**, nunca metade do que sobrou. Um Emanador de nível 10 com pool 60 que dorme no campo acorda com 30. No quarto dia de campo ele continua acordando com 30.

A Integridade volta inteira em qualquer lugar. É a única coisa que o ambiente não toca: não precisa de enfermaria quem precisa é do músculo.

> **Frações.** Arredonde para baixo, e o que você recupera nunca fica abaixo de 1.

O piso de 1 não desfaz um zero escrito. Quando a tabela `Degraus de Exaustão` diz que no degrau 3 você recupera **nada**, ela diz nada: o piso existe para a conta que deu 0,4.

## Exaustão

> **Da quarta luta do dia em diante, cada luta dá um degrau de exaustão. Máximo de três.**

As três primeiras lutas do dia são de graça.

### Contagem de luta

> **Quem conta é o mestre, e ele conta como em qualquer mesa: foi uma luta se pareceu uma luta.**

Não depende de ter rolado iniciativa. Uma perseguição que virou briga no meio conta; uma emboscada de uma rodada em que ninguém revidou pode não contar. E não é só maldição: feiticeiro contra feiticeiro cansa igual, e às vezes mais.

Costumam contar:

- um combate com inimigo que reage, maldição ou feiticeiro
- uma fuga em que o grupo gastou recurso para escapar
- um ritual ou uma contenção sob pressão, com alguém tentando impedir

Costumam não contar: a maldição de nível baixo que morre no primeiro golpe, o treino, a discussão que não virou porrada.

### Degraus

**Degraus de Exaustão**
| degrau | o que pega | quanto o descanso curto devolve, fora de ambiente propício |
|---|---|---|
| **0** | — | 25% |
| **1** | desvantagem em perícia e ofício | 15% |
| **2** | deslocamento cai para 6 m | 5% |
| **3** | desvantagem em ataque e em Teste de Resistência | nada |

Desvantagem é rolar dois d20 e ficar com o menor.

**Em ambiente propício o descanso curto devolve 25% em qualquer degrau.** A exaustão só corta o combustível de quem está longe de casa.

Os degraus sobem por consequência e não por tamanho: o primeiro pega o que você faz fora de combate, o segundo pega posicionamento, e só o terceiro pega a rolagem de luta. **O degrau 1 não é o leve** — ele tira o mesmo que o 3, em cima de outra coisa.

### Exaustão e Integridade ao mesmo tempo

As duas escadas se parecem muito, e é comum estar nas duas.

**Exaustão e Integridade**
| | exaustão | Integridade |
|---|---|---|
| **degrau 1** | desvantagem em perícia e ofício | desvantagem em testes de perícia |
| **degrau 2** | deslocamento cai para 6 m | deslocamento pela metade, e +1 PE por Classe |
| **degrau 3** | desvantagem em ataque e em Teste de Resistência | desvantagem em ataque e em Teste de Resistência, e teto de Classe |

> **Quem está nas duas pega o pior, não soma.**

Desvantagem não empilha com desvantagem, e dois cortes de deslocamento não se multiplicam. O que só uma das duas tem continua valendo normalmente: o +1 PE por Classe e o teto de Classe são da Integridade e não competem com nada do lado da exaustão.

### Teto

A exaustão para no terceiro degrau. Uma missão de campo de três dias com quatro lutas por dia acumula três degraus e trava ali: o grupo fica pior, sabe **quanto** pior, e escolhe se continua.

> **O mestre pode tirar um degrau quando a ficção pedir.** Uma noite de sono de verdade, um chá que alguém sabia fazer, um dia parado.

A válvula só anda para um lado. O mestre nunca adiciona degrau fora da regra.

## Relógios

**Relógios**
| relógio | recarrega quando | frequência |
|---|---|---|
| **por cena** | a cena acaba | a mais frequente |
| **por descanso curto** | você para entre lutas | ↓ |
| **por dia** | você dorme | ↓ |
| **por descanso longo** | a missão acaba | a menos frequente |

`Por dia` e `por descanso longo` não são a mesma coisa, e a diferença aparece em missão comprida. Uma missão pode durar cinco dias: quem tem alguma coisa `por dia` recarrega cinco vezes; quem tem `por descanso longo` recarrega uma.

## Exemplo

> **A Kaori** — Bastião de nível 2, Constituição 2. Vida 23, PE 8.
>
> **Manhã.** Sai da escola com tudo cheio.
>
> **Primeira luta.** Gasta 6 PE e leva 9 de dano. Fica com 2 PE e 14 de vida.
>
> **Descanso curto, no carro de apoio.** O carro está na lista: ambiente propício. Volta 25% de 8 = **2 PE**, e ela fica com 4. A vida não volta, porque ninguém ali sabe curar.
>
> **Segunda luta.** Gasta 3 PE e leva 7 de dano. Fica com 1 PE e 7 de vida.
>
> **Descanso curto, num prédio abandonado.** Não é propício, mas ela está no degrau 0 de exaustão, e no degrau 0 não há corte. Recupera os mesmos **2 PE**, ficando com 3.
>
> **Terceira luta.** Gasta 3 PE e sobrevive com 3 de vida e 0 PE, socando.
>
> **Quarta luta?** Se acontecer, ela ganha o primeiro degrau de exaustão: desvantagem em perícia e ofício.
>
> **Fim da missão, de volta na escola.** Ambiente propício: PE cheio, vida cheia, exaustão zerada, Integridade cheia.
>
> **Se a missão não tivesse acabado** e ela dormisse no mato: 4 PE, 11 de vida, e a exaustão que tivesse continuaria com ela.

O prédio abandonado sozinho não é problema. O prédio abandonado **com você cansado** é.

---


# Capítulo 6 · Criação de Personagem

*fonte: `manual/20-criacao-de-personagem.md`*

Uma ficha de feiticeiro cabe numa página e leva de vinte a quarenta minutos para montar. A parte longa é uma só: escrever a técnica.

## Peças da ficha

- **Uma técnica** que só você tem, escrita por você
- **Cinco atributos**, de 0 a 6
- **Um Caminho e uma Trilha**, que dizem o seu lugar numa equipe e quem você é dentro dele
- **Uma Origem**, que diz de onde veio o seu poder
- **Oito perícias e três ofícios** treinados, ou nove e dois, você escolhe
- **Dois Testes de Resistência** treinados, de quatro
- **Dois Legados**, das listas da sua Origem
- **Cinco feitiços**: dois pequenos e grátis, três de verdade
- **Os números que caem sozinhos**: vida, energia, Defesa, iniciativa

## Nível inicial

> **Personagem novo começa no nível 2.** Não existe ficha de nível 1 padrão.

O nível 1 é o personagem antes de virar feiticeiro: a pessoa que ainda não conjura, o Itadori antes do dedo. Ele fica como opção de campanha para quem quiser jogar essa parte.

No nível 2 você já tem técnica, já tem feitiço e já dá para encarar uma missão. As contas do passo 7 presumem o nível 2.

## Ordem dos passos

> **Origem → a Regra em uma frase → Caminho → Atributos → a técnica inteira → perícias e ofícios → os números → Pactos.**

A técnica sai partida em duas: a Regra, uma frase só, vem no passo 2, antes do Caminho decidir nada por você; o resto espera até o passo 5, depois que o Caminho e os atributos já estão na ficha.

## Passo 1 · Origem

De onde vem o seu poder. Nasceu com você, veio no sangue de um clã, você virou recipiente de alguma coisa, alguém te fez, ou trocaram uma coisa por outra antes de você nascer.

São sete Origens, mais a sub-origem Sem Técnica. Escolha e anote na ficha:

**Anotações da Origem**
| O que anotar | De onde sai |
|---|---|
| Uma perícia | da lista de quatro da sua Origem |
| Uma perícia livre | que a sua história justifique, com o mestre aprovando na leitura |
| Um ofício livre | ou, se você não quiser ofício, mais uma perícia |
| Um Teste de Resistência treinado | qualquer um dos quatro; o outro vem do Caminho |
| Um traço | do catálogo da sua Origem, ou escrito por você |
| Dois Legados | um `Destranca` obrigatório, mais um de qualquer formato |
| A rota de criação | por onde você monta o seu poder |

As listas de perícia, os traços e as rotas estão no capítulo 7, *Origens e Legados*, e é lá que estão também as listas de Legado de cada Origem.

A Origem não dá ponto de atributo nenhum, e não decide a sua patente: todo personagem começa **Grau 4**, venha de onde vier.

> **A Sem Técnica não fecha ficha hoje.** Ela é a única assim, e a tabela `Rotas de criação`, no fim do capítulo 7, *Origens e Legados*, diz por qual rota cada uma das outras monta o poder.

> **Duas rotas não montam poder pelo Fundamento**, e sim pela Técnica Marcial, no capítulo 10: o Corpo Amaldiçoado e a Restrição Celestial pelo ramo sem energia. Se for o seu caso, o Passo 2 e o Passo 3 valem igual — o que muda é o capítulo que você abre para montar.

## Passo 2 · Regra da técnica

Uma frase que diz o que a sua técnica faz com o mundo, sem falar em efeito nem em dano.

> *"Tudo que eu prendo entre as minhas mãos fica mais pesado."*
>
> *"Eu troco de lugar com qualquer coisa do meu tamanho que eu esteja enxergando."*
>
> *"Quem mente na minha frente sangra."*

Uma frase, verificável pela mesa, sem número. Você carrega ela a campanha inteira, porque a técnica nunca muda. O que evolui é o que você consegue fazer com ela.

Pare aqui e vá para o Caminho. O resto da técnica volta no passo 5.

## Passo 3 · Caminho e Trilha

Que lugar você ocupa numa equipe. Um Caminho por personagem, escolhido agora e para sempre. Não existe multiclasse.

**Caminhos**
| Caminho | O que ele é | Atributos naturais |
|---|---|---|
| **Bastião** | o corpo como resposta: aguentar, encarar, prender | Força, Constituição |
| **Vanguarda** | a arma como resposta: alcançar, cortar, acabar | Destreza, Força |
| **Guia** | o outro como resposta: estender, recuperar, reposicionar | Essência |
| **Emanador** | a técnica como resposta: mais feitiço, mais aptidão | Inteligência, Essência |
| **Evocador** | o que você trouxe como resposta: invocações | Inteligência, Essência |

O Caminho mexe em posicionamento, alvo, duração e recuperação. Ele nunca mexe em dados de dano, Classe de feitiço, Melhoria de graça ou cura.

### Características do Caminho

**Características do Caminho**
| Caminho | Vida inicial | Vida por nível | PE por nível | Perícias fixas |
|---|---|---|---|---|
| **Bastião** | 12 (d12) | 7 | 4 | Atletismo · Intimidação |
| **Vanguarda** | 8 (d8) | 5 | 5 | Acrobacia · Percepção |
| **Guia** | 8 (d8) | 5 | 5 | Persuasão · Medicina |
| **Evocador** | 6 (d6) | 4 | 6 | Religião · Lidar com Animais |
| **Emanador** | 6 (d6) | 4 | 6 | Ocultismo · Investigação |

Mais **quatro perícias à sua escolha**, de qualquer lugar do quadro, **dois ofícios à sua escolha** e **um Teste de Resistência treinado**.

### Trilha

A Trilha é escolhida agora, junto do Caminho, e nasce com o personagem. São três por Caminho: Muro · Punho · Brasa no Bastião, Estocada · Batedor · Executor na Vanguarda, e assim por diante. A lista está no capítulo 8, *Caminhos e Trilhas*.

> **A Trilha já entrega no nível 2**, junto do primeiro degrau do Caminho, e volta a entregar nos níveis 11, 19 e 27. O texto de cada uma está no capítulo 8, *Caminhos e Trilhas*.
>
> **As três do Evocador são a exceção:** `Servo`, `Matilha` e `Coro` concedem o corpo da invocação, e as entregas de nível delas ainda não existem. Se for a sua escolha, combine com o mestre o que ocupa essas casas.

## Passo 4 · Atributos

> **Nove pontos entre os cinco atributos. Nenhum acima de 3.**

O número **é** o modificador. Não existe valor separado nem tabela de conversão. A escala vai de 0 a 6, e 6 é o topo humano. Uma distribuição legal, por exemplo, é 3 · 2 · 2 · 1 · 1.

O que cada atributo governa está na tabela `Atributos` do capítulo 1, *Como Jogar*.

Inteligência sabe; Essência percebe. Sentir energia amaldiçoada é a sua energia reagindo à de outro.

> **Trave agora o seu Teste de Resistência Físico.** Ele usa Força ou Destreza, você escolhe na criação e não muda depois.

## Passo 5 · Técnica inteira

Aqui você abre o capítulo 9, *Fundamento*. É a parte longa. Você já tem a Regra e já sabe o Caminho; falta o resto.

1. **Descrição.** De onde a técnica veio, como ela aparece, o que as pessoas veem quando ela age. Sem efeito mecânico.
2. **Famílias.** Duas **Livres**, cujas Melhorias custam metade da Classe a menos, e três **Fechadas**, das quais você nunca compra nada.
3. **Selo.** O gesto, a condição ou o objeto que a sua técnica exige. Não custa nem devolve ponto. Restrição que o Selo já obriga não devolve ponto.
4. **Passiva Livre.** Uma, de graça, para todo mundo. Ela não rola dado, não muda número e não faz ninguém rolar.
5. **Os feitiços.** No nível 2 você tem **Classe 1**, dois feitiços de **Classe 0** (grátis, não ocupam espaço) e **três feitiços conhecidos**, montados pelo orçamento da Classe 1. Três é o que a fórmula `2 + (nível ÷ 2)` dá no nível 2.

> **A Regra da técnica é lida por outra pessoa antes de entrar em jogo.** Quem escreveu sabe o que quis dizer; quem vai arbitrar, não.

## Passo 6 · Perícias, ofícios e Testes de Resistência

**Treino na criação**
| De onde vem | Perícias | Ofícios | Teste de Resistência |
|---|---|---|---|
| **Caminho** | 2 fixas + 4 à sua escolha | 2 à sua escolha | 1 |
| **Origem** | 1 da lista dela + 1 livre | — | 1 |
| **Origem, o extra** | *ou* mais 1 perícia | *ou* 1 ofício livre | — |

O extra da Origem é uma escolha entre duas rotas, e as duas fecham a ficha:

**Rotas do extra**
| Rota do extra | Perícias | Ofícios |
|---|---|---|
| pegando o ofício | 8 de 23 | 3 de 11 |
| pegando a perícia | 9 de 23 | 2 de 11 |

Os dois Testes de Resistência treinados saem de quatro: Físico, Vigor, Espírito e Intelecto. Um vem da Origem, o outro do Caminho.

Perícia pertence a um atributo fixo: Atletismo é sempre Força. Ofício não pertence a atributo nenhum. O atributo muda conforme o que você faz com ele, e quem decide é o mestre na hora. Forjar uma lâmina é Força, falsificar uma assinatura é Destreza, saber qual selo o papel pede é Inteligência, e as três coisas são o mesmo ofício.

> **Perícia sem treino você tenta; ofício sem treino, não.** Qualquer um escala e falha. Ninguém forja uma lâmina por tentativa.

O quadro completo das perícias e dos ofícios está no capítulo 3, *Perícias e Ofícios*.

## Passo 7 · Números derivados

Nada aqui é escolha. Você copia da tabela e faz a conta.

**Números do nível 2**
| Número | Como sai |
|---|---|
| Maestria | 1 |
| Refino | 1 |
| Pontos de vida | (vida inicial do Caminho + Constituição) + (vida por nível do Caminho + Constituição) |
| Integridade | 28 |
| Pontos de Energia | PE por nível do Caminho × 2 |
| Defesa | 10 + Destreza + 1 |
| Iniciativa | d20 + Destreza |
| Deslocamento | 9 metros |
| Ataque corpo a corpo | d20 + Força + 1 |
| Ataque à distância | d20 + Destreza + 1 |
| Ataque de conjuração | d20 + atributo da técnica + 1 |
| CD de feitiço | 8 + atributo da técnica + maestria |
| Perícia treinada | d20 + atributo + 1 |
| Teste de Resistência | d20 + atributo do TR + maestria, e a maestria só se treinado |

No refino 1 você já tem duas aptidões, de graça: `cobrir-se de energia`, que dá proteção sem equipamento, e `canalizar energia`, que permite ferir uma maldição com o corpo ou com a arma. São básicas de qualquer feiticeiro.

> **Toda ficha de nível 2 nasce com proteção 1.** É o `+1` que entra na Defesa acima. Sem Traje e sem Revestimento, a sua proteção é `1/3 do refino + 1`, que no refino 1 dá 1. Escudo soma com ela; Traje e Revestimento desligam.

## Passo 8 · Pactos

Opcional, e a maioria dos personagens começa sem.

Pacto é o que você trocou por poder, e três das quatro formas dele já têm onde morar:

**Formas de pacto**
| O que você quer dizer | Onde isso se escreve |
|---|---|
| *"a minha técnica fica maior sob uma condição que eu aceitei"* | **Restrição**, por feitiço, no capítulo 9 |
| *"a minha técnica impõe uma regra ao mundo"* | **`Regra Própria`**, por técnica, no capítulo 9 |
| *"eu troquei uma coisa antes de a campanha começar"* | **Legado**, na criação, no capítulo 7 |
| *"eu e mais alguém fechamos um trato, aqui, na mesa"* | ainda não tem regra |

> **Pacto entre personagens não entra na criação.** Quem quiser começar com um usa a `Regra Própria` ou um Legado, que é onde essa ficção já mora. O mestre continua podendo abrir um em jogo, com o preço escrito na ficha.

## Exemplo

**A Kaori**, feiticeira de nível 2.

### Origem

**Descendente.** Um clã menor que perdeu o nome faz três gerações. Como todo mundo, ela começa Grau 4: quem abre porta pra ela é o sobrenome, mesmo com a patente baixa.

- *Perícia da lista* (Hierarquia · História · Ocultismo · Persuasão): **Hierarquia**
- *Perícia livre:* **História**, porque ela cresceu ouvindo de quem o clã perdeu o nome
- *Extra:* pegou o **ofício**, e escolheu **Herbalismo**, da avó
- *Teste de Resistência:* **Vigor**
- *Traço:* o ramo do clã que perdeu, e ela é dele
- *Legado · `Destranca`:* **O Sobrenome**, que dá audiência em qualquer lugar do meio jujutsu. Ser bem recebida é outra história
- *Legado · o segundo:* **Biblioteca**, que uma vez por cena refaz um teste de História ou Ocultismo. A casa tinha os livros, e ela foi obrigada a ler

### Regra

*"Tudo que eu prendo entre as minhas mãos fica mais pesado."*

### Caminho e Trilha

**Bastião**, Trilha **Muro**: o corpo é o escudo, e é o que a Regra dela já pedia. *Teste de Resistência do Caminho:* **Físico**.

### Atributos

Força 3 · Constituição 2 · Destreza 2 · Inteligência 1 · Essência 1. Nove pontos, nenhum acima de 3, e o **TR Físico travado em Força**.

### Técnica

*Famílias Livres:* Controle e Castigo. *Fechadas:* Amparo, Área e Auxiliares, porque ela não cura, não pega área e não dá suporte. *Selo:* as duas mãos precisam se tocar antes. *Passiva Livre:* ela sabe o peso exato de qualquer coisa que encoste nela.

### Perícias e ofícios

**Oito perícias.** Do Caminho, fixas: Atletismo e Intimidação. Do Caminho, livres: Sentir Energia, Percepção, Sobrevivência e Intuição. Da Origem: Hierarquia e História.

**Três ofícios.** Forja e Caligrafia, os dois livres do Caminho, e Herbalismo, o extra da Origem.

### Números

**Números da Kaori**
| | Conta | Resultado |
|---|---|---|
| Vida | (12 + 2) + (7 + 2) | **23** |
| Integridade | fixa | **28** |
| PE | 4 × 2 | **8** |
| Defesa | 10 + 2 + 1 | **13** |
| Iniciativa | d20 + 2 | |
| Ataque corpo a corpo | d20 + 3 + 1 | **d20 + 4** |
| Ataque de conjuração | d20 + 3 + 1 | **d20 + 4** |
| CD dos feitiços dela | 8 + 3 + 1 | **12** |
| Atletismo (treinado) | d20 + 3 + 1 | **d20 + 4** |

## Conferência da ficha

Sete perguntas, e todas têm resposta objetiva. Você mesmo passa por elas antes de entregar.

1. **Os atributos somam nove, e nenhum passa de 3?**
2. **O Teste de Resistência Físico está travado** em Força ou Destreza?
3. **São oito perícias e três ofícios, ou nove e dois?** As duas rotas são legais; o que não pode é somar as duas. E as duas perícias fixas do Caminho precisam estar entre elas.
4. **São dois Testes de Resistência treinados**, um da Origem e um do Caminho?
5. **A Regra da técnica cabe em uma frase**, é verificável pela mesa e não tem número?
6. **Alguém que não seja o dono leu a técnica?**
7. **Os três feitiços conhecidos fecham no orçamento da Classe 1?** Três pontos cada.

O mestre pode recusar mesmo quando a ficha passa nas sete.

---


# Capítulo 7 · Origens e Legados

*fonte: `manual/25-origens.md`*

A Origem responde uma pergunta só: de onde veio o seu poder. O que você faz com ele é a técnica; o seu lugar numa equipe é o Caminho.

São sete Origens. Cinco principais (Latente, Receptáculo, Descendente, Reencarnado e Feto) e duas especiais, Corpo Amaldiçoado e Restrição Celestial. Existe ainda uma sub-origem, Sem Técnica, que se soma a qualquer uma das cinco principais.

## Características da Origem

**Características da Origem**
| O que você anota | Detalhe |
|---|---|
| **Uma perícia** | da lista de quatro da sua Origem |
| **Uma perícia livre** | que a sua história justifique; o mestre aprova na leitura |
| **Um ofício livre** | ou, se você não quiser ofício, mais uma perícia |
| **Um Teste de Resistência treinado** | qualquer um dos quatro; o outro vem do Caminho |
| **Um traço** | do catálogo dela, ou escrito por você |
| **Dois Legados** | um `Destranca` obrigatório, mais um de qualquer formato |
| **A rota de criação** | por onde você monta o seu poder |

### Limites

Três coisas ficam de fora.

#### Atributo

Nenhuma Origem dá ponto de atributo. Ser recipiente de alguma coisa te dá um passageiro, e o corpo continua exatamente o que era.

#### Feitiço

Nenhuma Origem abre Família, fecha Família, dá Melhoria nem muda Classe.

#### Patente

Todo personagem começa **Grau 4**, venha de onde vier. A patente é eixo social e narrativo, e ela sobe por feito. A instituição pode classificar quem ela quiser onde ela quiser; nenhuma Origem começa na frente.

### Como ler uma Origem

Toda Origem abre pela frase que a resume, seguida do que é ser aquilo no mundo e de quem a carrega na obra.

Depois vem **O que muda**, sempre na mesma ordem: as **Perícias**, a lista de quatro de onde você escolhe uma; os **Traços**, três sugestões que você usa como estão ou troca por uma escrita por você; e a **Criação**, a rota por onde você monta o seu poder. As duas Origens especiais mexem nessa rota, e o texto delas diz como.

Por último vêm os **Legados** da Origem, nos três formatos, cada um com a sua tabela e o texto de cada entrada.

## Legados

Legado é um benefício pequeno e específico que você trouxe de antes de a história começar. Você recebe dois na criação e mais nenhum, nunca: não sobe com o nível, não aparece em marco, não se compra. Legado nenhum produz dano ou escala com nível.

> **Um deles é obrigatoriamente um `Destranca`, e `Destranca` é zero no dado.**
> O outro sai de qualquer lista da sua Origem, em qualquer um dos três formatos.

Cada um dos três formatos se lê de um jeito.

Quando uma entrada termina numa linha *Na mesa*, essa linha diz em que tipo de cena o Legado costuma aparecer e o que ele destrava para o grupo. A regra é o que veio antes dela.

### Como ler um Destranca

Um Destranca abre uma porta: um lugar onde você é recebido, uma coisa que você sabe, uma pessoa que existe no mundo por sua causa. Ele nunca mexe em acerto, CD ou dano.

Cada tabela de `Destranca` traz o nome e o **relógio**: quantas vezes por período você pode puxar o gatilho que arranca do mestre uma verdade que ele até então guardava. A maioria não tem relógio, e a afirmação vale sempre, sem contagem. Só quando o Destranca obriga o mestre a te entregar uma informação nova é que ele ganha relógio, pela mesma escada de sempre: por cena, por descanso curto, por dia, por descanso longo, do mais frequente ao mais raro.

### Como ler um Ajusta

Um Ajusta mexe num número de uma rolagem. Quase sempre de um dos dois jeitos: você refaz um teste que já falhou, ou rola com **vantagem** (joga dois dados e fica com o melhor resultado).

Cada tabela de `Ajusta` traz duas coisas além do nome. **Alcança** diz quantas coisas nomeadas o gatilho cobre: uma perícia só, uma condição só, ou uma categoria inteira (qualquer perícia, qualquer ofício). **Relógio** diz quantas vezes por período você pode usar, na mesma escada: por cena, por descanso curto, por dia, por descanso longo. Quanto mais largo o alcance, mais raro o relógio.

### Como ler um Desliga

Um Desliga apaga uma coisa que aconteceria com você, sempre que a situação aparecer, sem rolagem nenhuma. Não existe "tentar" um Desliga; ou a situação bateu e ele age, ou não bateu.

Cada tabela de `Desliga` traz o que ele **apaga** e o **relógio**. A maioria dos Desliga vale sempre, sem contagem, porque apagar algo pontualmente não pesa como uma rolagem extra. O texto de cada entrada também diz o que você paga em troca: nenhum Desliga é só ganho.

## Latente

*Você nasceu com. Ninguém te deu nada e ninguém te ensinou.*

A técnica é sua desde sempre, e o que fez ela aparecer foi você, um susto, ou a vida. Um dia a coisa saiu da sua mão e não tinha ninguém por perto para explicar o que aquilo era. A maior parte dos Latentes passa anos achando que o problema é médico, ou espiritual, ou culpa deles.

O meio jujutsu chega depois, e chega atrasado. Quando chega, chega avaliando: um feiticeiro de campo que sentiu alguma coisa, um professor de escola técnica atrás de aluno, ou gente pior que os dois. Um Descendente aprende o nome da própria técnica aos seis anos, junto com a tabuada. Você descobre que ela tem nome no dia em que alguém te olha e diz qual é. Daí vem a fama da Origem: Latente é onde mais tem gente que aprendeu errado antes de aprender certo, com vício de mão, gasto burro de energia e medo do próprio alcance.

A instituição gosta de Latente e desconfia de Latente pelo mesmo motivo. Gosta porque você não deve favor a clã nenhum e ninguém te reivindica em reunião. Desconfia porque não existe registro do que você faz, e a única fonte sobre a sua técnica é você. É a Origem mais comum entre feiticeiros que não têm sobrenome, e a que mais aparece em pasta aberta quando alguém some da vista da escola por seis meses.

**Na obra:** Nanami e Hakari, que não vêm de clã e construíram sozinhos o que fazem. O Junpei também: a técnica dele, Escória da Lua, era inata, e o que o Mahito fez foi mexer no cérebro dele para que ela despertasse antes da hora.

### Efeito na ficha

#### Perícias

Escolha uma: Sentir Energia · Sobrevivência · Furtividade · Intuição

#### Traços

- o professor que você não teve
- a primeira vez em que quase morreu
- alguém comum que sabe o que você é

#### Criação

Fundamento, do jeito padrão.

### Legados da Latente

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca da Latente**
| Legado | Relógio |
|---|---|
| O Jeito Errado | por dia |
| O Professor Que Você Não Teve | sem relógio |
| A Testemunha | sem relógio |
| Sem Patente | sem relógio |
| Sem Técnica → ver *Sem Técnica* | sem relógio |

> **O Jeito Errado** — escreva na ficha o que você aprendeu errado antes de aprender certo. Uma vez por dia, aponte alguém que esteja fazendo a mesma coisa errada. O mestre diz o que aquilo está custando a essa pessoa.
> *Na mesa:* serve quando a equipe está olhando outro feiticeiro trabalhar, ou o estrago que um deles deixou para trás. Vira leitura de inimigo sem precisar de teste.

> **O Professor Que Você Não Teve** — existe um feiticeiro que podia ter te ensinado e não ensinou. Escreva quem é e por que não. Essa pessoa está viva, sabe que você existe, e a escolha dela ainda está de pé.
> *Na mesa:* você entrega ao mestre um NPC competente com motivo pronto para negar ajuda. Ele volta na hora em que o grupo mais precisa de alguém desse nível.

> **A Testemunha** — alguém sem energia amaldiçoada sabe o que você é, e nunca contou para ninguém. Escreva quem é e o que essa pessoa viu. Ela continua na vida dela, e continua sabendo.
> *Na mesa:* é um endereço civil para onde a campanha pode voltar, e uma pessoa que o inimigo pode achar antes de você.

> **Sem Patente** — você nunca entrou na instituição, e ela sabe disso. Patente não te obriga a nada: ordem de superior é conselho, e a hierarquia te trata como o que você é, alguém que não deve nada e a quem não se deve nada.
> *Na mesa:* você é quem pode recusar uma ordem em cena, na frente de todo mundo, sem consequência disciplinar. O resto da equipe não pode.

> **Sem Técnica** — você tem energia amaldiçoada e a técnica não veio junto. O texto está adiante, em *Legado de Sem Técnica*.

#### Ajusta

**Ajusta da Latente**
| Legado | Alcança | Relógio |
|---|---|---|
| Aprendi Apanhando | qualquer perícia (23) | por dia |
| Instinto Bruto | Intuição (1) | por cena |
| Gambiarra | qualquer ofício (10) | por dia |
| Desconfiado | uma condição nomeada (1) | por cena |

> **Aprendi Apanhando** — uma vez por dia, refaça um teste de perícia que você falhou. Você já errou isso antes.
> *Na mesa:* é a rede que segura a cena travada por uma rolagem só. Uma por dia obriga a escolher qual falha valia desmanchar.

> **Instinto Bruto** — uma vez por cena, role Sentir Energia no lugar de Intuição, se disser como o seu jeito de sentir resolve aquilo.
> *Na mesa:* leitura de gente virando leitura de energia. Rende em interrogatório, em sala cheia e em negociação com quem está mentindo com o corpo.

> **Gambiarra** — uma vez por dia, use um ofício que você não tem treinado como se tivesse. Você já resolveu isso com o que estava na mão.
> *Na mesa:* aparece quando falta o especialista: fechadura, motor, curativo de emergência, papelada que precisa passar por um balcão.

> **Desconfiado** — uma vez por cena, role com vantagem o Teste de Resistência contra ficar `Enfeitiçado` (condição). Ninguém nunca te deu nada de graça, e você aprendeu cedo que quem se aproxima quer alguma coisa.
> *Na mesa:* cena de sedução, de promessa boa demais, de maldição que fala bonito antes de encostar.

#### Desliga

**Desliga da Latente**
| Legado | Apaga | Relógio |
|---|---|---|
| Inédito | ser reconhecido pelo catálogo | sempre |
| Chão Duro | a diferença entre lugar propício e lugar ruim | sempre |

> **Inédito** — a sua técnica não está em registro nenhum: ninguém a reconhece pelo catálogo, e preparar-se contra ela exige ter te visto fazer. Em troca, ninguém sabe te ajudar com ela pelo mesmo motivo: não existe quem tenha estudado o que você faz. *Não disponível para quem escolheu Sem Técnica: sem técnica própria, não há o que ficar de fora do catálogo.*
> *Na mesa:* transforma reencontro com o mesmo inimigo numa corrida. Ele só sabe de você o que te viu fazer, e está aprendendo em tempo real.

> **Chão Duro** — para você, qualquer lugar é ambiente propício. Você aprendeu a dormir no chão, comer o que tinha e acordar inteiro. Em troca, você não percebe quando os outros não estão aguentando; para você aquilo é terça-feira.
> *Na mesa:* apaga a logística de viagem, de cerco e de vigília longa. E cria atrito com o companheiro que está no limite e não sabe pedir.

## Receptáculo

*Você carrega alguma coisa, e ela ainda está aí.*

Um dedo, um selo, um feiticeiro de mil anos atrás. O que te habita divide o corpo com você, e você continua sendo você, com companhia. Tem quem tenha engolido por acidente, tem quem tenha engolido para salvar alguém na hora, e tem quem já tenha nascido com o hóspede dentro e só descoberto na adolescência.

A convivência tem horário e humor. Ele dorme, ele acorda, ele opina, e ele sabe coisa que você não sabe. Quando ele resolve falar, você é o único que escuta, e quando ele resolve calar, você fica sem a metade da informação que estava usando para decidir. Boa parte do tempo de mesa de um Receptáculo é negociação interna: o que você aceita ouvir, o que você aceita dever, e o que você faz quando ele acerta.

A instituição trata Receptáculo como material sob observação. Existe pasta, existe protocolo de contenção, e em quase todo caso existe uma ordem de execução assinada esperando gatilho. Você é útil enquanto for controlável, e o meio inteiro sabe disso. Feiticeiro de campo que vai trabalhar contigo quer saber o nome do que está dentro antes de virar as costas, e quem sabe o nome costuma tratar você pelo nome dele.

**Na obra:** o Itadori, que come o dedo e passa a dividir o corpo com o Sukuna, e que tem técnica inata própria por baixo disso. E a Hana Kurusu, em quem o Anjo vive simbioticamente, sem sobrescrever a consciência dela.

### Efeito na ficha

#### Perícias

Escolha uma: Sentir Energia · Ocultismo · Intuição · Religião

#### Traços

- o que ele quer, e não é o que você quer
- a testemunha do dia em que aconteceu
- a instituição sabe, e está observando

#### Criação

Fundamento, do jeito padrão. O passageiro mora na ficção da mesa, e a montagem da ficha é a mesma de qualquer feiticeiro.

### Legados do Receptáculo

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca do Receptáculo**
| Legado | Relógio |
|---|---|
| A Voz de Dentro | por dia |
| De Antes de Você | sem relógio |
| Alcunha | sem relógio |
| O Que Ele Quer | por descanso longo |
| Sem Técnica → ver *Sem Técnica* | sem relógio |

> **A Voz de Dentro** — uma vez por dia, pergunte ao mestre uma coisa sobre uma maldição ou técnica presente na cena. Ele responde com a verdade. O que está em você já viu aquilo.
> *Na mesa:* é reconhecimento de inimigo no meio da luta, sem rolagem. Use na criatura que ninguém identificou e a cena inteira muda de plano.

> **De Antes de Você** — escolha uma pessoa, um lugar ou um clã que conheceu o que te habita, de quando ele ainda andava sozinho. Eles existem, e sabem o que você carrega. O que fazem com essa informação é outra conversa.
> *Na mesa:* dá ao grupo uma porta de entrada em história antiga, com dono. Alguém lá dentro tem conta velha para acertar.

> **Alcunha** — escreva como ele era chamado quando andava sozinho. Quem é do meio e ouve esse nome sabe o que é, e reage antes de pensar. Você pode dizer o nome em voz alta quando quiser. Não tem como despronunciar.
> *Na mesa:* é uma arma social de uso único por sala. Dita a palavra, a negociação vira outra coisa, e você não escolhe qual.

> **O Que Ele Quer** — escreva na ficha o que ele quer, e não é o que você quer. Uma vez por descanso longo, você pode ceder: entregue a ele uma coisa que ele queria, e ele te dá passagem para o que você precisava. O mestre narra os dois lados. O que você cedeu fica escrito na ficha, e não sai de lá.
> *Na mesa:* é o botão que o jogador aperta quando a campanha está perdida. Cada aperto deixa marca permanente na ficha, e o grupo vê a conta crescer.

> **Sem Técnica** — você tem energia amaldiçoada e a técnica não veio junto. O texto está adiante, em *Legado de Sem Técnica*.

#### Ajusta

**Ajusta do Receptáculo**
| Legado | Alcança | Relógio |
|---|---|---|
| Não Sou Só Eu | Teste de Resistência de Espírito, três situações nomeadas (3) | por cena |
| Costume Antigo | uma perícia (1) | por cena |
| Tranco | Teste de Resistência Físico (1) | por cena |
| Passagem | qualquer rolagem | por dia |

> **Não Sou Só Eu** — uma vez por cena, refaça um Teste de Resistência de Espírito que você falhou contra ser controlado, dominado ou lido.
> *Na mesa:* segura o personagem contra o inimigo que ganha luta virando aliado contra aliado. Tem dois em casa, e convencer os dois dá trabalho.

> **Costume Antigo** — escolha uma perícia na criação: o que está em você já sabia fazer aquilo. Uma vez por cena, role essa perícia como se fosse treinada. Você lembra da sensação de fazer, sem lembrar de ter aprendido.
> *Na mesa:* rende cena curta de estranhamento. O personagem faz bem uma coisa que nunca praticou, e quem está junto repara.

> **Tranco** — uma vez por cena, refaça um Teste de Resistência Físico que você falhou. Ele não quer morrer nesse corpo mais do que você.
> *Na mesa:* é o segundo fôlego contra veneno, queda, agarrão e tudo que tenta te tirar da luta pelo corpo.

> **Passagem** — uma vez por dia, você deixa ele assumir: refaça qualquer rolagem. Quando você volta, o mestre diz uma coisa que ele fez enquanto estava no comando. Você não estava lá para impedir.
> *Na mesa:* o recurso mais largo do Receptáculo, e o único que devolve consequência escrita pelo mestre. Cada uso rende gancho de cena para depois.

#### Desliga

**Desliga do Receptáculo**
| Legado | Apaga | Relógio |
|---|---|---|
| Máscara | ser sentido pelo que você é | sempre |
| Revezamento | ficar `Impedido` | por descanso longo |

> **Máscara** — quem sente a sua energia amaldiçoada sente a dele. Você não aparece como o que é. Em troca, o que essas pessoas concluem sobre você costuma ser bem pior do que a verdade. Elas agem de acordo com essa conclusão.
> *Na mesa:* resolve infiltração e barreira de detecção, e cria a cena em que o aliado que chegou depois te ataca primeiro.

> **Revezamento** — prender você prende um dos dois: uma vez por descanso longo, você não fica `Impedido`. Ele empurra, e o seu corpo vai junto porque não é só seu. Em troca, quem estava olhando viu — naquele momento não era você que se mexia. O mestre diz o que as pessoas presentes passaram a achar de você, e elas agem de acordo.
> *Na mesa:* tira o grupo da cena em que prender você era o plano do inimigo, e cobra em reputação na cena seguinte.

## Descendente

*Você é de uma das famílias, e elas cobram.*

A técnica veio no sangue, com nome, com histórico e com gente que sabe usá-la melhor do que você. Você teve professor desde criança, e teve expectativa desde criança. Antes dos dez anos você já sabia qual ramo da família ia te medir, em que idade, e o que aconteceria com quem não passasse.

O meio te reconhece antes de te conhecer. Sobrenome abre porta e fecha porta na mesma proporção: quem odeia o seu clã não vai perguntar o que você acha dele antes de decidir o que acha de você. Cada família tem sua moeda de troca com o resto da sociedade jujutsu, e cada uma cobra a sua de você em particular: um cede nome, outro cede ferramenta, outro cede o arquivo de tudo que já fizeram com corpo, outro cede a palavra empenhada.

Para a instituição, Descendente é funcionário e representante estrangeiro ao mesmo tempo. Os clãs financiam boa parte da estrutura, indicam nome para cargo, e vetam quem quiserem sem precisar explicar. Isso significa proteção de que ninguém mais dispõe, e significa que a sua ficha disciplinar passa pela sua família antes de passar por você. O tipo de pessoa que sai daí costuma ser alguém treinado cedo demais para uma vida que não escolheu, com relação complicada com a única coisa que sabe fazer bem.

**Na obra:** Gojo, Inumaki, Kamo, Zen'in. As técnicas de clã têm nome próprio, e todo mundo do meio conhece.

### Efeito na ficha

#### Perícias

Escolha uma: Hierarquia · História · Ocultismo · Persuasão

#### Traços

- o casamento que já decidiram por você
- o parente que você não pode desapontar
- o ramo do clã que perdeu, e você é dele

#### Criação

Fundamento, do jeito padrão.

### Legados do Descendente

#### Destranca

*Escolha um destes, obrigatoriamente. Os quatro primeiros são arquétipos de clã; o quinto é para quem inventou o próprio; o sexto é a mesma sub-origem que as outras quatro Origens principais também alcançam.*

**Destranca do Descendente**
| Legado | O clã que ele desenha | Relógio |
|---|---|---|
| O Sobrenome | o clã do nome: *Gojo* | sem relógio |
| Armaria | o clã da ferramenta: *Zen'in* | sem relógio |
| Arquivo | o clã do corpo: *Kamo* | sem relógio |
| Palavra Dada | o clã da voz: *Inumaki* | sem relógio |
| Treino de Berço | qualquer clã, inclusive o seu | sem relógio |
| Sem Técnica → ver *Sem Técnica* | — | sem relógio |

> **O Sobrenome** — em qualquer lugar da sociedade jujutsu você consegue audiência com quem importa. Conseguir audiência não é o mesmo que ser bem recebido.
> *Na mesa:* pula a etapa de "como a gente chega até essa pessoa" e joga o grupo direto na sala difícil, que é onde a cena boa está.

> **Armaria** — a sua família guarda ferramenta amaldiçoada, e você sabe onde. Escreva na ficha qual peça é sua por direito e quem está com ela agora. Ela existe, é sua, e ninguém devolveu.
> *Na mesa:* é um objetivo de campanha com endereço e com nome de quem vai reagir quando você for buscar.

> **Arquivo** — a sua família fez coisas com corpo que nunca foram publicadas. Escreva uma delas. Você cresceu sabendo, ninguém de fora sabe, e alguém lá dentro ainda acha que valeu a pena.
> *Na mesa:* você é o único na equipe que reconhece o método quando ele reaparece. E é o único que tem motivo para esconder que reconheceu.

> **Palavra Dada** — na sua família não se desperdiça palavra, e o meio inteiro sabe disso. Quando você promete alguma coisa, quem é do meio trata como vínculo e cobra, com o peso do seu sobrenome atrás.
> *Na mesa:* faz do personagem a garantia do grupo em qualquer negociação. Cada promessa que ele empenha vira dívida que a mesa vai ter que pagar em cena.

> **Treino de Berço** — o seu clã ensina uma coisa que não se aprende fora dele. Escreva na ficha o que é. Quem quiser aquilo tem que passar pela sua família, ou por você.
> *Na mesa:* é a razão pela qual gente que não gosta de você continua procurando você.

> **Sem Técnica** — você tem energia amaldiçoada e a técnica não veio junto. O texto está adiante, em *Legado de Sem Técnica*. Um Descendente Sem Técnica é alguém com nome de peso e nenhuma técnica de clã.

#### Ajusta

**Ajusta do Descendente**
| Legado | Alcança | Relógio |
|---|---|---|
| Conversa de Jantar | técnica de clã (1) | por cena |
| Etiqueta | uma situação nomeada (1) | por cena |
| Repetição | um Teste de Resistência nomeado (1) | por cena |
| Biblioteca | duas perícias (2) | por cena |

> **Conversa de Jantar** — uma vez por cena, contra uma técnica de clã, você sabe o que vem: vantagem no Teste de Resistência contra ela. Você cresceu ouvindo falar dessas técnicas à mesa, com nome e com defeito.
> *Na mesa:* brilha quando o antagonista é do meio, e é justamente aí que a campanha costuma doer mais.

> **Etiqueta** — uma vez por cena, refaça um teste social que você falhou diante de alguém de patente ou clã superior ao seu. Você foi treinado para essa sala desde criança.
> *Na mesa:* audiência, tribunal interno, jantar de família, reunião de clã. A cena em que a equipe inteira depende de uma frase sua.

> **Repetição** — na criação, escolha um Teste de Resistência: é contra aquilo que a sua família te drilou, todo dia, por anos. Uma vez por cena, role-o com vantagem.
> *Na mesa:* declara na ficha, desde a criação, contra o que a sua casa tinha medo. Isso já é ficção pronta para o mestre usar.

> **Biblioteca** — uma vez por cena, refaça um teste de História ou Ocultismo que você falhou. A sua casa tinha os livros, e você foi obrigado a ler.
> *Na mesa:* segura a cena de pesquisa, que é onde a campanha costuma parar por causa de um dado ruim.

#### Desliga

**Desliga do Descendente**
| Legado | Apaga | Relógio |
|---|---|---|
| Coleira | ser localizado ou rastreado | sempre |
| Cabo | ficar `Desarmado` | por cena |

> **Coleira** — o seu clã te selou na infância: técnica nenhuma te localiza, te rastreia ou te encontra à distância. Em troca, o selo é dos dois lados: a sua família sempre sabe onde você está, e nunca precisou perguntar.
> *Na mesa:* o grupo pode se esconder do inimigo inteiro por sua causa, e nunca da sua casa. Toda fuga tem uma testemunha garantida.

> **Cabo** — a sua mão conhece o cabo antes de a cabeça mandar: uma vez por cena, você não fica `Desarmado`, e a ferramenta escorrega e volta. Em troca, você não larga ela quando devia: quem revista acha, quem te vê armado te trata como armado, e você não atravessa lugar nenhum como civil.
> *Na mesa:* a peça do clã não sai da sua mão, e nenhuma porta que peça gente desarmada se abre para você.

## Reencarnado

*Você já foi outra pessoa, e o corpo em que você está não nasceu seu.*

Alguém te selou, te guardou e te trouxe de volta, ou você aceitou ser guardado. Você acordou num corpo preparado, e quem estava nele antes não está mais. Entre uma coisa e outra pode ter passado um século ou mil anos, e o mundo mudou de idioma, de moeda e de mapa no meio do caminho.

Quase tudo o que você sabe está desatualizado. Você erra o nome dos clãs que mandam hoje, não reconhece metade da tecnologia que as pessoas usam para tarefas triviais, e leva um tempo até entender que a instituição virou burocracia. Em compensação, você sabe coisa que ninguém vivo sabe: onde as coisas estavam, quem fez o quê, como se fazia antes de alguém simplificar o método. E tem o detalhe de que o corpo em que você acordou teve uma vida, com endereço, documento e gente esperando na porta.

A instituição não tem casinha para você. Reencarnado entra na papelada como incidente, e o registro do corpo continua dizendo outro nome. Quem descobre o que você é costuma descobrir por acidente, e reagir rápido: a leitura padrão do meio é que corpo ocupado por consciência antiga é obra de alguém, e alguém que faz isso está fazendo por algum motivo. O tipo de pessoa que aceita voltar é gente que deixou assunto aberto, ou gente que nunca teve o que fazer com paz.

> **A diferença para Receptáculo.** Receptáculo é simbiose: os dois estão lá. Reencarnado é sobrescrita: sobrou um.

**Na obra:** o Kashimo, feiticeiro de quatrocentos anos atrás que aceitou virar objeto amaldiçoado e encarnar num corpo que o Kenjaku preparou, com a condição de poder enfrentar o Sukuna.

### Efeito na ficha

#### Perícias

Escolha uma: História · Ocultismo · Investigação · Intimidação

#### Traços

- o motivo pelo qual você aceitou voltar
- alguém que te reconheceu de antes
- a família do corpo que você está usando

#### Criação

Fundamento, do jeito padrão.

### Legados do Reencarnado

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca do Reencarnado**
| Legado | Relógio |
|---|---|
| O Que Ninguém Lembra | por descanso longo |
| Encomenda | sem relógio |
| Quem Morava Aqui | sem relógio |
| Enterrado | sem relógio |
| Sem Técnica → ver *Sem Técnica* | sem relógio |

> **O Que Ninguém Lembra** — uma vez por descanso longo, você sabe um lugar, um nome ou uma técnica de antes do seu tempo, e isso responde uma dúvida que ninguém vivo responderia.
> *Na mesa:* é a chave que destrava investigação parada. O mestre entrega um fato que ele estava guardando, e a sessão anda.

> **Encomenda** — alguém pagou para você voltar. Escreva quem foi e qual era a condição do acordo. Essa pessoa está viva, considera o acordo aberto, e o que ela acha que comprou não é necessariamente o que você acha que vendeu.
> *Na mesa:* dá ao mestre um credor que pode aparecer em qualquer sessão cobrando, e um motivo pronto para a campanha ir aonde ele quiser.

> **Quem Morava Aqui** — este corpo teve uma vida. Escreva de quem ele era, e uma pessoa que ainda está esperando essa pessoa voltar. Ela não sabe que é você quem está aqui agora. Ela continua esperando, e continua procurando.
> *Na mesa:* uma cena de reencontro que o jogador vai adiar o máximo que puder, e que o mestre pode marcar quando quiser.

> **Enterrado** — você guardou uma coisa antes de morrer, e nunca voltou para buscar. Escreva o que é e onde está. Continua lá, se o lugar ainda existir. Faz tempo demais para alguém ter tido motivo de mexer.
> *Na mesa:* põe no mapa um ponto que só você conhece, e um lugar que mudou de dono várias vezes desde então.

> **Sem Técnica** — você tem energia amaldiçoada e a técnica não veio junto. O texto está adiante, em *Legado de Sem Técnica*.

#### Ajusta

**Ajusta do Reencarnado**
| Legado | Alcança | Relógio |
|---|---|---|
| Corpo Emprestado | uma condição nomeada (1) | por cena |
| Espasmo | dois Testes de Resistência nomeados (2) | por cena |
| Já Morri | uma condição nomeada (1) | por cena |
| Método Velho | uma situação nomeada (1) | por cena |

> **Corpo Emprestado** — dor não te para como para os outros: uma vez por cena, role com vantagem o Teste de Resistência contra ficar `Incapacitado` (condição). O corpo avisa os outros e não avisa você.
> *Na mesa:* é o personagem que continua de pé na cena em que devia cair, e que só descobre o tamanho do estrago depois.

> **Espasmo** — uma vez por cena, refaça um Teste de Resistência Físico ou de Vigor que você já tenha falhado. O corpo fez uma coisa que você não mandou, e quem estava aqui antes ainda está nos músculos.
> *Na mesa:* boa desculpa para o mestre descrever o corpo agindo sozinho, na frente de quem conhecia o antigo dono.

> **Já Morri** — uma vez por cena, role com vantagem o Teste de Resistência contra ficar `Amedrontado` (condição). Você já esteve do outro lado e não achou grande coisa. Não mede risco como quem tem uma vida só.
> *Na mesa:* aparece contra maldição de terror e contra intimidação em cena social. Você é quem entra na sala que o resto do grupo evita.

> **Método Velho** — uma vez por cena, um teste que envolva método antigo (ritual, selo, barreira velha, escrita morta) sai como se você fosse treinado nele. Era assim que se fazia no seu tempo.
> *Na mesa:* ruína, templo lacrado, documento em língua morta, barreira que ninguém abre há gerações. Você é o único que sabe por onde começar.

#### Desliga

**Desliga do Reencarnado**
| Legado | Apaga | Relógio |
|---|---|---|
| Usado | ficar `Derrubado` | por cena |
| *vaga reservada* | objeto amaldiçoado, em desenvolvimento | — |

> **Usado** — este corpo já esteve em estado muito pior que este, e levantou: uma vez por cena, você não fica `Derrubado`. Em troca, ele cobra depois — o mestre diz uma coisa pequena que o seu corpo passa a fazer errado até o fim da cena, e ela é sua e não dele.
> *Na mesa:* você levanta na rodada em que o grupo precisava que alguém levantasse, e sai da cena devendo alguma coisa que o mestre escolhe.

## Feto

*Alguém te fez, peça por peça.*

Meio humano, meio maldição, e as duas metades são de verdade. Nem todo Feto é Pintura da Morte, mas todo Feto é cria artificial de alguém que estava tentando alguma coisa. Existe um método, existe uma anotação em algum lugar dizendo o que deu certo e o que não deu, e existe uma numeração que veio antes do seu nome.

O corpo funciona com regra própria. Envelhece em outro calendário, aguenta coisa que humano não aguenta, e falha em coisa que humano nem repara que está fazendo. Você pode ter passado décadas guardado antes de alguém decidir que estava na hora de você acordar, e esse tempo conta na sua cabeça mesmo sem ter contado no seu rosto. Você reconhece parente pelo que ele é, e não pelo que ele parece.

Para a instituição você é, no papel, uma maldição com nome. Tem gente que assinaria a sua execução sem ler o resto da pasta, e tem gente do departamento técnico que quer te estudar por um motivo que não é carinho. Entre os dois grupos sobra um espaço estreito de gente que trabalha contigo porque você é bom no serviço, e essa é a rede de contato que um Feto costuma ter: pequena, prática e sem ilusão.

**Na obra:** o Choso e os irmãos, ventres de Pintura da Morte, metade humano e metade maldição.

### Efeito na ficha

#### Perícias

Escolha uma: Ocultismo · Medicina · Sentir Energia · Natureza

#### Traços

- os irmãos, e o que aconteceu com eles
- quem te fez, e onde essa pessoa está
- o corpo que não envelhece igual

#### Criação

Fundamento, do jeito padrão.

### Legados do Feto

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca do Feto**
| Legado | Relógio |
|---|---|
| Irmãos | sem relógio |
| Numeração | sem relógio |
| Guardado | sem relógio |
| Devagar | sem relógio |
| Sem Técnica → ver *Sem Técnica* | sem relógio |

> **Irmãos** — escreva quantos vocês eram e o que aconteceu com eles. Você reconhece um irmão quando encontra, e sabe quando um morre, esteja onde estiver. Nem todos se parecem com você: quem te fez fez outras coisas, em outros lugares, e algumas delas nasceram de gente.
> *Na mesa:* o mestre ganha um alarme que ele pode tocar a qualquer momento, no meio de qualquer cena, e que muda tudo o que o personagem ia fazer naquela sessão.

> **Numeração** — você é um número dentro do que alguém estava tentando. Escreva qual é o seu e quantos eram no total. Quem sabe do assunto reconhece a série.
> *Na mesa:* transforma qualquer documento antigo em pista. Basta o número aparecer numa lista para a cena passar a ser sobre você.

> **Guardado** — antes de acordar você foi coisa, e alguém te teve. Escreva quem te guardou, onde, e por quanto tempo. Essa pessoa, ou o que sobrou dela, ainda tem a ver com você.
> *Na mesa:* põe um lugar concreto no mapa e um dono para ele. Voltar lá é sempre uma decisão pesada, e por isso rende.

> **Devagar** — o seu corpo não envelhece no calendário dos outros. Escreva há quanto tempo você existe e com que idade você parece. Quem te conheceu antes vai notar; você não.
> *Na mesa:* abre a campanha para o passado. Gente que te conheceu há trinta anos está viva, velha, e vai reagir ao te ver igual.

> **Sem Técnica** — você tem energia amaldiçoada e a técnica não veio junto. O texto está adiante, em *Legado de Sem Técnica*.

#### Ajusta

**Ajusta do Feto**
| Legado | Alcança | Relógio |
|---|---|---|
| Meio e Meio | veneno e doença (1) | por cena |
| Como Se Monta | Medicina (1) | por cena |
| Faro | maldição (1) | por cena |
| Paciência | qualquer perícia | por dia |

> **Meio e Meio** — uma vez por cena, role com vantagem um Teste de Resistência contra veneno ou doença. Metade de você não é feita de carne, e essa metade não escuta.
> *Na mesa:* você é quem entra no lugar contaminado, prova o que ninguém prova e segura a maldição que trabalha por apodrecimento.

> **Como Se Monta** — uma vez por cena, refaça um teste de Medicina que você falhou. Você sabe do que corpo é feito porque alguém montou o seu na sua frente.
> *Na mesa:* estabilizar companheiro caído, ler cadáver, entender o que uma técnica fez com o corpo da vítima.

> **Faro** — uma vez por cena, quando o que você procura é maldição, role Sentir Energia no lugar de Investigação. Você sente onde ela está, porque é parente.
> *Na mesa:* corta a busca por prédio, por bairro ou por escombro, e devolve a cena para a parte em que a coisa aparece.

> **Paciência** — uma vez por dia, refaça um teste de perícia feito enquanto você esperava, vigiava ou estava escondido sem se mexer. Você já passou mais tempo parado do que a maior parte das pessoas passa viva.
> *Na mesa:* recompensa o plano de tocaia. O grupo pode escolher esperar sabendo que você aguenta a espera melhor do que o alvo.

#### Desliga

**Desliga do Feto**
| Legado | Apaga | Relógio |
|---|---|---|
| Sangue que Não é Sangue | comer, dormir, respirar | sempre |
| Talhe | ficar `Agarrado` | por cena |

> **Sangue que Não é Sangue** — você não precisa comer, dormir nem respirar como um humano. Isso resolve problemas que param os outros. Em troca, cria problemas que os outros não têm, e nenhum deles tem nome ainda, porque ninguém precisou nomear fome para gente que come.
> *Na mesa:* água funda, gás, soterramento, vigília de vários dias. E a cena em que o grupo senta para comer e você fica olhando.

> **Talhe** — você foi guardado antes de andar, e o corpo aprendeu a sair: uma vez por cena, você não fica `Agarrado`. Em troca, você sai por onde couber — quem te agarrou escolhe se você larga uma coisa que estava na sua mão ou termina o movimento fora da posição em que queria estar.
> *Na mesa:* nenhum agarrão prende você duas vezes na mesma cena, e sair sempre custa a sua arma ou o seu lugar.

## Sem Técnica

*Você tem energia amaldiçoada e não tem técnica inata.*

É mais comum do que a ficção faz parecer. A maior parte da gente que trabalha no meio jujutsu está nessa situação, e a estrutura inteira depende dessas pessoas: quem levanta véu, quem faz varredura de bairro, quem escolta, quem cura, quem sustenta a escola de pé enquanto os nomes grandes viajam.

O meio te trata de acordo. Ninguém te chama para a missão que precisa de uma técnica específica; te chamam para as outras noventa. Isso significa carga de trabalho e pouca vitrine, e significa também que você aprende o ofício de verdade, porque o serviço nunca para. Quem vem de clã e nasce Sem Técnica costuma carregar uma vergonha que a família não deixa esquecer. Quem vem de fora costuma nem saber que devia estar constrangido, e trabalha melhor por isso.

Sem Técnica se soma a uma das cinco Origens principais. Você continua sendo Latente, Receptáculo, Descendente, Reencarnado ou Feto, com a marca de que a técnica não veio junto. Na obra isso é a Miwa: nome de peso, nenhuma técnica de clã.

O poder vem de dois lugares.

**Aptidão.** Você foi fundo no que todo feiticeiro pode fazer, em vez de ter uma coisa que só você faz. É a Shoko Ieiri, cuja Energia Reversa vale mais do que a maior parte das técnicas.

**Estilo da Sombra.** Você aprendeu a matar maldição com técnica de espada e de corpo, sem precisar de técnica amaldiçoada. É a Miwa e o Kusakabe.

### Efeito na ficha

Você não escreve Fundamento. Não tem Regra, não tem Famílias, não tem Selo, não tem feitiço. A Origem principal continua dando tudo o que dá.

#### Criação

Aptidão ou Estilo da Sombra.

> **Sem Técnica não fecha ficha hoje.** O que já dá para fazer é a ficção inteira: você escreve quem o personagem é e escolhe os dois Legados normalmente. O que falta é a montagem do poder — nem a Aptidão nem o Estilo da Sombra têm regra de construção, e sem ela a ficha para no meio.

### Legado de Sem Técnica

Sem Técnica não amplia a conta de Legados. Ela é uma entrada de `Destranca` e ocupa uma das duas vagas, como qualquer outra. Cinco Origens compartilham esta entrada em vez de cada uma repetir o texto na própria lista: Latente, Receptáculo, Descendente, Reencarnado e Feto.

> **Sem Técnica** — você tem energia amaldiçoada, e a técnica não veio junto: é outro caminho de poder. O seu poder não sai do Fundamento. Ele sai de aptidão ou de escola de espada, e é lá que você monta o personagem.

Corpo Amaldiçoado e Restrição Celestial não aceitam Sem Técnica. As duas já vêm com uma troca própria embutida no lugar da técnica.

## Corpo Amaldiçoado

*Alguém te fez, e você acordou.*

Cadáver Amaldiçoado de Mutação Abrupta, na linguagem da instituição. Você tem consciência e vontade própria. Técnica amaldiçoada e corpo humano você não tem, e ninguém sabe explicar direito por que a consciência apareceu: o método conhecido produz coisas que obedecem, e você faz perguntas.

Quem te fez trabalhou com núcleos, e o arranjo deles é o que te decidiu. Três num corpo só é o jeito que funciona, porque três se equilibram e se vigiam. Dois brigam. Um não devia acordar. O que existe dentro de você conversa entre si de um jeito que você mesmo tem dificuldade de descrever para outra pessoa, e as pessoas perguntam.

O meio jujutsu não sabe onde te colocar, e resolve isso de vários jeitos ruins. No papel você pode ser equipamento, aluno, prova de conceito ou pendência administrativa, dependendo de quem preencheu a ficha. Tem gente que fala de você em terceira pessoa na sua frente. Tem gente que te trata melhor do que trata os colegas humanos, e isso também é um jeito de dizer que você é exceção. Quem te fez tem opinião sobre tudo isso e quase nunca é chamado a dar.

**Na obra:** o Panda, feito pelo Yaga, com três núcleos que ele troca à vontade: o de gorila, o de panda e o de tricerátops.

### Efeito na ficha

Sem Fundamento, porque não existe técnica inata para escrever. Você tem energia amaldiçoada: cadáver de mutação abrupta produz a própria, uns três meses depois de acordar. Então PE, aptidões e refino são normais, com Técnica Marcial no lugar do Fundamento.

#### Perícias

Escolha uma: Atletismo · Percepção · Ocultismo · Intimidação

#### Traços

- quem te fez, e o que essa pessoa esperava
- o que as pessoas acham que você é
- o núcleo que você ainda não usou na frente de ninguém

#### Criação

Técnica Marcial, no capítulo 10.

Você tem energia amaldiçoada, então tem PE, aptidões e refino como qualquer feiticeiro tem — inclusive `canalizar energia`, que faz o seu golpe simples ferir maldição. O que você não tem é técnica inata para escrever, e é a Técnica Marcial que ocupa esse lugar.

### Legados do Corpo Amaldiçoado

#### Destranca

*Escolha um destes, obrigatoriamente. A configuração que você escolhe aqui decide qual das quatro listas de Ajusta abaixo você alcança.*

**Destranca do Corpo Amaldiçoado**
| Legado | Relógio |
|---|---|
| Ninhada | sem relógio |
| Gêmeos | sem relógio |
| Inteiro | sem relógio |
| Manutenção | sem relógio |

> **Ninhada** — três seres num corpo só, obrigados a se olharem. É o método que funciona, e funcionou em você. Escreva o que são os três.
> *Na mesa:* o jogador ganha três vozes para interpretar, e o mestre ganha três opiniões para consultar quando o grupo pedir conselho.

> **Gêmeos** — foram dois, e dois não estabilizam. Vocês se revezam, e nenhum dos dois manda na hora da troca.
> *Na mesa:* a troca acontece na hora errada, e é o mestre quem escolhe a hora. Vale combinar antes o que muda de uma para a outra.

> **Inteiro** — um núcleo só, e mesmo assim você acordou. Pelo método conhecido isso não acontece.
> *Na mesa:* você é a anomalia que os pesquisadores do meio querem abrir. Alguém está escrevendo sobre você agora.

> **Manutenção** — a consciência é sua; a energia é de quem te fez, e ela acaba. Escreva quem te abastece e o que ela cobra. Você decide quando ir.
> *Na mesa:* põe um relógio na campanha inteira e uma pessoa a quem o grupo vai ter que voltar, gostando ou não.

#### Ajusta

*Três por configuração; você só alcança os da sua.*

##### Ninhada

**Ninhada**
| Legado | Alcança | Relógio |
|---|---|---|
| Rodízio | três perícias nomeadas (3) | por cena |
| Vigília | Iniciativa (1) | por cena |
| Desempate | qualquer Teste de Resistência (4) | por dia |

> **Rodízio** — escolha três perícias na criação, uma por ser. Uma vez por cena, role uma delas como se fosse treinada. Cada um sabia fazer uma coisa, e vocês três continuam sabendo.
> *Na mesa:* cobre três buracos diferentes da equipe, um de cada vez, e dá nome a quem resolveu cada um.

> **Vigília** — uma vez por cena, role Iniciativa com vantagem. Nunca estão os três dormindo ao mesmo tempo.
> *Na mesa:* emboscada contra o grupo deixa de ser emboscada contra você. É você quem abre a rodada.

> **Desempate** — uma vez por dia, refaça um Teste de Resistência que você falhou. Dois cederam e o terceiro não, e é o terceiro que decide.
> *Na mesa:* uso único e largo. Segure para o efeito que tiraria o personagem da cena de vez.

##### Gêmeos

**Gêmeos**
| Legado | Alcança | Relógio |
|---|---|---|
| Cabeça Trocada | uma perícia nomeada (1) | por cena |
| Nunca os Dois | Teste de Resistência de Intelecto (1) | por cena |
| Palpite | qualquer perícia não treinada | por dia |

> **Cabeça Trocada** — escolha uma perícia e um atributo na criação: é o jeito que a outra faz aquilo. Uma vez por cena, role essa perícia com esse atributo em vez do que ela pede.
> *Na mesa:* é o momento em que a outra assume para fazer do jeito dela, na frente de quem está junto.

> **Nunca os Dois** — uma vez por cena, refaça um Teste de Resistência de Intelecto que você falhou. Enquanto uma cede, a outra ainda está lá.
> *Na mesa:* contra ilusão, leitura de mente e maldição que trabalha convencendo. Você é o alvo ruim para esse tipo de inimigo.

> **Palpite** — uma vez por dia, role com vantagem um teste de perícia em que você não é treinado. Ela chuta, e ela chuta bem: você descobre junto com todo mundo.
> *Na mesa:* resolve a perícia que ninguém da equipe tem, e rende a cena de todo mundo se virando para olhar.

##### Inteiro

**Inteiro**
| Legado | Alcança | Relógio |
|---|---|---|
| Feito de Uma Peça | Teste de Resistência de Vigor (1) | por cena |
| Teimosia | uma situação nomeada (1) | por cena |
| Peça Única | uma perícia nomeada (1) | por cena |

> **Feito de Uma Peça** — uma vez por cena, refaça um Teste de Resistência de Vigor que você falhou. Não existe parte sua que ceda antes das outras.
> *Na mesa:* desgaste longo, fogo, frio, esforço que não acaba. Você é quem sustenta enquanto o resto do grupo trabalha.

> **Teimosia** — uma vez por cena, refaça um teste para continuar fazendo uma coisa que você já começou (segurar, agarrar, sustentar, não largar). Ninguém aí dentro discorda de você no meio.
> *Na mesa:* segurar a porta, prender o inimigo no lugar, não soltar quem está caindo. É o Legado da cena em que a equipe depende de você não largar.

> **Peça Única** — escolha uma perícia treinada na criação. Uma vez por cena, role com vantagem. Você faz uma coisa, e faz bem.
> *Na mesa:* declara desde a criação para que serve o personagem, e o grupo pode contar com isso toda cena.

##### Manutenção

**Manutenção**
| Legado | Alcança | Relógio |
|---|---|---|
| Ajuste Fino | um ofício nomeado (1) | por cena |
| Recarga | duas perícias nomeadas (2) | por descanso curto |
| Fiado | qualquer rolagem | por dia |

> **Ajuste Fino** — escolha um ofício na criação: é o de quem te fez, e você viu por dentro como se faz. Uma vez por cena, role com vantagem.
> *Na mesa:* você é a oficina ambulante da equipe naquele ofício, e cada uso lembra de quem você aprendeu.

> **Recarga** — escolha duas perícias na criação: são as que ela calibrou em você. Uma vez por descanso curto, role uma delas com vantagem.
> *Na mesa:* o relógio mais rápido da Origem. Rende em sessão de missão longa, com paradas curtas entre confrontos.

> **Fiado** — uma vez por dia, refaça qualquer rolagem que você falhou: ela cobre a diferença de onde estiver. Escreva na ficha o que você passou a dever, e isso não sai no descanso.
> *Na mesa:* o grupo vê a dívida crescer sessão a sessão, e uma hora alguém vem cobrar. Essa hora é cena.

#### Desliga

**Desliga do Corpo Amaldiçoado**
| Legado | Apaga | Relógio |
|---|---|---|
| Ferro Velho | os degraus de exaustão | sempre |
| *vaga reservada* | alvo ainda não escolhido | — |

> **Ferro Velho** — os degraus de exaustão não te alcançam. Você dorme só porque combinaram que era hora. Em troca, você também não sente quando está perto de quebrar: o seu corpo para de uma vez, sem aviso antes.
> *Na mesa:* apaga a conta de descanso do grupo inteiro quando é você quem faz o turno. E entrega ao mestre o direito de te derrubar do nada.

## Restrição Celestial

*Você trocou uma coisa por outra antes de nascer, e não foi você que assinou.*

A troca é sempre desproporcional para os dois lados: você perde muito e ganha muito. Ninguém negociou, ninguém consultou, e não existe registro de quem cobrou. O meio jujutsu conhece o fenômeno há séculos, tem nome para ele e nunca conseguiu explicar por que acontece com quem acontece.

São dois ramos opostos, e você escolhe um na criação.

**Corpo pela técnica.** O corpo não funciona, e em troca a energia é enorme. É o Kokichi Muta: pele que não aguenta sol, membros que faltam, dor constante, e energia suficiente para operar cadáveres amaldiçoados a uma distância absurda. Ele pilota o Mechamaru de casa. O boneco vai à escola; a Origem descreve quem ficou.

**Sem energia.** Você nasceu sem energia amaldiçoada, nenhuma, e em troca o corpo recebeu a troca. É a Maki e o Toji. Você não conjura, não canaliza e não sente energia. Fere maldição com ferramenta amaldiçoada, e enxerga o mundo jujutsu de fora. O que a Origem fixa é a perda, e não o que você constrói em cima dela: um restringido que nunca levantou peso e resolve tudo pela cabeça é uma ficha tão legítima quanto o Toji.

Os clãs tratam os dois ramos como defeito de nascença, e tratam pior o segundo. Uma criança que nasce sem energia dentro de uma família do meio cresce sendo tratada como erro de produção, e o meio inteiro aceita isso com naturalidade. A instituição, por sua vez, é pragmática: gente com Restrição Celestial costuma render mais que a média, e a papelada acompanha o rendimento. Você vai ser útil, vai ser exibido, e vai ouvir a mesma frase sobre o seu corpo a vida inteira, dita por gente que acha que está sendo gentil.

### Efeito na ficha

**Ramos da Restrição Celestial**
| Ramo | O que muda | Criação |
|---|---|---|
| **Corpo pela técnica** | Fundamento normal, corpo com limitação escrita na ficha | Fundamento, no capítulo 9 |
| **Sem energia** | sem Fundamento, sem feitiço de Toque, sem Sentir Energia, sem aptidão e sem refino. No lugar deles, **Bênçãos e Lapidação**, e acesso a ferramenta amaldiçoada como eixo de poder | Técnica Marcial, no capítulo 10, com o capítulo 12 no lugar do 11 |

O `PE` do seu Caminho continua chegando. Nesta rota ele se lê **Pontos de Esforço** em vez de Pontos de Energia: é a mesma sigla, o mesmo número e a mesma coluna, e nenhuma regra do livro pergunta qual das duas você tem.

#### Perícias

A lista sai por ramo, e é a única Origem assim.

**Perícias por ramo**
| Ramo | Escolha uma |
|---|---|
| **Corpo pela técnica** | Sentir Energia · Tecnologia · Ocultismo · Percepção |
| **Sem energia** | Atletismo · Acrobacia · Furtividade · Pontaria |

Quem é do ramo sem energia não alcança `Sentir Energia` por lugar nenhum: ela é perícia de Essência, e essa é a percepção que a Origem não tem.

#### Traços

- o clã que te descartou
- a pessoa que te olha e vê o que você perdeu
- a ferramenta que te acompanha desde criança

### Legados: Corpo pela Técnica

*O corpo não funciona, e a energia é enorme. Você conjura pelo Fundamento normal, como qualquer feiticeiro.*

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca · Corpo pela Técnica**
| Legado | O que ele desenha | Relógio |
|---|---|---|
| Nasci Assim | o que o seu corpo não faz, e o que isso cobra todo dia | sem relógio |
| O Substituto | as pessoas conhecem uma coisa que não é você | sem relógio |
| A Oferta | você já pensou no preço de um corpo que funcione | sem relógio |
| Nunca Estive Lá | você conhece lugares onde o seu corpo nunca esteve | sem relógio |

> **Nasci Assim** — escreva o que o seu corpo não faz, e o que isso te cobra todo dia: o que dói, o que falta, o que você não pode encarar. Não é segredo, e não tem conserto conhecido.
> *Na mesa:* dá ao mestre uma lista pronta de coisas que complicam qualquer cena, e ao jogador o direito de dizer quando complicam.

> **O Substituto** — o meio jujutsu conhece você por uma coisa que não é o seu corpo: um nome, uma voz, uma casca. Escreva o que é. Quase ninguém sabe que existe outra pessoa do outro lado, e quem sabe conta nos dedos.
> *Na mesa:* o personagem pode estar em duas cenas ao mesmo tempo, e a revelação de quem está do outro lado é um marco de campanha inteiro.

> **A Oferta** — você já pensou no que daria por um corpo que funcione, e já chegou a um número. Escreva qual é. Existe gente que vende esse tipo de coisa, e uma delas sabe que você existe.
> *Na mesa:* é um antagonista com proposta, e a proposta é boa. O mestre pode voltar com ela toda vez que o preço ficar mais fácil de pagar.

> **Nunca Estive Lá** — a sua energia vai a lugares que você não vai. Escreva um lugar que você conhece de cor e onde o seu corpo nunca pisou, e o que você viu acontecer lá.
> *Na mesa:* você é a planta baixa da equipe. Descreve o lugar antes de todo mundo chegar, e sabe o que aconteceu lá dentro.

#### Ajusta

**Ajusta · Corpo pela Técnica**
| Legado | Alcança | Relógio |
|---|---|---|
| Antena | Sentir Energia (1) | por cena |
| Do Meu Canto | uma situação nomeada (1) | por cena |
| Insônia | qualquer perícia | por dia |
| Li Tudo | duas perícias nomeadas (2) | por cena |

> **Antena** — uma vez por cena, refaça um teste de Sentir Energia que você falhou. O seu alcance não é normal, e você passou a vida usando ele no lugar dos olhos.
> *Na mesa:* varredura de área, detecção de emboscada, contagem de quantos são do outro lado da parede.

> **Do Meu Canto** — uma vez por cena, role com vantagem um teste feito sem sair do lugar em que você está. Você nunca precisou chegar perto para trabalhar.
> *Na mesa:* recompensa a posição fixa. O personagem escolhe o canto no começo da cena e trabalha a cena inteira de lá.

> **Insônia** — uma vez por dia, refaça um teste de perícia feito enquanto os outros dormiam. Dor não tem horário, e você aproveitou as horas.
> *Na mesa:* a cena de madrugada, com o grupo dormindo, é sua. Pesquisa, vigília, conversa com quem também não dorme.

> **Li Tudo** — uma vez por cena, refaça um teste de Ocultismo ou Investigação que você falhou. Você teve tempo parado que ninguém mais teve.
> *Na mesa:* segura a investigação quando o dado trava, que é onde a sessão costuma morrer.

### Legados: Sem Energia

*Sem energia nenhuma, e o corpo recebeu a troca. Você não tem feitiço de Toque nem Sentir Energia: o seu poder vem da Técnica Marcial, e o seu eixo de controle são as Bênçãos.*

#### Destranca

*Escolha um destes, obrigatoriamente.*

**Destranca · Sem Energia**
| Legado | O que ele desenha | Relógio |
|---|---|---|
| Descartado | o clã que te jogou fora | sem relógio |
| Dividido | a sua restrição foi partida com outra pessoa | sem relógio |
| Desde Criança | a ferramenta que te acompanha desde sempre | sem relógio |
| Aprendi a Ver | você não nasceu enxergando maldição | sem relógio |

> **Descartado** — a sua família é do meio e te tratou como erro. Escreva quem te descartou e o que fizeram você fazer enquanto esteve lá. Eles continuam existindo, continuam achando que estavam certos, e você conhece a casa por dentro.
> *Na mesa:* você é o mapa da casa do inimigo, e a única pessoa da equipe que sabe por onde se entra sem bater.

> **Dividido** — a sua restrição foi partida com alguém que nasceu junto de você. Escreva quem é e onde essa pessoa está. Enquanto os dois lados existirem, nenhum dos dois está inteiro.
> *Na mesa:* entrega um NPC que a campanha vai perseguir, evitar ou enfrentar, e cuja existência mexe com o que o personagem é.

> **Desde Criança** — existe uma ferramenta que anda com você desde antes de você escolher. Escreva o que é e como veio parar na sua mão. Quem entende de ferramenta reconhece aquela.
> *Na mesa:* a peça tem história e tem quem a reconheça. Perder essa ferramenta é cena, e recuperá-la é arco.

> **Aprendi a Ver** — você não nasceu enxergando maldição, e a maior parte de quem te olha supõe que sim. Escreva como você resolveu isso: o que você usa, ou o que você treinou até substituir o que falta.
> *Na mesa:* dá um método visível na ficha, com limite próprio, que o mestre pode atrapalhar em cena para complicar uma missão inteira.

#### Ajusta

**Ajusta · Sem Energia**
| Legado | Alcança | Relógio |
|---|---|---|
| Sentido Treinado | maldição (1) | por cena |
| Couro | Teste de Resistência Físico (1) | por cena |
| Ninguém Viu | Furtividade (1) | por cena |
| No Braço | qualquer perícia de Força ou Destreza | por dia |

> **Sentido Treinado** — uma vez por cena, role Percepção no lugar de Sentir Energia. Você aprendeu a notar o que a energia mexe, em vez de senti-la direto.
> *Na mesa:* é como o personagem participa da cena de detecção sem ter o sentido que todo mundo ali tem.

> **Couro** — uma vez por cena, refaça um Teste de Resistência Físico que você falhou. O corpo é a única coisa que a troca te deu, e ele é absurdo.
> *Na mesa:* você é quem atravessa o que devia parar a equipe: queda, impacto, escombro, porta.

> **Ninguém Viu** — uma vez por cena, refaça um teste de Furtividade que você falhou. Você não emite nada, e passou a vida aproveitando isso.
> *Na mesa:* nenhum feiticeiro te sente chegar. Em missão de infiltração você entra sozinho e os outros esperam.

> **No Braço** — uma vez por dia, refaça um teste de perícia de Força ou Destreza que você falhou.
> *Na mesa:* a segunda chance na perseguição, na escalada e no agarrão, que é onde este personagem passa a maior parte do tempo.

### Legados: Desliga

*Vale para Corpo pela Técnica e para Sem Energia.*

**Desliga da Restrição Celestial**
| Legado | Apaga | Relógio |
|---|---|---|
| Peso Real | ser enganado por barreira, véu e ferramenta | sempre |
| Assinado | ficar `Cego` | por descanso longo |

> **Peso Real** — você percebe ferramenta amaldiçoada, barreira e véu pelo tato e pelo peso. O que engana feiticeiro não engana você. Em troca, o aviso vem sem nome: você sente que tem alguma coisa ali, e nunca o que é.
> *Na mesa:* você é o detector de armadilha do grupo em terreno preparado, e o que você entrega é um aviso que ninguém sabe interpretar sem investigar.

> **Assinado** — você nunca leu o mundo pela energia, e o resto do corpo cobriu: uma vez por descanso longo, você não fica `Cego`. Em troca, a troca não foi só essa. Escreva na ficha uma coisa comum que você nunca vai conseguir fazer, e ela não volta, em nível nenhum.
> *Na mesa:* a cena de escuro e de clarão não tira você do jogo, e a ficha carrega uma limitação permanente que o mestre pode usar em qualquer outra.

## Rotas de criação

**Rotas de criação**
| Origem | Rota de criação | Jogável hoje |
|---|---|---|
| Latente | Fundamento | **sim** |
| Receptáculo | Fundamento | **sim** |
| Descendente | Fundamento | **sim** |
| Reencarnado | Fundamento | **sim** |
| Feto | Fundamento | **sim** |
| *qualquer uma* **+ Sem Técnica** | Aptidão ou Estilo da Sombra | não: está sendo escrita |
| Corpo Amaldiçoado | Técnica Marcial | **sim** |
| Restrição Celestial · corpo pela técnica | Fundamento | **sim** |
| Restrição Celestial · sem energia | Técnica Marcial | **sim** |

---


# Capítulo 8 · Caminhos e Trilhas

*fonte: `manual/35-caminhos-e-trilhas.md`*

**O Caminho diz o seu lugar na equipe**, e você escolhe ele na criação. A Trilha diz quem você é dentro do Caminho, e ela nasce junto com ele, no nível 2. São cinco Caminhos, três Trilhas em cada um.


## Como ler um Caminho

Cada Caminho entrega quatro degraus, e eles chegam sempre nos mesmos níveis. A Trilha entrega outras quatro coisas, em níveis diferentes: você ganha alguma coisa em quase todo marco da campanha.

**Entregas por nível**
| Nível | O que chega |
|---|---|
| 2 | o primeiro degrau do Caminho, e a primeira entrega da Trilha |
| 7 | degrau de Caminho |
| 11 | entrega de Trilha, e aqui você pode trocar de Trilha |
| 15 | degrau de Caminho |
| 19 | entrega de Trilha, e aqui você pode trocar de Trilha |
| 27 | entrega de Trilha, e aqui você pode trocar de Trilha |
| 30 | degrau de Caminho |

> **Você é sempre exatamente uma Trilha, do nível 2 ao 30.** Nos níveis 11, 19 e 27 você pode trocar a sua por outra do mesmo Caminho, e a troca é total: tudo o que você tinha vira o equivalente da Trilha nova. Não existe acumular duas, e não existe pegar o degrau avançado de uma Trilha sem ter tido a base dela.

**Sem multiclasse.** Um Caminho por personagem.

### Vida e energia

Cada Caminho tem o próprio número de vida por nível e o próprio número de PE por nível, e os dois correm em sentidos contrários: quem tem mais vida por nível tem menos PE por nível.

**Vida e energia por Caminho**
| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| **Vida por nível** | 7 | 5 | 5 | 4 | 4 |
| **PE por nível** | 4 | 5 | 5 | 6 | 6 |

> **O seu PE máximo é o número da tabela vezes o seu nível.** Nenhum atributo entra nessa conta, e não existe valor inicial somado por cima.

### Termos dos degraus

**PE** são pontos de energia, o combustível que paga feitiço. **Maestria** é o número que cresce com o seu nível: `1` no nível 2 e `4` no 30. **Classe** é o tamanho de um feitiço, de `Classe 0` até `Classe 7`. **Vantagem** é jogar dois dados e ficar com o melhor.

E duas coisas que quase todo degrau daqui menciona:

> **Feitiço de Toque** — os dados da Classe, e nada mais. Arma e atributo ficam de fora da conta.
> **Golpe simples** — arma mais Força. É o que você faz quando não canaliza.
> **Um feitiço de Toque por turno.** Ataque extra é sempre golpe simples.

### Treino de arma

**O seu Caminho decide quais armas você pode empunhar.** Treino mora na categoria: treinar uma categoria libera todas as armas dela, e o catálogo inteiro está no capítulo 13, *Equipamento*.

> **Os dois Caminhos de corpo a corpo — Bastião e Vanguarda — treinam as treze categorias.** Qualquer arma do catálogo é deles.
>
> **Os três Caminhos conjuradores — Guia, Emanador e Evocador — treinam Arma de Fogo e Balestra**, que são as duas que se aponta e dispara sem anos de forma.

**Para um conjurador empunhar o resto, a porta é a Trilha.** É o que faz a `Empunhadura` do `Arremate`, no nível 2: ela concede um grupo de arma à sua escolha e ainda troca Força por Inteligência ou Essência naquele grupo. Um Emanador de espadão existe, e paga por isso com a escolha de Trilha.

> **Sem treino, você tem desvantagem na rolagem de ataque com aquela arma**, e sem o requisito de Força dela o seu deslocamento cai 3 metros enquanto você a estiver empunhando. O capítulo 13, *Equipamento*, tem as duas.

### Limites

> **O Caminho mexe em quando, onde e em quem o seu poder acontece.** O tamanho dele é assunto da sua técnica. Nenhum Caminho dá dado de dano, sobe a Classe dos seus feitiços, dá Melhoria de graça, cura, ou desconto de dano em tudo. **Cura é Forma de feitiço**: quem fechou a Família Amparo nunca vai curar, e Caminho nenhum contorna isso.

### Trilhas

**Trilhas**
| Trilha | Caminho | Em uma linha |
|---|---|---|
| `Muro` | Bastião | o corpo que ocupa o espaço |
| `Punho` | Bastião | vários golpes, e cada golpe tira alguém do lugar |
| `Brasa` | Bastião | conjura pequeno e bate na sequência |
| `Estocada` | Vanguarda | conjura de verdade na padrão e ainda bate |
| `Batedor` | Vanguarda | a luta acontece longe: `Yumi`, `Besta` ou `Arma de Fogo` |
| `Executor` | Vanguarda | arma e corpo contra um alvo só |
| `Elo` | Guia | o que outra pessoa fez chega mais longe |
| `Sutura` | Guia | Energia Reversa cedo, e nos outros |
| `Perímetro` | Guia | o chão decide quem pode estar onde |
| `Torrente` | Emanador | mais de um feitiço na rodada, e a energia acaba |
| `Explosivo` | Emanador | um feitiço só, e ele sai maior |
| `Arremate` | Emanador | o feitiço acontece onde a mão chega |
| `Servo` | Evocador | uma invocação, forte |
| `Matilha` | Evocador | cinco corpos fracos |
| `Coro` | Evocador | você e a invocação lutam juntos |

## Bastião

*O corpo é a resposta: aguentar, encarar, prender.*

O Bastião entra primeiro na sala e sai por último. Em campo ele é o corpo que a maldição enxerga: fica na porta, fica na frente do civil, fica entre o time e a coisa. Quem escolhe o Bastião descobriu cedo que aguenta mais pancada que os outros e resolveu fazer disso um trabalho, com ou sem técnica boa para acompanhar.

### Características do Bastião

**Características do Bastião**
| | |
|---|---|
| **Vida por nível** | 7 |
| **PE por nível** | 4 |
| **Atributos naturais** | Força · Constituição |
| **Perícias fixas** | `Atletismo` · `Intimidação` |
| **Perícias à sua escolha** | 4, de qualquer lugar do quadro |
| **Ofícios** | 2, à sua escolha. O Caminho não trava ofício |
| **Teste de Resistência** | 1 treinado, à sua escolha. A sua Origem treina o outro |
| **Treino de arma** | **as treze categorias**: Simples, Marciais e Arma de Fogo |

*Perícia, ofício e Teste de Resistência entram na ficha uma vez, na criação. O quadro completo das vinte e três perícias e dos onze ofícios está no capítulo 3, __Perícias e Ofícios__.*

### Degraus do Bastião

> **Nível 2: `Corpo Duro`.** *Reação.* Ao ser atingido, você reduz o dano em **o seu nível + 1d6**. Isso é o `Absorver`.
> **Você tem usos iguais à sua Constituição, e eles voltam no descanso longo.**
>
> **Nível 7: Ataque extra.** Você ganha **um golpe simples solto por rodada**. Ele não exige a Ação de Atacar: acontece junto do que a sua Ação Padrão fez naquele turno, inclusive quando ela conjurou.
>
> **Nível 15: `Puxar Para Si`.** *Reação.* Quando um inimigo a até 1,5 m ataca **outra pessoa**, o ataque passa a ter **você** como alvo.
> **Gastando `2` PE, você aplica o `Absorver` no mesmo golpe**, sem gastar um uso dele.
>
> **Nível 30: `Segurar`.** *Reação.* Quando alguém ao seu alcance **se move, conjura ou ataca**, você pode tentar `Agarrar` ou `Derrubar` essa pessoa. **A ação dela acontece de qualquer jeito.**
> **Enquanto você tiver alguém agarrado, você se move junto com ela, e o deslocamento dela cai pela metade.**

*O `Corpo Duro` faz o time aceitar que você entre primeiro: a sua Constituição vira quantas vezes por dia o grupo pode errar de leve. O `Puxar Para Si`, no 15, muda o planejamento inteiro da mesa, porque a partir dali os outros podem se expor de propósito sabendo que existe alguém para desmanchar o erro. E o `Segurar` resolve a cena de fuga: informante correndo, maldição tentando trocar de prédio, alvo que ia sumir no meio da multidão.*

### Trilha: Muro

*O espaço em volta de você deixa de ser do inimigo.*

Quem joga de `Muro` planta os dois pés e vira geografia: escolhe um corredor, uma porta, uma linha no chão, e dali em diante o combate acontece nos termos dele. Você chega na cena procurando o ponto certo de parar de andar, e o seu turno rende quando o inimigo desiste de ir aonde queria ir.

> **Nível 2: `Alicerce`.** *Ação bônus.* Você se firma no lugar. **Enquanto o `Alicerce` estiver de pé, o dano de dois tipos à sua escolha cai pela metade contra você, e o seu deslocamento é metade do normal.**
> **Sair dele não custa nada**, e **os tipos se escolhem no fim de cada descanso longo**.
>
> **Nível 11: `Aterro`.** *Sempre ligado, e não depende do `Alicerce`.* O chão a **4,5 m** em volta de você é terreno difícil para inimigos, cada metro custa dois. **E todo deslocamento forçado contra você, seja empurrão, puxão ou arremesso, tem metade da distância.**
>
> **Nível 19: `Escora`.** O `Absorver` do seu Caminho ganha **mais usos, iguais a metade da sua Constituição**, e **qualquer um deles pode ser gasto num aliado que você enxergue a até 9 m.** Continua custando a sua Reação.
>
> **Nível 27: `Cúpula`.** O `Alicerce` passa a segurar **quatro tipos** ao mesmo tempo, você troca os tipos a cada **descanso curto**, e **todo aliado dentro do seu espaço divide um deles com você.** O espaço continua de pé enquanto você estiver caído, agarrado ou apagado.

*Escolher os tipos do `Alicerce` no descanso longo é uma decisão de preparo de missão: se o briefing diz que a maldição queima, você chega com Fogo marcado. A `Cúpula`, no 27, transforma isso em cobertura de grupo, e é o que permite ao time atravessar uma sala que sozinho ninguém atravessaria.*

*Os tipos de dano do `Alicerce` são os do sistema: `Cortante`, `Fogo`, `Psíquico` e assim por diante. A lista completa é do capítulo 4, __Dano, Condições e Cobertura__.*

### Trilha: Punho

*Você bate mais vezes, e cada vez que bate alguém sai do lugar.*

Quem joga de `Punho` briga sem arma no meio, socando até a formação do inimigo desmanchar — o brigão de rua que entrou para a instituição já sabendo apanhar e aprendeu técnica depois, meio de má vontade. Na mesa você olha o mapa antes de olhar a vida do alvo, porque o que decide a rodada é para onde a pessoa voa.

> **Nível 2: `Engate`.** Quando você **acerta** um ataque na sua ação de atacar, você pode dar um golpe desarmado como **ação bônus**.
>
> **Nível 11: `Encontrão`.** Quando você acerta desarmado, **o alvo é empurrado até 3 m na direção que você escolher.** E **uma vez por rodada**, um alvo que você acertou faz um Teste de Resistência de Vigor; se falhar, fica **`Derrubado`** (condição).
>
> **Nível 19: `Tropel`.** Quando o empurrão do nível 11 joga alguém contra outra criatura, **ela também é empurrada.** Cada uma faz um Teste de Resistência de Vigor: **quem passa segura a corrente, e ela para ali.** A distância total nunca passa do deslocamento do primeiro empurrado. *Vale só no empurrão do nível 11.*
>
> **Nível 27: `Arranco`.** Ao usar o `Engate`, você dá um **segundo soco** num alvo adjacente a você ou ao primeiro, **com rolagem própria**. **E se os dois ataques da sua ação de atacar acertaram, o `Engate` é rolado com vantagem.**

*O `Encontrão` e o `Tropel` são a resposta para multidão sem matar ninguém: guarda em fila num corredor, gente empilhada numa saída, humano possuído que o grupo precisa tirar do caminho inteiro. Empurrar alguém para fora de uma sacada, para dentro de água, ou de volta para o lado seguro de uma barreira resolve cena que rolagem de dano nenhuma resolveria.*

### Trilha: Brasa

*O feitiço entra no meio dos socos.*

Quem joga de `Brasa` abre no braço e fecha com energia: o soco é como você chega, e o Classe 0 é o que você faz depois de ter chegado. O que a Trilha acrescenta ao Bastião é alcance — ela pega alvo que está fora do braço, aplica tipo de dano que soco nenhum aplica, e devolve energia quando acerta.

> **Nível 2: `Fagulha`.** Se você usou a ação de atacar neste turno, você pode lançar um feitiço de **Classe 0** como **ação bônus**. **E se algum dos seus socos acertou, esse feitiço é rolado com vantagem**, quando ele for um ataque.
>
> **Nível 11: `Braseiro`.** Quando o seu Classe 0 acerta, você ganha **`2` de energia temporária.** Ela nunca passa de `2` acumulados e some no fim da cena. *Energia temporária gasta como PE, e gasta primeiro.*
>
> **Nível 19: `Labareda`.** O feitiço que você lança na ação bônus **pode ser de Classe 3 em vez de Classe 0**, e **de Classe 4 a partir do nível 21**, quando a `Classe 6` libera. A Classe dos seus feitiços continua a mesma, e a sua Classe máxima também; o que muda é qual feitiço cabe na ação bônus.
> **Duas condições, e as duas valem em todo turno:** você **abre mão do ataque extra** naquela ação de atacar, e **pelo menos um dos seus socos daquela ação tem de ter acertado.** *Se nenhum acertou, você não lança nada na ação bônus naquele turno, nem o feitiço maior, nem o Classe 0 do nível 2.*
>
> **Nível 27: `Fornalha`.** *Ação bônus para entrar. Dura até o fim da cena.* **Cada ataque seu carrega um feitiço de Classe 0 junto, e cada ataque tem de ser num alvo diferente.** E a sua **ação bônus deixa de lançar feitiço e vira um soco a mais**, num terceiro alvo. **São três socos, três alvos, três Classe 0.**


## Vanguarda

*A arma é a resposta: alcançar, cortar, acabar.*

A Vanguarda encosta a lâmina onde ela precisa encostar, e chega lá antes do resto. Em campo ela é quem entra no alcance do inimigo e fica lá: corta, reposiciona, corta de novo. Ela treinou arma como quem treina técnica — anos numa categoria só, com professor, com forma, com linhagem —, e a energia amaldiçoada dela existe e é usada, só que ela não é o motivo de a Vanguarda estar na sala.

### Características da Vanguarda

**Características da Vanguarda**
| | |
|---|---|
| **Vida por nível** | 5 |
| **PE por nível** | 5 |
| **Atributos naturais** | Destreza · Força |
| **Perícias fixas** | `Acrobacia` · `Percepção` |
| **Perícias à sua escolha** | 4, de qualquer lugar do quadro |
| **Ofícios** | 2, à sua escolha. O Caminho não trava ofício |
| **Teste de Resistência** | 1 treinado, à sua escolha. A sua Origem treina o outro |
| **Treino de arma** | **as treze categorias**: Simples, Marciais e Arma de Fogo |

*Perícia, ofício e Teste de Resistência entram na ficha uma vez, na criação. O quadro completo das vinte e três perícias e dos onze ofícios está no capítulo 3, __Perícias e Ofícios__.*

### Degraus da Vanguarda

> **Nível 2: `Escola de Arma`.** **Escolha uma das treze categorias de arma.** Com armas daquela categoria você usa a **Manha** dela. *As treze estão na seção seguinte.*
>
> **Nível 7: Ataque extra.** Você ganha **um golpe simples solto por rodada**. Ele não exige a Ação de Atacar: acontece junto do que a sua Ação Padrão fez naquele turno, inclusive quando ela conjurou.
>
> **Nível 15: `Não Cede`.** **Quando você falha num Teste de Resistência, role de novo e use o segundo resultado.**
> **`Maestria` vezes por descanso curto (`1` no nível 2, `4` no 30) e no máximo uma por rodada.**
>
> **Nível 30: `Não Acabou`.** **Quando você reduz um alvo a 0 de vida, você recupera a sua Reação e o seu movimento, e pode fazer um golpe simples.** **Até `metade da sua maestria` vezes por rodada.**

*O `Não Cede` vale tanto quanto vale fora de combate: veneno, ilusão, maldição que tenta te dobrar pela cabeça, tudo isso resolve em Teste de Resistência, e a Vanguarda é o Caminho que sempre tem uma segunda chance no bolso.*

*O `Não Acabou` vive contra turba: um capanga de nível alto não cai num golpe simples, e um de nível baixo cai. É a regra de abrir caminho no meio de muita gente.*

### Manhas

Ter escola de arma quer dizer que alguém te ensinou aquela categoria de verdade, do jeito antigo: repetição, forma, um professor corrigindo o seu pulso até a coisa virar reflexo. Duas pessoas com a mesma espada na mão fazem coisas diferentes com ela, e a diferença é a escola.

A Manha entrega o que a sua categoria sabe fazer além de causar dano. Você usa a da categoria que escolheu na `Escola de Arma`, e ela vale com qualquer arma daquela categoria: a escola é do tipo de arma, e a peça específica é descartável. Se a sua lâmina quebrou no meio da missão e você pegou outra do chão, a Manha continua.

A Manha dá identidade à sua ficha. Você vira a pessoa do machado, a pessoa da corrente, a pessoa do fuzil, e o grupo aprende a jogar em volta do que a sua arma faz com a posição do inimigo.

**Manhas**
| Categoria | Manha | O que faz |
|---|---|---|
| Lâmina Curta | `Talho` | `+1` no acerto contra alvo que já levou dano seu nesta luta |
| Lâmina Longa | `Raspão` | o ataque que **erra** ainda causa o seu atributo |
| Massa | `Abalo` | o alvo cai: condição `Derrubado` |
| Porrete | `Tranco` | desvantagem no próximo ataque do alvo |
| Manopla | `Encaixe` | `+2` de Defesa até o seu próximo turno, se você acertou |
| Machado | `Racho` | o golpe pega um segundo alvo ao seu alcance |
| Ceifa | `Gancho` | você puxa o alvo `6 m` para perto de você |
| Armas Longas | `Espeto` | você empurra o alvo `6 m`, e ele não te acompanha |
| Flexível | `Laço` | o alvo perde o deslocamento inteiro do próximo turno |
| Arremesso | `Palmo` | `+1` no acerto do próximo arremesso contra o mesmo alvo |
| Yumi | `Zunido` | o tiro que **erra** ainda causa o seu atributo |
| Balestra | `Prego` | o alvo perde `9 m` do deslocamento do próximo turno |
| Arma de Fogo | `Estampido` | todo aliado que enxerga tem `+1` no próximo ataque contra o alvo |

> **A Manha nunca é dado de dano.** Ela mexe em onde as pessoas estão, em quem é atingido, e em quanto a próxima rolagem custa. Valor fixo de dano ela pode dar. Dado de dano é assunto do equipamento.

### Trilha: Estocada

*A arma faz o que a luta pedir, e o que ela pede muda toda rodada.*

Quem joga de `Estocada` troca de ferramenta mais rápido do que o inimigo troca de plano: espada na mão e técnica saindo por cima, na mesma rodada. A decisão de cada turno é qual feitiço vale gastar a ação padrão, sabendo que o golpe da bônus depende do que ele fez.

> **Nível 2: `Compasso`.** Você usa a ação **Conjurar** na ação padrão e dá um **golpe com arma do grupo escolhido** como ação bônus.
> **E naquele grupo de armas, o acerto e o dano usam Essência ou Inteligência** no lugar de Força ou Destreza. **O requisito de Força para empunhar continua valendo.**
>
> **Nível 11: `Traçado`.** Quando o feitiço que você conjurou **acerta**, o golpe da ação bônus **pega um segundo alvo adjacente ao primeiro**.
>
> **Nível 19: `Bote`.** Quando o feitiço que você conjura na ação padrão é **de condição e não de dano**, você pode usar o seu **ataque extra** na ação bônus.
>
> **Nível 27: `Ferrão`.** Se o feitiço que você conjurou na Ação Padrão **acertou**, o **primeiro** golpe da sua ação bônus carrega um **feitiço de Classe 0** junto. *O Classe 0 acompanha o golpe: se o golpe erra, ele não sai.*

*O `Compasso` também muda a sua ficha fora da luta, porque a partir dele a arma bate com o mesmo atributo que a sua técnica usa. Uma Vanguarda de `Estocada` pode montar personagem com Força baixa e ainda ser perigosa de arma na mão, e isso abre espaço para uma pessoa muito mais interessante socialmente do que o brutamontes de sempre.*

*O que a Trilha compra é o que a Vanguarda perdia: conjurar gasta a ação padrão, então usar a sua técnica custava todos os ataques da rodada. Aqui não custa mais.*

### Trilha: Batedor

*A luta acontece onde você decide, e você decide longe.*

Quem joga de `Batedor` trata distância como arma: sobe, se afasta, escolhe o ângulo, e quando o inimigo chega perto a briga já está decidida há três rodadas. Você passa a cena pensando em linha de visão e rota de subida, dentro e fora de combate — vigilância de alvo, cobertura de quem entrou no prédio, o tiro que resolve a cena sem ninguém precisar atravessar a porta.

**A rota se escolhe no nível 2 e vale a campanha inteira.** As três resolvem o mesmo problema (onde a luta acontece) por portas diferentes: o `Yumi` atira de onde ninguém alcança, a `Arma de Fogo` atira de dentro do aperto, e a `Besta` empurra o inimigo para fora do problema.

As três concedem a mesma ação no nível 11 e estendem ela no 27:

> **`Mirar`.** *Ação Bônus.* Você firma o corpo e alinha o tiro.
> **O seu próximo ataque com arma de projétil nesta rodada é rolado com vantagem.**
> **Você só pode `Mirar` se não tiver se deslocado nesta rodada, e o `Mirar` se perde se você se deslocar.**

#### Rota: Yumi

Arco longo, treino de clã, silêncio. A rota do `Yumi` troca cadência por precisão e por altura: um tiro bem colocado, de um lugar em que ninguém contava que houvesse alguém. É a mais móvel das três em terreno vertical, e a que mais gosta de crítico.

> **Nível 2: `Disparo Carregado`.** Você **não sofre desvantagem na faixa longa** de arma de projétil. O seu deslocamento sobe **`+3 m`** e conta como **deslocamento de escalada**, árvore, parede, o que a ficção permitir.
> **O `Disparo Carregado`:** *ação bônus.* O seu próximo ataque com arco tem a **margem crítica reduzida em 1** (crítico em `19` ou `20`). *E você pode abdicar do seu ataque extra para somar o dado da arma ao ataque carregado, **sem o atributo**, perde dano e ganha chance de crítico.*
>
> **Nível 11: `Mirar`.** Você ganha a ação **`Mirar`**. **Uma mesma Ação Bônus sua faz o `Mirar` e o `Disparo Carregado` juntos**, os dois custam aquele slot, e só o `Yumi` pode empilhar os dois. E os seus ataques com arma de longo alcance somam **`+2` no acerto**.
>
> **Nível 19: `Pique`.** O `Disparo Carregado` passa a reduzir a margem em **2**, crítico em `18` a `20`.
>
> **Nível 27: `Dobro`.** O `Mirar` passa a valer para o **ataque básico e o extra**, e o `Disparo Carregado` reduz a margem em **3**, crítico em `17` a `20`.

*O deslocamento de escalada do nível 2 é metade do valor dessa rota fora de combate: telhado, andaime, encosta, janela de terceiro andar. Você chega em lugar que o resto do time precisa de corda para alcançar.*

#### Rota: Besta

A besta é ferramenta de quem trabalha sozinho e não tem tempo de recarregar. Essa rota resolve a manivela de uma vez e usa o impacto do virote para tirar o inimigo do lugar, o que faz dela a única das três que também administra posicionamento.

> **Nível 2: `Manivela`.** As suas bestas **deixam de carregar `Munição`** — a propriedade de arma do capítulo 13, *Equipamento* —, você nunca recarrega.
>
> **Nível 11: `Mirar`.** Você ganha a ação **`Mirar`**, e os seus ataques com arma de longo alcance somam **`+2` no acerto**.
>
> **Nível 19: `Repuxo`.** Ao disparar, **uma vez por rodada**, o alvo faz um Teste de Resistência de Vigor; numa falha, é empurrado **`1,5 m × maestria`** na direção oposta.
> **E você deixa de sofrer desvantagem por estar colado**, o tempo todo.
>
> **Nível 27: `Dobro`.** O `Mirar` passa a valer para o **ataque básico e o extra**.

#### Rota: Arma de Fogo

Pólvora, ruído e uma profissão que finge não usar isso. É a rota que funciona no aperto: corredor estreito, sala pequena, inimigo colado em você. Quem escolhe `Arma de Fogo` aceita chamar atenção de todo mundo num raio de quarteirão, e o resto do time precisa contar com isso no plano.

> **Nível 2: `Ferrolho`.** A sua arma de fogo só força recarga no **`1` natural**, e não no `1` ou `2`.
> **E você deixa de sofrer desvantagem por estar colado**, o tempo todo.
>
> **Nível 11: `Mirar`.** Você ganha a ação **`Mirar`**, e os seus ataques com arma de longo alcance somam **`+2` no acerto**.
>
> **Nível 19: `Descarga`.** No começo de um combate, você pode gastar a sua **Reação** para atacar **um alvo por bala que a arma carrega**, com uma rolagem separada em cada um. **Os disparos contam para a munição**, você vai recarregar no primeiro turno.
>
> **Nível 27: `Dobro`.** O `Mirar` passa a valer para o **ataque básico e o extra**.

*A `Descarga` abre a luta com um tiro por bala carregada, cada um num alvo. Se o grupo abre a porta e encontra a sala cheia, ela é a diferença entre começar a luta atrás e começar com metade da sala já ferida.*

### Trilha: Executor

*Você mata o que ninguém consegue matar.*

Quem joga de `Executor` trabalha sem técnica grande e sem gritaria: uma lâmina, um alvo, e a paciência de trocar golpe até acabar. Você aceita um turno simples e uma ficha teimosa: bate, apanha, repõe casca e bate de novo, e o inimigo acaba antes de você.

> **Nível 2: `Pegada`.** Você escolhe um **estilo de luta**, e ele vale a campanha inteira. *Cada estilo pede um jeito diferente de segurar a arma, e é isso que impede um de ser a versão melhor do outro.*
>
> **Nível 11: `Aprumo`.** *Ação bônus.* Você ganha **`1d10 + o seu atributo de ataque`** de `vida temporária`, Força ou Destreza, o que a sua ficha usa para bater. **`Metade desse atributo` usos**, e eles voltam no descanso curto.
>
> **Nível 19: `Revide`.** *Reação.* Quando alguém a até `1,5 m` faz um ataque contra você, **acertando ou errando**, você pode gastar a sua Reação para atacar essa criatura.
>
> **Nível 27: `Retomada`.** Quando você **erra uma rolagem de ataque**, role de novo e use o segundo resultado. **`Maestria` vezes por dia.**

*O `Aprumo` repõe casca sozinho, sem gastar PE e sem depender de ninguém do time. Numa campanha em que a cura é escassa, isso é o que permite encadear duas ou três lutas no mesmo dia.*

#### Estilos da `Pegada`

**Estilos da `Pegada`**
| Estilo | Pede | O que dá |
|---|---|---|
| `Duelista` | uma arma numa mão, a outra vazia | `+2` de dano em todo golpe |
| `Arremesso` | arma arremessada | `+2` de dano em todo golpe |
| `Desarmado` | punho vazio | `+metade da maestria` de dano no soco |
| `Defesa` | vestindo `Traje` ou `Revestimento` | `+1` de Defesa |
| `Arma Grande` | arma de duas mãos | rerrolar `1` e `2` no dado de dano |

> **Todo estilo pede alguma coisa, e o pedido é regra.** Um estilo sem porta ficaria disponível para toda ficha, e aí ninguém escolheria os outros.

O `Traje` e o `Revestimento` são as duas formas de proteção do capítulo 13, *Equipamento*.

## Guia

*O outro é a resposta: estender, recuperar, reposicionar.*

O Guia faz o efeito de outra pessoa durar mais, pegar mais gente ou chegar mais longe. Ele passa a luta olhando para os aliados: quem está prestes a falhar um teste, quem está no lugar errado, quem cai na próxima rodada. Quando ele age, o resultado aparece na ficha de outra pessoa.

### Características do Guia

**Características do Guia**
| | |
|---|---|
| **Vida por nível** | 5 |
| **PE por nível** | 5 |
| **Atributo natural** | Essência |
| **Perícias fixas** | `Persuasão` · `Medicina` |
| **Perícias à sua escolha** | 4, de qualquer lugar do quadro |
| **Ofícios** | 2, à sua escolha. O Caminho não trava ofício |
| **Teste de Resistência** | 1 treinado, à sua escolha. A sua Origem treina o outro |
| **Treino de arma** | **Arma de Fogo** e **Balestra**, as duas que não pedem treino de verdade |

*Perícia, ofício e Teste de Resistência entram na ficha uma vez, na criação. O quadro completo das vinte e três perícias e dos onze ofícios está no capítulo 3, __Perícias e Ofícios__.*

> ****Nenhuma rota dá ataque extra ao Guia.**** Quem quiser lutar de Guia paga pela técnica, como todo mundo. Em troca, o degrau do nível 7 dele entrega duas coisas em vez de uma.

### Degraus do Guia

> **Nível 2: `Guiar`.** Quando um aliado que você enxerga falha num teste, some **`metade da sua Essência`** ao resultado dele. **Ação livre, uma vez por rodada.** *Você aplica depois da rolagem, então nenhum ponto se perde.*
>
> **Nível 7: `Mão na Roda`.** A ação **`Ajudar` passa a ser ação bônus para você.**
> **E quando você usa o `Guiar` num aliado, ele pode acrescentar um golpe simples ao turno dele.** Uma vez por rodada.
>
> **Nível 15: `Puxar a Linha`.** *Ação bônus.* Um aliado que você enxerga a até 9 m **se move até o deslocamento inteiro dele, sem provocar ataque de oportunidade.** Ele não pode recusar.
>
> **Nível 30: `Ninguém Cai`.** *Reação.* Quando um aliado que você enxerga chegaria a 0 de vida, **ele fica com `1`** e **o dano excedente é anulado.**

*O `Guiar` rende mais fora de combate do que dentro: a negociação que o grupo não podia perder, a fechadura, o teste de perícia que decidia a missão. Metade da sua Essência somada depois da rolagem cabe em qualquer cena em que alguém do time abre a boca ou põe a mão em alguma coisa.*

*O `Puxar a Linha` resolve o aliado inconsciente, o aliado agarrado por decisão ruim e o aliado que entrou num lugar de onde não ia sair. A parte de ele não poder recusar é o que faz a entrega funcionar sob fogo.*

### Trilha: Elo

*O que outra pessoa fez chega mais longe, dura mais e pega mais gente do que ela conseguiria sozinha.*

Quem joga de `Elo` amplifica: você escolhe uma pessoa, e enquanto o elo estiver de pé o que ela faz chega mais longe. A ficha do `Elo` quase não causa dano, e a sua decisão de cada cena é em quem você está pendurado agora.

> **Nível 2: `Nó`.** **Ação Bônus.** Escolha um aliado **que você enxerga**: vocês dois formam um **elo**. Ao formar, escolha **ataques de arma** ou **ataques de feitiço**, enquanto o elo durar, **os dois membros ganham `+1` de acerto** naquele tipo de ataque.
> **O elo dura até você formar outro**, e **não se quebra por distância**.
>
> **Nível 11: `Repasse`.** **Reação.** Quando um membro do elo falha num Teste de Resistência, ele **rerrola** e fica com o segundo resultado.
> **Na mesma Reação você pode gastar `3` PE para passar o elo** para alguém que não esteja nele, e o rerrolar vai junto, para quem acabou de entrar.
>
> **Nível 19: `Partilha`.** Quando um membro do elo recebe cura, **você reparte o total entre os membros como quiser.** *O total continua o mesmo. O que você escolhe é o destino dele.*
>
> **Nível 27: `Trança`.** O elo passa a aceitar um **terceiro membro**.
> **E `1×` por descanso curto** você passa até **`4` PE seus** para alguém do elo.

*O elo não se quebrar por distância é o que faz essa Trilha render em cena dividida: o grupo se separa no prédio, você fica com o time da entrada, e o `+1` continua valendo para quem subiu. A `Trança`, no 27, é a resposta para o conjurador do grupo que ficou sem PE no meio da missão.*

### Trilha: Sutura

*O dano que já aconteceu não é definitivo enquanto você estiver na sala.*

A `Sutura` põe o médico de campo no grupo — a pessoa que a instituição manda junto quando a missão tem chance real de alguém não voltar. A Trilha entrega a `Energia Reversa` sem os requisitos de nível e de refino que o resto da ficha paga, e no meio da luta a sua decisão é quem vale a energia.

> **Nível 2: `Agulha`.** Você ganha a aptidão **`Energia Reversa`** **sem os requisitos de nível e de refino**. *Por uso, você não pode gastar mais que **`metade da sua maestria`** em PE.*
>
> **Nível 11: `Enxerto`.** A sua `Energia Reversa` passa a **curar os outros**, e o teto por uso sobe para **`a sua maestria`** em PE.
> **E o mesmo uso pode tirar uma condição:** gaste **`1` PE por nível da condição**, e ele sai do mesmo teto da cura. *Condição sem nível declarado conta como **nível 1**.*
>
> **Nível 19: `Pulso`.** Some o seu **modificador de Essência** em toda rolagem de cura sua. *Vale também para cura que venha da sua técnica, e não só da `Energia Reversa`.*
>
> **Nível 27: `Cerzido`.** O teto por uso vai a **`a sua maior Classe`** em PE, e você **rerrola `1` e `2`** em todos os seus dados de cura, ficando com o segundo resultado.

*O `Enxerto` limpa veneno, paralisia, maldição pequena grudada em alguém, e condição que o grupo não tinha como tirar de outro jeito. Ele faz isso com o mesmo uso da cura, então a decisão vira quanto do teto você gasta consertando o corpo e quanto gasta tirando a coisa de cima dele.*

> **`Energia Reversa` não cura dano de alma.** Nenhum degrau desta Trilha alcança isso.

### Trilha: Perímetro

*Você escolhe onde todo mundo está.*

Quem joga de `Perímetro` anda com uma área em volta do corpo, e dentro dela o inimigo rola pior, abre guarda e paga por tentar sair. O seu trabalho é posicionamento: você se coloca onde a área cobre o máximo de inimigo, e o resto do time luta dentro dela sem precisar saber por quê.

> **Nível 2: `Chão`.** Você tem uma área de **`9 m` a partir de você**, e ela anda com você.
> **`1×` por rodada**, um inimigo dentro dela **rerrola um Teste de Resistência e fica com o pior**. *Você declara **antes** de o resultado ser lido.*
>
> **Nível 11: `Sentinela`.** **Reação.** Quando um inimigo dentro do `Chão` **erra** um ataque, um aliado que você enxerga dá **um golpe simples com vantagem** nele.
>
> **Nível 19: `Encalço`.** **Ação Bônus.** Ponha um alvo do `Chão` **no encalço**. **`1×` por rodada**, ele leva **`−1d6`** numa perícia ou num Teste de Resistência.
> **Ele dura até o fim da cena**, e você só tem **um alvo no encalço de cada vez**: pôr outro tira o primeiro.
>
> **Nível 27: `Portão`.** A `Sentinela` passa a disparar **quando o ataque do inimigo acerta também**, e **quando um alvo sai do `Chão` por movimento voluntário**.

*O `Encalço` atravessa a cena inteira, dentro e fora de combate: ele dura até o fim, ele pega perícia, e um alvo marcado erra a fuga, erra a mentira e erra a escalada. Numa perseguição pela cidade, é ele que decide.*

## Emanador

*A técnica é a resposta: mais feitiço, mais aptidão.*

O Emanador apostou tudo na técnica. Corpo pouco, energia muita, e um repertório que resolve problema que arma nenhuma resolve. Quem escolhe esse Caminho gosta de ficha com botão: quer ter a resposta certa para a situação específica e aceita ser o mais frágil da sala em troca disso.

### Características do Emanador

**Características do Emanador**
| | |
|---|---|
| **Vida por nível** | 4 |
| **PE por nível** | 6 |
| **Atributos naturais** | Inteligência · Essência |
| **Perícias fixas** | `Ocultismo` · `Investigação` |
| **Perícias à sua escolha** | 4, de qualquer lugar do quadro |
| **Ofícios** | 2, à sua escolha. O Caminho não trava ofício |
| **Teste de Resistência** | 1 treinado, à sua escolha. A sua Origem treina o outro |
| **Treino de arma** | **Arma de Fogo** e **Balestra**, as duas que não pedem treino de verdade |

*Perícia, ofício e Teste de Resistência entram na ficha uma vez, na criação. O quadro completo das vinte e três perícias e dos onze ofícios está no capítulo 3, __Perícias e Ofícios__.*

### Degraus do Emanador

> **Nível 2: `Sangria`.** *Ação bônus.* Gaste **`1/8` da sua vida MÁXIMA** e ganhe PE na razão de **`3` de vida por `1` PE**. A vida máxima só volta no **descanso longo**; metade dela volta no **descanso curto**.
>
> **Nível 7: `Resquício`.** Ao conjurar na Ação Padrão um feitiço **que não causa dano**, você pode lançar um **feitiço de Classe 0 na Ação Bônus**.
>
> **Nível 7: `Modelagem`.** Ao conjurar um feitiço **de dano ou de condição**, você pode **trocar uma Melhoria que ele já tem por outra de custo igual ou menor**. Nada novo entra na ficha. O que muda é qual peça está montada na hora.
> **A troca não mexe na condição.** A Melhoria `Condição` não entra nem sai. **E a Melhoria que entra tem de ser legal naquele feitiço**: o requisito dela continua valendo.
>
> **Nível 15: `Segunda Leitura`.** No fim de um descanso longo, você pode **esquecer um dos seus feitiços e aprender outro no lugar.**
> **O novo tem de ser um feitiço que você poderia ter escolhido no nível em que está.**
>
> **Nível 30: `Fonte`.** Feitiços de **Classe 3 ou menos custam metade do PE**.
> **E um feitiço de Classe 2 à sua escolha, de dano ou de condição, passa a custar `0`.**

*A `Modelagem` deixa o Emanador improvisar sem ter previsto: você chegou com o feitiço montado para uma coisa e o alvo é outra, e a peça se remonta na hora. A `Segunda Leitura` faz o mesmo em escala de missão, e muda o preparo do grupo: com um briefing decente, você dorme e acorda com a ficha desenhada para aquele alvo específico.*

*A `Sangria` se auto-limita no calendário: `1/8` cabe exatamente quatro vezes antes de você ter perdido metade da vida, e o dia esperado tem três a quatro lutas.*

### Trilha: Torrente

*Você lança até a energia acabar, e ela acaba.*

Quem joga de `Torrente` abre a torneira: dois feitiços na mesma rodada, técnica em cima de técnica, e um bolso de PE que some rápido. A Trilha te dá a rodada grande e cobra o resto da missão, então a decisão real é em qual luta do dia você abre a torneira.

> **Nível 2: `Acelerar`.** *`2×` por cena.* Você conjura um feitiço da sua **ação padrão como ação bônus**, pagando **`Classe e meia` de PE a mais**, arredondando para cima. *Num Classe 7 são `11` de PE.*
> Naquele turno, o outro feitiço que você lançar **não passa de `Classe 0`**.
>
> **Nível 11: `Vazão`.** Aquele teto deixa de ser `Classe 0` e passa a ser **metade da sua maior Classe**, arredondando para baixo.
>
> **Nível 19: `Cheia`.** Quando o feitiço que você conjura é **o único feitiço daquele turno**, **rerrole todo dado de dano dele que cair em `1`, `2` ou `3`.** Você fica com o segundo resultado.
>
> **Nível 27: `Transbordo`.** Aquela metade passa a **arredondar para cima.** *Com Classe 7 o teto vai de `Classe 3` para `Classe 4`.*

*A `Cheia` premia a rodada calma, e é ela que segura a Trilha nas cenas longas: nos turnos em que você não abre a torneira, o feitiço único sai mais consistente. As duas metades da `Torrente` se revezam ao longo da luta.*

> **Só o `Transbordo` arredonda para cima**; a regra global sempre desce. Ela vale aqui e em lugar nenhum mais.

### Trilha: Explosivo

*Um feitiço só na rodada, e ele sai maior.*

Quem joga de `Explosivo` trabalha como artilheiro: passa duas rodadas se posicionando e resolve a luta na terceira. Quase toda entrega da Trilha melhora a mesma coisa, que é o feitiço único do seu turno — você escolhe o momento em que o alvo está agrupado ou exposto e transforma uma rolagem em cena inteira.

> **Nível 2: `Pavio`.** Quando o feitiço que você conjura é **o único feitiço de dano daquele turno**, **rerrole todo dado de dano dele que cair em `1` ou `2`.**
>
> **Nível 11: `Estopim`.** Todo feitiço seu soma o **atributo da sua técnica** no dano.
>
> **Nível 19: `Rompante`.** Ao conjurar um feitiço que resolve por rolagem de acerto, você pode gastar **`a Classe` dele em PE** para rolar aquele ataque **com vantagem**. *Num Classe 7 são `7` PE, além dos `21` do próprio feitiço.*
>
> **Nível 27: `Ápice`.** `1×` por cena, um feitiço seu soma **`metade da Classe` em dados de dano**, e você paga **`1` PE por dado extra**. *Num Classe 7 são `+3d8` por `3` PE.*

*O `Rompante` compra vantagem na rolagem em que errar custaria a rodada inteira e o PE junto — que é a de chefe, quase sempre.*

### Trilha: Arremate

*O feitiço chega junto com você.*

Quem joga de `Arremate` precisa encostar: briga de mão, e o feitiço sai quando a mão chega. Você precisa estar dentro do alcance do inimigo para render, e boa parte da Trilha existe para você sobreviver ao lugar em que ela te obriga a ficar.

> **Nível 2: `Empunhadura`.** Escolha um **grupo de arma**. Você é treinado nele, e naquele grupo **o acerto e o dano usam Inteligência ou Essência**. *O requisito de Força para empunhar continua valendo.*
> **E quando você ataca com uma arma daquele grupo na Ação Padrão, você pode conjurar um feitiço de Classe na Ação Bônus.**
>
> **Nível 11: `Rebote`.** A sua ação de Atacar passa a dar **dois golpes**.
>
> **Nível 19: `Crosta`.** Quando você conjura estando **adjacente a um inimigo**, você ganha **`maior Classe` de `vida temporária`**.
>
> **Nível 27: *vaga*.** *A casa existe e está vazia. A ficção dela é o capstone do molde: deixar de precisar encostar.*

*A `Crosta` sustenta o `Arremate` a partir do 19: a mesma decisão que te põe em perigo, que é conjurar colado, passa a ser a que te dá casca. Antes disso, a sua sobrevivência depende do time.*

> **O `Arremate` ganha ataque extra pela Trilha, e não pelo Caminho.** A outra assim é o `Coro`. A outra é o `Coro`. **O golpe é uma Ação Bônus, e ele só existe se a Ação Padrão daquele turno conjurou ou atacou com a arma do grupo escolhido.** A trava que continua valendo é a de sempre: um feitiço de Toque por turno, e ataque extra é sempre golpe simples.

## Evocador

*O que você trouxe é a resposta: invocações.*

O Evocador chega acompanhado. Shikigami, talismã que vira bicho, maldição domada: o que ele põe em campo tem corpo próprio, anda por conta e obedece a ele. Quem escolhe esse Caminho gosta de jogar tabuleiro, contar espaço, flanquear, bloquear corredor, e usar corpo emprestado onde outro Caminho usaria o próprio.

### Características do Evocador

**Características do Evocador**
| | |
|---|---|
| **Vida por nível** | 4 |
| **PE por nível** | 6 |
| **Atributos naturais** | Inteligência · Essência |
| **Perícias fixas** | `Religião` · `Lidar com Animais` |
| **Perícias à sua escolha** | 4, de qualquer lugar do quadro |
| **Ofícios** | 2, à sua escolha. O Caminho não trava ofício |
| **Teste de Resistência** | 1 treinado, à sua escolha. A sua Origem treina o outro |
| **Treino de arma** | **Arma de Fogo** e **Balestra**, as duas que não pedem treino de verdade |

*Perícia, ofício e Teste de Resistência entram na ficha uma vez, na criação. O quadro completo das vinte e três perícias e dos onze ofícios está no capítulo 3, __Perícias e Ofícios__.*

### Degraus do Evocador

> **Nível 2: `Sintonia`.** **Escolha uma:**
> **`Presa`** — as suas invocações acertam crítico com **19 ou 20**.
> **`Casco`** — as suas invocações têm mais vida.
> **`Voz`** — a CD dos efeitos das suas invocações sobe em **`1`**, e vira **`metade da sua maestria`** a partir do nível 7.
>
> **Nível 7: `Coleira`.** As suas invocações são **treinadas nas perícias e Testes de Resistência que a ficha delas tiver**, e somam **`+1` no acerto**.
>
> **Nível 15: `Escudo de Osso`.** *Reação.* Quando você é alvo de um ataque com rolagem, uma invocação sua a até 9 m **recebe o ataque no seu lugar**.
>
> **Nível 30: `Segundo Corpo`.** **Uma vez por descanso curto, invocar não custa a ação padrão**, só o PE.

*A `Coleira` faz a invocação servir fora de combate: treinada nas perícias da ficha dela, ela vira o que entra no duto, o que fareja, o que fica de vigia enquanto o grupo dorme. E o `Escudo de Osso` é o que compra a rodada em que você ia cair, o que importa muito numa ficha de 4 de vida por nível.*

### Trilhas do Evocador

> **As três Trilhas do Evocador concedem o corpo da invocação, e mais nada.** As entregas de nível — as dos níveis 2, 11, 19 e 27 que as outras doze Trilhas têm — não existem nelas.
>
> **Um Evocador joga hoje com os quatro degraus de Caminho e com o corpo que a Trilha dá.** Se for a sua escolha, combine com o mestre o que ocupa essas quatro casas.

**O que cada Trilha concede** é o corpo que você põe em campo. O resto da ficha da invocação você monta com o orçamento do capítulo 15, *Invocações*, por cima do que está na tabela.

**Trilhas do Evocador**
| Trilha | O que ela concede | Orçamento do corpo | Vida do corpo |
|---|---|---|---|
| `Servo` | um corpo forte | **o da ficha mais metade**, arredondando para baixo | **`5 × h`** |
| `Matilha` | os cinco corpos | o da ficha | `5 × h`, em pool com cascata |
| `Coro` | atacar e comandar na mesma rodada | o da ficha | `h` |

*`h` é a vida de uma invocação pela fórmula do capítulo 15, __Invocações__, que já conta o tipo dela e o seu nível.*

#### Servo

*Uma invocação, forte.* O `Servo` põe em campo um corpo só, com nome, que anda com você a campanha inteira. Ele carrega a vida do bando inteiro da `Matilha` num corpo, e o orçamento dele é o da ficha mais metade. Perder esse corpo tira o kit da mesa de uma vez.

#### Matilha

*Muitos corpos fracos.* A `Matilha` põe cinco corpos em campo, e a sua vantagem é estar em cinco lugares ao mesmo tempo. Ela conta como **uma ficha com cinco corpos**: uma barra de vida só, e o dano que passa de um corpo cascateia para o seguinte. Os cinco continuam no campo, cada um com a sua posição. **A rodada dela se resolve em pool**, os cinco d20 saem de uma vez, conta-se os acertos, e o dano dos que acertaram se soma. Cada corpo declara o próprio alvo **antes** da rolagem.

#### Coro

*Você e a invocação lutam juntos.* No `Coro` você entra na luta junto com o corpo, e os dois se cobrem. Ele **ataca e comanda na mesma rodada**, e abre exceção na economia de ação. O golpe é uma **Ação Bônus**, e ele só existe se a Ação Padrão daquele turno **comandou, e a invocação atacou**. O corpo dele é o mais frágil dos três, e é o único cuja queda deixa o kit funcionando: você continua batendo.

> **Você e todas as suas invocações somados entregam a mesma saída de dano que você entregaria sozinho.** Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto. **A máquina completa (orçamento por nível, `Traço`, `Comando`, a amarra, morte e retorno) está no capítulo 15, *Invocações*.**

---


# Capítulo 9 · Fundamento

*fonte: `manual/40-fundamento.md`*

## Técnica e feitiços

Todo personagem nasce com uma única técnica, e ela nunca muda. Essa técnica se chama **Fundamento**, e é uma descrição e uma regra, escritas por você na criação do personagem. Tudo de sobrenatural que o personagem faz nasce dela.

O que você usa em jogo são os **feitiços**: aplicações concretas da técnica, cada uma com nome próprio. Você mesmo monta os seus feitiços, gastando pontos.

### Classe do feitiço

Todo feitiço tem uma **Classe**, que mede o tamanho dele. A Classe diz quantos pontos você tem para gastar na montagem.

> **Pontos = 3 × Classe.**
> Um feitiço de Classe 3 tem **9 pontos**.

Cada ponto que você não gastar em mais nada vira **1d8 de dano**. Uma Classe 3 que põe tudo em dano causa 9d8.

Os pontos também compram **Melhorias**: alcance maior, área, derrubar o alvo, conjurar como ação bônus. E, se quiser recuperar pontos, você pode aceitar **Restrições**, que são desvantagens devolvendo pontos ao orçamento em troca de o feitiço ficar mais difícil de usar.

Os pontos devolvidos por Restrição só servem para pagar Melhoria: **Restrição nunca aumenta o dano**. E, contra um alvo só, feitiço comum não passa dos pontos da Classe em dados. Quem rompe esse limite é a **Liberação Máxima**, que chega no nível 10.

São oito Classes.

**Classe do feitiço**
| Classe | O que é | Quando aparece |
|---|---|---|
| **0** | O feitiço grátis. Não custa PE, não ocupa espaço na lista e não se monta com pontos. | Nível 1 |
| **1 a 5** | Os feitiços montados. É onde o jogo acontece, e é o que este capítulo ensina a construir. | Níveis 1 a 20 |
| **6 e 7** | A faixa lendária. Mesma montagem, números maiores. | Níveis 21 a 30 |

Cada feitiço é montado na Classe que o seu nível já liberou, e *Números da montagem* mostra quando cada uma chega. Daqui para a frente, quando o texto disser só "a Classe", vale para a escala inteira.

### Exemplo

> **`Lança Negra` · Classe 2 · Projétil**
> Classe 2 dá **6 pontos**.
> A Melhoria `Fura` custa 2 e faz o feitiço ignorar até 6 de Redução de Dano.
> A Restrição `Lento` devolve 2, em troca de a conjuração custar a rodada inteira.
> 6 − 2 + 2 = **6 pontos sobrando**.
> **Dano: 6d8 (média 27). Custo: 6 de PE.**
>
> A Restrição pagou a Melhoria inteira, e o feitiço saiu com o dano cheio da Classe. É exatamente para isso que Restrição serve, e ela para aí: 6 pontos continuam sendo o máximo de dados de uma Classe 2 contra um alvo.

### Atributo da técnica

**Toda técnica usa um atributo, e você escolhe qual quando escreve ela.** Um dos cinco, na criação, e ele não muda depois.

> **Ataque de conjuração = d20 + o atributo da sua técnica + maestria**
> **Maestria** começa em 1 e sobe um ponto a cada oito níveis.

É a mesma forma do soco e do tiro — atributo mais maestria —, e é de propósito: **o feitiço não tem uma regra própria de acertar.** Uma técnica de cálculo usa Inteligência, uma de leitura de energia usa Essência, e o feiticeiro que conjura batendo usa Força. Na obra, o Todo conjura assim.

**Ataque e CD de um atributo levado ao teto**
| Seu nível | Maestria | Atributo | Ataque de conjuração | CD dos seus feitiços |
|---|---|---|---|---|
| 2 a 9 | 1 | 3 | d20 + 4 | 12 |
| 10 a 17 | 2 | 4 | d20 + 6 | 14 |
| 18 a 25 | 3 | 5 | d20 + 8 | 16 |
| 26 a 30 | 4 | 6 | d20 + 10 | 18 |

Esta tabela supõe que você levou o atributo da técnica até o topo. Se ele ficar parado, a sua técnica fica junto.

**Escolha o atributo que o seu personagem já ia querer alto.** As perícias que ele usa, o Teste de Resistência que ele quer aguentar, uma Trilha que soma o mesmo atributo no dano: se alguma dessas coisas já puxa um atributo para cima, aponte a técnica para ele. Apontar para um atributo que você não pretende pagar é a armadilha desta página.

> Nada te obriga a escolher Inteligência ou Essência. Elas são as mais comuns porque quase toda técnica é análise ou percepção — mas a regra é *um dos cinco*, e a ficção decide.

**Inteligência ou Essência**
| Inteligência | Essência |
|---|---|
| conhecimento, investigação | perceber energia amaldiçoada |
| reconhecer uma técnica pelo catálogo | trato social, hierarquia |
| Teste de Resistência de Intelecto | negociar Pactos, Teste de Resistência de Espírito |

Uma técnica de análise, registro, cálculo ou memória cai em Inteligência. Uma técnica de leitura de energia, presença, voz ou vínculo cai em Essência. Sentir energia amaldiçoada é a sua energia reagindo à de outro, e por isso mora em Essência.

### CD de feitiço

Metade dos seus feitiços deixa a rolagem com o alvo: ele é quem rola contra você. O número que ele precisa passar é a sua **CD de feitiço**.

> **CD de feitiço = 8 + o atributo da sua técnica + maestria.**

**Você tem uma CD só.** Ela não muda de feitiço para feitiço, não sobe com a Classe e não se compra com pontos. É um número da ficha, como a sua Defesa.

**O que o alvo rola.** Um **Teste de Resistência**: `d20 + o atributo daquele Teste`, mais 2 se ele for treinado nele. Igualou ou passou a sua CD, ele resistiu. Nos feitiços de área (`Explosão`, `Aura`, `Cone`, `Linha`) resistir quer dizer levar metade dos dados, salvo se você tiver comprado a Restrição `Tudo ou Nada`.

**O que mexe na CD.** Só três coisas sobem a sua CD, e todas são compradas por feitiço:

**CD de feitiço**
| O que | Quanto | De onde vem |
|---|---|---|
| `Precisão` | +2 na CD | Melhoria de Mira, custa Leve |
| `Adianta` | +2 na CD se você conjurar antes de qualquer inimigo agir na rodada | Melhoria de Tempo, custa Média |
| bônus de Controle | +2 na CD contra os efeitos de Controle, quando o feitiço sai sem nenhum dado de dano | de graça, ver *Controle* |

`Abre Ferida` e `Sobrecarga` chegam no mesmo lugar pelo outro lado: elas derrubam os números do alvo.

> **Exemplo.** Kaito é Classe 3, maestria 2: CD 14. Ele monta o mesmo feitiço em duas versões, uma de acerto e uma de Teste de Resistência, e escolhe na hora conforme o alvo. Contra a maldição de Defesa 12 e Vigor alto, ele usa a de acerto. Contra a de Defesa 19 e Vigor fraco, a de resistência. **O feitiço é o mesmo; o que muda é qual número do inimigo está mais baixo.**

### Peças da técnica

**Peças da técnica**
| Peça | O que é |
|---|---|
| **Fundamento** | Sua técnica. Uma descrição, uma Regra, Famílias Livres e Fechadas, um Selo e as Passivas. |
| **Feitiços** | As aplicações da técnica. Você monta cada uma. |
| **Passivas** | Efeitos que ficam ligados sozinhos. Custam espaços de feitiço. |
| **Liberação Máxima** | O feitiço que rompe o limite de dano num alvo só. Nos níveis 10, 20 e 30. |
| **Técnica Máxima** | O golpe de dano fixo que carrega o nome da técnica. Do nível 17 em diante. |

## Números da montagem

Esta seção concentra os números que o resto do capítulo usa. Não precisa decorar nada: volte aqui sempre que um trecho citar um valor.

> **Pontos** = 3 × Classe
> **Teto de dano** = 4 × Classe em dados
> **Devolução máxima** = 2 × Classe
> **Liberação Máxima** = + Classe em dados
> **Custo em PE** = 3 × Classe (o mesmo número dos pontos)
> Melhoria `Leve` custa metade da Classe · `Média` custa a Classe · `Pesada` custa Classe e meia. Arredonde para cima.

**Números da montagem**
| Classe | Nível | Pontos e PE | Leve | Média | Pesada | Devol. máx | Liberação | Teto | Dano cheio | Cura cheia |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | 1 | 3 | 1 | 1 | 2 | 2 | +1 | 4 | 3d8 = 13 | 2d8 = 9 |
| **2** | 5 | 6 | 1 | 2 | 3 | 4 | +2 | 8 | 6d8 = 27 | 4d8 = 18 |
| **3** | 9 | 9 | 2 | 3 | 5 | 6 | +3 | 12 | 9d8 = 40 | 6d8 = 27 |
| **4** | 13 | 12 | 2 | 4 | 6 | 8 | +4 | 16 | 12d8 = 54 | 8d8 = 36 |
| **5** | 17 | 15 | 3 | 5 | 8 | 10 | +5 | 20 | 15d8 = 67 | 10d8 = 45 |
| **6** | 21 | 18 | 3 | 6 | 9 | 12 | +6 | 24 | 18d8 = 81 | 12d8 = 54 |
| **7** | 26 | 21 | 4 | 7 | 11 | 14 | +7 | 28 | 21d8 = 94 | 14d8 = 63 |

A coluna **Nível** é quando aquela Classe abre para você. **Leve**, **Média** e **Pesada** são os três preços de Melhoria, e **Devol. máx** é o total que as Restrições de um feitiço podem devolver.

Todo valor de montagem que aparecer daqui para a frente sai desta tabela.

A coluna **Teto** é o máximo de dados de dano de um feitiço quando você soma todos os alvos e repetições. Contra um alvo só o limite é mais baixo: um feitiço comum para nos pontos da Classe. Quem alcança o teto num alvo só é a **Liberação Máxima**.

### Melhorias e Restrições por Classe

**Melhorias e Restrições por Classe**
| Classe do feitiço | Melhorias | Restrições |
|---|---|---|
| **1 e 2** | 2 | 2 |
| **3 e 4** | 3 | 2 |
| **5 em diante** | 4 | 2 |

A Forma não conta como Melhoria.

### Energia

Conjurar um feitiço custa **3 × Classe** de PE, o mesmo número dos pontos dele. Classe 0 é grátis.

**Liberação Máxima** custa 50% a mais que a Classe dela, arredondando para cima. **Técnica Máxima** custa 5 × a sua maior Classe de PE.

Com um conjurador ganhando 6 PE por nível, isso dá:

**Energia**
| Nível | PE total | Maior Classe | Custo | Quantas vezes você lança o seu melhor feitiço |
|---|---|---|---|---|
| 1 | 6 | 1 | 3 | 2 |
| 5 | 30 | 2 | 6 | 5 |
| 9 | 54 | 3 | 9 | 6 |
| 13 | 78 | 4 | 12 | 6 |
| 17 | 102 | 5 | 15 | 6 |
| 20 | 120 | 5 | 15 | 8 |

> **Essa última coluna é um teto, e não um dia.**
> Ela responde uma pergunta só: quantas vezes cabe, se você não fizer mais nada com o seu PE.
> Um dia de verdade tem outras despesas ao mesmo tempo. Tem efeito que cobra PE **por rodada** enquanto está ligado, e a Integridade encarece todo feitiço quando o segundo estágio dela acende.
> Na prática, um conjurador gasta PE em cerca de **metade das rodadas de luta do dia** e passa a outra metade no Classe 0, no golpe simples e no que for de graça. Leia a coluna como limite superior.

### Classe 0

Feitiços de Classe 0 não gastam PE, não ocupam espaço na lista e não se montam: escolha uma Forma e pronto. São o golpe de todo turno em que o PE precisa ser poupado.

**Classe 0**
| Seu nível | 1 | 5 | 11 | 17 | 25 |
|---|---|---|---|---|---|
| Quantos você tem | 2 | 3 | 4 | 5 | 5 |
| Dano | 2d8 | 3d8 | 4d8 | 5d8 | 6d8 |

Cabe uma Melhoria `Leve` numa Classe 0, tirando um dado para pagar. A base de alcance da Classe 0 fica um degrau abaixo da normal, e o valor está em *Criando feitiços*.

### Dado

Monte sempre em d8: pontos, Melhorias e Restrições só existem em d8. Se a sua mesa rola outro dado, converta o total final na hora de rolar.

**Dado**
| d8 | d6 | d12 | d8 | d6 | d12 | d8 | d6 | d12 |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 11 | 14 | 8 | 21 | 27 | 15 |
| 2 | 3 | 1 | 12 | 15 | 8 | 22 | 28 | 15 |
| 3 | 4 | 2 | 13 | 17 | 9 | 23 | 30 | 16 |
| 4 | 5 | 3 | 14 | 18 | 10 | 24 | 31 | 17 |
| 5 | 6 | 3 | 15 | 19 | 10 | 25 | 32 | 17 |
| 6 | 8 | 4 | 16 | 21 | 11 | 26 | 33 | 18 |
| 7 | 9 | 5 | 17 | 22 | 12 | 27 | 35 | 19 |
| 8 | 10 | 6 | 18 | 23 | 12 | 28 | 36 | 19 |
| 9 | 12 | 6 | 19 | 24 | 13 | | | |
| 10 | 13 | 7 | 20 | 26 | 14 | | | |

A média nunca se afasta mais de 3 pontos da conta em d8.

## Escrevendo o seu Fundamento

**Você escreve o Fundamento uma vez**, na criação, junto com o mestre, e ele não muda depois: o que evolui com os níveis são os feitiços que saem dele. Um Fundamento completo tem cinco partes, e esta seção percorre uma por uma.

> **Na criação, você escreve:**
> **1.** A **Descrição** da técnica, com o tipo de dano dela.
> **2.** A **Regra**: a frase que resume o que a técnica faz.
> **3.** As **Famílias**: duas Livres e três Fechadas.
> **4.** O **Selo**: o que você sempre faz para conjurar.
> **5.** A **Passiva Livre**, e, se a técnica pedir, uma `Regra Própria`.

### Descrição

Escreva a sua técnica como quiser, no tamanho que quiser: de onde ela veio, como aparece, o que as pessoas veem quando ela age. A Descrição não tem efeito mecânico direto, mas é dela que o mestre vai tirar a régua para aprovar ou recusar os seus feitiços.

Anote junto o **tipo de dano** da técnica, um ou dois: corte, fogo, peso, o que a Descrição pedir. Esse tipo vale para todos os seus feitiços.

> **Exemplo.** *Duas relíquias respondem ao chamado dela: um bastão com uma tranca na ponta, outro com uma chave. A tranca segura o instante: o que ela prende para de acontecer e continua parado até ela soltar. A chave abre distância: o que ela destrava deixa de estar onde estava. Ninguém sabe se os bastões são a técnica ou se a técnica só precisa deles para caber num corpo humano.*

### Regra

Depois da Descrição, resuma a técnica numa única frase: a Regra. Ela é o contorno da técnica, e todo feitiço que você criar, do primeiro ao último, precisa caber dentro dela.

*"Prender um instante no lugar, ou abrir a distância entre duas coisas."*
*"Cortar tudo o que eu enxergo em duas metades."*
*"Emprestar o meu peso para o que eu encostar."*

Uma boa Regra exclui coisas. "Controlar fogo" não exclui nada e vira um cheque em branco; "acender o que já passou pela minha mão" exclui bastante, e é isso que a torna interessante. O limite é o que obriga a criatividade na montagem dos feitiços.

Se estiver travado, o **Catálogo de temas** no apêndice traz 70 pontos de partida.

### Famílias

As Melhorias, que são as peças que você compra para os seus feitiços, estão divididas em nove Famílias, cada uma cuidando de um tipo de efeito:

**Famílias**
| Família | Do que trata |
|---|---|
| **Alcance** | Chegar longe, se mexer, mexer o inimigo de lugar |
| **Área** | Pegar mais de um alvo, aumentar tamanho, dividir o ataque |
| **Mira** | Acertar, não errar, atravessar defesa |
| **Controle** | Derrubar, prender, calar, barreira, terreno |
| **Auxiliares** | Somar e tirar número: vantagem, defesa, CD, deslocamento |
| **Castigo** | Fazer o dano render mais |
| **Tempo** | Ação bônus, reação, deixar armado, conjurar escondido |
| **Marca** | Preparar o próximo golpe, roubar vida, rastrear |
| **Amparo** | Curar, limpar condição, levantar aliado |

Na criação, o seu Fundamento define a relação dele com essas Famílias, e é aqui que duas técnicas com a mesma Regra viram personagens diferentes.

**Duas Famílias Livres:** as Melhorias delas custam metade da Classe a menos, com mínimo de 1 ponto. É onde a sua técnica é naturalmente boa.

**Três Famílias Fechadas:** você nunca compra nada delas, em Classe nenhuma. É o que a sua técnica simplesmente não faz.

As outras quatro ficam no preço normal.

Na prática: uma Melhoria `Média` num feitiço de Classe 4 custa 4 pontos. Se ela for de uma Família Livre sua, o desconto de metade da Classe (2) derruba o preço para 2. Se for de uma Família Fechada, ela não está à venda.

As Formas, que são o jeito como o feitiço sai, também têm Família: `Explosão`, `Cone` e `Linha` são de **Área**; `Cura`, `Apoio` e `Onda` são de **Amparo**. Fechar uma dessas Famílias bloqueia as Formas dela junto. `Projétil`, `Toque` e `Efeito` são de todo mundo.

### Selo

Para conjurar, o seu personagem sempre faz a mesma coisa, seja qual for o feitiço: um gesto, um som, uma condição visível. É a assinatura da técnica, o que a mesa vê ou ouve toda vez que ela entra em cena.

Bater palma. · Dizer o nome do feitiço. · Estar enxergando o alvo. · Ter tocado no alvo nesta cena. · Estar pisando no chão.

O Selo não mexe em ponto nenhum: não custa, não devolve e não dá bônus. Ele existe para dar corpo à técnica e para criar jogo, porque quem conhece o seu Selo sabe o que procurar quando você se mexe. A única regra mecânica ligada a ele aparece nas Restrições: como o Selo já é uma obrigação sua, **uma Restrição que cobra a mesma coisa que ele não devolve ponto**.

O seu Selo tem uma parte só, e a mesa consegue apontar o momento em que ela aconteceu. Se você precisa de mais de uma frase para explicar, aquilo virou condição de cena ou de alvo, e isso se compra por feitiço, com a Restrição `Condicional`.

**É Selo ou é `Condicional`**
| É Selo | Vira `Condicional` |
|---|---|
| Bater palma | Bater palma três vezes no ritmo certo |
| Estar enxergando o alvo | Enxergar o alvo sem que ele te enxergue |
| Ter tocado no alvo nesta cena | Ter tocado no alvo e saber o nome dele |
| Gastar o próprio sangue | Gastar sangue de alguém do seu clã |

O Selo pode mudar de forma sem perder a função: se você perde a mão que batia palma, arruma outra coisa que faça o mesmo som.

**Selos da obra**
| Selos de Jujutsu Kaisen | O Selo |
|---|---|
| Nobara (Boneco de Palha) | Martelo e prego na mão. |
| Nobara (Ressonância) | Um pedaço do alvo: sangue, cabelo, um membro. |
| Todo (Boogie Woogie) | Bater palma. Depois que perdeu a mão, um vibraslap: o som mudou de fonte, o Selo continuou. |
| Inumaki (Fala Amaldiçoada) | Falar o comando, e a garganta cobra o preço. |
| Megumi (Dez Sombras) | Um sinal de mão para cada shikigami. |
| Mahito (Transfiguração Ociosa) | Tocar no alvo. |
| Choso (Manipulação de Sangue) | Gastar o próprio sangue. |
| Nanami (Proporção) | Mirar o ponto 7:3 do corpo do alvo. |

### Passivas

Passiva é o que a sua técnica faz sem você mandar: o efeito que fica ligado enquanto você existe. Cada Passiva tem uma **Classe Passiva**, e é paga com **espaços de feitiço conhecido**. Você abre mão de saber mais feitiços para que a técnica trabalhe sozinha.

**Passivas**
| Classe Passiva | Custa | Libera no nível | O que cabe |
|---|---|---|---|
| **Livre** | nada | 1 | Ficção pura. Não rola dado, não muda número, não faz ninguém rolar. Todo personagem tem uma. |
| **1** | 1 espaço | 1 | Efeito pequeno, condicional, ou de informação. |
| **2** | 2 espaços | 7 | Efeito reativo, com limite de uso por cena ou por descanso. |
| **3** | 3 espaços | 13 | Permanente. Muda como você joga. |

Máximo de cinco Passivas pagas. A Passiva Livre não conta.

**Resistência**, quando alguma coisa aqui usar a palavra, quer dizer sempre a mesma coisa: o dano daquele tipo cai pela metade, antes de qualquer outra conta. Ela é sempre presa a um tipo, e não existe resistência a tudo.

#### Passiva Livre

Todo personagem começa com uma Passiva Livre, de graça. Ela não rola dado, não muda número nenhum e não faz ninguém rolar. Dentro desses limites, use quando e quanto quiser.

Você enxerga emoção como cor. Planta murcha quando você passa. Você nunca se perde. Seu reflexo aparece um segundo atrasado. Metal fica frio na sua mão.

A Livre entrega o dado cru: você vê o medo na cor de alguém, e descobrir o motivo do medo continua sendo trabalho seu.

#### Limites

- Bônus de dano ou acerto que vale o tempo todo, sem condição.
- Uma ação a mais por rodada.
- Imunidade completa a um tipo de dano ou condição.
- Cura sem limite de uso por descanso.
- Redução de Dano passiva, ou seja, descontar um número fixo de todo golpe que te acerta. Resistência presa a um tipo continua valendo, e é o que a `Escama` faz.

#### Lista

**Lista**
| Passiva | Classe Passiva | O que faz |
|---|---|---|
| `Leitura` | 1 | Você identifica a Classe e a Forma de qualquer feitiço conjurado a até 18 m. |
| `Instinto` | 1 | Você não é pego de surpresa enquanto estiver acordado. |
| `Raiz` | 1 | Você não é movido à força nem derrubado contra a sua vontade. |
| `Mão Firme` | 1 | Você não perde concentração nem carga por dano de 10 ou menos. |
| `Farejador` | 1 | Você sente se alguém conjurou num lugar nas últimas 24 horas, e de que Classe. |
| `Aviso` | 1 | Você sabe qual foi o último feitiço que um inimigo à vista usou. |
| `Fluxo` | 2 | Ao conjurar Classe 3 ou mais, você ganha 2 × Classe de vida temporária. |
| `Recomposição` | 2 | Uma vez por descanso curto, gasta a ação e recupera 5 × a sua maior Classe. |
| `Segunda Natureza` | 2 | Uma vez por dia, conjura um feitiço de Classe até metade da sua maior sem gastar PE. |
| `Eco` | 2 | Quando você derruba um inimigo com feitiço, o próximo feitiço da cena custa metade. |
| `Costura` | 2 | Uma vez por cena, um aliado a até 9 m que cairia a 0 fica com 1. |
| `Contramedida` | 2 | Como Reação, quando alguém conjura a até 9 m, gasta PE e sobe em 2 a CD daquele feitiço. |
| `Peso da Presença` | 2 | Inimigos fracos que começam o turno a até 6 m fazem Teste de Resistência ou ficam `Amedrontados` por uma rodada. |
| `Escama` | 3 | Escolha um tipo de dano que a sua Regra justifique. Você tem resistência a ele: todo dano daquele tipo cai pela metade. |
| `Afinidade` | 3 | Escolha um tema da sua Regra. Feitiços daquele tema ignoram cobertura leve e resistência ao seu tipo de dano. |
| `Reserva Profunda` | 3 | Seu PE máximo sobe em 3 × a sua maior Classe. |
| `Regra Própria` | 1 a 3 | Sua técnica impõe uma regra ao mundo. Ver abaixo. |
| `Passiva Própria` | 1 a 3 | Qualquer outra coisa, montada com o mestre na escala da tabela acima. |

#### Regra Própria

Algumas técnicas funcionam impondo uma regra ao mundo: julgamento, aposta, contrato, dívida, sorte. Para essas existe a `Regra Própria`, escrita junto com o mestre antes de a campanha começar, obedecendo cinco travas:

- Uma frase.
- Verificável: a mesa aponta o momento em que ela disparou.
- Simétrica: vale contra você nas mesmas condições.
- Sem dano direto: gera recurso, condição ou obrigação.
- Com limite por cena.

**Só a `Regra Própria` pode ser comprada em Classe Passiva 1 desde o nível 1.** Quando os níveis liberarem as alturas maiores, ela sobe para 2 e 3 pagando só a diferença de espaços.

*"Quem me atacar sabendo que eu não revidei acumula uma Dívida. Cobro uma por cena."*
*"Quando eu aposto e ganho, meu próximo teste na cena tem vantagem. Uma vez por cena."*
*"Duas coisas que eu tocar na mesma rodada ficam ligadas até o fim da cena."*

## Fundamentos prontos

Três Fundamentos completos, prontos para usar como estão ou para servir de régua na hora de escrever o seu. O primeiro deles, a **Régua**, volta em *Criando feitiços* para montar o primeiro feitiço do capítulo.

Os três param onde a criação de personagem para: Descrição, Regra, Famílias, Selo e, quando a técnica pede, a Passiva. Liberação Máxima e Técnica Máxima não aparecem aqui porque só chegam nos níveis 10 e 17, e são escritas na hora.

### Régua

**Ficha de feitiço**
| | |
|---|---|
| **Descrição** | Ele mede. Aponta o dedo, calcula a distância até o alvo e cobra essa distância do corpo do outro. Nada disso dá para ver: a mão dele fica parada, e o corte aparece sozinho no outro lado. Quanto mais longe, mais fundo. Tipo de dano: corte. |
| **Regra** | *"Medir a distância entre dois pontos e cobrar por ela."* |
| **Livres** | Mira · Alcance |
| **Fechadas** | Área · Amparo · Auxiliares |
| **Selo** | Apontar com o dedo e falar o nome do alvo em voz alta. |

### Sentença

**Ficha de feitiço**
| | |
|---|---|
| **Descrição** | Ela só registra. Cada coisa que acontece perto dela fica anotada em algum lugar que ninguém vê, e uma hora a conta fecha. O que ela cobra quando fecha é o que a pessoa devia. Tipo de dano: psíquico. |
| **Regra** | *"Registrar o que foi feito e cobrar quando fechar a conta."* |
| **Livres** | Marca · Castigo |
| **Fechadas** | Área · Alcance · Amparo |
| **Selo** | Ter visto o ato com os próprios olhos. |
| **Passiva** | `Regra Própria` (Classe Passiva 3): *"quem ferir alguém desarmado na minha frente acumula uma Dívida. Posso cobrar uma Dívida por cena: o alvo tem desvantagem no próximo teste e eu tenho vantagem contra ele até o fim do meu próximo turno."* |

### Banca

**Ficha de feitiço**
| | |
|---|---|
| **Descrição** | Ele joga. A técnica sai da mão como aposta: moeda no ar, carta virada, um dado rolando em algum lugar que ninguém vê. O golpe em si paga pouco, porque o prêmio de verdade fica guardado com a banca, e a banca fecha a conta quando ele ganha. Tipo de dano: impacto. |
| **Regra** | *"Apostar contra a sorte e cobrar o prêmio."* |
| **Livres** | Auxiliares · Marca |
| **Fechadas** | Área · Alcance · Castigo |
| **Selo** | Falar a aposta em voz alta. |
| **Passiva** | `Regra Própria` (Classe Passiva 1 na criação, subindo com os níveis): *"quando eu aposto e ganho, meu próximo teste na cena tem vantagem. Uma vez por cena."* |

O orçamento da Banca mora na Passiva. Os feitiços são fracos de propósito: a técnica guarda o poder para quando a conta fecha, e a `Regra Própria` é onde ela fecha.

## Criando feitiços

Com o Fundamento escrito, os feitiços saem dele. Montar um feitiço é uma conta curta: escolher o tamanho, escolher como ele sai, gastar os pontos e dar um nome. Esta seção percorre os passos e depois monta um feitiço completo, do zero, para você ver a conta acontecendo.

### Teto de feitiços

Antes de montar o primeiro, veja quantos você tem direito de escrever. A conta é do capítulo 16, *Experiência e Progressão*, e está repetida aqui porque é agora que você precisa dela.

> **Espaços de feitiço conhecido = `2 + (nível ÷ 2)`, arredondando para baixo. Mais um por marco já alcançado.**
> Os marcos são os níveis **6, 10, 14, 18, 22, 26 e 30**.

Na prática, você abre um espaço novo **a cada nível par**, e nos marcos abre dois de uma vez.

**Teto de feitiços**
| Seu nível | 1 | 2 | 5 | 10 | 14 | 20 | 26 | 30 |
|---|---|---|---|---|---|---|---|---|
| **Espaços** | 2 | 3 | 4 | 9 | 12 | 16 | 21 | 24 |

Duas coisas dividem esses espaços com os seus feitiços: cada **Passiva** paga custa de 1 a 3 espaços, e a **Expansão de Domínio** custa 2 ou 3. O resto vira feitiço montado.

Ficam **fora** da conta os feitiços de **Classe 0**, que são contados à parte, e as **Liberações Máximas**, que não ocupam espaço nenhum.

> **Exemplo.** Mei está no nível 10. São 9 espaços: `2 + 5` da conta, mais 2 dos marcos 6 e 10. Ela já gastou 2 numa Passiva de Classe Passiva 2, então tem **7 feitiços montados** na ficha, mais os 3 de Classe 0 e a Liberação Máxima que o nível 10 acabou de dar.

### Passos

1. Escolha a **Classe**, até a maior que o seu nível liberou. Ela define os pontos (3 × Classe), o custo em PE (o mesmo número) e quantas Melhorias e Restrições cabem.
2. Escolha a **Forma**: como o feitiço sai de você. Algumas Formas custam pontos; nenhuma conta no limite de Melhorias.
3. Compre **Melhorias** e, se quiser recuperar pontos, venda **Restrições**.
4. O que sobrar de ponto vira dado: **1 ponto = 1d8 de dano**.
5. Dê um nome e escreva na ficha.

> **Dados de dano = Pontos − Melhorias + Devolução**
> A devolução das Restrições nunca passa do que você gastou em Melhoria: se devolver mais, o excedente some. É por isso que Restrição barateia o feitiço e nunca aumenta o dano dele.

### Exemplo guiado: o primeiro feitiço da Régua

A **Régua** mede distâncias e cobra por elas. As Famílias Livres dela são Mira e Alcance; as Fechadas são Área, Amparo e Auxiliares. O jogador quer o golpe básico da técnica: um corte disparado à distância, que atravesse armadura.

**Passo 1, Classe.** O personagem está no nível 5, então a maior Classe dele é 2. Isso dá **6 pontos**, custo de 6 PE, e os limites da Classe: até 2 Melhorias, até 2 Restrições, devolução máxima de 4.

**Passo 2, Forma.** `Projétil`: 18 m, um alvo, rolagem de acerto. Não custa ponto.

**Passo 3, Melhorias e Restrições.** `Fura` (Mira, `Média`) custaria 2 pontos numa Classe 2, mas Mira é Família Livre da Régua: o desconto de metade da Classe (1) derruba o preço para **1 ponto**. `Precisão` (Mira, `Leve`) custa 1 e fica em 1, porque o desconto nunca leva um preço abaixo de 1. Foram 2 pontos em Melhoria, sobrariam 4. Para recuperar um, ele vende `Parado` (devolve 1): a Régua precisa dos pés no chão para medir, então não se move no turno em que conjura. A devolução paga 1 dos 2 pontos gastos.

**Passo 4, dano.** 6 − 2 + 1 = **5 pontos sobrando: 5d8 de corte**, uma média de 22.

**Passo 5, nome.** Está pronto, e vai para a ficha assim:

**Ficha de feitiço**
| | |
|---|---|
| **Nome** | `Corte Medido` |
| **Classe / Pontos / PE** | 2 · 6 pontos · 6 PE |
| **Forma** | `Projétil` (18 m, um alvo) |
| **Resolve com** | Rolagem de acerto, com +2 da `Precisão` |
| **Melhorias** | `Fura` (−1, Livre) · `Precisão` (−1, Livre) |
| **Restrições** | `Parado` (+1) |
| **Dano** | 5d8 = 22, ignorando até 6 de Redução de Dano (3 × Classe) |
| **Ação** | Padrão |
| **Como é** | Ele para, aponta, diz o nome do alvo, e a distância medida abre no corpo do outro, como um corte de papel do tamanho do caminho. |

> **Erros comuns**
> **Vender Restrição sem Melhoria para pagar.** A devolução some. O `Golpe Cru`, em *Feitiços prontos*, é um exemplo disso.
> **Contar que Restrição vira dado.** Nunca vira: contra um alvo só, 6 pontos continuam sendo o máximo de dados de uma Classe 2, com ou sem Restrição.
> **Empilhar duas Restrições de frequência** (`Uma Vez`, `Condicional`, `Aquecer`, `Dívida`). Não pode, e *Combinações inviáveis* explica a trava.

### Formas

A Forma define quem o feitiço atinge e como ele se resolve. Escolha uma por feitiço.

**Formas**
| Forma | Custa | O que é | Como resolve |
|---|---|---|---|
| `Projétil` | — | 18 m, um alvo | Rolagem de acerto |
| `Toque` | — | 1,5 m, um alvo. `Projétil` com a Restrição `Corpo a Corpo` embutida (devolve `Média`). | Rolagem de acerto |
| `Explosão` | `Leve` | Esfera de raio 3 m, num ponto a até 18 m | Teste de Resistência, metade no sucesso |
| `Aura` | `Leve` | Esfera de raio 3 m centrada em você. `Explosão` com `Corpo a Corpo` embutida (devolve `Média`). | Teste de Resistência, metade no sucesso |
| `Cone` | `Leve` | 4,5 m saindo de você | Teste de Resistência, metade no sucesso |
| `Linha` | `Leve` | 18 m por 1,5 m | Teste de Resistência, metade no sucesso |
| `Cura` | `Média` | Um aliado a até 9 m. Os dados viram cura. | Automático |
| `Apoio` | — | Um aliado a até 9 m. Sem dano. Cada ponto que sobra vira 3 de vida temporária. | Automático |
| `Onda` | `Pesada` | Esfera de raio 3 m centrada em você. A cura ou o apoio pega todos os aliados dentro, sem dividir. | Automático |
| `Efeito` | — | Fora de combate. Sem dano. Ver *Fora de combate*. | Automático |

Trocar rolagem de acerto por Teste de Resistência, ou o contrário, é de graça.

Cada Forma pertence a uma Família: `Explosão`, `Cone` e `Linha` à **Área**; `Cura`, `Apoio` e `Onda` ao **Amparo**. Fundamento com a Família Fechada fica sem essas Formas. `Projétil`, `Toque` e `Efeito` são de todo mundo.

### Escadas

Alcances e tamanhos crescem por degraus fixos. As Melhorias de Alcance e Área (`Longe`, `Maior` e as irmãs) sobem degraus nestas escadas:

**Escadas**
| Escada | Degraus |
|---|---|
| **Alcance** | 1,5 m → 9 m → 18 m → 36 m → 90 m → o que você enxergar |
| **Esfera (raio)** | 3 m → 4,5 m → 6 m → 9 m → 15 m |
| **Cone e Linha** | 4,5 m → 9 m → 18 m → 30 m → 60 m |

O degrau "o que você enxergar" vale para olho nu. Câmera, luneta, espelho e visão emprestada não contam.

Se uma Melhoria subir mais degraus do que a escada tem, ela para no último degrau.

#### Base por Classe

**Base por Classe**
| Forma | Classe 0 | Classes 1 a 5 | Classes 6 e 7 |
|---|---|---|---|
| `Projétil` e `Toque` | 9 m | 18 m | 36 m |
| `Explosão` | raio 3 m, a 9 m | raio 3 m, a 18 m | raio 4,5 m, a 36 m |
| `Cone` | 3 m | 4,5 m | 9 m |
| `Linha` | 9 × 1,5 m | 18 × 1,5 m | 30 × 1,5 m |
| `Cura`, `Apoio` e `Onda` | 4,5 m | 9 m | 18 m |

`Toque` fica em 1,5 m em qualquer Classe.

### Ampliar

Você pode lançar qualquer feitiço que conhece numa Classe maior que a original, até a sua Classe máxima, pagando o PE da Classe nova. Refaça a conta inteira com os números novos: pontos, preços de Melhoria e devoluções de Restrição mudam todos juntos.

**Ampliar**
| `Palma Trovejante` · Classe | Pontos | `Cone` (Leve) | `Derrubado` (Leve) | `Lento` (devolve) | Dano | PE |
|---|---|---|---|---|---|---|
| Classe 2 (original) | 6 | −1 | −1 | +2 | 6d8 = 27 | 6 |
| Classe 3 | 9 | −2 | −2 | +3 | 8d8 = 36 | 9 |
| Classe 5 | 15 | −3 | −3 | +5 | 14d8 = 63 | 15 |

Ampliar aumenta o número e não muda a natureza do feitiço: quem não alcançava o bônus de Controle continua sem alcançar, em Classe nenhuma.

### Cura

A Forma `Cura` custa `Média` e transforma em cura os dados que sobrarem, aplicados automaticamente num aliado a até 9 m. Não existe Liberação Máxima de cura: a linha de baixo é o teto por Classe.

Para pegar mais gente: `Junto` (Amparo) soma um aliado dividindo o efeito, e a Forma `Onda` cura em área sem dividir.

**Cura**
| Classe | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Cura cheia** | 2d8 = 9 | 4d8 = 18 | 6d8 = 27 | 8d8 = 36 | 10d8 = 45 |
| **`Onda` (área)** | 1d8 = 4 | 3d8 = 13 | 4d8 = 18 | 6d8 = 27 | 7d8 = 31 |
| **Dano da mesma Classe** | 13 | 27 | 40 | 54 | 67 |

### Controle

Feitiço que carrega pelo menos uma Melhoria da família **Controle** ganha um bônus quando abre mão de dano de verdade. Comprar a condição e continuar batendo forte não conta: o gatilho é o dano que sobrou no final.

> Dano final até **um quarto do teto** (o teto é 4 × Classe): os efeitos de Controle duram uma rodada a mais.
> **Sem dano nenhum**, ou seja, o feitiço gastou tudo em Controle: além da rodada extra, a CD contra esses efeitos sobe **+2**.

O bônus vale só contra os efeitos de Controle do feitiço. O Teste de Resistência do dano, quando existe, fica como está.

Por exemplo, num Classe 4 o teto é 16 dados: sobrar até 4 dados de dano já dá a rodada extra, e sobrar zero dá também o `+2` na CD.

**Controle**
| Feitiço de Classe 5 · 15 pontos · teto 20 · um quarto = 5 | Dano final | O que ganha |
|---|---|---|
| 15d8 puro, sem Controle | 15d8 | nada |
| `Condição` Leve (−3) | 12d8 | nada: ainda bate como feitiço de dano |
| `Condição` Média (−5) | 10d8 | nada |
| `Condição` Pesada (−8) | 7d8 | nada |
| `Condição` Pesada (−8) · `Condição` Média (−5) | 2d8 | dura uma rodada a mais |
| `Explosão` (−3) · `Cond.` Média (−5) · `Prende` (−5) · `Puxa` (−5) · `Parado` (+3) | 0d8 | uma rodada a mais e CD +2 |

Uma condição sozinha nunca dispara o bônus. Para chegar no primeiro degrau você compra duas peças de Controle, ou uma condição e alguma outra coisa cara. E para o segundo, o feitiço precisa sair sem um único dado de dano.

Falta uma peça nesta história: o feitiço que rompe o limite de dano contra um alvo só. Ela chega no nível 10, e tem seção própria em *Liberação Máxima*.

## Melhorias por família

Sessenta e seis Melhorias, em nove Famílias. O preço de cada uma depende da Classe do feitiço em que ela entra: `Leve` custa metade da Classe, `Média` custa a Classe inteira, `Pesada` custa Classe e meia, sempre arredondando para cima.

Exemplo de leitura: num feitiço de Classe 3, uma `Leve` custa 2 pontos, uma `Média` custa 3 e uma `Pesada` custa 5. Nas suas duas Famílias Livres, tire metade da Classe do preço, com mínimo de 1; nas três Fechadas, não há o que comprar.

### Alcance

Essas Melhorias resolvem distância: o feitiço chega mais longe, ou você se move junto com ele.

**Alcance**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Longe` | `Leve` | Sobe um degrau na escada de alcance. Pode comprar duas vezes. |
| `Muito Longe` | `Média` | Sobe três degraus de uma vez. |
| `Sem Ver` | `Pesada` | Você conjura contra um alvo fora da sua linha de visão, desde que saiba onde ele está. Alcance normal do feitiço. |
| `Passo` | `Leve` | Você anda até 6 m antes ou depois do feitiço, sem provocar ataque de oportunidade. |
| `Empurrão` | `Leve` | Move o alvo até 6 m na direção que você quiser. |
| `Troca` | `Média` | Você e o alvo trocam de lugar. |
| `Perseguir` | `Média` | Se o alvo sair do alcance antes de o feitiço resolver, o feitiço vai atrás. |

### Área

Aqui o feitiço para de mirar uma pessoa só: ele cresce, se divide em vários tiros, ou pula de alvo em alvo.

**Área**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Maior` | `Leve` | Sobe um degrau de tamanho de área. Pode comprar duas vezes. |
| `Muito Maior` | `Pesada` | Sobe três degraus de tamanho de uma vez. |
| `Escolher` | `Média` | Você decide quem, dentro da área, é atingido. |
| `Fica` | `Média` | A área continua ali por 1 minuto. Quem entrar ou começar o turno nela leva metade dos dados. Exige concentração. |
| `Mais Um` | `Leve` | Um alvo a mais. Os dados são divididos entre os alvos. Pode comprar duas vezes. |
| `Rajada` | `Leve` | Divide o feitiço em (Classe + 1) tiros, cada um com sua rolagem de acerto, distribuídos como você quiser. |
| `Salto` | `Média` | Depois do primeiro alvo, pula para o inimigo mais perto a até 9 m com metade dos dados. |
| `Contorno` | `Leve` | A área faz curva. Ignora cobertura e dobra esquinas. |

### Mira

Garantem o acerto: menos chance de errar, mais chance de atravessar a defesa do outro.

**Mira**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Precisão` | `Leve` | +2 na rolagem de acerto, ou +2 na CD do Teste de Resistência. |
| `Certeiro` | `Média` | Sem rolagem de acerto. O alvo ainda faz o Teste de Resistência para metade. |
| `Inescapável` | `Média` | Sem acerto e sem Teste de Resistência: o dano é automático. Este feitiço não pode ter mais nenhuma peça, nem Melhoria nem Restrição, e não pode ser uma Liberação Máxima. |
| `Fura` | `Média` | Ignora até 3 × Classe de Redução de Dano. O que passar disso continua valendo. |
| `Corrói` | `Pesada` | Resistência ao seu tipo de dano deixa de valer neste feitiço. Só pode ser comprada se Mira for uma das suas Famílias Livres. |
| `Sem Cobertura` | `Leve` | Cobertura leve e meia cobertura não atrapalham. |
| `De Novo` | `Média` | Se você errar, rola de novo. Uma vez por cena. |
| `Toca a Alma` | `Leve` | Só da Classe 3 em diante, e só para Fundamento cuja Regra encosta em alma, mente ou conceito. Os dados de dano deste feitiço viram dano na alma, e você fica com metade deles, arredondando para baixo. Não entra numa Liberação Máxima. A régua do dano na alma está no capítulo 4, *Dano, Condições e Cobertura*. |

> **Imunidade.** Nenhuma Melhoria fura imunidade. Quem quiser isso monta uma Passiva de `Regra Própria` com o mestre, com limite de uma vez por cena.

### Controle

O inimigo sai da luta sem cair morto: no chão, preso, ou lutando contra o próprio terreno.

**Controle**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Condição` | o nível dela | Aplica uma das catorze condições. O preço é o nível dela (`Leve`, `Média` ou `Pesada`), na tabela logo abaixo. Dura uma rodada. As de nível `Pesada` dão Teste de Resistência no fim de cada turno do alvo, e cabe só uma delas por feitiço. |
| `Terreno` | `Leve` | A área vira terreno difícil, ou fica obscurecida, por uma rodada. |
| `Anteparo` | `Média` | Deixa uma parede ou escudo com 10 × Classe de pontos de vida, por 1 minuto. |
| `Prende` | `Média` | O alvo não sai do lugar até o fim do próximo turno dele. Ele pode gastar a ação para tentar um Teste de Resistência e se soltar. |
| `Cerca` | `Leve` | O alvo não consegue se aproximar de você até o fim do próximo turno dele. |
| `Puxa` | `Média` | Todo mundo na área é puxado 6 m na direção do centro. |
| `Desarma o Feitiço` | `Média` | Cancela um efeito contínuo ou uma barreira de Classe igual ou menor que a sua. |

### Condições

São catorze, e cada uma tem um **nível**: `Leve`, `Média` ou `Pesada`. O nível faz duas coisas ao mesmo tempo. Ele é o **preço** da Melhoria `Condição` que aplica ela, e é o que custa em energia para **tirar** ela de alguém (1 ponto por nível). Uma condição dura uma rodada.

Cada condição custa o que ela vale. `Impedido` e `Surdo` pesam coisas muito diferentes numa luta.

Numa Classe 5, aplicar uma `Leve` custa 3 pontos, uma `Média` custa 5 e uma `Pesada` custa 8.

**Condições `Leve`**
| Nível `Leve` | O que faz |
|---|---|
| `Lento` | Deslocamento pela metade, e sem Ação Bônus. |
| `Incapacitado` | Você não pode Bloquear, e todo ataque corpo a corpo contra você é crítico. |
| `Derrubado` | No chão. Só se move rastejando, desvantagem nos seus ataques, e quem ataca de até 1,5 m tem vantagem; de longe, desvantagem. |
| `Agarrado` | Deslocamento 0. Acaba se quem agarrou ficar `Incapacitado`, ou se algo te tirar do alcance dele. |
| `Desarmado` | A sua arma está no chão ou na mão de outro. Você bate desarmado até pegar de volta. |
| `Surdo` | Não ouve. Falha automática em teste que precise de audição, e −2 na iniciativa. |

**Condições `Média`**
| Nível `Média` | O que faz |
|---|---|
| `Calado` | Você não conjura. Nada que precise de voz, gesto ou Selo sai. |
| `Enfeitiçado` | Você não ataca quem enfeitiçou nem mira efeito nocivo nele, e ele tem vantagem em teste social contra você. |

**Condições `Pesada`**
| Nível `Pesada` | O que faz |
|---|---|
| `Petrificado` | Virou pedra. `Incapacitado`, deslocamento 0, sem perceber o que está em volta, vantagem para quem te ataca, e resistência a todo dano. |
| `Impedido` | Deslocamento 0, desvantagem nos seus ataques e no Teste de Resistência Físico, e vantagem para quem te ataca. |
| `Cego` | Não enxerga. Falha automática em teste que precise de vista, desvantagem nos seus ataques, vantagem para quem te ataca. |
| `Amedrontado` | Desvantagem em ataque e teste enquanto enxergar a fonte do medo, e você não se aproxima dela de vontade própria. |
| `Envenenado` | Desvantagem nos seus ataques e em todo teste de perícia. |
| `Atordoado` | Você perde a Ação Padrão e não usa reação. Quem tem mais de uma Ação Padrão no turno perde só UMA delas, e guarda as demais. |

**`Atordoado` e `Incapacitado` atacam eixos diferentes, e não se empilham.** Um tira ação e o outro tira defesa, e o capítulo 4, *Dano, Condições e Cobertura*, abre a diferença.

E o `Atordoado` cobra uma Ação Padrão só, e nunca o turno inteiro: quem age mais de uma vez por rodada perde uma das ações e guarda as outras.

> **Três coisas que não são condição aqui.**
> `Inconsciente` é cair morrendo, e tem regra própria no capítulo 1, *Como Jogar*: não é efeito de uma rodada.
> Exaustão é relógio de descanso, e a Melhoria `Condição` não alcança ela.
> `Invisível` é benefício: comprar para aplicar num inimigo é pagar para ajudar ele.

### Auxiliares

Pequenos empurrões de sorte, pros dois lados da mesa: números em cima de alguém. Em feitiço de dano valem contra o alvo; nas Formas de Amparo, valem no aliado.

**Auxiliares**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Impulso` | `Leve` | O alvo tem vantagem no próximo teste dele, até o fim do próximo turno. |
| `Trava` | `Leve` | O alvo tem desvantagem no próximo ataque dele. |
| `Abre Ferida` | `Leve` | O alvo fica com −2 em Testes de Resistência até o fim do próximo turno dele. |
| `Sobrecarga` | `Leve` | Até o fim do próximo turno do alvo, o feitiço dele custa o dobro de energia e sai com a CD 2 menor. |
| `Firmeza` | `Média` | O alvo tem vantagem no próximo Teste de Resistência dele. |
| `Guarda` | `Média` | Até o fim do próximo turno, o alvo tem +2 de defesa. |
| `Pressa` | `Média` | O alvo ganha +6 m de deslocamento e não provoca ataques de oportunidade até o fim do próximo turno. |
| `Enfraquece` | `Média` | O dano do alvo cai um quarto até o fim do próximo turno dele. |
| `Ecoa` | `Média` | O próximo ataque de um aliado contra o alvo tem vantagem. |

### Castigo

O dano que continua doendo depois do golpe: queima que volta, corte que piora contra quem já está machucado.

**Castigo**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Queima` | `Média` | Metade dos dados de novo, no começo do próximo turno do alvo. |
| `Acúmulo` | `Média` | +1 dado por rodada seguida usando este feitiço no mesmo alvo. Para de somar em +3. |
| `Remate` | `Média` | +25% de dano contra alvo abaixo de metade da vida. Não entra num feitiço que tenha uma `Condicional` ligada à vida do alvo. |
| `Estilhaço` | `Leve` | Em crítico, ou quando o alvo erra o Teste de Resistência por 5 ou mais, metade dos dados respinga em quem estiver do lado. |
| `Quebra Coisa` | `Leve` | Dano dobrado contra barreiras, objetos e estruturas. |
| `Rasga Escudo` | `Média` | O dano ignora `vida temporária` e barreiras: bate direto na vida. |
| `Sem Cura` | `Média` | O alvo não pode receber cura até o fim do próximo turno dele. |

### Tempo

Aqui você compra o momento do feitiço: mais rápido que o normal, disparado escondido, ou fora da sua vez.

**Tempo**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Rápido` | `Pesada` | Custa Ação Bônus em vez de Ação Padrão. Não entra no mesmo feitiço que `Reação`. |
| `Reação` | `Pesada` | Você conjura como Reação, a um gatilho que você declara quando monta o feitiço. Não entra no mesmo feitiço que `Rápido`. |
| `Armado` | `Leve` | Deixa o feitiço pronto e dispara depois, na mesma cena. Disparar ainda gasta ação. |
| `Silencioso` | `Leve` | Sem gesto, sem palavra. Ninguém percebe que você conjurou. |
| `Adianta` | `Média` | Se você conjurar antes de qualquer inimigo agir na rodada, +2 na CD. |
| `Segura` | `Leve` | Você pode adiar o efeito por até uma rodada e disparar no seu próximo turno, de graça. |

> Se você conjurar um feitiço como Ação Bônus ou Reação, o único outro feitiço que cabe naquele turno é de **Classe 0**.

### Marca

O que sobra depois que o feitiço passou: uma marca no alvo, um fio que puxa energia de volta pra você.

**Marca**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Marca` | `Leve` | O alvo fica marcado até o fim do seu próximo turno. **Você** tem vantagem no seu próximo ataque contra ele. Só você. |
| `Rastro` | `Leve` | Você sabe onde o alvo está por 1 hora, desde que ele esteja no mesmo plano. |
| `Sugar` | `Média` | Você recupera um quarto do dano causado, até no máximo 5 × Classe. |
| `Isca` | `Leve` | Até o fim do próximo turno do alvo, ele tem desvantagem em qualquer ataque que não mire você. |
| `Cobrança` | `Média` | Se o alvo cair nesta cena, o seu próximo feitiço custa metade. |
| `Aviso` | `Leve` | Você sabe qual foi o último feitiço que o alvo usou e de que Classe ele era. |

### Amparo

A mão que segura quem caiu. Funcionam com as Formas `Cura`, `Apoio` e `Onda` e, quando fizer sentido, em feitiço de dano que atinja aliados.

**Amparo**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Limpa` | `Média` | Remove de um aliado uma condição de nível `Leve` ou `Média`. |
| `Limpa Fundo` | `Pesada` | Remove de um aliado uma condição de qualquer nível. |
| `Levanta` | `Pesada` | Um aliado caído em 0 pontos de vida volta com 5 × Classe. Uma vez por cena. |
| `Divide` | `Média` | Um aliado a até 9 m passa a receber metade do dano que você receberia, até o fim do próximo turno. Você escolhe na hora de conjurar. |
| `Junto` | `Leve` | A cura ou o apoio pega um aliado a mais. O efeito é dividido entre eles. Pode comprar duas vezes. |
| `Reserva` | `Média` | A cura fica guardada no aliado e é usada sozinha quando ele cair abaixo da metade da vida. Dura até o fim da cena. |
| `Remenda` | `Pesada` | Devolve 5 × Classe de Integridade a um aliado, e com ela a vida máxima que tinha sido derrubada. Uma vez por cena. |

### Fora de família

**Fora de família**
| Melhoria | Custo | O que faz |
|---|---|---|
| `Efeito Próprio` | o mestre decide | Uma mecânica que não existe em lugar nenhum desta lista. Um deslocamento junto com o dano, um efeito que só funciona em superfície molhada, o que for. Um por feitiço, combinado antes da sessão e nunca no meio dela. Não pertence a nenhuma Família, então Família Fechada não bloqueia. |

Do lado das Restrições, a equivalente dela se chama `Restrição Própria`, no fim de *As Restrições*.

## Restrições

Restrição é a desvantagem que você aceita em troca de pontos: o preço que a mesa vê o personagem pagando antes do golpe sair, um turno parado, um corte na própria pele, uma condição que sobra pra depois. Um feitiço carrega no máximo duas, e a devolução total não passa de **2 × Classe**. O que a Restrição devolve serve só para pagar Melhoria: se devolver mais do que você gastou, o excedente se perde. Restrição nunca vira dano.

Uma Restrição devolve `Leve` ou `Média`, nunca `Pesada`. Duas `Média` já batem no teto de devolução da Classe, então o catálogo inteiro cabe dentro do fecho.

**Restrições**
| Restrição | Devolve | O que muda |
|---|---|---|
| `Corpo a Corpo` | `Média` | `Projétil` vira `Toque` (1,5 m). `Explosão` vira `Aura`, centrada em você. `Cone` e `Linha` já saem de você, então não podem pegar esta. |
| `Lento` | `Média` | Custa a rodada inteira (Ação Completa): você não se move, não usa ação bônus e não faz mais nada naquele turno. |
| `Parado` | `Leve` | Você não se move no turno em que conjura. A ação bônus continua sua. |
| `Gesto` | `Leve` | Precisa das duas mãos livres e de falar em voz audível. |
| `Sangra` | `Média` | Você toma 2 × Classe de dano que nada reduz. |
| `Recuo` | `Leve` ou `Média` | Você fica com uma condição até o fim do seu próximo turno. Ela devolve o nível dela: uma condição `Leve` devolve `Leve`, uma `Média` devolve `Média`. Nível `Pesada` não entra, porque Restrição nunca devolve `Pesada`. |
| `Carregar` | `Média` | Você gasta um turno carregando o feitiço antes de disparar. Se tomar dano nesse meio-tempo, faz um Teste de Resistência de Espírito (CD 10, ou metade do dano, o que for maior) para manter. Se falhar, perde o feitiço. Carregar não é concentração: o feitiço ainda não saiu. |
| `Tudo ou Nada` | `Leve` | Quem passa no Teste de Resistência não toma nada, em vez de tomar metade. Só em feitiços de Teste de Resistência. |
| `Uma Vez` | `Leve` | Uma vez por cena. |
| `Condicional` | `Leve` ou `Média` | Só funciona quando uma condição de cena ou de alvo, escrita na ficha, é verdadeira: no escuro, marcado por você, abaixo de metade da vida, perto de água corrente. Falha em menos de uma cena a cada três: devolve `Leve`. Falha na maioria das cenas: devolve `Média`. |
| `Fraqueza` | `Leve` ou `Média` | Depois de usar, você fica com desvantagem num dos quatro Testes de Resistência, escolhido na montagem, até o fim da cena. Vigor ou Intelecto: `Leve`. Físico ou Espírito: `Média`. |
| `Frágil` | `Leve` | Se você tomar dano antes do seu próximo turno, o efeito do feitiço acaba na hora. Só serve em feitiço que deixa algo durando. |
| `Barulho` | `Leve` | Todo mundo num raio de 90 m ouve, e sabe de onde veio. |
| `Assinatura` | `Leve` | O feitiço deixa uma marca visível que dura 1 hora e aponta para você. |
| `Aquecer` | `Leve` | Não pode ser usado na primeira rodada do combate. |
| `Dívida` | `Média` | Depois de usar, o próximo feitiço que você conjurar nesta cena custa o dobro de energia. |
| `Peso Morto` | `Leve` | Seu deslocamento cai pela metade até o fim do próximo turno. |
| `Sem Volta` | `Média` | Se o feitiço não acertar ninguém, você não conjura nada no seu próximo turno. |

### Restrição Própria

Se a desvantagem que você imaginou não está na lista, escreva ela. Você propõe a desvantagem e o mestre define quanto ela devolve, do mesmo jeito que o `Efeito Próprio` funciona do outro lado.

**Restrição Própria**
| Restrição | Devolve | O que muda |
|---|---|---|
| `Restrição Própria` | `Leve` ou `Média` | Uma desvantagem que não existe nesta lista. Escrita com o mestre antes da sessão, nunca no meio dela, e vale só para o feitiço onde nasceu. Conta no limite de duas Restrições e obedece as mesmas travas de todas as outras. |

**Quanto ela devolve.** A pergunta é uma só: em quantas cenas isso vai realmente atrapalhar?

- Atrapalha em menos de uma cena a cada três: `Leve`.
- Atrapalha na metade das cenas ou mais: `Média`.
- Não dá para imaginar uma cena em que atrapalhe: **não devolve nada**, e não vale como Restrição.

Nenhuma Restrição do capítulo devolve `Pesada`, e a Própria também não. Duas `Média` já batem exatamente no teto de devolução da Classe (2 × Classe), então uma `Pesada` estouraria o fecho do sistema. Se a dor que você escreveu parece valer mais que uma `Média`, ela provavelmente são duas Restrições disfarçadas de uma. Separe.

> **Na dúvida, para que lado errar.**
> `Efeito Próprio` na dúvida é `Pesada`. `Restrição Própria` na dúvida é `Leve`.

As travas valem igual: a Própria precisa ser uma coisa que a mesa consegue apontar acontecendo, não pode cobrar o que a outra Restrição do feitiço já cobra, e não pode repetir o que o seu Selo já obriga. Se ela limita **quando** o feitiço sai, ela conta como Restrição de frequência para a regra abaixo.

### Combinações inviáveis

Restrição precisa ser uma coisa que a mesa consegue apontar acontecendo, e algumas combinações são proibidas de saída.

**As suas duas Restrições não podem ser as duas de frequência.** `Uma Vez`, `Condicional`, `Aquecer`, `Dívida` e qualquer `Restrição Própria` que faça a mesma coisa limitam quando o feitiço sai; escolha no máximo uma delas. Duas juntas devolvem o orçamento inteiro em troca de um feitiço que quase nunca é conjurado, e que, quando sai, é sempre o pico.

**Duas Restrições não podem cobrar a mesma coisa:** dois turnos de preparo, duas condições no seu corpo, dois jeitos de te entregar. Se as duas doem no mesmo momento, a segunda não devolve nada.

**Restrição que o seu Selo já obriga não devolve ponto.** Você já carrega o Selo de qualquer jeito, e vender a mesma dor duas vezes não vale ponto novo.

Depois de três sessões, o mestre revisa as Restrições em jogo. As que nunca atrapalharam são trocadas.

## Fora de combate

Nem tudo que a sua técnica faz precisa de rolagem ou de montagem. Fora de combate, duas regras cobrem o resto: o Uso Livre, para coisa pequena, e a Forma `Efeito`, para coisa grande.

### Uso Livre

De graça e sem rolar nada, você faz qualquer coisa que caiba na sua Regra e passe nos três testes:

1. Não rola dado e não faz ninguém rolar.
2. Não tira nem dá vida, não aplica condição, não mexe em rolagem de ninguém e não move nada que resista.
3. A escala cabe na Classe 0 da tabela de `Efeito`, logo abaixo: coisa de mão.

Falhou em um dos três, é feitiço: monte e pague. Passou nos três, funciona, mesmo que resolva a cena.

A régua geral é essa: **perceber é Livre, interferir é feitiço**. E o que você percebe vem cru: a cor do medo aparece, o motivo continua por sua conta.

**Uso Livre**
| Uso Livre | Vira feitiço |
|---|---|
| Aquecer uma xícara | Aquecer uma sala inteira |
| Marcar uma parede | Marcar uma pessoa |
| Saber de onde vem o vento | Saber onde está uma pessoa |
| Iluminar um corredor | Cegar quem está no corredor |
| Ver a cor da emoção de alguém | Saber o que a pessoa vai fazer |
| Fazer uma folha cair mais devagar | Fazer uma pessoa cair mais devagar |
| Abafar o som dos seus passos | Abafar o som de uma sala |
| Achar a fechadura no escuro | Abrir a fechadura sem chave |
| Saber se mexeram num objeto seu | Saber quem mexeu |
| Estabilizar a própria mão | Estabilizar a mão de outra pessoa |

### Forma Efeito

Quando a coisa é grande o bastante para mudar uma cena, monte um feitiço com a Forma `Efeito`. Ele não causa dano e não rola dado: a Classe define sozinha o que o efeito alcança e por quanto tempo dura, pela tabela abaixo.

Num feitiço de `Efeito`, os pontos da Classe servem só para comprar Melhorias. Ponto que sobrar não vira nada, porque a escala já está paga pela Classe.

**Forma Efeito**
| Classe | O que cabe | Quanto dura |
|---|---|---|
| **0** | Coisa de mão: acender uma vela, trancar uma porta, marcar um objeto. | até você desfazer |
| **1** | Uma pessoa, um objeto pequeno, um cômodo apertado. | um minuto |
| **2** | Um cômodo grande, uma parede, um carro, meia dúzia de pessoas. | dez minutos |
| **3** | Uma casa, um quarteirão, uma dúzia de pessoas. | uma hora |
| **4** | Um prédio, uma rua inteira, uma multidão. | um dia |
| **5** | Um bairro, uma noite inteira, o clima do lugar. Um prédio dormindo ao mesmo tempo, um rio parando de correr, uma ponte que não deixa ninguém passar. | uma semana |
| **Máxima** | Uma cidade, uma coisa que vira notícia. Todo mundo esquecendo um nome, um bairro de onde ninguém sai, uma noite que não amanhece. | até alguém desfazer |

Melhorias funcionam normalmente: `Longe` e `Maior` sobem alcance e escala, `Fica` estende a duração para o degrau seguinte da tabela, `Silencioso` esconde a conjuração.

Feitiço de `Efeito` custa PE igual a qualquer outro e ocupa espaço na sua lista.

> **Exemplo.** `Hora Morta` · Classe 3 · `Efeito` · `Longe` (−2)
> Um quarteirão inteiro para de fazer barulho por uma hora. Portas não rangem, tiro não estala, ninguém grita alto o bastante para ser ouvido de fora.
> Custa 9 de PE.

## Liberação Máxima

No nível 10, o personagem aprende a romper o próprio limite. **Só a Liberação Máxima passa dos pontos da Classe em dano contra um alvo só.** É o pico de dano que a ficha alcança, e por isso ela é contada: você só tem as que os níveis deram.

Liberação não se improvisa. Ela é escrita antes da sessão, montada como qualquer feitiço, e fica anotada na ficha com nome próprio.

> **Liberação Máxima**
> Você ganha uma no **nível 10**, outra no **20** e outra no **30**.
> Cada uma é um feitiço de **Classe 3 ou mais**, montado normalmente, que **não ocupa espaço** na sua lista de feitiços conhecidos.
> **+Classe em dados de dano** em cima do que a montagem der. Numa Classe 5, +5d8.
> Custa a rodada inteira e **+50% de PE**, arredondando para cima.
> Escolha o preço na hora de disparar:
> **Vazio**: você não conjura nada no seu próximo turno.
> **Sangue**: você toma 3 × Classe de dano que nada reduz.
> **Peso**: você fica `Lento` e com desvantagem em Testes de Resistência até o fim do seu próximo turno.
> Não serve para cura, e a Técnica Máxima não é uma Liberação.

Fora isso, ela é um feitiço como os outros: aceita Melhorias e Restrições dentro dos limites da Classe, obedece a Regra e as Famílias Fechadas, e pode ser Ampliada. Ao subir de nível, você pode reescrevê-la do zero, como qualquer feitiço.

> **Exemplo.** `Golpe do Voto` · Liberação Máxima · Classe 5 · `Projétil`
> Sem Melhoria e sem Restrição: os 15 pontos viram 15d8, e a Liberação soma +5d8.
> **20d8 = 90 de dano**, o pico do nível 20.
> PE: 15 + 50% = 22,5, arredondando para cima: **23**.
> Rodada inteira, mais o preço escolhido na hora.

## Técnica Máxima

No nível 17, a técnica ganha o golpe que carrega o nome dela. O dano da Técnica Máxima é **fixo**, definido pela sua faixa de nível, e nenhum ponto compra dado a mais. O que você monta é a Forma e as Melhorias que vestem esse dano.

**Técnica Máxima**
| Nível | Dano (fixo) | Pontos de montagem | PE |
|---|---|---|---|
| **17 a 20** | 24d8 = 108 | 8 | 25 |
| **21 a 25** | 28d8 = 126 | 8 | 30 |
| **26 a 30** | 32d8 = 144 | 12 | 35 |

> **Três números, três papéis.**
> **O dano é fixo.** Os 24d8 da faixa 17 a 20 já vêm prontos: você não compra dado, não vende dado, e Restrição não entra aqui.
> **Os pontos de montagem compram só a Forma e as Melhorias.** São um orçamento à parte, gasto nos preços da sua **maior Classe**. Na faixa 17 a 20, isso significa preços de Classe 5: `Leve` 3, `Média` 5, `Pesada` 8. Ponto de montagem que sobrar se perde, e não vira dado.
> **O PE tem fórmula própria.** A Técnica Máxima não tem Classe, então não custa 3 × Classe como um feitiço: custa **5 × a sua maior Classe**, ou seja, 25, 30 e 35 PE por faixa.

### Montagem

1. Escolha a **Forma**. `Projétil` e `Toque` são de graça; as outras custam o preço normal delas, pago do orçamento de montagem.
2. Gaste o resto do orçamento em **Melhorias**, nos preços da sua maior Classe. Melhoria que escala com Classe, como `Fura`, que ignora 3 × Classe de RD, também usa a sua maior Classe.
3. Dê um nome e escreva na ficha. Como a Liberação, a Técnica Máxima não se improvisa na mesa.

Custa **a rodada inteira** e 5 × a sua maior Classe de PE. Depois de usar, você só usa de novo depois do fim do seu **terceiro turno seguinte**.

Ela aceita qualquer Forma. Numa Forma que não causa dano, os dados viram escala pela linha `Máxima` da tabela de `Efeito`, ou viram cura.

**Não aceita Restrição.** Ela também não conta como Liberação Máxima, porque os dados dela já são fixos. Quem passa no Teste de Resistência reduz o dano em **um quarto**, não pela metade. Famílias Fechadas continuam fechadas.

Se a sua mesa quiser que pese mais, use uma vez por cena em vez do recarregamento por turnos.

> **Exemplo: duas Técnicas Máximas da faixa 17 a 20.**
> `O Fim da Linha`: Forma `Linha` (`Leve` na Classe 5: 3 pontos) + `Muito Longe` (`Média`: 5 pontos) = 8 dos 8 pontos de montagem. A linha sobe da base de 18 m até o fim da escada: 60 m. **24d8 = 108 de dano** em tudo na linha. Rodada inteira, 25 de PE.
> `Ponto Final`: `Projétil` (grátis) + `Fura` (`Média`: 5 pontos) = 5 dos 8; os 3 que sobram se perdem. **24d8 = 108**, ignorando 15 de Redução de Dano (3 × Classe 5). Rodada inteira, 25 de PE.

**Expansão de Domínio e Técnica Máxima são peças separadas.** A Técnica Máxima fecha o topo da sua técnica inata; o domínio estende a mesma técnica sobre o território em volta. Uma técnica feita de domínio continua tendo Técnica Máxima como qualquer outra.

## Expandindo o seu Domínio

Estender a sua técnica sobre o terreno: por alguns instantes, o lugar em volta deixa de obedecer ao mundo e passa a obedecer a você. É o topo do que um feiticeiro faz, e quase nenhum chega lá.

Ela é **comprada**, com espaços de feitiço conhecido, e só abre quando o seu nível e o seu **refino** alcançam os dois mínimos.

> **Refino, em uma linha.**
> O refino é o eixo de controle da sua ficha: quanto da sua energia você não desperdiça. Ele é do capítulo 11, *Aptidões e Refino*, sobe com os seus marcos e vai de 1 a 10.
> Aqui ele é lido em três lugares e nada mais: **o requisito**, **o desconto lá dentro** e **quanto tempo o domínio fica de pé.**

### Degraus

**Degraus**
| Degrau | Custa | Abre em | O Acerto dela |
|---|---|---|---|
| **Incompleta** | 2 espaços | nível 10 e refino 4 | resolve por rolagem, como um feitiço |
| **Completa** | 3 espaços (+1) | nível 14 e refino 5 | **acontece.** Sem rolagem e sem Teste de Resistência |

**A completa exige ter a incompleta**, e paga só a diferença: um espaço a mais, no molde da `Regra Própria`.

**Só a completa fecha barreira.** A incompleta é a técnica derramada no terreno, sem parede em volta.

O teto do feitiço não muda por causa dela, e as duas ficam **fora** da conta de Liberações Máximas.

### Acerto e Efeito

Um domínio tem duas peças, e elas fazem coisas diferentes. Escreva as duas com o mestre antes da campanha, uma frase cada, e as duas precisam caber na **Regra** da sua técnica.

**Acerto e Efeito**
| Peça | A pergunta que ela responde |
|---|---|
| **Acerto** | O que o domínio *garante que acontece* com quem está lá dentro. |
| **Efeito** | O que o domínio *permite você fazer* lá dentro que você não faria fora. |

**O Acerto vem em três formas, e a sua é uma delas:** o que a sua técnica já faz passa a acertar · todos no ambiente recebem alguma coisa · ninguém no ambiente pode fazer alguma coisa.

> **Duas réguas para o Acerto, e elas já existem neste capítulo.**
> **Se o seu Acerto é dano que sempre acerta**, a régua é a Melhoria `Inescapável`: ela custa uma `Média` e proíbe o feitiço de ter qualquer outra peça. Um Acerto que entrega dano garantido paga o mesmo tipo de preço: ele é o feitiço inteiro, e não sobra orçamento para mais nada em cima.
> **Se o seu Acerto é uma regra sobre o ambiente**, a régua são os requisitos da `Regra Própria`: uma frase, verificável, sem número solto. O mestre aponta o momento em que ela vale, e ela vale igual para todo mundo lá dentro, inclusive para você.
> A diferença entre as duas é de que máquina o mestre usa para dizer sim ou não.

### Abrir o Domínio

**Custa a rodada inteira.** A incompleta cobra **6 × a sua maior Classe** de PE; a completa, **8 ×**.

**O Acerto acontece no momento em que você abre**, e de novo no começo de cada turno seu. O relógio é o seu, e não o de quem está lá dentro.

**Lá dentro os seus feitiços ficam mais baratos:** −⅓ do refino de PE na incompleta, **−metade do refino** na completa. **Nenhum feitiço custa menos de 1 PE.**

**Você pode arrastar o domínio.** Se estiver com os pés no chão, gaste o seu deslocamento e a expansão inteira vai junto, e quem está lá dentro não percebe que se mexeu.

**Dura metade do refino em rodadas**, no mínimo uma.

> **A expansão conta como feitiço para a regra de ouro nº 6.**
> Se alguma coisa algum dia baixar o custo de abrir para Ação Bônus, a regra nº 6 passa a valer sozinha: *feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno.* Ou seja, quem abrir domínio em Ação Bônus não lança mais nada de peso naquele turno.

### Barreira e Rescaldo

Só a completa levanta barreira. Por dentro ela **não quebra**: quem está lá dentro está lá dentro. Por fora ela tem 50 × metade do refino de vida, e cair antes da hora é o único jeito de alguém encurtar o seu domínio.

*O mestre pode declarar que uma barreira cede fora dessa conta*: três domínios se atravessando, uma fraqueza que a ficção já estabeleceu, uma cena que pede. É exceção declarada, e não a régua.

> **Rescaldo**
> **Quando o domínio acaba, de qualquer jeito, a sua técnica queima.** Vale igual nos três casos: você desfez por vontade, o tempo correu, ou estilhaçaram a barreira.
> Pelo resto da cena a sua técnica não responde, e você fica com o Classe 0, com o corpo e com o que não for técnica.
> Isso é **preço**: acontece em todo uso, e você já sabia disso quando abriu. É o que impede o domínio de ser mais uma linha da rotação.
> Rescaldo e a exaustão do descanso não somam: são escadas diferentes, e esta aqui tem um degrau só.

### Domínios da obra

**Domínios da obra**
| Quem | Acerto | Efeito |
|---|---|---|
| Megumi *(incompleta)* | todas as invocações dele ganham reforço | invocar todas elas de uma vez |
| Sukuna | clivar e desmantelar acertam | alcança todos no ambiente |
| Mahito | ninguém desvia do toque dele | alcança todos no ambiente |
| Jogo | queima todos no ambiente | amplifica a técnica |
| Dagon | os shikigami dele acertam | amplifica a técnica |
| Yuta | os feitiços das espadas acertam | todas as técnicas copiadas, em forma de espada |
| Gojo | a enxurrada de informação | tocar em alguém para poupá-lo do Acerto |
| Hakari | todos recebem a informação do domínio | o pachinko, e a regeneração que ele paga |
| Higuruma | ninguém no ambiente pode causar dano | o julgamento, e as punições que ele libera |

O Acerto do Megumi *reforça* em vez de *atingir*, e é o que dá para fazer com uma incompleta, cujo Acerto ainda rola. Os completos da lista entregam coisas que não falham.

**Efeito quase nunca é dano.** Alcance, repertório, amplificação, uma mecânica nova, controle sobre quem o Acerto pega. O dano, quando existe, mora no Acerto.

## Regras de ouro

Oito regras seguram o sistema inteiro. Se um feitiço passar pelas oito, ele é legal.

**Regras de ouro**
| # | Regra |
|---|---|
| **1** | Restrição paga Melhoria. Nunca vira dado de dano. O excedente some. |
| **2** | O dano total, somando alvos e repetições, nunca passa de 4 × Classe em dados. Contra um alvo só, feitiço comum para nos pontos da Classe: 4 × Classe num alvo é coisa de Liberação Máxima. |
| **3** | Melhorias: 2 nas Classes 1 e 2, 3 nas Classes 3 e 4, 4 da Classe 5 em diante. Restrições: até 2. A Forma não conta. |
| **4** | Restrição devolve no máximo 2 × Classe. |
| **5** | Liberação Máxima é Classe 3 ou mais, custa a rodada inteira, e você só tem as que o nível deu. |
| **6** | Feitiço em Ação Bônus ou Reação só permite mais um de Classe 0 no turno. |
| **7** | Duas Restrições não podem ser as duas de frequência, nem cobrar a mesma coisa. |
| **8** | Restrição que não atrapalhou em três sessões é trocada. |

Duas notas acompanham as oito: Restrição que o seu Selo já obriga não devolve ponto, e o mestre pode recusar qualquer feitiço, mesmo um que passe em tudo.

## Progressão

**Progressão**
| Nível | O que ganha |
|---|---|
| **1** | Fundamento com três Famílias Fechadas. Dois feitiços de Classe 0 (grátis). Classe 1. Passiva Livre. |
| **5** | Classe 2. Um feitiço de Classe 0 a mais. |
| **7** | Libera Passiva de Classe Passiva 2. |
| **9** | Classe 3. |
| **10** | A primeira Liberação Máxima. |
| **11** | Um feitiço de Classe 0 a mais. |
| **13** | Classe 4. Libera Passiva de Classe Passiva 3. |
| **17** | Classe 5. Técnica Máxima. Um feitiço de Classe 0 a mais. |
| **20** | A segunda Liberação Máxima. |
| **21** | Classe 6. |
| **26** | Classe 7. |
| **30** | A terceira Liberação Máxima. |

O Fundamento manda na Classe, na Liberação Máxima e em quando cada Classe Passiva abre. Quantos feitiços você conhece é conta de *Experiência e Progressão*: a fórmula está resumida em *Criando feitiços*, e a progressão nível a nível mora no capítulo 16, *Experiência e Progressão*.

O que continua valendo aqui: **Passiva é paga com espaços dessa lista**, a **Expansão de Domínio** também, e as **Liberações Máximas ficam de fora**, porque elas não ocupam espaço.

Ao subir de nível você pode reescrever um feitiço que já conhece, do zero. Uma Liberação Máxima conta como feitiço para isso.

Se um feitiço que você conhece deixar de ser legal, por regra nova ou revisão da mesa, você o reescreve de graça na hora, sem gastar a troca de nível.

### Faixa lendária

As Classes 6 e 7 existem, mas a recomendação é que o ganho dos níveis 21 a 30 venha de Passivas que quebram regra, em vez de mais dado.

## Feitiços prontos

Trinta e cinco feitiços montados e conferidos, para usar como estão ou como referência de montagem. Na coluna do meio, **−** é o que a peça custou e **+** é o que ela devolveu.

### Classe 1 · 3 pontos · 3 PE

**Classe 1 · 3 pontos · 3 PE**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Estalo` | `Projétil` | 3d8 = 13 |
| `Chicote` | `Linha` (−1) | 2d8 = 9 numa linha de 18 m |
| `Perfurar` | `Projétil` · `Precisão` (−1) · `Parado` (+1) | 3d8 = 13, +2 no acerto |
| `Golpe Cru` | `Toque` (`Corpo a Corpo` +1), sem Melhoria para pagar | 3d8 = 13 no toque. A devolução some |

### Classe 2 · 6 pontos · 6 PE

**Classe 2 · 6 pontos · 6 PE**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Palma Trovejante` | `Cone` (−1) · `Derrubado` (−1) · `Lento` (+2) | 6d8 = 27 + `Derrubado` por uma rodada |
| `Lança Negra` | `Projétil` · `Fura` (−2) · `Lento` (+2) | 6d8 = 27, fura 6 de RD. O `Lento` pagou a `Fura` inteira |
| `Faísca em Cadeia` | `Projétil` · `Salto` (−2) · `Gesto` (+1) | 5d8 = 22 e 2d8 = 9 no segundo alvo |
| `Sopro` | `Cura` (−2) | cura 4d8 = 18 |
| `Vento a Favor` | `Apoio` · `Impulso` (−1) · `Pressa` (−2) | 9 de vida temporária, vantagem no próximo teste, +6 m sem provocar ataque |

### Classe 3 · 9 pontos · 9 PE

**Classe 3 · 9 pontos · 9 PE**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Marca do Carrasco` | `Projétil` · `Marca` (−2) · `Queima` (−3) · `Uma Vez` (+2) | 6d8 = 27 e 3d8 = 13 no turno seguinte |
| `Domo de Gelo` | `Explosão` (−2) · `Terreno` (−2) · `Maior` (−2) · `Condicional`: no escuro (+2) | 5d8 = 22 num raio de 4,5 m + terreno difícil por uma rodada |
| `Passo Cortante` | `Toque` (`Corpo a Corpo` +3) · `Passo` (−2) · `Precisão` (−2) | 8d8 = 36 no toque, anda 6 m, +2 no acerto |
| `Costura` | `Cura` (−3) · `Limpa` (−3) · `Gesto` (+2) | cura 5d8 = 22 e tira uma condição de nível `Leve` ou `Média` |
| `Rede` | `Explosão` (−2) · `Atordoado` (−5) · `Terreno` (−2) | zero dano: `Atordoado` + terreno difícil, CD +2, tudo durando uma rodada a mais |
| `Hora Morta` | `Efeito` · `Longe` (−2) | um quarteirão em silêncio absoluto por uma hora |
| `Fissura` | `Projétil` · `Toca a Alma` (−2) | 7 dados viram 3d8 = 13 na alma |

### Classe 4 · 12 pontos · 12 PE

**Classe 4 · 12 pontos · 12 PE**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Prisão de Sombras` | `Explosão` (−2) · `Atordoado` (−6) · `Escolher` (−4) · `Sangra` (+4) | 4d8 = 18 + `Atordoado` durando uma rodada a mais; você toma 8 |
| `Julgamento Vertical` | `Linha` (−2) · `Fura` (−4) · `Precisão` (−2) · `Lento` (+4) | 8d8 = 36, fura 12 de RD, +2 na CD |
| `Roubo de Fôlego` | `Projétil` · `Sugar` (−4) · `Remate` (−4) · `Condicional`: o alvo te acertou desde o seu último turno (+4) | 8d8 = 36, cura 9, +25% em alvo abaixo de metade |
| `Passo do Espelho` | `Toque` (`Corpo a Corpo` +4) · `Rápido` (−6) · `Passo` (−2) · `Recuo` (+4) | 12d8 = 54 como Ação Bônus, no toque |
| `Muralha` | `Apoio` · `Anteparo` (−4) · `Guarda` (−4) · `Parado` (+2) | parede com 40 de vida, aliado com +2 de defesa e 18 de vida temporária |
| `Maré Branca` | `Onda` (−6) | cura 6d8 = 27 em todos os aliados num raio de 3 m |
| `Alinhavo` | `Cura` (−4) · `Remenda` (−6) · `Gesto` (+2) | cura 4d8 = 18 e devolve 20 de Integridade, com a vida máxima junto |

### Classe 5 · 15 pontos · 15 PE

**Classe 5 · 15 pontos · 15 PE**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Purga Escarlate` | `Projétil` · `Inescapável` (−5) | 10d8 = 45 automático, sem acerto e sem resistência |
| `Chuva de Agulhas` | `Projétil` · `Rajada` (−3) · `Precisão` (−3) · `Parado` (+3) | 12d8 = 54 em 6 tiros, +2 cada |
| `Vala Comum` | `Explosão` (−3) · `Maior` (−3) · `Derrubado` (−3) · `Lento` (+5) | 11d8 = 49 num raio de 4,5 m, todos `Derrubados` por uma rodada |
| `Fim de Turno` | `Explosão` (−3) · `Escolher` (−5) · `Lento` (+5) | 12d8 = 54 num raio de 3 m, só em quem você escolher |
| `Segunda Vida` | `Cura` (−5) · `Levanta` (−8) · `Uma Vez` (+3) · `Gesto` (+3) | cura 8d8 = 36, ou levanta um aliado caído com 25 |
| `Fio Preso` | `Efeito` · `Fica` (−5) | um bairro de onde ninguém sai, até alguém desfazer |
| `Sete Palmos` | `Toque` (`Corpo a Corpo` +5) · `Toca a Alma` (−3) | 15 dados viram 7d8 = 31 na alma, no toque |

### Liberações Máximas

Escritas antes da sessão, Classe 3 ou mais, fora da lista de feitiços conhecidos. Todas custam a rodada inteira, 50% a mais de PE e o preço escolhido na hora.

Repare na `Rachadura`: o `Lento` devolveria 3 pontos, mas a `Linha` só custou 2, e devolução nunca passa do que foi gasto em Melhoria, então o terceiro ponto some sem virar dado.

**Liberações Máximas**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `Golpe do Voto` | Classe 5 · `Projétil` (nada mais) | 20d8 = 90, o máximo do nível 20. 23 PE |
| `Rachadura` | Classe 3 · `Linha` (−2) · `Lento` (+3, só 2 aproveitados) | 12d8 = 54 numa linha de 18 m, o teto da Classe 3. 14 PE |
| `Sentença Final` | Classe 5 · `Explosão` (−3) · `Escolher` (−5) · `Lento` (+5) | 17d8 = 76 num raio de 3 m, só em quem você escolher. 23 PE |

### Técnicas Máximas

Montadas com o orçamento da faixa 17 a 20: 8 pontos nos preços da Classe 5.

**Técnicas Máximas**
| Nome | Como foi montado | Resultado |
|---|---|---|
| `O Fim da Linha` | `Linha` (−3) · `Muito Longe` (−5), 8 do orçamento | 24d8 = 108 numa linha de 60 m |
| `Ponto Final` | `Projétil` · `Fura` (−5), 5 do orçamento, 3 se perdem | 24d8 = 108 furando 15 de RD |

## Apêndice

*Os termos deste capítulo estão no glossário do livro, logo depois da introdução.*

### Ficha de feitiço

**Ficha de feitiço**
| | |
|---|---|
| **Nome** | |
| **Classe / Pontos / Teto / PE** | |
| **Forma** | `Projétil` · `Toque` · `Explosão` · `Aura` · `Cone` · `Linha` · `Cura` · `Apoio` · `Onda` · `Efeito` |
| **Resolve com** | Acerto · Teste de Resistência · Automático |
| **Melhorias** | |
| **Restrições** | |
| **É Liberação Máxima?** | Sim ☐   Não ☐        Preço na hora: Vazio · Sangue · Peso |
| **Dano ou cura** | ____ d8  =  ____ |
| **Ação** | Padrão · Bônus · Reação · Rodada inteira |
| **Como é** | |

### Catálogo de temas

Setenta pontos de partida para escrever a sua Regra. Não têm regra nenhuma amarrada, são só ideias.

**Catálogo de temas**
| Grupo | Temas |
|---|---|
| **Corpo e matéria** | Corte · Impacto · Perfuração · Peso · Elasticidade · Carne · Sangue · Osso · Doença · Crescimento |
| **Elementos** | Fogo · Gelo · Raio · Vento · Água · Terra · Metal · Ácido · Veneno · Fumaça |
| **Força e movimento** | Gravidade · Vetor · Velocidade · Inércia · Rotação |
| **Espaço e tempo** | Distância · Espaço · Tempo · Direção · Reflexo |
| **Sentidos** | Som · Silêncio · Luz · Sombra · Cheiro |
| **Mente e alma** | Medo · Memória · Sono · Ilusão · Voz · Nome · Emoção · Vontade · Instinto · Loucura |
| **Conceito** | Vínculo · Troca · Cópia · Contrato · Dívida · Sorte · Aposta · Julgamento · Regra · Registro · Valor · Verdade · Segredo · Herança · Ausência |
| **Criação** | Invocação · Construção · Marionete · Ferramenta · Selamento · Bloqueio · Semente · Enxame · Máquina · Molde |

Os do grupo Conceito quase sempre pedem uma Passiva de `Regra Própria` para funcionarem bem.

---


# Capítulo 10 · Técnica Marcial

*fonte: `manual/42-tecnica-marcial.md`*

Duas rotas de criação montam o poder aqui em vez de montar no Fundamento: o **Corpo Amaldiçoado** e a **Restrição Celestial pelo ramo sem energia**. As duas estão no capítulo 7, *Origens e Legados*.

> **Técnica Marcial é o Fundamento com o corpo no lugar da energia.** Mesma máquina, mesmo orçamento, mesma conta de montagem.
>
> **Onde o Fundamento escreve um Selo, você escolhe três grupos de arma ou uma ferramenta sob medida.**

## Máquina herdada

**Tudo que o capítulo 9, *Fundamento*, diz vale aqui.** Pontos são `3 × Classe`, o custo em PE é o mesmo número, o que sobra de ponto vira `1d8` de dano, Melhorias e Restrições obedecem os mesmos tetos, e a sua lista tem `2 + (nível ÷ 2)` espaços, mais um por marco.

Três coisas mudam de nome e duas somem.

### `Kata`

**`Kata`** (型, a forma que se treina) — a sua aplicação concreta, montada com pontos. Mesma Classe, mesmos pontos, mesmo custo em PE, mesmo teto de Melhoria e de Restrição. **Onde o capítulo 9 escreve *feitiço*, leia `Kata`.**

### `Ruptura`

**`Ruptura`** — a única Kata que passa do limite de dano contra um alvo só. Uma no nível 10, uma no 20 e uma no 30. **`+Classe` em dados, custa a rodada inteira, `+50%` de PE**, e o preço se escolhe na hora: `Vazio`, `Sangue` ou `Peso`.

É a Liberação Máxima do capítulo 9, com as mesmas regras.

### `Ōgi`

**`Ōgi`** (奥義, a técnica que a escola guarda) — o golpe de dano fixo, do nível 17 em diante. **Dano pela faixa de nível, orçamento de montagem à parte, `5 × maior Classe` de PE**, e não aceita Restrição.

É a Técnica Máxima do capítulo 9.

### Selo e Expansão de Domínio

> **Você não tem Selo.** O equipamento ocupa o lugar dele.
>
> **Você não tem Expansão de Domínio.** Nem incompleta, nem completa, tenha a sua ficha energia amaldiçoada ou não. Uma Expansão estende a técnica inata sobre o território em volta, e esta rota não tem técnica inata para estender.

**E quem não tem energia amaldiçoada troca refino e aptidões por Lapidação e Bênçãos**, no capítulo 12.

## Rotas

Na criação, depois da Descrição e da Regra, você escolhe uma das duas. **A escolha é uma vez e não muda**, como o Caminho e a Trilha.

### Rota de arma

> **Escolha três das treze categorias de arma, diferentes entre si.** As treze estão no capítulo 13, *Equipamento*.
> **Você recebe uma arma de cada uma, de grau 4.** Grau 4 fere maldição e não dá `Estigma` nenhum — capítulo 14, *Ferramenta Amaldiçoada*.
> **Você é treinado nas três**, seja qual for a lista de treino do seu Caminho.
> **As suas Katas valem com qualquer arma amaldiçoada desses três grupos.**

A peça específica é descartável, o grupo não. Se a sua lâmina quebrou no meio da missão e você pegou outra do chão, as suas Katas continuam.

#### Limites

**Os três grupos entregam arma, treino e o Selo. Manha nenhuma.** Uma Vanguarda desta rota continua escolhendo **uma** categoria na `Escola de Arma`, e pode escolher uma que não seja das três.

**As três armas começam em grau 4, e param aí.** Subir de grau é assunto do capítulo 14, pelo mesmo ritmo que vale para todo mundo.

**Três armas na mochila não são três `Estigma`.** O teto conta pelo que está na mão, e não pelo que está guardado.

#### Atributo

A sua técnica declara um atributo na criação, como toda técnica declara — capítulo 9, *Fundamento*, na seção *Atributo da técnica*.

> **Os três grupos têm de acertar pelo atributo que você declarou.**

O catálogo de armas só tem duas respostas para *"que atributo acerta com essa arma?"*, então sobra escolha:

**Grupos por atributo de acerto**
| Atributo | Grupos | Quais |
|---|---|---|
| **Força** | 8 | Lâmina Longa · Massa · Porrete · Manopla · Machado · Ceifa · Armas Longas · Flexível |
| **Destreza** | 6 | Lâmina Curta · Lâmina Longa · Arremesso · Yumi · Balestra · Arma de Fogo |

A `Lâmina Longa` está nas duas porque a Rapieira e a Katana carregam `Fineza`.

> **Nenhum grupo de arma acerta por Inteligência, Essência ou Constituição.** Esta rota é sempre Força ou Destreza. Se a sua ficha é a pessoa que resolve com a cabeça, a rota é a de baixo.

### Rota de ferramenta

> **Escolha uma ferramenta amaldiçoada sob medida, de grau 4, na forma de objeto de apoio** — a categoria que o capítulo 14 abre ao lado do catálogo de armas.
> **Ela não tem dado de arma**, e não precisa ter: as suas Katas nunca somaram o dado do equipamento.
> **Ela declara na criação se o seu golpe simples atravessa por ela.**
> **As suas Katas valem só com ela.**
> **Ela declara qualquer um dos cinco atributos**, e quem justifica é a ficção do objeto.

Uma armadura construída por engenharia, uma câmera amaldiçoada, uma maleta, um instrumento. Uma armadura de engenharia acerta por Inteligência; um instrumento que se toca acerta por Essência.

> **Se a ficção for armadura, ela É o seu uniforme.** Não some com o `Traje` nem com o `Revestimento` do capítulo 13 — ela é um dos dois, e usa os números de lá.

## Selo

> **O seu Selo é ter o equipamento em uso.** Uma das três armas, ou a ferramenta.

Ele funciona como qualquer outro Selo: não custa ponto, não devolve ponto e não dá bônus. E cobra as duas mesmas coisas que o capítulo 9 cobra de todo Selo:

**Restrição contra o Selo**
| A Restrição | O que acontece |
|---|---|
| qualquer uma que peça *"estar com a minha arma"* | **não devolve ponto.** O Selo já obriga isso |
| `Gesto`, que pede as duas mãos livres | quase invendável nesta rota, e sem-arma nenhuma numa arma de duas mãos |

## Ferir maldição

Uma arma comum não fere maldição. Quem tem energia resolve isso com `canalizar energia`, a aptidão de graça do refino 1 — e quem não tem energia não tem aptidão nenhuma.

> **Toda Kata passa pelo equipamento, e o equipamento é ferramenta amaldiçoada de grau 4.** Então toda Kata fere maldição, nas duas rotas.

Sobra o golpe simples, que não é Kata e sai de graça em todo turno.

**Golpe simples e maldição**
| Rota | O golpe simples |
|---|---|
| **arma** | sai por uma das três, que são grau 4. **Fere maldição** |
| **ferramenta** | é o soco, e soco não fere maldição. **Depende do objeto** |

Na rota de ferramenta, o objeto declara qual dos dois é na criação — uma linha da ficha, junto da Descrição, no mesmo lugar em que o Fundamento anota o tipo de dano.

> **Coisa que o golpe atravessa** — armadura, manopla, máscara, coturno. O seu golpe simples fere maldição.
> **Coisa que você só carrega** — câmera, lanterna, maleta, instrumento. O seu golpe simples não fere maldição, e as suas Katas continuam ferindo.

> **⚠ Escolha com cuidado, porque ela cobra tarde.** O ataque extra que Bastião e Vanguarda ganham no nível 7 é um golpe simples solto. Se o seu objeto é do tipo que você só carrega, esses dois Caminhos passam a valer bem menos na sua ficha.
> **O Corpo Amaldiçoado fere maldição com o golpe simples, seja qual for o objeto.** Ele tem energia amaldiçoada, então tem aptidões e refino normais — e com eles o `canalizar energia` de graça no refino 1. **O equipamento continua obrigatório**, porque ele é o Selo, e sem Selo não sai Kata.

## `Desarmado`

Pôr o Selo num objeto põe a sua ficha atrás de uma condição — `Desarmado`, no capítulo 4, quando alguém tira a sua arma da sua mão. É por isso que os grupos são **três**, e não um:

> **Rota de arma:** a Kata vale com arma de qualquer um dos três grupos. Tiraram uma, sobram duas.
> **Rota de ferramenta:** objeto de apoio não ocupa a mão de arma, e o `Desarmado` não alcança ele.

Sacar a segunda é o primeiro saque do seu turno, então sai de graça — capítulo 2, *O Turno*, na seção *Sacar e guardar*.

## Marco

**O seu marco tem os três eixos**, iguais aos de todo mundo: `Corpo`, o eixo de controle, e `Leque`. Você tem lista de Katas, tem Passivas e tem espaços, então o `Leque` compra o que ele sempre comprou.

O eixo de controle muda de nome com a Origem: quem tem energia amaldiçoada leva `Refino` e aptidões, no capítulo 11; quem não tem leva `Lapidação` e Bênçãos, no capítulo 12.

## Técnicas Marciais prontas

Duas, uma de cada rota. As duas param onde a criação de personagem para: Descrição, Regra, atributo, rota, Famílias e a Passiva. `Ruptura` e `Ōgi` não aparecem porque só chegam nos níveis 10 e 17, e são escritas na hora.

### Fisga

**Ficha de Técnica Marcial**
| | |
|---|---|
| **Descrição** | Ela não aprendeu nada elegante. Aprendeu a segurar peso, a alcançar mais longe do que o braço dela alcança, e a não largar. O que ela faz com uma arma é o que qualquer um faria, feito rápido demais para dar tempo de responder. Tipo de dano: corte. |
| **Regra** | *"Alcançar antes, e não soltar."* |
| **Atributo** | Força |
| **Grupos** | Armas Longas · Ceifa · Flexível |
| **Livres** | Alcance · Controle |
| **Fechadas** | Amparo · Auxiliares · Área |
| **Passiva** | `Raiz` (Classe Passiva 1): você não é movido à força nem derrubado contra a sua vontade |

Os três grupos fecham em Força, e os três carregam `Alcance` e `Emaranha` — é isso que justifica as duas Famílias Livres. `Amparo` está Fechada porque nenhuma das três cura ninguém.

### Bancada

**Ficha de Técnica Marcial**
| | |
|---|---|
| **Descrição** | Ele nasceu sem nada e leu tudo. A armadura é dele: fez, refez, e conhece cada solda. Ela não tem energia amaldiçoada nenhuma dentro — o que ela tem é a maldição que ele prendeu no chassi e um sistema que ele entende melhor que o fabricante entenderia. Tipo de dano: impacto. |
| **Regra** | *"Resolver o problema com a peça certa."* |
| **Atributo** | Inteligência |
| **Ferramenta** | uma armadura de corpo inteiro. **Coisa que o golpe atravessa** — os punhos dela são dele |
| **Livres** | Auxiliares · Amparo |
| **Fechadas** | Área · Marca · Castigo |
| **Passiva** | `Leitura` (Classe Passiva 1): você identifica a Classe e a Forma de qualquer feitiço conjurado a até 18 m |

A armadura da Bancada é o `Revestimento` do capítulo 13, com os números publicados lá. E `Amparo` é Livre porque a ficção aguenta: uma arma que cura é difícil de justificar, e uma bancada de engenharia não é.

---


# Capítulo 11 · Aptidões e Refino

*fonte: `manual/45-aptidoes-e-refino.md`*

Aptidão é o que qualquer feiticeiro pode aprender, venha a energia de onde vier: cobrir-se de energia, levantar uma barreira, ficar de pé dentro de uma Expansão de Domínio. Ela não depende da sua técnica.

Aptidão se ensina. Ela passa de mestre para aluno, de escola de espada para escola de espada, e dois feiticeiros de técnicas opostas sabem exatamente as mesmas quatro coisas contra um domínio. É o repertório comum da profissão, e é o que faz a mesa inteira falar a mesma língua no meio de uma luta.

Quem compra aptidão é o **refino**, o eixo de controle da sua ficha. Poder é quanto você tem. Refino é quanto você não desperdiça.

> **Sem energia amaldiçoada não existe refino nem aptidão.** Uma ficha nessa situação usa **Lapidação** e **Bênçãos** no lugar dos dois, no capítulo 12, *Bênçãos e Lapidação*. A máquina é a mesma casa por casa; o que muda é o conteúdo do catálogo.

## Refino

Energia amaldiçoada vaza. Ela escapa do corpo de quem produz, o tempo todo, e é por isso que um feiticeiro fareja outro a um quarteirão de distância. O refino mede quanto da sua você segura.

Um feiticeiro de refino 1 gasta muito para fazer pouco. A camada em volta do corpo dele sai fina, o domo que ele levanta desmancha no primeiro empurrão, e o que sobra dele no ar avisa qualquer maldição de que ele está chegando. Um feiticeiro de refino 10 entrega a energia inteira onde mandou: a mesma quantidade rende o dobro, a camada aguenta a luta toda, o domo aguenta o cerco, e o que ele solta no ar é só o que ele decidiu soltar.

É por isso que o refino é a moeda que compra aptidão. Aptidão se aprende manejando energia, com a técnica fora da conta, e quem maneja melhor aprende mais coisas.

Na ficha, o refino é um número de 1 a 10. Toda ficha começa em 1, e ele sobe nos marcos: os níveis **6, 10, 14, 18, 22, 26 e 30**, sete ao longo da campanha inteira.

> **Cada marco te dá +1 de refino de graça. Se você escolher Refino no marco, você ganha mais +1.**

Sete marcos de graça mais o 1 do começo fecham em refino 8 sem você escolher nada. Quem escolhe Refino em todos eles bate no teto no nível 22.

**Refino por marco**
| marco | quem nunca escolhe Refino | quem sempre escolhe |
|---|---|---|
| começo da ficha | 1 | 1 |
| 6 | 2 | 3 |
| 10 | 3 | 5 |
| 14 | 4 | 7 |
| 18 | 5 | 9 |
| 22 | 6 | **10** |
| 26 | 7 | 10 |
| 30 | **8** | 10 |

### Efeito do refino

> **O refino nunca entra num número disputado contra alguém que cresce mais devagar que ele.** Ele fica fora de acerto, CD, defesa, Teste de Resistência e dano.

**Efeito do refino**
| onde o refino não entra | onde ele entra |
|---|---|
| acerto | custo: quanto PE a aptidão cobra |
| CD | frequência: quantas vezes por cena, por descanso, por dia |
| defesa | escopo: alcance, duração, quantos alvos |
| Teste de Resistência | magnitude fora de disputa: Redução de Dano, proteção |
| dano | disputa contra outro refino, como o clash de expansões |

**Só a `Projetar energia` põe refino em dano.** A proteção de `Cobrir-se de energia` entra na sua Defesa, e por isso usa `1/3 do refino` em vez do valor cheio.

> **Arredondamento.** Toda divisão de refino arredonda para baixo: refino 5 dividido por 2 dá 2.

## Marco

A cada marco a ficha ganha três coisas de graça e escolhe uma quarta.

> **Passivo:** +1 ponto de atributo, +1 de refino e +1 espaço de feitiço.
>
> **Escolha, uma das três:**
>
> **Corpo** — mais um ponto de atributo.
>
> **Refino** — mais um de refino, e uma aptidão. **Se o seu refino já estiver no teto, você leva duas aptidões no lugar.**
>
> **Leque** — mais um feitiço, que só pode ser feitiço, e uma Passiva.

Quem escolhe Refino em todo marco bate no teto no nível 22. Dali em diante a metade "mais um de refino" não tem onde cair, e a escolha entrega a segunda aptidão no lugar dela.

> **Quem nunca escolhe Refino termina a campanha com zero aptidões.** A rota existe e é legítima: ela troca dez aptidões por sete pontos de atributo a mais. Está escrito aqui para ninguém descobrir isso no nível 20.
Mesmo essa ficha não fica sem nada. `Cobrir-se de energia` e `Canalizar energia` vêm de graça no refino 1, e a primeira continua crescendo com o refino passivo até 8. O que ela nunca vai ter é `Energia Reversa` nem `Barreira Simples`.

*O marco é do capítulo 16, __Experiência e Progressão__: é lá que estão os sete níveis em que ele cai, quanto refino cada rota junta marco a marco, e o que Corpo e Leque compram. Aqui interessa só a escolha de Refino, que é a que vira aptidão.*

## Aptidões

Um marco de Refino compra **uma aptidão**, de qualquer altura que o seu refino alcance. Duas do catálogo não custam marco nenhum: `Cobrir-se de energia` e `Canalizar energia` já estão na sua ficha desde o refino 1.

> **Aptidão não custa espaço de feitiço.** Espaço de feitiço é a moeda das Passivas e da Expansão de Domínio. As duas economias são separadas: aptidão custa marco, e só marco.

`Sua maior Classe` aparece no texto de várias aptidões. Ela é a variável do capítulo 9, *Fundamento*, e é lá que ela é definida.

### Classe Passiva

As aptidões usam a mesma escada das Passivas, e ela está no capítulo 9, *Fundamento*.

Aqui ela não cobra nada: o marco compra uma aptidão de qualquer altura, e o preço é o mesmo. Quem separa as alturas é o requisito. E como o refino escala o que a aptidão entrega, uma Classe Passiva 1 no refino 10 rende bem mais do que no refino 2.

### Requisito

Cada aptidão declara o próprio requisito, e ele está na linha dela no catálogo: nenhum, nível, refino, os dois juntos, outra aptidão, ou Origem.

`Cortina` é a única que hoje exige outra aptidão: ela pede `Barreira Simples`, porque cortina é a barreira maior. As três de kokusen são alternativas entre si, e nenhuma exige a outra.

## Catálogo

Catorze entradas.

### Como ler uma aptidão

Cada entrada aparece duas vezes. Primeiro nesta tabela, com quatro campos: **nome**, **requisito**, **Classe Passiva** e **o que o refino escala**. Depois na seção dela, com uma descrição do que ela é e uma caixa com a regra.

Traço na coluna de Classe Passiva quer dizer que a entrada não declara uma. Traço na última coluna quer dizer que o refino não mexe naquela aptidão.

**Como ler uma aptidão**
| Aptidão | Requisito | Classe Passiva | O que o refino escala |
|---|---|---|---|
| Cobrir-se de energia | grátis no refino 1 | — | a proteção, e a Redução de Dano da Reação |
| Canalizar energia | grátis no refino 1 | — | — |
| Projetar energia | sem requisito | — | o dano |
| Energia Reversa | refino 7 e nível 13 | 3 | — |
| Kokusen | sem requisito | — | a chance no d100 |
| Kokusen Melhorado | refino 5 e nível 14 | — | vantagem no d100 |
| Kokusen Constante | refino 5 | — | a chance no d100 |
| Cesta Oca de Vime | sem requisito | 1 | — |
| Domínio Simples | refino 4 e nível 7 | 2 | o raio |
| Pétala | refino 4 e nível 7 | 2 | quantos Acertos ela devolve |
| Extensão de Domínio | refino 7 e nível 13 | 3 | a duração |
| Barreira Simples | sem requisito | — | a vida do domo |
| Cortina | exige a `Barreira Simples` | — | a vida dela |
| Aptidão Própria | uma vez na ficha inteira | 1 ou 2 | conforme o que for escrito |

## Aptidões de graça

Estas duas chegam com a ficha, no refino 1, sem custar marco nenhum. Elas são o que separa alguém que tem energia amaldiçoada de alguém que sabe usar energia amaldiçoada.

### Cobrir-se de energia

A primeira coisa que se ensina, e a que nunca se desliga. Você espalha a sua energia por cima da pele e deixa ligada: uma casca que não aparece, que aguenta o impacto que quebraria o osso de uma pessoa comum. Quem enxerga energia vê a camada acender no instante do golpe. Quem não enxerga vê alguém apanhar e continuar de pé.

Como Reação, em vez de espalhar a camada você joga ela inteira no ponto onde o golpe vai chegar, e fica descoberto no resto do corpo até se recompor. Por exemplo, com refino 6 a sua proteção passiva é 3, e a Reação desconta 9 de um golpe por 2 PE.

> **Cobrir-se de energia** — sem Traje e sem Revestimento, a sua proteção é `1/3 do refino + 1`. Escudo soma com ela.
>
> Como Reação, você concentra a energia no impacto: Redução de Dano de `1,5 × refino` num golpe, por **2 PE**. Você fica sem proteção até o fim do seu próximo turno.
>
> Requisito: grátis no refino 1. O refino escala a proteção e a Redução de Dano da Reação.

A proteção é um piso. Ela sustenta o feiticeiro que não investiu em corpo nenhum, e sai de cena assim que Traje ou Revestimento entram na conta.

Fora de combate ela decide as cenas em que ninguém está brigando: a queda de três andares, o teto que cede, o carro. Um feiticeiro atravessa isso e levanta, e é por essa aptidão que o mestre pode jogar o grupo dentro de um prédio desabando sem matar ninguém.

### Canalizar energia

Mão nua atravessa maldição sem machucar. Para o golpe encostar de verdade, a energia precisa sair pelo punho no exato momento em que ele chega. Canalizar é empurrar a técnica pela pele: o que era um soco vira feitiço na hora de resolver.

> **Canalizar energia** — você conjura feitiço de Toque. Um feitiço de Toque é um feitiço de Forma Toque, sem Melhoria e sem Restrição: mesma Classe, mesmo orçamento de pontos, mesmo custo em PE.
>
> Requisito: grátis no refino 1.

Ela é a porta de toda técnica de contato. Sem ela, tudo o que a sua ficha faz precisa sair de longe, e encostar num inimigo vira uma decisão sem recompensa.

## Energia crua

Duas aptidões trabalham com a energia sem forma. Uma dispara ela crua, a outra inverte o sinal dela.

### Projetar energia

Você junta energia na mão e solta, sem técnica e sem forma. Sai como um borrão que estala no ar e empurra o que acerta. Todo feiticeiro sabe fazer, ninguém se orgulha de fazer, e todo mundo já usou.

> **Projetar energia** — você dispara energia crua. O dano é `refino`, e ela não gasta PE.
>
> Requisito: nenhum. O refino escala o dano.

`Projetar energia` é o que sobra quando o combustível acaba. Ela existe para o turno em que o seu PE zerou, a luta ainda não terminou e você continua precisando fazer alguma coisa.

### Energia Reversa

Toda energia amaldiçoada é negativa. Multiplicar uma negativa por outra dá positivo, e energia positiva conserta carne. Quem consegue fechar essa conta dentro do próprio corpo fecha o corte enquanto ele ainda está abrindo.

É a coisa mais difícil do catálogo de aprender, e quase ninguém aprende num treino. O feiticeiro costuma descobrir sozinho, no meio de estar morrendo, e depois passa anos tentando repetir de propósito.

> **Energia Reversa** — ação padrão. Gaste até `a sua maior Classe` de PE e recupere `1d8` de vida por PE gasto, em você.
>
> Requisito: refino 7 e nível 13. Classe Passiva 3.

> **A `Energia Reversa` cura só você.** Curar outra pessoa é o degrau raro: quem faz isso é a Trilha `Sutura`, e é lá que se paga por isso.

Ela muda a forma das lutas longas e muda o que acontece entre elas. Um personagem com Energia Reversa não precisa voltar para casa depois de cada cena, e o mestre perde a alavanca de encerrar um arco pelo desgaste do grupo. Quando você monta uma sequência de cenas sem descanso, é esta aptidão que decide se ela aperta alguém.

## Aptidões de kokusen

Quando o soco e a energia chegam no alvo dentro da mesma fração de instante, o espaço em volta do ponto de contato racha. Sai um estalo preto, curto, e o golpe entrega muito mais do que devia entregar. Ninguém acerta um kokusen de propósito: você percebe pelo barulho e pela cara de quem apanhou.

Feiticeiro que acerta um passa a entender a própria energia de um jeito que treino nenhum ensina, e a mesa inteira lembra do dia.

### Kokusen

> **Kokusen** — em crítico no corpo a corpo, role d100. `2 × refino` ou menos é kokusen: o dano leva +50% depois de todos os valores resolvidos.
>
> Cada d100 falhado empurra o próximo em **+2**, e o acumulado zera no descanso longo.
>
> Requisito: nenhum. O refino escala a chance no d100.

O +50% entra em cima do crítico que já dobrou os dados. Um crítico entrega dois punhados de dado; um kokusen entrega três. Por exemplo, com refino 6 o kokusen sai em 12 ou menos no d100 — 12% dos seus críticos corpo a corpo.

O `+2` acumulado é a memória do personagem. Quem passou a noite inteira quase acertando está mais perto do que estava quando a briga começou.

### Kokusen Melhorado

Você já acertou um antes, e o corpo guardou o tempo. A segunda tentativa da mesma noite sai mais perto do ponto do que a primeira.

> **Kokusen Melhorado** — mesma regra do `Kokusen`, exceto que você rola dois d100 e fica com o melhor.
>
> Requisito: refino 5 e nível 14. O refino escala a vantagem no d100.

### Kokusen Constante

Você parou de esperar pela sorte e passou a mirar o instante. A janela continua absurda de pequena, e você simplesmente acerta ela com mais frequência.

> **Kokusen Constante** — mesma regra do `Kokusen`, exceto que a base sobe para `3 × refino`.
>
> Requisito: refino 5. O refino escala a chance no d100.

> **As três empilham, nesta ordem: a base é `3 × refino`, e a vantagem da `Kokusen Melhorado` rola em cima dela.** Com as três na ficha, o d100 sai em 51% no refino 10. Nenhuma delas exige a outra.

**Kokusen Constante**
| refino | só a `Kokusen` | só com a `Melhorado` | só com a `Constante` | com as duas |
|---|---|---|---|---|
| 1 | 2% | 4,0% | 3,0% | 5,9% |
| 5 | 10% | 19,0% | 15,0% | 27,8% |
| 10 | 20% | **36,0%** | 30,0% | **51,0%** |


## Aptidões anti-domínio

Uma Expansão de Domínio completa não erra. O Acerto dela simplesmente acontece com quem está lá dentro, sem rolagem e sem Teste de Resistência, e nenhuma defesa da ficha encosta nele.

Estas quatro são as respostas que o ofício inteiro desenvolveu para esse problema. Elas são a razão de um feiticeiro entrar numa luta contra alguém que tem domínio e sair vivo, e são conhecidas até por gente que nunca teve técnica nenhuma.

> **As quatro anulam o Acerto de uma Expansão de Domínio. Nenhuma delas serve contra a Expansão incompleta.**
>
> A incompleta não tem acerto garantido: o Acerto dela rola. Contra ela você se defende com Defesa e com Teste de Resistência, como se defende de tudo o mais no jogo.

O que separa as quatro é quanta liberdade você tem enquanto está protegido.

**Aptidões anti-domínio**
| | protege | e cobra | PE por rodada |
|---|---|---|---|
| **Cesta Oca de Vime** | só você, dentro de uma esfera | você segura o símbolo e não faz mais nada | nenhum |
| **Domínio Simples** | um raio em volta de você | os pés não saem do chão | `1 × maior Classe` |
| **Pétala** | o seu corpo, e devolve o golpe | concentração, e não vale contra ataque físico | `1 × maior Classe` |
| **Extensão de Domínio** | o seu corpo, e faz o seu ataque acertar | nenhum feitiço enquanto ela estiver de pé | `1,5 × maior Classe` |

### Cesta Oca de Vime

Você trava as mãos num símbolo e uma esfera de energia se fecha em volta do seu corpo. Enquanto o símbolo estiver de pé, o Acerto passa por fora de você. Enquanto o símbolo estiver de pé, você também está fora da luta: as mãos ocupadas, a atenção inteira presa ali, e o mundo continuando sem a sua participação.

> **Cesta Oca de Vime** — você faz o símbolo e uma esfera se fecha em volta de você. Enquanto você o segurar, o Acerto de uma Expansão não te alcança, e você não faz mais nada. Ela não tem duração, não pede teste e não custa PE: enquanto o símbolo estiver de pé, ela está de pé.
>
> Requisito: nenhum. Classe Passiva 1.

A `Cesta Oca de Vime` anula o Acerto e mais nada: o Efeito da Expansão continua acontecendo em cima de você. Em troca ela não quebra, e é a única das quatro assim.

Ela é a resposta de quem não tinha nada preparado. Chega já no primeiro marco de Refino de qualquer ficha, e é o que salva o feiticeiro de apoio, o estudante e a pessoa que estava passando na rua quando o domínio abriu.

### Domínio Simples

Um domínio em miniatura, com os seus pés no centro. Você derrama energia no chão em volta e declara aquele círculo seu: dentro dele, o Acerto de outro domínio não tem por onde entrar. Ele se ensina em escola de espada e passa de mestre para aluno, e é por isso que feiticeiro sem técnica nenhuma aparece sabendo fazer.

> **Domínio Simples** — um domínio pequeno em volta de você, de raio `1,5 m + refino ÷ 2`. Dentro dele o Acerto de uma Expansão não acontece, e ele cobre quem estiver no raio. Custa `1 × a sua maior Classe` de PE por rodada, e ela quebra se os seus pés saírem do chão.
>
> Requisito: refino 4 e nível 7. Classe Passiva 2. O refino escala o raio.

É o único dos quatro que protege o grupo, e isso muda a cena inteira: uma pessoa da mesa vira o abrigo, e o resto decide se vale a pena sair dele. Em compensação, quem segura o círculo vira um poste no meio da luta.

O raio nunca passa de um movimento:

**Domínio Simples**
| refino | 1 | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| raio | 1,5 m | 2,5 m | 3,5 m | 4,5 m | 5,5 m | **6,5 m** |

### Pétala

A energia sobe pela pele e fica esperando. Quando o Acerto encosta em você, ela reage no ponto exato de contato e devolve o golpe, e quem estiver olhando vê a energia se abrir em volta do corpo por um instante. Você continua andando, continua batendo, e continua contando quantas vezes ainda dá para fazer isso.

> **Pétala** — a energia cobre o seu corpo e devolve o golpe. Quando o Acerto de uma Expansão te alcança, ele é anulado no ponto de contato, `refino ÷ 2` vezes por cena. Custa `1 × a sua maior Classe` de PE por rodada, e ela cai se você perder a concentração.
>
> Requisito: refino 4 e nível 7. Classe Passiva 2. O refino escala quantos Acertos ela devolve.

É a resposta de quem se recusa a parar de lutar dentro de um domínio. Ela nunca cobre a Expansão inteira: a completa dispara o Acerto ao abrir e no começo de cada turno de quem a levantou, e sempre sobra um.

**Pétala**
| refino | Acertos que a Expansão solta | a Pétala devolve |
|---|---|---|
| 4 | 3 | 2 |
| 6 | 4 | 3 |
| 8 | 5 | 4 |
| 10 | **6** | **5** |

### Extensão de Domínio

Você abre um domínio e não põe técnica nenhuma dentro dele: fica só a camada, colada no corpo, fina como uma segunda pele. Técnica que encosta nela se desfaz. O seu golpe atravessa a técnica do outro como se ela não estivesse ali. E ela cobra a sua própria técnica enquanto estiver de pé, porque a camada não distingue de quem é a energia que encostou.

> **Extensão de Domínio** — você se envolve numa camada fina de domínio sem técnica dentro. Ela anula o Acerto de uma Expansão, anula qualquer técnica que encostar nela, e faz o seu ataque acertar independentemente da técnica do alvo. Dura `refino` rodadas e custa `1,5 × a sua maior Classe` de PE por rodada. Enquanto ela estiver de pé, você não usa a sua técnica.
>
> Requisito: refino 7 e nível 13. Classe Passiva 3. O refino escala a duração.

Ela é a única das quatro que ganha a luta em vez de sobreviver a ela. Contra um inimigo que depende inteiro da técnica dele, é a aptidão que decide a cena: você desliga o que ele sabe fazer e resolve no braço.

A duração é um teto. Segurar as dez rodadas no refino 10 custa 110 de PE, e quem tem pouco PE fica seco antes do fim.

## Aptidões de barreira

Barreira é ofício à parte. Ela não sai do Fundamento de ninguém, se aprende estudando, e o feiticeiro que sabe levantar uma boa é procurado por isso.

> **As duas levam um minuto para levantar**, e um minuto são dez rodadas. As duas são ferramenta de preparação, e se levantam antes da briga começar.

### Barreira Simples

Um domo de energia que você monta num lugar e deixa ali. Ele fecha passagem nos dois sentidos: ninguém entra, ninguém sai, e feitiço nenhum atravessa. Levantar leva um minuto de mãos ocupadas, e por isso ele nasce antes da briga, quando alguém do grupo ainda está pensando.

> **Barreira Simples** — um domo de raio `6 m`, ancorado no lugar onde você o ergueu, que bloqueia passagem e linha de efeito nos dois sentidos. Ele tem `5 × refino` de pontos de vida, e cai quando você fica `Inconsciente`.
>
> Requisito: nenhum. O refino escala a vida do domo.

O domo fica onde foi erguido. Você não leva ele junto, e é por isso que ele serve para fechar um cômodo, uma porta, uma escada.

Fora de combate ela é uma porta que você fabrica: prende uma maldição num quarto até o grupo se organizar, corta o corredor por onde o reforço viria, isola a coisa que a investigação achou para ela continuar lá quando vocês voltarem. Numa cena de perseguição, ela é o jeito de decidir por onde o alvo vai ter que passar.

### Cortina

A cortina cai sobre o lugar inteiro e o mundo comum para de enxergar o que acontece lá dentro. Quem não tem energia amaldiçoada olha para o prédio e vê um prédio; escuta o desabamento e não escuta nada. Cortina exige um nível de manejo que muitos feiticeiros poderosos nunca alcançaram, e as boas são encomendadas a quem sabe fazer.

> **Cortina** — mesma preparação de um minuto da `Barreira Simples`, exceto que ela cobre um lugar inteiro: um prédio, uma escola, um quarteirão. Ela esconde o que está dentro de quem não é feiticeiro, e você pendura uma condição sobre quem atravessa. Ela tem `20 × refino` de pontos de vida, e cai quando você fica `Inconsciente`.
>
> Requisito: exige a `Barreira Simples`. O refino escala a vida dela.

A `Cortina` custa dois marcos, porque você precisa da `Barreira Simples` antes. Quem não escolhe Refino pelo menos duas vezes não levanta cortina nenhuma.

Ela é a aptidão que muda a campanha inteira, e quase todo o valor dela está fora de combate. Com uma cortina, a mesa luta no meio da rua às três da tarde, fecha uma escola sem evacuar ninguém, prende uma pessoa específica dentro de um quarteirão até resolver o que fazer com ela. E ela funciona na direção contrária também: achar uma cortina já levantada é descobrir que alguém preparou aquilo com antecedência, e um arco inteiro cabe nessa única informação.

A condição da `Cortina` fala de quem atravessa, e de mais nada.

**Cortina**
| a condição pode | a condição não pode |
|---|---|
| barrar uma pessoa específica | causar dano a quem entra |
| deixar entrar quem tem energia amaldiçoada, e mais ninguém | mover a cortina, ou fazer ela seguir você |
| impedir que quem está dentro saia | dar bônus a quem está dentro |
| deixar passar quem você nomeou na hora de levantar | esconder de quem é feiticeiro, porque o efeito base já é o contrário |

> **O tamanho da `Cortina` não se mede em metros.** Ela cobre um lugar — um prédio, uma escola, um quarteirão —, e nada do que ela faz depende de distância. Quem precisa fechar uma distância com energia usa a `Barreira Simples`, que tem raio.

## Escrever uma aptidão

### Aptidão Própria

A vaga em branco do catálogo. É o truque que o seu feiticeiro desenvolveu manejando a própria energia, pequeno o bastante para nunca ter virado regra escrita, e específico o bastante para ninguém mais na mesa fazer igual.

> **Aptidão Própria** — você escreve, com o mestre, uma aptidão que não está no catálogo. Antes da sessão, e nunca no meio dela. Ela é Classe Passiva 1 ou 2, nunca 3, e você só pode pegá-la uma vez na ficha inteira.
>
> A ficha registra duas coisas: a frase, e a resposta de *"em quantas cenas por arco isso vai importar?"*.
>
> Requisito: uma vez na ficha inteira. Classe Passiva 1 ou 2.

A resposta dessa pergunta é o que decide o degrau:

**Peso e degrau**
| em quantas cenas por arco | o peso | o degrau |
|---|---|---|
| uma | Leve | Classe Passiva 1 |
| metade | Média | Classe Passiva 2 |
| quase toda | Pesada | Classe Passiva 3 |

> **Na dúvida, Pesada.** Pesada é Classe Passiva 3, e a Classe Passiva 3 está fora do que a `Aptidão Própria` alcança. Então dúvida reprova a proposta.

As cinco travas:

1. **Uma frase.**
2. **Verificável**: a mesa aponta o momento em que ela disparou.
3. **Não é atalho**: ela não repete uma das treze outras entradas do catálogo com outro nome, e não entrega uma que o seu requisito ainda não alcança.
4. **Sem dado de dano.**
5. **Com limite por cena**, se ela for Classe Passiva 2.

Três propostas, e uma delas é recusada:

**Exemplos de Aptidão Própria**
| proposta | em quantas cenas | degrau | veredito |
|---|---|---|---|
| *"você sabe se um objeto foi tocado por energia amaldiçoada nas últimas 24 horas"* | uma por arco | Classe Passiva 1 | **passa** |
| *"uma vez por cena, quando um aliado a até 9 m falha um Teste de Resistência, ele rerrola"* | metade | Classe Passiva 2 | **passa** |
| *"o seu deslocamento é `+3 m`"* | quase toda | Classe Passiva 3 | **recusada** |

A terceira mostra que a trava é de forma e não de tamanho: `+3 m` é pouca coisa, e mesmo assim está fora. Uma coisa que fica sempre ligada é Classe Passiva 3, no tamanho que for.

> Quem quiser a mesma ficção com Classe Passiva 3 tem a `Passiva Própria`, do lado do Fundamento, pagando em espaço de feitiço. A porta existe, ela só não é esta.

## Passivas

As Passivas são do capítulo 9, *Fundamento*. O que segue é o preço delas.

> **Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também.** Quanto mais alta a Classe Passiva, mais espaço a Passiva cobra. Aptidão não entra nessa conta.

Os feitiços que você conhece:

> **`2 + (nível ÷ 2)`, arredondando para baixo, mais um por marco.**

São três no nível 2 e doze no nível 20. Cada Passiva e cada pedaço de Expansão que você comprar sai desse mesmo bolo — e o espaço que todo marco solta de graça entra nele também.

As Passivas pedem nível: Classe Passiva 1 no nível 1, Classe Passiva 2 no 7, Classe Passiva 3 no 13. **A lista de quais Passivas existem em cada altura é uma só, e está no capítulo 9, *Fundamento*.**

> **Você paga no máximo cinco Passivas.** Cada escolha de Leque no marco sobe o teto em uma vaga, e a Passiva que o Leque concede ocupa a vaga nova. As pagas continuam sendo cinco.

## Expansão de Domínio

A regra da Expansão está no capítulo 9, *Fundamento*, e é lá que ela é montada e paga. Deste capítulo você só precisa de duas coisas, e as duas já estão acima: ela gasta espaço de feitiço, como Passiva; e o Acerto dela é o que as quatro aptidões anti-domínio anulam, contanto que a Expansão seja a completa.

---


# Capítulo 12 · Bênçãos e Lapidação

*fonte: `manual/47-bencaos-e-lapidacao.md`*

Bênção e Lapidação valem para **uma** rota de criação: a Restrição Celestial pelo ramo **sem energia**, no capítulo 7, *Origens e Legados*. Uma ficha com energia amaldiçoada — inclusive o Corpo Amaldiçoado, que produz a própria — usa refino e aptidões, no capítulo 11, *Aptidões e Refino*.

> **Sem energia amaldiçoada não existe refino nem aptidão.** No lugar dos dois vêm a **Lapidação** e as **Bênçãos**, e a máquina é a mesma casa por casa. O que muda é o conteúdo do catálogo.

## Lapidação

Um corpo humano tem folga: ele para antes de arrebentar e desiste de um peso que aguentaria mais dez segundos. A Lapidação mede quanto dessa folga o seu personagem já gastou treinando.

> **A Lapidação vai de `1` a `10`.** Toda ficha começa em 1, e ela sobe nos marcos: **`+1` de graça em cada um, e mais `+1` se você escolher Lapidação no marco**.
>
> **São os mesmos degraus do refino, casa por casa** — a tabela `Refino por marco` do capítulo 11 vale para ela, trocando o nome.

> **A Lapidação nunca entra num número disputado contra alguém que cresce mais devagar que ela.** Ela fica fora de acerto, CD, defesa, Teste de Resistência e dano.

Onde ela entra é em custo, em quantas vezes por cena, em alcance e duração, e em magnitude fora de disputa — a proteção de `Defesa sem Armadura` e o piso do `Esteio`.

> **Arredondamento.** Toda divisão de Lapidação arredonda para baixo: Lapidação 5 dividido por 2 dá 2.

## Marco

> **Passivo:** +1 ponto de atributo, +1 de Lapidação e +1 espaço de Kata.
>
> **Escolha, uma das três:**
>
> **Corpo** — mais um ponto de atributo.
>
> **Lapidação** — mais um de Lapidação, e uma Bênção. **Se a sua Lapidação já estiver no teto, você leva duas Bênçãos no lugar.**
>
> **Leque** — mais uma Kata, que só pode ser Kata, e uma Passiva.

> **Quem nunca escolhe Lapidação termina a campanha com zero Bênçãos pagas.** A rota existe e é legítima: ela troca dez Bênçãos por sete pontos de atributo a mais. Está escrito aqui para ninguém descobrir isso no nível 20.
`Defesa sem Armadura` e `Estímulo Muscular` vêm de graça na Lapidação 1, então nenhuma ficha fica sem Bênção nenhuma. A primeira continua crescendo com a Lapidação passiva até 8.

## Bênçãos

Um marco de Lapidação compra **uma Bênção**. Duas do catálogo não custam marco nenhum: `Defesa sem Armadura` e `Estímulo Muscular` já estão na sua ficha desde a Lapidação 1.

> **Bênção não custa espaço de Kata.** Espaço de Kata é a moeda das Passivas. As duas economias são separadas: Bênção custa marco, e só marco.

### Classe Passiva

As Bênçãos usam a mesma escada das Passivas e das aptidões, e ela está no capítulo 9, *Fundamento*.

A Classe Passiva não cobra nada aqui: o marco compra uma de qualquer altura. Quem separa as alturas é o requisito.

### Requisito

Cinco Bênçãos pedem um **atributo**, e nenhuma outra pede coisa nenhuma.

> **Requisito de atributo:** você precisa daquele atributo em **4** ou mais para pegar a Bênção.
>
> **⚠ Uma Bênção com requisito de atributo não soma aquele atributo na rolagem dela.** Ou você paga para destravar, ou usa na conta — nunca os dois.

Os cinco requisitos são um por atributo, e nenhuma ficha alcança os cinco.

## Catálogo

Catorze entradas.

### Como ler uma Bênção

Cada entrada aparece duas vezes. Primeiro nesta tabela, com três campos: **nome**, **requisito** e **Classe Passiva**. Depois na seção dela, com uma caixa de regra.

Traço na coluna de requisito quer dizer que ela não pede nada. Traço na de Classe Passiva quer dizer que a entrada não declara uma.

**Como ler uma Bênção**
| Bênção | Requisito | Classe Passiva |
|---|---|---|
| Defesa sem Armadura | grátis na Lapidação 1 | — |
| Estímulo Muscular | grátis na Lapidação 1 | — |
| Ímpeto | Destreza 4 | 2 |
| Casco | Constituição 4 | 3 |
| Presilha | Força 4 | 2 |
| Vigília | — | 2 |
| Esteio | — | 3 |
| Faro | — | 1 |
| Sem Pegada | — | 1 |
| Vulto | — | 2 |
| Antecipar | Inteligência 4 | 2 |
| Campo | — | 1 |
| Assombro | Essência 4 | 1 |
| Bênção Própria | uma vez na ficha inteira | 1 ou 2 |

## Bênçãos de graça

Estas duas chegam com a ficha, na Lapidação 1, sem custar marco nenhum.

### Defesa sem Armadura

O golpe chega e o corpo já está no lugar certo, já contraído, já girando com ele em vez de contra. Ela faz a mesma coisa que a `Cobrir-se de energia` do capítulo 11 faz, na mesma faixa, com outro recurso pagando.

> **Defesa sem Armadura** — sem Traje e sem Revestimento, a sua proteção é `1/3 da Lapidação + 1`. Escudo soma com ela.
>
> **Barreira de energia não segura você.** `Barreira Simples` e `Cortina` não valem contra você.
>
> **O Acerto garantido de uma Expansão de Domínio completa não alcança você.** O Efeito continua acontecendo em volta, e uma Expansão incompleta funciona normalmente, porque o Acerto dela rola.
>
> Requisito: grátis na Lapidação 1. A Lapidação escala a proteção.

Ela sai de cena assim que Traje ou Revestimento entram na conta. Em troca das duas linhas acima, quem não tem energia nunca tem Expansão de Domínio.

### Estímulo Muscular

Você aprendeu a mandar no que o corpo faz sozinho. Antes do movimento que decide, você acerta a respiração, trava o que precisa travar e solta o resto.

> **Estímulo Muscular** — escolha **uma perícia** e **um Teste de Resistência** na criação, e eles não mudam.
>
> **`1×` por cena, e `2×` se a sua Lapidação for `10`.** Cada uso dá **vantagem** numa rolagem de um dos dois.
>
> Requisito: grátis na Lapidação 1.

A escolha não precisa ser física. `Ocultismo` mais `Intelecto` é uma ficha tão legítima quanto `Atletismo` mais `Físico`.

## Bênçãos de corpo

### Ímpeto

> **Ímpeto** — como Ação Bônus, você se move até o seu deslocamento sem provocar ataque de oportunidade.
>
> **E o chão deixa de ser obrigatório:** você anda em parede, em água e no ar enquanto estiver se movendo. Se terminar o movimento sem apoio, você cai.
>
> Requisito: Destreza 4. Classe Passiva 2.

### Casco

> **Casco** — você ganha **`+1` de vida a cada dois níveis** e **`+1`** em todo Teste de Resistência de Vigor.
>
> Requisito: Constituição 4. Classe Passiva 3.

### Presilha

> **Presilha** — quando você **falha** numa rolagem para **agarrar, derrubar ou tirar alguém do lugar**, role de novo. Uma vez por rodada.
>
> Requisito: Força 4. Classe Passiva 2.

### Vigília

> **Vigília** — você conta **um degrau de exaustão a menos** do que tem, para todo efeito.
>
> O degrau continua marcado na ficha. O que muda é o que ele cobra de você.
>
> Requisito: nenhum. Classe Passiva 2.

Ela não vira imunidade: a escada de exaustão do capítulo 5 tem três degraus e não tem degrau zero, então o pior caso continua sendo dois. E o descanso longo continua limpando no mesmo ritmo.

### Esteio

> **Esteio** — escolha **um atributo** na criação. Num Teste de Resistência daquele atributo, se o `d20` sair abaixo da sua **Lapidação**, ele vale a sua Lapidação.
>
> **O piso nunca passa do atributo escolhido mais `2`** — então o máximo dele é `8`.
>
> Requisito: nenhum. Classe Passiva 3.

Contra a CD de um conjurador do seu nível o `d20` precisa sempre de 8, e o piso só chega lá quando o atributo escolhido chega a 6. Abaixo disso ele resolve o teste médio e deixa o difícil de pé.

## Bênçãos de perseguição

Duas, e uma anula a outra. Duas fichas desta Origem numa perseguição empatam.

### Faro

> **Faro** — você segue rastro de feiticeiro e de maldição pelo que o corpo deles deixou: cheiro, marca, o que ficou fora do lugar.
>
> **E, encostando no que uma técnica fez, você sabe o superficial do que ela fez ali** — o tipo de coisa que aconteceu, e nunca o detalhe nem de quem é.
>
> Requisito: nenhum. Classe Passiva 1.

Ela não diz onde a coisa está agora e não identifica ninguém. Vestígio é passado.

### Sem Pegada

> **Sem Pegada** — você não deixa rastro físico: pegada, cheiro, marca, som de passo. **Nem `Faro`, nem cão, nem técnica de rastreamento acham por onde você passou.**
>
> Requisito: nenhum. Classe Passiva 1.

Não é furtividade: `Furtividade` continua sendo a perícia, e esta Bênção não soma nada nela. E quem te viu passar continua sabendo — isto apaga o vestígio, não a testemunha.

## Bênçãos de combate

### Vulto

> **Vulto** — você percebe tudo o que estiver a **`1,5 m × metade da Lapidação`** de você sem precisar enxergar.
>
> Requisito: nenhum. Classe Passiva 2.

No teto são 7,5 metros.

### Antecipar

> **Antecipar** — quando você **falha** num Teste de Resistência contra um efeito, você passa a rolar **com vantagem** contra aquele mesmo efeito pelo resto da cena.
>
> Requisito: Inteligência 4. Classe Passiva 2.

O corpo aprende o golpe apanhando dele. Ela não tem limite de uso, e o que a segura é o preço de entrada: sem a falha, ela não liga.

### Campo

> **Campo** — a ação **`Estudar`** custa a sua Ação Bônus em vez da Ação Padrão, **uma vez por cena**.
>
> Requisito: nenhum. Classe Passiva 1.

O `Ler o Ambiente` continua custando o que custava: ele é sobre o lugar, e o `Estudar` é sobre a criatura.

### Assombro

> **Assombro** — uma vez por cena, ao entrar numa cena ou ao ser visto pela primeira vez, escolha uma criatura que enxerga você.
>
> **Ela faz um Teste de Resistência de Espírito contra a CD da sua técnica ou fica `Amedrontado` até o fim do próximo turno dela.**
>
> Requisito: Essência 4. Classe Passiva 1.

A CD é a da sua técnica, do capítulo 9: `8 + atributo da técnica + maestria`. Se o atributo da sua técnica for Essência, a trava do requisito vale — a Essência não entra duas vezes.

## Escrever uma Bênção

### Bênção Própria

A vaga em branco do catálogo: a coisa que o seu personagem descobriu que o corpo dele faz, pequena o bastante para nunca ter virado regra escrita.

> **Bênção Própria** — você escreve, com o mestre, uma Bênção que não está no catálogo. Antes da sessão, e nunca no meio dela. Ela é Classe Passiva 1 ou 2, nunca 3, e você só pode pegá-la uma vez na ficha inteira.
>
> A ficha registra duas coisas: a frase, e a resposta de *"em quantas cenas por arco isso vai importar?"*.
>
> Requisito: uma vez na ficha inteira. Classe Passiva 1 ou 2.

A régua é a mesma da `Aptidão Própria`, no capítulo 11, e vale inteira: uma frase, verificável, sem dado de dano, com limite por cena se for Classe Passiva 2, e não pode repetir uma das doze do catálogo com outro nome nem entregar uma que o seu requisito não alcança.

> **Na dúvida, Pesada.** Pesada é Classe Passiva 3, e a Classe Passiva 3 está fora do que a `Bênção Própria` alcança. Então dúvida reprova a proposta.

E existe uma trava a mais deste lado:

> **Uma Bênção com requisito de Constituição ou de Força não pode ser bônus, vantagem ou rerrolagem numa perícia.** Ela tem de ser **feito**: sobrevivência, recuperação, ou uma coisa que o corpo passa a poder fazer.

---


# Capítulo 13 · Equipamento

*fonte: `manual/50-equipamento.md`*

Equipamento mexe em três coisas: a sua Defesa, o dado que você rola quando bate, e o que dá para fazer com a coisa que está na sua mão. Nenhum item deste capítulo concede técnica.

## Proteção

> **Defesa = 10 + Destreza + proteção.**

Existem duas classes de uniforme, e você usa uma ou outra: **Traje**, que é a leve, e **Revestimento**, que é a pesada. Cada uma tem três degraus.

Feiticeiro trabalha em prédio de escritório, em escola, em estação de metrô, quase sempre com civil por perto e sem tempo de esvaziar o andar. O guarda-roupa sai daí. Escolher entre as duas classes é escolher em que tipo de missão você quer estar confortável.

### Como ler as tabelas de proteção

Os três campos aparecem sempre na mesma ordem.

- **proteção** — o número que soma na sua Defesa.
- **teto de Destreza** — o máximo de Destreza que conta na Defesa enquanto você estiver com aquilo vestido. `—` quer dizer que não tem teto.
- **requer Força** — a Força mínima para vestir. `—` quer dizer que não pede nada.

Se você estiver usando duas coisas com teto de Destreza diferente, vale o menor dos dois.

### Traje

A classe leve. Nenhum degrau trava a sua Destreza, e só o de cima pede Força.

**Traje**
| degrau | proteção | teto de Destreza | requer Força |
|---|---|---|---|
| 1 | 1 | — | — |
| 2 | 2 | — | — |
| 3 | 3 | — | 3 |

Quem fabrica é o ofício **Alfaiate**. Quem não tem o ofício encomenda de quem tem.

Traje é roupa cortada para um corpo só. Alguém tirou as suas medidas, ouviu o que você faz em campo e costurou em cima disso: reforço onde você costuma levar golpe, folga onde você precisa dobrar. De fora ele passa por uniforme escolar, por terno, por jaqueta de trabalho. É o que você veste quando a missão começa no meio de gente que não pode saber o que está acontecendo, e é o que deixa você continuar de pé numa cena de conversa, de infiltração ou de fuga por telhado.

#### Situação do Traje

O Traje é feito sob medida para você, e é aí que mora o benefício dele.

> **Todo Traje carrega uma situação, e é uma só.** Escolha na criação, escreva na ficha como o seu traje é, e quando a cena estiver naquela condição você rola com **vantagem**: joga dois d20 e fica com o melhor. Vantagem não empilha, duas fontes valem uma.

Na prática, você está dizendo ao alfaiate onde costuma se meter. Um traje curto e sem aba para quem vive em vão de ventilação, sola aderente para quem trabalha em beirada, tecido tratado para quem entra em incêndio.

A lista é fechada e vale igual em toda mesa:

**Situação do Traje**
| situação |
|---|
| vão apertado |
| altura e beirada |
| escuro |
| superfície ruim |
| água e chuva |
| multidão |
| terreno instável |
| calor e fogo |

E existe uma vaga aberta: você pode inventar a sua, desde que ela passe nos três itens abaixo. Quem confere é o mestre, e um segundo mestre tem que chegar na mesma resposta.

> 1. É **condição física que o mestre já descreveu na cena**.
> 2. **Não decide o que uma das quatro perícias de Destreza já decide.** Senão vira vantagem em Furtividade pela porta dos fundos.
> 3. **Não acontece toda cena.** O alvo é mais ou menos um disparo por missão.

> **Exemplo.** Você pega **escuro**. Numa perseguição por um prédio sem luz, você rola com vantagem. Numa sala iluminada, o traje não faz nada, e o mestre não precisa julgar se você "usou bem" a roupa, porque a condição já estava descrita na cena antes de você pedir.

### Revestimento

A classe pesada. Todo degrau trava a sua Destreza em 0 na Defesa, e todo degrau pede Força.

**Revestimento**
| degrau | proteção | teto de Destreza | requer Força |
|---|---|---|---|
| 1 | 4 | 0 | 3 |
| 2 | 5 | 0 | 4 |
| 3 | 6 | 0 | 6 |

Revestimento é placa, acolchoamento e peso, montado para aguentar o golpe de frente. Ninguém confunde aquilo com roupa: vestido, você já entrou na cena como uma coisa que a maldição vai ter que resolver. Ele é o uniforme de quem segura a porta enquanto os outros trabalham. Também é o que faz o supervisor esvaziar o quarteirão antes de te mandar entrar, porque com aquilo no corpo você não passa por civil em lugar nenhum, e a missão inteira passa a ser planejada em torno disso.

#### Uniforme e energia amaldiçoada

> **Traje e Revestimento desligam a sua proteção passiva de energia amaldiçoada.** Vestido, a sua proteção é a do uniforme, e só ela. Escudo soma por cima, sempre.

A Reação de cobrir-se continua disponível de uniforme. Ninguém tira o colete no meio do golpe. Ela é a aptidão `Cobrir-se de energia`, e o preço dela está no capítulo 11, *Aptidões e Refino*.

## Escudo

Três degraus. O escudo ocupa uma mão, soma com a sua proteção venha ela de onde vier, e cobra teto de Destreza.

**Escudo**
| degrau | nome | proteção | teto de Destreza | requer Força |
|---|---|---|---|---|
| 1 | **Broquel** | 1 | 5 | — |
| 2 | **Médio** | 2 | 3 | 3 |
| 3 | **Torre** | 3 | 1 | 5 |

O Broquel é de punho, entre 15 e 45 cm: por isso ele quase não come Destreza e não pede Força. A Torre cobre o corpo e se planta no chão. Quanto mais escudo, menos braço sobra.

Fora da rolagem de Defesa, escudo é a peça que decide cena de corredor: com uma Torre plantada no vão de porta, o resto do grupo trabalha atrás de você e a maldição precisa achar outro caminho.

### Escolha do degrau

**Escolha do degrau**
| a sua Destreza | o degrau que rende mais |
|---|---|
| 0 a 1 | Torre |
| 2 a 3 | Médio |
| 4 a 6 | Broquel |

De Revestimento a sua Destreza já não conta na Defesa, então o teto do escudo não te cobra nada: a Torre é a resposta. Na rota sem uniforme, contando com a proteção de energia, o Broquel é o que menos atrapalha.

> **Aviso para quem tem `Selo` = `Gesto`.** Pegar um escudo ocupa a mão e desliga a sua técnica inteira. É o Selo funcionando: se o gesto é obrigatório para conjurar, sem a mão você não conjura. Para essa gente, escudo nunca esteve no menu.
## Armas

São 52, divididas em treze categorias. A categoria diz o que a coisa é, de onde vem o dano dela e em qual lista de treino ela cai.

Nenhuma arma deste catálogo fere maldição sozinha. Contra maldição, o que resolve é energia amaldiçoada no golpe ou uma ferramenta amaldiçoada na mão, que é uma arma daqui mais um `Estigma`, no capítulo 14, *Ferramenta Amaldiçoada*. O catálogo abaixo continua valendo inteiro contra gente, contra bicho e contra parede.

### Como ler uma arma

O `Catálogo de armas` tem seis colunas, nesta ordem:

**arma** · **categoria** · **mão** · **dado** · **propriedades** · **requer Força**

- **arma** — o nome. Nome japonês vem com a tradução entre parênteses.
- **categoria** — a família dela, e é onde o treino mora: treinar uma categoria libera todas as armas dela.
- **mão** — `1` ou `2`. Arma de duas mãos não deixa espaço para escudo.
- **dado** — o dado de dano que você rola quando acerta.
- **propriedades** — o que a arma faz de diferente das outras. As restrições aparecem nessa mesma lista.
- **requer Força** — a Força mínima para empunhar. `—` quer dizer que não pede nada.

### Propriedades

São doze. Propriedade é o que a arma é: ela já está impressa na linha do catálogo, e você nunca escolhe uma na hora de atacar.

**Propriedades**
| propriedade | o que faz |
|---|---|
| `Alcance` | Estica o corpo a corpo. Ver *Alcance no corpo a corpo* |
| `Longo Alcance` | A arma alcança à distância, em metros. Ver *Faixa de projétil* |
| `Duas mãos` | Ocupa as duas mãos, então não sobra mão para escudo. No catálogo ela aparece como o `2` da coluna **mão** |
| `Fineza` | No corpo a corpo, troca Força por Destreza no acerto **e** no dano |
| `Par` | Role dois dados de dano e fique com o melhor |
| `Oculta` | Não muda o seu ataque — é propriedade de fora de combate. **Você esconde a arma no corpo:** um teste de `Prestidigitação`, e ela passa por revista e por detector |
| `Versátil` | Nas duas mãos, o dado sobe um passo: `d6`→`d8`, `d8`→`d10`, `d10`→`d12` |
| `Munição` | Recarregar custa Ação Bônus. Ver *Munição* |
| `Rompe` | Vantagem contra objeto e estrutura |
| `Emaranha` | Você pode `Agarrar` sem largar a arma |
| `Vestida` | Não ocupa a mão |
| `Talha` | A arma é ruim de aparar: **−1** no `Bloquear` de quem se defende |

> **`Talha` é a única das doze ligada ao `Bloquear`**, a rolagem de `2d10` que a sua mesa pode usar no lugar da Defesa estática — o capítulo 17 explica a escolha. Onde a mesa usa a Defesa estática, as nove armas com `Talha` seguem valendo por tudo o mais que elas são: dado, alcance, o resto das propriedades. Só esse `−1` específico não tem onde entrar.

Três delas decidem cena fora de combate com frequência. `Oculta` é a que deixa você entrar armado numa reunião, num velório ou numa portaria com detector. `Rompe` é a que abre cadeado, grade, alçapão e tampa de bueiro sem esperar ninguém. `Vestida` é a que responde quando alguém manda você largar tudo o que está na mão.

### Restrições

Restrição é defeito de verdade. Ela aparece na mesma coluna das propriedades.

**Restrições de arma**
| restrição | o que é |
|---|---|
| `Volumosa` | Não dá para esconder, e atrapalha em espaço apertado |
| `Embainhada` | Não se saca sozinha: precisa de tempo, ou de outra pessoa |
| `Comprida` | Perde no corpo a corpo colado |

Nenhuma das 52 usa a `Comprida` hoje.

### Alcance no corpo a corpo

O padrão de qualquer arma de mão é **1,5 m**. As Armas Longas chegam a **3 m**.

### Faixa de projétil

> **Toda arma de projétil tem duas faixas.**
>
> **Faixa normal** — até o `Longo Alcance` da arma. Ataque normal.
> **Faixa longa** — até o segundo número da tabela. Você rola com **desvantagem**: joga dois d20 e fica com o pior.
> **Além da faixa longa, você não alcança.**
>
> **E tem uma terceira, do outro lado: `colado`.** Atacar com arma de projétil estando adjacente a um inimigo (qualquer inimigo, não só o seu alvo) também é desvantagem.

> **Exemplo.** Você está com a Pistola e o alvo está a 20 metros. A faixa normal dela é 9 m e a longa vai até 27 m: você alcança, e rola com desvantagem. Se um inimigo estiver colado em você na hora do tiro, a desvantagem vale do mesmo jeito, mesmo que o alvo esteja a 5 metros.

**Armas de tiro**
| arma | faixa normal | faixa longa |
|---|---|---|
| Hankyū | 24 m | 96 m |
| Daikyū | 45 m | 180 m |
| Besta de Uma Mão | 9 m | 36 m |
| Besta | 30 m | 120 m |
| Pistola | 9 m | 27 m |
| Revólver | 12 m | 36 m |
| Submetralhadora | 15 m | 45 m |
| Espingarda | 9 m | 27 m |
| Rifle | 24 m | 72 m |
| Rifle de Precisão | 24 m | 72 m |
| Metralhadora Pesada | 24 m | 72 m |

**Armas de arremesso**
| armas | faixa normal | faixa longa |
|---|---|---|
| Punhal · Machadinha · Lança · Kunai · Shuriken · Tessen · Chakram · Kusarigama | 6 m | 18 m |


### Munição

> **Recarregar é Ação Bônus.** Você recarrega quando tirar **1 ou 2 natural** no ataque, **ou** depois de **X** ataques, o que vier primeiro. O X é da arma.

**Munição**
| X | armas |
|---|---|
| 4 | Metralhadora Pesada |
| 3 | Rifle · Submetralhadora |
| 2 | Pistola · Revólver · Espingarda · Rifle de Precisão · Besta · Besta de Uma Mão |

O `Yumi` não carrega `Munição`. Flecha existe na ficção, e uma flecha se encaixa como parte do disparo: não há ciclo de recarga para modelar. Uma besta se arma e um pente se troca, e é disso que a propriedade trata.

> **Exemplo.** Você está com o Rifle, que tem X = 3. Você atira duas vezes sem problema. No terceiro tiro sai um `2` natural no dado de ataque: recarga na sua Ação Bônus, e o tiro seguinte já está pronto.

## Treino de arma

> **Treino mora na categoria.** Treinar uma categoria libera todas as armas dela. São treze categorias em três listas.

**Treino de arma**
| lista | categorias | armas |
|---|---|---|
| **Simples** | Lâmina Curta · Porrete · Ceifa · Arremesso · Manopla · Massa · Balestra | 26 |
| **Marciais** | Lâmina Longa · Machado · Armas Longas · Flexível · Yumi | 19 |
| **Arma de Fogo** | Arma de Fogo | 7 |

> **Bastião e Vanguarda treinam as treze categorias.** Qualquer arma deste catálogo é deles.
>
> **Guia, Emanador e Evocador treinam Arma de Fogo e Balestra**, as duas que se aponta e dispara sem anos de forma.

Um Caminho conjurador não pega espadão de graça: ele precisa da Trilha que concede o grupo, como a `Empunhadura` do `Arremate`. O quadro de cada Caminho está no capítulo 8, *Caminhos e Trilhas*.


> **Sem treino, você tem desvantagem na rolagem de ataque com aquela arma.**
>
> **Sem o requisito de Força dela, o seu deslocamento cai 3 metros enquanto você a estiver empunhando.**

As duas se somam, e somadas elas fecham a porta na prática: quem pega uma arma que não é sua rola pior e anda menos. Não é proibição escrita, e o resultado é quase o mesmo.

## Requisito de Força

> **Força 3 nos dois degraus de cima de cada escada de dado.** No corpo a corpo, `d10` e `d12`. No tiro, `2d8` e `2d10`. São 16 armas das 52.

Três coisas que essa frase decide, e vale ler as três:

- **O requisito lê o dado impresso na linha da arma.** O passo do `Versátil` não conta. Katana, Espada Longa e Taco chegam a `d10` nas duas mãos sem pedir Força nenhuma.
- **O `Yumi` não é com requisito.** As duas ficam no fundo da escada do tiro, e o arco paga em Destreza.
- **Nenhuma arma pede mais que Força 3**, que é o teto da criação. O requisito resolve acesso: quem investiu Força não paga nada a mais por arma nenhuma. O único item deste capítulo que pede acima disso é o escudo **Torre**, com Força 5.

O requisito e o treino são requisitos diferentes e não se substituem. Um olha o seu corpo, o outro olha o que você aprendeu. Um Emanador com Força 6 passa no primeiro e para no segundo.

## Catálogo

O `Catálogo de armas` traz as 52 armas com tudo que decide o golpe, em três blocos, um por lista de treino. Depois dele vem o índice por propriedade, para quando você sabe o que quer que a arma faça e não qual é o nome dela. As treze categorias, no fim, dizem o que cada família é na mão e na cena.

### Armas por treino

**Catálogo de armas**
| arma | categoria | mão | dado | propriedades | requer Força |
|---|---|---|---|---|---|
| **Treino simples** | | | | | |
| Bastão | Porrete | 1 | **d6** | `Versátil` · `Alcance` · `Rompe` | — |
| Besta | Balestra | 2 | **2d8** | `Longo Alcance` · `Munição` · `Rompe` | 3 |
| Besta de Uma Mão | Balestra | 1 | **1d10** | `Longo Alcance` · `Munição` · `Oculta` | — |
| Bō | Porrete | 2 | **d10** | `Alcance` · `Emaranha` | 3 |
| Canivete | Lâmina Curta | 1 | **d4** | `Fineza` · `Oculta` · `Rompe` | — |
| Cassetete | Porrete | 1 | **d6** | `Oculta` · `Vestida` | — |
| Chakram | Arremesso | 1 | **d4** | `Longo Alcance` · `Fineza` · `Oculta` | — |
| Faca | Lâmina Curta | 1 | **d6** | `Fineza` · `Rompe` | — |
| Foice | Ceifa | 2 | **d10** | `Emaranha` · `Talha` | 3 |
| Kama | Ceifa | 1 | **d6** | `Par` · `Rompe` | — |
| Kanabō | Massa | 2 | **d12** | `Talha` | 3 |
| Kunai | Arremesso | 1 | **d6** | `Longo Alcance` · `Oculta` | — |
| Kusarigama | Ceifa | 2 | **d8** | `Alcance` · `Emaranha` · `Longo Alcance` | — |
| Maça | Massa | 1 | **d8** | `Talha` | — |
| Marreta | Massa | 2 | **d10** | `Rompe` · `Talha` | 3 |
| Maul | Massa | 2 | **d12** | `Rompe` | 3 |
| Nunchaku | Porrete | 1 | **d6** | `Par` · `Emaranha` | — |
| Punhal | Lâmina Curta | 1 | **d6** | `Fineza` · `Longo Alcance` | — |
| Sai | Lâmina Curta | 1 | **d6** | `Fineza` · `Par` | — |
| Shuriken | Arremesso | 1 | **d4** | `Longo Alcance` · `Oculta` · `Par` | — |
| Soqueira | Manopla | 1 | **d4** | `Vestida` · `Oculta` · `Par` | — |
| Taco | Massa | 1 | **d8** | `Versátil` · `Oculta` | — |
| Tanto | Lâmina Curta | 1 | **d6** | `Fineza` · `Oculta` | — |
| Tekko | Manopla | 1 | **d4** | `Vestida` · `Par` · `Oculta` | — |
| Tessen | Arremesso | 1 | **d4** | `Longo Alcance` · `Oculta` · `Vestida` | — |
| Tonfa | Porrete | 1 | **d6** | `Par` · `Vestida` | — |
| **Treino marcial** | | | | | |
| Chicote | Flexível | 1 | **d4** | `Alcance` · `Emaranha` · `Oculta` | — |
| Corrente | Flexível | 2 | **d8** | `Alcance` · `Emaranha` · `Rompe` | — |
| Daikyū | Yumi | 2 | **1d10** | `Longo Alcance` | — |
| Espada Longa | Lâmina Longa | 1 | **d8** | `Versátil` · `Rompe` | — |
| Espadão | Lâmina Longa | 2 | **d12** | `Alcance` | 3 |
| Hankyū | Yumi | 2 | **1d8** | `Longo Alcance` · `Oculta` | — |
| Katana | Lâmina Longa | 1 | **d8** | `Versátil` · `Fineza` | — |
| Lança | Armas Longas | 1 | **d6** | `Alcance` · `Longo Alcance` | — |
| Machadinha | Machado | 1 | **d6** | `Longo Alcance` · `Rompe` | — |
| Machado | Machado | 1 | **d8** | `Rompe` | — |
| Machado de Guerra | Machado | 2 | **d12** | `Rompe` · `Talha` · `Volumosa` | 3 |
| Machete | Lâmina Longa | 1 | **d8** | `Rompe` | — |
| Manriki | Flexível | 1 | **d6** | `Emaranha` · `Oculta` | — |
| Naginata | Armas Longas | 2 | **d10** | `Alcance` · `Rompe` | 3 |
| Nodachi | Lâmina Longa | 2 | **d12** | `Alcance` · `Rompe` · `Volumosa` | 3 |
| Odachi | Lâmina Longa | 2 | **d12** | `Alcance` · `Talha` · `Embainhada` | 3 |
| Rapieira | Lâmina Longa | 1 | **d6** | `Fineza` · `Talha` | — |
| Wakizashi | Lâmina Longa | 1 | **d8** | `Oculta` | — |
| Yari | Armas Longas | 2 | **d10** | `Alcance` · `Talha` | 3 |
| **Treino de fogo** | | | | | |
| Espingarda | Arma de Fogo | 2 | **2d8** | `Longo Alcance` · `Munição` · `Rompe` | 3 |
| Metralhadora Pesada | Arma de Fogo | 2 | **2d10** | `Longo Alcance` · `Munição` · `Rompe` · `Volumosa` | 3 |
| Pistola | Arma de Fogo | 1 | **1d10** | `Longo Alcance` · `Munição` · `Oculta` | — |
| Revólver | Arma de Fogo | 1 | **1d10** | `Longo Alcance` · `Munição` · `Oculta` | — |
| Rifle | Arma de Fogo | 2 | **2d8** | `Longo Alcance` · `Munição` · `Talha` | 3 |
| Rifle de Precisão | Arma de Fogo | 2 | **2d10** | `Longo Alcance` · `Munição` | 3 |
| Submetralhadora | Arma de Fogo | 2 | **2d6** | `Longo Alcance` · `Munição` · `Par` · `Oculta` | — |
### Índice por propriedade

**Índice por propriedade**
| propriedade | armas |
|---|---|
| `Alcance` | Espadão · Odachi · Nodachi · Bastão · Bō · Kusarigama · Naginata · Yari · Lança · Corrente · Chicote |
| `Longo Alcance` | Punhal · Machadinha · Lança · Kunai · Shuriken · Tessen · Chakram · Kusarigama · e as onze de tiro |
| `Fineza` | Tanto · Punhal · Canivete · Faca · Sai · Rapieira · Katana · Chakram |
| `Par` | Sai · Tonfa · Nunchaku · Soqueira · Tekko · Kama · Shuriken · Submetralhadora |
| `Oculta` | Tanto · Canivete · Wakizashi · Taco · Cassetete · Soqueira · Tekko · Chicote · Manriki · Kunai · Shuriken · Tessen · Chakram · Hankyū · Besta de Uma Mão · Pistola · Revólver · Submetralhadora |
| `Versátil` | Katana · Espada Longa · Taco · Bastão |
| `Munição` | Besta · Besta de Uma Mão · Pistola · Revólver · Submetralhadora · Espingarda · Rifle · Rifle de Precisão · Metralhadora Pesada |
| `Rompe` | Canivete · Faca · Machete · Espada Longa · Nodachi · Marreta · Maul · Bastão · Machado · Machado de Guerra · Machadinha · Kama · Naginata · Corrente · Besta · Espingarda · Metralhadora Pesada |
| `Emaranha` | Bō · Nunchaku · Foice · Kusarigama · Corrente · Chicote · Manriki |
| `Vestida` | Cassetete · Tonfa · Soqueira · Tekko · Tessen |
| `Talha` | Rapieira · Odachi · Maça · Marreta · Kanabō · Machado de Guerra · Foice · Yari · Rifle |
| `Volumosa` | Nodachi · Machado de Guerra · Metralhadora Pesada |
| `Embainhada` | Odachi |
| `Comprida` | nenhuma |

### Lâmina Curta

Treino simples. Todas carregam `Fineza`, então o dano delas sai de Destreza.

Lâmina curta é briga de distância zero. Você entra por dentro da guarda, encosta e corta, e o que decide o golpe é leitura de corpo e mão rápida. É também a categoria que passa por qualquer lugar sem levantar pergunta: uma faca cabe no bolso do casaco e continua lá durante a entrevista inteira.


### Lâmina Longa

Treino marcial. O dano sai de Força, ou de Destreza nas duas que carregam `Fineza`.

Lâmina longa se luta com o corpo inteiro: o pé escolhe a distância, o quadril faz o corte, e o braço só entrega. As de uma mão deixam a outra livre para escudo, para segurar alguém ou para fechar um selo. As de duas trocam essa mão por alcance e por dado grande, e quem empunha uma delas está declarando que não pretende se esconder de ninguém.


Odachi e Nodachi são a mesma lâmina longa demais para o cinto, com a mesma mão e o mesmo dado. A diferença está em como cada uma resolve o tamanho: o Odachi se carrega nas costas e precisa de tempo ou de ajuda para sacar, o Nodachi você saca sozinho e carrega à mostra. Se a sua mesa costuma começar cena já em briga, o Odachi vai chegar atrasado em algumas delas.

### Massa

Treino simples. O dano sai de Força.

Massa fere com peso chegando rápido, e peso não perde o fio. É a arma que continua funcionando depois de uma noite inteira batendo em concreto, e a que menos se importa com o que o alvo vestiu por cima.


### Porrete

Treino simples. O dano sai de Força.

Porrete é madeira e controle. Você acerta, empurra, prende, afasta e a cena continua com todo mundo vivo. É a categoria de quem trabalha perto de civil e precisa poder errar o alvo sem abrir um buraco na parede.


### Manopla

Treino simples. O dano sai de Força.

Manopla é o soco com uma peça de metal por cima. Ela vai vestida: você chega de mãos vazias em qualquer portaria e continua armado do outro lado. Quem luta assim briga colado, e usa o corpo inteiro como parte da arma.


O Tekko e a Soqueira têm a mesma linha, o mesmo gasto e a mesma regra. O que muda é de onde cada uma veio.

### Machado

Treino marcial. O dano sai de Força.

Machado concentra o peso na ponta e cobra o gesto inteiro: quem erra fica aberto por um instante. Em compensação, o que ele acerta ele abre, e isso vale para porta trancada, grade e assoalho tanto quanto para o que estiver do outro lado.


O Machado tem a mesma linha do Machete, lá na Lâmina Longa: `d8`, uma mão, `Rompe`. A escolha entre os dois é de sabor, e as duas categorias caem no mesmo balde de treino.

### Ceifa

Treino simples. O dano sai de Força.

Ceifa puxa. A curva da lâmina engancha braço, perna, cano de andaime e o cabo da arma do outro, e o golpe costuma terminar com o alvo mais perto de você do que ele gostaria. É a categoria de quem prefere escolher onde o inimigo vai estar.


### Armas Longas

Treino marcial. O dano sai de Força. É a única categoria em que o `Alcance` chega a 3 m.

Arma longa serve para decidir a distância. Você mantém a coisa a três metros e ela gasta o turno inteiro só para chegar ao ponto onde a luta começaria. Em corredor e em vão de porta, uma lança sozinha segura uma passagem enquanto o resto do grupo faz o trabalho.


### Flexível

Treino marcial. O dano sai de Força.

Corrente e chicote fazem curva. O golpe contorna guarda, escudo e quina de parede, e ninguém aprende a ler a trajetória numa luta só. O dado é pequeno em todas as três: o que a categoria entrega é alcance e `Emaranha`.


### Arremesso

Treino simples. O dano sai de Força: o arremesso sai do corpo.

Arremesso resolve seis metros na hora, sem trocar de arma e sem sair da briga de perto. Todas as quatro escondem, e todas cabem numa cena em que você precisa acertar alguma coisa do outro lado da sala antes que ela termine de se virar.


### Yumi

Treino marcial. O dano sai de Destreza: o arco se puxa, e puxar é coisa do corpo. As duas rolam um dado só e nenhuma delas carrega `Munição`.

Yumi é o arco japonês, assimétrico e alto, puxado até passar da orelha. Atirar com ele é postura e respiração antes de ser mira. O disparo sai calado, e é isso que faz um arco resolver um vigia no fim do corredor sem acordar os outros três.


O daikyū passa de dois metros e se carrega nas costas. O hankyū fica entre 45 e 160 cm: é o arco de espaço apertado e de montaria, e é por isso que ele esconde e o outro não. O Daikyū tem o dado maior; o Hankyū tem a propriedade a mais.

### Balestra

Treino simples. **Não soma atributo nenhum**: a energia já está armazenada na corda, e você só precisa mirar. Em troca, o dado é maior.

A besta guarda a força por você. Quem atira aponta e solta, e por isso ela é a arma que qualquer um do grupo pega emprestada e usa igual. O preço vem depois do disparo, na hora de armar de novo.


### Arma de Fogo

Lista de treino própria, sozinha. **Não soma atributo nenhum**, pelo mesmo motivo da Balestra.

Arma de fogo resolve distância e barulho no mesmo gesto. Ela cobra treino próprio e devolve o tiro mais rápido do catálogo, com o custo de que a cena discreta acaba no primeiro disparo: a partir dali existe polícia, existe testemunha e existe relatório para alguém escrever depois.


Pistola e Revólver têm a mesma linha de regra. A diferença entre os dois está na faixa: a Pistola vai a 9 m, o Revólver a 12 m.

## Soco

O punho vazio não é uma das 52. Ele não entra no catálogo, não tem categoria e não entra na divisão simples/marcial.

> **O soco não tem propriedade nenhuma. O dado dele sobe com a maestria.**
>
> | maestria | níveis | dado |
> |---|---|---|
> | 1 | 2 a 9 | **d4** |
> | 2 | 10 a 17 | **d6** |
> | 3 | 18 a 25 | **d8** |
> | 4 | 26 a 30 | **d10** |

Ele soma Força, como todo corpo a corpo. E vale como arma para todo efeito de regra: crítico, ataque extra, requisito de treino.

O requisito de Força não pega o soco. Ele existe para arma que você levanta, e não tem como alguém não alcançar o próprio punho.

O soco não tem propriedade nenhuma, então ele abre mão de alcance, de `Par`, de `Oculta` e de todo o resto. Em troca, ninguém desarma um punho e ninguém confisca um punho na portaria: a condição `Desarmado` não alcança quem bate com a mão.

---


# Capítulo 14 · Ferramenta Amaldiçoada

*fonte: `manual/55-ferramenta-amaldicoada.md`*

> **Uma ferramenta amaldiçoada é uma arma do catálogo de Equipamento (ou um objeto de apoio) mais um `Estigma`.**
>
> **Ela fere maldição. Isso é sim ou não, sem meio-termo.**
>
> **Uma ferramenta que você não sintonizou é arma comum, e nada mais.**

Ferir maldição é a porta que separa o feiticeiro de quem não tem energia amaldiçoada. Quem conjura já atravessa essa porta de graça, pelo feitiço de Toque. Quem não conjura só atravessa com ferramenta na mão.

## Ferramenta forjada

Uma ferramenta amaldiçoada é um objeto que alguém encheu de energia amaldiçoada de propósito, martelada por martelada, até o material aprender a segurar aquilo. Isso leva tempo, custa a energia de quem forja e não sai barato: quem tem o ofício é pouca gente, trabalha por encomenda e conhece o nome de quase todas as peças boas que estão circulando. Ferramenta boa tem procedência, tem dono anterior e tem gente que se lembra dela.

Para quem tem energia amaldiçoada, uma ferramenta é conveniência: uma lâmina que já corta maldição poupa o que você gastaria cobrindo o próprio punho. Para quem não tem, ela é o passaporte. Sem ferramenta, um corpo humano bem treinado atravessa uma maldição como atravessa fumaça, e a maldição continua ali, do outro lado, olhando. Com uma ferramenta de grau 4 na mão, a mesma pessoa entra na luta que o feiticeiro está lutando. É por isso que ninguém do meio jujutsu empresta ferramenta de bom grado.

> **Como se sintoniza uma ferramenta está sendo escrito.** Quanto tempo leva, o que se gasta e se dá para desfazer é acordo com o seu mestre por enquanto.

A arma por baixo continua sendo a arma de sempre: ela custa os mesmos pontos que qualquer outra do catálogo, `3` numa mão e `5` em duas. O `Estigma` entra como camada por cima disso, e não devolve nem cobra ponto de arma.

Uma ferramenta carrega **um** `Estigma`. Nunca dois.

## Ferramenta e objeto amaldiçoado

São duas coisas, e o meio jujutsu separa as duas por escrito: tirando as ferramentas amaldiçoadas e os cadáveres amaldiçoados, todo item que contém energia amaldiçoada é chamado de objeto amaldiçoado.

**Ferramenta e objeto amaldiçoado**
| É ferramenta amaldiçoada | É objeto amaldiçoado |
|---|---|
| foi forjada para canalizar energia | é a maldição presa numa forma de objeto |
| você empunha, e ela fere maldição | você carrega, e o que está dentro dele age |
| a espada, o machado, a corrente | o cubo que prendeu o Gojo |

Os dois são ranqueados pela mesma escada, pela força da energia que carregam: grau 4 a grau 1, mais o especial. O que muda é o que cada um é.

> Objeto amaldiçoado é outro assunto, e está sendo escrito.

## Grau

O que o grau escolhe é o **formato** do `Estigma`: se ele é pequeno e condicional, se é reativo com limite de uso, ou se é permanente.

**Graus de ferramenta**
| Grau | `Estigma` | Nível mínimo | Exemplar do material |
|---|---|---|---|
| **4** | nenhum. Ela fere maldição, e para nisso | nenhum | a katana da Kasumi, a semi-ferramenta |
| **3** | Classe 1: efeito pequeno, condicional ou de informação | nenhum | a espada do Toji, o machado da Mei Mei |
| **2** | Classe 2: reativo, com limite por cena ou por descanso | 7 | a Katana de Alma Partida |
| **1** | Classe 3: permanente, muda como você joga | 13 | as forjadas de topo |
| **especial** | Classe 3, e ela é única no mundo | 13 | Nuvem Divertida · Lança Invertida do Céu · Corrente de Mil Milhas |

As Classes são as mesmas do capítulo 11, *Aptidões e Refino*, e o nível mínimo é o de lá: uma aptidão de Classe 2 pede nível 7, uma de Classe 3 pede nível 13, e Classe 1 não pede nada.

### Grau e refino

Não existe requisito de refino para ferramenta amaldiçoada. Ela é a rota de quem tem pouca energia amaldiçoada, ou nenhuma.

### Grau 4

Ele não dá `Estigma` nenhum. Ferir maldição é a única coisa que um personagem sem energia amaldiçoada não consegue sozinho. Uma ferramenta de grau 4 é o que põe essa pessoa na mesma luta que o feiticeiro.

Na mesa, esse degrau costuma ser a primeira peça que muda a cara de um personagem inteiro. Antes dela, o cara com a espingarda estava ali para tirar civil do prédio; depois dela, ele tem um alvo.

### Grau 1 e especial

Os dois dão um `Estigma` de Classe 3 e os dois pedem nível 13. A diferença é de ficção: uma ferramenta de grau 1 se forja, e uma especial é uma só que existe no mundo inteiro, com nome próprio e história conhecida. Quem carrega uma especial carrega junto a história dela: gente vai reconhecer a peça antes de reconhecer você.

As três especiais citadas acima entram como exemplar, e nenhuma delas tem ficha escrita: quem quiser pôr uma em jogo monta com o mestre, dentro do que a Classe 3 permite.

### Grau e patente

> **A sua patente não decide que ferramenta você pode portar. A ferramenta que você porta não mexe na sua patente.**

São duas escadas de cinco casas com o mesmo nome, e elas não se encostam em lugar nenhum. Patente é reconhecimento; grau é a energia que a peça carrega.

## `Desgaste`

> **`Desgaste`: a ferramenta ignora o nível mínimo do `Estigma` dela.**
>
> **Em troca, ela se gasta: a cada missão em que o `Estigma` foi usado, ela desce um grau. No grau 4 ela vira arma comum. Ela não volta.**

Uma ferramenta com `Desgaste` é a peça que já foi usada demais por outra pessoa antes de chegar em você: ela ainda faz o que faz, e cada vez que faz, faz um pouco menos. Dá para ver acontecendo, e a mesa costuma tratar isso como relógio de campanha.

O `Desgaste` compra o nível mínimo, e só ele. Ele nunca sobe a Classe do `Estigma`: Classe é formato, e formato não está à venda.

Uma ferramenta de grau 1 com `Desgaste` dura **três missões** de uso antes de virar arma comum.

> **Exemplo.** O Ryo é nível 4 e ganha uma corrente de grau 1 com `Desgaste`. O `Estigma` dela é `Anátema`, que pediria nível 13; com o `Desgaste`, ele usa hoje. Na primeira missão ele encosta a corrente numa técnica e anula o efeito: fim da missão, a corrente desce para grau 2. Na segunda ele usa de novo: grau 3. Na terceira: grau 4, e o que sobra na mão dele é uma corrente que fere maldição e nada mais. Se ele tivesse guardado o `Anátema` para a missão que importava, teria três usos para gastar em três momentos escolhidos.

## Teto de `Estigma`

> **A arma tem teto pelas mãos. O apoio tem teto de dois.**

**Objeto de apoio** é a ferramenta que você carrega sem empunhar: um anel, um cordão, uma peça costurada no forro do casaco. A lista do que conta como apoio e o preço dele estão sendo escritos; o teto de dois já vale desde agora.

**Teto de `Estigma`**
| A ficha carrega | `Estigmas` |
|---|---|
| arma de grau 4, sem apoio nenhum | 0 |
| uma arma com `Estigma` | 1 |
| **uma arma mais dois apoios: o teto declarado** | **3** |
| duas armas de uma mão mais dois apoios | 4 |

Não existe ficha com cinco ferramentas: as mãos fecham um lado e o teto de dois apoios fecha o outro.

## Catálogo de `Estigma`

Onze entradas, agrupadas por Classe. A Classe diz o grau da ferramenta que pode carregar aquele `Estigma`, e diz o nível mínimo junto.

### Como ler uma entrada

Cada tabela de Classe traz o nome e **quando o `Estigma` age**: sempre ligado, na hora de um gatilho, ou como Reação. Quando existe limite de uso, ele aparece na coluna do relógio. O texto embaixo da tabela é a regra inteira.

### Classe 1 · grau 3 · sem nível mínimo

**`Estigma` de Classe 1**
| `Estigma` | Quando age |
|---|---|
| `Fiel` | no seu turno |
| `Aferido` | ao encostar numa maldição |
| `Presságio` | sempre |
| `Perene` | sempre |

> **`Fiel`** — ela volta para a sua mão no seu turno. Não dá para te desarmar dela. Você a solta na queda, rola por três metros de escada e ela está de volta no seu punho antes de você terminar de levantar.
>
> **`Aferido`** — ao encostar numa maldição, você sabe o grau dela. A instituição classifica maldição por grau, e ninguém acerta isso olhando de longe. O primeiro toque já responde a pergunta que decide se o grupo fica ou pede reforço.
>
> **`Presságio`** — ela avisa que tem maldição perto, antes de você ver. Um zumbido no metal, um puxão na bainha, o cabo esfriando na mão. Numa investigação, é ela que diz em qual andar do prédio a coisa mora.
>
> **`Perene`** — ela não quebra, não enferruja e funciona onde arma comum não funciona. Sai de baixo d'água, do fogo e de dez anos num porão com a mesma cara de sempre.

### Classe 2 · grau 2 · nível 7

**`Estigma` de Classe 2**
| `Estigma` | Quando age | Relógio |
|---|---|---|
| `Quebranto` | Reação | por cena |
| `Avulsa` | Reação | *não declarado* |
| `Bojo` | no seu turno | por descanso curto |

> **`Quebranto`** — Reação: anula um feitiço que ia te acertar. Uma vez por cena. Você levanta a arma no caminho do golpe e ele termina ali, na lâmina, sem chegar em você.
>
> **`Avulsa`** — Reação: a arma sai da sua mão e faz o ataque sozinha. Ela solta do punho, cruza o vão e trabalha no lugar onde você não conseguiria estar a tempo. **O limite de uso dela está sendo escrito**; até fechar, combine um com o seu mestre.
>
> **`Bojo`** — uma vez por descanso curto, ela guarda um feitiço que você lançou e devolve ele depois, sem custo de PE. O feitiço fica dentro dela como um eco esperando a hora. É o único dos onze que só serve para quem conjura.

### Classe 3 · grau 1 e especial · nível 13

**`Estigma` de Classe 3**
| `Estigma` | Quando age |
|---|---|
| `Anátema` | ao encostar |
| `Cisão` | sempre |
| `Insondável` | enquanto a ponta dela estiver escondida |
| `Contrapeso` | sempre |

> **`Anátema`** — o contato dela anula técnica amaldiçoada. Encostou, apagou. Numa cena montada em cima de uma técnica (a sala que se dobra, a corrente de água que persegue), esta é a peça que desmonta a cena inteira.
>
> **`Cisão`** — o golpe dela causa dano de alma no lugar do dano de vida. O corpo do alvo não mostra nada, e o que rasga está por baixo. É uma troca: contra alvo de alma dura, você vai sentir falta do dano normal.
>
> **`Insondável`** — enquanto a ponta dela estiver escondida, o alcance dela é **na cena**. Enquanto ninguém consegue ver onde a lâmina termina, ela termina onde você quiser. As três faixas de alcance estão no capítulo 15, *Invocações*.
>
> **`Contrapeso`** — ela ignora o requisito de Força da arma. Qualquer um empunha, e o peso da coisa se resolve sozinho na mão de quem a segura.

## Ritmo de entrega

O único nível mínimo obrigatório é o do `Estigma`, na tabela de grau.

**Ritmo de entrega**
| Grau | Nível sugerido | Faixa, se a mesa preferir espalhar |
|---|---|---|
| 4 | **2** | 2 a 6 |
| 3 | **10** | 7 a 12 |
| 2 | **18** | 13 a 17 |
| 1 | **26** | 18 a 23 |
| especial | **30** | 24 a 29 |

Uma ferramenta por faixa de grau, entregue nesse ritmo, dá cinco na campanha inteira. Cada uma delas rende cena própria: onde estava guardada, de quem era, e o que a pessoa que a perdeu vai querer fazer a respeito.

> **Uma especial aparece uma vez por arco.** O que segura o topo desta escada é escassez: cada uma delas é única no mundo, e o mundo não fabrica mais.

---


# Capítulo 15 · Invocações

*fonte: `manual/60-invocacoes.md`*

Uma invocação é um corpo que anda no campo por sua conta e obedece você: um shikigami, um talismã que vira bicho, uma maldição que você domou. Ela se monta gastando um orçamento de pontos, numa mini ficha bem menor que a do seu personagem.

Quem ganha o corpo é quem tem uma das três Trilhas do Evocador. **O que a Trilha concede não sai do orçamento**: ela entrega quantos corpos você tem e quanta vida cada um aguenta, e o orçamento desta página compra capacidade por cima disso. As três Trilhas estão no capítulo 8, *Caminhos e Trilhas*, com o número de cada uma. Nada na regra abaixo depende de ser Evocador: ela vale para qualquer ficha que ganhe uma invocação, venha ela de onde vier.

## Regra rápida do turno

Comece por aqui. Isto é o que você precisa saber para jogar com uma invocação já montada; o resto do capítulo é para montá-la.

> **Invocar custa `1 × a sua maior Classe` de PE e a sua Ação Padrão.**
> **Comandar a invocação custa a sua Ação Padrão, toda rodada.** Sobram o seu movimento, a sua Ação Bônus e a sua Reação.
> **A invocação usa o seu número de iniciativa e age logo depois de você.** Ela não abre uma casa nova na ordem, nem com um corpo nem com cinco.
> **Ela tem de ficar a até 18 metros de você.** Mais longe que isso ela não pode ser comandada: fica onde está, sem agir, até voltar ao alcance. Ela não some.

Não existe "a primeira do dia é grátis". **Fora de combate, ação não custa nada**, e é aí que mora a diferença: quem invoca antes da luta paga só os PE e entra em campo com a invocação de pé. Quem é pego sem ela paga os PE **e** a Ação Padrão da primeira rodada.

> **Exemplo.** O Kaito está no nível 10 e a maior Classe dele é `3`, então invocar custa `3` PE. Ele entra no prédio abandonado com a invocação já de pé, porque invocou no carro e ali a ação não custou nada. Na rodada 1 da luta ele gasta a Ação Padrão comandando: a invocação ataca. Ele ainda anda `9` metros e usa a Ação Bônus dele. Na rodada 2 ele decide bater ele mesmo, e nesse turno a invocação não faz nada, porque ninguém a comandou.

### Presença em campo



Fora de combate a conta some e a invocação vira mão de obra. Ela entra no duto na frente do grupo, fica de vigia a noite inteira na única porta que ninguém quer atravessar, carrega o ferido até a rua, cava o que precisa ser cavado. Uma boa parte do valor de uma invocação nunca aparece numa rolagem de ataque.

### Teto

**Rotina** é o dano que um personagem entrega numa rodada comum, sem gastar recurso guardado — a saída de um turno normal, sem Liberação Máxima e sem Técnica Máxima.

**Teto de Rotina**
| Seu nível | 1 a 4 | 5 a 8 | 9 a 12 | 13 a 16 | 17 a 20 | 21 a 25 | 26 a 30 |
|---|---|---|---|---|---|---|---|
| **Rotina** | 13 | 31 | 45 | 63 | 76 | 94 | 108 |

É contra esse número que o teto abaixo se mede.

> **Você e todas as suas invocações somados entregam uma Rotina.**
> Com uma invocação, cada um entrega metade. Com três, cada um entrega um quarto.

A conta se fecha sozinha na mesa: comandar custa a sua Ação Padrão, então numa rodada ou você bate ou elas batem. Não dá para somar os dois.

**Só a Trilha `Coro` escapa disso**: ela ataca e comanda na mesma rodada. O texto dela está no capítulo 8, *Caminhos e Trilhas*.

## Ficha da invocação

A ficha dela é derivada da sua: cada linha ou copia um número seu, ou sai de uma fórmula. Você não rola atributo nem escolhe Caminho para ela.

### Metades da ficha

> **Linha que encara dado** (acerto, Defesa, Teste de Resistência) **= o seu número**, com um deslocamento fixo por cima.
> **Linha fora de dado** (vida, movimento) **= fórmula própria, com o atributo dela dentro.**

A invocação tem atributos, e eles valem nas linhas de fora do dado: a Constituição dela entra na vida, e a Força e a Destreza dela entram como deslocamento. Os três deslocam o número uma vez e param por aí. Nenhum deles faz a invocação crescer mais rápido que você ao longo da campanha.

### Deslocamento

> **A invocação começa no seu número e só pode descer.**

**Deslocamento**
| a ficha faz | custa ou devolve |
|---|---|
| fica no seu número | `0` |
| `−1` de acerto | **devolve `4` pontos** |
| `−1` de Defesa | **devolve `4` pontos** |
| `+1` em qualquer linha | **proibido** |

Vender número é a única moeda extra que existe: fora do orçamento, não há outro jeito de comprar capacidade.

### Tipos e vida

Toda invocação é de um dos quatro tipos, e o tipo é o que decide a base da vida dela.

> **`vida = base do tipo + (2 + a Constituição dela) × o seu nível`**

**Tipos e vida**
| tipo | base | nível 2 | nível 10 | nível 18 | nível 30 |
|---|---|---|---|---|---|
| `talismã` · `corpo amaldiçoado` | `1` | 5 | 21 | 37 | 61 |
| `técnica` | `2` | 6 | 22 | 38 | 62 |
| `maldição domada` | `3` | 7 | 23 | 39 | 63 |

*As colunas de nível mostram a conta com a Constituição dela em `0`. Cada ponto de Constituição soma o seu nível inteiro à vida.*


O tipo também decide o que a mesa vê chegar. Um `talismã` é papel que se desdobra e cresce. Um `corpo amaldiçoado` é carne que já foi de alguém. Uma invocação de `técnica` é feita da sua própria energia, e some do jeito que veio. Uma `maldição domada` é uma coisa que quis te matar antes de aceitar andar do seu lado, e todo mundo na cena sabe disso.

A vida de um corpo é o que o capítulo 8, *Caminhos e Trilhas*, chama de **`h`** quando escreve a vida que cada Trilha concede.

### Orçamento

O orçamento é o que você gasta comprando `Traço` e `Comando`. Ele cresce nos mesmos marcos que governam atributo, refino e feitiço.

> **O orçamento é `8` no nível 2, e cada marco dá `+4`.**

**Orçamento**
| nível | marcos | orçamento | o que dá para montar |
|---|---|---|---|
| 2 | 0 | **8** | dois `Traço` baratos, ou um dos caros |
| 6 | 1 | 12 | três baratos, ou um caro mais um barato |
| 10 | 2 | 16 | dois dos caros |
| 18 | 4 | 24 | três |
| 26 | 6 | 32 | quatro |
| 30 | 7 | **36** | quatro e folga |

O orçamento compra capacidade: três `Traço` não sobem o seu acerto nem o dano dela. O teto de uma Rotina já governa a saída.

### Limites do orçamento

Estas três não têm preço em ponto nenhum, e nenhum mestre pode inventar um.

**Limites do orçamento**
| não pode | por quê |
|---|---|
| **dado de dano** | o teto de uma Rotina já governa a saída. Um `Traço` que dê `+1d6` não existe a preço nenhum |
| **qualquer coisa que cresça com refino** | refino cresce muito mais rápido que a ficha dela, e ela passaria de você |
| **deslocamento positivo** | a invocação não passa de quem a carrega |

E nada do catálogo pode dar Defesa, acerto ou vida direto. Esses três já são a moeda do deslocamento, e comprá-los de novo por ponto seria pagar duas vezes pela mesma coisa.

## Catálogo

> **`Traço` é o que ela é.** Sempre ligado, sem gastar nada.
> **`Comando` é o que ela faz** quando você gasta a Ação Padrão nela.

`Traço` é o corpo dela. Quem olha a invocação já vê os `Traço` antes de ela fazer coisa nenhuma: as asas estão lá, o tamanho está lá, o focinho está lá. `Comando` é a ordem, e a ordem aparece na mesa do jeito que a sua mesa combinar (você fala, você aponta, você assobia, ou você só quer). Vale escrever na ficha como a sua invocação recebe ordem, junto com o resto.

São 19 entradas compráveis, mais o `Investir`, que custa `0` e toda invocação tem.

### Como ler as tabelas

Cada linha diz quanto ela custa do orçamento, o nome que vai na ficha, e o efeito inteiro. Não há requisito em nenhuma delas, tirando a faixa mais longa do `Remoto`, que está adiante neste capítulo.

### `Traço`

**Traço**
| pontos | `Traço` | o que faz |
|---|---|---|
| **2** | `Escalada` | sobe parede e teto sem teste. Ela anda no reboco como anda no chão |
| **2** | `Nado` | move na água sem penalidade. Rio, cisterna, tanque alagado de estação |
| **3** | `Fala` | ela fala, e dá para conversar com ela. Ela também responde a quem não é você, o que nem sempre te ajuda |
| **5** | `Faro` | rastreia por cheiro e por energia. Pega rastro velho de horas |
| **5** | `Vigia` | o que ela vê e ouve, **você** vê e ouve. Você fica parado num lugar seguro e olha pelos olhos dela |
| **7** | `Miúdo` | ocupa espaço menor e passa por vão. Duto, grade de bueiro, folga embaixo da porta |
| **8** | `Voo` | voa. O terreno para de valer para ela |
| **8** | `Montaria` | carrega uma pessoa. O grupo inteiro passa a se mover no ritmo dela |
| **8** | `Fisgada` | prende à distância. Ela alcança, engancha, e quem ia fugir para de ir |
| **8** | `Emboscada` | surge do chão, fora do alcance de ver. Do ponto de vista do inimigo, ela já estava ali |
| **8** | `Jorro` | empurra em linha ou em área. Limpa um corredor inteiro de uma vez |
| **8** | `Graúdo` | ocupa espaço maior e **barra passagem**. Ela vira parede com opinião |
| **8** | `Remoto` | funciona além dos 18 metros da amarra. Ver *A amarra, e as três faixas de alcance* |

> **O `Graúdo` e o `Miúdo` são o mesmo eixo em degraus diferentes, e o que os separa é quem sofre.** O `Miúdo` passa por um vão, e isso é coisa que a invocação faz consigo mesma. O `Graúdo` barra passagem, e barrar é o inimigo perdendo movimento.

Os três de percepção (`Fala`, `Faro`, `Vigia`) são os que mais decidem sessão fora de luta. Uma invocação com `Vigia` transforma toda cena de vigilância: o grupo fica no carro e a invocação fica no telhado. Uma com `Fala` faz o interrogatório, o recado e a negociação em lugar onde nenhum de vocês podia aparecer.

### `Comando`

**Comando**
| pontos | `Comando` | o que faz |
|---|---|---|
| **0** | `Investir` | o ataque. **Toda invocação tem**, e é ele que entrega a cota da Rotina |
| **4** | `Agarrar` | prende o alvo. Ele para de escolher onde está |
| **4** | `Arrastar` | move o alvo, ou se move levando ele. Tira alguém de cima de uma beirada, ou põe |
| **4** | `Buscar` | pega um objeto, ou rastreia de forma ativa. Ela entra no cômodo em chamas no lugar de você |
| **4** | `Cavar` | abre buraco, desenterra, revira o terreno. Faz rota onde não havia rota |
| **8** | `Interpor` | se põe entre você e o golpe. O corpo dela come o que ia em você |
| **8** | `Chamariz` | o alvo tem de vir para cima dela. Você escolhe em quem a coisa está prestando atenção |

`Cavar` faz buraco no chão; `Emboscada` é ela **saindo** dele. Os dois funcionam sozinhos.

Os dois de `8` pontos são os que mudam a matemática do grupo inteiro. `Interpor` é o que mantém de pé quem tem pouca vida, e `Chamariz` é o que tira o inimigo de cima de quem estava prestes a cair.

### Traço e Comando próprios

Você pode escrever `Traço` e `Comando` que não estão nas listas acima, e o catálogo serve de régua para isso. Escreva o efeito, ache na tabela abaixo o degrau em que ele cai, e leve para o mestre. A palavra final é dele, sempre em cima de uma entrada escrita, nunca do zero.

**Régua de `Traço`**
| pontos | `Traço` cai aqui quando |
|---|---|
| **2** | muda **como ela anda**, e só ela. `Escalada`, `Nado` |
| **3** | muda **o que ela comunica**. `Fala` |
| **5** | muda **o que ela percebe**, e o `Vigia` chega até você. `Faro`, `Vigia` |
| **7** | muda **que espaço ela ocupa**, a um passo de mexer no tabuleiro. `Miúdo` |
| **8** | **encosta em outra criatura ou no tabuleiro**: carrega, prende, empurra, barra, alcança além do alcance, aparece onde não dava. `Voo`, `Montaria`, `Fisgada`, `Emboscada`, `Jorro`, `Graúdo`, `Remoto` |

**Régua de `Comando`**
| pontos | `Comando` cai aqui quando |
|---|---|
| **0** | é **o ataque**. `Investir`, que toda invocação tem |
| **4** | **faz uma coisa com um alvo ou um objeto**. `Agarrar`, `Arrastar`, `Buscar`, `Cavar` |
| **8** | **protege você, ou nega a ação de outro**. `Interpor`, `Chamariz` |

*O `Voo` mostra a régua funcionando: ele sai do degrau da `Escalada` para o de cima porque deixa de ser coisa que a invocação faz consigo mesma e passa a ignorar o tabuleiro inteiro.*

### Montagens de exemplo

Seis invocações conhecidas, montadas com o catálogo acima.

**Montagens de exemplo**
| invocação | montagem | pontos | cabe no nível |
|---|---|---|---|
| *Cão Divino* | `Faro` | 5 | **2** |
| *Nue* | `Voo` | 8 | **2** |
| *Elefante Máximo* | `Jorro` | 8 | **2** |
| *Serpente* | `Emboscada` + `Agarrar` | 12 | 6 |
| *Sapo* | `Fisgada` + `Agarrar` | 12 | 6 |
| *Nue* completo | `Voo` + `Montaria` | 16 | 10 |

Três dos seis cabem já no nível 2, e os outros chegam nos marcos seguintes.

> **Exemplo com a Trilha por cima.** A Mei escolhe a Trilha `Matilha` no nível 2, e é a Trilha que dá os cinco corpos dela: isso não custa nenhum ponto do orçamento. Com os `8` pontos que ela tem, ela compra `Miúdo` por `7`, e os cinco corpos passam por vãos que ninguém mais passa. Sobra `1` ponto, que não compra nada ainda e fica guardado até o nível 6.

## Amarra e alcance

> **A invocação tem de ficar a até 18 metros de você.**
> Além disso ela **não pode ser comandada**: fica onde está, sem agir, até voltar ao alcance. Ela **não some**.

Os 18 metros são o alcance base de Projétil, a referência de distância do sistema. Na prática, a invocação anda até dois turnos de movimento à frente de você.

Empurrar a invocação para fora da amarra custa a ela a rodada, e não o corpo: ela volta a agir assim que você voltar ao alcance dela, ou ela do seu.

**Faixas de alcance**
| faixa | o que é | quem alcança |
|---|---|---|
| **no combate** | os 18 metros da amarra | toda invocação |
| **na cena** | *(um quarteirão, na ordem de 100 metros)* | o `Traço` `Remoto` |
| **fora da cena** | *(um país)* | o `Remoto`, com requisito |

> **A metragem entre parênteses é referência.** Quem decide onde a cena acaba é o mestre, que já decide isso o tempo todo.

> **O `Remoto` é a única entrada do catálogo inteiro com requisito, e ele vale só para a faixa de fora da cena.** Operar uma invocação a essa distância exige Restrição Celestial pelo ramo do corpo limitado, e uma técnica voltada a isso. Dentro da cena o `Remoto` funciona para qualquer um que pague os 8 pontos.

## Queda e morte

A máquina de cair morrendo do capítulo 1, *Como Jogar*, não vale aqui.

> **Ela some no zero, sem estado intermediário.** Nada de `Inconsciente`, nada de Sequela, nada de Cicatriz.
> **Área causa o dano uma vez, na barra dela**, e não uma vez por corpo.
> **E a invocação é vulnerável a área: o dano dobra.**


> **Ela morre em definitivo se o excedente passar de metade da vida máxima, ou se um único golpe causar a vida máxima inteira.**
> O talismã se desfaz, o corpo se perde, a invocação de técnica ou a maldição domada é exorcizada.

Nenhum golpe de rotina dispara isso. Derrubar a barra é comum; matar de vez exige uma área grande de verdade ou uma Expansão de Domínio.

### Voltar

> **Se ela morreu em definitivo, acabou.** Não se reconsegue.
> **Se ela só chegou a zero**, sem excedente acima de metade da vida máxima e sem um golpe que causasse a vida máxima inteira, **ela volta pelo preço normal de invocar, mas com metade da vida máxima.**

Você paga os PE de novo, paga a Ação Padrão de novo, e o corpo que volta cai na metade do tempo do primeiro. Numa luta longa isso vira decisão de verdade: gastar a rodada trazendo um corpo frágil de volta, ou aceitar terminar a cena sozinho.

> **Quando a vida cheia volta ainda está sendo decidido.** O candidato óbvio é o descanso longo. Combine com o seu mestre até isso fechar.

> **Exemplo.** O Kaito, nível 10, tem uma invocação de `técnica` com Constituição `1`, então a vida máxima dela é `2 + (2 + 1) × 10 = 32`. Ela está com `4` de vida e leva um golpe de `18`. O excedente é `14`, que não passa de `16`, que é metade de `32`; e `18` não é `32`. Ela some, mas não morreu de vez: no turno seguinte ele gasta `3` PE e a Ação Padrão, e ela volta com `16`.

## Em aberto

Duas coisas vão aparecer na sua mesa antes de ganharem regra.

**Invocação que não obedece.** A regra supõe que ela obedece: você gasta a Ação Padrão e ela faz. Existem invocações na ficção que agem por conta própria, contra a vontade de quem as carrega, e elas não têm regra escrita ainda. Se a sua mesa quiser uma dessas, é acordo com o mestre.

**Selar com talismã.** O talismã do material sela objeto amaldiçoado, e o alvo dela é o objeto amaldiçoado do capítulo 14, *Ferramenta Amaldiçoada*, que ainda não tem regra de selamento escrita. Por enquanto o `talismã` é um tipo de invocação como os outros três, com a vida dele, e selar não é uma entrada do catálogo.

---


# Capítulo 16 · Experiência e Progressão

*fonte: `manual/80-experiencia-e-progressao.md`*

Você sobe de nível gastando XP, e o XP vem de missão. A regra inteira cabe em cinco linhas.

> **Cada nível custa um número inteiro de missões, e esse número sobe uma missão a cada três níveis.**
>
> **Uma missão padrão paga 100 XP, e paga o mesmo para todo mundo na mesa.**
>
> **Nenhuma missão faz você subir mais de um nível. O que sobra fica acumulado.**
>
> **Na sua semana, as duas primeiras missões pagam cheio. Da terceira em diante o valor cai pela metade a cada uma.**
>
> **Do nível 20 para o 21, além do XP é preciso um feito.**

O XP não muda com o seu nível nem com o Grau de quem está na mesa. Um nível 8 e um nível 14 na mesma missão levam os mesmos 100, e é isso que faz mesa aberta funcionar: quem está atrás sobe mais rápido sozinho, porque cada nível custa mais que o anterior.

Grau é reconhecimento; nível é poder. O Grau abre porta, dá acesso e pesa em conversa, e não paga XP.

> **Uma ficha nova começa no nível 2.** O nível 1 é opção de campanha, para a mesa que quiser jogar o personagem antes de ele ser feiticeiro.

## Curva de XP

**Curva de XP**
| você está no nível | o próximo nível custa | em XP |
|---|---|---|
| **2 a 4** | 1 missão | 100 |
| **5 a 7** | 2 missões | 200 |
| **8 a 10** | 3 | 300 |
| **11 a 13** | 4 | 400 |
| **14 a 16** | 5 | 500 |
| **17 a 19** | 6 | 600 |
| **20 a 22** | 7 | 700 |
| **23 a 25** | 8 | 800 |
| **26 a 28** | 9 | 900 |
| **29** | 10 | 1.000 |

Do nível 2 ao 4 é uma missão por nível: a ficha entra em jogo e ganha corpo antes de qualquer decisão pesada. Do 17 em diante são seis missões por nível, e subir vira coisa de arco inteiro.

Chegar ao nível 20 custa **6.300 XP** no total. Do 20 ao 30 são **8.200**.

## Tamanho da missão

**Tamanho da missão**
| tamanho | paga | o que é |
|---|---|---|
| **curta** | 50 | uma cena, um interrogatório, roleplay puro, uma escolta sem incidente |
| **padrão** | 100 | a missão de uma sessão: sai, resolve, volta |
| **longa** | 200 | duas ou mais sessões, ou uma sessão que virou noite |
| **final de arco** | 300 | o fecho de uma linha de missões, ou o que a mesa vai lembrar por meses |

> **Quem declara o tamanho é quem posta a missão, e declara antes de ela acontecer.**

Missão de roleplay que qualquer Grau pode entrar é missão curta, e ela paga.

## Ritmo de subida

> **Você sobe no máximo um nível por missão. O XP que sobrar fica acumulado e sai na próxima.**

**Ritmo de subida**
| no nível | curta | padrão | longa | final de arco |
|---|---|---|---|---|
| **2** | +50 | **1 nível** | 1 nível, +100 | 1 nível, +200 |
| **5** | +50 | +100 | **1 nível** | 1 nível, +100 |
| **8** | +50 | +100 | +200 | **1 nível** |
| **12 e acima** | +50 | +100 | +200 | +300 |

Quem levou um final de arco no nível 2 sobe um nível na hora e entra na missão seguinte com 200 XP no bolso. Sobe de novo, e continua subindo até o acumulado acabar. O teto espalha a subida por várias sessões em vez de entregar três níveis de decisão de ficha numa noite só.

## Desconto da semana

**Desconto da semana**
| missão da semana | paga |
|---|---|
| **1ª e 2ª** | 100% |
| **3ª** | 50% |
| **4ª** | 25% |
| **5ª** | 12% |
| **6ª** | 6% |

A contagem zera na virada da semana, e ninguém sai com zero: a sexta missão ainda paga.

**O desconto é individual.** Numa missão com quatro pessoas, uma pode estar na primeira missão da semana dela e outra na quarta. Cada um aplica o seu.

## Falhar

> **Missão falhada paga metade ou nada, e quem decide é o mestre.**

Uma missão perdida por azar de dado pesa diferente de uma abandonada na metade, e é essa diferença que o mestre está lendo quando escolhe entre as duas.

## XP de quem mestra

> **Mestrar paga na moeda que o sistema já tem separada: patente, contato, favor da instituição, acesso.**

Um mestre ativo constrói patente e rede, e as duas abrem porta que nível nenhum abre.

## Limiar do nível 20

> **Você chega ao nível 20 por XP. Você passa dele por feito.**

Aos 6.300 de XP acumulado o personagem para no nível 20 até a mesa reconhecer alguma coisa que ele fez. O XP continua acumulando e nada se perde: quando o feito acontece, o que estava guardado destrava de uma vez.

O que conta como feito é conversa de mesa, e a mesa fecha a lista antes de alguém chegar lá.

## Operação na mesa

1. **O mestre posta a missão e declara o tamanho:** curta, padrão, longa ou final de arco.
2. **A mesa acontece.**
3. **No fim, o mestre paga o valor declarado:** cheio no sucesso, metade ou nada na falha.
4. **O jogador anota na ficha** e aplica o desconto da semana, se já for a terceira missão dele.
5. **Chegou ao XP do próximo nível, sobe.** No máximo um nível, e o resto fica acumulado.

Não precisa de aprovação de ninguém, exceto no limiar do 20. E uma linha de missões paga a cada missão: quem entra no meio de uma linha recebe pelo que jogou.

## Progressão por nível

Na maior parte dos níveis, subir é o mesmo personagem com o número maior: você acerta um pouco mais, o feitiço custa a mesma coisa e rende igual, e cabe mais um feitiço na lista. De vez em quando o nível abre uma porta de verdade, e aí a ficha muda de forma: uma Classe nova, uma Liberação Máxima, um degrau de Caminho, um marco.

Ache a sua linha e leia ela inteira.

**Progressão por nível**
| nível | XP | maestria | espaços de feitiço | refino | Classe | Passiva | Classe 0 | o que este nível entrega |
|---|---|---|---|---|---|---|---|---|
| **1** | — | 1 | **2** | 1 | 1 | 1 | 2 | **Fundamento**, Passiva Livre, dois feitiços de Classe 0 |
| **2** | 100 | 1 | **3** | 1 | 1 | 1 | 2 | degrau de **Caminho** · entrega de **Trilha** · +1 espaço de feitiço |
| 3 | 100 | 1 | **3** | 1 | 1 | 1 | 2 | — |
| 4 | 100 | 1 | **4** | 1 | 1 | 1 | 2 | +1 espaço de feitiço |
| **5** | 200 | 1 | **4** | 1 | 2 | 1 | 3 | Classe 2 · mais um Classe 0 |
| **6** | 200 | 1 | **6** | 2 | 2 | 1 | 3 | **marco** · +2 espaços de feitiço |
| **7** | 200 | 1 | **6** | 2 | 2 | 2 | 3 | degrau de **Caminho** · libera Passiva de Classe 2 |
| 8 | 300 | 1 | **7** | 2 | 2 | 2 | 3 | +1 espaço de feitiço |
| **9** | 300 | 1 | **7** | 2 | 3 | 2 | 3 | Classe 3 |
| **10** | 300 | 2 | **9** | 3 | 3 | 2 | 3 | **marco** · **1ª Liberação Máxima** · +2 espaços de feitiço |
| **11** | 400 | 2 | **9** | 3 | 3 | 2 | 4 | entrega de **Trilha** · mais um Classe 0 |
| 12 | 400 | 2 | **10** | 3 | 3 | 2 | 4 | +1 espaço de feitiço |
| **13** | 400 | 2 | **10** | 3 | 4 | 3 | 4 | Classe 4 · libera Passiva de Classe 3 |
| **14** | 500 | 2 | **12** | 4 | 4 | 3 | 4 | **marco** · +2 espaços de feitiço |
| **15** | 500 | 2 | **12** | 4 | 4 | 3 | 4 | degrau de **Caminho** |
| 16 | 500 | 2 | **13** | 4 | 4 | 3 | 4 | +1 espaço de feitiço |
| **17** | 600 | 2 | **13** | 4 | 5 | 3 | 5 | Classe 5 · **Técnica Máxima** · mais um Classe 0 |
| **18** | 600 | 3 | **15** | 5 | 5 | 3 | 5 | **marco** · +2 espaços de feitiço |
| **19** | 600 | 3 | **15** | 5 | 5 | 3 | 5 | entrega de **Trilha** |
| **20** | 700 | 3 | **16** | 5 | 5 | 3 | 5 | **2ª Liberação Máxima** · +1 espaço de feitiço |
| **21** | 700 | 3 | **16** | 5 | 6 | 3 | 5 | Classe 6 |
| **22** | 700 | 3 | **18** | 6 | 6 | 3 | 5 | **marco** · +2 espaços de feitiço |
| 23 | 800 | 3 | **18** | 6 | 6 | 3 | 5 | — |
| 24 | 800 | 3 | **19** | 6 | 6 | 3 | 5 | +1 espaço de feitiço |
| 25 | 800 | 3 | **19** | 6 | 6 | 3 | 5 | — |
| **26** | 900 | 4 | **21** | 7 | 7 | 3 | 5 | **marco** · Classe 7 · +2 espaços de feitiço |
| **27** | 900 | 4 | **21** | 7 | 7 | 3 | 5 | entrega de **Trilha** |
| 28 | 900 | 4 | **22** | 7 | 7 | 3 | 5 | +1 espaço de feitiço |
| 29 | 1.000 | 4 | **22** | 7 | 7 | 3 | 5 | — |
| **30** | — | 4 | **24** | 8 | 7 | 3 | 5 | **marco** · degrau de **Caminho** · **3ª Liberação Máxima** · +2 espaços de feitiço |

Nível em negrito é nível que entrega decisão nova: uma Classe, um marco, um degrau de Caminho, uma entrega de Trilha. Os espaços de feitiço correm no ritmo próprio deles e por isso aparecem também em linha sem negrito. Nos níveis que ficaram de fora, o personagem cresce só em número.

### Como ler cada coluna

- **XP** é o que custa **sair** daquele nível, e ele é o mesmo dentro de cada faixa de três níveis. Uma missão padrão paga 100. O nível 30 é o topo e não tem custo.
- **maestria** é o bônus que entra no seu ataque de conjuração, na CD dos seus feitiços e nas perícias em que você é treinado.
- **espaços de feitiço** é o tamanho da sua lista de feitiços conhecidos, e é a coluna que responde "quantos feitiços eu tenho agora?". Passiva é paga com espaço, e a Expansão de Domínio também. Liberação Máxima não ocupa.
- **refino** aqui é só a linha de graça, o que todo mundo tem sem escolher nada. Quem escolhe Refino no marco tem mais que isso, e o teto é 10.
- **Classe** é a maior Classe de feitiço que você consegue montar.
- **Passiva** é a maior Classe de Passiva que já abriu para você.
- **Classe 0** é quantos feitiços grátis você carrega, e eles ficam fora da conta de espaços.

### Feitiços por nível

> **Espaços de feitiço conhecido = `2 + (nível ÷ 2)`, arredondando para baixo. Mais um por marco já alcançado.**

São **3 no nível 2**, **16 no nível 20** e **24 no nível 30**, e a coluna *espaços de feitiço* da tabela acima já traz a conta pronta em cada linha.

A parte de baixo da conta dá um feitiço novo **a cada nível par**. A parte de cima é o espaço que cada **marco** solta de graça, então nos níveis 6, 10, 14, 18, 22, 26 e 30 entram dois de uma vez.

Passiva custa espaço de feitiço conhecido, e a Expansão de Domínio também: as três saem desta mesma coluna.

### Vida e PE

As duas dependem do seu Caminho, e cabem em duas linhas:

> **Vida:** no nível 1, a vida inicial do seu Caminho mais a sua Constituição. Em cada nível depois, a vida por nível do seu Caminho mais a Constituição de novo.
>
> **PE:** o PE por nível do seu Caminho vezes o seu nível.

## Marcos

A cada quatro níveis o personagem chega a um **marco**: os níveis **6, 10, 14, 18, 22, 26 e 30**. São sete na campanha inteira, e o último cai exatamente no nível 30.

Marco é o nível em que a ficha muda de forma. Nos outros níveis a subida acontece sozinha e você só anota; no marco você para, olha a ficha e decide uma coisa. Você volta da missão diferente de como saiu: mais forte no corpo, mais fino no controle da própria energia, ou com um jeito novo de usar a técnica que já tinha.

> **De graça, em todo marco:** +1 ponto de atributo, +1 de refino e +1 espaço de feitiço.
>
> **E escolha uma destas três:**
>
> **Corpo** — mais um ponto de atributo.
>
> **Refino** — mais um de refino, e uma aptidão. **Se o seu refino já estiver no teto, você leva duas aptidões no lugar.**
>
> **Leque** — mais um feitiço, que só pode ser feitiço, e uma Passiva.

**Teto de atributo: 6. Teto de refino: 10.**

A escolha é do momento: você decide no marco, e nada obriga você a repetir a escolha anterior.

### Rotas do marco

**Rotas do marco**
| escolha | o que entra na ficha | quando ela é boa |
|---|---|---|
| **Corpo** | +1 num atributo | cedo, enquanto o seu atributo principal ainda não bateu no 6 |
| **Refino** | +1 de refino e uma aptidão | quando você quer fazer coisa que a sua técnica não faz |
| **Leque** | +1 feitiço e uma Passiva | quando a sua lista está apertada de Passiva e de Expansão |

Você começa a campanha com nove pontos de atributo distribuídos na criação. A linha de graça dos sete marcos leva isso a dezesseis, e quem escolhe **Corpo** nos sete chega a vinte e três, espalhados por até cinco atributos com teto de 6 em cada.

Refino não vale nada para quem não tem aptidão: quem escolhe Leque sete vezes tem zero aptidões, e o refino dele fica sendo número morto. Quem escolhe Refino sete vezes tem dez aptidões e nenhuma Passiva a mais para querer.

> **Quem nunca escolhe Refino termina a campanha com zero aptidões.** A rota é legítima e está escrita aqui para ninguém descobrir isso no nível 20. Mesmo essa ficha não fica sem nada: `Cobrir-se de energia` e `Canalizar energia` vêm de graça no refino 1, e a primeira continua crescendo com o refino da linha passiva até 8. O que ela nunca vai ter é `Energia Reversa` nem `Barreira Simples`.
### Refino por rota

O refino começa em `1`, sobe `+1` de graça em cada um dos sete marcos, e a escolha do marco pode somar mais `+1` até o teto de `10`. Três rotas, e a sua provavelmente fica entre elas:

**Refino por rota**
| rota | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |
|---|---|---|---|---|---|---|---|
| **especialista**, sempre Refino | `3` | `5` | `7` | `9` | **`10`** | `10` | `10` |
| **meio a meio** | `3` | `4` | `6` | `7` | `9` | `10` | `10` |
| **generalista**, nunca Refino | `2` | `3` | `4` | `5` | `6` | `7` | **`8`** |

A faixa é de `4` a `7` no nível 14 e de `6` a `10` no nível 22: duas fichas do mesmo nível nunca ficam a mais de quatro degraus de distância.

O especialista bate no teto no **nível 22**, e é aí que a escolha de Refino troca de moeda: dali em diante ela entrega duas aptidões no lugar do degrau que não teria mais onde cair.

> **Guardar marco não guarda refino.** A linha de graça sobe sozinha, e ela não espera você decidir. Quem deixa para investir tarde chega aos níveis altos com o refino da linha de baixo e ainda precisa de mais um marco para alcançar o degrau que queria. Requisito de refino se paga com tempo, e o tempo não volta.

### Maestria

**Maestria por marco**
| marco | nv 6 | nv 10 | nv 14 | nv 18 | nv 22 | nv 26 | nv 30 |
|---|---|---|---|---|---|---|---|
| atributo, refino, espaço e escolha | sim | sim | sim | sim | sim | sim | sim |
| maestria sobe | — | **sim** | — | **sim** | — | **sim** | — |

Um marco sim, um não, começando pelo segundo.


### Teto de Passivas

Você paga por **cinco** Passivas ao longo da campanha, e esse número não muda. Cada escolha de **Leque** abre uma vaga a mais no teto, e a Passiva que a própria escolha concede ocupa essa vaga nova. Uma rota pura de Leque termina com doze Passivas na ficha, e cinco delas continuam sendo as cinco pagas de sempre.

---


# Capítulo 17 · Apêndice · Bloquear

*fonte: `manual/90-apendice-bloquear.md`*

> **Defesa parada ou `Bloquear`: a mesa escolhe.** Combinem antes da primeira sessão, e a resposta vale para todo mundo — jogadores e inimigos. Nenhum número de nenhum outro capítulo muda por causa dessa escolha.
A sua Defesa é um número parado: o inimigo rola contra ela e você não rola nada. Se a sua mesa preferir rolar para se defender, usa `Bloquear`.

## Rolagem de Bloquear

> **A sua Defesa é `10 + Destreza + proteção`, e ela continua sendo o padrão.**
>
> **Ao ser atacado, você pode `Bloquear`:** role `2d10 + (a sua Defesa − 11)` e use esse resultado no lugar da sua Defesa contra aquele ataque.
>
> **Duplo 10, `Aparar`.** O ataque não acerta. Você pode gastar a sua Reação para atacar o agressor na hora, e esse ataque sai com `+3` de dano.
>
> **Duplo 1, `Brecha`.** O ataque acerta. O agressor pode gastar a Reação dele para atacar você de novo na hora, sem bônus nenhum.
>
> **O `Aparar` não anula um 20 natural.** Crítico fura guarda.
>
> **`Bloquear` não vale em Teste de Resistência.** Só contra ataque com rolagem de acerto.
>
> `Bloquear` não custa nada, não gasta a sua Reação, e é de todo mundo.

### Linha da ficha

O `−11` some no número que a ficha imprime. Ela traz a linha pronta, do lado da Defesa:

> **Defesa 17 · Bloquear 2d10+6**

Na mesa você lê *"role 2d10+6"*, que dá o mesmo trabalho que *"role d20+7"*.

## Exemplo

A Rina está com Defesa 17, então a linha dela é `Bloquear 2d10+6`. Uma maldição ataca e tira **18** no ataque: com a Defesa parada, isso acerta.

Ela escolhe `Bloquear`. Tira `7` e `4`, que somados ao `+6` dão **17**. O ataque acerta do mesmo jeito, e ela não perdeu nada por tentar.

Na rodada seguinte a mesma maldição tira **19**. A Rina bloqueia e sai `10` e `10`: `Aparar`. O ataque não acerta, e ela ainda tem a Reação na mão. Aí vem a decisão: gastar a Reação para bater de volta com `+3` de dano, ou guardar ela para o capanga que ainda não agiu neste turno.

## Custo

`Bloquear` é neutro na média: ele entrega tanto quanto tira.

**Resultados de Bloquear**
| o que acontece quando você rola | chance |
|---|---|
| `Aparar`, e a história é boa | 1,0% |
| duplo 1, e a história é ruim | 1,0% |
| o dado mudou o resultado, sem extremo | 14,5% |
| nada mudou; você rolou por rolar | 83,5% |

> **Um em cada doze golpes vai passar porque você rolou, quando a sua Defesa parada teria segurado.** `Bloquear` não é defesa melhor. É a mesma defesa com variação, e os dois resultados de 1% são o que você está comprando.

O outro preço é tempo de mesa: uma rolagem a mais por golpe recebido. Num combate de quatro rodadas com quatro personagens, isso passa de uma dúzia de rolagens novas.

## Limites

### Aparar e crítico

Quem ataca continua rolando d20, e 20 natural continua sendo 20 natural. O `Aparar` para o golpe comum e não para o crítico. Nenhuma regra de crítico muda por causa deste apêndice.

### Modificador compartilhado

> **`Bloquear` usa exatamente o mesmo modificador da sua Defesa parada. Nada pode aumentar um sem aumentar o outro.**

Se um escudo, uma aptidão, um Legado ou uma ferramenta der `+1` na Defesa e não no `Bloquear`, ou o contrário, a regra quebra: `+1` de diferença entre os dois lados vale dois pontos e meio percentuais.

## Bloquear e Incapacitado

A condição `Incapacitado` cita `Bloquear` diretamente: quem está `Incapacitado` não pode bloquear, e todo ataque corpo a corpo contra ele é crítico.

> **Se a sua mesa não usa `Bloquear`, o `Incapacitado` é só o crítico no corpo a corpo.** É a metade que vale sempre, e ela sozinha já paga o preço da condição.


---

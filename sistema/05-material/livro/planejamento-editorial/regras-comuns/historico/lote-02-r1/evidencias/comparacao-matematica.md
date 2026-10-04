# Movimento, lote 2 — comparação matemática dos candidatos

**Recomendação para o primeiro teste jogável:** saltos curtos automáticos com teste para estender; para queda, testar primeiro **3 de dano por 1,5 m completos, a partir de 3 m, sem teto**, com **uma tentativa de Acrobacia CD 14 que reduz a altura em 3 m**, sem Reação. O perfil fixo oferece previsão e evita o pico de dano que pode zerar um iniciante numa queda de 4,5 m. Ele ainda torna precipícios uma ameaça importante, inclusive para personagens avançados. A alternativa **1d6 por 3 m** é preferível se o objetivo prioritário for permitir mais quedas e retornos ao combate durante a mesma cena.

Eu não recomendaria **1d6 por 1,5 m** como primeira versão comum: ela combina grande dano nos níveis iniciais com variação suficiente para derrubar alguém em um único desnível de 4,5 m. A comparação completa está abaixo. Nenhum candidato foi aplicado ao projeto.

## 1. Fontes, hipóteses e alcance das contas

Fontes lidas na raiz `/media/mizuki/HD Externo II/Claude/Claude 2/`:

- `sistema/03-mecanica/01-atributos-acerto-defesa.md`: atributos, maestria e fórmula de Vida.
- `sistema/03-mecanica/04-pericias-e-testes.md`: d20 + atributo + maestria treinada; escada fixa de CDs.
- `sistema/05-material/livro/manual/10-como-jogar.md`: Vida, arredondamento, Bloquear e Vida a 0.
- `sistema/05-material/livro/manual/11-o-turno.md`: movimento, Correr e conversões de ações.
- `caminhos/05-Edicao-Integrada/06-Incursor-Caminho-e-Trilhas.md`: Movimento Acrobático e Parkour.
- `caminhos/05-Edicao-Integrada/01-Bastião-Caminho-e-Trilhas.md`: Alicerce.

Constituição 2 nas três comparações de nível, como referência controlada, sem pretender representar toda build:

| Nível | Incursor/Emanador/Evocador | Bastião | Bônus de Acrobacia do especialista simulado | Sucesso na CD 14 |
|---|---:|---:|---:|---:|
| 2 | 14 PV | 23 PV | +4: Destreza 3 + maestria 1 | 55% |
| 11 | 68 PV | 104 PV | +7: Destreza 5 + maestria 2 | 70% |
| 30 | 182 PV | 275 PV | +10: Destreza 6 + maestria 4 | 85% |

Destreza 5 no nível 11 representa investimento nos aumentos disponíveis; não é obrigatória. Um Bastião com outras prioridades terá Acrobacia menor. Sem bônus, a chance na CD 14 é 35%.

As chances de zero partem da Vida cheia indicada, salvo quando outra Vida atual estiver explícita. Não incluem cura, vida temporária, Ainda de Pé, reduções adicionais ou salvamentos por aliados. Portanto não são a mortalidade final de uma ficha completa. Modelam **o dano da queda suficiente para atingir zero naquele momento**, antes das respostas e das regras de Aguentar/Insistir.

Resistência usa `ceil(dano/2)`, com arredondamento contra o beneficiado, conforme o princípio geral do livro. A redação final deve confirmar esse arredondamento explicitamente. Usar o piso altera os limiares em um ponto, mas não muda a conclusão entre os perfis. Alicerce só se aplica se Concussão estiver escolhida e Olhos Em Mim ativo; a análise não concede resistência permanente a todo Bastião.

**Convenção necessária de altura:** abaixo de 3 m, dano zero. A partir de 3 m, conta-se **toda a altura**, por faixas completas. Os primeiros 3 m não são uma franquia subtraída. O teste bem-sucedido reduz a altura primeiro; só então se verifica o limiar e se calcula dano.

## 2. Salto horizontal proposto: a escala funciona, com duas cautelas

A sonda é coerente com os bônus do Projeto:

| Distância com impulso de 3 m | Resolução candidata | Bônus +0 | +4, nv2 | +7, nv11 | +10, nv30 |
|---|---|---:|---:|---:|---:|
| Até 3 m | Sem teste em condições normais | 100% | 100% | 100% | 100% |
| Até 4,5 m | CD 10 | 55% | 75% | 90% | 100% |
| Até 6 m | CD 14 | 35% | 55% | 70% | 85% |
| Até 7,5 m | CD 18 | 15% | 35% | 50% | 65% |
| Até 9 m | CD 22 | 0% | 15% | 30% | 45% |

São percentuais exatos da distribuição uniforme dos vinte resultados; não há simulação aleatória. O salto básico não exigir teste é importante: caso a CD 6 fosse usada em toda travessia simples, o especialista +4 ainda falharia 5% das vezes, acumulando tropeços em deslocamentos cotidianos.

O teste deve usar **Atletismo**; o Assassino substitui por **Acrobacia durante o Parkour**, conforme seu benefício. Dar Acrobacia como escolha universal esvazia a entrega da Trilha.

### Impulso e movimento disponível

Impulso de 3 m e salto de 3 m gastam 6 m da distância disponível. Impulso e salto de 6 m gastam os 9 m de um personagem comum. O salto de 7,5 m, com o mesmo impulso, exige 10,5 m: cabe no Incursor de 12 m, mas o personagem comum precisa de movimento adicional. Impulso e salto de 9 m exigem 12 m.

A tabela de dificuldade não fornece metros. Correr aumenta o saldo de movimento, sem aumentar automaticamente a distância segura do salto ou dispensar o teste. A distância do salto é declarada antes do d20; o resultado não cria uma escolha retroativa do destino mais conveniente.

No Assassino, **6 m de parede + salto de 3 m** gastam 9 dos 12 m. O salto precisa continuar viável depois de consumida a metade permitida por parede. Usar Acrobacia no teste não transforma automaticamente o salto em metros adicionais de parede. A regra do impulso deve aceitar um percurso válido de Parkour, sem exigir que toda aproximação ocorra exclusivamente sobre piso horizontal; a redação deve também impedir que movimento desconectado do salto conte como impulso.

### Parado: metade produz distâncias inconvenientes

Metade literal gera **1,5 / 2,25 / 3 / 3,75 / 4,5 m** para as mesmas linhas de resolução. Funciona matematicamente, mas cria medidas de 0,75 m no salto horizontal; arredondar à grade de 1,5 m faz duas faixas colapsarem e uma tentativa pagar CD para alcançar a mesma distância já gratuita.

Dois candidatos honestos:

1. **Metade literal:** fisicamente intuitivo, mais curto e restritivo; manter os valores exatos e não arredondar a grade às escondidas.
2. **Mesmas faixas com um degrau de dificuldade adicional:** parado, até 1,5 m sem teste; até 3 m CD 10; 4,5 m CD 14; 6 m CD 18; 7,5 m CD 22; 9 m CD 26. Mais fácil de consultar, deliberadamente mais favorável a saltos sobrenaturais parados.

**Prefiro testar a segunda opção**, por consulta e por compatibilidade com o uso da vítima como apoio. O iniciante +4 salta 3 m parado com 75%, 4,5 m com 55% e 6 m com 35%. O especialista +10 chega a 9 m parado com 25%, ainda limitado pelos metros disponíveis. Isso deve ser apresentado como opção deliberada; não é a mesma regra que metade.

O fracasso e a possibilidade de agarrar a borda ainda precisam de um procedimento fixo. Não presumir que todos recebem gratuitamente o mesmo término pendurado com uma mão do Assassino.

### Altura: candidato separado, explicitamente mais curto

Para uma sonda de altura, usar metade das medidas horizontais preserva uma conta curta: **1,5 m com impulso ou 0,75 m parado sem teste**, depois limites verticais 2,25 / 3 / 3,75 / 4,5 m nas CDs 10 / 14 / 18 / 22 com impulso. O personagem +4 tem 55% para elevar os pés em 3 m; o +10 tem 85%. Esses números já representam força sobrenatural apreciável, e não atletismo humano comum.

Se isso parecer alto demais para a identidade pretendida, reduzir a **tabela vertical** mantém a lógica das probabilidades sem desregular o salto horizontal. Não reduzir ambos só porque a altura ficou excessiva. Para o primeiro teste, basta anunciar que essa é a tabela vertical candidata e medir pés/destino de aterrissagem; alcance das mãos, tamanho do corpo e borda são outra informação. Saltar 1,5 m verticalmente não significa automaticamente agarrar qualquer borda até uma altura inventada depois.

## 3. Os três perfis de queda

Seja `H` a altura depois da redução por Acrobacia, nunca menor que zero:

- **A — suave, com dados:** se H < 3 m, zero; caso contrário, `floor(H/3 m)d6`.
- **B — intenso, com dados:** se H < 3 m, zero; caso contrário, `floor(H/1,5 m)d6`.
- **C — fixo:** se H < 3 m, zero; caso contrário, `3 × floor(H/1,5 m)` de dano.

Sem teto nas comparações principais. A seção de teto mostra o que ele alteraria.

| Altura | A: dados / média | B: dados / média | C: dano certo |
|---|---|---|---:|
| 3 m | 1d6 / 3,5 | 2d6 / 7 | 6 |
| 4,5 m | 1d6 / 3,5 | 3d6 / 10,5 | 9 |
| 6 m | 2d6 / 7 | 4d6 / 14 | 12 |
| 12 m | 4d6 / 14 | 8d6 / 28 | 24 |
| 30 m | 10d6 / 35 | 20d6 / 70 | 60 |
| 60 m | 20d6 / 70 | 40d6 / 140 | 120 |

O perfil C causa aproximadamente 85,7% da média de B nas mesmas faixas. Sua diferença importante é eliminar os picos e os resultados muito baixos do dano, tornando possível prever a consequência antes de saltar. Isso aumenta a segurança de um iniciante em certas alturas e torna outras alturas determinísticas: a passagem de um limiar de Vida pode mudar o risco abruptamente.

## 4. Chance exata de atingir zero: iniciante com 14 PV

Em cada célula: **sem mitigação / com Acrobacia +4, CD 14, reduzindo 3 m**. Percentuais exibidos arredondados; o cálculo usa frações exatas. As alturas representam queda livre real, não descida por uma escada, corda ou apoio válido.

| Altura | A: 1d6/3 m | B: 1d6/1,5 m | C: 3 por 1,5 m |
|---|---:|---:|---:|
| 4,5 m | 0% / 0% | 16,2037% / 7,2917% | 0% / 0% |
| 6 m | 0% / 0% | 55,6327% / 25,0347% | 0% / 0% |
| 9 m | 16,2037% / 7,2917% | 96,4120% / 73,9834% | 100% / 45% |
| 12 m | 55,6327% / 33,9468% | 99,9234% / 97,9921% | 100% / 100% |
| 18 m | 96,4120% / 90,0251% | >99,9999% / 99,9997% | 100% / 100% |

Exemplos de cálculo exato:

- B em 4,5 m: `P(3d6 ≥ 14) = 35/216`; a Acrobacia zera a queda no sucesso de 55%, portanto o risco final é `(9/20)×(35/216) = 7/96` = **7,291666…%**.
- A em 12 m: falha de Acrobacia usa 4d6; sucesso usa 3d6. O risco é `(9/20)P(4d6≥14)+(11/20)P(3d6≥14) = 2933/8640` = **33,946759…%**.
- C em 9 m: dano 18 na falha e 12 no sucesso. Com 14 PV, apenas a falha de Acrobacia zera: **45%**.
- C em 12 m: dano 24 ou 18; ambos superam 14. Mitigação reduz dano, mas o risco de atingir zero continua **100%**.

**Vida já gasta muda a leitura.** Com apenas 7 PV atuais, a queda de 4,5 m tem risco de zero, após a Acrobacia +4, de **0% em A**, **40,8333% em B** e **45% em C**. O dano fixo protege contra picos em Vida cheia, mas se torna previsivelmente perigoso para quem já está ferido.

## 5. Níveis avançados: sobrevivência sobrenatural continua existindo

Chance de zero para Incursor, sempre sem mitigação / com a Acrobacia indicada na primeira tabela. Todas estas comparações são **sem teto**.

| Nível e Vida | Queda | A | B | C |
|---|---:|---:|---:|---:|
| 11, 68 PV | 30 m | 0% / 0% | 62,7425% / 37,6322% | 0% / 0% |
| 11, 68 PV | 60 m | 62,7425% / 50,1109% | >99,9999% / >99,9999% | 100% / 100% |
| 30, 182 PV | 60 m | 0% / 0% | 0,004646% / 0,000787% | 0% / 0% |
| 30, 182 PV | 90 m | 0% / 0% | 98,4539% / 95,5893% | 0% / 0% |
| 30, 182 PV | 120 m | 0,004646% / 0,001376% | >99,9999% / >99,9999% | 100% / 100% |

No fixo, os limiares ficam transparentes:

- Incursor 14 PV: 7,5 m causam 15; com mitigação, só a falha zera. A partir de 10,5 m, mesmo reduzir 3 m ainda deixa dano suficiente.
- Incursor 68 PV: 34,5 m causam 69; Acrobacia +7 reduz o risco a 30%. A partir de 37,5 m, também zera no sucesso.
- Incursor 182 PV: 91,5 m causam 183; Acrobacia +10 reduz o risco a 15%. A partir de 94,5 m, também zera no sucesso.

O perfil fixo permite sobreviver a quedas altas graças aos PV, mas não tem um teto que torne qualquer altura adicional irrelevante. Isso **não mantém igual o risco percentual entre níveis**: mantém o mesmo dano absoluto para a mesma altura. Se a meta fosse a mesma ameaça relativa em todos os níveis, nenhum dos três perfis faria isso; seria outra proposta de sistema.

## 6. O Bastião resistente deve continuar resistente

Acrobacia e resistência são efeitos diferentes: primeiro reduz-se a altura, calcula-se o dano e então se aplica a metade. A tabela abaixo usa Bastião nv2, **23 PV**, resistência ativa a Concussão e Acrobacia +4.

| Queda | A: zero sem / com Acrobacia | B: zero sem / com Acrobacia | C: zero sem / com Acrobacia |
|---|---:|---:|---:|
| 12 m | 0% / 0% | 0,00982% / 0,00442% | 0% / 0% |
| 18 m | 0% / 0% | 33,8061% / 17,3574% | 0% / 0% |
| 30 m | 3,8995% / 2,0093% | 99,9690% / 99,7175% | 100% / 100% |

No perfil C, a primeira altura que pode zerar esses 23 PV com resistência é **22,5 m**: 45 de dano bruto, arredondado a 23 depois da metade. Com mitigação, o risco ali é 45%; a partir de 25,5 m, é 100% mesmo no sucesso. Sem resistência, o limiar começa em 12 m e se torna inevitável pela mitigação limitada a partir de 15 m.

Com Constituição 2 e resistência, o limiar fixo sem mitigação chega a **103,5 m no nível 11** e **274,5 m no nível 30**. Isso mede o efeito conjunto de muitos PV e resistência; não é erro de cálculo. A mitigação acrescenta apenas uma faixa de 3 m à margem. Ajustar toda a queda para ameaçar esse extremo faria as quedas comuns muito mais letais aos outros Caminhos.

Ainda de Pé e outras recuperações foram deliberadamente excluídas: o Bastião completo poderá conservar mais vida ao longo de impactos sucessivos. Também não se deve permitir Bloquear contra dano ambiental sem ataque, nem presumir que toda redução “num golpe” funciona em queda; essas compatibilidades precisam de regra expressa.

## 7. Quedas repetidas de 4,5 m após empurrões

**Empurrar 4,5 m na horizontal não é causar uma queda de 4,5 m.** Esta sonda exige precipício real com esse desnível e uma nova queda efetiva em cada ocorrência. Proibir escolher um destino no ar acima do apoio inicial fecha o lançamento vertical fabricado; precipícios continuam relevantes.

Cenário de estresse: Incursor com 14 PV, nenhuma cura, n quedas independentes de 4,5 m, **uma Acrobacia +4 por queda**. Reduzir a altura em 3 m deixa 1,5 m, abaixo do limiar, e zera o dano daquela ocorrência. É uma chance de evitar uma queda curta, não imunidade a alturas arbitrárias.

| Quedas | A: chance acumulada de zero | B | C |
|---|---:|---:|---:|
| 1 | 0% | 7,2917% | 0% |
| 2 | 0% | 27,5443% | 20,25% |
| 3 | 1,4766% | 47,9427% | 42,525% |
| 4 | 5,5297% | 64,4343% | 60,9019% |

Para C, cada queda é 0 de dano com probabilidade 0,55 ou 9 com probabilidade 0,45. Duas falhas já zeram os 14 PV; após duas quedas a probabilidade exata é `0,45² = 81/400`. Após quatro é `97443/160000`. Em B, após duas quedas o resultado exato é `10577/38400`. A distribuição completa foi convoluída, não estimada pela média.

Sem mitigação, duas quedas desse tipo zeram o Incursor com probabilidade **0% em A**, **96,4120% em B** e **100% em C**. Portanto a redução de altura importa bastante no fixo, e o desenho do cenário precisa oferecer trajetórias e decisões que não forcem a mesma queda repetidamente.

Bastião nv2, resistência ativa, nas mesmas quatro quedas:

- A: no máximo 3 de dano por ocorrência; 0% de zero até quatro quedas, com ou sem mitigação.
- B: sem mitigação, 43,4383% de zero até a quarta; com Acrobacia +4, 1,9637%.
- C: cada falha causa 5 após resistência; quatro falhas somam 20, então 0% de zero até a quarta. Recuperações excluídas.

A condição Derrubado e o custo de voltar à luta podem ser tão relevantes quanto o dano; estes números não os somam como dano fictício. O controle já possui valor por deslocar e impedir a posição desejada.

## 8. Mitigação: benefício finito, sem sufocar a Reação

A sonda Acrobacia CD 14, redução de 3 m, uma vez por queda contínua e sem Reação é coerente com o kit. Passo Guardado, Evasão e Reflexo preservam sua economia, e a queda não passa a exigir gastar uma reserva que a Trilha usa para outras respostas.

Benefício esperado para uma queda de 4,5 m, com bônus +4:

| Perfil | Dano médio sem tentativa | Dano médio com tentativa | Economia média |
|---|---:|---:|---:|
| A | 3,5 | 1,575 | 1,925 |
| B | 10,5 | 4,725 | 5,775 |
| C | 9 | 4,05 | 4,95 |

Em quedas suficientemente altas para que os dois resultados ainda causem dano, a redução do perfil C é sempre **6 de dano no sucesso**, antes da resistência; economia média de **3,3 no nv2**, **4,2 no nv11** e **5,1 no nv30**. Em 3 m e 4,5 m, o limiar pode ampliar a economia, porque o sucesso deixa o restante abaixo da altura que causa dano.

Condições mínimas para o teste: personagem consciente, capaz de agir e controlar a aterrissagem; uma tentativa por queda efetiva, sem repetir a cada trecho de parede ou começo de turno. A redação deve decidir como Agarrado/Impedido afetam essa capacidade, evitando que um personagem totalmente contido receba uma rolagem de aterrissagem livre sem critério.

O teste de salto resolve alcançar o destino. Se ele falhar e produzir uma queda real, o teste de aterrissagem resolve reduzir as consequências. Isso não é a mesma coisa que exigir duas aprovações consecutivas para saltar com sucesso. Não adicionar ainda uma terceira rolagem universal para não ficar Derrubado, salvo se houver uma finalidade expressa.

## 9. Tetos e alturas extremas

Tetos nos perfis com dados mudam o resultado de forma estrutural:

| Teto de dados | Média / máximo | Incursor nv11, 68 PV: chance de zero no teto | Incursor nv30, 182 PV |
|---|---|---:|---:|
| 12d6 | 42 / 72 | 0,00008361% | 0% |
| 20d6 | 70 / 120 | 62,7425% | 0% |
| 30d6 | 105 / 180 | 99,9981% | 0% |

Nenhum desses tetos consegue zerar o Incursor de 182 PV cheio, mesmo no maior dano possível. Isso pode ser uma opção de fantasia sobrenatural; não pode ser descrito como risco físico extremo sempre preservado. O Bastião resistente torna o teto ainda menos relevante.

Também é importante a ordem: para mitigação por altura, primeiro subtraem-se os 3 m e depois se calcula o número de dados com teto. Em alturas muito acima dele, os dois resultados chegam ao mesmo teto; a Acrobacia já não altera dano. Reduzir um dado depois de aplicar o teto seria outra regra, com outro efeito.

**Para C, recomendo testar sem teto numérico**, pois já não existe a razão operacional de evitar dezenas de dados. O dano alto ainda segue Vida a 0; não adicionar morte instantânea, dano de alma, sequelas extras ou um salvamento narrativo arbitrário como parte implícita desta fórmula. Queda de altura extrema, velocidade terminal, aterrissagem na água e corpos de tamanhos muito diferentes continuam limites de abstração a declarar, sem fingir uma simulação física.

## 10. Escolha recomendada e condição para reconsiderar

**Candidato principal:** base de salto com impulso 3 m, salto comum 3 m, parado 1,5 m, distâncias maiores nas CDs propostas; para parado, testar tabela com um degrau adicional em vez de metade literal. Altura recebe sua tabela curta própria. Dano de queda C, 3 por 1,5 m completos, a partir de 3 m, sem teto; Acrobacia CD 14 reduz 3 m uma vez, sem Reação.

Ele reúne:

- movimento cotidiano sem rolagem desnecessária;
- progresso perceptível do especialista no mesmo obstáculo;
- consulta previsível por mestres diferentes;
- ausência de pico capaz de zerar 14 PV numa única queda de 4,5 ou 6 m;
- sobrevivência em grandes alturas para fichas avançadas, mantendo um limite por Vida;
- mitigação útil, mas finita; resistência do Bastião continua importante.

**Reconsiderar em favor de A** se o primeiro teste mostrar que personagens iniciantes precisam tomar várias quedas reais de 4,5 m na mesma luta para exercer o próprio kit. No fixo, duas quedas sem mitigação já excedem seus 14 PV; com mitigação ainda há 20,25% de chegar a zero. A torna esse tipo de sequência muito mais tolerante. O gatilho de descer 4,5 m com apoio do Assassino deve ser tratado como percurso controlado quando houver apoio válido, não convertido automaticamente em uma dessas quedas livres.

**B fica como perfil mais letal, não como padrão recomendado.** Sua chance de zerar a ficha iniciante em 6 m já é 55,63% antes de Acrobacia, com média igual à Vida inteira. Ele só deveria avançar se a intenção for tornar quedas de poucos andares uma ameaça severa desde o início e aceitar essa variância.

Estas recomendações são uma avaliação matemática de candidatos. Ainda exigem texto de ativação/falha, geometria e testes de mesa; não são mudanças aprovadas no sistema.

## Reprodução

- `/tmp/movimento-lote2-calculo.py`: distribuições exatas de somas de d6, mistura com o d20, resistência e convolução das ocorrências repetidas.
- `/tmp/movimento-lote2-fixo.py`: acrescenta o perfil fixo e seus limiares.
- `/tmp/movimento-lote2-resultados.json`: probabilidades decimais e frações exatas para as comparações; as tabelas do relatório só arredondam a exibição.

O cálculo utiliza contagem inteira/Fraction, sem Monte Carlo. Para restaurar todas as sondas do JSON, executar o segundo script, que primeiro regenera a parte de dados e depois acrescenta o fixo.

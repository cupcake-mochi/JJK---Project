# RASCUNHO — resultados da bancada procedimental

**243 verificações passaram, incluindo 79 rejeições esperadas.** Isso confirma os casos declarados nesta bancada. Não certifica balanceamento, facilidade de uso ou integração completa com o Projeto M.

O programa foi escrito, relido e executado com Python 3, usando apenas a biblioteca padrão. Comando efetivamente executado, com saída 0:

```bash
python3 '/home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-invocacoes-2026-09-24/testes-invocacoes.py'
```

Saída: `{"verificacoes": 243, "passaram": 243, "falharam": 0}`.

O script reproduz `resultados-testes.json`. Este relatório resume essa execução; não é regenerado pelo programa. O protótipo foi apenas lido. Seu SHA-256 nesta execução foi `2009bb60aca236f485f1bbac5dea35a2bc325c3e98feb3e5016d4e6f3f516df6`. A comparação antes/depois verifica sua integridade durante o processo; não garante que nenhuma outra versão tenha sido escrita antes ou depois.

## Fixtures declaradas

- Os sete cenários usam exatamente pesos, capacidades, papéis e vidas instrumentais da tabela do protótipo. `U` identifica o usuário; `C1`, `C2` etc. seguem a ordem da composição. Não-Evocador e Singular atacam com `C1`; Parcerias, com `U + C1`; Múltiplas, com `C1 + C2`. Controlador e Batedor não recebem ataque inventado.
- Cada subteste começa num estado novo. O movimento do turno comum seleciona `U + C1`, ambos até 9 m. Os golpes comuns pressupõem alvo elegível corpo a corpo, a 1,5 m, e Concussão. O orçamento de 20 PE é uma reserva de ensaio suficiente para observar custos; não representa uma ficha legal.
- Dano focado: dois acertos fixos de 15, sem Bloquear ou cura. Cada golpe escolhe o corpo ativo de menor PV atual; empates seguem a ordem da tabela. Depois da queda, o segundo golpe escolhe outro corpo disponível. Dano excedente não migra.
- Área: todos os corpos e o usuário estão dentro dela, falham no TR e recebem 12. Os TR são contados, não simulados. A vida do usuário não foi inventada: registra-se somente o dano 12 nele.
- Troca: apenas um substituto `R`, saudável, com peso e vida máxima iguais a `C1`. A criatura original começa ferida em 8, Derrubada e com dois marcadores de persistência: um prazo de duas rodadas e um uso esgotado. Esses marcadores são sondas de estado, não novas habilidades concedidas aos cartões.
- Interceptar pressupõe adjacência e ataque originalmente dirigido ao usuário. Resposta Coordenada pressupõe orientação percebida, Abertura e destinatário elegível. As condições de elegibilidade são entradas declaradas; esta bancada verifica custos e reservas.

## Turnos, dano e entrada em combate

`P/B/M` significam Padrão/Bônus/Movimento. Pools de dano são rolagens separadas, não quantidade de dados. Erros podem reduzir o número de pools efetivamente rolados.

| Cenário | Ataque no turno comum | Movimento comum | Entrada com campo vazio |
|---|---|---|---|
| Não-Evocador + 1 | P: 1d20, até um pool de 2d6 | U + C1 | 1 P; 2 PE |
| Singular | P: 1d20, até um pool de 2d6 | U + C1 | 1 P; 2 PE |
| Parceria + 1 | P+B: 2d20, até dois pools de 1d6 | U + C1 | 1 P; 2 PE |
| Parceria + 2 | P+B: 2d20, até dois pools de 1d6 | U + C1 | 2 P; 4 PE |
| Múltiplas + 2 | P+B: 2d20, até dois pools de 1d6 | U + C1 | 2 P; 4 PE |
| Múltiplas + 3 | P+B: 2d20, até dois pools de 1d6 | U + C1 | 3 P; 6 PE |
| Múltiplas + 4 | P+B: 2d20, até dois pools de 1d6 | U + C1 | 4 P; 8 PE |

O modo conjunto alcança no máximo dois alvos distintos. Corpos adicionais não acrescentam golpes. Esse limite descreve o modo conjunto; Reações e ações concedidas elegíveis são contabilizadas separadamente. Manifestar não dá ataque de chegada. A entrada exige `n` Padrões e `2n` PE; na fixture, uma entidade entra por rodada. Entrar já manifestado conserva o gasto de PE e desloca o tempo de preparação para antes da iniciativa.

Reposicionar três ou quatro corpos usa M e a B convertida em outro Movimento: ainda sobra P, mas o modo conjunto fica indisponível. Reposicionar cinco corpos, contando o usuário e quatro invocações, usa também P convertida; não sobra ataque normal. Nenhum Movimento desloca mais de dois corpos.

## Reação inimiga, Bloquear e respostas

Nos sete cenários, dois ataques inimigos com acerto confirmado contra C1 permitem dois Bloquear: **duas resoluções de 2d10**, sem consumir Reação. Com dados fixos `[6,6]` e Defesa 15, cada resultado é 16. A bancada não inventa uma distribuição de dano líquido desses ataques.

O usuário gasta uma Reação e o conjunto de criaturas gasta outra, independentemente do número de corpos. O Guardião intercepta 12 de dano, sem novo teste de acerto e sem Bloquear a transferência. Gastar a coletiva impede oportunidade e Resposta Coordenada posteriores de qualquer invocação até a renovação prevista. Uma tentativa impossível não consome acidentalmente a Reação restante do Guia.

O Guia orientando sua própria criatura gasta **Reação do usuário + coletiva**, para um ataque concedido elegível. Uma fixture adicional aplica a dispensa da segunda Reação do Guia no nível 30: a resposta de outra invocação continua barrada especificamente pela coletiva já gasta. Isso verifica esse custo, sem implementar toda a progressão do Guia.

Foram acrescentadas duas cadeias forçadas com os critérios de Aparar/Brecha informados na revisão do projeto:

| Cadeia | Resoluções observadas |
|---|---|
| Dois ataques inimigos, ambos Bloquear `[10,10]`, sem críticos naturais | Dois Bloquear; apenas um contra-ataque coletivo de 2d6+3. Total: 3d20 de ataque, 4d10 de Bloquear e um pool de dano, supondo acerto do contra-ataque e inimigo sem Bloquear essa resposta. |
| Ataque inimigo → `[1,1]` Brecha → ataque extra do inimigo → `[10,10]` Aparar → contra-ataque da criatura → `[1,1]` Brecha no inimigo | Total: três ataques, três Bloquear, 3d20 + 6d10 e dois pools de dano. A coletiva já gasta impede um quarto ataque. |

Duplo 10 contra um 20 natural foi conferido como caso sem Aparar. As cadeias contam eventos e consumo, não probabilidades de acontecerem em mesa. O limite de duas resoluções de Bloquear pertence à fixture de dois ataques; não é um teto por rodada.

## Perda, área e reserva de vida

| Cenário | PV após foco 15 + 15 | PV após área 12 em cada | TR na área, incluindo usuário |
|---|---|---|---:|
| Não-Evocador + 1 | 6 | 24 | 2 |
| Singular | 42 | 60 | 2 |
| Parceria + 1 | 6 | 24 | 2 |
| Parceria + 2 | 6, 36 | 24, 24 | 3 |
| Múltiplas + 2 | 6, 36 | 24, 24 | 3 |
| Múltiplas + 3 | 0, 24, 24 | 12, 12, 12 | 4 |
| Múltiplas + 4 | 24, 24, 0, 0 | 12, 12, 0, 0 | 5 |

Os zeros são perdas individuais: não drenam uma barra comum. Sem socorro imediato, os corpos retirados não voltam na cena. Uma fixture adicional fornece uma cura de 5 já preparada na janela de zero: ela evita a retirada. Essa fixture verifica a janela; não cria uma fonte de cura gratuita.

Trocar exige P+B+2 PE, preserva M e conserva a vida, as condições, os usos e a coletiva já gasta. Remanifestar a criatura original também conserva o estado. A sonda de relógio aplica 3 de dano periódico e faz passar uma rodada enquanto ela está recolhida, sem apagar a condição. Não há implementação genérica de relógios ou efeitos.

**Limitar vida simultânea não limita toda a vida acessível durante a cena.** A tabela abaixo inclui a criatura original ferida e um substituto saudável, antes da sonda periódica:

| Cenário | PV máximos simultâneos | PV do substituto acrescentados ao repertório | PV restantes acessíveis, somando campo e reserva |
|---|---:|---:|---:|
| Não-Evocador + 1 | 36 | 36 | 64 |
| Singular | 72 | 72 | 136 |
| Parceria + 1 | 36 | 36 | 64 |
| Parceria + 2 | 72 | 36 | 100 |
| Múltiplas + 2 | 72 | 36 | 100 |
| Múltiplas + 3 | 72 | 24 | 88 |
| Múltiplas + 4 | 72 | 24 | 88 |

O custo paga acesso ao substituto em campo; não cura os 8 perdidos pela primeira criatura. Essa vida adicional exige tempo e futuras trocas para ser utilizada. Mesmo assim, o benefício existe e não é resolvido apenas pelo limite de 72 PV máximos em campo.

## Enumeração do d20 e cobertura

Enumeraram-se os 20 resultados para ataque +4, crítico em 20 e dados dobrados. Sem vantagens, Bloquear ou efeitos por acerto:

| Defesa | Acerto comum | Crítico | Acerto total | E[1d6] | E[2d6] = E[dois golpes de 1d6] |
|---:|---:|---:|---:|---:|---:|
| 15 | 45% | 5% | 50% | 1,925 | 3,85 |
| 17 | 35% | 5% | 40% | 1,575 | 3,15 |
| 20 | 20% | 5% | 25% | 1,05 | 2,10 |

Para Defesa 15: `0,45 × 7 + 0,05 × 14 = 3,85`. Dois golpes de 1d6 somam `2 × (0,45 × 3,5 + 0,05 × 7) = 3,85`. O programa calcula a expectativa do ataque de 2d6 separadamente da soma dos dois menores.

Defesas 17 e 20 são sondas dos acréscimos de cobertura sobre Defesa 15, usando separadamente um ataque à distância +4. Não se aplicou cobertura distante a um soco adjacente. Não foi criado um mapa nem provado que uma posição oferece cobertura. A igualdade pressupõe a mesma Defesa para cada ataque; não iguala variância, efeitos por acerto, disponibilidade de alvos ou custo de mesa.

## Controlador

Nas três composições que incluem Controlador, o uso custa **Padrão + 1 PE**, produz um TR Físico do alvo contra CD 12 e não produz teste de ataque ou pool de dano. Com TR +1, a enumeração de 1 a 20 dá dez falhas e dez sucessos: **50% de chance de Derrubado**, sem resistências ou outros modificadores.

Na fixture de falha, o alvo usa Movimento para levantar e conserva sua Padrão e Bônus. Não se converteu Derrubado em perda de Padrão nem em dano equivalente. A tentativa com 0 PE é rejeitada sem gastar ação.

## Testes negativos e limites

### Sonda espacial: três passagens

**Premissa exclusiva desta sonda:** um corpo estacionado obstrui sua passagem de 1,5 m para um inimigo terrestre sem voo ou teleporte. Isso não declara que toda invocação recebe esse efeito na regra vigente. Não há motor de mapa; enumeram-se três passagens paralelas independentes A, B e C.

C1 ocupa A; C2, B; C3, C; C4 fica numa área de espera fora de todas as passagens. A geometria é abstraída, sem simular física ou bloqueios em série. A posição inicial é fornecida e seu custo anterior não é apagado. Enquanto permanecem imóveis, a hipótese de obstrução não exige novas ações, Reações ou PE.

| Corpos estacionados | Rotas livres | Ocupante único retirado | Rotas livres depois |
|---:|---:|---|---:|
| 1 | 2 | C1 de A | 3 |
| 2 | 1 | C1 de A | 2 |
| 3 | 0 | C1 de A | 1 |
| 4 | 0 | C1 de A | 1 |

A remoção é uma alteração externa da fixture: não representa recolher gratuitamente. Retirar C1 reabre A inclusive no cenário de quatro corpos, porque C4 está fora das passagens e não se reposiciona automaticamente.

**Resultado condicional:** com essa premissa espacial, três corpos obstruem três passagens mesmo que o modo conjunto só permita dois ataques. O teto de ações não mede sozinho o benefício passivo de ocupar espaço. A aplicação dessa premissa a criaturas reais e a formas de atravessar/enfrentar a obstrução permanece uma decisão de regra e de mesa.

### Escopo das rejeições

Entradas deliberadamente inválidas tentaram acrescentar terceiro ataque, terceira criatura no modo conjunto, segunda Reação coletiva, ataque para Batedor, dados de arma maiores, Sequência/Ataque Extra, cura por troca, remoção de condições, renovação de usos/Reação, interceptação recursiva e retorno após zero. Também foram rejeitados excesso de capacidade, quinto corpo e manifestação com apenas 1 PE, sem consumir ações ou PE. O teto de quatro corpos foi isolado numa sonda de capacidade 10, sem transformar esse valor numa composição aprovada. Os casos negativos não alteram o protótipo ou a fixture positiva original.

Essas rejeições demonstram o comportamento do validador escrito para o ensaio. Não demonstram que toda redação possível do sistema seja inequívoca, que o validador não tenha outras falhas ou que as regras sejam equilibradas. Parte dos contadores decorre diretamente da sequência declarada; não se trata de simular todos os turnos possíveis.

Continuam fora do programa: motor geral de mapa, distâncias reais, percepção/comunicação, catálogo completo de condições, seleção estratégica, dano líquido após Bloquear, probabilidades das cadeias de Reação, concentração, energia temporária, custos de origem, progressão completa do Guia, demais Caminhos e duração real de turno. A sonda das três passagens é a única geometria enumerada e depende de uma premissa explícita. Incapacitado, Atordoado e Lento foram lidos na versão final, mas suas interações não foram simuladas. As regras são transcritas em fixtures; editar o protótipo não atualiza automaticamente o código. O hash registra qual arquivo acompanhou a execução.

Para o próximo ensaio, a decisão mais relevante revelada por estes casos é **como obter e limitar substitutos no repertório**. Uma Singular com reserva saudável mantém 72 PV máximos simultâneos, mas já dispõe de 136 PV restantes acessíveis depois do primeiro ferimento instrumental. O teste aponta esse benefício para avaliação; não recomenda um preço ou limite novo.

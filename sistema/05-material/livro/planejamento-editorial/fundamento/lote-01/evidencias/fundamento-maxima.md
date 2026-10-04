# Auditoria de Técnica Máxima — 2026-10-03

Auditoria paralela para R06/R08. Não altera livro publicado, candidato ou fonte mecânica. Arquivos auxiliares da primeira passagem: `/tmp/fundamento-maxima-auditar.py` e `/tmp/fundamento-maxima-evidencias.json`. A conclusão numérica vigente usa `/tmp/fundamento-maxima-auditar-descontos.py` e `/tmp/fundamento-maxima-descontos.json`.

## Conclusão recomendada

A reclamação do jogador é sustentada pelo texto e pela conta. O capítulo apresenta a Máxima repetidamente como golpe, só ensina dois exemplos ofensivos e não entrega um procedimento completo para suas alternativas. Há também regressão real: a mesma montagem pode deixar de caber quando o personagem sobe do nível 20 para o 21.

Recomendo **corrigir o orçamento 8/8/12 para 8/12/16**, preservar dano-base, PE e recarga, separar claramente montagem ofensiva, cura e Efeito sem dano, e explicar um **Efeito Máximo próprio** com ficha de alcance, oposição, duração e encerramento. Não recomendo o novo orçamento utilitário 24/28/32 nesta rodada: a busca encontrou nova regressão no nível 26 e ele não garante benefício em relação a feitiço comum.

A correção numérica está calculada, mas aumenta a variedade de combinações nas faixas altas; isso precisa constar no registro de mudanças. O restante pede decisões de R08 registradas como mecânicas candidatas, sem alegar que uma simples reescrita curou todos os problemas. Exemplos de Efeito fora de combate podem ser completados já; controle/proteção/movimento de combate exigem definir o resultado central, não apenas aumentar a quantidade de pontos.

## Donos lidos e pontos de referência

Caminhos relativos à raiz `/media/mizuki/HD Externo II/Claude/Claude 2`.

| Fonte | Linhas | Relevância |
|---|---:|---|
| `sistema/05-material/livro/manual/40-fundamento.md` | 95–120 | preços por Classe e limite de quatro Melhorias |
| mesma | 234–242 | Famílias Livres, Fechadas e Formas |
| mesma | 480–528 | Formas e escadas; Toque e Aura já trazem Corpo a Corpo |
| mesma | 564–587 | controle sem dano e seus bônus |
| mesma | 602–628 | alcance, movimento e área |
| mesma | 655–663 | Anteparo, Terreno, Prende e oposição |
| mesma | 709–718 | Guarda, Pressa e demais auxiliares |
| mesma | 747–767 | custos de ação e duração |
| mesma | 810 | Efeito Próprio e proibição de comprimir várias peças numa |
| mesma | 910–935 | Efeito fora de combate; escala Máxima e duração indefinida |
| mesma | 962–996 | regra inteira da Máxima e exemplos exclusivamente ofensivos |
| `manual/gerador/partE.js` | 86–121 | confirma origem da mesma redação, não é uma errata posterior |
| `sistema/05-material/livro/manual/42-tecnica-marcial.md` | 9–35 | equivalência de Kata, Ruptura e Ōgi; Ōgi também chamado golpe |
| `sistema/03-mecanica/25-sem-tecnica.md` | 35–65 | Manejo/Auge herdam a máquina, sem números novos |
| `sistema/05-material/livro/manual/43-sem-tecnica.md` | seção Auge | cópia de jogador deve acompanhar a Máxima |
| `sistema/05-material/livro/manual/60-invocacoes.md` | seção Técnica Máxima | domada usa orçamento 8/8/12, dano reduzido próprio; correção não pode ser esquecida aqui |
| `sistema/05-material/livro/planejamento-editorial/regras-basicas/lote-01/TESTES-E-TURNOS.md` | 171 | rodada inteira consome padrão, bônus e movimento; conserva Reação |

## Contrato que deve continuar verdadeiro

- Nível mínimo 17; faixas 17–20, 21–25 e 26–30.
- Dados-base 24d8, 28d8 e 32d8: médias 108, 126 e 144. “Fixo” deve significar quantidade base de dados, não resultado invariável da rolagem.
- PE 25/30/35 = cinco vezes maior Classe; rodada inteira; nova utilização após o fim do terceiro turno seguinte.
- Melhorias usam preços/escala da maior Classe. A Máxima não se transforma num feitiço de Classe 8.
- Restrições não devolvem pontos; Famílias Fechadas continuam limitando as escolhas.
- Um efeito não pode ganhar quatro benefícios cobrados como uma única Melhoria própria.
- Alterações não criam nova aptidão canônica nem acesso automático a poder alheio à Regra/rota.
- Ōgi e Auge recebem a mesma alteração; domada conserva sua tabela de dano reduzido.

## Achados

### M01 — Regressão de orçamento (mecânico, reproduzido)

| Faixa | Maior Classe | Orçamento atual | Leve/Média/Pesada | Pesada cabe? |
|---|---:|---:|---|---|
| 17–20 | 5 | 8 | 3/5/8 | sim |
| 21–25 | 6 | 8 | 3/6/9 | não |
| 26–30 | 7 | 12 | 4/7/11 | sim |

Uma Máxima de Onda perde a própria Forma no nível 21, sem Família Livre ou qualquer alteração da ficha. Linha + Muito Longe custa 8, depois 9, depois 11; o exemplo publicado também deixa de caber. O defeito independe do gosto pela habilidade.

**Revisão após contraponto do agente principal:** conferir só preços neutros não bastava. Quatro Melhorias Médias de Família Livre custam 8 na Classe 5 e 12 na Classe 6. A primeira proposta de 9 pontos ainda descartava sete perfis. O menor reparo uniforme, preservando também novas montagens abertas no nível 21, é **8/12/16**.

A busca ampliada enumerou **840 perfis**: Forma sem custo/Leve/Média/Pesada e de zero a quatro Melhorias de cada faixa, em Família Livre ou neutra. Usa desconto arredondado para cima, piso de um ponto por Melhoria e nenhum desconto automático na Forma. Os perfis são um superconjunto das montagens reais; isso torna a prova de suficiência conservadora. Duas montagens concretas abaixo demonstram que os limites inferiores também são necessários.

| Orçamentos | Perfis que cabem nas Classes 5/6/7 | Perdas 5→6 | Perdas 6→7 |
|---|---|---:|---:|
| publicado: 8/8/12 | 68/42/85 | 26 | 0 |
| primeiro reparo: 8/9/12 | 68/64/85 | 7 | 0 |
| 8/12/12 | 68/133/85 | 0 | 48 |
| 8/12/15 | 68/133/150 | 0 | 2 |
| **8/12/16** | **68/133/175** | **0** | **0** |

**Por que 12 é necessário no nível 21:** Projétil + Troca + Perseguir + Fura + De Novo, com Alcance e Mira Livres, contém quatro Médias: 2+2+2+2=8 na Classe 5 e 3+3+3+3=12 na 6. Também se pode construir o perfil com Apoio + Firmeza + Guarda + Pressa + Duradoura, Auxiliares e Tempo Livres, embora Apoio possua outra lacuna de conversão independente da conta.

**Por que 16 é necessário no nível 26:** Projétil + Longe + Passo + Empurrão + Precisão, com Alcance e Mira neutras, custa 3+3+3+3=12 na Classe 6 e 4+4+4+4=16 na 7. Explosão + Longe + Passo + Precisão também é testemunha, com a Forma ocupando a quarta parcela Leve. Ambas podem ser montadas no nível 21; protegê-las exige 16 depois.

Se o contrato fosse apenas preservar as escolhas disponíveis no nível 17, 8/12/12 bastaria para esse subconjunto. Mas ele quebraria escolhas feitas entre os níveis 21 e 25, repetindo o problema do jogador. Por isso esse contrato mais fraco foi rejeitado.

O reparo aumenta opções ofensivas também. **Não é uma correção sem aumento de força:** preserva dano-base, ação e PE, mas comporta mais peças nas faixas altas. É o custo explícito da monotonicidade com os preços e descontos atuais. Alternativa seria congelar preços de montagem da Máxima numa única Classe, com outra revisão mais ampla de escala; não foi adotada nesta recomendação. Perfis não são builds semanticamente aprovadas: a enumeração não prova combinação, oposição ou equilíbrio final.

### M02 — “Qualquer Forma” não tem resposta para Apoio (mecânico/textual)

Apoio converte cada ponto restante em 3 PV temporários. A Máxima diz que suas sobras se perdem e que Formas sem dano usam escala Máxima ou cura. Não diz se Apoio usa os pontos do orçamento, os 24/28/32 dados ou uma quantidade própria. Portanto, **não existe resultado único sustentado pelo texto**.

Três interpretações diferentes seriam 24/36/48 PV com o orçamento corrigido (antes de comprar melhorias), 72/84/96 PV (3 por dado-base), ou nenhum PV automático. A última é a mais conservadora para uma montagem utilitária que usa Apoio apenas para chegar ao aliado; qualquer montante especial de PV deve ser decisão explícita de R08.

Onda torna a interpretação numérica especialmente sensível porque não divide o benefício. Quatro aliados recebendo 72 PV seriam 288 PV de proteção distribuída por 25 PE; quatro recebendo cura média 108 seriam até 432 PV restaurados, limitados pelas perdas prévias. Isso não prova que a proteção está equilibrada: PV temporário pode ser aplicado antes da luta e tem janela diferente. **Não recomendar 72/84/96 automaticamente só porque é menor que a cura.**

### M03 — Controle tem uma saída formal, mas ela está inadequada para ensinar Máxima (mecânico/textual)

O capítulo dá +1 rodada e +2 CD ao feitiço sem dano com Controle, mas descreve esse resultado como gastar todos os pontos. Na Máxima gastar pontos não remove nenhum dos dados fixos. O jogador que quer só controlar não tem como executar a instrução.

Esclarecimento conservador: permitir registrar uma Máxima sem dano, sem reembolso por cada dado descartado. Não aplicar automaticamente a esse caso o bônus de controle da construção comum: ele depende de um trade-off de dados/pontos que não existe na Máxima. Registrar a decisão no contrato, pois é delimitação mecânica.

Essa saída por si só **não torna a Máxima de controle competitiva**. Um efeito pequeno, que já cabe num feitiço comum, deveria continuar comum. A peça criativa da Máxima deve ser o resultado central de Efeito, previamente definido e limitado.

### M04 — Efeito promete mais do que consegue resolver (mecânico, maior risco)

A tabela autoriza cidade inteira, esquecer nome coletivo, impedir saída de bairro e noite que não amanhece, “até alguém desfazer”. Não define alcance de instalação, alvos involuntários, oposição, como se desfaz, nem o que ocorre quando o combate começa. Uma promessa dessa escala pode derrotar campanha inteira por 25 PE sem contrajogo.

Cidade é referência de **abrangência**, não licença para impor qualquer condição a toda população. Não usar “escala Máxima” como atalho para automaticamente petrificar, apagar memórias, impedir ações ou superar barreiras de outro criador. A duração e o encerramento precisam estar na ficha. Cidade + duração infinita + ausência de oposição não é parâmetro de equilíbrio.

### M05 — Falta declaração de compatibilidades

- **Toque/Aura:** conservar entrega curta, mas nenhuma devolução por Corpo a Corpo embutida na Máxima. Do contrário a proibição de Restrição não fecha a conta.
- **Rápido/Reação:** não podem reduzir a rodada inteira de uma Máxima. Se a peça troca apenas uma Ação Padrão, não encontra esse custo aqui.
- **Família Livre:** declarar se o desconto vale. Recomendação: vale nas Melhorias, como na máquina comum; não se estende automaticamente ao preço da Forma. O original não destaca isso e exemplos neutros não demonstram o desconto.
- **Número de Melhorias:** declarar quatro, mais a Forma, mesmo sendo habilidade sem Classe própria. Usar a maior Classe como referência, sem orçamento virar ausência de limite.
- **Condição pesada:** conservar uma por montagem e TR ao fim de turnos. “Reduz dano em um quarto” não significa resistir só a um quarto da condição.
- **Dano total/área:** o exemplo oficial da própria regra entrega 24d8 em cada alvo da linha, incompatível com aplicar cegamente 4×Classe somando todos os alvos. Não afirmar que o teto comum automaticamente fiscaliza Máxima.
- **Queima/Remate/Fica/Estilhaço:** são modificadores e repetições, enquanto “dano fixo” parece proibi-los. Antes de validar dano final precisa definir se a tabela fixa dados-base ou dano total. `Toca a Alma` reduz os dados e já foi modelado no `manual/matematica/v7.py`; não apagar essa interação silenciosamente.
- **Recarga + Acúmulo:** não pode criar sequência de usos em rodadas seguidas quando recarga proíbe.

## Comparação externa: o que aproveitar

Pesquisa em 03/10/2026; apenas fontes primárias de regra para as comparações.

| Referência | Solução observada | Aplicação ao Projeto M |
|---|---|---|
| [D&D 2024: Forcecage](https://www.dndbeyond.com/spells/2618916-forcecage) | Controle de nível alto descrito por prisão, tamanho, duração, concentração e formas de saída; não depende de uma quantidade de dano para existir. | Escrever o resultado central e a oposição da Máxima. Não importar prisão automática, preço em ouro ou números de outro sistema. |
| [PF2 Player Core: Synaptic Pulse](https://2e.aonprd.com/Spells.aspx?ID=1710) | Controle em área declara alvos, defesa, duração e resultados diferentes conforme sucesso; possui Incapacitation. | Controle precisa informar resposta de cada alvo. Não importar graus de sucesso nem atributo de defesa sem conversão. |
| [Fate Core: Building Stunts](https://fate-srd.com/fate-core/building-stunts) | Habilidade própria pode acrescentar uma ação ou exceção delimitada; exemplos e limites definem o que a exceção compra. Ramificações oferecem usos novos, sem só aumentar números. | Melhor referência para Efeito Máximo próprio: uma exceção concreta com fronteira e custo, em vez de lista crescente de bônus. É a solução diferente dos catálogos fechados de D&D/PF2. |

Esses livros mostram métodos de apresentação/limitação. Não demonstram que uma Máxima específica está equilibrada dentro do Projeto M.

## Verificação de cânone

Foi localizado o [capítulo 134 na VIZ](https://www.viz.com/shonenjump/jujutsu-kaisen-chapter-134/chapter/21808). O acesso aberto mostrou a página de entrada, mas o capítulo exige assinatura; **os painéis não foram verificados nesta auditoria**. Não atribuir à leitura da VIZ uma confirmação de extração, conversão ou uso de Uzumaki.

A [errata oficial do fanbook](https://sp.shonenjump.com/j/notice/2021/03/04/210304_oshirase001.html) corrige Uzumaki de “maldição utilizada” para “técnica” na página 70. Isso confirma uma classificação, não sua lista de efeitos. Wiki serve para localizar o capítulo, não para preencher a lacuna.

Portanto os exemplos propostos abaixo são **exemplos originais do sistema**, sem atribuí-los a personagens ou declarar que todas as Máximas da obra funcionam assim. PE, níveis, orçamento e recarga são convenções do Projeto M. Não usar o número da Máxima do jogo como afirmação sobre a obra.

## Texto pronto recomendado para candidata

### Técnica Máxima

No nível 17, você desenvolve uma aplicação excepcional da sua técnica. Ela pode concentrar um ataque, restaurar aliados ou produzir um efeito próprio. Escreva essa aplicação na ficha antes da sessão, com o mestre. A Regra da sua técnica e suas Famílias continuam limitando o que ela faz.

| Nível | Dados-base, quando houver dano ou cura | Pontos para Forma e Melhorias | PE |
|---|---|---:|---:|
| 17–20 | 24d8 | 8 | 25 |
| 21–25 | 28d8 | 12 | 30 |
| 26–30 | 32d8 | 16 | 35 |

O orçamento de montagem compra a Forma e até quatro Melhorias, nos preços da sua maior Classe. As Melhorias de Família Livre recebem o desconto normal; Famílias Fechadas continuam indisponíveis. Pontos de montagem não compram dados, e pontos que sobrarem se perdem.

A Máxima não recebe pontos de Restrição. Toque e Aura mantêm sua distância e posição de origem, mas não devolvem pontos por Corpo a Corpo. Ela custa Rodada inteira e não pode receber Rápido ou Reação para reduzir esse custo.

Depois de usá-la, espere terminar seu terceiro turno seguinte para poder usá-la novamente. O efeito, a duração e os alvos são os registrados na montagem; você não troca esses elementos a cada uso.

**Dano e cura.** Use os dados-base da sua faixa. A Forma e as Melhorias definem como o efeito chega ao alvo. Se o alvo resistir a uma Máxima de dano, ele recebe três quartos do dano. Isso não aplica condições nem outros efeitos que o teste evitou.

**Efeito sem dano.** Você pode registrar a Máxima sem dano nem cura. Nesse caso, escreva o resultado concreto que deseja produzir. Defina seus alvos ou área, como chega até eles, quanto dura, como alguém resiste e como o efeito termina. Os pontos de montagem continuam pagando Forma e Melhorias; abrir mão dos dados não devolve pontos. Não receba PV temporários apenas por usar Apoio nessa montagem: se houver proteção em PV, sua quantidade precisa estar definida pelo efeito aprovado.

**Efeito fora de combate.** A escala Máxima permite propor uma alteração que alcance uma cidade. A abrangência não elimina oposição nem concede qualquer poder ao personagem. Um efeito que impede ações, prende criaturas, altera memórias ou atravessa barreiras precisa declarar essas consequências e suas respostas na ficha. Um efeito sem oposição não pode passar a prejudicar criaturas por simples mudança de descrição.

**Antes de aprovar.** Compare com um feitiço comum que já realize a mesma tarefa. Se a mesma montagem entregar o mesmo resultado com menos energia e sem um custo adicional relevante, use-a como feitiço comum. A Máxima precisa de um alcance de aplicação ou uma capacidade central que a ficha realmente queira reservar para esse momento.

### Ficha de Efeito Máximo próprio

1. **Resultado:** uma alteração que qualquer jogador consiga reconhecer na cena.
2. **Aplicação:** alvos, área, origem e alcance; distância em múltiplos de 1,5 m.
3. **Oposição:** defesa ou TR quando houver criatura hostil afetada; resultado no sucesso; eventual teste para sair ou encerrar.
4. **Duração:** quanto permanece; concentração quando aplicável; que acontecimento encerra antes.
5. **Limites:** o que o efeito não atravessa, não revela ou não modifica; relação com barreiras e efeitos de outras criaturas.
6. **Montagem:** Forma, peças compradas, custo de cada uma, total, PE e ação.

Uma nova capacidade não é grátis só por aparecer na descrição. Se ela puder ser representada pelo catálogo, pague suas peças. Se realmente precisar de Efeito Próprio, registre seu custo e a comparação que justificou esse custo. Conte benefícios independentes separadamente.

**Nota editorial:** o checklist acima serve no material de montagem/aprovação. Não repetir seis campos em todo exemplo básico do capítulo inicial; apresentar uma primeira ficha curta e direcionar o leitor de nível alto ao procedimento avançado.

## Exemplos utilizáveis e limites honestos

### 1. Híbrida de movimento: Fenda de Arrasto (montagem já suportada)

Nível 17; Projétil 0 + Empurrão Leve 3 + Passo Leve 3 = 6/8; duas Melhorias; 25 PE; rodada inteira. A Regra desta técnica comprime e libera a distância de fios esticados. O ataque causa os 24d8 base; Empurrão desloca o alvo até 6 m e Passo desloca você até 6 m antes ou depois sem ataque de oportunidade.

É evidência de que movimento pode compor a Máxima, não solução para quem quer renunciar a dano. A revisão geral deve fixar oposição e destino do Empurrão; sem isso, não declarar o exemplo inteiramente pronto para mesa. Precisa espaço de chegada permitido, não atravessar ocupação/barreira nem multiplicar dano de queda gratuitamente.

### 2. Controle e posição, sem depender de atordoar (proposta de teste, não pronta)

Para futura versão utilitária: Explosão + Prende + Puxa + Escolher + Duradoura custariam 3+5+5+5+5 = **23** na Classe 5; 27 na 6; 32 na 7. A imagem é fios que recolhem adversários para uma área enquanto aliados passam. Exige TR inicial contra as peças hostis, ação/TR para escapar de Prende e duração clara; Duradoura não transforma o deslocamento instantâneo de Puxa em repetição a cada turno.

Não cabe no orçamento base 8/12/16. Cabe no pool utilitário experimental, mas feitiço comum com duas Restrições também pode montá-lo. Portanto não publicar como Máxima mecanicamente resolvida só porque a conta fecha. Serve de caso concreto para R08 avaliar uma capacidade central própria ou abandonar o pacote como feitiço comum.

### 3. Efeito de travessia: Passagem de Papel (contrato original delimitado, fora de combate)

Exemplo de escrita de Efeito Máximo para técnica cuja Regra é unir, com papel dobrado, superfícies previamente marcadas. **Proposta individual para testar:** duas marcas fixas, ambas visitadas e colocadas pelo usuário na mesma cidade; até 1.500 m uma da outra; abertura com 3 m de largura, por 1 minuto. Uma criatura entra voluntariamente e gasta 1,5 m de seu deslocamento para aparecer num espaço livre imediatamente diante da outra marca. Não atravessa barreira ativa entre os dois pontos, não retira uma criatura agarrada contra a vontade de quem a prende, não transporta objeto que não caiba na abertura, nem funciona através de marca destruída. Danificar uma marca encerra a passagem. O usuário pode encerrá-la; ninguém fica dentro da passagem quando ela fecha.

Forma Efeito; resultado original precisa de Efeito Próprio antes de fechar o custo. A faixa de custo candidata é Pesada = 8 na Classe 5, mas o valor **não está validado**: deslocamento de grupo em cidade afeta missões, perseguições e transporte. PE25/30/35 e ação/recarga normais. Não publicar preço8 como dado existente. Esse exemplo demonstra o grau de completude necessário e é diferente de prometer “mover pela cidade” sem destinos/restrições.

### 4. Efeito de informação sem onisciência: Avisos na Chuva (contrato original delimitado, fora de combate)

Para técnica cuja Regra registra vibrações em gotas depositadas. Proposta: por dez minutos, receber de até doze recipientes próprios previamente distribuídos na mesma cidade um aviso quando uma criatura visível no local atravessar uma passagem de 3 m marcada pelo recipiente. O aviso identifica apenas qual recipiente disparou, não nome, grau, aparência ou intenção. Não detecta além da passagem, não segue criatura, não vence ocultação/barreira por ser Máxima, e para com destruição/remoção da marca. O criador precisa estar na mesma cidade e manter concentração.

Também exige Efeito Próprio com preço e utilidade comparados à versão comum. **Pode ser fraco demais para 25 PE** dependendo do sistema de sentinelas: é precisamente o teste que impede chamar todo efeito grande de Máxima. Não é exemplo canônico nem deve ser vendido como Máxima equilibrada. Se couber na Classe 5 comum, deve ir para ela.

Os exemplos 3 e 4 são úteis para a revisão por exibirem o procedimento e seus riscos. Para o livro do jogador, escolher somente um após a comparação e o teste, em vez de fingir que ambos passaram.

## Alternativas calculadas e decisão

| Alternativa | Vantagem | Falha/riscos | Recomendação |
|---|---|---|---|
| Só reescrever “não serve só para dano” | Nenhuma mudança numérica | Mantém orçamento regressivo e Apoio indefinido | insuficiente |
| 8/12/16, campos de efeito/oposição e exemplos | Corrige regressão e permite explicar criatividade sem inflar todos os ataques | Não cria automaticamente Máximas de controle competitivas | adotar base e preparar R08 |
| Permitir Restrições e manter dados cheios | Mais peças | Somar desconto e restrições baratas pode produzir grande pacote +108/126/144; precisa busca semântica completa | não adotar agora |
| Vender dados individualmente por pontos | Flexibilidade gradual | Reabre identidade e curva inteira; permite otimização de pequena perda por grande Controle | não adotar agora |
| Sem dados, orçamento24/28/32 | Permite quatro efeitos importantes sem Restrição | RegressãoClasse6→7; muitas montagens dominadas por comuns com Atrasar | rejeitado na forma testada |
| Sem dados, orçamento escalonado por custos 24/27/33 | Corrige pacote neutro do exemplo | Ainda perde outros perfis e não elimina dominância; número nasce de caso, não de eixo completo | não adotar por remendo |
| Apoio3PV por dado-base | Define proteção forte, fácil de entender | 72/84/96 por aliado; Onda multiplica; muda preparação de combate | teste separado, não necessário agora |
| Efeito central próprio com limites e orçamento auxiliar8/12/16 | Capacidade nova, criativa, em vez de dano obrigatório | Exige catálogo mínimo de exemplos realmente julgados; preço não emerge só da gramática | caminho recomendado para R08 |

## O que o próximo validador deve cobrir

1. Preservação de faixa, dados-base, PE, ação e recarga.
2. Monotonicidade: cada montagem já aprovada continua possível após cada mudança de Classe; não só checar uma Pesada isolada.
3. Quatro Melhorias + Forma; soma de partes independentes; Famílias Livres/Fechadas e desconto explicitamente definido.
4. Não devolução de Corpo a Corpo na Máxima; Rápido/Reação impedidos de trocar rodada inteira.
5. Separação entre TR de dano e resultado de cada efeito; teste de término de condições pesadas.
6. Movimento não atravessa obstáculo, suporte ou espaço ocupado sem permissão; distância/destino explícitos.
7. Duração não repete resultado instantâneo; escala não amplia alcance sem regra; cidade não anula resistência.
8. Comparação de utilidade contra feitiço comum com Atrasar, e também contra comum com duas Restrições que de fato cobram algo na mesa.
9. Cura, PV temporário e parede não contam como mesma moeda: comparar alvos, preparação, duração e dano absorvido real.
10. Espelhos Ōgi/Auge/domada atualizados sem substituir sua natureza ou dano próprio.
11. Pendência Integridade após revisão de Morrendo: Toca a Alma e Remenda dependem dela; não usar esta auditoria para certificar novo sistema de morte.

Resultado atualizado: sete checagens do reparo com descontos passaram em 840 perfis, incluindo testemunhas concretas dos dois mínimos. A primeira passagem, somente neutra, foi insuficiente e está preservada como histórico de auditoria. Não há certificação global de equilíbrio nem leitura de jogadores; compatibilidades e dano final ainda precisam da matriz semântica do capítulo completo.

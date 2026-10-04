# Reavaliação 04 — regras comuns, sentido e funcionamento

02/10/2026. Auditoria adversarial dos lotes 02 e 03 lidos nesta rodada contra a v0.331 e Caminhos integrados. Os achados descrevem o retrato anterior às correções anunciadas pelo autor durante a auditoria. Não editei fontes e não usei Git.

Arquivos candidatos:
- `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-02/02-SALTOS-E-QUEDAS.md` — 135 linhas no retrato.
- `sistema/05-material/livro/planejamento-editorial/regras-comuns/lote-03/03-PERCEPCAO-E-FURTIVIDADE.md` — 125 linhas no retrato.

Abreviações: **M** = `sistema/05-material/livro/manual/`; **I** = `caminhos/05-Edicao-Integrada/`; **P** = `sistema/03-mecanica/`. Raiz: `/media/mizuki/HD Externo II/Claude/Claude 2/`.

## Conclusão

Há atalhos reais, que conferir apenas exemplos escolhidos e a presença de termos não detectou. Dois merecem correção direta: saltinhos neutralizam o custo de terreno difícil; e a manutenção gratuita permite voltar a desconhecer uma posição que o observador acabou de ver durante o ataque. Alterar somente CD 8 para CD 10 não resolve o segundo.

A fórmula curta de Furtividade também omite a especialização vigente. A combinação entre a nova regra de fumaça e o Cego atual produz a consequência contrária ao esperado: acrescentar cegueira aos dois combatentes pode melhorar a precisão de ambos. O radar energético é uma capacidade nova de exploração; não está validado por dizer que preserva nomes de habilidades.

Recomendo aposentar a manutenção universal e o radar universal desta versão, corrigir os custos de saltar no terreno e completar os bônus de perícia. A alteração de Cego pode ser pequena, mas deve ser registrada como alteração mecânica da condição.

## 1. Saltos curtos contornam terreno difícil

**Onde:** lote02:24–31, 40, 46, 58, 60. O custo adicional está ligado a caminhar/escalar/nadar. Saltos custam somente a maior distância entre avanço e subida; saltos pequenos no mesmo piso não exigem teste.

**Cena reproduzível:** 9 m de piso firme sob o efeito **Terreno**, obscurecimento desligado, opção de terreno difícil (M40-fundamento.md:658). Personagem com Força 0 e 9 m disponíveis. O salto parado alcança 1,5 m. Ele faz seis saltos de 1,5 m, cada um começando e terminando no piso difícil. Pela redação, paga 9 m e atravessa. Andando, precisaria de 18 m; com seu movimento inicial só atravessaria 4,5 m.

Não depende de inventar apoio no cenário nem de rolar alto. Transformar toda aterrissagem em um teste novo também não resolve o custo e acrescenta rolagens que o projeto tentou evitar.

**Menor correção:** um salto que começa, atravessa ou termina **dentro do mesmo trecho difícil sem realmente ultrapassá-lo** continua sujeito ao custo de terreno pertinente. Só ultrapassar o obstáculo por inteiro e aterrissar em piso regular evita a dificuldade daquele obstáculo. A redação precisa distinguir atravessar um obstáculo com salto de saltitar dentro da área difícil; não basta dizer que saltar custa movimento.

**Contra-teste:** um vão/canteiro de lama de 1,5 m entre dois apoios regulares pode ser ultrapassado por um salto capaz de atravessá-lo. Isso não deve virar dois custos de terreno só porque há lama lá embaixo. O benefício depende da geometria real, não de anunciar “pulo” a cada quadrado.

## 2. Manutenção gratuita permite apagar uma exposição real

**Onde:** lote03:106–117 e exemplo 125. A mesma regra permite expor-se pela lateral, adia a revelação para depois do ataque e então oferece teste gratuito para manter ocultação se terminar de volta atrás da cobertura.

**Cena reproduzível:** o arqueiro oculto aparece pela lateral das caixas, atira e volta atrás delas. O vigia viu o arqueiro e o espaço de onde ele disparou. O exemplo permite que Furtividade com desvantagem faça o vigia continuar sem localizá-lo. Não existe mudança de esconderijo, distração nem habilidade especial: o dado apaga uma observação já produzida.

Isso se aproxima de Esconder grátis após atacar, apesar do rótulo “manutenção”. O requisito de começar oculto impede que qualquer ataque gere ocultação do nada, mas não impede a repetição do benefício em ataques e turnos seguintes. O Assassino 11 entrega Esconder sem ação **depois de um movimento**, em posição apropriada, uma vez por turno (I06-Incursor-Caminho-e-Trilhas.md:261–271); a regra geral pode renovar a vantagem sem esse movimento.

**Conta executada por enumeração do d20:**

| Furtividade / Percepção | CD base | Esconder | Manutenção sem ação, com desvantagem |
|---|---:|---:|---:|
| +4 / +4 | 8 | 65% | 42,25% |
| +4 / +4 | 10 | 55% | 30,25% |
| +12 / +4 | 8 | 100% | 100% |
| +12 / +4 | 10 | 95% | 90,25% |

O último caso é possível com Destreza 6, maestria 4 e especialização +2. Isso não prova que um veterano vencer um vigia seja errado. Prova que baixar a probabilidade não corrige a economia de ação nem a contradição entre exposição e posição desconhecida.

**Menor correção recomendada:** retirar a manutenção universal. Ataque acerte ou erre revela a posição a observadores capazes de perceber o ataque; esconder-se novamente segue Padrão, Bônus do Incursor ou Desaparecer do Assassino. Preservar o benefício do primeiro ataque declarado oculto sem estendê-lo automaticamente à sequência. Silencioso e outras exceções expressas permanecem específicas.

**Decisão antiga:** P14-equipamento.md:1825 prevê fogo revela/resto testa. A nova solução substitui esse compromisso **na candidata**, com a nova autorização do usuário; não deve continuar se apresentando como mera preservação daquela decisão.

**Limite importante:** saber a posição e enxergar não são a mesma coisa. A regra que impede repetir o truque da lateral não pode apagar a vantagem vigente contra um alvo Cego, ou a desvantagem de atacar alguém não visto só porque sua posição foi informada.

## 3. A fórmula de Furtividade perde especialização

**Onde:** lote03:36. Publica `d20 + Destreza + maestria, se treinado` como fórmula completa.

**Regra vigente:** M45-aptidoes-e-refino.md:67, M80-experiencia-e-progressao.md:314 e P11-aptidoes-e-refino.md:159–166. Especialização concede metade da maestria adicional; no nível 26, vale +2. P04-pericias-e-testes.md:17 também reconhece esse segundo grau de treino.

**Cena reproduzível:** Destreza 6, maestria 4, especialista. Bônus correto +12; a fórmula impressa dá +10. Contra CD 18, a chance cai de 75% para 65%, e o resultado guardado para buscas perde dois pontos. A compra do personagem deixa de funcionar no procedimento que deveria usar essa perícia.

A fórmula de Percepção fala em outros modificadores permanentes, o que pode incluir especialização; isso não resgata a fórmula explícita de Furtividade e ainda cria assimetria de leitura.

**Menor correção:** remeter ao bônus completo de Furtividade da ficha. Caso mostre a fórmula expandida, incluir especialização e outros modificadores aplicáveis. Fazer o mesmo para a CD passiva de Percepção. A mudança para base 10 é uma decisão sobre observação passiva; não deve reescrever CDs de resistência das classes.

## 4. A nova fumaça e o Cego vigente invertem o resultado quando ambos ficam Cegos

**Onde:** lote03:98–102 versus M15-dano-e-condicoes.md:216–224.

**Cena reproduzível:** duas criaturas sabem os espaços uma da outra, mas estão em fumaça densa. Pela candidata, cada ataque recebe desvantagem porque ninguém enxerga e a vantagem por atacante não visto exige enxergar o alvo. Agora aplique **Cego** nas duas: cada uma continua com desvantagem nos próprios ataques, porém a condição da outra concede vantagem a quem a ataca. Pelo cancelamento normal, ambas voltam a atacar normalmente.

Acrescentar cegueira a ambos melhorou a precisão. A frase “condições específicas mantêm seus textos” torna a combinação legal, em vez de consertá-la.

**Menor correção aceitável:** na candidata, exigir visão ou sentido substituto para a vantagem concedida contra Cego, alinhando-a ao procedimento de combate sem visão. Preservar a falha automática em testes estritamente visuais e os demais efeitos. Registrar a mudança da condição Pesada; não chamá-la de simples esclarecimento.

**Vulto:** a regra também deve esclarecer que um sentido substituto válido para combate afasta a desvantagem **por falta de visão** contra o alvo que ele permite perceber. Caso contrário, a frase vigente “Seus ataques: desvantagem” vence literalmente a nova ponte de visão às cegas. Isso não concede visão através de paredes, leitura fina ou ignora Selos explicitamente oculares.

**Contra-testes:** vidente contra Cego mantém vantagem; dois Cegos sem sentido substituto atacam com desvantagem; Vulto só resolve isso dentro de seu alcance e limites próprios. O efeito não deve retirar desvantagens de outras causas, como estar Impedido.

## 5. Radar de energia cria uma varredura automática de exploração

**Onde:** lote03:81–83. Todas as presenças não ocultas/suprimidas a 9 m são localizadas sem teste; paredes comuns não bloqueiam; uma busca abrange todas as presenças do setor.

**Cena reproduzível:** um corredor silencioso passa junto de várias salas. A cada trecho, o feiticeiro gasta uma Padrão para varrer 9 m. Maldições paradas que não usaram Esconder e objetos amaldiçoados sem regra especial de supressão têm seus espaços revelados através das paredes, sem rolagem ou gasto de PE. Fora do combate, se não há perigo imediato por tempo, o custo vira alguns segundos de marcha. Ferramentas e objetos também emanam energia, conforme M47-bencaos-e-lapidacao.md:104.

O procedimento transforma a descrição geral da perícia em um poder universal, preciso, coletivo, de atravessar paredes. O alcance de 9 m não tinha dono nas fontes. Trocar posição exata por direção aproximada diminui a precisão, mas conserva a capacidade nova de varrer indiscriminadamente salas e objetos ocultos.

**Não há demonstração de dominância total sobre os quatro benefícios citados:**
- **Presságio** ainda pode avisar sem ação e atende quem não tem Sentir Energia (M55:153; P16:227).
- **Rastro** informa a posição durante uma hora em todo o plano; a busca de 9 m exige ação e não acompanha sozinho (M40:780).
- **Vulto** substitui visão para combate no raio próprio; a busca energética não remove a desvantagem (M47:187).
- **Faro**, tanto o Legado quanto a Bênção, conserva usos de pistas/rastros que não sejam uma presença atual (M25:419; M47:167–173).

Porém, essas diferenças não validam o novo radar: ele ocupa gratuitamente uma função extensa de exploração, que não foi calibrada e não decorre de preservar aquelas compras. É incorreto escrever que “não mudou nada relevante” apenas porque nenhum nome ficou literalmente igual.

**Menor correção recomendada agora:** suspender o radar universal de 9 m e a localização automática por paredes nesta candidata. Conservar os efeitos que já localizam, sentidos especiais, leitura das perícias e suas distinções; registrar que o procedimento geral de detecção energética ainda precisa de decisão própria. Isso é uma pendência mecânica real, explicitamente assumida, e é mais honesto do que publicar uma capacidade não calibrada apenas para fechar o capítulo.

## O que não se demonstrou como problema

- **Apoios não renovam o limite acrobático em combate:** lote02:115 o renova no começo do turno, e diz que Correr não o renova. Parar e recomeçar, usar Passo Rápido ou Passo Guardado não recarrega o limite. Não encontrei loop de metros acrobáticos infinitos por apoiar o pé numa borda durante o mesmo ciclo.
- **Fora de combate**, a renovação por percurso apoiado permite progresso sucessivo. Com tempo livre e apoios reais, subir uma parede em etapas também é possível por escalada comum. Não é prova de exploração por si só; o Assassino conservar apoios especiais é parte da habilidade. Se há pressão de tempo, a candidata manda usar turnos.
- **Queda não é zerada por encostar:** lote02:88 exige um apoio que realmente sustentou o corpo. Uma passada/raspada durante queda não demonstra, sozinha, que o corpo tenha sido sustentado. A aterrissagem que interrompe uma queda precisa resolver o impacto antes de um novo salto; não há permissão escrita para apagar esse impacto.
- **Parkour não ganha ataque grátis:** os dois gatilhos continuam exigindo trajetória e movimento; a vítima como apoio usa movimento restante e tem limite próprio. Queda livre não satisfaz a descida apoiada de 4,5 m.
- **Soltura Preparada** conserva deslocamento de escalada próprio e suas mãos/requisitos atuais. O custo acrobático do Incursor não deve ser aplicado ao Batedor nem sua quota transplantada para escalada comum (I02-Vanguarda-Caminho-e-Trilhas.md:220–230).
- **Projeção Marcial** não duplica o dano de uma queda no alvo secundário: lote02:133 preserva somente o dano próprio da projeção na colisão. A projeção também não gera Fluidez por acerto (I06:425–447).
- **Mão Pesada** continua podendo empurrar em direção escolhida e usar precipício real; não ganha lançamento vertical gratuito com queda pelo simples uso da palavra “empurrar” (I01-Bastião-Caminho-e-Trilhas.md:116–118; lote02:100–102).
- **Busca múltipla/novo observador:** uma rolagem contra cada CD acessível resolve o exemplo com resultados 12 e 17 e busca 15: somente o primeiro é localizado. Observador sem acesso a sinais não localiza por uma estatística abstrata. O empate está consistente com a comparação publicada.
- **Cruzado/Mudar o Destino:** a diferença entre ataque adicional e correção da tentativa continua escrita. Na correção em preparação, verificar a revelação no primeiro disparo/percepção efetiva; o fato de Mudar o Destino contar como o mesmo ataque para certos gatilhos não deve apagar um sinal que um observador já percebeu.

## Validação executada e o que falta conferir nas correções

Executei enumeração exata das vinte faces e dos quatrocentos pares de d20 para a tabela de ocultação/manutenção. Conferi a perda de +2 de especialização e os custos de 9 m de terreno por caminhada versus seis saltos. Executei em leitura os estados antes/depois dos casos acima e comparei os custos das habilidades integradas. Não houve playtest humano, simulação integral de combate nem prova de equilíbrio global.

A próxima revisão deve usar casos que produzam resultados diferentes antes/depois, não testes que apenas confirmem o número recém-escrito:
1. Saltitar dentro de Terreno não consegue atravessar 9 m pagando só 9 m; saltar um obstáculo inteiro entre apoios regulares continua possível.
2. Disparar da lateral e retornar não conserva ocultação sem gastar uma permissão de Esconder; o primeiro ataque legitimamente oculto preserva seu benefício.
3. Especialista usa bônus completo tanto para o teste quanto para a oposição passiva.
4. Dois Cegos não ganham precisão sobre o caso de ambos na fumaça; Vulto funciona somente no raio permitido.
5. Uma varredura de energia não ganha alcance e precisão inexistentes na regra publicada; poderes específicos continuam com os efeitos que compraram.
6. Nova tentativa de Esconder substitui o resultado relevante, inclusive se piorar; não permite guardar indefinidamente o melhor d20 por repetir ações.

## Conferência dirigida após as correções candidatas

Ainda em 02/10/2026, reli os MD ativos: lote02 revisão 3, 137 linhas; lote03 revisão 2, 124 linhas. O autor corrigiu as candidatas, mantendo os donos publicados intactos. Os cinco achados materiais acima foram atendidos; esta conclusão não apaga o registro do problema anterior.

| Caso reexecutado | Resultado na revisão corrigida |
|---|---|
| Força 0, seis saltos de 1,5 m dentro de Terreno difícil | Consome 18 m. Com apenas 9 m, só percorre 4,5 m. Não equivale a caminhar em terreno regular (lote02:62). |
| Salto capaz de ultrapassar por inteiro um obstáculo no chão entre apoios regulares | Conserva a possibilidade de evitar esse obstáculo, sem isentar obstáculos que atinjam a trajetória pelo ar (lote02:62). |
| Andar 1,5 m e tentar gastar a mesma Ação de Movimento inteira para uma recarga | Não permitido. Movimento adicional de outra fonte não é gasto duas vezes por essa frase (lote02:12). |
| Arqueiro oculto aparece, dispara e volta atrás das caixas | O primeiro ataque pode receber o benefício; o ataque revela posição. Não há manutenção nem novo total gratuito (lote03:110–114). |
| Segundo ataque contra o mesmo observador sem Esconder novamente | Não conserva vantagem apenas por repetir a exposição pela lateral. Revelação foi resolvida antes dele. |
| Atacante invisível, posição revelada pelo primeiro ataque | Revelar posição não remove invisibilidade. Se ele enxerga a vítima e ela não o enxerga, a regra de atacante não visto continua pertinente; não foi confundida com ocultação (lote03:100, 116). |
| Assassino11 ataca, move-se para posição adequada e Esconde | Permissão própria continua sem ação, uma vez no turno e com teste normal; outros precisam de sua ação apropriada (I06:261–271; lote03:62, 124). |
| Especialista, Destreza6/maestria4/especialização2 | Furtividade +12 e CD posterior correspondentes; observador especialista também usa bônus completo (lote03:36, 46). |
| Dois combatentes na fumaça; depois ambos Cegos | Desvantagem antes e depois, salvo outra fonte independente. Cegueira mútua não passa a aumentar a precisão (lote03:100–106). |
| Cego com Vulto, alvo dentro e fora do raio | Dentro do raio, o sentido substituto pode afastar falta de visão conforme seus limites. Fora, não. Desvantagens de outras causas permanecem (lote03:29, 106). |
| Vidente atacando alvo Cego | Mantém vantagem. O ajuste não removeu a vulnerabilidade normal da condição (lote03:106). |
| Tentativa de escanear automaticamente várias salas e objetos por Sentir Energia9m | Não há mais permissão. O procedimento foi suspenso expressamente, preservando poderes particulares e marcando a pendência (lote03:79–87). |
| Busca15 contra ocultos12/17 e novo observador com CD igual ao resultado guardado | Busca localiza apenas o primeiro; empate do teste inicial continua favorecendo Esconder. A mudança da base não alterou esses procedimentos. |

**Precisão textual pequena, sem novo bloqueio mecânico:** lote03:58 diz que uma nova tentativa exige mudar a situação, enquanto 124 manda usar Esconder de novo atrás das caixas após atacar. Convém esclarecer que não se pode repetir um teste falho sem mudança relevante, mas que uma nova ação legítima depois de atacar segue a permissão comum de Esconder; não introduzir acidentalmente uma exigência de abandonar sempre aquela cobertura. A intenção está recuperável pelo conjunto.

Não encontrei nova quebra de custo ou de habilidade nesta revisão dirigida. A pendência de detecção energética é real e permanece explícita. As escolhas de alcance de salto, dano de queda e condição Cego continuam candidatas: consistência dos casos não equivale a equilíbrio integral ou teste humano concluído.

# Lote 03 — auditoria de percepção, furtividade e visão

Leitura somente de fontes locais vigentes, em 02/10/2026. Não alterei fontes, não usei Git e não fiz teste humano. Este parecer sustenta uma minuta; não é regra publicada.

Raiz de todas as referências: `/media/mizuki/HD Externo II/Claude/Claude 2/`.

Abreviações: **M** = `sistema/05-material/livro/manual/`; **P** = `sistema/03-mecanica/`; **I** = `caminhos/05-Edicao-Integrada/`. Os números após os nomes são linhas, na leitura desta auditoria. Caminhos integrados prevalecem sobre as versões antigas. O catálogo atual de Invocações está em `invocacoes/05-Edicao-Integrada/60-invocacoes.md` e M60; a peça P15 de Invocações é histórica.

## Resultado

Já existem as perícias e ações necessárias, mas não existe um procedimento geral completo para ficar oculto, permanecer oculto, descobrir uma criatura e lidar com alguém que não se enxerga. A menor adaptação é completar **Esconder** e ampliar explicitamente **Vasculhar**. Não é preciso criar uma quarta ação de investigação. A extensão deve ser identificada como regra candidata: resolve lacunas e uma divergência atual, não é apenas revisão textual.

Os principais compromissos a preservar são: esconder como Bônus do Incursor; esconder grátis após movimento do Assassino 11; oportunidade verificada na declaração do ataque; alvos percebidos do Malabarista; alcance e custos comprados de Sem Ver, Silencioso e sentidos especiais; e a decisão registrada de que armas de fogo revelam enquanto as outras permitem teste.

## O que está escrito hoje

| Tema | Fonte e localização | Estado e consequência |
|---|---|---|
| Teste de perícia | M12-pericias-e-oficios.md:29, 56, 70–71 | d20 + atributo; maestria quando treinado. Furtividade é Destreza; Percepção e Sentir Energia são Essência. |
| Furtividade | M12:104; P07-pericias-e-oficios.md:87 | Move-se sem ser visto nem ouvido. Não define CD oposta, condições para iniciar, duração, revelação nem benefícios de ocultação. |
| Percepção | M12:138; P07:104 | Som, cheiro, movimento e sinais mundanos. Não é exclusivamente visão. |
| Sentir Energia | M12:136, 154–160; P07:103, 117 | Pode perceber o feiticeiro escondido e ler o fluxo de energia. Não localizei raio, procedimento de localizar, grau de precisão ou passagem por obstáculos como regra geral. |
| Escolha de treino | P07:195 | Sentir Energia deliberadamente não é fixa de nenhum Caminho. Não transformar a perícia em radar automático que ignore treino. |
| Esconder | M11-o-turno.md:71 | Ação Padrão, teste de Furtividade. O restante do procedimento não está ali. |
| Vasculhar | M11:75 | Ação Padrão, Percepção ou Investigação sobre coisa/criatura ao alcance. A extensão de procurar uma criatura distante precisa ser escrita. |
| Estudar | M11:76; P03-economia-de-acao-e-iniciativa.md:237 | Sentir Energia, Ocultismo, Medicina ou História sobre criatura/objeto **que você enxerga**. Análise de algo já acessível, não solução pronta para descobrir um alvo que não se vê. |
| Contradição Vasculhar/Estudar | M11:106 | A prosa restringe Vasculhar à inspeção manual/Investigação e chama Estudar de olhar distante/Percepção, divergindo das perícias da tabela. A minuta precisa corrigir a distinção, não tentar cumprir simultaneamente as duas versões. |
| Ler o Ambiente | M11:112–118 | Bônus, 1/cena, informação útil do lugar. **Nunca informa sobre criatura.** Não deve virar busca barata de inimigo oculto. |
| CD contra algo com nível | P04-pericias-e-testes.md:65–79 | Precedente de base 8 + atributo + maestria + degrau. Não localizei uma Atenção passiva ou CD de Percepção já definida. Usar `8 + bônus de Percepção` é uma extensão compatível com o molde, não transcrição da regra existente. |
| Furtividade em grupo | P04:139 | Metade do grupo precisa passar. Completar o procedimento individual não deve apagar silenciosamente essa regra fora do combate. |
| Exemplo de furtividade | M10-como-jogar.md:34, 66 | CD 12 contra guardas e exemplo narrativo de falha que gera investigação. Não constituem CD universal nem regra de oculto. |
| Cego | M15-dano-e-condicoes.md:216–224 | Falha automática em testes que precisem de vista; desvantagem em ataques; vantagem contra ele. É a referência existente para combate sem visão. |
| Invisível | M15:276–287 | Declarado benefício, não condição comprável para aplicar num alvo. Não localizei um bloco geral de efeitos. Não importar bônus de iniciativa ou imunidade a detecção como se já existissem. |
| Luz, escuridão e obscurecimento | M40-fundamento.md:658 | Terreno pode obscurecer uma área por 1 rodada, mas não há procedimento geral de obscurecimento/iluminação localizado. É uma lacuna real do efeito atual. |
| Cobertura | M15:306–323 | Parcial +2 Defesa/TR Físico; Boa +5; Total impede escolha como alvo. Direção importa. Efeito de área pode alcançar atrás quando dispensa linha até o alvo. Esconder a visão não equivale a uma parede que detém um ataque. |
| Oportunidade | M11:120–128; P04:145 em diante | Reação por sair do alcance corpo a corpo. Não localizei requisito geral de enxergar. Importá-lo seria uma mudança com efeito em Reflexo. |
| Bloquear | M10:153–157, 181–187 | Gratuito, sem Reação, contra ataques; Incapacitado é a única condição que o impede. Ataque oculto/invisível não pode passar a ignorar Bloquear sem uma nova decisão explícita. |

**Atenção:** a palavra aparece em concentração e em descrições comuns, sem formar recurso ou estatística própria. Não é necessário criar um novo medidor.

## Decisão já registrada que a nova peça deve incorporar

P14-equipamento.md:503–518 registra a discussão de `Silenciosa`: o usuário queria que certas armas permitissem novo teste com penalidade ao atacar furtivamente. A propriedade foi abandonada, preservando a solução pela categoria da arma. Em **P14:1825, §8 item 19**, a decisão adiada está explícita: **Arma de Fogo revela; o resto pede teste**, quando a regra de furtividade existir.

Portanto, seguir D&D como referência não autoriza aplicar automaticamente “todo ataque revela”. A distinção entre armas já tem compromisso local. Desvantagem no teste de manutenção é uma forma candidata de implementar a penalidade; ainda precisa ser registrada como a definição nova do procedimento.

O texto deve deixar claro que o teste gratuito apenas **mantém** uma ocultação que existia contra aquele observador. Não concede Esconder pela primeira vez nem recupera ocultação já perdida por exposição. Caso contrário, apaga parte da entrega do Assassino 11.

## Interações que não podem ser perdidas

| Regra vigente | Fonte | Compatibilidade necessária |
|---|---|---|
| Esconder pela Bônus | I06-Incursor-Caminho-e-Trilhas.md:40–42 | O procedimento comum deve admitir a troca de ação; não exigir uma ação adicional para obter a posição de oculto. |
| Alvo Estudado / Estudar a Guarda | I06:149–170 | Escolha exige **ver** a criatura a 18 m. Apenas localizar energia ou ouvir atrás de uma parede não satisfaz esse requisito. Não há exigência escrita de manter visão continuamente para conservar um Alvo Estudado já escolhido. |
| Oportunidade de abate | I06:153–160 | Oculto é **em relação à vítima**, verificado na declaração. Também existem outros gatilhos; não transformar ocultação em obrigação para todo Golpe Cirúrgico. |
| Desaparecer no Percurso | I06:261–271 | Depois de atacar, termina um movimento em posição legal e Esconde sem ação, 1/turno. O ataque não precisa acertar. A regra comum de manutenção pós-ataque não deve conceder essa aquisição de ocultação a todos. |
| Sentença Final | I06:291–305 | Deve estar oculto do Alvo Estudado **ao declarar**. Revelar-se depois de resolver o ataque não invalida retroativamente o golpe e seus benefícios. |
| Reflexo e Inverter a Pressão | I06:73–76, 98, 106 | Ataque de oportunidade corpo a corpo; sem requisito escrito de visão. O mínimo compatível é exigir que seja possível escolher/localizar aquele alvo e aplicar as consequências comuns de não o enxergar. Não adicionar visão obrigatória nem dar localização automática porque o inimigo errou. |
| Ricochete | I06:528–538 | Exige alvo percebido e percurso livre nos dois trechos. Pode contornar cobertura mesmo sem linha direta. Percepção não passa a ser sinônimo obrigatório de visão; detectar posição tampouco remove obstáculos físicos. |
| Lançamento Cruzado | I06:548–552 | Continuação é **outro ataque** contra outra criatura percebida. Consequências da ocultação do primeiro ataque precisam estar resolvidas antes de executar o segundo. |
| Mudar o Destino | I06:558–564 | Correção é parte do **mesmo ataque** para gatilhos que contam ataques, mas reavalia vantagem/desvantagem/cobertura contra a nova vítima. Cuidado para não cobrar um segundo teste de manutenção simplesmente por existir outra rolagem. |
| Trajetória Perfeita | I06:614–627 | Declara alvos percebidos e caminho; cada alvo sofre ataque separado. Não revela alvos. Tem vantagem própria; perda de ocultação não elimina essa fonte de vantagem. Ignorar Bloquear é benefício desta execução, não da furtividade genérica. |
| Guia: Leitura de Equipe | M35-caminhos-e-trilhas.md:833 | Usa os nomes Estudar, Vasculhar e Ler o Ambiente. Ampliar Vasculhar preserva o gatilho; inventar uma quarta ação sem remissão deixa esse benefício para trás. |

### Sentidos especiais e poderes

- **Sem Ver**, M40:606, custa Melhoria Pesada para conjurar contra alvo fora da linha de visão, sabendo sua posição. Localizar e enxergar precisam continuar distintos. **Rastro**, M40:780, fornece posição por 1 hora no mesmo plano; não diz conceder olhos extras. O degrau de alcance “o que você enxergar” exige olho nu (M40:526).
- **Silencioso**, M40:750, não revela posição pelo uso e remove sinais/gesto/palavra; Selo de condição, como enxergar o alvo, permanece. Uma regra de revelação por conjurar precisa preservar a exceção. Ela não declara invisibilidade do corpo exposto.
- **Terreno**, M40:658, obscurece área com Melhoria Leve. Definir obscurecimento é necessário, mas não converter o efeito em aplicar permanentemente a condição Cego em todos. É obstrução situacional da visão, com entrada/saída e geometria.
- **Faro (Legado)**, M25-origens.md:419 / P13-legados.md:896, permite Sentir Energia no lugar de Investigação **1/cena quando se procura maldição**. Se a extensão de Vasculhar permitir a todos investigar qualquer rastro com Sentir Energia, esvazia essa compra. Separar detecção de **presença atual** de investigação de pistas/rastros preserva o Legado.
- **Antena**, M25:653, rerrola Sentir Energia 1/cena; **Sentido Treinado**, M25:687–688, substitui por Percepção 1/cena, pela perturbação física que a energia causa. Não converter a substituição em poder básico irrestrito.
- O ramo **sem energia** não pode ter Sentir Energia (M12:89; M25:618). Equipamento amaldiçoado continua emitindo energia mesmo carregado por quem não a possui (M47-bencaos-e-lapidacao.md:94, 104). **Máscara**, M25:207–208, muda o que a leitura encontra, não apaga universalmente a presença.
- **Faro (Bênção)**, M47:167–173, acompanha vestígios e obtém informação superficial da técnica ao tocá-los; não identifica o autor nem localiza automaticamente onde ele está agora. **Sem Pegada**, M47:175–181, apaga vestígios físicos, mas não é bônus de Furtividade e não apaga quem viu passar.
- **Vulto**, M47:185–189, é visão às cegas baseada em som/movimento, com raio escrito de 1,5 m × metade da Lapidação. Não usar Sentir Energia básico como substituto universal de Vulto. A interação com escuridão/Cego pode ser explicitada como reconhecimento pelo sentido especial, sem inventar leitura fina ou atravessar paredes.
- **Presságio**, M55-ferramenta-amaldicoada.md:153, avisa que há maldição perto; não publica coordenada ou identidade. A informação de presença não basta sozinha para ricochetear contra um alvo.
- As invocações têm sentidos próprios (M60-invocacoes.md:79); Intenção e Comunicação não fornecem compartilhamento automático de sentidos (M60:628–669). Uma informação comunicada não concede visão direta para Alvo Estudado ou para dispensar Sem Ver.

## Menor adaptação recomendada para a minuta em preparação

Isto é recomendação de procedimento, não texto de regra vigente.

1. **Completar Esconder sem outra ação.** Condição ficcional de poder deixar de ser percebido; teste de Furtividade; oposição ao observador apto a detectar; ocultação relativa a cada observador. Um resultado pode ser comparado com vários observadores, sem rolar de novo a cada um.
2. **Usar base 8 de forma explícita.** `8 + bônus de Percepção` é coerente com a régua local, mas novo. Bônus significa Essência + maestria se treinado. O mesmo resultado guardado de Furtividade pode servir de CD para uma busca ativa. Definir desempate e que não há teste do observador na primeira comparação. Não há necessidade de nomear “Atenção” como nova característica.
3. **Ampliar Vasculhar por modalidade.** Percepção procura algo dentro do alcance dos sentidos; Investigação inspeciona objetos/pistas acessíveis; Sentir Energia pode buscar uma presença energética atual. Estudar continua analisando algo visto; Ler o Ambiente permanece sobre lugar, nunca criatura. Isso pede ajuste declarado na tabela e na prosa contraditória de M11.
4. **Sentir Energia precisa de limite novo declarado.** Não foi localizado alcance geral com dono. Um raio candidato em múltiplo de 1,5 m pode fechar a minuta, mas não deve ser apresentado como restauração de regra. Definir se o sucesso dá só presença/direção ou posição atual. O mínimo funcional para combate é posição atual dentro do limite e em situação que permita detectar; isso não concede visão, passagem de ataques por paredes, identificação completa ou rastreamento indefinido. Não incluir investigação de vestígios como substituição geral de Investigação: Faro já ocupa essa exceção.
5. **Separar três perguntas em linguagem comum:** vejo a criatura? Sei em que espaço ela está? Só percebi que existe algo por perto? Não precisam virar três condições rastreadas. Essa distinção resolve Sem Ver, Alvo Estudado, Malabarista e Presságio.
6. **Manutenção após ataque é restrita e imediata.** Arma de Fogo revela; demais armas podem testar com a penalidade escolhida se o atacante já estava oculto daquele observador e continua em posição compatível. Resolver depois daquele ataque, antes de outro. Se já ficou exposto, não existe manutenção: precisa Esconder novamente pela ação ou exceção apropriada. Consequências de visão e ruído evidentes não são apagadas por resultado alto no dado.
7. **Não importar outros nerfs junto.** Escuridão e invisibilidade não proíbem Bloquear. Oportunidade/Reflexo não ganham exigência nova de enxergar inadvertidamente. O procedimento novo de alvo não visto deve funcionar com posição conhecida sem conceder identificação/localização automática.

A probabilidade e a duração são decisões de design da minuta, não conclusões que a auditoria possa tratar como aprovadas. Não há necessidade de abrir regras de surpresa/iniciativa, inventar novos sentidos ou refazer classes para resolver este lote.

## Casos obrigatórios para conferir na minuta

- Incursor atrás de uma esquina usa Bônus para Esconder; o observador A pode ouvi-lo, B não. Um teste, conclusões por observador; não “oculto de todo o combate”.
- Assassino já oculto declara Sentença Final, acerta, resolve dano e então perde ocultação. O ataque mantém o gatilho que possuía na declaração.
- Assassino exposto ataca, vai para trás da parede e usa Desaparecer. Um personagem comum fazendo o mesmo precisa Esconder com sua ação; manutenção gratuita não deve funcionar para ele.
- Malabarista escondido faz primeiro ataque e Lançamento Cruzado. Reavaliar se o segundo alvo o percebe; não distribuir automaticamente a vantagem de ocultação a toda a ação.
- Mudar o Destino redireciona a tentativa contra outra criatura. Reavalia condições contra ela sem transformar a correção em dois ataques para todos os gatilhos.
- Oponente invisível localizado erra um golpe contra Incursor que já tinha Fluidez. Reflexo continua possível se a regra comum permitir atacar sua posição, com as penalidades cabíveis; o erro sozinho não informa coordenadas de um agressor ainda desconhecido.
- Feiticeiro localiza energia atrás da parede. Isso pode dar posição, mas não preenche “consiga ver” de Alvo Estudado. Um projétil não atravessa a parede por ter sido localizado; Ricochete só funciona se houver caminho físico e os demais requisitos.
- Presságio apita; o jogador ainda não tem posição para selecionar um alvo. Rastro dá posição; Sem Ver continua cumprindo sua função na conjuração.
- Restrito sem energia carregando ferramenta: corpo e equipamento não devem ser confundidos como fontes. Ler a ferramenta não necessariamente revela todos os dados do portador.
- Faro de Origem continua útil ao investigar onde uma maldição esteve/para onde foi; a detecção básica de presença atual não substitui sua permissão 1/cena.

## Divergência adjacente para registrar, sem expandir o lote

**Oculta (arma) não é oculto (criatura).** M50-equipamento.md:130 diz que a propriedade esconde a arma no corpo **sem teste**; M07-glossario.md:223 diz **com Prestidigitação**; P14 contém a versão antiga de permitir teste (por exemplo, linhas 666 e 697–699). Há conflito de fonte atual. Não usar a propriedade como fundamento do procedimento de esconder pessoas. Registrar correção de sincronização com decisão do dono, sem atrelar à criação do lote de percepção.

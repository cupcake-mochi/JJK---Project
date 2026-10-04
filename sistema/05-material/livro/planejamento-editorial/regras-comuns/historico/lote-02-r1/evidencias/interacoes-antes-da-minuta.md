# Lote 2 — compatibilidades recomendadas para movimento

Parecer de design, 02/10/2026, sobre a v0.331. **As respostas abaixo são propostas para decisão; não são regras já aprovadas nem texto publicado.** Leitura focada das seis capacidades pedidas, confrontada com movimento, condições e apoio. Nenhuma fonte foi editada.

## 1. Menor regra geral recomendada para deslocamento forçado

Recomendo tratar separadamente deslocamento voluntário, deslocamento imposto e queda. Para empurrões/lançamentos comuns, adotar este conjunto mínimo:

- O deslocamento imposto não gasta o movimento da vítima e **não provoca ataques de oportunidade**. Uma caminhada que ela faz por escolha, mesmo concedida por uma resposta ao ataque, continua voluntária e segue suas próprias exceções.
- O trajeto não atravessa obstáculo sólido. Encontrar uma parede encerra a distância que não puder ser percorrida; **não concede dano de colisão por si só**. Habilidades que já têm dano de colisão o conservam.
- **Não se pode escolher como destino um ponto no ar acima do apoio inicial da vítima.** Um destino mais alto precisa oferecer apoio real, salvo efeito que autorize expressamente erguer, suspender ou lançar para cima. Um arco narrativo de arremesso não fornece altura adicional para calcular dano.
- É possível deslocar alguém além de uma beirada. A falta de apoio então provoca queda; o precipício continua sendo um perigo do cenário. Resolver essa queda antes de passar à próxima ação ou a uma resposta que só funciona depois do efeito.

Isso impede converter todo acerto de Mão Pesada em “subir 4,5 m e cair”, sem retirar o uso de beiradas ou a possibilidade de lançar alguém sobre uma plataforma existente. Evita também dar dano gratuito ao empurrar contra uma parede. **O dano do golpe/projeção continua existindo; o dano de uma queda real para um nível inferior pode somar-se**, conforme a regra ambiental que for escolhida. Essa soma terá efeito de equilíbrio e deve aparecer nos casos de teste.

Não recomendo resolver o problema declarando “qualquer espaço livre precisa ser apoiado”: isso proibiria o precipício por outra porta. “Livre” significa desocupado e sem bloqueio físico; “apoiado” é uma exigência adicional, presente onde a habilidade a declara.

**Mudança reconhecida:** Mão Pesada diz “na direção escolhida”; Projeção diz “espaço livre [...] alcançável pelo lançamento”. Não há veto vertical expresso nesses textos. A regra acima restringe uma leitura hoje possível e precisa ser apresentada ao autor como compatibilização mecânica nova. Não chamá-la de mera revisão textual. Se aprovado, os textos específicos devem remeter à regra de trajetória para não conservar uma promessa mais ampla.

## 2. O que cada capacidade conserva

| Capacidade e fonte integrada | Compatibilidade recomendada |
|---|---|
| **Mão Pesada**, Bastião, linhas 116–118 | Mantém até 4,5 m após acerto, uma vez por alvo/rodada, sem acrescentar TR ao empurrão. O TR de Vigor para Derrubado/Agarrado é outra parte da habilidade. Se empurrar para fora do alcance, não conserva o agarrão. Terreno/beirada não dá outra tentativa de resistir ao próprio empurrão por omissão; uma reação para agarrar borda é uma resposta ambiental distinta. |
| **Cortar a Fuga**, Incursor/Assassino, linhas 204–212 | Mantém um TR Físico, Derrubado e empurrão opcional de até 3 m para longe. O movimento forçado não consome a distância da vítima; estar Derrubado não diminui esses 3 m. A ordem do ataque e seus efeitos vem antes de usar a vítima como apoio. Se a vítima já não está alcançável, não se usa sua posição anterior para o salto. |
| **Projeção Marcial**, Incursor/Pugilista, linhas 425–449 | Mantém o destino livre a até 6 m, trajetória desobstruída, TR, custo de 3 PE, dano desarmado e Derrubado. Pode cruzar um vão por trajetória de lançamento válida ou terminar além de beirada, mas não cria altura gratuita no ar. Dano ambiental da queda não entra em “mesma quantidade de dano da projeção” sofrida pela segunda criatura: essa cópia refere-se ao dano próprio da habilidade. Não copiar a queda de uma vítima para outra que não caiu. |
| **Recuperar a Base**, Incursor/Pugilista, linhas 366–374 | O retorno é movimento voluntário adicional, não desfaz o deslocamento imposto nem o dano anterior. O gatilho continua exigindo um único empurrão suficiente; não somar vários empurrões, e não adicionar metros de queda livre à distância empurrada. Proponho conservar o escopo literal “empurrado”: Projeção é lançamento, portanto pode ativar a opção contra Derrubado, mas não recebe automaticamente o retorno reservado a empurrão. Ampliar para todo lançamento exigiria alteração expressa da habilidade. |
| **Apoios de infiltração**, Incursor/Assassino, linhas 228–234 | Conserva terminar Movimento Acrobático pendurado/em apoios que sustentem o corpo, com pelo menos uma mão ocupada, e atacar durante o percurso. Não fornece aderência a parede lisa, uma mão adicional ou sucesso automático. |
| **Passo Guardado**, Incursor, linhas 100–106 | Conserva metade do deslocamento como movimento adicional, uma vez por ciclo, fora do turno, exigindo Fluidez e capacidade de mover-se após resolver o ataque/TR. Não exige reação nem gasta Fluidez. Só evita oportunidade do responsável; outras criaturas mantêm suas respostas contra esse movimento voluntário. |

Os arquivos citados são `caminhos/05-Edicao-Integrada/01-Bastião-Caminho-e-Trilhas.md` e `06-Incursor-Caminho-e-Trilhas.md`.

## 3. Borda comum e benefício do Assassino

**Recomendação:** qualquer personagem pode escolher uma borda alcançável como destino de uma escalada ou de um salto, em vez de precisar chegar com os pés. Quando houver risco, resolver a tentativa de alcançar/segurar usando o procedimento comum de Atletismo. Ficar pendurado é uma posição física sustentada por apoio e mãos disponíveis; não é a condição Agarrado por criatura. Subir da borda usa a regra de escalada e o movimento correspondente.

Isso não deve conceder Movimento Acrobático a todos. A especialidade do Assassino continua sendo **usar essa posição como término válido de seu percurso acrobático**, trocar Atletismo por Acrobacia nos saltos/apoios abrangidos pelo Parkour e atacar durante o percurso. Não é necessário tornar uma borda fisicamente impossível para outras pessoas a fim de proteger essa identidade. Também não proponho um número novo de mãos para toda escalada comum; a exigência expressa de ao menos uma mão do Assassino permanece.

**Para perda inesperada de apoio**, recomendo uma janela própria: gastar a Reação para tentar alcançar/segurar uma borda efetivamente ao alcance, com teste e risco declarados pelo mestre. Não há borda, apoio ou mão disponível, não há tentativa. A Reação pode já ter sido gasta em outra defesa.

Não repetir o teste do mesmo risco: se um salto voluntário já foi rolado para alcançar aquela borda, seu resultado determina a posição final — não concede automaticamente uma segunda rolagem reativa. A oportunidade de terminar pendurado em vez de cair deve entrar no resultado anunciado daquela tentativa. Essa resposta de emergência é uma concessão geral nova, deve ser marcada como proposta e reduz a letalidade de empurrões junto a bordas; não adiciona outro TR à manobra em si.

## 4. Ordem para cair e depois recuperar-se

Recomendo fixar a sequência:

1. Resolver o ataque/TR original e o deslocamento imposto, respeitando a ordem da habilidade.
2. Se perder apoio, abrir a resposta ambiental cabível para a borda; se não interromper a queda, resolver queda, impacto, dano e posição/condição finais.
3. Só então executar respostas de **“depois de resolver”**, se seus requisitos ainda forem atendidos.

Assim, Recuperar a Base e Passo Guardado não viram passos no ar que anulam retrospectivamente a queda. Um personagem que esteja capaz de mover-se no fundo pode usar o movimento concedido, mas precisa de um percurso real; não volta automaticamente à plataforma. Se terminar Derrubado, o movimento segue as regras dessa condição, a menos que ele primeiro consiga levantá-la. Recuperar a Base pode levantar depois do efeito, pagando Fluidez; isso não restitui Vida perdida.

Há uma escolha real de recursos: se gastar sua única Fluidez para levantar, pode deixar de atender à exigência “enquanto tiver Fluidez” de Passo Guardado. Não oferecer os dois como se a Fluidez permanecesse automaticamente disponível. Uma recuperação comum/ambiental não gera Fluidez por si só.

## 5. Quota acrobática dentro e fora do turno

Minha recomendação inicial é **uma distância acrobática compartilhada por ciclo, renovada no começo do turno do Incursor**, usando o mesmo marco de renovação já empregado por Fluidez e Passo Guardado. Todos os movimentos voluntários acrobáticos nesse intervalo consomem essa distância, inclusive Passo Rápido/Guardado e retorno de Recuperar a Base. Correr e dividir o percurso não renovam o limite. Movimento imposto e queda não contam como um percurso acrobático escolhido.

É a opção mais simples de conferir sem criar uma franquia por ação. **Seu custo de design precisa ser reconhecido:** gastar a quota inteira na parede durante o próprio turno pode deixar Passo Guardado disponível apenas por um percurso comum fora do turno. A habilidade ainda concede movimento, mas não uma nova quota de parede/líquido. Isso é uma interpretação proposta do limite compartilhado, não uma restrição já explicitamente aprovada.

Se a intenção autoral for assegurar uma segunda travessia acrobática reativa, a alternativa coerente é renovar por turno de cada criatura, com os custos/limites das respostas impedindo movimentos gratuitos. Não recomendo renovar por trecho, por Correr ou por cada concessão de movimento: isso faz a mesma quota desaparecer quando o jogador divide a descrição.

Para a proposta inicial, escolheria o ciclo e mostraria expressamente o caso “parede 6 m no próprio turno; Passo Guardado depois”. Só alterar essa recomendação se o autor preferir o benefício reativo adicional. Um Passo à Frente começa um turno real, portanto renova o ciclo; por substituir o turno habitual da rodada, não recebe uma segunda renovação naquela posição.

## Casos de aceitação essenciais

- Mão Pesada no chão plano: reposiciona; não fabrica queda de 4,5 m nem dano de parede.
- O mesmo golpe numa beirada: pode gerar queda do desnível real; agarrar borda disputa a Reação.
- Projeção contra uma segunda criatura junto do precipício: cada uma sofre só sua própria queda; a colisão copia apenas o dano da habilidade.
- Pugilista empurrado 3 m e caindo mais 9 m: não soma 12 m para ativar retorno; se cair Derrubado, pode usar a opção de levantar após resolver o efeito, caso tenha recursos e capacidade.
- Assassino falha ao alcançar a borda: a consequência usa o teste já declarado, sem uma rerrolagem automática do mesmo risco.
- Incursor consome 6 m acrobáticos e responde fora do turno: o ciclo proposto não renova a quota, mas preserva os metros adicionais utilizáveis por um percurso permitido.

O conjunto fecha as interpretações de trajetória, borda e ordem de respostas sem escolher ainda dano por altura ou metros de salto. As limitações novas de verticalidade, resposta de borda e quota devem ser aprovadas como decisões de design e só depois refletidas no livro e nas Trilhas.

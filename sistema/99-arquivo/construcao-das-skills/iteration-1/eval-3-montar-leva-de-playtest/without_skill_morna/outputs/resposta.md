# Como organizar a leva de teste da v1 do combate

Cinco a sete mestres, mesas em dias diferentes, personagem que atravessa todo mundo: esse conjunto é o que decide se essa leva de teste vira dado útil ou vira ruído. Sem organizar em torno disso, dá pra terminar a rodada sem saber se um problema é da regra ou de quem estava mestrando naquele dia — e pior, um personagem de alguém pode sair machucado, ou morto, por causa de um bug de v1, não de uma escolha de jogo.

Cinco frentes, nessa ordem.

## 1. Proteja o personagem persistente da própria versão

V1 vai ter buraco — é o ponto de ser v1. O problema é que na Guilda um buraco de regra não fica isolado numa mesa: ele viaja com o personagem pra mesa do mestre seguinte, na semana seguinte. Decida isso antes de marcar a primeira sessão:

- **Fichas de teste padronizadas** — três ou quatro fichas-tipo, simples e genéricas de propósito (o molde de técnica ainda nem está fechado, então não é hora de testar em cima de poder inventado por jogador). Usa elas nos combates de teste em vez do personagem de verdade. Tira o risco de continuidade e, de brinde, dá a mesma entrada em mãos de mestres diferentes — o que importa pro item 2.
- **Personagens reais, com rede de segurança** — se preferir testar com o elenco de verdade, mais orgânico e mais engajado, combine antes que durante a janela de teste nenhuma morte é permanente por causa da v1. Pior resultado possível: personagem fora de cena. "Misto letal/não-letal por mesa" volta a valer assim que a versão fechar.

Não precisa escolher só uma linha — dá pra deixar cada mestre optar, contanto que a regra de segurança da segunda opção seja combinada por todo mundo, não decidida mesa a mesa.

## 2. Isole o que está sendo testado

O que entra na v1 é o motor: iniciativa, resolução, gasto de energia amaldiçoada, dano e desgaste, morte. O catálogo de técnica não tem molde fechado ainda, então misturar as duas coisas confunde o dado — você não vai saber se o combate travou por causa do motor ou por causa do poder que um jogador inventou pra própria ficha.

Prepare duas ou três cenas fixas: mesmo inimigo, mesmo terreno, um gatilho de dúvida embutido em cada uma (por exemplo: jogador tenta algo que a ficha não previu; personagem chega a zero de energia no meio da luta). Toda mesa de teste roda a mesma cena, sem improvisar em cima. Parece tirar a graça, mas é o único jeito de responder à pergunta que decide se o sistema serve pra Guilda: dois mestres que nunca se falaram, resolvendo a mesma cena, chegam no mesmo lugar? Se sim, a regra é arbitrável por estranho — que é literalmente o critério de sucesso que já está escrito no pitch. Se não, você achou o buraco antes dos jogadores acharem por você.

## 3. Encaixe o ciclo real na semana real

O formato — três rodadas com conserto entre elas, num bloco temático de duas semanas focado só em combate — já está decidido. Falta encaixar isso na rotação real: 2 a 3 mesas por semana, dias diferentes, nem todo mestre roda toda semana.

Antes de abrir pra guilda inteira, rode a cena de teste numa mesa reduzida — você e um co-mestre de confiança, ou até só você. Não custa nada e pega o buraco óbvio antes de gastar a paciência dos outros seis mestres numa versão que travava no primeiro ataque.

Depois disso, use a rotação normal como as próprias rodadas, em vez de tentar juntar todo mundo numa semana especial:

| Rodada | Quando | Quem prioriza | Depois |
|---|---|---|---|
| 1 | próxima semana de mesas | os 2-3 mestres que já rodariam essa semana | conserto do que quebrou feio |
| 2 | semana seguinte | quem ainda não testou | conserto de novo |
| 3 | terceira semana | quem sobrou, mais repescagem de quem quiser rodar de novo | fecha a versão |

O trabalho de verdade aqui é escalar quem testa em cada rodada — se sobrar sempre pros mesmos dois mestres mais animados, você mede se o sistema funciona nas mãos deles, não se funciona pra Guilda inteira. Se numa semana ninguém tiver combate natural na campanha, não pule a rodada: peça a um mestre disponível pra encaixar um encontro avulso, fora da história principal, só pra não perder a janela.

## 4. Alinhe os mestres antes da primeira sessão valer

Cinco mestres lendo o mesmo texto de regra pela primeira vez, cada um rodando ao vivo sem chance de comparar nota antes — isso mede leitura de texto, não mede a regra. Antes da rodada 1:

- Manda o documento da v1 com folga, não na véspera da primeira mesa.
- Reserva 20 minutos de conversa (call ou thread escrita, o que for mais fácil de sincronizar com sete pessoas) só pra tirar dúvida antes de qualquer mesa rodar. Toda dúvida que aparecer aqui já é achado — se um mestre perguntou, o texto escondeu.
- Combina a regra do improviso: na dúvida durante a mesa, resolve do jeito que parecer mais justo, e anota o que foi decidido e por quê. Não existe houserule silenciosa nessa janela — ela vira dado perdido, não uma solução esperta.

## 5. Centralize o retorno no mesmo dia, feche por padrão

Com mesas em dias diferentes, retorno que não é capturado na hora evapora até o fim de semana. Dois fluxos, os dois indo pro mesmo lugar — um canal ou uma planilha única, não um documento por mestre:

- O mestre registra logo depois da sessão, ainda no mesmo dia. Uso o modelo em anexo (`modelo-registro-de-sessao-teste.md`) pra isso não virar redação livre nem depender de lembrar detalhe três dias depois.
- Os jogadores respondem um formulário curto e anônimo, também no mesmo dia. Conversa ao vivo pós-mesa é boa pra medir clima, ruim pra crítica dura — o anônimo pega o que ninguém fala pro mestre na cara.

No fim de cada rodada, olha padrão, não caso isolado: um jogador achando o combate longo é comentário; três mesas diferentes achando o mesmo é achado. Isso vira a próxima entrada do CHANGELOG, do jeito que o resto do projeto já é registrado — o que mudou, e por quê.

---

Se o achado novo despencar depois da rodada 3, fecha a v1 e sobe pra v1.1 — é o sinal de que uma quarta rodada renderia pouco. Se ainda estiver vindo achado grosso, roda mais uma leva de três antes de declarar o combate estável. Nenhuma das duas é fracasso; é o ciclo funcionando como foi desenhado.

Anexo nesta mesma pasta: `modelo-registro-de-sessao-teste.md`, o formulário que cada mestre preenche depois de rodar uma cena de teste.

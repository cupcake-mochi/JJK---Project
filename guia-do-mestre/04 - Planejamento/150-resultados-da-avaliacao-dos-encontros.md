# Resultados da avaliação dos encontros

Registro 150, 02/11/2026. Este registro executa o [plano 149](<149-plano-de-avaliacao-dos-encontros.md>) por simulação, aplica ao livro as três orientações aprovadas pelo autor e registra a decisão sobre PE de inimigo.

Nenhum número de regra mudou. As fontes do capítulo 6 foram alteradas, mas o PDF e o HTML ainda são os do registro 147.

## Como foi medido

Tudo está em `apoio-encontros-149`. Antes dos casos, três portões foram conferidos:
- `c01_portao.py` reproduz por conta exata o caso 74;
- `c01b_reproduz_piloto.py` reproduz os números do registro 15 com as mesmas sementes;
- `c01c_motor_estendido_igual.py` mostra o motor estendido igual ao do piloto em 32.000 combates.

O motor do piloto foi copiado sem mudança para `motor/`, e `cmp` confirma que é idêntico ao de `apoio-piloto`.

`r53-para-r60.py` compara os fatos numéricos das duas revisões. Ele lê a R60 na `main`, e não roda nesta branch. Nenhum fato da R53 sumiu. A única mudança de regra, a Reação fora do turno, não afeta os números do guia.

Cada linha usa 4.000 lutas, com margem de Wilson de 95%. A saída completa está em `casos-saida.txt`, `casos-resultado.json`, `c08-saida.txt` e `c09-saida.txt`.

## Resultados

**C02 a C12, nível 2, contra o Amontoado** (`casos.py`):

- **Estado de entrada.** Com vida cheia, há queda em 21% das lutas. Com metade da vida, em 60%. Com metade da vida e 2 Sequelas, alguém é Derrotado em 24%.
- **Escolha de alvo.** Atacar o mais ferido leva as quedas de 21% para 48%.
- **Corpos.** Dois corpos de 16 PV contra um de 32 PV: quedas de 11% para 30%. A ação a mais pesa mais que a vida.
- **Recurso do inimigo.** Em luta de 2 rodadas, PE, sem PE e recarga 5–6 dão quase o mesmo resultado (21%, 23% e 15% de queda).
- **Distância do socorro.** A 2 turnos, a derrota no trio vai de 1% para 11% (24% contra o mais ferido). Na dupla, vai de 8% para 25%.
- **Grade da peça 26.** O Desastre ×3 (85 PV) dura 4 rodadas em vez de 3, com 13% a 31% de Derrotado. O trio causa cerca de 5 a 6 de dano por personagem e por rodada; a grade supõe 9,5. A Defesa 13 do inimigo é suposta, porque a peça 26 só a define a partir do nível 5.

**C08, o Sineiro** (`c08_sineiro.py`, perfis de nível 6 do caso 73, modelo sem grade):

| Conduta do grupo | Mediana / p90 de rodadas | Alguém cai | Derrotado |
|---|---|---:|---:|
| Ignorar a preparação, só Rina perto | 5 / 6 | 0,3% | 0% |
| A presa tenta fugir quando há preparação | 5 / 7 | 0% | 0% |
| Interromper (Mei empurra, Rina tenta Derrubar) | 6 / 11 | 6,2% | 3,1% |
| Mei fica dentro da zona | 5 / 6 | 5,3% | 0,3% |

Com Mei entrando com 18/44 PV, as duas últimas linhas sobem para 8,5% e 9,1% de quedas. Com o Alicerce de Rina, interromper volta a 0,2%.

**Interromper a preparação sai mais caro que deixá-la acontecer.** Interrompido, o Sineiro não fica com Guarda Aberta e volta a usar Atacar no turno seguinte. Rina, por sua vez, perde o ataque que trocou por Derrubar.

Contra esse trio o Sineiro raramente derruba alguém. O perigo do caso 73 vem de posição: alguém ficar dentro da zona. A ficha não precisa de mudança por isso, mas o ensaio deve continuar mostrando o erro de posição.

**C09, o portão** (`c09_portao.py`, Carregador do caso 63 contra o trio do piloto, modelo em linha):

| Versão | Mediana / p90 de rodadas | Portão fechou | Fechou com alguém dentro |
|---|---|---:|---:|
| Motor desligado | 2 / 3 | 0% | 0% |
| Fechamento ativo, grupo ignora | 2 / 3 | 8% | 5,8% |
| Conjurador para o motor na rodada 1 | 3 / 4 | 0% | 0% |
| Apoio ocupa a faixa | 3 / 4 | 10% | 0,1% |

Ninguém caiu em nenhuma versão. O Carregador gasta o único ataque em Agarrar e quase não causa dano: 0,09 acerto por luta.

**O prazo de três rodadas é mais longo que a luta.** O fechamento só pesa quando alguém é arrastado para o recuo. Nesses casos a saída leva de 4 a 9 rodadas. Parar o motor ou ocupar a faixa custa uma rodada e não traz ganho para esse grupo. Para o portão pressionar, o cenário pediria um prazo menor ou uma criatura que demore mais a cair. Fica como observação; nada foi alterado.

## O que entrou no livro

As três orientações aprovadas pelo autor em 02/11:

1. **Capítulo 6, seção 6.5:** novo trecho "O que mais muda a dificuldade". Põe em ordem estado de entrada, escolha de alvo, ações do lado inimigo, distância do socorro e vida.
2. **Capítulo 6, "Quando o grupo corre risco":** quem cura deve ficar a no máximo um turno de quem está na frente.
3. **Capítulo 6, seção 6.4:** conferir o dano que uma tabela geral supõe antes de usar a vida que ela indica.

O novo caso 104, **O que mais pesa no encontro**, traz os números e foi incluído no índice de casos. A ficha de registro para mesas reais está em `apoio-encontros-149/ficha-de-registro-de-mesa.md`.

## PE de inimigo

O autor decidiu em 02/11: *"Por enquanto mantém sem, se o livro n aborda, se o livro aborda põem"*.

Busca na R60 (`LIVRO-COMPLETO-R60.md`): o livro não define reserva de PE para inimigos.
- O exemplo de combate (§ "Ataque da maldição") não usa PE.
- Leitura de Reservas (linha 3263) lê PE "do alvo", sem dizer que inimigos têm reserva.
- A peça 26 §6.1 diz que inimigos não contam PE.

A decisão vale então como **inimigo sem PE**. O Sineiro já segue esse modelo, com 0 PE e capacidades por preparação.

**A aplicação ainda não foi feita.** O guia usa PE de inimigo em cerca de 32 arquivos. Os principais são a primeira missão, o Amontoado, Toru e Sayo, a seção 6.3 e os casos 14, 52, 57, 59, 60, 75, 76 e 77. A Doma também depende disso. A mudança mexe em mecânica e em muitos arquivos, por isso a proposta de troca vai ao autor antes de qualquer edição.

## Limites

- Os modelos não têm grade, Bloquear, Cobrir-se de Energia nem escolhas táticas dos jogadores.
- O Sineiro sempre agarra Rina.
- O Carregador não usa Derrubar nem Empurrar.
- Ficaram fora C03, C06, C10, C11 em mapa real e C13.
- São resultados de simulação; não substituem mesa.

## Próximo trabalho

- Proposta de troca para inimigo sem PE, com a lista de arquivos e a substituição de cada reserva por frequência, preparação ou usos.
- Regerar o HTML e o PDF com os geradores de `apoio-editorial-147`.
- Registrar mesas reais com a ficha.
- Atualizar `SALVAMENTO.json` no próximo salvamento.

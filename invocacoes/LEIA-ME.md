# Invocações — o subsistema em desenvolvimento, fora da edição jogável

**O subsistema completo ainda não foi aprovado para publicação. As decisões autorais até o §46 estão aprovadas; a consolidação r5 continua candidata.** O Evocador e as Invocações saíram do livro na v0.270, a pedido do Mizuki, até o subsistema fechar:

> *"Bloqueie temporariamente Evocador e Invocações na edição jogável. Prefiro que suas regras saiam do livro nesta edição, incluindo as Trilhas antigas vinculadas ao Evocador. Preserve as fontes antigas em arquivo e todo o desenvolvimento atual em pasta separada. Não destrua material nem substitua o Evocador por outro Caminho."*

O desenvolvimento foi feito fora desta pasta, num chat que não a via, e voltou num pacote. Esta pasta guarda o que ele trouxe, sem mudar um byte, e as fontes antigas que saíram do livro.

## O que tem em cada pasta

| pasta | o que é |
|---|---|
| `03-INVOCACOES/` | o subsistema como ele está: a candidata v0.3, revisão 5, com as decisões até o §45 e as 212 verificações simbólicas. **Sem prova de equilíbrio e sem playtest humano.** Comece pelo `00-REGISTRO-E-PONTO-DE-RETOMADA.md` |
| `04-PESQUISAS-E-HISTORICO/` | as pesquisas, os rascunhos, os retornos de auditoria e os pacotes originais que levaram à r5. Serve para uma dúvida específica, e não para leitura inteira |
| `museu/` | o texto que saiu do livro na v0.270, sem mudar uma linha: o capítulo de Invocações (`60-invocacoes.md`) e a seção do Evocador do capítulo de Caminhos (`35-evocador.md`) |
| `DECISOES-A-PARTIR-DO-46.md` | as decisões depois do pacote, a partir do §46, no formato do registro dele |

## O que continua valendo, e onde

**A peça 15 continua em `sistema/03-mecanica/`**, com o validador dela rodando contra a cópia do capítulo que está no `museu/`. Ela é a regra da arquitetura anterior, e é o texto que volta se o subsistema voltar como estava.

**O Evocador continua como desenho** na peça 6 e no `DESENHO-caminhos.md`. A base dele não mudou.

**A candidata r5 não substitui a peça 15.** Ela vira regra quando o Mizuki fechar o subsistema, e aí a peça, o livro e o validador mudam juntos.

## Onde o trabalho parou

**O §56 fechou na v0.297, e mora em `DECISOES-A-PARTIR-DO-46.md`, junto com os §§46 a 55** — *o `03-INVOCACOES/` continua como chegou.* A entrada e a troca custam a Ação Bônus do invocador; a primeira intenção de quem entra sem trocar é outra Bônus. **O §55, da v0.296:** a entidade que entra sem trocar aparece colada no invocador, e na troca a substituta aparece no lugar de quem sai; distância maior pode vir da invocação, de Trilha, de Caminho ou de técnica. **O §54, da v0.295:** a entidade só é recolhida no turno do invocador, e com ele consciente; a queda e a morte do invocador não são recolhimento. **O §53, da v0.294:** a entidade só entra em campo no turno do invocador, e com ele consciente; a troca também; um Caminho ou uma Trilha pode mudar isso no futuro. **O §52, da v0.293:** no turno do invocador, o limite de quantas entidades atacam conta só a atuação com dano; ficam fora a especial comandada, a condição sem dano e as ações comuns sem dano, `Agarrar` e `Derrubar` incluídos, e o que acontece fora do turno; e a condição Média ou Pesada só vem de especial comandada. O número do limite continua pendente. **O §51, da v0.292:** uma Ação Bônus de redirecionamento alcança todas as entidades em campo, e cada uma pode receber uma intenção diferente, desde que seja de básica; isso revê duas frases da r5 §4, por decisão do Mizuki. **O §50, da v0.291:** cada corpo tem uma básica por ciclo, e a quantidade não cresce com o nível. **O §49, da v0.290:** o campo não reparte capacidade entre as entidades — cada uma tem a própria ficha, e o que limita quantas cabem é um teto de corpos. **O §48, da v0.289:** quando o invocador morre, as entidades saem de campo na hora, e a que não recolhe fica `Desligada` ("e a escolha é A"). **O §47, da v0.288:** o invocador apagado não derruba a sustentação — a entidade segue a rotina e cumpre as ordens recebidas antes ("Continua A"). **O §46, da v0.275:** a zero PV a invocação para de atuar e sai de campo, e a que o vínculo não deixa recolher fica no lugar, `Desligada`.

**O primeiro lote de desenvolvimento depois do §46 foi feito fora desta pasta, e fica no HD** ("fica no hd por enquanto"), em `/media/mizuki/HD Externo II/Claude/invocacoes-pos46/`: a candidata na revisão 16, que já integra os §§46 a 56; os testes de cada um, à parte das 212 verificações da r5, que continuam passando; e a bancada paramétrica. **A pergunta que espera o Mizuki é com que ação se recolhe uma entidade sem pôr outra no lugar** — a Bônus, a de Movimento ou nenhuma, uma por turno; o PE vem depois. Morte definitiva, volta, cura, preço e o destino das entidades de um invocador morto continuam pendentes, candidatos a depender do vínculo, e esperam o construtor.

*Até a v0.287 este parágrafo parava no §46 e dizia que a próxima revisão da candidata o integraria; a candidata, no HD, integrou os onze.*

## Por que esta pasta fica fora da checagem de referência morta

As citações dentro de `03-INVOCACOES/` e `04-PESQUISAS-E-HISTORICO/` são caminhos do próprio pacote e dos pacotes que vieram antes, e os arquivos carregam SHA-256 no manifesto: consertar um caminho quebraria a prova de que nada mudou na viagem. O `conferir-repositorio.py` escreve o motivo junto da isenção. **Este arquivo e o `museu/` continuam sob a checagem.**

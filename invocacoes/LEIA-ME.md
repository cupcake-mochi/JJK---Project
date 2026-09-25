# Invocações — o subsistema em desenvolvimento, fora da edição jogável

**Nada aqui é regra aprovada.** O Evocador e as Invocações saíram do livro na v0.270, a pedido do Mizuki, até o subsistema fechar:

> *"Bloqueie temporariamente Evocador e Invocações na edição jogável. Prefiro que suas regras saiam do livro nesta edição, incluindo as Trilhas antigas vinculadas ao Evocador. Preserve as fontes antigas em arquivo e todo o desenvolvimento atual em pasta separada. Não destrua material nem substitua o Evocador por outro Caminho."*

O desenvolvimento foi feito fora desta pasta, num chat que não a via, e voltou num pacote. Esta pasta guarda o que ele trouxe, sem mudar um byte, e as fontes antigas que saíram do livro.

## O que tem em cada pasta

| pasta | o que é |
|---|---|
| `03-INVOCACOES/` | o subsistema como ele está: a candidata v0.3, revisão 5, com as decisões até o §45 e as 212 verificações simbólicas. **Sem prova de equilíbrio e sem playtest humano.** Comece pelo `00-REGISTRO-E-PONTO-DE-RETOMADA.md` |
| `04-PESQUISAS-E-HISTORICO/` | as pesquisas, os rascunhos, os retornos de auditoria e os pacotes originais que levaram à r5. Serve para uma dúvida específica, e não para leitura inteira |
| `museu/` | o texto que saiu do livro na v0.270, sem mudar uma linha: o capítulo de Invocações (`60-invocacoes.md`) e a seção do Evocador do capítulo de Caminhos (`35-evocador.md`) |

## O que continua valendo, e onde

**A peça 15 continua em `sistema/03-mecanica/`**, com o validador dela rodando contra a cópia do capítulo que está no `museu/`. Ela é a regra da arquitetura anterior, e é o texto que volta se o subsistema voltar como estava.

**O Evocador continua como desenho** na peça 6 e no `DESENHO-caminhos.md`. A base dele não mudou.

**A candidata r5 não substitui a peça 15.** Ela vira regra quando o Mizuki fechar o subsistema, e aí a peça, o livro e o validador mudam juntos.

## Onde o trabalho parou

A próxima discussão é o que acontece quando uma invocação chega a zero PV. A decisão do §22 aprovou a equivalência entre campo e reserva, mas não escolheu entre dissipar, ficar inconsciente, ser destruída ou se recuperar. Foi recomendado que ela saia do campo a zero PV, encerrando ordens e preparações pela saída, sem devolução nem cura automática — e **o Mizuki ainda não aprovou**. Não há §46.

## Por que esta pasta fica fora da checagem de referência morta

As citações dentro de `03-INVOCACOES/` e `04-PESQUISAS-E-HISTORICO/` são caminhos do próprio pacote e dos pacotes que vieram antes, e os arquivos carregam SHA-256 no manifesto: consertar um caminho quebraria a prova de que nada mudou na viagem. O `conferir-repositorio.py` escreve o motivo junto da isenção. **Este arquivo e o `museu/` continuam sob a checagem.**

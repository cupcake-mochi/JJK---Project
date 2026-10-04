# Revisão independente — Bastião

**Fotografia:** `9d572799c5d882a8eeae475b648abffc68bb2192a72caca19e435fc0b406c302`. Leitura integral das 11 páginas lógicas, feita pelo agente R12/R17, distinto do autor R13. Não houve edição do manuscrito, playtest ou avaliação com leitores humanos.

Foram lidos `ALTERACOES.json`, `INTERFACES.json` e `FONTES.json`. O nome INTERFACES.md não existe neste lote: o contrato está em JSON. Foi lido o trecho completo de Bastião em manual35, conferido idêntico à edição integrada, e o contrato autoral v0.331. As interfaces dirigidas consultadas foram R02 Ataques/Bloquear, R03 Dano/Resistência/tipos, R04 Recuperação e as permissões de R06, R09 e R10 já auditadas.

## Achado P2 — Ataque e TR em Nem Um Arranhão

**Local:** Defesa e recuperação, Nível7. O benefício diz TR Físico provocado por um ataque. R02, abertura Ataques, define ataque por uma rolagem de acerto e separa feitiços de TR. Uma Explosão ofensiva por TR Físico pode, por leitura técnica, ficar fora da habilidade mesmo lançada por inimigo dentro de Olhos Em Mim.

**Recomendação:** decidir o alcance do termo antes da integração. Se a intenção é proteger dos efeitos ofensivos de um agressor próximo, escrever: “TR Físico exigido por um ataque ou efeito ofensivo de uma criatura dentro da área”. A frase preserva o uso passivo, a localização do causador e o TR específico, sem estender a proteção a uma queda ambiental. Caso o veto às conjurações por TR seja intencional, manter a regra e dar esse exemplo negativo explicitamente.

A regra original usa o mesmo vocabulário, portanto este achado não é perda na transcrição da candidata. É uma ambiguidade revelada pela definição técnica mais precisa de R02.

## Dependência P2 de integração — Dano misto transferido

**Local:** Passa Pra Mim. O procedimento local está executável no exemplo e preserva tipos, mas a candidata R03 lida nesta revisão ainda não contém a nova ordem de consumo das parcelas. Ela só manda separar por tipo para resistência e depois somar para RD genérica. O contrato INTERFACES.json já registra a alteração aprovada pela raiz.

**Recomendação:** aplicar a sincronização R03 antes de publicar o conjunto, pois Passa Pra Mim remete a um procedimento que hoje só está registrado na interface. O leitor precisa saber quem escolhe a ordem e em que momento, inclusive quando RD genérica e vida temporária consomem parte do dano.

## Casos e contas

| Caso | Resultado da candidata |
|---|---|
| Assumir um golpe | Reação declarada antes do d20, alvo passa a Bastião e defesa própria é resolvida depois. |
| Assumir e Bloquear | Não cobra segunda Reação, nem transfere cobertura que só protegia o aliado. |
| Ataque assumido erra, mas tem dano no erro | Bastião recebe somente o efeito específico de erro. Casca, Trocação e Retaliação não disparam. |
| Duro de Matar falha duas vezes na rodada | Aplica nas duas, sem limite reintroduzido. Usa dados já rolados e Constituição. |
| Nem Um Arranhão com Reação gasta | Continua funcionando, sujeito ao esclarecimento de tipo de efeito acima. |
| Casca: dano36, Con3, Bloquear5+4, Casca2+7 | Duro reduz12, Casca reduz11, restam13. Com resistência,18−12−11 chega a0. |
| Passa Pra Mim: aliado10PV recebe16 | Aliado perde9; transfere7 e fica1. Reação gasta não impede a habilidade. |
| Dano misto15Cortante+6Fogo, aliado10PV | Aliado perde9Cortante; Bastião recebe6Cortante+6Fogo. Resistência a Cortante resulta3+6=9. |
| Transferência e outra defesa | Bastião não bloqueia a parcela, não é alvo do ataque e não repete Casca/Duro por ela. Não retransmite a parcela. |
| Aliado já com0PV | Passa Pra Mim não produz recuperação. |
| Arrastão com1/2/3/5/6alvos | Ampliação custa0/2/4/8/10PE. Pagamento é por tentativas, antes dos resultados. |
| Arrastão com alcance9m | Golpes alcançam alvos na área por exceção expressa; não atravessam parede. Agarrar continua exigindo alcance corporal e mão. |
| Arrastão após usar controle de Mão Pesada | Não amplia novamente o mesmo controle. Empurrões conservam um uso por alvo. |
| Arrastão acerta e Bônus disponível | Permite Trocação, mas o soco da Bônus usa alcance normal. |
| Contra a Parede, nível27, Classe máxima7 | Feitiço Classe3, normalmente9PE, uma vez na ação. |
| Contra a Parede com segundo ataque escolhido | Segundo não recebe Canalizar/Estímulo. Primeiro conserva seus requisitos normais. |
| Ataque físico de Contra a Parede crítico | Dados físicos seguem crítico. Feitiço separado não causa crítico. |
| Ataque físico de Contra a Parede erra | Feitiço ainda resolve com ataque/TR, alcance e requisitos próprios. |
| Contra a Parede e Carregar | Não libera gratuitamente um preparo de múltiplos turnos. |
| Inabalável com personagem inconsciente | Preserva área e passivos aplicáveis, sem conceder ações ou Reações novas. |

As contas foram recalculadas independentemente das tabelas do auditor do autor. Os exemplos não constituem uma simulação integral de combate. O rendimento do Bastião após a remoção do limite de Duro depende de quantidade de ataques recebidos, Defesa, proteção, críticos e dano por golpe. Essa remoção é autorização humana explícita e foi preservada, não reaberta nesta revisão.

## Escrita e consulta

O texto usa títulos diretos, quadros de progressão, gatilhos antes de resultados e exemplos de interação. A separação de acerto, dano e reação facilita consultar o kit. As repetições sobre alcance da interceptação e alcance do revide são funcionais: fecham a falsa leitura de que o alcance de proteção aumenta também o soco.

A inspiração editorial pode ser reconhecida na estrutura de características e níveis do PHB2024 local, em leitura dirigida, sem transplantar a classe de outro jogo. Os nomes atuais foram preservados, conforme a fila de revisão global. Não há nova alegação de cânone neste Caminho.

## Cobertura

- `bas-bastiao` — Bastião.
- `bas-olhos` — Olhos Em Mim.
- `bas-defesa` — Defesa e recuperação.
- `bas-aliados` — Proteção de aliados.
- `bas-muro` — Muro.
- `bas-casca` — Casca Grossa e Inabalável.
- `bas-punho` — Punho.
- `bas-mao` — Mão Pesada e Minha Vez.
- `bas-arrastao` — Arrastão.
- `bas-combatente` — Combatente Amaldiçoado.
- `bas-oportunista` — Oportunista e Contra a Parede.

Sem bloqueio adicional identificado nas alterações humanas4.1–4.5. A ambiguidade de Nem Um Arranhão e a sincronização de dano misto são os pontos a fechar. O sistema de morte, Integridade e a diagramação permanecem com suas validações próprias.

## Fechamento após BAS26

O coordenador autorizou explicitar ataque ou efeito ofensivo de criatura hostil na área. Correção aplicada, com snapshot integral prévio em `historico/antes-BAS26`. Hash final: `3334f5e2ff950bc79bbad12ae3f4c2b902e8fbf1539a22e64af7e8826cd14e9d`. Releitura da habilidade e oito casos de origem/tipo de TR confirmaram a inclusão de explosão hostil sem teste de acerto, exclusão do ambiente, de aliado e de fonte fora da área. A queda causada por efeito ofensivo de hostil na área mantém essa origem.

Auditoria reproduzível: 113 verificações, 52 casos, 216 perfis defensivos, 12 de TR, 27 de Provocar e 10.200 transferências, todos aprovados. Checker editorial de exportação: zero achados. Os números descrevem modelos de regras, não sessões reais. A integração do R03 para dano misto ainda precisa ser confirmada pelo coordenador. PDF e inspeção visual não realizados nesta revisão.

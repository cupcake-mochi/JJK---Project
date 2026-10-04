# Revisão independente de R08

**Revisor:** subagente rotas_didatica, distinto do autor de R08. **Método:** leitura integral do manuscrito, cotejo dirigido das fontes mecânicas e análise de casos. Revisão por modelo, sem leitores humanos e sem playtest. Não inclui inspeção visual do PDF.

**Snapshot:** `PODERES-AVANCADOS.md`, SHA-256 `bb29892e3f665781a5533ea772af39a8de1518d3c0ce751b7658b4fc18d403fc`. Foram lidas as 15 páginas lógicas, não apenas os exemplos finais.

## Achados

### P2 — Sucesso de TR da Incompleta diverge da regra comum

**Local:** `acerto`, linha 64: “sucesso no TR recebe metade do dano”. R06, `Conjurar — Resultados`, usa metade dos **dados**, arredondada para baixo. Manual40:1017 encaminha Incompleta à resolução de um feitiço. Não encontrei na decisão registrada de R08 justificativa para essa outra distribuição.

**Caso:** Acerto de 8d8. A candidata rolaria 8d8 e dividiria o total. O dono comum pede 4d8 no sucesso. As médias ficam próximas, mas a variância e a aplicação de outros efeitos sobre os dados são diferentes.

**Recomendação exata:** trocar por “sucesso no TR recebe metade dos dados de dano, arredondada para baixo” e ajustar o exemplo: “na Incompleta com TR, role 4d8 para quem resistiu”. Não é necessário criar exceção nova ao domínio para esse caso.

### P2 — Primeira entrada numa regra contínua da Incompleta não tem teste definido

**Locais:** `acerto`, linha 66; `sembarreiras`, linhas 165–167. O TR ocorre quando o Acerto acontece. A outra seção diz que uma regra contínua alcança quem entra e que quem sai e volta conserva seu TR anterior. Falta decidir o primeiro ingresso de quem ainda não tinha feito teste naquela aplicação.

**Caso:** a Incompleta abre quando Bruno está fora. Entre pulsos, Bruno entra na área de uma regra que proíbe causar dano. Ele não tem um TR anterior. Aplicar a proibição automaticamente torna o ingresso mais forte que a abertura; esperar o próximo pulso contradiz a leitura de regra contínua presente para quem entra.

**Recomendação exata:** acrescentar à Incompleta que uma criatura sem resultado vigente faz o TR na primeira entrada na área de uma regra contínua. O resultado dura até o próximo Acerto ou encerramento. Sair e voltar nesse intervalo conserva o mesmo resultado. Isso é resolução da regra contínua, não outro Acerto de dano nem um consumo extra de proteção por pulso.

### P3 — Mesmo nome de protagonista para técnicas diferentes

**Local:** `galeriavidro`, linha 269, e referências anteriores a Mei. R06 ensina o leitor com Mei e sua técnica de fios. R08 usa Mei com lâminas de vidro sem indicar que se trata de outro exemplo.

**Efeito sobre a leitura:** isoladamente o exemplo está claro. Na sequência do livro, pode parecer que completar a técnica ou abrir domínio autoriza mudar seu funcionamento. Isso é especialmente inconveniente num capítulo que exige manter a Regra.

**Recomendação:** usar outra personagem no exemplo de vidro, ou declarar explicitamente que se trata de uma ficha independente. Mudar apenas o nome é suficiente, sem mexer nas contas.

## Cobertura integral por página lógica

| Página | Parecer e caso conferido |
|---|---|
| degraus | Aquisição distingue custo total e diferença: 2 → 3 → 5 espaços. Completa não é recebida automaticamente por atingir Classe. Rotas Sem Técnica e Marcial continuam sem Expansão. |
| criardominio | Acerto e Efeito têm tarefas distintas. A exigência de uma ficha executável melhora o texto antigo. Efeitos originais ainda dependem de revisão individual; não há prova de equilíbrio para qualquer efeito inventado. |
| acerto | Dados 2 × maior Classe e garantia estão explícitos. Aliados não são poupados automaticamente. Achados de TR e entrada acima. |
| protecao | Remete corretamente aos procedimentos de R09. Suspensão por disputa não é bloqueio por aptidão, portanto não consome capacidade de Domínio Simples. |
| abertura | A duração conta turnos seguintes, sem contar abertura duas vezes. Refino 5 produz três aplicações e dois turnos seguintes. Classe 0 não vira custo positivo pela regra de mínimo 1. |
| barreira | Vida exterior e interior compartilham um registro, evitando restaurar a casca ao mudar de face. Transportar a barreira não dispensa Agarrado. Procedimento é candidato e foi registrado, sem alegar ser regra canônica. |
| rescaldo | O preço ocorre para o dono cujo domínio termina. O vencedor ainda ativo não recebe Rescaldo prematuro. Efeitos concluídos e sustentações futuras são distinguidos. |
| sembarreiras | Centro fixo e alcance de alvos sem energia dependem da técnica registrada. Raio de 199,5 m segue grade. Exemplo de descontos: 49/42 PE para abrir e 7/10 PE para Classe 5. |
| disputa | Ordem refino → Acerto sem dano → d12 é inequívoca. Um encontro não permite rolar todo turno nem sair e voltar para procurar resultado melhor. |
| manterdisputa | Falhas por domínio, testes separados de Concentração e limite por jogador no inimigo estão explicados. O exemplo do total 16 contra CD 15 e depois 17 não refaz o d20. |
| sobreposicao | Aberto atinge casca uma vez por pulso, não por ocupante. Dano na casca não causa TR de Vigor no dono. Incompleta suspende sem vencer e seu fim não cria um dano adicional. |
| multiplos | A região comum evita derrubar barreiras em cadeia sem encontro triplo. Um d12 por dono em resolução simultânea reduz dependência da ordem dos pares. Ainda exige mapa em casos complexos. |
| galeriavidro | 24 PE, 8d8, raio 7,5 m, três aplicações, 100 PV exteriores e média 108 conferem. Proteção de uma pessoa ocupa uma mão e não se estende a ataques comuns. Achado editorial de nome acima. |
| salatregua | Regra de ambiente é simétrica. Agarrar continua disponível, cura continua pagando seu custo. 30 PE, refino 7, raio 10,5 m, três turnos seguintes e 150 PV conferem. |
| confronto | 250 → 187 → 124 → 61 → 0 após quatro aplicações de 63. O Acerto do derrotado é separado do dano na casca, sem passar o mesmo dano duas vezes. O prazo não reinicia. |

## Interfaces verificadas

Foram cotejados manual40:998–1096 e 1117–1175, R06 `Conjurar`, R03 `Dano e Condições`, R09 `Proteção contra domínios`, Cesta, Domínio Simples, Pétala e Extensão. Também foram lidos `CONTRATO.json`, `ESCOPO-E-FONTES.md` e trechos de `ALTERACOES.md` de R08.

- **Cesta:** sua queda prevê Acerto imediato. R08 remete à entrada sem retirar esse preço.
- **Domínio Simples:** esgotar a capacidade deixa passar o próximo Acerto normal; encerramentos por voto, manutenção, vontade ou inconsciência têm aplicação adicional. R08 distingue esses momentos.
- **Pétala:** queda não causa Acerto adicional. Regra abstrata sem contato não é anulada por ela. R08 mantém essa fronteira.
- **Extensão:** permissão específica sobre Incompleta não é anulada pela apresentação geral de Acerto garantido.
- **R10:** a ausência de energia impede seleção pelo critério de energia pessoal, sem conceder imunidade a toda aplicação ambiental. R08 exige capacidade registrada para alcançar quem não tem energia.

## Comparação editorial e limites

A organização por aquisição, campo da capacidade, ação, custo, duração e exemplos é compatível com a leitura dirigida do PHB 2024 fornecido pelo usuário, páginas PDF 241 e 243. O uso de regras concretas para os dois exemplos acompanha os critérios de criação do DMG 2024, página PDF 63, consultados nesta sessão. Isso é comparação de organização e campos, não cópia de texto ou importação da economia de magias.

Títulos são simples e correspondem a tarefas de consulta. A introdução tem aparência de capítulo de regras de RPG. A repetição mais visível — domínio sem barreiras retomando centro, custo e saída — tem função de esclarecer o modo, sem reproduzir uma habilidade de Trilha. Não identifiquei prosa de justificativa interna ou narrativa excessiva nos exemplos.

O exame não valida diversão, duração real de combate ou compreensão de iniciantes humanos. As alegações canônicas não foram promovidas a fatos: o manuscrito identifica a adaptação e seus documentos registram acesso primário incompleto. Essa limitação é adequada à evidência disponível. Inspeção visual e leitura final depois das correções cabem ao PDF da coordenação.

**Conclusão de revisão:** corrigir os dois procedimentos P2 antes de considerar o manuscrito fechado. O P3 é um ajuste pequeno, recomendado para coerência entre capítulos. Fora desses pontos, a candidata oferece procedimentos executáveis e remissões úteis nas interfaces examinadas.

## Tratamento pelo principal

Os três achados foram corrigidos em R08-31 a R08-33. Nova revisão textual conferiu os trechos e suas remissões. A prova numérica e a inspeção do PDF são executadas sobre o novo hash.

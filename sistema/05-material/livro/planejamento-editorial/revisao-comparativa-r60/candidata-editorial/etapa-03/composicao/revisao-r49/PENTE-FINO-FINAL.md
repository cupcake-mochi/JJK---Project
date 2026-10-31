# Pente fino final — R49

## Resultado

A composição e a integridade do PDF passaram pela última conferência. Não encontrei nova falha bloqueadora de diagramação nos casos reinspecionados. **Há três pendências textuais confirmadas que devem acompanhar a entrega ao Claude.** Portanto, a revisão visual está encerrada, mas a integração editorial das Origens não deve ser declarada inteiramente encerrada.

PDF mantido intacto: 397 páginas. Sem alteração de texto, regra, diagramação, fonte ou arte nesta auditoria. Sem commit ou push.

## O que foi conferido agora

- Nova execução da conferência integral: 118.063 checagens, zero problemas; conteúdo, margens, sobreposição, extração do PDF, links e marcadores.
- 1.540 títulos conferidos quanto à permanência com o elemento seguinte: nenhum separado por página ou coluna.
- 331 faixas de duas colunas: sequência esquerda → direita preservada.
- 511 blocos e texto consolidado idêntico à R48. Os 2.643 arquivos da R48 continuam intactos.
- Nenhuma ocorrência das expressões proibidas “suas fichas” e “não tem como recusar” no texto consolidado.
- Reinspeção visual ampliada das páginas 48, 72, 74, 79, 84, 111, 137, 163, 238, 299, 340 e 342. Os renders correspondem ao mesmo PDF conferido por hash.
- Casos solicitados: Receptáculo aproveita a coluna direita; Leitura a Dois permanece inteira; a duração de Extensão de Domínio vem depois da apresentação na mesma coluna; tabelas e exemplos nos recortes examinados estão legíveis, sem cortes.

A passagem anterior pelas 397 páginas continua documentada em REVISAO-VISUAL.json. Esta última rodada combina checagem integral com inspeção ampliada seletiva; não é uma nova leitura palavra por palavra de todas as regras.

## Pendências para o Claude

### PF01 — Olho adicional, página 84

Bloco: `origens--feto-beneficios`.

O PDF ainda diz apenas “visão noturna a 9 m”. A definição aprovada pelo autor ainda precisa ser incorporada: enxergar na penumbra e na escuridão comum até 9 m sem penalidade por falta de luz, sem distinguir cores no escuro; os demais impedimentos de visão continuam valendo.

A aprovação do autor foi “Sim, essa definição”. Não é uma questão nova de balanceamento.

### PF02 — Pacto permanente, página 340

Bloco: `ritual--pacto-permanente`.

Trecho: “Não converta esses benefícios em níveis de Caminho, Trilha ou Legado.”

A referência a níveis de Legado está desatualizada após a reconstrução das Origens. Corrigir a remissão, preservando a proibição relativa a Caminho e Trilha.

### PF03 — Pactos na criação, página 342

Bloco: `ritual--pacto-restricao`.

Trecho: “use os benefícios e limites da Origem, do Legado e da técnica”.

A frase ainda trata Legado como benefício mecânico. Acompanhar a definição atual de Legado de história e o ajuste preparado no rascunho.

## Rascunho separado que também acompanha a passagem

`/home/mizuki/CHAT-GPT/RPG -JJK/entregas/rascunho-polimento-legados-sobre-r46-2026-10-13/`

O LEIA-ME-RASCUNHO-PRESERVADO.md explica por que o polimento narrativo dos Legados, as referências de Pactos e a explicação da exceção CE4 foram separados da R47: aquela edição recebeu exclusivamente o item 194. A R48 e a R49 foram rodadas de diagramação e conservaram o texto.

O CE4 já está definido na Restrição corporal; a pendência da explicação geral é de remissão e compreensão, não ausência completa da regra. O texto geral de Talentos pagos limita explicitamente o assunto aos Talentos pagos. Não alterar a tabela normal de aquisição para conceder CE4 a todos.

**Usar a R49 como base. Não substituir a R49 pelo PDF antigo do rascunho**, que não preserva automaticamente todos os ajustes posteriores. Transferir apenas as alterações necessárias, registrar antes/depois e conferir novamente as páginas afetadas.

## Espaços em branco

As 23 páginas de meio de capítulo com mais de um terço de vazio inferior continuam listadas no RELATORIO.md, com o motivo da composição escolhida. O branco restante não foi classificado como inexistente nem integralmente inevitável. Uma nova redução precisa ser comparada com o risco de fragmentar entradas, apresentações e exemplos.

## Arquivo de referência

PDF: `output/pdf/Ciclo-Maldito-R49.pdf`.

SHA-256: `c9d1b6cc5f4a63493f7c966caf1a6dfc71c7ff8afe1ee9f45e03fb59ac9f8975`.

Evidências: PENTE-FINO-FINAL.json e PENTE-FINO-CONFERENCIA.log.

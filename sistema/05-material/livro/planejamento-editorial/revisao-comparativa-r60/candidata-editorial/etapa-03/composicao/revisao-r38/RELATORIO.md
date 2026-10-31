# Entrega R38 — aproveitamento e duas Bênçãos

**367 páginas, 27 a menos que as 394 da R37.** A R37 foi preservada integralmente. Sem commit ou push.

## Texto

A frase «Gastar seus PE até chegar a zero não torna um feiticeiro uma criatura sem energia.» voltou ao ponto pedido, em geral--pressao, na p. 38, logo após a frase sobre a busca energética não encontrar uma criatura sem energia amaldiçoada.

As duas opções novas entram como Bênçãos adquiridas por Lapidação, na p. 291, e aparecem no catálogo da p. 288:

| Bênção | Acesso | Efeito |
|---|---|---|
| Represália | CE 2, Lapidação mínima 4, Destreza 4 | Reação para um ataque corpo a corpo contra criatura percebida a até 1,5 m que use aptidão amaldiçoada ativa ou conjure feitiço. Resolve depois do uso, sem cancelá-lo; exige que o alvo permaneça no alcance. |
| Sangue Frio | CE 3, Lapidação mínima 7, Constituição 4 | Vantagem em TR contra aptidões amaldiçoadas e feitiços de criatura a até 3 m; uma repetição de TR falho por combate, antes das consequências, com resultado obrigatório e o mesmo alcance. |

Não há custo adicional de PE. As decisões de balanceamento delegadas pelo autor estão em DECISOES-DE-BALANCEAMENTO.md. São decisões editoriais de projeto, ainda sem teste de mesa.

**O LIVRO-COMPLETO.md é idêntico ao da R37 fora da frase restaurada, das duas Bênçãos e de suas duas linhas no catálogo.** São três blocos alterados, todos com antes/depois e motivo em ALTERACOES-TEXTO.json. O pedido adicional de duas Bênçãos é a exceção autorizada à preservação textual. Nenhum exemplo foi reescrito. Os dados e a ordem das demais tabelas foram preservados.

## Aproveitamento

| Medida uniforme nesta auditoria | R37 | R38 |
|---|---:|---:|
| Páginas totais | 394 | 367 |
| Branco inferior somado, em páginas equivalentes de conteúdo | 71.53 | 41.55 |
| Branco inferior em meio de capítulo | 61.94 | 29.49 |
| Páginas de meio com média acima de um terço vazio | 35 | 11 |

O branco inferior de meio de capítulo caiu cerca de 52.4%, usando a mesma medição nas duas provas. Não apresento esses números como reprodução dos 83/72 informados pelo autor: aqui a área útil vai de 23 mm abaixo do topo a 36 mm acima do pé; capas, arte e modelos ficam fora, e a primeira/última página após cada capa é considerada borda de capítulo. Elementos largos contam para os dois lados.

Restam as páginas **5, 67, 74, 78, 103, 145, 149, 154, 159, 281, 286**. Todas precedem aberturas ilustradas preservadas. A lista, a porcentagem e a justificativa individual estão em ESPACOS-RESTANTES.md; esse arquivo inclui também as três assimetrias de coluna e os começos/fins de capítulo.

## Continuidade e aparência

O gerador deixa o bloco continuar entre parágrafos e linhas de tabela. Mantém título, preço e primeiro parágrafo juntos; em aberturas curtas ligadas a tabelas, mantém também as primeiras linhas. Tabelas longas podem quebrar, repetindo o cabeçalho. As partes de uma tabela que couberem juntas voltam a formar uma única tabela, sem cabeçalhos duplicados dentro da mesma coluna.

Há no máximo um par de colunas por página: leitura integral da esquerda, depois integral da direita. Depois de um elemento largo, o par seguinte é equilibrado dentro das possibilidades dos parágrafos inteiros. Algumas diferenças de altura permanecem para preservar aberturas e unidades de leitura. Parágrafos não foram cortados no meio nesta rodada. Fontes, tamanhos, estilos aprovados, artes, capa e créditos foram mantidos. Corpo permanece 10,25 pt, entrelinha 13,2 pt.

Na inspeção apareceu uma abertura curta de Balestra sem a tabela. Foi corrigida; agora começa com a tabela na p. 190. Muro começa junto da primeira habilidade na p. 87, seguindo a ordem das colunas. Extensão de Domínio e Duração e custo estão na coluna esquerda da p. 271. As nove Famílias do catálogo começam na mesma página de sua primeira Melhoria.

## Validação e limites

- Comparação exata do Markdown: só os três blocos autorizados diferem.
- Arquivos da R37 conferidos contra o inventário inicial: nenhum foi alterado.
- Ordem dos parágrafos e linhas de tabelas preservada; 33 repetições de cabeçalho correspondem a continuações reais.
- Nenhum título isolado, retorno da coluna direita à esquerda ou segundo par de colunas na mesma página de fluxo.
- Validação geral: 108.108 verificações, 2.240 links internos, nenhum problema encontrado.
- Visão geral das 367 páginas, incluindo reinspeção das 88 páginas recompostas na última prova; inspeção ampliada de 50 páginas selecionadas. Composições idênticas aproveitaram a inspeção anterior, com comparação de texto e geometria documentada. As imagens correspondem ao PDF final.

O exame visual desta rodada verifica composição e continuidade, com leitura das adições. Não substitui o pente-fino textual anterior nem representa uma nova leitura palavra por palavra de todas as páginas. Não foi realizado teste de mesa das novas Bênçãos.

## Arquivos de auditoria

- ALTERACOES-TEXTO.json: três blocos textuais completos.
- ALTERACOES-REGRAS.json: os dois blocos da adição de Bênçãos.
- ALTERACOES-DIAGRAMACAO.json: 502 registros com composição anterior/posterior, incluindo elementos gerados.
- CONFERENCIA.json, CONFERENCIA-GERAL.log e INDICE-CONFERIDO.json: verificações.
- REVISAO-PAGINAS.json e REVISAO-VISUAL.json: cobertura da inspeção visual.
- CORRESPONDENCIA-PAGINAS.json: localização na R38 dos conteúdos das 43 páginas apontadas da R37.
- APROVEITAMENTO-R37.json e APROVEITAMENTO-R38.json: medição completa.
- PROVA-R38.html: navegador das páginas renderizadas; abre nas Bênçãos.
- IMPLEMENTACAO.patch e REGISTRO-IMPLEMENTACAO.json: alterações do gerador e seus verificadores.

PDF final: output/pdf/Ciclo-Maldito-R38-Aproveitamento.pdf.

SHA-256 do PDF: 1523e5f8749f792dd4089f4e5d284e07695d2f5306d8fb2f44c931b090d2b19c.

SHA-256 do LIVRO-COMPLETO.md: f9e60bf4bcc7ce890966b9273d75f75b9773e9adadf26e58df7be152cc6567f7.

Próxima etapa da fila: leitura e aceite do autor sobre a R38. Para analisar os retornos, recomendação editorial: GPT-6 Astra, esforço alto. A documentação oficial o indica para trabalho complexo com documentos e oferece esforço high: https://developers.openai.com/api/docs/models/gpt-6-astra. A escolha de alto é julgamento para esta etapa, não uma comparação medida entre modelos neste livro.

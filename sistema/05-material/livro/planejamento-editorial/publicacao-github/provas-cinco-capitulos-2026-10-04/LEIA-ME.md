# Provas de cinco capítulos atualizadas — 04/10/2026

Item 1 da fila em `../../PROMPT-CONTINUAR-NO-CLAUDE.txt`: Aptidões, Fundamento, Origens, Perícias e Poderes avançados.

Revisão por modelo. Não é revisão humana, leitura de jogador nem playtest.

## Antes

O `conferir.py` dos cinco saía com código 1. A conferência independente da manhã registrou as falhas em `../conferencia-independente-2026-10-04/`.

| Capítulo | Verificações | Com falha |
|---|---:|---:|
| Aptidões | 160 | 7 |
| Fundamento | 233 | 5 |
| Origens | 204 | 5 |
| Perícias | 83 | 7 |
| Poderes avançados | 125 | 7 |

Nenhuma falha era regra quebrada. Eram o PDF do capítulo sem o texto novo e evidências presas ao hash do texto anterior.

## O que tinha mudado no texto

Na montagem do livro completo, em 03/10, os cinco receberam ajustes de remissão. Estão registrados em `../../consolidacao/lote-01/evidencias/AJUSTES-FINAIS-INTEGRACAO.json`, e a prova de cada capítulo não acompanhou.

| Capítulo | Seção | Antes | Depois |
|---|---|---|---|
| Aptidões | Domínio Simples | segue a regra própria da próxima página | segue [Duração do Domínio Simples] |
| Fundamento | Formas de ataque | as medidas desta página | as medidas desta seção |
| Origens | Escolhas da Origem | os benefícios desta página | os benefícios desta seção |
| Perícias | Investigação e conhecimento | as perícias desta página | as perícias desta seção |
| Perícias | Ambiente e saúde | as perícias desta página | as perícias desta seção |
| Perícias | Percepção e influência | as perícias desta página | as perícias desta seção |
| Poderes avançados | Criar um domínio | a quantidade da próxima página | a quantidade indicada em [Acerto do domínio] |

Desfazendo essas 7 trocas, cada texto volta exatamente ao hash que as evidências tinham lido. Então não existe outra diferença escondida.

## O que foi feito

- **Revisão editorial por delta.** As 7 linhas foram lidas no contexto. "Desta seção" fala da seção onde a frase está, e os dois links levam a um título que existe no capítulo. O `conferir_editorial` dá os mesmos achados no texto antigo e no atual (mesmo código, termo e trecho), e todos já tinham exceção revisada. O registro está no bloco `revisao_delta_2026_10_04` do `REVISAO-EDITORIAL.json` e do `LOCALIZACAO-EDITORIAL.json` de cada capítulo.
- **PDF do capítulo regerado** pelo `gerar_pdf.py`, sem mudar o gerador. Os geradores leem a fonte tipográfica de uma pasta do computador do Mizuki. No container, as quatro fontes de `../../consolidacao/lote-01/fontes-tipograficas/` foram copiadas para esse caminho, depois de conferidas por SHA-256 contra o `AMBIENTE.json`. As bibliotecas são as mesmas do registro (reportlab 4.4.9, pypdf 6.16.2, pdfplumber 0.11.9).
- **Inspeção visual por delta.** Página a página, a 60 dpi, contra o PDF anterior, que é o mesmo da inspeção registrada. Só 7 páginas mudaram, as das trocas. Elas foram abertas e não têm defeito. As outras 92 saíram idênticas em pixel, o que confirma que o ambiente reproduz o da reconstrução. Cada capítulo tem um `COMPARACAO-VISUAL-2026-10-04.json`.
- **Auditorias de regra reexecutadas**, sem desligar checagem. Mudaram só hashes e contagens de palavras e caracteres das seções trocadas.

| Capítulo | PDF antes → depois | Página aberta | Auditoria |
|---|---|---|---|
| Aptidões | `9f2409bf` → `1b1e9480` | 14 | 74 checagens |
| Fundamento | `2d8ecd73` → `05766e65` | 8 | 68 checagens de texto, 39.032 estados, 53 casos |
| Origens | `9794238a` → `75dd8939` | 2 | 333 verificações, 268 pares de Legados |
| Perícias | `8f23c332` → `c5c8039c` | 4, 5 e 6 | 41 verificações, 9.954 estados |
| Poderes avançados | `fe220c70` → `6989a923` | 2 | 154 checagens |

## Uma correção de registro, em Origens

O auditor de Origens parou na checagem de hash do `INVENTARIO.json`, o mapa dos 85 Legados. Antes de atualizar o hash, cada entrada foi conferida contra o texto atual. Uma não batia, e já não batia no texto antigo: **Revezamento**.

A migração de nomes trocou "Incapacitado" por "Guarda Aberta" e "Dano e Condições" por "Dano e recuperação" no segundo parágrafo do Revezamento. O inventário acompanhou só o primeiro parágrafo. O livro estava certo; o registro ficou para trás. Ele passou despercebido porque o hash do inventário foi atualizado por script, sem conferir o conteúdo, e o auditor só confere se cada entrada existe.

O segundo parágrafo do inventário foi alinhado ao texto, com antes, depois e motivo em `revisao_delta_2026_10_04` do próprio inventário.

## Depois

Os cinco saem com código 0 e nenhuma falha, num total de 805 verificações. As saídas estão nesta pasta, uma por capítulo, no mesmo formato da conferência independente.

Conferido também, depois das mudanças:

- os 22 capítulos do livro que têm `conferir.py` saem com código 0, e o auditor de Dano e recuperação, que não tem, passa com 55 verificações;
- os 27 validadores de `sistema/03-mecanica`, `pac7.py` e `v7.py` saem com código 0, sem PULADA;
- `conferir-repositorio.py` sai igual ao registro anterior: código 0, uma checagem pulada (a 7, `finalizado/` não existe no clone) e 37 avisos;
- `testar_editorial.py` passa;
- a conferência editorial global ia de 104 achados para 94. Os 10 que saíram são os desses capítulos. Os 94 restantes são idênticos, item a item, aos de antes, e ficam nos rascunhos antigos de regras básicas e comuns e no Incursor de trabalho;
- `conferir_livro.py`, rodado numa cópia para não reescrever o QA do livro, dá 3497 verificações, 384 páginas, 508 links e nenhuma falha, com o mesmo PDF de antes.

## Efeito no jogo

Nenhum. Nenhum custo, requisito, efeito, número ou título mudou. A correção do Revezamento mexe no registro, não no livro.

## Testes negativos

Numa cópia isolada, sem tocar os arquivos reais. A cópia passou antes de cada perturbação, e cada perturbação mudou o arquivo de fato. Saída completa em `perturbacao.txt`.

1. Origens voltando a "desta página": acendem o texto da página 2, a revisão, o bloqueio editorial, os cenários e a auditoria.
2. Aptidões perdendo o link novo: acendem o texto e os links da página 14, a revisão, o bloqueio editorial, os cenários e a auditoria.
3. Inspeção registrando defeito na página 14 de Aptidões: acende "Inspeção sem defeitos".
4. Hash errado no inventário de Origens: o auditor sai com código 1.

## Limites

- A inspeção nova cobre só as 7 páginas mudadas. As outras herdam a inspeção anterior por igualdade de pixel, sem alegar leitura nova.
- Estes PDFs são provas por capítulo. O PDF que vale é o livro completo, e o fechamento da cadeia de evidência dele é o item 2 da fila.
- Os `MANIFESTO.json` dos capítulos, que guardam o hash de cada arquivo da unidade, continuam com os hashes de antes. Isso vale para estes cinco e para os 13 da rodada anterior, e entra no item 2.

## Depois, a pedido do Mizuki

**O auditor de Origens passou a conferir o texto do inventário.** Antes ele só via se cada Legado existia no livro. Agora ganhou 85 checagens, uma por Legado, que comparam o texto inteiro (ignorando espaços). Ele vai de 333 para 418 verificações. Com o inventário de antes da correção, a checagem nova acusa só o Revezamento; o auditor antigo deixa passar. Uma palavra trocada no Faro também acende. Saída em `perturbacao-origens.txt`.

**O validador de PDF compartilhado ficou com ordem fixa.** Ele percorria as remissões de cada página num conjunto do Python, cuja ordem muda a cada execução. Com o mesmo livro, o `CONFERENCIA.json` saía diferente toda vez, e o diff mostrava mudança onde não tinha. Agora percorre em ordem alfabética. Antes do conserto, três sementes davam três arquivos diferentes no Catálogo, no Equipamento e nas Regras gerais; depois, sempre o mesmo. Os `CONFERENCIA.json` dos capítulos do livro foram regravados uma vez nessa ordem, e fora destes cinco só a ordem das checagens mudou.

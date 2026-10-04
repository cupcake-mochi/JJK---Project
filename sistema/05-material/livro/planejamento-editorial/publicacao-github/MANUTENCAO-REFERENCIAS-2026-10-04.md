# Manutenção das referências — 04/10/2026

Item 1 da fila pós-reconstrução. A publicação de 03/10 registrou 166 referências mortas no `conferir-repositorio.py`, na checagem 2 (todo caminho citado em `.md` resolve). Este registro separa defeito real de limitação do verificador, diz o que mudou e guarda o resultado novo.

O relatório antigo, `conferencia-repositorio.txt`, fica como estava: ele é o retrato da publicação. O novo é `conferencia-repositorio-2026-10-04.txt`. A lista completa, referência por referência, está em `DIAGNOSTICO-REFERENCIAS-2026-10-04.json`.

## Primeiro achado: 166 virou 182 sem mudar nada

Num clone limpo do GitHub, com a mesma árvore do merge `75a814d`, a checagem achou **182**, e não 166. A diferença são 16 caminhos `/tmp/...` citados em evidências antigas. Eles ainda existiam na máquina que rodou a conferência de 03/10, então passaram lá.

Ou seja, o resultado dependia do computador. Isso é defeito do verificador: caminho absoluto era procurado no disco da máquina, e não no repositório.

## Diagnóstico das 182

| Grupo | Quantas | O que é | O que foi feito |
|---|---:|---|---|
| Caminho relativo a uma pasta acima do documento | 131 | Limitação do verificador. O planejamento escreve `abertura/lote-01/...` relativo a `planejamento-editorial/` e `manual/40-fundamento.md` relativo a `livro/`, de dentro de subpastas. O arquivo existe e abre. A checagem só tentava a pasta do documento, a raiz e `sistema/`. | Verificador passa a tentar a pasta do documento e cada pasta acima dela até a raiz. |
| Caminho em `/tmp` | 29 | Script ou saída de uma sessão antiga que nunca foi guardada no repositório. Nenhum conserto de caminho traz o arquivo de volta. | Vira aviso, impresso e contado. Fica registrado como **lacuna de rastreabilidade** dessas evidências (lista abaixo). |
| Caminho abreviado ou relativo errado | 14 | Defeito real nos documentos. | Corrigido no texto (lista abaixo). |
| Arquivo local fora do git | 8 | Material que o `.gitignore` exclui de propósito: `finalizado/`, os pacotes de continuidade de 03/10 em entregas, o manual.html do build, os mosaicos PNG e dois PDFs de terceiros. | Vira aviso. O verificador lê os padrões do próprio `.gitignore`; três nomes que o `.gitignore` cobre só pela pasta ou extensão ficam numa lista declarada, com motivo. |

Resultado novo: **0 mortos e 37 avisos**, com os mesmos 1796 caminhos de antes mais os que este registro cita (29 temporários + 8 locais). A checagem 7 continua pulando porque `finalizado/` não vem no clone, e ela diz isso.

## Defeitos reais corrigidos

- `sistema/ESTADO-ATUAL.md`: dez citações começavam em `planejamento-editorial/...` ou `regras-comuns/lote-0N/...`, que não resolvem a partir de `sistema/`. Agora levam o caminho inteiro, `sistema/05-material/livro/planejamento-editorial/...`. Uma delas (`.../equipamento/lote-01`, sem extensão) não era cobrada pela checagem e foi corrigida junto.
- `planejamento-editorial/RETOMADA-PAUSA-2026-10-03.md`: "evidencias/MOSAICOS-ROOT.json" e "migracao-nomes/QA-FECHAMENTO.md" eram relativos a `consolidacao/lote-01/` e o texto não dizia. Agora levam esse prefixo. O conteúdo do registro da pausa não mudou.
- `planejamento-editorial/validacao-editorial/LEIA-ME.md`: citava "evidencias/LOCALIZACAO-EDITORIAL.json" como se fosse um arquivo só, mas cada unidade tem o seu. A frase agora fala do arquivo da pasta de evidências de cada unidade.

## O que mudou no verificador

Só a checagem 2 do `conferir-repositorio.py`:

1. Caminho relativo resolve da pasta do documento ou de qualquer pasta acima dela, até a raiz. `sistema/` continua como tentativa, pelos documentos antigos.
2. Caminho absoluto nunca é procurado no disco. Em `/tmp` vira aviso; fora de `/tmp` continua **falhando**.
3. Caminho que o `.gitignore` exclui vira aviso. Três nomes ficam na constante `LOCAIS`, com motivo.
4. A mensagem deixou de dizer "não existe em lugar nenhum". Agora diz o que foi tentado: "não resolve da pasta do documento nem de nenhuma pasta acima dela", "caminho absoluto fora do repositório" ou "nenhum arquivo da árvore tem esse nome".

Nenhuma checagem foi desligada e nenhuma pasta nova saiu da varredura. Os avisos continuam na saída, com contagem própria.

## Teste negativo

Numa cópia isolada do repositório, sem `.git`. A cópia passou antes de cada perturbação (`rc=0`) e voltou a passar depois. Saída integral em `perturbacao-referencias-2026-10-04.txt`; resumo:

| Perturbação | Esperado | Resultado |
|---|---|---|
| Documento cita "sistema/nao-existe/X.md" | falha | falhou, 1 morto |
| Documento cita "/home/fulano/y.md" | falha | falhou, "caminho absoluto fora do repositório" |
| Documento cita um caminho em /tmp que **existe** na máquina | aviso, sem depender do disco | aviso, `rc=0` |
| Documento cita "finalizado/qualquer.md" | aviso (`.gitignore`) | aviso, `rc=0` |
| Documento em `consolidacao/lote-01/evidencias/` cita "abertura/lote-01/NAO-EXISTE.md" | falha (a regra das pastas acima não aceita arquivo inexistente) | falhou, 1 morto |
| Documento cita o nome solto "NOME-QUE-NAO-EXISTE.md" | falha | falhou, 1 morto |

Contra-teste: o verificador anterior, na mesma cópia, aceitou o `/tmp/...` existente como referência válida. É o comportamento que produzia 166 numa máquina e 182 em outra.

## Lacuna de rastreabilidade que fica

Estas evidências citam scripts ou saídas que só existiram em `/tmp` de alguma sessão. Os números que elas relatam não podem ser reproduzidos a partir do repositório. Os textos não foram alterados, porque são registro histórico. Quem precisar de um desses números como prova tem de refazer a conta.

- `fundamento/lote-01/evidencias/`: `fundamento-compatibilidade.md` (4), `fundamento-maxima.md` (4), `fundamento-revisao-regras.md` (2), `fundamento-maxima-checklist-final.md` (1)
- `regras-comuns/lote-03/evidencias/` (4) e a cópia em `regras-comuns/historico/lote-03-r1/` (2)
- `regras-comuns/lote-04/evidencias/` (3)
- `regras-comuns/historico/lote-02-r1/evidencias/comparacao-matematica.md` (3)
- `origens/lote-01/evidencias/REVISAO-INDEPENDENTE-COMPATIBILIDADE.md` (1) e sua cópia em `consolidacao/lote-01/migracao-nomes/qa-antes/` (1)
- `invocacoes/lote-02/REVISAO-E-FONTES.md` (2, extratos de livros de terceiros)
- `caminhos/incursor/lote-01/RELATORIO-DE-REVISAO.md` (1, PNG de página)
- `piloto-editorial-r2/evidencias/comparacao-fm.md` (1)

## Validadores

Rodados no clone limpo, com `python-docx` instalado: os 27 de `sistema/03-mecanica`, `pac7.py` e `v7.py` saíram com código 0 e nenhuma PULADA. O `conferir-repositorio.py` saiu com código 0, uma checagem pulada (a 7, por falta de `finalizado/`) e 37 avisos.

Isso confere a árvore do repositório. Não diz nada sobre as regras da candidata.

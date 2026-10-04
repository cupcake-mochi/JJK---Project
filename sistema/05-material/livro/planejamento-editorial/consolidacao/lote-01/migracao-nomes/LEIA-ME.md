# Migração de nomes nas fontes candidatas

Foram examinadas as 22 fontes de `ORDEM.json` atribuídas a esta tarefa. Consulta ficou com `/root/maxima`, responsável pelos aliases históricos e pelos novos destinos do índice. A escrita alterou **17 arquivos, 189 blocos e 206 linhas**. Nenhuma fonte publicada ou histórico foi regravado.

## Nomes adotados

| Antes | Depois | Regra preservada |
|---|---|---|
| Incapacitado / Incapacitada | Guarda Aberta | Impede Bloquear e torna críticos os acertos físicos corpo a corpo; conserva ações e Defesa estática. |
| Aviso, Melhoria | Identificar Feitiço | Último feitiço do alvo e sua Classe, obtidos naquele instante. |
| Aviso, Passiva | Leitura de Feitiços | Último feitiço de inimigo à vista, sem conceder ficha ou Classe. |
| Passiva Livre | Expressão da técnica | Manifestação pessoal gratuita, sem benefício funcional ou espaço ocupado. |
| Passiva / Passivas adquiridas | Talento / Talentos | Mesmos efeitos, requisitos, espaços, frequência e custos. |
| Classe Passiva / CP | Categoria de Efeito / CE | Mesma escala 1–3, com requisitos próprios de Talentos, Aptidões e Bênçãos. |

Os usos comuns de “proteção passiva” e “CD passiva” permanecem. Não se trocou “passivo” quando descreve como um efeito funciona. “Talento Próprio”, artigos, pronomes e adjetivos receberam concordância masculina. A expressão cosmética mantém concordância feminina.

## Escopo das evidências

Todas as linhas alteradas foram comparadas com a cópia anterior e lidas em contexto. `MIGRACAO.json` traz antes, depois, contexto, linhas e SHA de cada arquivo. `diffs/` oferece diferenças por unidade. `antes/` preserva as 22 fontes originais.

O auditor `auditar.py` passou por **367 verificações**: mesma sequência de números, estrutura de tabelas, âncoras e destinos de links; nomes aprovados preservados; adjetivos comuns intactos; ausência de CP e rótulos antigos na prosa; concordância nominal e casos semânticos de Guarda Aberta, Leitura de Feitiços e Expressão da técnica. Essa conferência é documental, não teste com leitores.

Os PDFs, hashes de revisão, scripts mecânicos e demais evidências das unidades **não foram atualizados às cegas**. As unidades alteradas precisam de revisão dos deltas, ajuste de verificadores que dependem dos nomes e nova prova visual. Os números idênticos não permitem declarar essas próximas etapas concluídas.

## Correções de remissão autorizadas

- Levanta agora aponta para **Socorro** nas consequências da queda.
- O feito de voltar do estágio 4 de dano na alma aponta para **Derrota e morte**.

Essas duas trocas não alteram os respectivos procedimentos. A proposta de mínimo 1 de Integridade para NPC de vida positiva ficou com a raiz e não foi misturada nesta migração de nomes.

## Nomes mantidos

Incursor, Pugilista e Malabarista conservam a aprovação expressa do usuário. Refino, Lapidação, Classe e Fundamento permanecem. Mão Firme, Reflexo e Sentença Final não possuem duas habilidades distintas na seleção corrente: a antiga lista de colisões misturava remissões, palavras comuns e um exemplo histórico.

A peça `sistema/03-mecanica/11-aptidoes-e-refino.md`, seção 4, declara que sua lista de Mão Firme e outros nomes copia a lista de Passivas do manual. O dono do benefício continua o Catálogo. A nota de dupla propriedade em `DONOS.json` precisa de reconciliação futura, não de invenção de uma nova Aptidão.

## Arquivos alterados

| Fonte | SHA final |
|---|---|
| abertura/lote-01/ABERTURA-E-CRIACAO.md | `33036eda547311f2658bf5e241b1dc0f0483fd99e02d3a5b1225b48838216974` |
| regras-gerais/lote-final/REGRAS-GERAIS.md | `423da38b173df0e05f9b07ce1ba2edc1f69ac928cf2a9709da0c33cb5ed93ee9` |
| dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md | `0e17abe4e79c3ffb2fa1222fb9b03613a725b14bfa9f5c23de994d6bc79d93d3` |
| origens/lote-01/ORIGENS-E-LEGADOS.md | `93300f9489531a3709e28959f673ff7850674218ddacdb734d49643970ce91ae` |
| equipamento/lote-final/EQUIPAMENTO.md | `89a3f7bb705a7c931a3c69f4f051fb98d62acbc065ffa42dc48275f00e2afec1` |
| progressao/lote-01/PROGRESSAO.md | `483925447a9de1d0bc32fa2dfe46af1b079438106881b67ced66f0fefe10e653` |
| fundamento/lote-01/FUNDAMENTO.md | `0160f774f5ea87f4ffd29bb7f7e3335dead51677bf2b894041aa61e2c5041273` |
| catalogo/lote-01/CATALOGO.md | `bf0d8df8707ecfd43c18e9c32c6295e70a8c692c8513b1692d2f53ca5e706b76` |
| aptidoes/lote-01/APTIDOES-E-REFINO.md | `d6135572a93bfd3e07864703889a3ce158dc2a1b59215f5f2fb4a03873459fe0` |
| rotas/lote-01/ROTAS.md | `c7759aebe3c3cb1da8af76d79f802387eb447dddbff7d0585acf535b18397834` |
| ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md | `2e5614e1d6cc519bccc6d264017c960ba97deca89d3f854ae2df81a5182211cd` |
| invocacoes/lote-01/INVOCACOES-EM-CAMPO.md | `297d96084502eb65780b9ed2ac4f7e121a235cfdbb6e41db254f980e55393dcd` |
| invocacoes/lote-02/CONSTRUIR-INVOCACOES.md | `bd3d2cc16b5a6c2b373eba1f0ebfabfbc548bae3d6a7cd2eec6dcbb4bfab95d9` |
| caminhos/guia/lote-01/GUIA.md | `5bf3964d6d8c233069b9f2569fe9487361f9dec0c6473579f594d71c217cca5c` |
| caminhos/emanador/lote-01/EMANADOR.md | `027d4f93d4d59d6674cf3d0ac7f380bd387c367d1e012740b6d25e71b744ba1f` |
| caminhos/evocador/lote-01/EVOCADOR.md | `77e47e82794850bf8e051fab789fe1e6acfa8f545a9b18d41f4f8f4bc8b45083` |
| caminhos/incursor/lote-01/INCURSOR.md | `3705e460791db6ae03b79eb2f7b25d13936a1c1ab54ddba616fa3872407f09f1` |

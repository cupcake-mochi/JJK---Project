# Grupo, arquivo e pó — registro 123

29 de outubro de 2026. Lote B2-05 da etapa 6: três cópias revistas em duas passagens, com originais preservados. Antes de começar, conferi a pasta: o último trabalho era o registro 122.

[Prova em PDF](apoio-revisao-textual-123/output/pdf/Ciclo-Maldito-Grupo-Arquivo-e-Po-Revisao-Textual.pdf) · [HTML](apoio-revisao-textual-123/prova-textual.html) · [Índice atual](apoio-revisao-textual-123/casos-completos.html) · [Fila atual](apoio-revisao-textual-123/fila-dos-casos.md).

## O que mudou

**Haru, Vigia e Tessa.** As remissões usam o nome atual da consulta revista, *Inimigos de níveis mais altos*. Prende tem sujeito explícito: quem falha não se desloca até o fim do próprio turno seguinte, mas ainda ataca e conjura. O texto também deixa claro que anunciar a faixa não gasta ação, que Leitura de Reservas revela os PE atuais e que as contas de uso descrevem uma única reserva.

**Correção de regra, documentada.** O golpe desarmado de Tessa aparecia como **1d4 + 2d4**, crítico **2d4 + 2d4**. No Livro de Regras 1.0, o dado desarmado é d4 com Maestria 1 e **d6 com Maestria 2**. Tessa tem Maestria 2 e Força 0, então o golpe passa a **1d6 + 2d4**, crítico **2d6 + 2d4**. Os 2d4 de Canalizar do Refino 4 continuam iguais. A comparação numérica do confronto não usa esse golpe, então nenhuma tabela muda. O original e o PDF integrado anterior conservam o texto antigo até a integração.

**Disputa pelo arquivo.** A tabela de posições dizia que o painel estava "fixado na parede junto de C12". Pelo mesmo texto, porém, todas as colunas passam livres para a linha 13, então não há parede ali. Na cópia, o painel fica **num suporte junto de C12, sem bloquear a área de passagem**. Acesso, células e regras ficam iguais. A comparação numérica agora explica por que suas porcentagens diferem das da consulta de níveis mais altos: as duas usam Defesas diferentes. No exemplo de socorro, Mei, Akira e Bao são identificados como perfis de referência de nível 15, para não serem confundidos com os personagens de nível 6 dos outros casos.

**O pó na sala de conservação.** Os nomes das consultas foram atualizados. A remissão aos perfis aponta para a seção dos personagens no ensaio do Sineiro. A alternativa de Aguentar diz o que muda: Mei não poderia sair sozinha e precisaria ser transportada ou atendida no lugar.

## Leituras, números e regras

A primeira passagem leu integralmente as três fontes e as regras citadas. Criou as cópias e fez 32 ajustes de clareza, além da correção do golpe desarmado e da posição do painel. A segunda leu as catorze páginas da primeira prova e fez 4 ajustes de pente fino, dois deles sobre frases da própria primeira passagem. Não houve terceira leitura integral independente nem leitura de pessoa externa.

O [registro de alterações](apoio-revisao-textual-123/alteracoes.json) reproduz as cópias a partir dos originais. A conferência exige a mesma sequência de números visíveis, com duas trocas permitidas e declaradas (d4 → d6 no golpe de Tessa). As células de tabela também precisam ser as mesmas, com uma única exceção declarada: a célula do painel.

As [37 contas dirigidas](apoio-revisao-textual-123/contas-conferidas.json) refazem TRs, perícias, CDs, Defesa, montagens, custos por estágio de Integridade, faixas exatas dos estágios, objetos, socorro e o exemplo do pó. As médias de dano da Fita foram recalculadas exatamente e conferem, inclusive o 14,38 com Cobrir-se. As porcentagens de composição, a sobrevivência de Tessa e a tabela "Queda não é derrota" foram comparadas com os resultados guardados no apoio-lote7, e todas conferem. O script antigo não foi executado, porque grava arquivos.

Foram consultados no Livro de Regras 1.0: atributos das perícias, dado desarmado por Maestria, Canalizar por Refino, Cobrir-se, Kokusen, Prende, Defesa e vida de objetos, Nem Um Arranhão, Duro de Matar, vida a zero e socorro, Integridade, Envenenado, condições Pesadas, Concentração, visão em fumaça leve e corpos amaldiçoados.

Não houve simulação nova, parâmetro novo de inimigo, mecânica de treinamento ou detalhamento de Reserva Condensada. As fichas e o perigo continuam experimentais. Contas corretas não demonstram equilíbrio.

## Mapas e diagramação

A prova tem **14 páginas**, no mesmo padrão: duas colunas, Spectral 10,25/13,2 pt, margens de 19 mm e intervalo de 7 mm. Tabelas usam 9,2/11,5 pt; quadros largos e mapas ocupam a largura da página.

O desenho vetorial do s079 em `MAPAS.py` foi conferido contra o caso: sala de 3 × 18 m, pó em A1–B12, fecho e pino junto de A12, Mei em A0 e Akira em B0. Corresponde ao texto e substitui, na prova, o esquema em caracteres. Na primeira prova, o mapa ficava depois da tabela de posições, não cabia e deixava meia página vazia. Também deixava vazio um terço da página quando posto no fim da seção de preparo. Por isso, ficou logo depois do primeiro parágrafo do caso. O s102 só tinha uma tabela de posições. Foi feito um vetor no mesmo estilo, com as duas versões lado a lado, porque o texto pede escolher uma antes da sessão. O `MAPAS.py` não foi alterado. [Escolhas e origem](apoio-revisao-textual-123/mapas-selecionados.json).

Todas as páginas foram inspecionadas. As páginas 10–14 foram vistas de novo depois de reposicionar o mapa; o pente fino não mexeu no s079, e essas páginas são idênticas byte a byte às vistas. Das páginas que o pente fino alterou, a 4 e a 8 foram vistas de novo; as demais são idênticas às da primeira prova. Os hashes estão registrados. Sobram espaços no fim de cada caso, nas páginas 4 e 9, e um pequeno vazio antes de "Queda não é derrota", na página 8. Eles serão reavaliados na integração. Esta prova não conclui a revisão visual global.

## Continuidade

O índice mantém os 59 casos, agora com **30 cópias revistas**. Restam **29 casos em 7 lotes**, além das **17 consultas complementares**. Os dez controles apontam para este registro e para a fila vigente.

A consulta revista *Inimigos de níveis mais altos* (registro 119) ainda aponta para as fontes originais de Haru e do arquivo. Ela não foi alterada neste lote; a integração deve trocar essas remissões.

[Conferência documental](apoio-revisao-textual-123/conferencias.json), [leituras por caso](apoio-revisao-textual-123/leitura-por-caso.json), [inspeção visual](apoio-revisao-textual-123/revisao-final.json) e [destinos em dados](apoio-revisao-textual-123/destinos-e-fontes.json) registram o escopo. O manifesto é atualizado por união depois de conferir as entradas anteriores.

As 104 fontes originais, a base técnica, as provas anteriores e a edição integrada de 357 páginas permanecem preservadas. Sem envio ao GitHub e sem substituição do PDF integrado.

## Próxima tarefa

**B2-06 — Doença e fichas preenchidas (s103, s077, s068). Claude Opus 5.5, esforço alto** (o equivalente indicado no plano é GPT-6.1 Sol, alto). Duas passagens nas cópias, conferência das regras e inspeção de cada página. Depois dos lotes e consultas, ainda faltam a conferência do conjunto, a integração, a revisão visual global e a comparação final com os livros de referência.

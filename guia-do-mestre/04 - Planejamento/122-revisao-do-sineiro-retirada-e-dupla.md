# Sineiro, retirada e dupla — registro 122

29 de outubro de 2026. Lote B2-04 da etapa 6: quatro cópias revistas em duas passagens, com originais preservados. Antes de começar, a pasta foi conferida: não havia registro 122 nem arquivo posterior ao 121, além do prompt de retomada e do manifesto.

[Prova em PDF](apoio-revisao-textual-122/output/pdf/Ciclo-Maldito-Sineiro-Retirada-e-Dupla-Revisao-Textual.pdf) · [HTML](apoio-revisao-textual-122/prova-textual.html) · [Índice atual](apoio-revisao-textual-122/casos-completos.html) · [Fila atual](apoio-revisao-textual-122/fila-dos-casos.md).

## O que mudou

**Sineiro: ficha após a Doma.** A abertura diz o que o jogador vai receber e o que não passa da ficha do confronto. A CD da Doma usa o nome do Livro de Regras 1.0 (CD de conjuração, pela técnica, Manejo ou Kata), e o resultado do TR está em frases completas. A destruição ganhou um exemplo marcado. "Reação coletiva" substitui "coletiva de Reação". A exposição depois de Dobrar o sino deixa claro que os ataques ainda precisam acertar.

**Correção de regra, documentada.** A cópia dizia que religar o Sineiro domado custa **Bônus e 2 PE**, igual à entrada. No Livro de Regras 1.0, religar usa o retorno, que custa **o dobro do PE da entrada**. A entrada do Sineiro, de nível 6, custa 2 PE, porque a maior Classe permitida nesse nível é 2. Religar passa a custar **4 PE**, e a frase "os custos coincidem neste nível" saiu. O Carregador, de nível 2, já estava certo, com 1 e 2 PE. Esta é a única mudança de número do lote. O original e o PDF integrado anterior conservam o texto antigo até a integração.

**Retirar a caixa, proteger a equipe.** Termos alinhados à ficha revista do Sineiro: *arrastar* a presa, *preparação* interrompida ao mudar de posição, dano que sozinho não interrompe. Três frases ambíguas ficaram com sujeito explícito: de quem são os ataques com vantagem pela provocação, de quem é a Reação gasta na abertura de Akira e o que acaba no começo da rodada 2. O título da rodada 3 passou a "todos saem", porque o Sineiro continua ativo. A comparação com "seis feitiços do planejamento" agora aponta para a revisão numérica do Sineiro.

**Ren e Sora.** A remissão usa o nome atual da consulta revista, *Escolher os números de um inimigo*. A explicação da montagem de Fio de impulso foi posta na ordem certa. Leitura de Reservas, Kokusen e a derrota estão escritos de forma mais direta. Tabelas e números foram preservados.

**Escolher quem enfrentar primeiro.** A remissão aos perfis aponta para a seção dos personagens no ensaio do Sineiro. Executar diz o que concede no momento em que é preparado. Sora tem 1 PE no fim da rodada 2; o texto agora diz que esse saldo não basta para Cobrir-se, em vez de dizer que ela não tinha PE.

## Leituras, números e regras

A primeira passagem leu integralmente as quatro fontes e as regras que elas citam, criou as cópias e fez 70 ajustes de clareza, mais a correção de religar. A segunda leu as dezessete páginas da primeira prova completa e fez 12 ajustes de pente fino, alguns deles sobre frases da própria primeira passagem. Não houve terceira leitura integral independente nem leitura de pessoa externa.

O [registro de alterações](apoio-revisao-textual-122/alteracoes.json) reproduz as cópias a partir dos originais. A conferência exige a mesma sequência de números visíveis, com uma única troca permitida e declarada (2 → 4, religar), e as mesmas células de tabela.

As [63 contas dirigidas](apoio-revisao-textual-122/contas-conferidas.json) refazem vida e Integridade da construção, destruição na Doma, montagens, custos de entrada e de religar, distâncias de cada percurso, zonas de 3 m, dados, vida, PE, tratamento de Insistir e Aguentar, estágios exatos de Integridade de Ren e Sora, perícias e TRs. As probabilidades do confronto (23,9% e 4,5%) e as médias de dano (7,39 → 10,12; 3,86 → 5,28; 2,38) foram recalculadas por convolução exata, nas condições escritas no texto, e conferem. Foram consultados no Livro de Regras 1.0: recursos do turno e conversão de ações, Correr, Desengajar, Provocar, Olhos Em Mim, vida a zero e socorro, Integridade, Cobrir-se, Canalizar, Kokusen, Abrir Caminho, atributos das perícias, Invocações em campo, Domar uma maldição, Carregar, Recuo e Escolher.

Não houve simulação de combate, parâmetro novo de inimigo, mecânica de treinamento ou detalhamento de Reserva Condensada. As quatro fichas continuam experimentais. Contas corretas não demonstram equilíbrio.

## Mapas e diagramação

A prova tem **17 páginas**, duas colunas, Spectral 10,25/13,2 pt, margens de 19 mm e intervalo de 7 mm. Tabelas usam 9,2/11,5 pt; quadros largos e mapas ocupam a largura da página.

O mapa de referência `mapa-vetorial-4.png` foi conferido contra o ensaio: Rina C0, Mei D0, Akira F0, caixa C6, Sineiro em D6–E7, recinto 12 × 18 m e porta C–F. Corresponde ao texto e foi exportado do desenho vetorial existente, com a altura do próprio desenho. O confronto de Ren e Sora usa o mesmo recinto com outras posições e não tinha desenho. Foi feito um vetor no mesmo estilo e grade, só com as posições da tabela do caso; o `MAPAS.py` não foi alterado. As fichas da Doma e da dupla não têm posições e não receberam mapa. [Escolhas e origem](apoio-revisao-textual-122/mapas-selecionados.json).

Todas as páginas foram inspecionadas na primeira prova. Depois do pente fino, as nove páginas que mudaram foram vistas de novo; as outras oito são idênticas byte a byte às já inspecionadas, conforme os hashes registrados. Os espaços que restam ficam no fim de cada caso, antes da quebra de página entre consultas (páginas 4, 9 e 13). Eles serão reavaliados na integração. Esta prova não conclui a revisão visual global nem demonstra paridade do livro completo com as referências.

## Continuidade

O índice mantém os 59 casos, agora com **27 cópias revistas**. Restam **32 casos em 8 lotes**, além das **17 consultas complementares**. Os dez controles apontam para este registro e para a fila vigente.

A ficha revista do Sineiro (registro 121) ainda aponta para a Doma e o ensaio originais. Ela não foi alterada neste lote, porque é uma entrega encerrada; a integração deve trocar essas remissões pelas cópias revistas.

[Conferência documental](apoio-revisao-textual-122/conferencias.json), [leituras por caso](apoio-revisao-textual-122/leitura-por-caso.json), [inspeção visual](apoio-revisao-textual-122/revisao-final.json) e [destinos em dados](apoio-revisao-textual-122/destinos-e-fontes.json) registram o escopo. O manifesto é atualizado por união depois de conferir as entradas anteriores.

As 104 fontes originais, a base técnica, as provas anteriores e a edição integrada de 357 páginas permanecem preservadas. Sem envio ao GitHub e sem substituição do PDF integrado.

## Próxima tarefa

**B2-05 — Grupo, arquivo e pó (s101, s102, s079). Claude Opus 5.5, esforço alto** (o equivalente indicado no plano é GPT-6.1 Sol, alto). Duas passagens nas cópias, conferência das regras e inspeção de cada página. Depois dos lotes e consultas, ainda faltam a conferência do conjunto, a integração, a revisão visual global e a comparação final com os livros de referência.

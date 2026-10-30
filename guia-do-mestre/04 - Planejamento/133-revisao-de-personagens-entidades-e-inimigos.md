# Personagens, entidades e inimigos — registro 133

30 de outubro de 2026. Terceiro lote das consultas complementares (C-03): cinco fichas e registros revistos em duas passagens, com originais preservados. Antes de começar, a pasta foi conferida: o último trabalho era o registro 132.

[Prova em PDF](apoio-revisao-textual-133/output/pdf/Ciclo-Maldito-Personagens-Entidades-e-Inimigos-Revisao-Textual.pdf) · [HTML](apoio-revisao-textual-133/prova-textual.html) · [Índice atual](apoio-revisao-textual-133/casos-completos.html) · [Fila atual](apoio-revisao-textual-133/fila-dos-casos.md).

O lote cobre o registro de dedicação por ficha, o registro de Pactos e Promessas, o registro de aquisição e estado de entidade, a ficha de inimigo e encontro e a conferência de habilidade de inimigo. As cópias ficam em `revisao-98/consultas/`.

## O que mudou

**Remissões para a estrutura nova.** Pelo mapa de destinos do registro 99:
- "Atividades e tempo entre missões" agora aponta para **Tempo para as atividades**, em Entre missões (8.2).
- "Pactos e Promessas" agora aponta para o capítulo **Pactos e entidades**.
- O "método principal" da ficha de inimigo agora aponta para o capítulo **Inimigos e perigos**.
- Os casos citados apontam para as cópias revistas. São 15: Promessa do arquivo, sete de entidades (tempo, reconstrução, Cão de sombra, Amontoado, Escriba, Mula, Vigia), Ren e Sora, perigos ambientais, sala de conservação, chefes, montar habilidades e os dois do Carregador (corredor, consulta e Doma).
- O registro de estado e socorro, revisto no C-01, e as duas fichas de inimigo apontam uma para a outra dentro de `consultas/`.

**Clareza.** São 4 ajustes:
- a dedicação separa a concessão (28 horas novas a cada sete dias) da validade do saldo ("o que sobrar das horas novas de um ciclo vale só no ciclo seguinte");
- a entrada proporcional diz de onde vem o 4 da conta: "a quatro horas por dia";
- a ficha de inimigo indica a ordem de uso: preparar o encontro e, depois, registrar o resultado;
- a conferência de habilidade chamava a mesma ficha de "ficha única" e de "ficha de construção e encontro"; ficou o título dela, ficha de inimigo e encontro.

Nenhum campo, número ou regra mudou.

**Prova.** As linhas de preenchimento ficam nos campos da dedicação e da ficha de inimigo. Os registros de Pactos e de entidade e a conferência de habilidade são quadros de orientação; esses ficaram sem linhas. Campos que vinham unidos por quebra de linha foram separados na prova, cada um com suas linhas. A lista "Antes de jogar" ganhou caixas de marcar, e o quadro de perguntas da conferência de habilidade ocupa a largura toda.

## Leituras, números e regras

A primeira passagem leu integralmente as cinco fontes e as regras citadas. A segunda leu a prova completa, conferiu os trechos alterados no contexto e varreu o texto; não encontrou nada para mudar.

O [registro de alterações](apoio-revisao-textual-133/alteracoes.json) reproduz as cópias a partir dos originais. A conferência exige a mesma sequência de números visíveis e as mesmas células de tabela, sem exceção.

O [script de contas](apoio-revisao-textual-133/contas-conferidas.json) faz 20 conferências:
- **Dedicação:** refaz os seis ciclos de Rina e Mei pela regra (gaste antes as horas antigas; só passa a parte livre das novas) e confere cada linha da tabela, o saldo que passa de um ciclo ao outro, as aberturas de 38 e 56 horas, a entrada no quinto dia (12 horas) e a conferência pendente (10 + 8 + 10 = 28). As 28 horas são o padrão recomendado do guia, em Entre missões, não regra do Livro de Regras 1.0.
- **Overtime:** 8 horas a 2,5% dão 20%; máximo 40 vira 32 e 48; a passagem rende 16 PE e leva 12 a 28. Essência 4 dá duas vagas.
- **Calígrafa:** CD 8 + 4 + 2 − 2 = 12, teste d20 + 6, um 6 basta, igual ao livro.
- **Agarrar do Carregador:** CD 8 + Força 3 + maestria 1 = 12, igual ao exemplo de Rina no livro. Escapar usa a mesma CD, o estágio 2 de Integridade só encarece feitiços e o estágio 3 dá desvantagem nos ataques e TRs de quem está nele.

## Diagramação

A prova tem **11 páginas**. Todas foram inspecionadas depois dos ajustes, e o PDF final é idêntico byte a byte ao inspecionado. Há um espaço de fechamento no pé da página 3, antes do exemplo do Overtime.

## Continuidade

Os 59 casos continuam revistos. Das 17 consultas complementares, **15 estão revistas e 2 pendentes**, no lote C-04. Os dez controles apontam para este registro. O guia das consultas (Escolher uma folha para a mesa) aponta para as cópias revistas destas fichas.

**Para a integração:**
- O exemplo da dedicação usa Rina e Mei como duas fichas da mesma pessoa, como em Entre missões; nos casos, esses nomes são personagens diferentes. Vale entrar na decisão pendente sobre renomear os exemplos.
- Os registros de Pactos e de entidade trazem a orientação dentro da coluna "Registro". Se forem impressos para preencher, precisam de uma coluna livre.

[Conferência documental](apoio-revisao-textual-133/conferencias.json), [leituras](apoio-revisao-textual-133/leitura-por-caso.json), [inspeção visual](apoio-revisao-textual-133/revisao-final.json) e [destinos em dados](apoio-revisao-textual-133/destinos-e-fontes.json) registram o escopo. O manifesto é atualizado por união depois de conferir as entradas anteriores.

As 104 fontes originais, a base técnica, as provas anteriores e a edição integrada de 357 páginas permanecem preservadas. Sem envio ao GitHub e sem substituição do PDF integrado.

## Próxima tarefa

**C-04 — Mundo e obra (s088, s087). Claude Opus 5.5, esforço alto** (equivalente no plano: GPT-6.1 Sol, alto). Depois: conferência do conjunto, integração, revisão visual global e comparação final com os livros de referência.

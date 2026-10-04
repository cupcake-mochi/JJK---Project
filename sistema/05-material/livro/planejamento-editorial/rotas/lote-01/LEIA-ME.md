# Rotas de criação — lote 01

Candidata para substituir os capítulos de Técnica Marcial, Sem Técnica e Bênçãos e Lapidação. O texto está em `ROTAS.md`. Nenhuma dessas fontes publicadas foi alterada por este lote.

O manuscrito apresenta as escolhas das rotas, todos os benefícios de seus catálogos, cinco aplicações completas e a criação de Bênção Própria. A montagem comum continua em Fundamento. Formas, Melhorias, Restrições e limites não recebem uma segunda tabela aqui.

## Revisão

- `ALTERACOES.md` e `ALTERACOES.json`: antes, depois, motivo e localização das fontes. Mudanças mecânicas estão identificadas.
- `INVENTARIO.json`: destino de cada seção dos três capítulos, incluindo Pétala e Espinho recuperados da peça vigente.
- `INTERFACES.md`: regras que dependem de outras partes da edição.
- `REVISAO-E-FONTES.md`: leitura dirigida, comparação editorial e limites da validação.
- `evidencias/CASOS.json`: cenários positivos e negativos analisados pelo modelo.
- `evidencias/REVISAO-EDITORIAL.json`: avaliação contextual de cada página lógica.

Execute `python3 auditar.py` nesta pasta para reproduzir as conferências estruturais e numéricas. A auditoria lê as tabelas atuais de Fundamento e de Canalizar. Se a estrutura de uma tabela mudar, o programa interrompe a leitura em vez de usar números de reserva.

O programa produz `AUDITORIA.json` e `evidencias/auditoria-numerica.json`. Ele confere contas dos exemplos, progressão de Lapidação, curva de Estímulo e comparações delimitadas de Presilha e Assombro. **Essas contas não comprovam equilíbrio global.**

## Estado da entrega

A fonte tem marcadores de páginas planejadas. A quantidade e o aspecto das páginas exportadas devem ser conferidos no PDF gerado pela coordenação. Resultados de renderização, revisão independente e inspeção visual ficam em `evidencias` quando concluídos.

As revisões descritas aqui foram realizadas por modelos. Não houve playtest, teste de tempo de consulta ou avaliação com jogadores humanos. A revisão de Morrendo e Integridade e a revisão global de nomes permanecem na fila.


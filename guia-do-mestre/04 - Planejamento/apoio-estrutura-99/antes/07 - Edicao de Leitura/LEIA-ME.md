# Guia do Mestre — edição de leitura

**Atualização vigente — registro 93, 26/10/2026:** capítulo 1 revisado; PDF com 359 páginas, inspeção de todas as páginas após a repaginação. Próxima tarefa: capítulo 2, GPT-6.1 Sol, esforço alto. Consulte o [relatório da revisão](<../04 - Planejamento/93-revisao-editorial-do-capitulo-1.md>). As descrições anteriores registram a entrega 92.

Abra [index.html](index.html) no navegador. A edição funciona localmente, com capítulos, busca e consultas. Mantenha a pasta completa: estilos, busca e páginas são arquivos separados.

Para editar o texto, use as fontes numeradas da pasta `06 - Redacao do Guia`. O [manuscrito completo em Markdown](GUIA-DO-MESTRE-PRE-1.0.md) é uma cópia editável organizada; correções que devam persistir precisam ser aplicadas também à fonte antes de regenerar.

`GERAR-EDICAO.py` organiza novamente as fontes e registra o resultado no [mapa editorial](mapa-editorial.json). Ele requer Python3 com Markdown e BeautifulSoup, disponíveis no ambiente usado nesta entrega. A leitura emHTML não depende de Python, internet ou instalação de bibliotecas.

Os casos da obra com revelações têm página separada e ficam fora da busca e do manuscrito principal. Os dois estudos antigos de chefe permanecem na produção. [Fontes e limites](fontes-e-limites.html) explicam o alcance dos casos e as referências locais.

Para registrar retorno, copie o [modelo de observação](COMENTAR-LEITURA.md). Esta é a **pré-1.0 — revisão de leitura 2**, acompanhada pelo [PDF diagramado](<../08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf>). O [registro92](<../04 - Planejamento/92-revisao-critica-e-edicao-diagramada.md>) documenta a revisão e seus limites.

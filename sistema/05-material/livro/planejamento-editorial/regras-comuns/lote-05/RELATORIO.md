# Revisão da proposta 5: energia e vestígios

03/10/2026. [Texto atual](05-ENERGIA-E-VESTIGIOS.md), [PDF de leitura](output/pdf/Projeto-M-Energia-e-Vestigios-Proposta-05.pdf) e [decisões E01–E14](05-DECISOES.md). Complemento candidato à v0.331; não integrado.

## Resultado

A unidade apresenta busca energética local, pressão como pista de cena, análise de uma fonte observada e uso de vestígios. Reutiliza Vasculhar, Estudar, Investigação e Sobrevivência. Mantém os benefícios próprios de Caminhos, entidades, Legados, Bênçãos, ferramentas e Fundamento.

O alcance de 18 m é novo e permanece **de ensaio**. A busca usa Padrão, não custa PE, pode localizar sem conceder visão e não atravessa obstáculos sólidos que isolem a fonte. Não cria uma segunda oposição passiva para Esconder nem renova Furtividade. A pressão de cena não se torna uma varredura repetível do prédio.

## Correções produzidas pela revisão

- A redação inicial permitia interpretar a aura acessível como acompanhamento contínuo. A leitura agora é expressamente instantânea; posição futura depende de outra fonte de informação ou busca.
- Foi retirado um requisito novo de pista física prévia em Sentido Treinado, que restringia a substituição comprada.
- Interferência e Furtividade usam a maior CD, com um dado; não se somam.
- Antena pode resolver a parte falha do pedido sem apagar descobertas, oferecer alvos ocultos gratuitamente ou repetir um sucesso completo só por precaução.
- Equipamento carregado não ganha supressão por estar em estojo rígido; Cortina remete à ocultação específica do texto publicado.
- Gastar o último PE não equivale à característica de não possuir energia.

Os [pareceres mecânicos](evidencias/revisao-mecanica-r1.md) e de [leitura](evidencias/revisao-leitura-r1.md) contêm o retrato inicial e uma releitura vinculada ao hash final. Após as correções, os dois revisores não identificaram bloqueador restante nos casos examinados.

## Evidências e alcance

[33 cenários documentais](evidencias/CENARIOS.md) conferem ações antes/depois, informação, barreiras, rerrolagem, visibilidade e interações. Incluem a entidade que usa Vasculhar com seus próprios meios e comunica o resultado, e Atuação Complementar do Evocador. São permissões existentes com custo próprio, não busca gratuita universal ou compartilhamento automático de visão.

As [contas exatas](evidencias/deteccao-contas.md) condicionam a busca ao sucesso anterior de Esconder e incluem treino/especialização nos bônus dos perfis. Com bônus +4 de Furtividade, Percepção e Sentir, a busca encontra 30% dos personagens que conseguiram esconder-se; com Antena, 48,5%. Isso não é a chance contra uma CD fixa nem uma simulação de combate completo. Uma segunda CD passiva indevida reduziria Esconder em 40 pontos percentuais nos dois perfis com Sentir +12 e Percepção +4.

A [pesquisa primária](evidencias/pesquisa-primaria.md) compara D&D 2024 e Pathfinder, sem copiar a redação ou adotar seus custos por semelhança. O perfil oficial de Toji confirma energia zero; a pesquisa pública não certificou uma regra universal de resíduos ou distância em Jujutsu. Os procedimentos métricos deste lote são design do Projeto M.

O [verificador](conferir.py) confere texto do PDF, páginas, quatro marcadores, fontes incorporadas, geometria, exemplos, medidas, links e preservação das fontes publicadas e dos lotes anteriores. Os resultados ficam em [CONFERENCIA.json](CONFERENCIA.json). Guardas de texto são somente proteção contra perda acidental de cláusulas.

As quatro páginas finais foram renderizadas e examinadas visualmente. Títulos, tabelas, exemplos e rodapés ficaram legíveis e sem cortes encontrados; paleta e fontes seguem as amostras anteriores. Não há ilustração gerada por IA. A inspeção está vinculada ao hash do PDF em `evidencias/inspecao-visual.json`.

## O que ainda precisa de decisão ou prova

Não houve teste humano de compreensão nem playtest de equilíbrio. As cinco tarefas de leitor foram executadas por um agente como revisão documental. A enumeração de d20 não valida 18 m, a utilidade de cada informação ou o equilíbrio global da classe que a usa.

Antes da integração, conciliar o alcance e as convenções propostas; atualizar os donos de ações/perícias, exemplos de Antena/Faro/Máscara, introdução de Refino e remissões. O alcance próprio de Presságio continua sem número publicado; não foi substituído pelo alcance da busca. Origens e fichas externas devem ser recebidas e conciliadas, não sobrescritas.

A etapa seguinte é consolidar os procedimentos comuns em uma prova contínua de leitura, verificando sua sequência e referências, antes da revisão ampla das exceções e da nova abertura. O livro publicado e as candidatas anteriores foram preservados.

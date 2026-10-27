# Confronto com objetivo e pressão ambiental

25 de outubro de 2026. Continuação autorizada por Mizuki após a recuperação das entregas 66/67. Entregas: [seção 65 — Comparar confronto e pressão ambiental](<../06 - Redacao do Guia/65-comparar-confronto-e-pressao-ambiental.md>) e [seção 66 — O Carregador e a saída que fecha](<../06 - Redacao do Guia/66-o-carregador-e-a-saida-que-fecha.md>). Método e variante de cenário; sem nova escolha autoral de números, curva de dificuldade ou economia de inimigos.

## Estado inicial e preservação

Os **232 arquivos** do manifesto de produção estavam presentes e com SHA-256 correspondente. A produção foi retomada na pasta Linux `/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/`; os caminhos Windows nos registros 66/67 documentam o ambiente usado naquelas entregas. A cópia da R53 incluída em `apoio-carregador/fontes` e o original local têm o mesmo hash `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

Estado inicial e cópias dos oito registros alterados preservados em [apoio-composicao-carregador](apoio-composicao-carregador/estado-inicial.json), com histórico em `historico/antes-da-composicao/`. O registro 06, a base do piloto, os protótipos, as seções 62–64 e os apoios anteriores não foram reescritos. A ferramenta atual `CONFERIR-SALVAMENTO.py` foi usada somente para leitura; os verificadores históricos que regeneram manifestos não foram executados.

## Escolha de composição

A variante conserva o Carregador de 32 PV/16 Integridade/0 PE, suas ações e sua Doma. Altera a saída, sem acrescentar dano ambiental ou entregar ações de chefe. O fechamento de um portão pode alongar o percurso até o pátio de 6 para 18 m; um corredor de serviço permanece acessível.

Não foi somada a passarela à criatura: o caso 67 permanece um perigo separado, com seus próprios apoios e queda. Seu método de sinalizar o prazo e separar interrupção de encerramento foi aplicado a outro dispositivo, com consequência diferente. A duração local de três rodadas continua uma proposta, não uma regra aprovada por sua repetição em dois exemplos.

São comparadas três referências: encontro original; novo mapa com motor desligado; novo mapa com fechamento ativo. A referência intermediária impede atribuir ao relógio uma mudança causada pelo corredor adicional. A ampliação do espaço também pode favorecer o grupo ou mudar a perseguição.

| Escolha do exemplo | Função e estatuto |
|---|---|
| Mesmo corpo e capacidades do inimigo | Evita alterar ficha, mapa e ritmo simultaneamente. Não revalida os números experimentais. |
| Saída curta 6 m e serviço 18 m | O fechamento muda acesso e custo de retirada, preservando saída. Medidas locais declaradas. |
| Parada a 12 m da abertura / 6 m do trabalho | Produz custo de posicionamento e de Padrão, com intervenção possível já na primeira rodada. |
| Marcador 0–3; fase única ao fim da rodada | Prazo explícito, independente da quantidade de participantes. Convenção local de abertura e resolução. |
| Sensor por corpo sólido ou objeto de pelo menos 1 Volume | Permite manter o vão aberto por posição ou objeto. Propriedade proposta deste dispositivo, sem dano de esmagamento. |
| Espera no estado 3; nova tentativa no próximo fim de rodada | Evita fechamento instantâneo entre ações quando alguém sai da faixa. |
| Comando madeira/objeto de mão resistente, Defesa14/PV10 | Escolha de material e porte aplicada à tabela publicada. Destruição para o motor, sem reabrir o portão. |
| Folha metálica/objeto maior resistente, Defesa18/PV40 | Outro alvo possível; a zero libera a passagem conforme o cenário. Não é preço de dificuldade nem dano adicional. |
| Doma sem portão ou controle ambiental | O dispositivo pertence ao cenário. Aquisição conserva apenas a ficha preparada da entidade. |

O grupo pode resolver a pressão rapidamente ou escolher a rota longa. Não foram acrescentadas imunidades, inimigos ou uma segunda contagem para impedir soluções válidas. A variante não promete exigir três rodadas de combate.

## Fonte primária consultada

[Livro do Jogador R53](apoio-carregador/fontes/LIVRO-COMPLETO-R53.md):

| Trecho | Aplicação |
|---|---|
| Turnos, Conversão de ações e Ações | Movimento/Bônus/Padrão separados; Correr e Desengajar competem pela Padrão; Reação não volta a cada rodada. |
| Preparar | Padrão na preparação, Reação depois do gatilho, prazo até começo do próximo turno; deslocamento preparado não retrocede o fechamento. |
| Reações e ataques de oportunidade | Movimento do transportador pode provocar; vítima arrastada não provoca pelo movimento imposto. |
| Agarrar e Escapar de uma contenção | O portão não oferece soltura ou Agarrar gratuito; ação de fuga continua distinta de Desengajar. |
| Movimento e terreno; Carga; Arrastar e transportar | Distâncias, custos por trecho, Volume exato, apoios, passagem, conversões e ausência de saldo de movimento entre turnos. |
| Danificar objetos; Vida do objeto; Objetos e efeitos | Defesas14/18, vidas10/40, dano acumulado, alvo/material, zero e ausência de Bloquear nos objetos. |
| Vida a zero, Socorro, Derrota | Separação entre fim da oposição, fim da pressão e retirada; atendimento não é pausado. |
| Invocações em campo e ficha do Carregador domado | Ação do invocador não vira ação adicional da entidade; cenário não vira talento adquirido. |

A leitura foi dirigida aos procedimentos usados. Não houve pesquisa externa nova, afirmação sobre engenharia real, auditoria do acervo do Claude ou importação de números de outro sistema. A escrita segue a skill local de redação acessível já aplicada ao projeto: regra, exemplo, custos completos e distinção entre base e proposta.

## Conferências

O [programa de conferência](apoio-composicao-carregador/conferir.py) é somente de leitura e não regenera manifestos. Lê os parâmetros da [comparação](apoio-composicao-carregador/dados-comparacao.json) e da base do Carregador; os [resultados](apoio-composicao-carregador/resultados.json) registram **41 casos determinísticos**. Não simula ataques, fichas completas de jogadores, escolhas humanas ou um confronto inteiro.

| Recorte | Resultado |
|---|---|
| C → A aberto / fechado | Andar6/18; arrastar12/36. Retorno A → C continua possível pelo serviço. |
| A → P | 12m; dois Movimentos de9 deixam6m e conservam Padrão para operar. Pode voltar até C depois, sem ataque adicional. |
| Socorrista Força2, itens1; corpo72kg e itens2 | Total9, dentro do teto de arrasto14. Não é carregamento erguido sem penalidade. |
| C → A arrastando, orçamento18 e Padrão reservada | Um turno pelo atalho; dois pelo serviço, sem outra interferência. |
| Mesmo recorte com estágio2, orçamento9 | Dois turnos pelo atalho; quatro pelo serviço. |
| Recuo → C → A arrastando pelo atalho | Custo54, mas quatro turnos de orçamento18: 16,5/16,5/18/3. Dividir54por18 não respeitaria os trechos. |
| Recuo → C → serviço → A | Cinco turnos de orçamento18: 16,5/16,5/18/18/9. Condições e rota fixas, sem reação adversária simulada. |
| Sem intervenção | Um único fechamento no terceiro fim de rodada. |
| Parada na terceira rodada antes da fase | Mantém aberto; parar depois conserva fechado. |
| Faixa ocupada no terceiro avanço | Aguarda aberto; faixa livre na rodada seguinte permite fechar só na fase seguinte. |
| Folha destruída | Libera o vão e impede novos fechamentos, antes ou depois da primeira tentativa. |
| Resposta preparada de9m | Alcança A saindo de C antes de fechar; não percorre os18m do serviço numa única resposta depois. |

A revisão documental conferiu posição da parada, linha de visão distinta de distância de caminhada, ocupação por corpos e objetos, cadência em iniciativa, estados após destruição, gatilho de Preparar, interferência do agarrão, Doma e fechamento da missão. Os casos não cobrem todas as combinações de técnicas e Origens.

## Revisão de clareza

| Risco de apresentação | Solução usada | Motivo |
|---|---|---|
| Chamar combinação de dois exemplos de encontro equilibrado. | Comparação de três referências, sem rótulo de dificuldade. | Separa o que mudou no espaço do que mudou pelo prazo. |
| Escrever apenas “a porta fecha em três rodadas”. | Definir abertura, fase, ocupação, parada e estado posterior. | Permite resolver a cena sem inventar o momento da consequência. |
| Tratar saída maior como acréscimo de dano. | Mostrar custos de andar e arrastar e ações concorrentes. | Expõe a pressão sobre socorro e retirada sem nova parcela de dano. |
| Usar custo total dividido pelo deslocamento como duração. | Conferir segmentos e sobras por turno. | Evita conceder metros que não pagam o próximo trecho. |
| Fazer a criatura saber tudo sobre a cena. | Preservar percepção, comportamento e limites de acesso nos dois lados. | Mudança de cenário afeta também a oposição. |

## Continuidade

Plano v58, caderno v52, matriz, roteiro, índice, referências e retomada atualizados. M124 recebe método de composição e variante; M017/M129 recebem um efeito de acesso com intervenções e estados. Permanecem abertos construtor numérico geral, chefes, doenças e outros perigos. Nenhuma escolha nova foi adicionada ao registro autoral 06.

Preservados todos os arquivos anteriores fora dos oito registros previstos, inclusive as fichas e os exemplos de origem. Salvamento local; esta etapa não faz commit ou push. A publicação remota anterior continua sendo outra operação. Sem sessão humana, simulação integral ou declaração de equilíbrio.

**Próxima tarefa recomendada:** desenvolver o método de chefes e confrontos maiores, comparando quantidade de ações, fases, sinais e oportunidades de resposta antes de propor uma ficha ampliada ou multiplicadores. Usar as composições anteriores para explicitar os problemas que cada recurso tenta resolver. **GPT-6 Astra, esforço extra alto**, para desenho e interações; **GPT-6.1 Sol, esforço alto**, para a redação. Bestiário integral e treinamentos continuam adiados.

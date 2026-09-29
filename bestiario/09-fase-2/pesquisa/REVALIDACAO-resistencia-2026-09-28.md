# Revalidação da abordagem de resistência dos inimigos

28/09/2026. Pedido do Mizuki: aprofundar a comparação antes de decidir como cobrar resistência. A pesquisa abaixo precedeu a aprovação. Mizuki aprovou a recomendação com "Pode fechar e aprovar essa mudança nas pastas do Claude 2 tbm, sigamos". A retirada do Evocador da média foi aprovada separadamente.

## Conclusão da pesquisa

Há apoio explícito em D&D 2024 para dar resistência pontual sem recalcular a ficha. Não há fundamento para dizer que todos os sistemas fazem isso, que a maioria dos sistemas foi demonstrada por esta amostra, ou que uma resistência pontual não afeta o combate. D&D 2014 e 2024 são duas edições da mesma família, não duas confirmações independentes de um consenso.

| Fonte primária conferida | Procedimento | O que permite concluir |
|---|---|---|
| D&D, Guia do Mestre 2014, páginas impressas 277–278; PDF local, páginas 278–279 | Ao discutir três ou mais tipos, sobretudo os físicos, usa PV efetivos para estimar o nível de desafio quando o grupo não consegue contornar a proteção. O próprio texto manda conservar os PV reais nessa etapa. | Há cobrança no cálculo de dificuldade para proteção ampla. Reduzir PV para conservar uma dificuldade escolhida seria uma adaptação de construção, não a instrução literal desse passo. |
| D&D, Dungeon Master's Guide 2024, página impressa 57; PDF local, página 61, seção Resistances and Immunities | Permite conceder resistência ou imunidade a um ou dois tipos a uma criatura sem essas defesas; também permite trocar tipos já existentes. Não manda descontar PV nessa operação. | Suporte explícito para modificação pontual sem esse desconto. Não autoriza repetir a operação indefinidamente nem conceder todos os tipos. |
| Pathfinder 2e, GM Core, página 119, Archives of Nethys | Recomenda normalmente menos PV a criaturas resistentes, com ênfase em resistência ampla ou física. Não determina o desconto. A resistência subtrai um valor do dano; não é a redução pela metade do Projeto M. | É precedente para compensação em PV, mas não fornece um divisor transferível nem uma decisão idêntica entre mestres. |
| 13th Age, Archmage Engine v4.0, Monster Creation, páginas 423–424 do PDF da editora | Traz ajustes gerais de atributos e recomenda evitar defesas que prolonguem a morte do monstro sem uma maneira ofensiva de desbloqueá-las. Não dá tarifa específica por resistência nessa seção. | A nota anterior foi categórica demais ao escrever “não cobra”. A conclusão sustentada é “não encontrei tarifa específica nessa seção”; a cautela com defesas está explícita. |

Fontes online:
- Pathfinder: https://2e.aonprd.com/Rules.aspx?ID=2893
- 13th Age, PDF da editora: https://pelgranepress.com/srv/htdocs/wp-content/uploads/2013/10/13th-Age-Archmage-Engine-v4.0_Monsters.pdf

Os dois PDFs de D&D foram lidos e suas páginas relevantes foram inspecionadas em imagem na coleção local de sistemas. A revisão não redistribui os livros.

## Limites da pesquisa anterior

O endereço antigo de Monster Basics do Steel Compendium não devolveu o conteúdo necessário nesta consulta. A página atual de Damage Immunity se identifica como produto independente sob licença, não como publicação da MCDM. Trocar o tipo de uma defesa já existente e adicionar uma defesa são operações diferentes. A ausência de um termo na fórmula de valor de encontro não demonstra que adicionar resistências arbitrárias seja gratuito. Draw Steel não foi usado aqui como prova dessa conclusão.

GURPS cobra vantagens em pontos de personagem; isso não equivale a um desconto fixo de PV nem a um preço de encontro. GURPS e 3D&T não foram recontados como votos sobre a fórmula de encontro do Projeto M. Suas entradas anteriores permanecem como pesquisa histórica, sem nova certificação nesta revisão.

## Aplicação ao Projeto M

O divisor `1,11` segue a hipótese de que um tipo isolado representa 20% do dano recebido: com metade desse dano cortada, passa 90% do dano. O multiplicador teórico de vida efetiva é `1 / 0,9`, aproximado a duas casas. A peça 19 declara que a distribuição de dano ainda é previsão. Portanto, a aritmética é explicável, mas o peso de qualquer tipo individual não foi medido em mesas. O peso dos três grupos, por si só, também não demonstra o peso de cada um dos catorze tipos.

Para uma fração `q` do dano coberta por resistência, a duração relativa simplificada é `1 / (1 − q/2)`. Essa conta supõe fluxo contínuo de dano e não simula arredondamento de cada golpe, mudança de ataque, acerto, cura ou perda de ações.

No exemplo já publicado do Desastre ×4 de nível 30, use 945 PV e dano do grupo 315 por rodada. Com o desconto atual, a ficha fica com 851 PV:

| Fração do dano do grupo coberta, hipótese de exemplo | Duração com 851 PV | Duração com 945 PV |
|---|---|---|
| 0% | 2,70 rodadas | 3,00 rodadas |
| 20% | 3,00 rodadas | 3,33 rodadas |
| 100% | 5,40 rodadas | 6,00 rodadas |

Calculado por `PV / (315 × (1 − q/2))`. Os pesos são cenários de sensibilidade, não frequências observadas. Nenhuma das duas escolhas equaliza automaticamente todas as composições de grupo.

## Recomendação aprovada em 28/09/2026

Retomar a regra da Fase 1 para **um ou dois tipos fixos no total da ficha**, sem desconto de PV; conservar a cobrança já existente para resistência a um grupo inteiro. A justificativa é dar uma exceção simples e reproduzível para proteção pontual e preservar o custo da proteção ampla. A resistência continua reduzindo o dano pela metade, e pode dificultar muito uma luta contra um grupo sem alternativa.

Não alterar o preço de imunidades, resistências de jogadores ou vulnerabilidades por extensão desta recomendação. Não converter “é sabor” em “não tem efeito mecânico”. Não permitir obter proteção a um grupo inteiro gratuitamente escrevendo seus tipos em entradas separadas.

**Lacuna real preservada:** a fronteira de três ou mais tipos mistos, sem completar um grupo, não fica resolvida apenas pelas duas linhas antigas “1–2 tipos” e “grupo inteiro”. Se esse caso for permitido no construtor de inimigos, precisa de tratamento explícito; a pesquisa não fornece automaticamente um número para ele. Isso não impede decidir o caso de um ou dois tipos agora.

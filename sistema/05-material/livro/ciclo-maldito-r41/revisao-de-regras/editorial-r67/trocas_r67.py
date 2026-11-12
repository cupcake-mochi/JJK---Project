"""Trocas da R67: Técnica Máxima com Forma e função pagas nos dados.

Decisões do Mizuki em 12/11/2026:
1. A Forma e a base da função saem dos dados-base, 1 ponto de preço = 1d8, como no feitiço comum.
   Os pontos de montagem pagam só as Melhorias.
2. Máxima sem dano: o Efeito Próprio principal (até Pesada) é a função, pago nos dados;
   ela recebe o reforço de Controle dos feitiços comuns.
3. Vida temporária vira função da Máxima, com as bases do feitiço comum (individual Leve;
   coletiva Média mais a Forma). Sem os tetos do feitiço comum; vale metade da vida máxima.
"""
MOTIVO = 'Técnica Máxima: Forma e função nos dados (decisão do autor, 12/11/2026)'

TROCAS = [
 ('fundamento--maxima',
  'No nível **17**, você desenvolve uma aplicação excepcional da técnica. Pode concentrar um ataque, restaurar aliados ou realizar um Efeito próprio de grande alcance.',
  'No nível **17**, você desenvolve uma aplicação excepcional da técnica. Pode concentrar um ataque, restaurar ou proteger aliados ou realizar um Efeito próprio de grande alcance.'),
 ('fundamento--maxima',
  '| Nível | Dados de dano ou cura | Pontos de montagem | PE |',
  '| Nível | Dados-base | Pontos de montagem | PE |'),
 ('fundamento--maxima',
  'Use a coluna de **pontos de montagem** para pagar a Forma e as Melhorias. A quantidade de dados permanece igual ao valor indicado na tabela para sua faixa de nível. Descarte os pontos que sobrarem após as compras.',
  'Os **dados-base** pagam a Forma e a base da função, como os pontos de um feitiço comum: cada ponto de preço tira 1d8. Os dados que restam formam o resultado da Máxima. Use a coluna de **pontos de montagem** só para as Melhorias. Descarte os pontos que sobrarem após as compras; eles não viram dados.'),
 ('fundamento--maxima',
  'Famílias Livres dão seu desconto normal; Fechadas continuam indisponíveis. A Forma não recebe desconto.',
  'Famílias Livres dão seu desconto normal; Fechadas continuam indisponíveis. A Forma e a base da função não recebem desconto e não ocupam vaga de Melhoria.'),
 ('fundamento--maxima',
  'Escolha durante a criação se a Máxima causará dano, recuperará vida ou produzirá uma aplicação sem dano.',
  'Escolha durante a criação se a Máxima causará dano, recuperará vida, concederá vida temporária ou produzirá uma aplicação sem dano.'),
 ('fundamento--maxima',
  'Dano ou cura\n\nUse os dados da faixa da Técnica Máxima. Na criação, anote dano ou cura e a Forma que entrega o resultado. A cura paga sua base Média; a aplicação coletiva paga também a Forma de área e exige Amparo e Área. Os dados de cura da Máxima não usam o teto comum. A cura coletiva alcança cada aliado válido na região.',
  'Dano, cura ou vida temporária\n\n'
  'Use os dados da faixa da Técnica Máxima. Na criação, anote a função e a Forma que entrega o resultado. Tire dos dados o preço da Forma e a base da função, nos preços da sua maior Classe. Cada dado que resta vira o resultado indicado.\n\n'
  '| Função | Base tirada dos dados | Cada dado que resta |\n'
  '|---|---|---|\n'
  '| Dano | 0 | 1d8 de dano. |\n'
  '| Cura direta | Média | 1d8 de cura. Exige Amparo. |\n'
  '| Vida temporária individual | Leve | 3 de vida temporária. Exige Amparo. |\n'
  '| Cura ou vida temporária coletiva | Média, mais a Forma de área | A parte inteira para cada aliado válido na região. Exige Amparo e Área. |\n\n'
  'A cura e a vida temporária da Máxima não usam o teto de cura individual nem o teto coletivo dos feitiços comuns. A vida temporária respeita o limite de cada criatura, metade da vida máxima, e não se soma a outra vida temporária.\n\n'
  '> **Exemplo.** Na faixa 17 a 20, os preços são os da Classe 5. Uma Máxima de dano com Explosão tira 5 dos 24 dados e causa 19d8 em cada alvo da área. Uma cura individual com Projétil tira a base Média e recupera 19d8. Uma vida temporária coletiva com Aura tira a base Média e a Aura, 5 e 3: cada aliado na região recebe 16 × 3 = 48 de vida temporária, até metade da própria vida máxima.'),
 ('fundamento--maxima',
  'Mei monta **Fenda de Arrasto**, na faixa 17 a 20: Projétil (0), Passo (1, Alcance Livre) e Empurrão (1, Alcance Livre).',
  'Mei monta **Fenda de Arrasto**, na faixa 17 a 20: Projétil, que não tira dados, com Passo (1, Alcance Livre) e Empurrão (1, Alcance Livre).'),
 ('fundamento--maxima',
  'Para criar uma Máxima de utilidade, defina sua função e descarte os dados de dano ou cura. O orçamento de montagem permanece o da tabela. O reforço de Controle dos feitiços comuns fica indisponível nessa aplicação.',
  'Para criar uma Máxima de utilidade, escreva sua função como um **Efeito Próprio principal**, de preço até Pesado. Ele é a função dessa Máxima: seu preço sai dos dados-base, junto com o da Forma, e os dados que restam são descartados. O Efeito principal não ocupa vaga de Melhoria, e os pontos de montagem ficam inteiros para as Melhorias.\n\n'
  'Nessa aplicação, a Máxima recebe o **reforço de Controle** dos feitiços comuns: a rodada adicional e +2 na CD dos TRs próprios de Controle, quando aplicáveis.'),
 ('fundamento--maxima',
  'Para conceder uma proteção especial em pontos de vida, crie um Efeito Próprio com quantidade definida.',
  'Para conceder vida temporária, use a função de vida temporária, em Dano, cura ou vida temporária.'),
 ('fundamento--maxima',
  'Uma Máxima sem dano nem cura pode usar **uma aplicação própria de utilidade em combate** quando seu Efeito Próprio autorizar esse uso',
  'Uma Máxima sem dano, cura ou vida temporária pode usar **uma aplicação própria de utilidade em combate** quando seu Efeito Próprio principal autorizar esse uso'),
 ('fundamento--maxima',
  'Ao atingir os níveis 21 e 26, atualize dados, pontos, preços e PE.',
  'Ao atingir os níveis 21 e 26, atualize dados, pontos, preços e PE, e recalcule os dados que a Forma e a função tiram.'),
 ('fundamento--passagem',
  '**Aplicação de utilidade (base 0) + Efeito Próprio: passagem entre marcas (Pesada).** Sem desconto de Família. O custo é 8, 9 ou 11 pontos, para maior Classe 5, 6 ou 7, nessa ordem. Cabe nos orçamentos 8, 12 e 16. Os dados de dano e cura são descartados.',
  '**Efeito Próprio principal: passagem entre marcas (Pesada).** Sem Forma de área e sem desconto de Família. O preço é 8, 9 ou 11, para maior Classe 5, 6 ou 7, nessa ordem, e sai dos 24, 28 ou 32 dados. Os dados que restam são descartados. Os 8, 12 ou 16 pontos de montagem ficam livres para Melhorias compatíveis.'),
 ('fundamento--retirada',
  '**Aplicação própria de utilidade (base 0) + Efeito Próprio: retirada coletiva (Pesada, sem desconto).** São 8/9/11 pontos nas faixas 17/21/26, dentro dos orçamentos 8/12/16.',
  '**Efeito Próprio principal: retirada coletiva (Pesada, sem desconto).** O preço, 8/9/11 nas faixas 17/21/26, sai dos 24/28/32 dados, e os que restam são descartados. Os 8/12/16 pontos de montagem ficam livres para Melhorias.'),
 ('campo--inv-maxima',
  'Os pontos pagam Forma e Melhorias, sem comprar dados adicionais.',
  'Os dados fixos pagam a Forma e a base da função, como na Técnica Máxima pessoal. Os pontos pagam só as Melhorias, sem comprar dados adicionais.'),
 ('campo--inv-maxima',
  '> **Exemplo.** A domada de nível 17 causa 19d8 numa montagem ofensiva válida.',
  '> **Exemplo.** A domada de nível 17 causa 19d8 com Projétil, ou 14d8 com Explosão, que tira 5 dados.'),
 ('campo--inv-maxima',
  'Uma aplicação de cura usa 19d8.',
  'Uma cura individual tira a base Média e recupera 14d8.'),
 ('consulta--consulta-glossario-6',
  '[Técnica Máxima](#fundamento--maxima). Aplicação avançada com montagem e uso próprios, incluindo dano, cura ou utilidade.',
  '[Técnica Máxima](#fundamento--maxima). Aplicação avançada com montagem e uso próprios, incluindo dano, cura, vida temporária ou utilidade.'),
]

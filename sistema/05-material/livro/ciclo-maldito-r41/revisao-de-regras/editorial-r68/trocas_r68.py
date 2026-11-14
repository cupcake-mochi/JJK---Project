"""Trocas da R68: o reforço de Controle da Máxima sem dano, nas duas seções que ainda o negavam.

A R67 (decisão do Mizuki em 12/11/2026) deu à Máxima sem dano o reforço de Controle dos
feitiços comuns, mas a seção de Controle e a de Controle das entidades continuaram dizendo
que a Técnica Máxima não o recebe. A domada segue o procedimento da Máxima pessoal, então
recebe o reforço do mesmo jeito. Classe 0, Liberação Máxima e a básica continuam sem ele.
Achado em 14/11/2026, ao levar a regra para a ficha.
"""
MOTIVO = 'Reforço de Controle da Máxima sem dano nas seções de Controle (consequência da R67, 14/11/2026)'

TROCAS = [
 ('fundamento--controle',
  'Classe 0, Liberação Máxima e Técnica Máxima não recebem este reforço de feitiço comum.',
  'Classe 0 e Liberação Máxima não recebem este reforço de feitiço comum. A Técnica Máxima o recebe só na aplicação sem dano, descrita em [Técnica Máxima](#fundamento--maxima).'),
 ('construcao--entidades-controle',
  'A básica e as aplicações máximas não recebem esse reforço comum.',
  'A básica e a Liberação Máxima não recebem esse reforço comum. A Técnica Máxima da domada o recebe só na aplicação sem dano, como a pessoal.'),
]

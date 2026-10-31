from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];R=B/'revisao-r54'
d=json.loads((R/'TEXTOS-TRABALHO.json').read_text());ops=[]
def rep(k,a,z,m):
 assert d[k].count(a)==1,(k,a)
 d[k]=d[k].replace(a,z);ops.append(dict(bloco=k,antes=a,depois=z,motivo=m,passada=2))
rep('fundamento--formas','com **+2 no ataque**, o bônus da Melhoria','com resolução por ataque e **+2 no acerto**, o bônus da Melhoria','Deixar explícita a resolução escolhida no exemplo de Precisão, sem atribuí-la a todo feitiço de Toque.')
rep('origens--restricao-sem-energia','Defesa sem Armadura e Estímulo Muscular já são gratuitas pela rota,','**Defesa sem Armadura**, que fornece proteção sem uniforme, e **Estímulo Muscular**, que reforça ataques desarmados com esforço, já são gratuitas pela rota,','Identificar as capacidades gratuitas antes de remeter ao capítulo da rota.')
rep('evocador--ev-turnos','Kaito tem 12 PE e começa seu turno com o cão.','Kaito tem 12 PE e começa seu turno com o [Cão de sombra](#construcao--entidade-cao), cuja básica é Mordida e cuja especial é Mordida precisa.','Identificar as duas capacidades do exemplo antes de aplicar suas despesas e rolagens.')
rep('geral--critico','| Dados adicionais de Melhoria, aptidão ou Bênção |','| Dados adicionais de outras capacidades, incluindo Melhorias de feitiço, aptidões e Bênçãos |','Expressar a categoria da regra de crítico sem exigir conhecimento prévio dos três catálogos.')
rep('emanador--ema-instintiva','Um desconto fixo de Ritual entra antes da metade,','O [Ritual](#ritual--ritual) reforça uma conjuração com preparação e pode conceder desconto de energia. Um desconto fixo de Ritual entra antes da metade,','Explicar a origem do desconto antes da ordem de cálculo.')
rep('ab--ab-kaori','Suas Famílias Livres são Controle e Castigo. Amparo, Área e Auxiliares estão Fechadas.','Suas Famílias Livres são **Controle**, voltada a condições e contenções, e **Castigo**, voltada ao dano. Ela fecha **Amparo**, ligada à cura e à proteção, **Área**, ligada a efeitos sobre regiões, e **Auxiliares**, ligada a recursos de apoio. Consulte [Conheça as Famílias](#fundamento-link-guia-familias) para os acessos de cada uma.','Explicar a função das Famílias usadas na primeira ficha de exemplo, sem transformá-las em proibições narrativas gerais.')
(R/'TEXTOS-TRABALHO.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'OPERACOES-PASSADA-2.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
print(len(ops),'ajustes na segunda passagem')

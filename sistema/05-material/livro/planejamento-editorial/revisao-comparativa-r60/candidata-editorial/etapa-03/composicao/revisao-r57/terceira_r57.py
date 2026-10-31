from pathlib import Path
import json
B=Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r57');R=B/'revisao-r57';base=json.loads((B/'revisao-r56/BLOCOS-R56.json').read_text());d=json.loads((R/'TEXTOS-TRABALHO.json').read_text());ops=json.loads((R/'OPERACOES.json').read_text())
def rep(k,a,z,why):
 assert d[k].count(a)==1,(k,a)
 d[k]=d[k].replace(a,z,1);ops.append(dict(bloco=k,antes=a,depois=z,motivo=why,passada=3))
rep('aptidoes--apt-catalogo','**Kokusen básico não exige compra.**','**Kokusen** é um reforço de dano que pode ocorrer após um crítico corpo a corpo com energia amaldiçoada. **Sua versão básica não exige compra.**','Contextualizar Kokusen antes da orientação sobre aquisição.')
rep('aptidoes--apt-kokusen','role **d100**.','role **d100**, obtendo um resultado de 1 a 100.','Explicar a notação de dado ausente da lista inicial.')
rep('rotas--rota-lapidacao','aprende Faro, de Categoria de Efeito 1.','aprende [Faro](#rotas--rota-perseguicao), de Categoria de Efeito 1, que permite perceber vestígios físicos para seguir feiticeiros e maldições.','Contextualizar a Bênção usada no exemplo de aquisição.')
rep('rotas--rota-lapidacao','pode aprender Presilha, de Categoria de Efeito 2, se tiver Força 4.','pode aprender [Presilha](#rotas--rota-corpo), de Categoria de Efeito 2, se tiver Força 4; ela permite exigir a repetição de um TR bem-sucedido contra certas manobras suas.','Contextualizar a segunda Bênção do exemplo sem antecipar seu procedimento completo.')
rows=[dict(id=f'R57-{i+1:03d}',bloco=k,antes=base[k],depois=d[k],motivo=' '.join(dict.fromkeys(o['motivo'] for o in ops if o['bloco']==k)),item='Revisão editorial: contexto e ordem de apresentação',altera_regras=False) for i,k in enumerate(k for k in base if base[k]!=d[k])]
(R/'TEXTOS-TRABALHO.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');(R/'OPERACOES.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(B/'ALTERACOES-R56-para-R57.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');print(len(ops),'operações',len(rows),'blocos')

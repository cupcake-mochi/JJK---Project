"""Melhorar a consulta de Pactos e entidades sem alterar as escolhas e valores."""
from pathlib import Path
import json,shutil,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
names=['10-jogar-em-guilda.md','consultas/40-registro-de-dedicacao-por-ficha.md']
states={n:(A/'antes'/T.relative_to(R)/n).read_text() for n in names};logs=[]
def edit(name,before,after,reason):
 s=states[name];assert s.count(before)==1,(name,before,s.count(before));states[name]=s.replace(before,after,1)
 logs.append({'fonte':(T/name).relative_to(R).as_posix(),'antes':before,'depois':after,'motivo':reason})
n=names[0]
edit(n,'com saldo válido só no ciclo seguinte e gasto das antigas primeiro.','com saldo válido só no ciclo seguinte e gasto das antigas primeiro. Transfira apenas as horas novas que ficaram livres.','Explicitar no resumo que somente a parcela nova e livre pode passar, conforme a regra já apresentada em Entre missões.')
edit(n,'Separe **horas confirmadas, reservadas e livres**, sem contar duas vezes.','Separe [**horas confirmadas, reservadas e livres**](<08-entre-missoes.md#trabalho-ainda-em-conferencia>), sem contar duas vezes.','Levar diretamente à explicação dos três estados, sem exigir procurar no capítulo inteiro.')
edit(n,'Sugerir uma tarefa não significa aceitar fazê-la.','Registre uma pessoa como responsável somente quando ela tiver aceitado a tarefa.','Dizer diretamente quando atribuir a responsabilidade, em acordo com a linha de continuidade.')
n=names[1]
edit(n,'O que sobrar das horas novas de um ciclo vale só no ciclo seguinte.','Apenas as horas novas que ficaram livres podem passar para o ciclo seguinte.','Evitar que a abertura da folha pareça incluir horas pendentes no saldo livre; manter a orientação já presente no fechamento.')
for name,s in states.items():(T/name).write_text(s)
(A/'alteracoes.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
composition=json.loads((A/'base-composicao.json').read_text())['ordem'];routes=[]
for name in names:
 rel=(T/name).relative_to(R).as_posix();row=next(x for x in composition if x['fonte']==rel);p=E/row['pagina'];q=A/'antes'/p.relative_to(R)
 if not q.exists():q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
 routes.append({'fonte':rel,'pagina':row['pagina'],'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
(A/'destinos-alterados.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2)+'\n')
print(len(logs),'ajustes em',len(names),'fontes.')

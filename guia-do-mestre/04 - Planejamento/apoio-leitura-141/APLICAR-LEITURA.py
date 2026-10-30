"""Esclarecer Entre missões e seus registros, preservando as regras e contas."""
from pathlib import Path
import json,shutil,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
names=['08-entre-missoes.md','casos/34-oficios-fabricacao-e-reparos.md','casos/99-limiar-feitos-e-promocao.md','consultas/16-linha-de-continuidade.md','consultas/38-ficha-de-projeto-e-entrega.md','consultas/40-registro-de-dedicacao-por-ficha.md']
states={n:(A/'antes'/T.relative_to(R)/n).read_text() for n in names};logs=[]
def edit(name,before,after,reason):
 s=states[name];assert s.count(before)==1,(name,before,s.count(before));states[name]=s.replace(before,after,1)
 logs.append({'fonte':(T/name).relative_to(R).as_posix(),'antes':before,'depois':after,'motivo':reason})
n=names[0]
edit(n,'Este capítulo reúne descanso, dedicação, Ofícios, equipamento e recompensas. O Livro de Regras 1.0 fornece suas regras; o ciclo de dedicação é a recomendação deste Guia para a guilda. As regras usadas aqui estão no Livro de Regras 1.0, e os casos completos ficam disponíveis para consulta.','Este capítulo trata de descanso, dedicação, Ofícios, equipamento e recompensas. Use as regras do Livro de Regras 1.0; para organizar as atividades da guilda, o Guia recomenda o ciclo de dedicação apresentado a seguir. Os casos completos ficam disponíveis para consulta.','Retirar a repetição sobre a referência e explicar diretamente de onde vem a recomendação de ciclo.')
edit(n,'Anote separadamente as horas de trabalho já conferidas, as que ainda aguardam conferência e as que podem ser usadas: **confirmadas, reservadas e livres**. As reservadas ficam vinculadas à atividade; não podem também financiar outro projeto ou aparecer como saldo transferido.','No registro, **confirmadas** são as horas de trabalho já conferidas; **reservadas**, as horas vinculadas a trabalho que aguarda conferência; **livres**, as horas ainda disponíveis. Horas reservadas não podem também financiar outro projeto ou aparecer como saldo transferido.','Definir cada estado junto ao nome, para que horas de trabalho confirmadas não pareçam saldo livre.')
edit(n,'### Combinar o trabalho','<span id="combinar-o-trabalho"></span>\n\n### Planejar o projeto','Usar um subtítulo que identifique o conteúdo e conservar o destino anterior.')
edit(n,'Caixa e selo são diferentes. Abrir a caixa pode expor o selo sem retirá-lo.','Caixa e selo são diferentes. O selo de contenção do objeto também é diferente do Selo exigido para conjurar. Abrir a caixa pode expor o selo sem retirá-lo.','Distinguir a proteção do objeto do requisito de conjuração, como já faz a Pastilha.')
edit(n,'O desconto é **por jogador, dentro da campanha**. Trocar de ficha não reinicia a contagem.','O desconto é **por jogador, dentro da campanha**. A dedicação às atividades é **por ficha**. Trocar de ficha não reinicia a contagem de XP.','Identificar os dois registros com critérios diferentes e explicitar qual contagem não reinicia.')
edit(n,'Se adotar salário por participação, a parcela mínima é um quarto. A campanha define quantas participações completam o mês; a recomendação publicada é três. Curta e padrão contam uma, longa duas e final de arco três.','Se adotar salário por participação, a parcela mínima é um quarto. A campanha define quantas participações completam o mês; a recomendação publicada é três. Divida os três quartos restantes pelo número de participações exigidas; cada participação soma uma dessas parcelas, até completar o salário. Curta e padrão contam uma, longa duas e final de arco três.','Incluir a fórmula publicada que permite calcular o salário quando a campanha usa outro total de participações.')
n=names[1]
edit(n,'Treinamentos específicos ainda não têm regras próprias aprovadas; não os presuma a partir de um projeto concluído.','Uma prática só altera a ficha quando a regra adotada explicar o ganho e seus requisitos.','Orientar o leitor sobre aquisição, retirando uma nota do processo de produção sem conceder benefícios de treinamento.')
n=names[2]
edit(n,'Veja as regras em [Conferir a ficha](<../07-personagens-e-tecnicas.md#71-conferir-a-ficha>).','Veja as regras em [Ao subir de nível](<../07-personagens-e-tecnicas.md#ao-subir-de-nivel>).','Levar a atualização após o Limiar à seção que explica ganhos e saldos, como no caso de vida rolada.')
n=names[3]
edit(n,'**Estado dos personagens que precisa ser considerado:**','**Conclusão e recompensas:** data de conclusão, resultado da missão, XP e desconto semanal de cada participante, dinheiro, itens e portadores; feitos e promoções confirmados ou pendentes.\n\n**Estado dos personagens que precisa ser considerado:**','Oferecer o campo de fechamento e recompensas para o qual o capítulo já remete, sem criar recompensa ou promoção automática.')
n=names[4]
edit(n,'Ele separa trabalho da ficha, serviço contratado e espera;','Ele separa trabalho do personagem, serviço contratado e espera;','Nomear a pessoa que dedica o trabalho, em vez de atribuir trabalho à ficha.')
n=names[5]
edit(n,'Consulte [Tempo para as atividades](<../08-entre-missoes.md>), no capítulo Entre missões,','Consulte [Tempo para as atividades](<../08-entre-missoes.md#82-tempo-para-as-atividades>), no capítulo Entre missões,','Abrir diretamente a orientação de dedicação, em vez de levar ao início de um capítulo longo.')
for name,s in states.items():(T/name).write_text(s)
(A/'alteracoes.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
composition=json.loads((A/'base-composicao.json').read_text())['ordem'];routes=[]
for name in names:
 rel=(T/name).relative_to(R).as_posix();row=next(x for x in composition if x['fonte']==rel);p=E/row['pagina'];q=A/'antes'/p.relative_to(R)
 if not q.exists():q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
 routes.append({'fonte':rel,'pagina':row['pagina'],'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
(A/'destinos-alterados.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2)+'\n')
print(len(logs),'ajustes em',len(names),'fontes.')

"""Melhorar a consulta de Pactos e entidades sem alterar as escolhas e valores."""
from pathlib import Path
import json,shutil,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
names=['09-pactos-e-entidades.md','casos/43-aquisicao-e-projetos-de-entidades.md','casos/49-liberacao-irregular-minuta.md']
states={n:(A/'antes'/T.relative_to(R)/n).read_text() for n in names};logs=[]
def edit(name,before,after,reason):
 s=states[name];assert s.count(before)==1,(name,before,s.count(before));states[name]=s.replace(before,after,1)
 logs.append({'fonte':(T/name).relative_to(R).as_posix(),'antes':before,'depois':after,'motivo':reason})
n=names[0]
edit(n,'Não concede Estilo, níveis de Caminho ou Trilha, escolhas extras de Origem ou bônus numérico em ataque, Defesa e perícias.','Pode modificar um Estilo que a personagem já possua, mas não concede outro. Também não concede níveis de Caminho ou Trilha, escolhas extras de Origem ou bônus numérico em ataque, Defesa e perícias.','Explicar a diferença publicada entre modificar um Estilo e recebê-lo por Pacto, em acordo com a escala de ganhos.')
edit(n,'O sorteio inicial antes da primeira ação da sequência resolve Reações anteriores ao primeiro turno e não prepara Refluxo.','Antes da primeira ação de uma sequência com iniciativa, sorteie um limite inicial para as Reações que possam ocorrer antes do primeiro turno do portador. Esse sorteio não prepara Refluxo.','Explicar a finalidade e o momento do sorteio inicial com frases diretas, conservando o gatilho de Refluxo.')
edit(n,'Não há teto geral de adquiridas; o limite normal é **duas ativas**, salvo permissão específica. Corpos mantidos têm sua conta própria.','Não há teto geral de adquiridas; o limite normal é **duas ativas**, salvo permissão específica. Para o total de corpos mantidos, some o atributo escolhido para a Defesa das entidades à maior capacidade de entidades ativas que o Caminho permite em combate. Conte juntos os corpos ativos e inativos. Ativar um deles continua respeitando o teto de atuação.','Explicar a conta publicada de corpos mantidos, sem confundi-la com o total adquirido ou o limite de atuação.')
edit(n,'Use Construir invocações para corpo, nível, Classe, atributos, testes, Defesa, vida, Famílias, básicas, especiais e talentos.','Use a seção **Construir invocações**, do livro de regras, para definir corpo, nível, Classe, atributos, testes, Defesa, vida, Famílias, básicas, especiais e talentos.','Identificar uma seção da referência, em vez de parecer uma instrução ou ferramenta não apresentada.')
edit(n,'| Classe | Criar | Reconstruir | Transferir |','| Classe | Criar (horas) | Reconstruir (horas) | Transferir (horas) |','Levar a unidade de trabalho para os cabeçalhos, permitindo consultar a tabela sozinha.')
edit(n,'Aparência e personalidade não aumentam o tempo por si, e uma parte pronta não precisa ser fabricada novamente.','Aparência e personalidade não aumentam o tempo por si, e uma parte pronta não precisa ser fabricada novamente. [Tempo e materiais para criar entidades](<casos/45-tempo-materiais-e-retomada-de-entidades.md>) mostra o orçamento e a divisão do trabalho em etapas.','Dar acesso direto ao exemplo de tempo e materiais a partir da explicação principal.')
edit(n,'| Relação de Classes | Criar ou transferir | Reconstruir |','| Relação de Classes | Ajuste para criar ou transferir | Ajuste para reconstruir |','Explicitar que os valores são ajustes à base da CD, não CDs finais ou horas de trabalho.')
edit(n,'Inconsciência não é morte. Entidades que permanecem podem seguir ordens anteriores válidas e seus recursos, mas o personagem inconsciente não emite comandos novos.','Um corpo **inativo** conserva vida e posição e pode acompanhar o grupo, mas falha em toda rolagem, não recebe tarefas e não executa capacidades. Interpretação e trabalhos extremamente simples sem rolagem seguem a permissão do livro. **Desligada** é a entidade que caiu e não pode ser recolhida: fica como objeto no lugar e precisa do retorno próprio. Ativar um corpo inativo e religar um corpo Desligado são operações diferentes.\n\nInconsciência não é morte. Entidades que permanecem podem seguir ordens anteriores válidas e seus recursos, mas o personagem inconsciente não emite comandos novos.','Distinguir dois estados presentes nos exemplos antes de tratar a inconsciência e a morte do invocador; não transformar ativação em retorno ou recuperação.')
n=names[1]
edit(n,'Corpos mantidos têm uma conta própria.','Para conferir o total de corpos mantidos, veja [o limite de corpos](<../09-pactos-e-entidades.md#94-obter-uma-entidade>). Ativos e inativos entram nessa conta; o teto de atuação continua separado.','Oferecer a conta de corpos mantidos também a quem abrir esta consulta diretamente.')
n=names[2]
edit(n,'sem recarregá-lo pela troca de ficha.','sem recarregá-lo pela saída e nova adesão.','Nomear o encerramento e a nova adesão ao Pacto, em vez de sugerir troca de personagem.')
for name,s in states.items():(T/name).write_text(s)
(A/'alteracoes.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
composition=json.loads((A/'base-composicao.json').read_text())['ordem'];routes=[]
for name in names:
 rel=(T/name).relative_to(R).as_posix();row=next(x for x in composition if x['fonte']==rel);p=E/row['pagina'];q=A/'antes'/p.relative_to(R)
 if not q.exists():q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
 routes.append({'fonte':rel,'pagina':row['pagina'],'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
(A/'destinos-alterados.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2)+'\n')
print(len(logs),'ajustes em',len(names),'fontes.')

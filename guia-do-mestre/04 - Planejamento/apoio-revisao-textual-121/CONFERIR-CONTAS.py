from pathlib import Path
import json,hashlib,math
A=Path(__file__).resolve().parent;R=A.parents[1];checks=[]
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
rule=primary.read_text()
def row(start):
 line=next(x for x in rule.splitlines() if x.startswith('| '+start+' |'))
 return [v.strip() for v in line.strip('|').split('|')]
def ck(name,x,y):
 assert x==y,(name,x,y);checks.append({'conta':name,'resultado':x,'esperado':y})
ck('Travessia superior',[3+3+3,6/3],[9,2.0])
ck('Rota inferior: metros físicos e movimento',[3+6+9+6+3,3+6*2+9+6*2+3],[27,39])
ck('Três rodadas em segundos',3*6,18)
ck('Parada pela rota inferior: metros iniciais/restantes/segunda rodada',[9*3,39-27,9*2],[27,12,18])
ck('Pino de madeira: soma de danos e PV restantes',[2+3,5-2],[5,3])
ck('Queda 6m: dados/intervalo/exemplo',[6//3,2,12,3+4,10-7,max(0,5-7)],[2,2,12,7,3,0])
ck('Salto sem impulso, Força 0/1/2',[math.floor((3+1.5*f)/2/1.5)*1.5 for f in [0,1,2]],[1.5,1.5,3.0])
ck('Salto Força 1 com extensão',1.5+1.5,3.0)
ck('Atalho por G: andar/arrastar',[3+3,(3+3)*2],[6,12])
ck('Serviço por P e Q: andar/arrastar',[6*3,6*3*2],[18,36])
ck('A até P e saldo para ir a C',[6+6,18-12,6],[12,6,6])
ck('Carga do resgate e teto Força 2',[1+72/12+2,2*(5+2)],[9.0,14])
ck('Turnos de resgate a partir de C, com 18m por turno',[math.ceil(12/18),math.ceil(36/18)],[1,2])
# Percorrer cada passo, sem levar sobras de um turno ao seguinte.
steps=[3]*4+[4.5]*4+[3]*8;costs=[];spent=0
for cost in steps:
 if spent+cost>18:costs.append(spent);spent=0
 spent+=cost
costs.append(spent)
ck('Recuo até pátio: custos por turno',costs,[16.5,16.5,18,3])
ck('Recuo até pátio: custo e divisão idealizada',[sum(steps),sum(steps)/18,len(costs)],[54.0,3.0,4])
ck('Objetos da passarela e portão: madeira/metal, PV por porte',[int(row('Madeira')[1]),int(row('Pequena peça: garrafa, fecho ou cadeado')[2]),int(row('Madeira')[1]),int(row('Objeto de mão: caixa ou instrumento')[2]),int(row('Ferro ou aço')[1]),int(row('Objeto maior: mesa grande ou carrinho')[2])],[14,5,14,10,18,40])
ck('Sineiro: CD, acerto, carga normal/arrasto',[8+4+1,4+1,5+4,(5+4)*2],[13,5,9,18])
ck('Sineiro: mínimo/máximo de Pancada e crítico',[2*1+4,2*6+4,4*1+4,4*6+4],[6,16,8,28])
ck('Sineiro: Integridade e deslocamento',[108/2,9/2],[54,4.5])
stages={i:(4 if i==0 else max([0]+[s for fraction,s in [(1/4,1),(1/2,2),(3/4,3)] if 54-i>=54*fraction])) for i in range(55)}
ck('Faixas exatas dos estágios',[[min(i for i,s in stages.items() if s==n),max(i for i,s in stages.items() if s==n)] for n in [0,1,2,3,4]],[[41,54],[28,40],[14,27],[1,13],[0,0]])
ck('Condução especial: carga e distâncias',[72/12+1,9/1.5*1.5,9/3*1.5],[7,9.0,4.5])
ck('Impacto: dados e limites de dano, sucesso arredondado para cima',[5,5*8,math.ceil(5/2),math.ceil(40/2)],[5,40,3,20])
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d={'registro':121,'novos_parametros':False,'conferencias':checks,'regras_primarias':{'fonte':str(primary.relative_to(R)),'sha256':sha(primary),'trechos_consultados':['Preparar — prazo, gatilho e deslocamento','Movimento, escalada, saltos, quedas e queda sobre criaturas','Usar objeto, Danificar objetos e adequação de efeitos','Carga, arrasto e manobras','Lento, Guarda Aberta e estágios exatos de Integridade']},'limites':['Conferência dirigida da aritmética e das regras existentes. Sem simulação de combate ou resgate.','O prazo de três rodadas, as capacidades próprias e o chefe continuam experimentais.','Não inclui aprovação da dificuldade ou atualização do bestiário completo.']};(A/'contas-conferidas.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(len(checks),'contas conferidas')

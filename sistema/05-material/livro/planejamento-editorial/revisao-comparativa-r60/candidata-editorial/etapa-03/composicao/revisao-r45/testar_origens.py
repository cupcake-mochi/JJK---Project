"""Casos determinísticos de Etapa 6. Não são playtest nem prova de equilíbrio."""
from pathlib import Path
from itertools import combinations,product
import json,math
R=Path(__file__).resolve().parent
rows=[]
def case(group,name,inputs,expected,obtained,source):
 rows.append(dict(grupo=group,caso=name,entradas=inputs,esperado=expected,obtido=obtained,fonte=source,passou=expected==obtained,tipo='cálculo determinístico'))
def classe(n):return 1+(n>=5)+(n>=9)+(n>=13)+(n>=17)+(n>=21)+(n>=26)
def maestria(n):return 1+(n>=10)+(n>=18)+(n>=26)
for name,n,expected in [('Sem energia',8,28),('Latente',8,28),('Corpo geral',8,28),('Corpo Manutenção',10,45),('Encarnado',7,21),('Restrição corporal',8,28),('Receptáculo Coexistência',7,21),('Receptáculo Conflito',7,21),('Cada clã Descendente',7,21)]:
 case('T01/T16',name,{'menores_elegiveis':n,'vagas':2},expected,len(list(combinations(range(n),2))),'A008/A010 e montagem vigente de cada Origem')
options=[('Anatomia',i) for i in range(2)]+[('Armamento',i) for i in range(4)]+[('Locomoção',i) for i in range(3)]+[(str(i),0) for i in range(5)]
case('T16','Duplas detalhadas do Híbrido',{'opcoes':options},91,len(list(combinations(options,2))),'A050: repetição somente dos três menus e com opções distintas')
for m,expected in [(1,[8,4,8]),(2,[7,4,9]),(3,[6,4,10]),(4,[5,4,11])]:
 totals=[d+m for d in range(1,21)]
 case('T03','Distribuição exata Latente',{'maestria':m,'d20':'1–20'},expected,[sum(x<=9 for x in totals),sum(10<=x<=13 for x in totals),sum(x>=14 for x in totals)],'A038')
for total,expected in [(9,8),(10,6),(13,6),(14,4)]:
 variation=math.ceil(3/2); cost=max(1,6+(variation if total<=9 else -variation if total>=14 else 0))
 case('T03','Fronteira do custo',{'classe':3,'custo_completo':6,'total':total},expected,cost,'A037/A038')
case('T03','Piso de custo Classe 1',{'custo_completo':1,'controle':True},1,max(1,1-math.ceil(1/2)),'A038')
case('T03','Desconto antes da oscilação',{'base':9,'desconto':2,'classe':3,'controle':True},5,max(1,(9-2)-math.ceil(3/2)),'A037')
for current,maxhp,expected in [(31,100,False),(30,100,True),(0,100,False),(13,41,False),(12,41,True),(20,100,True),(40,100,False),(20,60,False)]:
 case('T04/T05','Faixa de regeneração',{'vida':current,'maximo_atual':maxhp,'temporaria_ignorada':10},expected,1<=current<=math.floor(maxhp*30/100),'A048 e requisito de ficha')
case('T04','Usos por Constituição',{'constituições':list(range(7))},[1,1,2,2,3,3,4],[c//2+1 for c in range(7)],'A048')
case('T04','Cura pode passar do limiar',{'maximo':41,'vida':12,'dados':[3,5]},20,min(41,12+3+5),'A048')
for delta,adjust,den in [(-2,-4,2),(-1,-2,2),(0,0,2),(1,0,3),(2,0,4)]:
 case('T06','Reparo por diferença de Classe',{'corpo_menos_reparador':delta,'atributo':3,'maestria':2,'especializacao':1,'vida_maxima':31},[13+adjust,6,31//den],[8+3+2+adjust,3+2+1,31//den],'R44 itens 24/188; I002')
case('T06','Autorreparo mantém 30%',{'maximo':31},9,31*30//100,'A055; I002')
for ess,n,expected in [(3,2,3),(3,10,5),(4,10,8),(5,18,13),(6,30,27)]:
 marks=sum(n>=v for v in [6,10,14,18,22,26,30])
 case('T07','Núcleo Dependente',{'essencia':ess,'nivel':n},expected,ess+marks*(ess//2),'A053')
for normal,temp,expected in [(0,0,True),(0,1,False),(1,0,False)]:
 case('T07','Inatividade e energia temporária',{'PE':normal,'temporarios':temp},expected,normal+temp==0,'A059')
case('T08','Reserva Impregnada mínimos separados',{'nivel':1,'essencia':0},2,max(1,1//2)+max(1,0//2),'A066')
case('T10','Ensaio e desvantagem',{'preparo':[5,12,17],'gasto':17,'outro_d20':6},[12,6],[sorted([5,12,17])[-2],min(17,6)],'A081')
case('T10','Entendimento Tácito bônus próprios',{'naturais':[6,15],'bonus':[2,7]},[17,22],[max(6,15)+b for b in [2,7]],'A084/A085')
case('T10','Leitura a Dois substitui bônus',{'d20':9,'proprio':2,'emprestado':7},16,9+7,'A085')
case('T12','Saída Elevada',{'classes':list(range(1,8))},[1,1,1,2,2,3,3],[max(1,c//2) for c in range(1,8)],'A092')
case('T14','Sobrecarga arredonda custo-base',{'base':9,'desconto_ignorado':3},5,math.ceil(9/2),'A099')
case('T13','Exaurido: descanso não é dividido novamente',{'maximo':41,'vida':7},17,min(41,7+max(1,41//4)),'A095/A096')
case('T13','Exaurido cura positiva',{'curas':[1,3,8]},[1,1,4],[max(1,v//2) for v in [1,3,8]],'A095/A096')
case('T14','Recuperação Abundante',{'maximoPE':41},16,max(1,41*40//100),'A099')
# Gabarito literal independente da função calculadora: nível, Classe, Maestria, Saída, usos.
for n,c,m,s,u in [(1,1,1,1,1),(2,1,1,1,1),(5,2,1,1,1),(6,2,1,1,1),(9,3,1,1,1),(10,3,2,1,2),(13,4,2,2,2),(14,4,2,2,2),(17,5,2,2,2),(18,5,3,2,3),(21,6,3,3,3),(22,6,3,3,3),(25,6,3,3,3),(26,7,4,3,4),(30,7,4,3,4)]:
 case('T09/T12/T16','Marco de progressão',{'nivel':n},[c,m,s,u],[classe(n),maestria(n),max(1,classe(n)//2),maestria(n)],'Progressão vigente; A071/A092')
# Cenários de leitura: gabaritos separados de cálculos e sem alegar execução humana.
scenarios=[
('T02','Kata acerto/TR/Automático','2 PE, primeira resolução ofensiva de um defensor; TR sem penalidade extra.','A028–A030'),
('T02','Estudar e reencontro','Teste inicial bem-sucedido; memória por portador/perfil, sem reinício por cena.','A028/A030'),
('T02','Terceiro assume ataque','Intervenção preservada; conferir suscetibilidade do alvo efetivo.','A021/A029'),
('T03/T15','Duas aplicações entre começos de turno','Tentativa e Erro só pode alterar uma; não é uso renovado no turno de cada criatura.','A037'),
('T06','Ferramentas Integradas + criar entidade','Vantagem por cena não vale para criação R44; vale no reparo elegível.','A056 e R44 item190'),
('T06','Falha de reparo e Manutenção Precisa','Mesma tentativa, uma recuperação; não autoriza novo reparador a repetir de novo.','A052/I002'),
('T07','Alma em PV e Integridade','Mantém dano em PV, sem conversão em PE; perda exclusiva de Integridade não se aplica.','A057'),
('T07','PE volta após derrota por PV','Reativação da energia não remove queda/derrota ou inconsciência independentes.','A059'),
('T08','Conflito e Coexistência','Alternativas exclusivas; menor exclusiva da outra modalidade não é elegível.','A063/A067'),
('T08','Resposta à invasão durante turno do agressor','Resolve original primeiro; medo/imunidade até fim do turno seguinte, não do atual.','A070'),
('T09','Experiência Transmitida e Preservada','Uso do aliado consome estoque comum; falha do aliado não ativa preservação.','A076'),
('T10','Cofre e nível alto','Nível não fornece patente; grau 1 ainda exige feitos e autorização.','A086/A087'),
('T11','CE4 na criação','Um, fora do repertório e dos cinco pagos; três conceitos não importam parâmetros candidatos.','A088/I001/A090'),
('T12','Saída Elevada e limite de Melhorias','Pontos só para Melhorias; não amplia quantidade, teto ou Famílias; não vale para Máximas/Manejos.','A092'),
('T13','Corpo real e marionete','Defesa0/sem Bloquear do corpo real não se transfere à Defesa própria da entidade.','A096'),
('T14','Reserva Condensada','Quantidade/ocasião/máximo com mestre; energia temporária de Último Fôlego não pode ser armazenada.','A097/A098'),
('T14','Prática Cotidiana','Dois Classe0 adicionais em qualquer Forma normalmente permitida.','A100'),
('T15','Dia e descanso longo','Dormir em missão não concede longo; estoques de dia e longo conservam renovações diferentes.','A071/A079 e Descansos'),
('T16','Bênçãos e aptidões','Nova Origem não duplica gratuitas; limitações de rota permanecem.','A004/A031/A047')]
(R/'CENARIOS-DE-LEITURA.json').write_text(json.dumps([dict(grupo=g,caso=n,gabarito=e,fonte=s,tipo='inspeção de regra; sem leitor humano',estado='gabarito definido antes da redação') for g,n,e,s in scenarios],ensure_ascii=False,indent=2)+'\n')
(R/'TESTES-CALCULOS.json').write_text(json.dumps({'metodo':'Enumeração e cálculo determinístico; não é playtest ou prova de equilíbrio','casos':rows,'total':len(rows),'falhas':sum(not r['passou'] for r in rows)},ensure_ascii=False,indent=2)+'\n')
assert all(r['passou'] for r in rows)
print(len(rows),'casos de cálculo aprovados;',len(scenarios),'cenários com gabarito para revisão textual.')

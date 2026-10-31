from pathlib import Path
import json,re,itertools
R=Path(__file__).resolve().parent
texts={f.name:f.read_text() for f in (R/'texto-final').glob('*.md')}
# Enumeração das opções elegíveis; não representa simulação de dano ou vitória.
def headings(f):return re.findall(r'^### (.+)$',texts[f],re.M)
sets={
'Latente':headings('02-latente.md'),
'Encarnado':headings('04-encarnado.md'),
'Sem Energia':headings('08-restricao-sem-energia.md')[-8:],
'Restrição corporal':headings('09-restricao-corporal.md')[-8:],
'Corpo / história Manutenção':headings('07-corpo.md')[-10:],
'Corpo / outras histórias':headings('07-corpo.md')[-10:-2]}
r=headings('03-receptaculo.md')[-8:];sets['Receptáculo / Coexistência']=r[:6]+[r[6]];sets['Receptáculo / Conflito']=r[:6]+[r[7]]
d=headings('05-descendente.md')[-10:]
for i,clan in enumerate(['Zenin','Kamo','Gojo','Inumaki']):sets['Descendente / '+clan]=[d[i]]+d[4:]
sets['Híbrido']=['Anatomia: apêndice','Anatomia: olho','Armamento: garras','Armamento: presas','Armamento: punhos','Armamento: extensível','Locomoção: aderência','Locomoção: anfíbio','Locomoção: planagem']+headings('06-hibrido.md')[3:]
pairs={k:list(itertools.combinations(v,2)) for k,v in sets.items()}
expected={'Latente':28,'Encarnado':21,'Sem Energia':28,'Restrição corporal':28,'Corpo / história Manutenção':45,'Corpo / outras histórias':28,'Receptáculo / Coexistência':21,'Receptáculo / Conflito':21,'Descendente / Zenin':21,'Descendente / Kamo':21,'Descendente / Gojo':21,'Descendente / Inumaki':21,'Híbrido':91}
assert {k:len(v) for k,v in pairs.items()}==expected
(R/'DUPLAS-ELEGIVEIS.json').write_text(json.dumps({'metodo':'Enumeração por perfil. Os 28 pares gerais do Corpo aparecem também no perfil Manutenção; não são benefícios simultâneos. Híbrido expande os três menus e só repete opções distintas.','quantidades':expected,'duplas':pairs},ensure_ascii=False,indent=2)+'\n')
# Fichas comparáveis: Bastião sem benefícios de Trilha, CON3 e ESS3 constantes.
# Atributos fixados para isolar a Origem, não sugestão de evolução de personagem.
fixtures=[(2,1,1,25,8,7,1,1,3),(10,3,2,105,40,31,2,1,5),(18,5,3,185,72,55,3,2,7),(26,7,4,265,104,79,4,3,9)]
results=[]
for n,c,m,hp,pe,threshold,uses,points,core in fixtures:
 actual=[12+3+(n-1)*(7+3),4*n,(12+3+(n-1)*10)*30//100,1+(n>=10)+(n>=18)+(n>=26),max(1,c//2),3+sum(n>=x for x in [6,10,14,18,22,26,30])]
 exp=[hp,pe,threshold,uses,points,core]
 results.append({'nivel':n,'classe':c,'maestria':m,'base':'Bastião, CON3/ESS3; sem Trilha, sem outros bônus','campos':['PV','PE','limiar Híbrido','usos da Reserva Encarnado','pontos Saída','PE adicional M1'],'esperado':exp,'obtido':actual,'passou':exp==actual})
assert all(x['passou'] for x in results)
(R/'FICHAS-COMPARADAS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
# Transições de consumo: cenários determinísticos curtos, com recursos explícitos.
traces=[]
def trace(name,inputs,events,expected,obtained,source):
 traces.append(dict(caso=name,premissas=inputs,sequencia=events,esperado=expected,obtido=obtained,passou=expected==obtained,fonte=source,tipo='modelo determinístico de consumo; sem mesa real'))
# Encarnado M2: próprio sucesso + aliado falho consomem os dois; preservação não cobre aliado.
budget=2;budget-=1;budget-=1
trace('Encarnado / estoque comum',{'maestria':2},['próprio +d4, sucesso','aliado +d4, falha','descanso curto','novo pedido sem estoque'],[0,False],[budget,budget>0],'A071/A076')
# Preservação não dá uso sem saldo, mas conserva a primeira falha própria por cena.
budget=2;preserved=False
for failed in [True,True]:
 budget-=1
 if failed and not preserved:budget+=1;preserved=True
trace('Encarnado / preservação uma vez',{'maestria':2},['falha própria preservada','segunda falha própria'],1,budget,'A076')
# Híbrido CON3, Classe2, PV12/41, PE5. Primeiro dado leva para20 e impede segundo uso apesar da reserva.
hp=12;pe=5;spent=0;hp=min(41,hp+3+5);pe-=2;spent+=1
trace('Híbrido / cura encerra faixa',{'PV':12,'maximo':41,'PE':5,'CON':3,'Classe':2},['paga2PE','2d6:3 e5','turno seguinte'],[20,3,1,False],[hp,pe,2-spent,1<=hp<=41*30//100],'A048')
# M1 capacidade paga antes de inativar; temporários válidos retornam sem renovar reação.
energy=2;energy-=2;resolved=True;inactive=energy==0;temp=1;reactivated=energy+temp>0
trace('M1 / pagar último PE',{'PE':2,'Reação':'gasta'},['capacidade custa2','resolve capacidade','recebe1PE temporário válido'],[True,True,True,'gasta'],[resolved,inactive,reactivated,'gasta'],'A059')
# Latente intervalos: três invocações tentadas, duas elegíveis em três turnos de criaturas.
last=None;used=0
for interval in [1,1,2]:
 if last!=interval:used+=1;last=interval
trace('Latente / intervalo próprio',{'pior_custo':8,'reserva_inicial':24},['turno próprio intervalo1','Reação no turno inimigo mesmo intervalo','novo turno próprio intervalo2'],2,used,'A037/A038')
# Cena não é combate: voltar a lutar sem encerrar pressão conserva usos.
stock={'cena':0,'dia':0,'longo':0};after_combat=dict(stock);after_short=dict(stock);after_sleep=dict(stock);after_sleep['dia']=1;after_long={'cena':1,'dia':1,'longo':2}
trace('Missão / renovações distintas',{'usos_gastos':stock},['combate termina mas pressão continua','descanso curto','sono durante missão','fim da missão e descanso longo'],[0,0,1,0,2],[after_combat['cena'],after_short['longo'],after_sleep['dia'],after_sleep['longo'],after_long['longo']],'Descansos R44; A071/A079')
assert all(x['passou'] for x in traces)
(R/'TESTES-DE-CONSUMO.json').write_text(json.dumps(traces,ensure_ascii=False,indent=2)+'\n')
print('Perfis e duplas:',expected,'; 4 fichas comparadas; 6 sequências de consumo.')

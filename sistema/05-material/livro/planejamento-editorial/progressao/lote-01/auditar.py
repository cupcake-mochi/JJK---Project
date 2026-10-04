"""R21: extrai as tabelas candidatas e confere progressão, XP e regularizações.
Escreve apenas evidencias/AUDITORIA.json no próprio lote. Não altera fontes.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib,json,re
B=Path(__file__).resolve().parent;P=next(p for p in B.parents if p.name=='planejamento-editorial');R=next(p for p in P.parents if (p/'sistema').is_dir());F=B/'PROGRESSAO.md';s=F.read_text();checks=[];cases=[]
def ck(n,ok,why=''):checks.append(dict(nome=n,passou=bool(ok),motivo=why))
def case(n,v,e,w):cases.append(dict(nome=n,obtido=v,esperado=e,motivo=w,passou=v==e));ck(n,v==e,w)
def xp_cost(n):return 200 if n==2 else (min(17,3+2*((n-2)//3))*100 if 3<=n<30 else None)
def reward(base,ordinal,failure=Q(1),bonus=Q(1)):
 raw=Q(base)*failure*bonus/Q(2**max(0,ordinal-2));return max(1,int(raw)) if raw>0 else 0
M=[6,10,14,18,22,26,30]
def curve(n):
 marcos=sum(n>=m for m in M)
 return [n,1+sum(n>=m for m in [10,18,26]),2+n//2+marcos,1+marcos,max(c for g,c in [(1,1),(5,2),(9,3),(13,4),(17,5),(21,6),(26,7)] if n>=g),1+sum(n>=g for g in [7,13]),2+sum(n>=g for g in [5,11,17])]
def levelup(level,balance,received,feat=True):
 total=balance+received
 if level>=30:return(level,total)
 if level==20 and not feat:return(level,total)
 cost=xp_cost(level)
 return(level+1,total-cost) if cost is not None and total>=cost else(level,total)
def resources(oldmax,cur,newmax,pv=False,growth=False):
 if pv and cur==0:return 0
 return min(newmax,cur+(max(0,newmax-oldmax) if growth else 0))
def hp(n,con,initial=8,gain=5):return initial+con+(gain+con)*(n-1)
def slots(n):return curve(n)[2]
def keep_entities(groups,free):
 # Duplicação encerrada: uma entidade por vaga, sem apagar as fichas excedentes.
 current=[g[0] for g in groups];excess=[name for g in groups for name in g[1:]]
 current+=excess[:free];return(current,excess[free:])
rows=[]
for ln in s.splitlines():
 if re.match(r'^\| \d+ \|(?: \d+ \|){6}$',ln):rows.append([int(x) for x in re.findall(r'\d+',ln)])
case('Trinta níveis completos',[x[0] for x in rows],list(range(1,31)),'Sem linha omitida ou duplicada.')
for row in rows:case(f'Progressão nível {row[0]}',row,curve(row[0]),'Reconstrução por calendários dos donos, não cópia da tabela da candidata.')
case('Custo 2→20',sum(xp_cost(n) for n in range(2,20)),14300,'Curva vigente, substitui 12.500 herdado.')
case('Custo 20→30',sum(xp_cost(n) for n in range(20,30)),16400,'Três níveis a1.500 e sete a1.700.')
case('Custo total',sum(xp_cost(n) for n in range(2,30)),30700,'XP gasto, não saldo disponível.')
expectedranges=[('2',200),('3–4',300),('5–7',500),('8–10',700),('11–13',900),('14–16',1100),('17–19',1300),('20–22',1500),('23–29',1700)]
for rng,val in expectedranges:ck('curva_publicada_'+rng,f'| {rng} | {val:,}'.replace(',','.')+' |' in s)
case('Quinta longa exata',reward(200,5),25,'12,5%, não 12%.')
case('Sexta padrão',reward(100,6),6,'Arredonda só o XP final6,25.')
case('Décima curta piso positivo',reward(50,10),1,'Resultado positivo menor que1.')
case('Zero não recebe piso',reward(100,8,Q(0)),0,'Falha sem recompensa permanece zero.')
case('Falha terceira longa',reward(200,3,Q(1,2)),50,'Metade por falha, depois metade semanal.')
case('Dobro e arredondamento único',reward(50,5,bonus=Q(2)),12,'100/8=12,5, piso12.')
case('Final de arco nível2',levelup(2,0,300),(3,100),'Um nível, sobra conservada.')
case('Saldo enorme não compra dois níveis',levelup(2,0,10000),(3,9800),'Teto por missão.')
case('Limiar bloqueia saldo',levelup(20,4000,100,False),(20,4100),'Guardar, não perderXP.')
case('Limiar liberado só um nível',levelup(20,4000,0,True),(21,2500),'Feito não exige esperar outro pagamento, mas só uma passagem no encerramento.')
case('Próxima missão pode gastar reserva',levelup(21,2500,0,True),(22,1000),'O limite é um por missão, não precisaXPnovo para saldo antigo.')
case('Topo não tem31',levelup(30,1000,300),(30,1300),'Registra história sem inventar nível31.')
case('HP Con2 nível5',hp(5,2),38,'8+2+7×4.')
case('HP Con3 nível6',hp(6,3),51,'11+8×5; recalcula todos níveis.')
case('PV parcialmente gastos',resources(38,20,51,True,True),33,'Conserva18PVde ferimentos, ganha só13de máximo.')
case('PV zero não levanta',resources(38,0,51,True,True),0,'Não substitui cura ou queda.')
case('PE zerado ganha aumento',resources(25,0,30,growth=True),5,'Exceção zero sóPV.')
case('PE parcial conserva gasto',resources(25,7,30,growth=True),12,'Continua faltando18PE.')
case('Máximo reduzido limita saldo',resources(50,48,40),40,'Nunca acima do máximo.')
case('Troca não cura pela oscilação',resources(90,resources(100,40,90,True),100,True),40,'40/100→40/90→40/100, sem aplicar delta por troca.')
case('PE troca não reabastece',resources(20,resources(30,8,20),30),8,'Benefícios novos não são recuperação.')
case('Nível antes da troca',resources(110,resources(100,40,110,True,True),100,True),50,'Crescimento legítimo dá10; troca posterior não subtrai de novo esse ganho se cabe no máximo.')
case('PV0 antes de troca',resources(110,resources(100,0,110,True,True),120,True),0,'Nem subir nem trocar levanta a zero.')
case('PE0 nível antes de troca',resources(35,resources(30,0,35,growth=True),40),5,'Recebe5por nível, zero adicional por troca.')
resource_profiles=0
for cur,newmax,pv in product(range(101),(60,90,100,150),(False,True)):
 after=resources(100,cur,newmax,pv);back=resources(newmax,after,100,pv)
 assert after<=cur and back<=cur
 resource_profiles+=1
ck('Oscilação de máximos nunca recupera',resource_profiles==808,'101saldos×4máximos×PV/PE; a exceção de crescimento não é usada em ajuste.')
def domain_feat(complete,conscious,can_act,zero_before):return complete and conscious and can_act
case('Domínio socorrido antes da saída',domain_feat(True,True,True,True),True,'Queda anterior não invalida o resultado final.')
case('Domínio ainda em Insistir',domain_feat(True,True,True,True),True,'Apto a agir e consciente; depende da regra futura de Morrendo para seu estado.')
case('Domínio sai inconsciente',domain_feat(True,False,False,True),False,'Não satisfaz sair de pé.')
case('Domínio incompleto não concede feito',domain_feat(False,True,True,False),False,'Exige Expansão completa.')

case('Duplas sem vagas novas',keep_entities([['ave','cão'],['vigia','serpente']],0),(['ave','vigia'],['cão','serpente']),'Dois disponíveis, dois registros suspensos.')
case('Duplas com uma vaga livre',keep_entities([['ave','cão'],['vigia','serpente']],1),(['ave','vigia','cão'],['serpente']),'Uma vaga recupera sóuma entidade.')
case('Corpos redução de capacidade',[3+4,3+2],[7,5],'Total ativos+inativos, não só ativos.')
case('Leque base30',slots(30),24,'Ganhos separados não aumentam capacidade comum.')
# Exhaust all choices: gain baseline before optional Refino, duplicate purchase at cap.
paths=[]
for seq in product('CRL',repeat=7):
 ref=1;attrs=9;apts=0;freepass=0;applications=0;skills=0
 for choice in seq:
  attrs+=1;ref=min(10,ref+1)
  if choice=='C':attrs+=1;skills+=1
  elif choice=='R':
   if ref>=10:apts+=2
   else:ref+=1;apts+=1
  else:freepass+=1;applications+=1
 assert 1<=ref<=10 and 16<=attrs<=23 and 5+freepass<=12
 paths.append(dict(escolhas=''.join(seq),refino=ref,pontos_atributo=attrs,aptidoes=apts,passivas_concedidas=freepass,aplicacoes_adicionais=applications,treinos=skills))
case('Sempre Refino aptidões',next(x['aptidoes'] for x in paths if x['escolhas']=='RRRRRRR'),10,'Gratuito primeiro; escolhas22/26/30 dão2.')
case('Sempre Corpo atributo',next(x['pontos_atributo'] for x in paths if x['escolhas']=='CCCCCCC'),23,'Nove iniciais, sete comuns e sete escolhas.')
case('Sempre Leque Passivas',5+next(x['passivas_concedidas'] for x in paths if x['escolhas']=='LLLLLLL'),12,'Cinco pagas e sete em vagas concedidas.')
# Timing tables are expectation models, not simulated calendar/playtest.
times=[]
for freq in [Q(1,2),Q(1),Q(2),Q(3),Q(4)]:
 eq=sum(Q(1,2**max(0,i-2)) for i in range(1,int(freq)+1))+(freq-int(freq))
 m20=Q(14300)/(Q(425,4)*eq*Q(52,12));m30=m20+Q(16400)/(240*eq*Q(52,12))
 standard20=Q(14300)/(100*eq*Q(52,12));standard30=Q(30700)/(100*eq*Q(52,12))
 times.append(dict(frequencia=float(freq),equivalente=float(eq),meses20=round(float(m20),1),meses30=round(float(m30),1),padrao20=round(float(standard20),1),padrao30=round(float(standard30),1)))
case('Ritmo2sem mistura',[(t['meses20'],t['meses30']) for t in times if t['frequencia']==2],[(15.5,23.4)],'Média106,25 antes20 e240depois, não promessa.')
case('Ritmo2sem só padrão',[(t['padrao20'],t['padrao30']) for t in times if t['frequencia']==2],[(16.5,35.4)],'Contraprova de hipótese da faixa final.')
case('Salário participação3',[float(Q(1,4)+Q(3,4)*min(Q(k,3),1)) for k in range(5)],[.25,.5,.75,1.,1.],'Fatias da parcela restante, teto100%.')
case('Marca de mestre',Q(12,3),4,'X/Ymeses, nãoXparaquemmestraY.')
for source in json.loads((B/'FONTES.json').read_text())['fontes_publicadas']:
 ck('fonte_intacta_'+source['arquivo'],hashlib.sha256((R/source['arquivo']).read_bytes()).hexdigest()==source['sha256'])
# 14 até 04/10/2026; a página Ritmo de campanha saiu do livro do jogador (D15). O modelo de tempo abaixo continua como conta de projeto.
ck('treze_paginas',len(re.findall(r'<!-- page:',s))==13)
ck('titulos_diretos',not re.search(r'^#+\s+(?:A|O|As|Os)\s|^#+.*como ler',s,re.M|re.I))
contracts=['no máximo um nível por missão','14.300','lista é fechada','não libere vários níveis','cada entidade por espaço passa a exigir','zero de vida permanece a zero']
def present(txt):return [x.casefold() in txt.replace('**','').casefold() for x in contracts]
for n,ok in zip(contracts,present(s)):ck('invariante_'+n,ok)
mutations=[('14.300','12.500'),('A lista é fechada.','A lista tem exemplos.'),('no máximo um nível por missão concluída','no máximo três níveis por missão concluída'),('Quem está a zero de vida permanece a zero','Quem está a zero de vida recupera tudo')]
for old,new in mutations:ck('mutacao_'+old,not all(present(s.replace(old,new))))
report=dict(sha256_texto=hashlib.sha256(F.read_bytes()).hexdigest(),aprovado=all(x['passou'] for x in checks),quantidades=dict(checks=len(checks),casos=len(cases),sequencias_marcos=len(paths),perfis_ritmo=len(times),mutacoes=len(mutations),perfis_saldo=resource_profiles),verificacoes=checks,casos=cases,modelos=dict(marcos=paths,tempo=times),limites=['Sem playtest; tempos são modelos de média e não calendário simulado.','Conservação de recursos e regularização de ficha são fechamentos candidatos, registrados em alterações.','Conferidores legados verificam fontes históricas, não certificam este manuscrito.'])
# JSON-safe Fractions only arise in an integral illustrative case.
def serial(o):return int(o) if isinstance(o,Q) and o.denominator==1 else float(o)
(B/'evidencias/regras-verificadas.json').write_text(json.dumps({'ok':report['aprovado'],'sha256_texto':report['sha256_texto'],'casos':cases,'auditoria':'AUDITORIA.json','limites':report['limites']},ensure_ascii=False,indent=2,default=serial)+'\n')
(B/'evidencias/auditoria-numerica.json').write_text(json.dumps({'ok':report['aprovado'],'sha256_texto':report['sha256_texto'],'manuscritos_auditados':{str(F.relative_to(R)):report['sha256_texto']},'auditoria':'AUDITORIA.json','quantidades':report['quantidades'],'modelos':report['modelos'],'limites':report['limites']},ensure_ascii=False,indent=2,default=serial)+'\n')
(B/'evidencias/AUDITORIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=serial)+'\n');print(json.dumps(dict(aprovado=report['aprovado'],quantidades=report['quantidades'],falhas=[x for x in checks if not x['passou']]),ensure_ascii=False,indent=2));raise SystemExit(0 if report['aprovado'] else 1)

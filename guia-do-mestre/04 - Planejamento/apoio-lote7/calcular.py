"""Recortes finitos de L7. Não é motor de combate nem estima dificuldade geral.
Enumera dados e estados declarados; sem sorteios. --salvar grava resultados.json.
"""
from collections import defaultdict
from itertools import product
from functools import lru_cache
from pathlib import Path
import json,math,sys
HERE=Path(__file__).absolute().parent
def checked(d):
 assert abs(sum(d.values())-1)<1e-8
 assert all(v>=0 for v in d.values())
 return dict(d)
@lru_cache(None)
def dice(n,sides):
 d={0:1.0}
 for _ in range(n):
  z=defaultdict(float)
  for x,p in d.items():
   for y in range(1,sides+1):z[x+y]+=p/sides
  d=dict(z)
 return checked(d)
def add(a,b):
 z=defaultdict(float)
 for x,p in a.items():
  for y,q in b.items():z[x+y]+=p*q
 return checked(z)
def average(d):return sum(x*p for x,p in d.items())
def fail(bonus,cd,adv=False):
 f=sum(x+bonus<cd for x in range(1,21))/20
 return f*f if adv else f
@lru_cache(None)
def attack(atk,defense,n,sides,fixed=0,channel=0,blocked=False,duro=0,adv=False):
 # Ataque: 20 natural crítico; não há falha automática no 1 na R53.
 # Duro de Matar só entra nesta comparação quando se escolheu Bloquear.
 rolls=[(x,.05) for x in range(1,21)] if not adv else [(max(a,b),.0025) for a in range(1,21) for b in range(1,21)]
 blocks=[(0,0,defense,1)] if not blocked else [(a,b,a+b+defense-11,.01) for a in range(1,11) for b in range(1,11)]
 weights=defaultdict(float)
 for x,p in rolls:
  for a,b,dc,q in blocks:
   crit=x==20;hit=crit or (not(a==b==10) and ((blocked and a==b==1) or x+atk>=dc))
   rd=a+b+duro if hit and blocked and duro else 0
   weights[(hit,crit,rd)]+=p*q
 out=defaultdict(float)
 for (hit,crit,rd),p in weights.items():
  if not hit:out[0]+=p;continue
  d=add(dice(n*(2 if crit else 1),sides),dice(channel,4)) if channel else dice(n*(2 if crit else 1),sides)
  for v,q in d.items():out[max(0,v+fixed-rd)]+=p*q
 return checked(out)
def area(n,cd,tr,adv=False,rd=0):
 out=defaultdict(float);f=fail(tr,cd,adv)
 for v,p in dice(n,8).items():
  out[max(0,v-rd)]+=p*f;out[max(0,math.ceil(v/2)-rd)]+=p*(1-f)
 return checked(out)
LEVELS=[2,6,10,15,20,22,26,30]
PROGRESSION={2:(1,1,1),6:(1,2,2),10:(2,3,3),15:(2,4,4),20:(3,5,5),22:(3,6,6),26:(4,7,7),30:(4,8,7)}
CANDIDATES={2:[16,24,32],6:[48,72,108],10:[90,140,200],15:[140,200,280],20:[180,260,360],22:[220,320,440],26:[250,360,500],30:[250,360,500]}
def profile(level,path):
 a={'Bastiao':[3,2,2,1,1],'Emanador':[0,2,2,3,2],'Guia':[0,2,2,2,3]}[path][:]
 main={'Bastiao':0,'Emanador':3,'Guia':4}[path];side={'Bastiao':3,'Emanador':4,'Guia':3}[path]
 for milestone in [6,10,14,18,22,26,30]:
  if milestone>level:break
  if milestone<=14:a[main]+=1;a[2]+=1
  elif milestone==18:a[2]+=1;a[1]+=1
  else:a[1]+=1;a[side]+=1
 assert max(a)<=6 and sum(a)==9+2*sum(m<=level for m in [6,10,14,18,22,26,30])
 m,r,c=PROGRESSION[level];initial,gain,ep={'Bastiao':(12,7,4),'Emanador':(6,4,6),'Guia':(8,5,5)}[path]
 return dict(nivel=level,caminho=path,atributos=a,maestria=m,refino=r,classe=c,PV=initial+a[2]+(gain+a[2])*(level-1),PE=ep*level,integridade=20+(a[4]+5)*(level-1),defesa=11+a[1],ataque=a[main]+m,CD=8+a[main]+m,TR_fisico=(a[0]+m if path=='Bastiao' else a[1]+m if path=='Emanador' else a[1]),canalizar=1 if r<=2 else 2 if r<=5 else 3,ataques_na_padrao=2 if path=='Bastiao' and level>=7 else 1)
PROFILES=[profile(n,p) for n in LEVELS for p in ['Bastiao','Emanador','Guia']]
@lru_cache(None)
def group(level,defense,mixed=False,boost=False):
 p=profile(level,'Bastiao');c=p['classe'];atk=p['ataque'];spell=attack(atk,defense,3*c,8)
 if not mixed:return [spell,spell,spell]
 sw=attack(atk,defense,1,8,p['atributos'][0],p['canalizar'],adv=boost)
 other=attack(atk,defense,1,8,p['atributos'][0],p['canalizar'])
 return [sw]+([other] if level>=7 else [])+[spell,spell]
def cdf(d,below):return sum(p for x,p in d.items() if x<below)
rows=[]
for level in LEVELS:
 for defense in [13,16,19]:
  for mixed in [False,True]:
   d={0:1};waves=[]
   for wave in range(2):
    for attack_d in group(level,defense,mixed):d=add(d,attack_d)
    waves.append(d)
   for hp in CANDIDATES[level]:rows.append(dict(nivel=level,defesa=defense,misto=mixed,PV=hp,integridade=hp//2,sobrevive=[cdf(x,hp) for x in waves],media_por_conjunto=average(waves[0])))
defense_study=[]
for level in [10,15,20,22,26,30]:
 p=profile(level,'Bastiao');atk=p['ataque'];d=p['defesa'];con=p['atributos'][2]
 for block,duro in [(False,0),(True,0)]+([(True,con)] if level>=15 else []):
  result=attack(atk,d,1,8,p['atributos'][0],p['canalizar'],block,duro)
  defense_study.append(dict(nivel=level,ataque=atk,defesa=d,bloquear=block,duro=duro,media=average(result),chance_dano_positivo=1-result.get(0,0)))
support_adv=[]
for level in [10,15,20,22,26,30]:
 support_adv.append(dict(nivel=level,media_normal=sum(average(d) for d in group(level,16,True)),media_com_um_impulso=sum(average(d) for d in group(level,16,True,True))))
# Um único aplicador de Toca a Alma a preço normal, dois usos. Os outros
# quatro feitiços do conjunto são dano comum. Sem resposta ativa do alvo.
soul=[]
for level,hp in [(10,140),(15,200),(20,260),(22,320),(26,360),(30,360)]:
 p=profile(level,'Emanador');c=p['classe'];n=(3*c-math.ceil(c/2))//2;atk=p['ataque'];inte=hp//2
 sd=add(attack(atk,16,n,8),attack(atk,16,n,8));normal={0:1}
 for _ in range(4):normal=add(normal,attack(atk,16,3*c,8))
 # CDF para não multiplicar toda a distribuição bidimensional.
 max_d=max(normal);acc=[];total=0
 for i in range(max_d+1):total+=normal.get(i,0);acc.append(total)
 def normal_below(x):return 0 if x<=0 else acc[min(x-1,max_d)]
 live=[(loss,prob*normal_below(hp-loss)) for loss,prob in sd.items() if loss<inte]
 soul.append(dict(nivel=level,PV=hp,integridade=inte,classe=c,dados_Alma=n,sobrevive_PV_e_integridade=sum(q for _,q in live),vivo_em_estagio_1_ou_maior=sum(q for loss,q in live if loss>=inte/4),vivo_em_estagio_2_ou_maior=sum(q for loss,q in live if loss>=inte/2),vivo_em_estagio_3=sum(q for loss,q in live if loss>=3*inte/4)))
# Comparação condicional de oportunidades: grupo age primeiro; permanece
# apto a repetir sua ofensiva. Inimigos recebem dano real e o apoio pode curar.
# Não converte sobrevivência em duração de um combate integral.
def foe_window(mixed,boss_hp=None,heals=True):
 # (apoioPV, vigiaPV, apoioPE); no chefe, apenas o campo vigia é usado.
 states={(0,boss_hp,0):1.0} if boss_hp else {(80,120,26):1.0};result=[]
 for wave in range(1,4):
  for d in group(15,14,mixed):
   nxt=defaultdict(float)
   for (a,b,e),p in states.items():
    for damage,q in d.items():
     na=max(0,a-damage) if a else 0;nb=b if a else max(0,b-damage)
     nxt[(na,nb,e)]+=p*q
   states=checked(nxt)
  boss_alive=sum(p for (a,b,e),p in states.items() if b>0) if boss_hp else 0
  both=sum(p for (a,b,e),p in states.items() if a>0 and b>0)
  support=sum(p for (a,b,e),p in states.items() if a>0)
  attacker=sum(p for (a,b,e),p in states.items() if b>0)
  expected_heal=0;impulse=0;nxt=defaultdict(float)
  for (a,b,e),p in states.items():
   if not boss_hp and heals and 0<a<80 and e>=12:
    expected_heal+=p
    for amount,q in dice(8,8).items():nxt[(min(80,a+amount),b,e-12)]+=p*q
   else:
    if not boss_hp and a>0 and b>0 and e>=3:impulse+=p;nxt[(a,b,e-3)]+=p
    else:nxt[(a,b,e)]+=p
  states=checked(nxt)
  result.append(dict(conjunto=wave,chefe_ativo=boss_alive,ambos_ativos=both,apoio_ativo=support,atacante_ativo=attacker,acoes_de_cura_esperadas=expected_heal,impulsos_esperados=impulse,pelo_menos_um_ativo=sum(p for (a,b,e),p in states.items() if a or b)))
 return result
composition=[]
for mixed in [False,True]:
 for label,hp,heal in [('chefe200',200,False),('chefe280',280,False),('dupla_sem_cura',None,False),('dupla_com_cura',None,True)]:composition.append(dict(misto=mixed,caso=label,resultados=foe_window(mixed,hp,heal)))
pressure=[]
for path in ['Bastiao','Emanador','Guia']:
 p=profile(15,path)
 for adv in [False,True] if path=='Bastiao' else [False]:
  for rd in [0,6]:
   d=area(6,15,p['TR_fisico'],adv,rd)
   pressure.append(dict(caminho=path,PV=p['PV'],TR=p['TR_fisico'],vantagem=adv,reducao=rd,media=average(d),falha=fail(p['TR_fisico'],15,adv)))
# Sequência concentrada: Insistir mantém o alvo consciente. Nenhuma volta
# temporal, ação de cura, Kokusen ou redução entre quatro ataques declarados.
def concentrated(sequela):
 states={(24,False,0):1.0};rows=[];d=attack(6,13,1,8,4,2)
 for i in range(1,5):
  nxt=defaultdict(float)
  for (hp,dying,w),p in states.items():
   for damage,q in d.items():
    if dying:
     nxt[(0,True,max(0,w-(damage>0)))]+=p*q
    elif damage>=hp:nxt[(0,True,3-sequela)]+=p*q
    else:nxt[(hp-damage,False,0)]+=p*q
  states=checked(nxt)
  rows.append(dict(ataques=i,zero_PV=sum(p for (h,m,w),p in states.items() if m),derrotado=sum(p for (h,m,w),p in states.items() if m and w==0)))
 return rows
focus=[dict(sequelas=s,resultados=concentrated(s)) for s in [0,2]]
tests=[]
def test(label,actual,expected,tol=1e-8):
 assert abs(actual-expected)<tol,(label,actual,expected);tests.append(label)
test('6d8 média',average(dice(6,8)),27)
test('Carregador +4 Def13 média',average(attack(4,13,1,4,3)),3.425)
test('Pancada antiga +5 Def13 média',average(attack(5,13,2,6,4)),7.5)
test('Acerto Bloquear antigo 59,85%',1-attack(4,13,1,4,3,blocked=True).get(0,0),.5985)
test('Emanador6 PV',profile(6,'Emanador')['PV'],44)
test('Guia6 Integridade',profile(6,'Guia')['integridade'],65)
test('Bastiao30 PV',profile(30,'Bastiao')['PV'],395)
test('Físico+4 CD15 com vantagem',fail(4,15,True),.25)
for p in PROFILES:assert p['PE']>=2*3*p['classe']
for p in [p for p in PROFILES if p['nivel']==15]:assert p['PE']>=3*3*p['classe']
# Conferência independente por resultados elementares de um golpe.
# Não chama attack(), add() ou dice() para reconstruir a redução.
direct_total=0.0
for roll,ba,bb in product(range(1,21),range(1,11),range(1,11)):
 hit=roll==20 or ((ba,bb)!=(10,10) and ((ba,bb)==(1,1) or roll+8>=ba+bb+2))
 if not hit:continue
 weapon=[a+b for a,b in product(range(1,9),repeat=2)] if roll==20 else list(range(1,9))
 direct_total+=sum(max(0,w+c+d+6-ba-bb-5) for w,c,d in product(weapon,range(1,5),range(1,5)))/(2000*len(weapon)*16)
test('Duro de Matar por enumeração independente',average(attack(8,13,1,8,6,2,True,5)),direct_total)
for level in LEVELS:
 for mixed in [False,True]:
  subset=[r for r in rows if r['nivel']==level and r['misto']==mixed]
  for wave in range(2):
   for hp in CANDIDATES[level]:
    vals=[r['sobrevive'][wave] for r in subset if r['PV']==hp]
    assert all(a<=b+1e-8 for a,b in zip(vals,vals[1:]))
   for defense in [13,16,19]:
    vals=[r['sobrevive'][wave] for r in subset if r['defesa']==defense]
    assert all(a<=b+1e-8 for a,b in zip(vals,vals[1:]))
for row in rows:assert 0<=row['sobrevive'][1]<=row['sobrevive'][0]<=1+1e-8
for x in composition:
 v=[r['pelo_menos_um_ativo'] for r in x['resultados']];assert all(b<=a+1e-8 for a,b in zip(v,v[1:]))
for x in focus:
 assert all(r['derrotado']<=r['zero_PV']+1e-8 for r in x['resultados'])
out=dict(metodo='Enumeração finita de recortes; sem mesa humana ou previsão de duração de combate.',perfis=PROFILES,referencias=rows,defesas=defense_study,apoio=support_adv,alma=soul,composicoes=composition,area=pressure,concentracao_de_ataques=focus,verificacoes=tests,limites=['Sem política ótima, recursos de Origem/Trilha, Kokusen, Domínio, Liberações ou Técnica Máxima.','Os perfis são recortes; os conjuntos ofensivos pressupõem ações, alvos, alcance e energia disponíveis.','A comparação de oportunidades não executa dano e controle sobre os jogadores; pode superestimar as ações ofensivas disponíveis a eles.','Duro de Matar é analisado separadamente com os dados efetivos de Bloquear, não uma redução média.','Alma pressupõe um único feitiço legal, Classe3+, Regra sobre alma e preço normal de Toca a Alma.'])
if '--salvar' in sys.argv:(HERE/'resultados.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(perfis=len(PROFILES),curvas=len(rows),verificacoes=len(tests),composicoes=composition,area=pressure,concentracao=focus),ensure_ascii=False,indent=2))

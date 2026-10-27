"""Reproduz dois percursos didáticos fixos. NÃO é motor geral da R53.
Confere aritmética, trajetos livres, ações declaradas, Reações, PE e socorro.
Dados escolhidos, sem sorteio ou inferência estatística. A revisão documental
confere permissões de ficha, escolhas não tomadas e interpretação dos efeitos.
--salvar grava somente resultados.json, sem tocar no manifesto.
"""
from pathlib import Path
import json, math, sys

HERE = Path(__file__).resolve().parent

def cell(s):
    return (ord(s[0])-64, int(s[1:]))

def label(p):
    return chr(p[0]+64)+str(p[1])

def footprint(p, size=1):
    return {(p[0]+i,p[1]+j) for i in range(size) for j in range(size)}

def distance(a,b):
    return min(max(abs(x-u),abs(y-v))*1.5 for x,y in a for u,v in b)

def dice(values,sides):
    assert all(1<=x<=sides for x in values)
    return sum(values)

class Rehearsal:
    def __init__(self,wounded=False):
        vals={'Rina':('C0',65,24,50),'Mei':('D0',44,36,55),'Akira':('F0',51,30,65),'Sineiro':('D6',108,0,54)}
        self.a={k:dict(pos=cell(p),max=h,hp=h,pe=e,integridade=i,reacao=True,sequelas=0) for k,(p,h,e,i) in vals.items()}
        if wounded:self.a['Mei']['hp']=18
        self.log=[];self.checks=[];self.active=None;self.held=None;self.prepared=False;self.opening=None;self.box='C6';self.clock=None;self.impulse=False
        self.note('Entrada',ferida=wounded)
    def ck(self,name,value):
        assert value,name
        self.checks.append(name)
    def note(self,name,**data):
        self.log.append({'evento':name,**data})
    def foot(self,n):return footprint(self.a[n]['pos'],2 if n=='Sineiro' else 1)
    def near(self,a,b,limit):self.ck(f'Alcance {a}/{b} até {limit} m',distance(self.foot(a),self.foot(b))<=limit)
    def turn(self,n,round):
        self.active=n;self.a[n].update(P=1,B=1,M=9,reacao=True)
        if n=='Akira':self.opening=None
        self.note('Turno',pessoa=n,rodada=round)
    def spend(self,n,slot):
        a=self.a[n]
        if slot=='R':
            self.ck(f'{n}: Reação disponível',a['reacao']);a['reacao']=False
        else:
            self.ck(f'{n}: {slot} disponível no próprio turno',self.active==n and a[slot]>0);a[slot]-=1
    def pe(self,n,cost):
        self.ck(f'{n}: PE para {cost}',self.a[n]['pe']>=cost);self.a[n]['pe']-=cost
    def hurt(self,n,amount):
        self.a[n]['hp']=max(0,self.a[n]['hp']-amount)
        self.note('Dano',alvo=n,dano=amount,vida=self.a[n]['hp'])
    def path(self,start,end):
        p=start;out=[]
        while p!=end:
            p=tuple(x+(1 if y>x else -1 if y<x else 0) for x,y in zip(p,end));out.append(p)
        return out
    def move(self,n,dest,mode='M',drag=False):
        a=self.a[n];start=a['pos'];end=cell(dest);path=self.path(start,end);cost=len(path)*1.5
        limits={'passo':6,'avancar':3,'imposto':6,'correr':9,'bonus':9}
        if mode in ('M','correr','bonus'):
            self.ck(f'{n}: movimento próprio no turno',self.active==n)
            self.ck(f'{n}: não está Agarrado',self.held!=n)
        if mode=='M':self.ck(f'{n}: metros disponíveis',a['M']>=cost);a['M']-=cost
        else:
            self.ck(f'{n}: limite de {mode}',cost<=limits[mode])
            if mode=='correr':self.spend(n,'P')
            if mode=='bonus':self.spend(n,'B')
        for p in path:
            delta=tuple(v-u for u,v in zip(a['pos'],p));updates={n:p}
            if drag:
                self.ck('Condução exige presa',n=='Sineiro' and self.held is not None)
                updates[self.held]=tuple(x+d for x,d in zip(self.a[self.held]['pos'],delta))
            for who,pos in updates.items():
                f=footprint(pos,2 if who=='Sineiro' else 1)
                self.ck(f'{who}: piso e porta',all((1<=x<=8 and 1<=y<=12) or (3<=x<=6 and y==0) or y<0 for x,y in f))
                for other in self.a:
                    if other==who:continue
                    of=footprint(updates.get(other,self.a[other]['pos']),2 if other=='Sineiro' else 1)
                    if who=='Sineiro' or other=='Sineiro' or p==end:
                        self.ck(f'{who}: percurso sem sobreposição com {other}',f.isdisjoint(of))
            for who,pos in updates.items():self.a[who]['pos']=pos
        if n=='Sineiro' and cost:
            self.prepared=False
            if self.held and distance(self.foot('Sineiro'),self.foot(self.held))>1.5:self.held=None
        if drag:self.near('Sineiro',self.held,1.5)
        self.note('Movimento',pessoa=n,de=label(start),para=dest,modo=mode,metros=cost)
    def attack(self,target,rolls,bonus,defense,damage,adv=0,physical=True,original=None):
        n=self.active
        if physical:self.near(n,original or target,1.5)
        else:self.near(n,target,18)
        assert all(1<=r<=20 for r in rolls)
        roll=max(rolls) if adv>0 else min(rolls) if adv<0 else rolls[0]
        self.ck('Percursos sem crítico escolhido',roll!=20)
        hit=roll+bonus>=defense
        if hit:self.hurt(target,damage)
        self.note('Ataque',origem=n,alvo=target,dados=rolls,total=roll+bonus,defesa=defense,acertou=hit)
        return hit
    def windup(self):
        self.spend('Sineiro','B');self.prepared=True
        self.note('Preparação',posicao=label(self.a['Sineiro']['pos']))
    def opening_for(self,kind,target,dest=None):
        self.spend('Akira','B');self.pe('Akira',1);self.near('Akira',target,18)
        self.opening=(kind,target,dest)
    def advance(self,n):
        self.ck('Avançar preparado e vigente',self.opening is not None and self.opening[:2]==('Avançar',n))
        if self.active!=n:self.spend(n,'R')
        dest=self.opening[2];self.opening=None;self.move(n,dest,'avancar')
    def get_box(self):
        self.ck('Caixa acessível para interação simples',self.box=='C6' and self.a['Akira']['pos']==cell('C6'))
        self.box='Akira'
    def spell(self,remodel=False,miss=False):
        self.spend('Mei','P');self.pe('Mei',7 if remodel else 6)
        hit=self.attack('Sineiro',[2 if miss else 8 if remodel else 7],5,11,dice([2,4,5,6,6] if remodel else [3,4,4,5,6],8),physical=False)
        if remodel:self.impulse=True
        return hit
    def heal(self,values):
        self.spend('Akira','P');self.pe('Akira',6);self.near('Akira','Mei',9)
        amount=dice(values,8);self.clock['tratamento']+=amount
        if self.clock['tratamento']>=self.clock['necessario']:
            self.a['Mei']['hp']=min(self.a['Mei']['max'],self.clock['tratamento']);self.a['Mei']['sequelas']+=1;self.clock['encerrada']=True
        self.note('Cura',valor=amount,vida=self.a['Mei']['hp'],**self.clock)
    def result(self):
        return {'estado_final':{k:{'posicao':label(v['pos']),'vida':v['hp'],'PE':v['pe'],'integridade':v['integridade'],'sequelas':v['sequelas']} for k,v in self.a.items()},'caixa':self.box,'socorro':self.clock,'impulso_pendente':self.impulse,'conferencias_executadas':len(self.checks),'eventos':self.log}

def first_two(s):
    s.turn('Rina',1);s.move('Rina','C6');s.spend('Rina','B');s.spend('Rina','P')
    s.ck('Provocação: 16 vence Espírito 15',11+5>14+1)
    s.attack('Sineiro',[12],5,11,dice([5],8)+4+dice([2],4))
    s.turn('Sineiro',1);s.spend('Sineiro','P');s.near('Sineiro','Rina',1.5)
    s.ck('Agarrar: 10 falha contra 13',5+5<13);s.held='Rina'
    s.attack('Rina',[8,14],5,13,math.ceil((dice([4,4],6)+4)/2),adv=1)
    s.ck('Carga da presa cabe em 9',72/12+1.3<=9)
    s.move('Sineiro','D10',drag=True);s.windup()
    s.ck('Rina claramente dentro da primeira zona',math.dist((4.5,10.5),s.a['Rina']['pos'])*1.5<3)

def akira_one(s,kind):
    s.turn('Akira',1)
    for x in ['E1','D2','C3','C4','C5','C6']:s.move('Akira',x)
    s.get_box();s.opening_for(kind,'Rina','C8' if kind=='Avançar' else None)
    if kind=='Avançar':s.advance('Rina')
    s.move('Akira','C0','correr')

def main_route():
    s=Rehearsal();first_two(s)
    s.turn('Mei',1);s.move('Mei','D6');s.ck('Empurrão acerta',s.spell());s.move('Sineiro','E10','imposto')
    s.ck('Empurrão cancela preparo e separa presa',not s.prepared and s.held is None)
    akira_one(s,'Avançar')
    s.turn('Rina',2);s.move('Rina','C4');s.spend('Rina','P') # Esquivar
    s.turn('Sineiro',2);s.move('Sineiro','D7');s.spend('Sineiro','P');s.near('Sineiro','Mei',1.5)
    s.ck('Mei resiste a Agarrar',14+3>=13)
    s.near('Rina','Mei',6);s.spend('Rina','R')
    s.attack('Rina',[17,9],5,dice([4,6],10)+2,math.ceil((dice([3,4],6)+4)/2),adv=-1,original='Mei')
    s.windup()
    s.ck('Mei dentro e Rina fora da segunda zona',math.dist((4.5,7.5),s.a['Mei']['pos'])*1.5<3 and math.dist((4.5,7.5),s.a['Rina']['pos'])*1.5>3)
    s.turn('Mei',2);s.spell(remodel=True);s.move('Mei','D2','passo');s.move('Mei','D-4')
    s.ck('Dano sozinho mantém preparo',s.prepared)
    s.turn('Akira',2);s.opening_for('Avançar','Rina','C2')
    s.ck('Rina não pode usar Avançar fora do turno sem Reação',not s.a['Rina']['reacao'])
    s.turn('Rina',3);s.advance('Rina');s.move('Rina','C-1')
    s.ck('Retirada de todos',all(s.a[n]['pos'][1]<=0 for n in ['Rina','Mei','Akira']))
    s.ck('Vida final principal',[s.a[n]['hp'] for n in ['Rina','Mei','Akira','Sineiro']]==[53,44,51,52])
    s.ck('PE final principal',[s.a[n]['pe'] for n in ['Rina','Mei','Akira']]==[24,23,28])
    return s.result()

def wounded_route():
    s=Rehearsal(True);first_two(s)
    s.turn('Mei',1);s.move('Mei','C6');s.move('Mei','C11','bonus');s.ck('Controle errou',not s.spell(miss=True))
    akira_one(s,'Resguardar')
    s.turn('Rina',2);s.spend('Rina','P');s.ck('Resguardar vigente',s.opening[:2]==('Resguardar','Rina'));s.opening=None
    s.ck('Fuga com vantagem passa',max(4,15)+5>=13);s.held=None
    # Oportunidade acontece ao deixar o alcance, no trecho C9 -> C8; não usa Atacar.
    s.move('Rina','C9');s.near('Sineiro','Rina',1.5);s.spend('Sineiro','R');s.ck('Pancada de oportunidade erra',5+5<13)
    s.move('Rina','C4');s.move('Rina','C-2','bonus')
    s.turn('Sineiro',2);s.spend('Sineiro','P');s.ck('Impacto tem preparo',s.prepared);s.prepared=False
    center=tuple(x+.5 for x in s.a['Sineiro']['pos']);meipos=s.a['Mei']['pos']
    s.ck('Mei claramente dentro do raio de 3 m',math.dist(center,meipos)*1.5<3)
    s.ck('Mei falha no TR',5+3<13);s.spend('Mei','R');s.pe('Mei',2);s.hurt('Mei',dice([6]*5,8)-3)
    s.clock={'necessario':min(math.ceil(44/3),15*2),'tratamento':0,'rodadas':3,'encerrada':False,'marca':'impacto: iniciativa 14, rodada 2'}
    s.ck('Insistir começa a zero e exige 15',s.a['Mei']['hp']==0 and s.clock['necessario']==15)
    s.turn('Mei',2);s.spell(remodel=True);s.move('Mei','C7','passo');s.move('Mei','C1');s.move('Mei','C-5','bonus')
    s.turn('Akira',2);s.heal([1,2,3,4]);s.ck('Primeira cura não encerra queda',s.a['Mei']['hp']==0 and s.clock['tratamento']==10 and s.clock['rodadas']==3)
    s.turn('Rina',3);s.turn('Sineiro',3);s.clock['rodadas']-=1;s.note('Volta ao ponto da queda',rodadas=s.clock['rodadas'])
    s.turn('Mei',3);s.impulse=False;s.turn('Akira',3);s.heal([1,1,2,4])
    s.ck('Socorro encerra com tratamento integral',s.a['Mei']['hp']==18 and s.a['Mei']['sequelas']==1 and s.clock['encerrada'] and s.clock['rodadas']==2)
    s.ck('Vida final ferida',[s.a[n]['hp'] for n in ['Rina','Mei','Akira','Sineiro']]==[59,18,51,74])
    s.ck('PE final ferida',[s.a[n]['pe'] for n in ['Rina','Mei','Akira']]==[24,21,17])
    s.ck('Aguentar exigiria reposicionamento',math.ceil(44/4)==11 and distance(footprint(cell('C0')),footprint(cell('C11')))==16.5)
    return s.result()

out={'metodo':'Percursos fixos; sem aleatoriedade; verificador parcial, não motor da R53.','principal':main_route(),'ferida':wounded_route()}
if '--salvar' in sys.argv:(HERE/'resultados.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:{'estado_final':out[k]['estado_final'],'conferencias':out[k]['conferencias_executadas']} for k in ['principal','ferida']},ensure_ascii=False,indent=2))

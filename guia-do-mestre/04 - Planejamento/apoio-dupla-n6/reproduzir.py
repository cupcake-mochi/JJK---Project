"""Reprodução parcial do percurso didático de G76. Dados fixos, sem IA.
Confere campos usados, alcance, corpos, trajetos, ações, Reações e reservas.
Permissões de capacidade, fala, visão, escolhas e efeitos omitidos dependem da
revisão documental. --salvar grava somente resultados-ensaio.json.
"""
from pathlib import Path
import json,math,sys
HERE=Path(__file__).resolve().parent

def pos(s):return (ord(s[0])-64,int(s[1:]))
def loc(p):return chr(p[0]+64)+str(p[1])
def dist(a,b):return max(abs(a[0]-b[0]),abs(a[1]-b[1]))*1.5

def dice(values,sides):
    assert all(1<=v<=sides for v in values)
    return sum(values)

class Replay:
    def __init__(self):
        self.a={}
        for name,cell,hp,pe,integ in [('Rina','C0',65,24,50),('Mei','D0',44,36,55),('Akira','F0',51,30,65),('Ren','D5',72,8,36),('Sora','F8',48,12,24)]:
            self.a[name]=dict(pos=pos(cell),hp=hp,max=hp,pe=pe,temp=0,R=True,integridade=integ)
        self.log=[];self.active=None;self.opening=None;self.impulse=False;self.olhos=False;self.case='Sora';self.count=0
    def ck(self,name,value):
        assert value,name;self.count+=1
    def event(self,name,**data):self.log.append({'evento':name,**data})
    def turn(self,name,round):
        self.ck('Participante ativo',self.a[name]['hp']>0)
        self.active=name;self.a[name].update(P=1,B=1,M=9,R=True)
        if name=='Akira':self.opening=None
        self.event('Turno',pessoa=name,rodada=round)
    def pay(self,name,slot,pe=0):
        a=self.a[name];self.ck('PE disponíveis',a['pe']>=pe)
        if slot=='R':self.ck('Reação disponível',a['R']);a['R']=False
        else:self.ck('Ação no próprio turno',self.active==name and a[slot]>0);a[slot]-=1
        a['pe']-=pe
    def near(self,a,b,limit):self.ck('Alcance',dist(self.a[a]['pos'],self.a[b]['pos'])<=limit)
    def move(self,name,path,mode='M'):
        a=self.a[name];start=a['pos'];length=len(path)*1.5
        if mode=='M':self.ck('Movimento no turno',self.active==name and a['M']>=length);a['M']-=length
        else:
            self.ck('Limite de movimento especial',length<={'Passo':6,'Empurrão':6,'Avançar':3,'Bônus':9}[mode])
            if mode=='Bônus':self.pay(name,'B')
        for i,c in enumerate(path):
            p=pos(c);self.ck('Passo adjacente',dist(a['pos'],p)==1.5)
            self.ck('Recinto ou porta',1<=p[0]<=8 and 1<=p[1]<=12 or 3<=p[0]<=6 and p[1]<=0)
            for other,b in self.a.items():
                if other==name:continue
                same=(name in ['Ren','Sora'])==(other in ['Ren','Sora'])
                self.ck('Corpos respeitados',p!=b['pos'] or same and i<len(path)-1)
            a['pos']=p
        self.event('Movimento',pessoa=name,de=loc(start),para=loc(a['pos']),metros=length,modo=mode)
    def attack(self,name,target,rolls,bonus,damage,reach,pe=0,cover=False,adv=False,original=None):
        self.pay(name,'P',pe);self.near(name,original or target,reach)
        self.ck('Dados de ataque válidos',all(1<=r<=20 for r in rolls))
        d=max(rolls) if adv else rolls[0];self.ck('Não há crítico escolhido',d!=20)
        hit=d+bonus>=13
        if hit:
            if target=='Rina' and self.olhos:damage=math.ceil(damage/2) # somente Cortante/Concussão neste percurso
            if cover:self.pay(target,'R',2);damage=max(0,damage-3)
            a=self.a[target];temp=min(a['temp'],damage);a['temp']-=temp;a['hp']=max(0,a['hp']-(damage-temp))
            if target=='Sora' and a['hp']==0:self.case=loc(a['pos'])
        self.event('Ataque',origem=name,alvo=target,acerto=d+bonus,acertou=hit,dano_apos_defesas=damage if hit else 0,vida=self.a[target]['hp'])
    def opening_to(self,kind,target,dest=None):
        self.pay('Akira','B',1);self.near('Akira',target,18);self.opening=(kind,target,dest)
    def result(self):
        return {'estado_final':{n:{'PV':a['hp'],'PE':a['pe'],'integridade':a['integridade'],'temporarios':a['temp'],'posicao':loc(a['pos'])} for n,a in self.a.items()},'estojo':self.case,'conferencias':self.count,'eventos':self.log,'limites':'Percurso com dados escolhidos; não motor completo da R53, sorteio, taxa de vitória ou teste humano.'}

s=Replay()
s.turn('Sora',1);s.pay('Sora','P',3);s.near('Sora','Ren',9);s.a['Ren']['temp']=3;s.impulse=True
s.turn('Rina',1);s.move('Rina',['C1','C2','C3','C4']);s.pay('Rina','B');s.olhos=True;s.ck('Ren resiste a Provocar',17+1>=11+5)
s.attack('Rina','Ren',[12],5,dice([5],8)+4+dice([2],4),1.5,cover=True)
s.ck('Vida temporária depois da redução',s.a['Ren']['hp']==67 and s.a['Ren']['temp']==0)
s.turn('Ren',1);s.ck('Impulso pronto',s.impulse);s.impulse=False
s.attack('Ren','Rina',[3,13],5,dice([6],8)+4+dice([3],4),1.5,adv=True)
s.turn('Mei',1);s.move('Mei',['D1','D2','D3','D4']);s.attack('Mei','Sora',[8],5,dice([6,6,5,6,6],8),18,pe=6,cover=True);s.move('Sora',['G9','H10','H11','H12'],'Empurrão')
s.ck('Empurrão rompe alcance de benefícios',dist(s.a['Ren']['pos'],s.a['Sora']['pos'])==10.5)
s.turn('Akira',1);s.move('Akira',['F1','F2','F3','F4','F5','F6']);s.attack('Akira','Sora',[6],5,0,18,pe=6);s.opening_to('Executar','Mei')
s.turn('Sora',2);s.move('Sora',['G11','F10','F9','F8']);s.pay('Sora','P',6);s.a['Sora']['hp']=min(48,s.a['Sora']['hp']+dice([3,4,5,6],8));s.ck('Cura deixa40PV e1PE',s.a['Sora']['hp']==40 and s.a['Sora']['pe']==1)
s.turn('Rina',2);s.attack('Rina','Ren',[9],5,dice([4],8)+4+dice([3],4),1.5,cover=True)
s.turn('Ren',2);s.near('Rina','Mei',6);s.pay('Rina','R');s.attack('Ren','Rina',[9],5,dice([5,6],8),18,pe=3,original='Mei');s.move('Ren',['E6','F7'],'Passo')
s.turn('Mei',2);s.ck('Executar vigente',s.opening[:2]==('Executar','Mei'));s.opening=None;s.attack('Mei','Sora',[7,14],5,dice([4,4,5,5,6],8),18,pe=6,adv=True);s.move('Sora',['G9','H10','H11','H12'],'Empurrão')
s.ck('Sora não paga Cobrir-se',s.a['Sora']['R'] and s.a['Sora']['pe']<2)
s.turn('Akira',2);s.attack('Akira','Sora',[12],5,dice([2,3,3,4,4,5],8),18,pe=6);s.opening_to('Avançar','Rina','D6');s.ck('Rina não usa a abertura fora do turno sem Reação',not s.a['Rina']['R'])
s.turn('Rina',3);s.ck('Avançar vigente',s.opening==('Avançar','Rina','D6'));s.opening=None;s.move('Rina',['D5','D6'],'Avançar');s.move('Rina',['E6']);s.attack('Rina','Ren',[12],5,dice([6],8)+4+dice([3],4),1.5)
s.turn('Ren',3);s.pay('Ren','P');s.event('Desengajar',pessoa='Ren');s.move('Ren',['G6','G5','G4','F3','F2','F1']);s.move('Ren',['F0','F-1'],'Bônus')
s.turn('Mei',3);s.event('Grupo decide não perseguir')
s.turn('Akira',3);s.move('Akira',['G7','G8','G9','G10','G11','G12']);s.ck('Objeto solto ao alcance',s.case=='H12' and dist(s.a['Akira']['pos'],pos(s.case))==1.5);s.case='Akira'
s.ck('Estado final de vida',[s.a[n]['hp'] for n in ['Rina','Mei','Akira','Ren','Sora']]==[52,44,51,46,0])
s.ck('Estado final de energia',[s.a[n]['pe'] for n in ['Rina','Mei','Akira','Ren','Sora']]==[24,24,16,1,1])
s.ck('Gastos do grupo',24+36+30-s.a['Rina']['pe']-s.a['Mei']['pe']-s.a['Akira']['pe']==26)
s.ck('Gastos da dupla',8+12-s.a['Ren']['pe']-s.a['Sora']['pe']==18)
out=s.result()
if '--salvar' in sys.argv:(HERE/'resultados-ensaio.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['estado_final','estojo','conferencias']},ensure_ascii=False,indent=2))

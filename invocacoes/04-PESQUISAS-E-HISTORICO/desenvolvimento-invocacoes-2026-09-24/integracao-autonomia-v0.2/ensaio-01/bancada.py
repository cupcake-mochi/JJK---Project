"""Bancada delimitada, não motor do Projeto M. Python 3, biblioteca padrão.

Dados forçados ilustram procedimentos; probabilidades são enumerações exatas.
Executar regrava somente resultados.json e execucao.txt nesta pasta.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
CHECKS, SCENES = [], {}


def check(name, actual, expected):
    CHECKS.append(dict(caso=name, passou=actual == expected,
                       obtido=actual, esperado=expected))


class Illegal(Exception):
    pass


class Unknown(Exception):
    pass


def need(condition, why):
    if not condition:
        raise Illegal(why)


def faces(mode):
    if mode == 'normal':
        return [(i, F(1, 20)) for i in range(1, 21)]
    choose = max if mode == 'vantagem' else min
    counts = Counter(choose(a, b) for a, b in product(range(1, 21), repeat=2))
    return [(i, F(n, 400)) for i, n in counts.items()]


def outcome(d20, bonus, defense, block=None, incapacitated=False):
    """Ataque corpo a corpo; nenhum dano auxiliar no ensaio."""
    critical = d20 == 20
    parry = block == (10, 10)
    breach = block == (1, 1)
    threshold = defense if block is None else sum(block) + defense - 11
    hit = critical or (not parry and (breach or d20 + bonus >= threshold))
    return hit, hit and (critical or incapacitated), parry, breach


def stats(mode='normal', policy='fixa', defense=16, bonus=5):
    hit = crit = parry = breach = blocks = F(0)
    for die, p in faces(mode):
        use = policy == 'sempre' or (policy == 'apos_acerto_fixo' and (die == 20 or die + bonus >= defense))
        samples = [(None, F(1))] if not use else [((a, b), F(1, 100)) for a, b in product(range(1, 11), repeat=2)]
        for block, q in samples:
            h, c, pa, br = outcome(die, bonus, defense, block)
            prob = p*q
            hit += h*prob; crit += c*prob; parry += pa*prob; breach += br*prob
            blocks += use*prob
    return dict(acerto=hit, critico=crit, aparar=parry, brecha=breach,
                dados_bloquear=2*blocks,
                dados_ataque=F(1 if mode == 'normal' else 2))


def expected(dice, flat, st):
    return (st['acerto'] + st['critico'])*F(7, 2)*dice + st['acerto']*flat


def plain(value):
    if isinstance(value, F):
        return dict(exato=str(value), decimal=float(value))
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    if isinstance(value, set):
        return sorted(value)
    return value


def numerical():
    rows = []
    for defense in [13, 16, 19]:
        for policy in ['fixa', 'sempre', 'apos_acerto_fixo']:
            for mode in ['normal', 'vantagem', 'desvantagem']:
                st = stats(mode, policy, defense)
                rows.append(dict(defesa=defense, politica=policy, modo=mode, **st,
                                 usuario=expected(3, 2, st), basica=expected(1, 1, st)))
    n, a = stats(), stats('vantagem')
    # Oráculos aritméticos independentes das funções de probabilidade.
    check('N01: acerto e crítico normais +5 vs 16', (n['acerto'], n['critico']), (F(1,2), F(1,20)))
    check('N02: vantagem por complemento de duas falhas', (a['acerto'], a['critico']), (F(3,4), F(39,400)))
    check('N03: dano pessoal inclui fixo uma vez no crítico', expected(3,2,n), F(271,40))
    check('N04: dano básico inclui fixo uma vez no crítico', expected(1,1,n), F(97,40))
    check('N05: 20 vence duplo 10', outcome(20,5,16,(10,10))[:2], (True,True))
    check('N06: Aparar vence acerto comum', outcome(19,5,16,(10,10))[0], False)
    check('N07: Brecha força acerto', outcome(2,5,16,(1,1))[0], True)
    check('N08: enumerar d20 soma probabilidade um', [sum(p for _,p in faces(m)) for m in ['normal','vantagem','desvantagem']], [F(1)]*3)
    help_rows = []
    sensitivity = []
    for policy in ['fixa','sempre','apos_acerto_fixo']:
        sn, sa = stats(policy=policy), stats('vantagem',policy)
        for strong in [1,2,3,4,6,8]:
            help_rows.append(dict(politica=policy, dados_aliado=strong, fixo_aliado=2,
                basica_atacando=expected(1,1,sn), ganho_de_ajudar=expected(strong,2,sa)-expected(strong,2,sn),
                ganho_com_vantagem_preexistente=F(0)))
        routine = expected(3,2,sn)+expected(1,1,sn)
        helped = expected(3,2,sa)
        for dice in range(2,9):
            for pe in [1,2,3]:
                special = expected(dice,1,sn)
                sensitivity.append(dict(politica=policy,dados_especial=dice,fixo=1,pe_por_uso=pe,
                    dano_rotina=routine,dano_usuario_ajudado=helped,dano_especial=special,
                    diferenca_rotina=special-routine,diferenca_ajuda=special-helped,
                    dano_tres_ciclos=special*3,pe_tres_ciclos=pe*3))
    offense=[]
    for count in [1,2,3]:
        ids=['C','S','X'][:count]
        for spec in [None,4,5,6]:
            option_sets=[]
            for key in ids:
                if key=='C' and spec:opts=['especial']
                else:opts=(['atacar'] if key!='X' else ['buscar'])+['ajudar:'+k for k in ['U',*ids] if k!=key]
                option_sets.append(opts)
            best=None;choices=[]
            for combination in product(*option_sets):
                assignment=dict(zip(ids,combination))
                attacks={} if spec else {'U':(3,2)}
                for k,v in assignment.items():
                    if v=='atacar':attacks[k]=(1,1)
                    if v=='especial':attacks[k]=(spec,1)
                helped={v.split(':')[1] for v in assignment.values() if v.startswith('ajudar:')}
                value=sum((expected(d,f,a if k in helped else n) for k,(d,f) in attacks.items()),F(0))
                if best is None or value>best:best=value;choices=[assignment]
                elif value==best:choices.append(assignment)
            offense.append(dict(entidades=count,dados_especial=spec,dano_primario_maximo=best,
                                escolhas_equivalentes=choices,
                                premissa='Somente estas escolhas; alvos ao alcance e contribuição dos ajudantes já estabelecida. Sem Bloquear, defesa, busca, PE ou reação na função de valor.'))
    return dict(probabilidades=rows,ajuda=help_rows,especiais=sensitivity,combinacoes_ajuda=offense,
                horizonte_pe=[dict(PE_inicial=4,PE_por_especial=c,usos_em_tres_ciclos=min(3,4//c),
                    PE_final=4-min(3,4//c)*c,
                    dano_esperado=min(3,4//c)*expected(6,1,n)+(3-min(3,4//c))*expected(3,2,a),
                    ganho_sobre_ajudar_tres_vezes=min(3,4//c)*(expected(6,1,n)-expected(3,2,a))) for c in [1,2,3]],
                cobertura=[dict(defesa=d, dano_inimigo=expected(2,2,stats(defense=d))) for d in [16,18,21]],
                observacao='Dano primário esperado, sem dano de contra-ataques. Aparar/Brecha são oportunidades, não ataques gratuitos. Política apos_acerto_fixo é hipótese separada.')


def body(name, dice, flat, hp, pos, move=6):
    return dict(nome=name,dados=dice,fixo=flat,hp=hp,hp_max=hp,pos=list(pos),base_move=move,
                metros=move,basica=1,cond=[],consciente=True,intencao='enfrentar a ameaça',
                defesa=16,ataque=5,esquiva=False,preparada=None,pe_proprio=None)


class Bench:
    def __init__(self, count=3, guia_owner=False, guia_level=7):
        self.s = dict(ciclo=0,turno='nenhum',rodada_global=1,coletiva=1,
            P=1,B=1,M=9,R=1,PE=12,ataque_pessoal_acertou=False,
            corpos={'U':body('Usuário',3,2,40,(0,0),9),
                    'E':body('Inimigo',2,2,200,(1.5,0),6)},
            ajuda={},tarefas=0,rolagens=Counter(),ataques=0,dano=Counter(),
            guia=dict(proprio=guia_owner,nivel=guia_level,ciclo=0,B=1,R=1,PE=8,
                      aberta=None,usados=[],tipos=[],respostas=[],janela=False,abriu=False,
                      plano=False,plano_usado=False))
        cards=[('C',body('Combatente',1,1,18,(1.5,4.5))),
               ('S',body('Sentinela',1,1,24,(6,0))),
               ('X',body('Explorador',0,0,12,(-6,0)))]
        for key,b in cards[:count]: self.s['corpos'][key]=b
        self.log=[]

    def save(self,name):
        SCENES[name]=dict(eventos=self.log,estado_final=deepcopy(self.s))

    def do(self, label, fn, reject=None, unknown=False):
        before=deepcopy(self.s)
        status='resolvido';error=None;result=None
        try:
            result=fn()
            if reject or unknown: check(label+': deveria interromper', 'resolvido', 'interrompido')
        except (Illegal,Unknown) as e:
            self.s=deepcopy(before)  # histórico não pode compartilhar o estado mutável restaurado.
            error=str(e);status='indeterminado' if isinstance(e,Unknown) else 'recusado'
            if isinstance(e,Unknown):
                check(label+': pendência reconhecida',unknown,True)
            else:
                check(label+': recusa esperada',error,reject)
        self.log.append(dict(evento=label,status=status,motivo=error,resultado=result,
                             antes=before,depois=deepcopy(self.s)))
        return result

    def actor(self,key): return self.s['corpos'][key]
    def entities(self): return [x for x in self.s['corpos'] if x not in ['U','E']]
    def live(self,key):
        b=self.actor(key)
        need(b['consciente'] and b['hp']>0 or key=='U' and b['consciente'] and b.get('insistir'), 'executor sem atuação consciente')
    def inturn(self): need(self.s['turno']=='I','fora da janela do conjunto')
    def can_react(self,key):
        self.live(key)
        need('Atordoado' not in self.actor(key)['cond'],'Atordoado não reage')
        need(self.s['R'] if key=='U' else self.s['coletiva'],'reserva reativa esgotada')
    def use_react(self,key):
        self.can_react(key)
        if key=='U': self.s['R']=0
        else:
            self.s['coletiva']=0
            for k in self.entities(): self.actor(k)['preparada']=None
    def distance(self,a,b):
        x,y=self.actor(a)['pos'];u,v=self.actor(b)['pos']
        return ((x-u)**2+(y-v)**2)**.5
    def start(self):
        self.s['turno']='I';self.s['ciclo']+=1;self.s['coletiva']=1;self.s['R']=1
        u=self.actor('U');awake=u['consciente']
        self.s['P']=int(awake and 'Atordoado' not in u['cond'])
        self.s['B']=int(awake and 'Lento' not in u['cond'])
        self.s['M']=9*(.5 if 'Lento' in u['cond'] else 1) if awake else 0
        if {'Agarrado','Impedido'} & set(u['cond']): self.s['M']=0
        self.s['ataque_pessoal_acertou']=False
        self.s['ajuda']={}
        for k in self.entities():
            a=self.actor(k)
            a['basica']=int(a['consciente'] and a['hp']>0 and 'Atordoado' not in a['cond'])
            a['metros']=a['base_move']*(.5 if 'Lento' in a['cond'] else 1)
            if {'Agarrado','Impedido'} & set(a['cond']) or not a['consciente']: a['metros']=0
            a['preparada']=None;a['esquiva']=False
        if self.s['guia']['proprio']: self.start_guide(own=True)
    def spend_p(self):
        self.inturn();self.live('U');need(self.s['P']>0,'Padrão indisponível');self.s['P']-=1
    def spend_b(self):
        self.inturn();self.live('U');need('Lento' not in self.actor('U')['cond'],'Lento não usa Bônus')
        need(self.s['B']>0,'Bônus indisponível');self.s['B']-=1
    def basic(self,key,action,help_to=None):
        self.inturn();self.live(key);a=self.actor(key)
        need('Atordoado' not in a['cond'],'Atordoado não usa básica')
        need(a['basica']>0,'básica indisponível')
        if action=='atacar': need(a['dados']>0,'não possui ataque')
        if action=='ajudar':
            need(help_to is not None,'destinatário da ajuda ausente')
            need(self.distance(key,help_to)<=3,'sem contribuição concreta na sonda')
        if action=='especial': raise Illegal('especial exige comando')
        a['basica']-=1
        if action=='esquivar': a['esquiva']=True
        if action=='correr': a['metros']+=a['base_move']*(.5 if 'Lento' in a['cond'] else 1)
        if action=='preparar':
            need(a['dados']>0,'não possui ataque');a['preparada']='ataque ao gatilho visível'
        if action=='ajudar': self.s['ajuda'][help_to]=True
    def move(self,key,dest):
        self.inturn();self.live(key);a=self.actor(key)
        need(not ({'Agarrado','Impedido'} & set(a['cond'])),'deslocamento impedido')
        x,y=a['pos'];u,v=dest;dist=((x-u)**2+(y-v)**2)**.5
        available=self.s['M'] if key=='U' else a['metros']
        need(dist<=available+1e-8,'movimento insuficiente')
        # Só caminhos livres sem saída de alcance ameaçado nas sondas de movimento.
        if key=='U': self.s['M']-=dist
        else: a['metros']-=dist
        a['pos']=list(dest)
        return dict(metros=dist,destino=dest)
    def redirect(self,keys,intention):
        need(len(keys)<=3,'mais de X destinatárias')
        need(all(k in self.entities() for k in keys),'destinatária ausente')
        self.spend_b()
        for key in keys: self.actor(key)['intencao']=intention
    def convert(self,source):
        if source=='P':
            self.spend_p();self.s['B']+=1
        elif source=='B':
            self.spend_b();self.s['M']+=9*(.5 if 'Lento' in self.actor('U')['cond'] else 1)
    def bonus(self,kind,cost=0):
        need(self.s['PE']>=cost,'PE insuficiente')
        if kind=='Trocação': need(self.s['ataque_pessoal_acertou'],'falta acerto da Ação Atacar')
        self.spend_b();self.s['PE']-=cost
    def special(self,key,cost=2,intention_ok=True):
        self.inturn();self.live('U');self.live(key)
        if not intention_ok: raise Unknown('especial muda intenção: custo de redirecionar não definido')
        need(key=='C','cartão sem especial ativa')
        need('Atordoado' not in self.actor(key)['cond'],'Atordoado não usa básica')
        need(self.actor(key)['basica']>0,'básica indisponível')
        need(self.s['PE']>=cost,'PE insuficiente')
        self.spend_p();self.actor(key)['basica']=0;self.s['PE']-=cost
    def condition(self,key,name):
        a=self.actor(key);a['cond'].append(name)
        if name=='Atordoado':
            if key=='U': self.s['P']=0
            else:a['basica']=0
        if name=='Lento':
            if key=='U': self.s['B']=0;self.s['M']/=2
            else:a['metros']/=2
        if name in ['Agarrado','Impedido']:
            if key=='U':self.s['M']=0
            else:a['metros']=0
    def resistance(self,key,die,bonus=1,dc=12,end_condition=None,advantage=False):
        rolls=die if isinstance(die,list) else [die]
        need(len(rolls)==(2 if advantage else 1),'dados de TR incompatíveis')
        self.s['rolagens']['d20']+=len(rolls)
        success=max(rolls)+bonus>=dc
        if success and end_condition: self.actor(key)['cond'].remove(end_condition)
        return dict(sucesso=success,resultado=max(rolls)+bonus,CD=dc)
    def strike(self,source,target,roll,damage,block=None,intercept=None,personal_action=False,nd=None,flat=None,kind='comum'):
        a,t=self.actor(source),self.actor(target)
        need(a['dados']>0,'não possui ataque')
        need(self.distance(source,target)<=1.5+1e-8,'alvo fora do alcance')
        dice=nd if nd is not None else a['dados'];fixed=flat if flat is not None else a['fixo']
        rs=roll if isinstance(roll,list) else [roll]
        advantage=bool(self.s['ajuda'].get(source,False))
        disadvantage=t['esquiva']
        # Cancelamento vantagem/desvantagem não é inferido: sonda combinada fica pendente.
        if advantage and disadvantage: raise Unknown('vantagem e desvantagem simultâneas fora desta sonda')
        need(len(rs)==(2 if advantage or disadvantage else 1),'quantidade de d20 incompatível')
        die=min(rs) if disadvantage else max(rs)
        if block is not None: need('Incapacitado' not in t['cond'],'Incapacitado não Bloqueia')
        hit,crit,parry,breach=outcome(die,a['ataque'],t['defesa'],tuple(block) if block else None,'Incapacitado' in t['cond'])
        self.s['rolagens']['d20']+=len(rs);self.s['ataques']+=1
        if block: self.s['rolagens']['d10']+=2
        if advantage:self.s['ajuda'].pop(source,None)
        original=target
        if intercept:
            need(hit,'não há acerto para interceptar')
            need(intercept=='S' and original=='U','interceptação protege o usuário original')
            need(self.distance('S','U')<=3,'usuário fora da interceptação de laboratório')
            need(kind!='transferido','acerto já transferido')
            self.use_react('S');target='S';t=self.actor(target)
        dealt=0
        if hit:
            need(len(damage)==dice*(2 if crit else 1),'quantidade de dados de dano incompatível')
            self.s['rolagens']['d6']+=len(damage);dealt=sum(damage)+fixed
            t['hp']-=dealt;self.s['dano'][source]+=dealt
        if personal_action and source=='U' and hit:self.s['ataque_pessoal_acertou']=True
        return dict(fonte=source,alvo_original=original,alvo_final=target,d20=rs,acerto=hit,critico=crit,
                    aparar=parry,brecha=breach,dano=dealt,transferido=bool(intercept),tipo=kind)
    def reaction_attack(self,key,roll,damage,why,flat_extra=0):
        need(self.actor(key)['dados']>0,'não possui ataque')
        if why=='preparada': need(self.actor(key)['preparada'],'preparação indisponível')
        self.use_react(key)
        return self.strike(key,'E',roll,damage,flat=self.actor(key)['fixo']+flat_extra,kind=why)
    def start_guide(self,own=False):
        g=self.s['guia'];g['ciclo']+=1;g['B']=1;g['R']=1
        g.update(aberta=None,usados=[],tipos=[],respostas=[],janela=False,abriu=False,plano=False)
        if not own:self.s['turno']='G'
    def guide_pay(self,resource,cost=0):
        g=self.s['guia']
        if g['proprio']:
            if resource=='B':self.spend_b()
            else:self.use_react('U')
            need(self.s['PE']>=cost,'PE insuficiente');self.s['PE']-=cost
        else:
            need(g[resource]>0,'recurso do Guia indisponível');g[resource]-=1
            need(g['PE']>=cost,'PE do Guia insuficiente');g['PE']-=cost
    def opening(self,key,kind,plan=False):
        g=self.s['guia'];need(not g['abriu'],'Abrir Caminho já usado neste turno')
        need(key in self.entities(),'aliado inválido para esta sonda')
        if plan:need(g['nivel']==30 and not g['plano_usado'],'plano indisponível')
        self.guide_pay('B',1);g['abriu']=True;g['plano']=plan
        if plan:g['plano_usado']=True
        g['aberta']=[key,kind];g['usados']=[];g['tipos']=[]
    def consume_opening(self,key,kind):
        g=self.s['guia'];need(g['aberta']==[key,kind],'Abertura ausente ou incompatível')
        if kind=='Avançar':
            need(not ({'Agarrado','Impedido'} & set(self.actor(key)['cond'])),'deslocamento impedido')
            if self.s['turno']!='I':self.use_react(key)
            self.actor(key)['pos'][1]+=3  # caminho livre fornecido pelo cenário, fora de ameaça escolhida.
        if kind=='Executar':self.s['ajuda'][key]=True
        g['aberta']=None;g['usados'].append(key);g['tipos'].append(kind);g['janela']=True
    def pass_opening(self,key,kind):
        g=self.s['guia']
        need(g['nivel']>=23,'Guia não pode passar Abertura')
        need(len(g['usados'])<(3 if g['plano'] else 2),'cadeia encerrada')
        need(key not in g['usados'] and kind not in g['tipos'],'aliado ou tipo repetido')
        need(g['aberta'] is None,'Abertura anterior não consumida')
        g['aberta']=[key,kind];g['janela']=False
    def response(self,key,roll,damage):
        g=self.s['guia'];need(g['janela'],'não há gatilho de Abertura')
        need(len(g['respostas'])<(2 if g['plano'] else 1),'limite de respostas do Guia')
        need(key not in g['respostas'],'mesma criatura responderia duas vezes')
        need(self.actor(key)['dados']>0,'não possui ataque');self.can_react(key)
        if not g['respostas']:self.guide_pay('R')
        self.use_react(key);g['respostas'].append(key);g['janela']=False
        return self.strike(key,'E',roll,damage,kind='resposta comum do Guia')


def stage(w):
    """Posições livres já existentes, para sondas sem custo de entrada."""
    for k,pos in [('C',(1.5,1.5)),('S',(3,0)),('X',(-3,0))]:
        if k in w.entities():w.actor(k)['pos']=list(pos)


def routines():
    for count in range(4):
        for victim in ['usuario','sentinela_se_presente']:
            w=Bench(count)
            for i in range(3):
                w.do(f'ciclo {i+1}: renovar',w.start)
                if i==0:
                    for k,dest in [('C',(1.5,1.5)),('S',(3,0)),('X',(-3,0))]:
                        if k in w.entities():w.do(k+': aproximar',lambda k=k,dest=dest:w.move(k,dest))
                def ua():
                    w.spend_p()
                    return w.strike('U','E',[12,7,20][i],[[3,4,2],[],[3,4,2,5,1,6]][i],personal_action=True)
                w.do('usuário: Ação Atacar',ua)
                if 'C' in w.entities():
                    def ca():
                        w.basic('C','atacar');return w.strike('C','E',[11,15,9][i],[[2],[4],[]][i])
                    w.do('Combatente: básica',ca)
                if 'S' in w.entities():w.do('Sentinela: Esquivar',lambda:w.basic('S','esquivar'))
                if 'X' in w.entities():
                    def search():
                        w.basic('X','vasculhar');die=[11,7,16][i];w.s['rolagens']['d20']+=1
                        success=die+3>=12;w.s['tarefas']+=success
                        return dict(objeto=['gaveta','caixa','bolsa'][i],d20=die,bonus=3,CD=12,sucesso=success)
                    w.do('Explorador: investigar objeto distinto',search)
                w.s['turno']='inimigo'
                target='S' if victim=='sentinela_se_presente' and 'S' in w.entities() else 'U'
                rolls=[[14,7],[12,10],[18,8]][i] if target=='S' else [14,12,18][i]
                w.do('inimigo: ataque',lambda target=target,rolls=rolls:w.strike('E',target,rolls,[[3,3],[3,4],[4,4]][i]))
            name=f'T1-{count}-{victim}'
            check(name+': dano pessoal invariável',w.s['dano']['U'],34)
            check(name+': dano do Combatente',w.s['dano']['C'],8 if count else 0)
            check(name+': tarefas distintas',w.s['tarefas'],2 if count==3 else 0)
            check(name+': dano no usuário depende do alvo inimigo',w.actor('U')['hp'],40 if target=='S' else 13)
            w.save(name)


def basic_special_help():
    for order in permutations(['U','C','S']):
        w=Bench();stage(w);w.start()
        for k in order:
            if k=='U':w.do('especial C',lambda:w.special('C'),reject='básica indisponível' if w.actor('C')['basica']==0 else None)
            else:w.do(k+': básica',lambda k=k:w.basic(k,'atacar'),reject='básica indisponível' if w.actor(k)['basica']==0 else None)
        check('T2 '+''.join(order)+': C e S agem uma vez; X preservado',
              (w.actor('C')['basica'],w.actor('S')['basica'],w.actor('X')['basica']),(0,0,1))
        check('T2 '+''.join(order)+': comando recusado não paga P/PE',
              (w.s['P'],w.s['PE']),(0,10) if order.index('U')<order.index('C') else (1,12))
        w.save('T2-ordem-'+''.join(order))
    w=Bench();stage(w);w.start()
    w.do('X não recebe ataque por existir',lambda:w.basic('X','atacar'),reject='não possui ataque')
    w.do('C ajuda ataque U',lambda:w.basic('C','ajudar',help_to='U'))
    w.do('S tenta ajudar a mesma tentativa',lambda:w.basic('S','ajudar',help_to='U'))
    def attack():
        w.spend_p();return w.strike('U','E',[4,16],[3,4,2],personal_action=True)
    w.do('U recebe só dois d20',attack)
    check('T1 ajuda não empilha dados',w.s['rolagens']['d20'],2)
    check('T1 segunda ajuda desperdiça a básica',w.actor('S')['basica'],0)
    w.do('Guia do ensaio não resolve vantagem/desvantagem silenciosamente',lambda:raise_unknown('combinação de vantagem/desvantagem não examinada'),unknown=True)
    w.save('T1-ajuda')
    for dice,damage in [(4,[3,4,2,5]),(5,[3,4,2,5,1]),(6,[3,4,2,5,1,6])]:
        w=Bench();stage(w)
        for cycle in range(3):
            w.do('renovar',w.start)
            def special():
                w.special('C',2);return w.strike('C','E',14,damage,nd=dice)
            w.do('especial em vez de U + C',special)
            w.do('Sentinela atua normalmente',lambda:w.basic('S','esquivar'))
            w.do('Explorador usa objeto',lambda:w.basic('X','usar_objeto'))
            w.do('nova especial no mesmo ciclo',lambda:w.special('C'),reject='básica indisponível')
        check(f'T2 especial {dice}d6: PE e execuções',(w.s['PE'],w.s['ataques']),(6,3))
        w.save(f'T2-especial-{dice}d6')
    w=Bench();stage(w);w.start()
    w.do('especial que muda objetivo',lambda:w.special('C',intention_ok=False),unknown=True)
    w.do('fila após básica',lambda:raise_unknown('pagamento, validade e execução futura não definidos'),unknown=True)
    w.save('T2-pendencias')


def raise_unknown(message):raise Unknown(message)


def coordination():
    w=Bench();stage(w);w.start()
    w.do('básica antes da nova intenção',lambda:w.basic('C','atacar'))
    w.do('mesma nova intenção para três',lambda:w.redirect(['C','S','X'],'recuar e guardar esta saída'))
    check('T3 redirecionar não renova básica',w.actor('C')['basica'],0)
    w.do('Abrir Caminho disputa Bônus',lambda:w.bonus('Abrir Caminho',1),reject='Bônus indisponível')
    w.do('converter Padrão para Bônus',lambda:w.convert('P'))
    w.do('abrir espaço para outra tarefa individual',lambda:w.redirect(['X'],'investigar o recipiente'))
    w.do('comando sem Padrão',lambda:w.special('C'),reject='básica indisponível')
    check('T3 duas intenções custam P e B',(w.s['P'],w.s['B']),(0,0))
    w.save('T3-coordenacao')
    w=Bench();stage(w);w.start()
    w.do('Olhos Em Mim',lambda:w.bonus('Olhos Em Mim'))
    w.do('redirecionar sem segunda Bônus',lambda:w.redirect(['C'],'mudar objetivo'),reject='Bônus indisponível')
    w.do('converter P',lambda:w.convert('P'))
    w.do('redirecionar com P convertida',lambda:w.redirect(['C'],'mudar objetivo'))
    w.do('especial sem P',lambda:w.special('C'),reject='Padrão indisponível')
    w.save('T3-bastiao-area')
    for spec in [False,True]:
        w=Bench();stage(w);w.start()
        if spec:w.do('comando substitui Atacar pessoal',lambda:w.special('C'))
        else:
            def hit():w.spend_p();return w.strike('U','E',14,[3,4,2],personal_action=True)
            w.do('Atacar pessoal acerta',hit)
        w.do('Trocação Franca',lambda:w.bonus('Trocação'),reject='falta acerto da Ação Atacar' if spec else None)
        w.save('T3-trocacao-'+str(spec))


def defenses():
    w=Bench();stage(w);w.start();w.s['turno']='inimigo'
    first=w.do('Sentinela intercepta após Bloquear falhar',lambda:w.strike('E','U',14,[3,4],block=[4,4],intercept='S'))
    w.do('oportunidade C com coletiva gasta',lambda:w.reaction_attack('C',14,[3],'oportunidade'),reject='reserva reativa esgotada')
    w.do('Sentinela ainda pode Bloquear outro ataque',lambda:w.strike('E','S',14,[],block=[8,9]))
    check('T4 transferência não faz segundo Bloquear',(w.s['rolagens']['d10'],w.actor('U')['hp'],w.actor('S')['hp']),(4,40,15))
    w.do('retransferência do acerto',lambda:w.strike('E','U',14,[3,4],intercept='S',kind='transferido'),reject='acerto já transferido')
    check('T4 a pessoal continua separada',w.s['R'],1);w.save('T4-interceptacao')
    w=Bench();stage(w);w.start();w.s['turno']='inimigo'
    w.do('C obtém Aparar',lambda:w.strike('E','C',14,[],block=[10,10]))
    w.do('C contra-ataca com +3',lambda:w.reaction_attack('C',14,[3],'aparar',3))
    w.do('S também obtém Aparar',lambda:w.strike('E','S',15,[],block=[10,10]))
    w.do('S não contra-ataca sem coletiva',lambda:w.reaction_attack('S',14,[3],'aparar',3),reject='reserva reativa esgotada')
    check('T4 dois Aparar bloqueiam, um contra-ataca',(w.s['ataques'],w.s['dano']['C'],w.actor('S')['hp']),(3,7,24))
    w.save('T4-aparar')
    w=Bench();stage(w);w.start();w.s['turno']='inimigo'
    w.do('20 natural atravessa Aparar',lambda:w.strike('E','C',20,[2,3,4,1],block=[10,10]))
    check('T4 crítico não foi apagado',w.actor('C')['hp'],6)
    w.save('T4-critico')
    w=Bench();stage(w);w.start();w.s['turno']='inimigo';w.s['reacao_inimigo']=1
    w.do('C oferece Brecha',lambda:w.strike('E','C',3,[2,2],block=[1,1]))
    def breach():
        need(w.s['reacao_inimigo'],'reação inimiga esgotada');w.s['reacao_inimigo']=0
        return w.strike('E','C',12,[2,2])
    w.do('E paga sua Reação pelo ataque extra',breach)
    check('T4 Brecha não consome coletiva',(w.s['coletiva'],w.s['reacao_inimigo'],w.actor('C')['hp']),(1,0,6))
    w.save('T4-brecha')
    for prepared in [True,False]:
        w=Bench();stage(w);w.start()
        w.do('C prepara ataque',lambda:w.basic('C','preparar'))
        w.do('S prepara ataque',lambda:w.basic('S','preparar'))
        w.s['turno']='inimigo'
        if prepared:w.do('C executa no gatilho',lambda:w.reaction_attack('C',14,[3],'preparada'))
        else:w.do('S usa oportunidade antes do gatilho',lambda:w.reaction_attack('S',14,[3],'oportunidade'))
        w.do('S tenta preparação sem recurso',lambda:w.reaction_attack('S',14,[3],'preparada'),reject='preparação indisponível')
        check('T4 outra preparação perdida',w.actor('C')['preparada'],None)
        w.save('T4-preparadas-'+str(prepared))


def guides():
    w=Bench(3,guia_owner=True);stage(w);w.do('turno Guia-invocador',w.start)
    w.do('Abrir Executar para C',lambda:w.opening('C','Executar'))
    w.do('C usa Abertura',lambda:w.consume_opening('C','Executar'))
    def basic():w.basic('C','atacar');return w.strike('C','E',[3,14],[3])
    w.do('C básica com vantagem',basic)
    w.do('C responde mesmo depois de básica',lambda:w.response('C',14,[4]))
    w.do('resposta não gera novo convite',lambda:w.response('S',14,[3]),reject='não há gatilho de Abertura')
    w.do('especial continua impedida após básica',lambda:w.special('C'),reject='básica indisponível')
    check('T4 Guia-invocador: B 1PE e duas Reações',(w.s['B'],w.s['PE'],w.s['R'],w.s['coletiva'],w.s['P']),(0,11,0,0,1))
    w.save('T4-guia7-proprio')
    w=Bench();stage(w);w.start();w.do('Guia externo começa',w.start_guide)
    w.do('Avançar para C',lambda:w.opening('C','Avançar'))
    w.s['turno']='inimigo'
    w.do('Avançar fora do turno paga coletiva',lambda:w.consume_opening('C','Avançar'))
    w.do('nem S aceita resposta sem coletiva',lambda:w.response('S',14,[3]),reject='reserva reativa esgotada')
    check('T4 falha do convite não gasta Reação Guia',w.s['guia']['R'],1)
    w.save('T4-avancar-fora')
    w=Bench();stage(w);w.start();w.start_guide();w.opening('X','Avançar');w.start()
    w.do('Avançar na janela coletiva preserva Reação',lambda:w.consume_opening('X','Avançar'))
    check('T4 Avançar no turno não gasta movimento próprio nem coletiva',(w.actor('X')['metros'],w.s['coletiva']),(6,1))
    w.do('X não ganha ataque pelo convite',lambda:w.response('X',14,[]),reject='não possui ataque')
    w.save('T4-avancar-dentro')
    # Guia 30: duas respostas com uma renovação real entre elas, no mesmo ciclo do Guia.
    w=Bench(3,guia_level=30);stage(w);w.start()
    w.do('G inicia seu ciclo',w.start_guide)
    w.do('plano: Resguardar C',lambda:w.opening('C','Resguardar',plan=True))
    w.s['turno']='inimigo'
    w.do('ameaça observada exige TR',lambda:w.consume_opening('C','Resguardar'))
    w.do('C resiste com vantagem',lambda:w.resistance('C',[6,14],advantage=True))
    w.do('primeira resposta C antes do turno I',lambda:w.response('C',14,[3]))
    w.do('passa Executar S',lambda:w.pass_opening('S','Executar'))
    w.do('I começa: única renovação coletiva',w.start)
    w.do('S consome Executar',lambda:w.consume_opening('S','Executar'))
    def sb():w.basic('S','atacar');return w.strike('S','E',[5,14],[3])
    w.do('S realiza sua básica',sb)
    w.do('segunda resposta S, dispensa somente R de G',lambda:w.response('S',14,[4]))
    check('T6 duas respostas entre turnos do Guia',(len(w.s['guia']['respostas']),w.s['guia']['ciclo'],w.s['ciclo'],w.s['guia']['R']),(2,1,2,0))
    w.do('passa Avançar X',lambda:w.pass_opening('X','Avançar'))
    w.do('X Avança no turno',lambda:w.consume_opening('X','Avançar'))
    w.do('não existe terceira resposta',lambda:w.response('C',14,[3]),reject='limite de respostas do Guia')
    w.save('T6-guia30-com-renovacao')
    # Sem renovação entre os dois gatilhos, as duas destinatárias disputam a mesma reserva.
    w=Bench(3,guia_level=30);stage(w);w.start_guide();w.opening('C','Executar',True);w.start()
    w.consume_opening('C','Executar')
    w.basic('C','atacar');w.strike('C','E',[2,14],[3]);w.response('C',14,[3]);w.pass_opening('S','Resguardar')
    w.do('perigo durante o mesmo turno ativa Resguardar',lambda:w.consume_opening('S','Resguardar'))
    w.do('S resiste',lambda:w.resistance('S',[4,14],advantage=True))
    w.do('segunda resposta sem renovação',lambda:w.response('S',14,[3]),reject='reserva reativa esgotada')
    check('T6 sem renovação só uma resposta',len(w.s['guia']['respostas']),1)
    w.save('T6-guia30-sem-renovacao')


def conditions_clocks():
    w=Bench();stage(w);w.actor('U')['consciente']=False;w.actor('U')['hp']=0
    w.do('início com usuário inconsciente',w.start)
    def autonomous():
        w.basic('C','atacar');return w.strike('C','E',14,[3])
    w.do('C ataca autonomamente',autonomous)
    w.do('S move sem pedir ordem',lambda:w.move('S',(1.5,-1.5)))
    w.s['turno']='inimigo'
    w.do('S intercepta sem comando consciente',lambda:w.strike('E','U',20,[2,3,1,4],intercept='S'))
    w.s['turno']='I'
    w.do('usuário inconsciente não comanda',lambda:w.special('C'),reject='executor sem atuação consciente')
    w.do('usuário inconsciente não redireciona',lambda:w.redirect(['X'],'buscar socorro'),reject='executor sem atuação consciente')
    w.do('PE do inconsciente para capacidade',lambda:raise_unknown('acesso aos PE do inconsciente não definido'),unknown=True)
    check('T5 inconsciência não paga manutenção inventada',w.s['PE'],12)
    w.save('T5-inconsciente')
    w=Bench();stage(w);w.condition('U','Atordoado');w.do('início atordoado',w.start)
    w.do('comando com C ainda disponível exige Padrão',lambda:w.special('C'),reject='Padrão indisponível')
    w.do('C usa básica',lambda:w.basic('C','atacar'))
    w.do('Bônus pessoal continua possível',lambda:w.redirect(['X'],'buscar objeto'))
    w.do('Padrão pessoal indisponível',lambda:w.special('C'),reject='básica indisponível')
    w.do('usuário não usa Reação',lambda:w.use_react('U'),reject='Atordoado não reage')
    w.do('fim do turno: TR pesado encerra Atordoado',lambda:w.resistance('U',15,end_condition='Atordoado'))
    check('T5 cura da condição não renova P já perdida',w.s['P'],0)
    w.do('S pode usar coletiva',lambda:w.use_react('S'))
    w.save('T5-usuario-atordoado')
    for condition in ['Atordoado','Incapacitado','Lento','Agarrado','Impedido']:
        w=Bench();stage(w);w.condition('C',condition);w.start()
        w.do('C tenta básica com '+condition,lambda:w.basic('C','esquivar'),reject='Atordoado não usa básica' if condition=='Atordoado' else None)
        if condition=='Atordoado':
            w.do('comando não contorna condição',lambda:w.special('C'),reject='Atordoado não usa básica')
            w.do('C não gasta coletiva',lambda:w.use_react('C'),reject='Atordoado não reage')
            w.do('S usa mesma reserva',lambda:w.use_react('S'))
            w.do('TR fim da janela da entidade',lambda:w.resistance('C',15,end_condition='Atordoado'))
            check('T5 terminar Atordoado não cria básica no fim do turno',w.actor('C')['basica'],0)
        if condition=='Incapacitado':
            w.actor('C')['esquiva']=False
            w.do('C não Bloqueia',lambda:w.strike('E','C',14,[2,2,2,2],block=[8,8]),reject='Incapacitado não Bloqueia')
            result=w.do('acerto corpo a corpo torna-se crítico',lambda:w.strike('E','C',14,[2,2,2,2]))
            check('T5 Incapacitado crita acerto',result['critico'],True)
        if condition=='Lento':
            w.do('C anda três metros',lambda:w.move('C',(1.5,4.5)))
            w.do('C não anda mais',lambda:w.move('C',(1.5,6)),reject='movimento insuficiente')
        if condition in ['Agarrado','Impedido']:
            w.do('C não ignora deslocamento zero',lambda:w.move('C',(1.5,3)),reject='deslocamento impedido')
        w.save('T5-entidade-'+condition)
    w=Bench();stage(w);w.actor('U').update(hp=0,insistir=True);w.start()
    w.do('Insistir consciente comanda',lambda:w.special('C'))
    check('T5 zero PV consciente não perde P antes de usá-la',w.s['PE'],10)
    w.save('T5-zero-consciente')
    w=Bench();stage(w);w.start();w.basic('C','preparar');w.basic('S','esquivar')
    w.do('C corre não soma ataque',lambda:w.basic('C','correr'),reject='básica indisponível')
    w.s['turno']='inimigo'
    w.do('virada global da rodada',lambda:w.s.update(rodada_global=2))
    check('T6 rodada global não renova básica',(w.actor('C')['basica'],w.actor('S')['esquiva']),(0,True))
    w.do('começo do turno I expira e renova',w.start)
    check('T6 preparação expira, Esquivar termina, básica renova',
          (w.actor('C')['preparada'],w.actor('S')['esquiva'],w.actor('C')['basica']),(None,False,1))
    w.do('C corre usando básica',lambda:w.basic('C','correr'))
    check('T6 Correr aumenta metros, sem atacar',(w.actor('C')['metros'],w.actor('C')['basica']),(12,0))
    w.do('C não ataca após Correr',lambda:w.basic('C','atacar'),reject='básica indisponível')
    w.save('T6-relogio-correr')


def boundary_probes():
    w=Bench();stage(w);w.start();w.use_react('C');w.basic('C','esquivar')
    w.do('rodada global muda após gastar coletiva',lambda:w.s.update(rodada_global=2))
    check('T6 rodada global não repõe coletiva gasta',(w.s['coletiva'],w.actor('C')['basica']),(0,0))
    w.do('próximo turno repõe as reservas uma vez',w.start)
    check('T6 fronteira pessoal repõe coletiva e básica',(w.s['coletiva'],w.actor('C')['basica']),(1,1))
    w.save('T6-fronteira-global')
    w=Bench();stage(w);w.start();w.s['PE']=1
    w.do('especial sem energia suficiente não paga P/básica',lambda:w.special('C',2),reject='PE insuficiente')
    check('T2 recusa de PE preserva recursos',(w.s['P'],w.actor('C')['basica'],w.s['PE']),(1,1,1))
    w.save('T2-energia')
    w=Bench();stage(w);w.start();w.actor('X')['pos']=[-10,0]
    w.do('Ajudar sem contribuição concreta',lambda:w.basic('X','ajudar',help_to='U'),reject='sem contribuição concreta na sonda')
    w.do('básica não autoriza especial autônoma',lambda:w.basic('C','especial'),reject='especial exige comando')
    w.do('converter B em Movimento pessoal',lambda:w.convert('B'))
    check('T3 conversão não move corpos nem cria básicas',(w.s['M'],w.actor('C')['metros'],w.actor('C')['basica']),(18,6,1))
    w.save('T1-limites-fisicos')
    w=Bench();stage(w);w.start();w.basic('S','esquivar');w.s['turno']='inimigo'
    result=w.do('Esquivar S não refaz ataque confirmado contra U',lambda:w.strike('E','U',14,[3,4],intercept='S'))
    check('T4 interceptação não aplica Esquivar retroativo',(result['dano'],w.s['rolagens']['d20']),(9,1))
    w.save('T4-interceptacao-esquivar')
    w=Bench();stage(w);w.start();w.start_guide();w.opening('C','Avançar');w.condition('C','Impedido')
    w.s['turno']='inimigo'
    w.do('Avançar não ignora Impedido',lambda:w.consume_opening('C','Avançar'),reject='deslocamento impedido')
    check('T4 Avançar inválido preserva Abertura/coletiva',(w.s['guia']['aberta'],w.s['coletiva']),(['C','Avançar'],1))
    w.save('T4-avancar-impedido')
    # Rejeitar a retransferência por Olhos Em Mim é propriedade do cartão de S,
    # não mudança da habilidade do Bastião. A sonda abaixo só isola esse veto.
    w=Bench();stage(w);w.start()
    attack=w.do('S recebe acerto destinado a U',lambda:w.strike('E','U',14,[3,4],intercept='S'))
    def bastiao_transfer():
        need(not attack['transferido'],'cartão de S encerrou a transferência deste acerto')
        w.use_react('U')
    w.do('Olhos Em Mim não devolve o mesmo golpe neste cartão',bastiao_transfer,reject='cartão de S encerrou a transferência deste acerto')
    check('T4 veto do cartão conserva Reação pessoal',w.s['R'],1)
    w.save('T4-fronteira-bastiao')
    # Saldo de básica e reserva de Reação são distintos, mesmo após especial.
    w=Bench(3,guia_owner=True);stage(w);w.start()
    w.do('Guia-invocador prepara Executar C',lambda:w.opening('C','Executar'))
    w.do('C usa Abertura na especial',lambda:w.consume_opening('C','Executar'))
    def special():
        w.special('C');return w.strike('C','E',[5,14],[3,4,2,5,1],nd=5)
    w.do('especial comandada com vantagem',special)
    w.do('resposta comum C após especial',lambda:w.response('C',14,[3]))
    w.do('isso não liberou uma básica',lambda:w.basic('C','atacar'),reject='básica indisponível')
    check('T4 especial mais resposta paga P B e ambas Reações',(w.s['P'],w.s['B'],w.s['R'],w.s['coletiva'],w.s['PE']),(0,0,0,0,9))
    w.save('T4-guia-especial')


def audit_traces():
    """Conferência dos registros, separada das transições que os produziram."""
    events=[e for scene in SCENES.values() for e in scene['eventos']]
    check('Auditoria: tentativas recusadas/indeterminadas não pagaram recursos',
          all(e['antes']==e['depois'] for e in events if e['status']!='resolvido'),True)
    check('Auditoria: nenhuma reserva coletiva saiu de 0/1',
          all(e['depois']['coletiva'] in [0,1] for e in events),True)
    check('Auditoria: nenhuma criatura ficou com mais de uma básica',
          all(b['basica'] in [0,1] for e in events for k,b in e['depois']['corpos'].items() if k not in ['U','E']),True)
    check('Auditoria: recursos pessoais nunca negativos',
          all(all(e['depois'][k]>=0 for k in ['P','B','M','R','PE']) for e in events),True)
    check('Auditoria: nenhuma reação originou ataque sem ficha',
          all(e['antes']['corpos'][e['resultado']['fonte']]['dados']>0
              for e in events if e['status']=='resolvido' and isinstance(e['resultado'],dict) and 'fonte' in e['resultado']),True)


def replacement():
    # Transições abstratas de recursos; não são operações de troca autorizadas.
    rows=[]
    for policy in ['aguardar_renovacao','herdar_saldo']:
        for spent in [False,True]:
            w=Bench(1);stage(w);w.start()
            w.actor('C')['hp']=10
            if spent:w.basic('C','atacar');w.actor('C')['metros']=0
            before=deepcopy(w.actor('C'));pool=w.s['coletiva']
            def enter():
                new=body('Reserva',1,1,18,(1.5,1.5))
                new['basica']=0 if policy=='aguardar_renovacao' else before['basica']
                new['metros']=0 if policy=='aguardar_renovacao' else before['metros']
                w.s['retirada']=before;w.s['corpos']['C']=new
                return dict(custo_acao=None,custo_PE=None,primeira_intencao=None,hipotese=policy)
            w.do('transição abstrata, custo desconhecido',enter)
            check('T7 '+policy+str(spent)+': não renova coletiva',w.s['coletiva'],pool)
            rows.append(dict(hipotese=policy,anterior_agiu=spent,basica_entrada=w.actor('C')['basica'],
                 movimento_entrada=w.actor('C')['metros'],vida_anterior=10,vida_reserva=18,
                 vida_disponivel_no_repertorio=28,custo_acao=None,custo_PE=None))
            w.do('troca legal completa',lambda:raise_unknown('custo, primeira ordem e elegibilidade reativa na entrada não definidos'),unknown=True)
            w.do('próxima renovação habilita reserva',w.start)
            check('T7 '+policy+str(spent)+': reserva habilita só pelo relógio',w.actor('C')['basica'],1)
            w.save('T7-'+policy+'-'+str(spent))
    return rows


def energy_horizon():
    for cost in [1,2,3]:
        w=Bench(1);stage(w);w.s['PE']=4;uses=0
        for cycle in range(3):
            w.do('início do ciclo '+str(cycle+1),w.start)
            if w.s['PE']>=cost:
                def special():
                    w.special('C',cost);return w.strike('C','E',14,[3,4,2,5,1,6],nd=6)
                w.do('usar especial 6d6+1',special);uses+=1
            else:
                w.do('comando sem PE é recusado',lambda:w.special('C',cost),reject='PE insuficiente')
                w.do('recurso intacto permite C ajudar',lambda:w.basic('C','ajudar',help_to='U'))
                def helped():
                    w.spend_p();return w.strike('U','E',[5,14],[3,4,2],personal_action=True)
                w.do('U ataca com a ajuda',helped)
        expected_uses={1:3,2:2,3:1}[cost]
        check(f'T2 horizonte PE {cost}: usos e saldo',(uses,w.s['PE']),(expected_uses,4-expected_uses*cost))
        w.save('T2-horizonte-PE-'+str(cost))


def cooperative_special():
    w=Bench(2);stage(w);w.start()
    w.do('S usa sua básica para ajudar C',lambda:w.basic('S','ajudar',help_to='C'))
    def special():
        w.special('C',2);return w.strike('C','E',[5,14],[3,4,2,5,1],nd=5)
    w.do('U comanda especial ajudada de C',special)
    check('T2 especial ajudada ocupa três contribuições',(w.s['P'],w.actor('C')['basica'],w.actor('S')['basica']),(0,0,0))
    check('T2 ajuda na especial só dá dois d20',w.s['rolagens']['d20'],2)
    w.save('T2-especial-ajudada')


def main():
    math=numerical();routines();basic_special_help();coordination();defenses();guides();conditions_clocks();boundary_probes();swaps=replacement();energy_horizon();cooperative_special();audit_traces()
    # Confere fontes usadas, sem alterar o repositório de leitura.
    sources=json.loads((HERE.parent/'verificacao-fontes.json').read_text())['referencias_comparadas']
    integrity=[]
    for entry in sources:
        p=Path(entry['arquivo_atual']);got=hashlib.sha256(p.read_bytes()).hexdigest()
        integrity.append(dict(arquivo=str(p),sha256=got,igual_referencia=got==entry['sha256']))
    failed=[x for x in CHECKS if not x['passou']]
    events=[e for s in SCENES.values() for e in s['eventos']]
    result=dict(status='RASCUNHO / hipóteses de bancada autorizadas para ensaio, não regras finais',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        resumo=dict(checagens=len(CHECKS),passaram=len(CHECKS)-len(failed),falharam=len(failed),
                    cenarios=len(SCENES),eventos_registrados=len(events),
                    recusas=sum(e['status']=='recusado' for e in events),
                    indeterminados=sum(e['status']=='indeterminado' for e in events)),
        verificacoes=CHECKS,matematica=math,troca=swaps,cenarios=SCENES,fontes=integrity,
        limites=['Não é simulador completo; só as regras explicitamente descritas na ficha de bancada.',
                 'Dados dos traços são escolhidos; enumeração é exata apenas no modelo informado.',
                 'Tarefas, caminhos livres, contribuição da ajuda e gatilhos são premissas fornecidas.',
                 'Ataques inimigos e capacidades acionadas nos microcasos são eventos isolados, não turnos legais completos do inimigo.',
                 'Ajudar é consumido na próxima tentativa indicada dentro do ciclo; duração fora desse recorte não resolvida.',
                 'Não há custo de aquisição/sustentação/manifestação validado; ausência de cobrança na cena não significa gratuidade.',
                 'Não mede diversão, tempo real, equilíbrio de fichas completas ou orçamento em fatias.'])
    (HERE/'resultados.json').write_text(json.dumps(plain(result),ensure_ascii=False,indent=2)+'\n')
    summary=json.dumps(result['resumo'],ensure_ascii=False)
    (HERE/'execucao.txt').write_text('python3 bancada.py\n'+summary+'\n')
    print(summary)
    if failed:
        print(json.dumps(plain(failed),ensure_ascii=False,indent=2));raise SystemExit(1)
    assert all(x['igual_referencia'] for x in integrity),'Fontes mudaram'


if __name__=='__main__':main()

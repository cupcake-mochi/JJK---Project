"""Comparações exatas de propostas de Refluxo. Não simula combate ou equilíbrio."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json

DISTRIBUICOES = {'d4': [0,25,50,100], 'd6': [0,25,50,75,100,100], 'd8': [0,25,50,50,75,75,100,100]}
GANHOS = {'uma_25': (1,25), 'duas_15': (2,15), 'uma_50': (1,50)}

def oportunidades(q,n):
    # State: last roll was zero, number of zero-to-positive transitions.
    states={(False,0):Fraction(1)}
    for _ in range(n):
        new=defaultdict(Fraction)
        for (zero,count),prob in states.items():
            new[(True,count)]+=prob*q
            new[(False,count+int(zero))]+=prob*(1-q)
        states=new
    counts=defaultdict(Fraction)
    for (_,count),prob in states.items():counts[count]+=prob
    assert sum(counts.values())==1
    return counts

def cap(maximo,pct):return 0 if maximo<=0 or pct<=0 else max(1,maximo*pct//100)
def ganho(maximo,pct):return cap(maximo,pct)
def profile(n,rate,dist):
    c=sum(n>=level for level in [1,5,9,13,17,21,26]); m=n*rate
    caps=[cap(m,pct) for pct in dist]
    costs={'feitico':3*c,'feitico_e_reacao_2':3*c+2,'manutencao_2_feitico_reacao_2':3*c+4,'integridade_2':4*c,'manutencao_2':2}
    if n>=10:costs['liberacao_maxima']=(9*c+1)//2
    return {'nivel':n,'PE_por_nivel':rate,'maximo':m,'classe':c,'tetos':caps,'custos':costs,'cabem':{key:sum(v>=cost for v in caps) for key,cost in costs.items()},'total_resultados':len(dist)}

r={'estado':'COMPARAÇÃO: após o estudo, o autor escolheu d6 e uma recuperação de 25% por descanso. Demais opções são alternativas não adotadas; números não validam equilíbrio.',
   'premissas':['Sorteios independentes, máximo constante, sem descontos ou outros acréscimos na ficha.',
                'Perfis numéricos não presumem acesso ao Pacto ou a todas as capacidades.',
                'Cabimento exige saldo suficiente e não mede acerto, eficácia ou disponibilidade de ações.',
                'N sorteios próprios observados, sem marca prévia, sem descanso entre eles; não presume duração de combate.',
                'Oportunidades pressupõem poder usar a Bônus e ter espaço na reserva; recuperações reais podem ser menores.',
                'Liberação Máxima não pode usar a mesma ação Bônus já gasta no Refluxo.',
                'Resultados positivos arredondados para baixo, mínimo 1; zero conserva zero. Essa convenção ainda é proposta.'],
   'distribuicoes':DISTRIBUICOES,'ganhos':GANHOS,'perfis':{},'resumo_58_perfis':{},'janelas':{},'recuperacao_por_maximo':{}}
for die,dist in DISTRIBUICOES.items():
    rows=[profile(n,k,dist) for k in [4,6] for n in range(2,31)]
    r['perfis'][die]=rows
    r['resumo_58_perfis'][die]={str(count):sum(x['cabem']['feitico']==count for x in rows) for count in range(len(dist)+1)}
    q=Fraction(dist.count(0),len(dist)); windows={}
    for n in [3,5,8,10]:
        counts=oportunidades(q,n)
        windows[str(n)]={'p_ao_menos_um_zero_pct':float(100*(1-(1-q)**n)),
                         'p_ao_menos_uma_oportunidade_pct':float(100*(1-counts[0])),
                         'p_ao_menos_duas_oportunidades_pct':float(100*sum(v for k,v in counts.items() if k>=2)),
                         'distribuicao_exata_oportunidades':{str(k):str(v) for k,v in sorted(counts.items())},
                         'usos_esperados':{name:float(sum(min(k,limit)*v for k,v in counts.items())) for name,(limit,pct) in GANHOS.items()}}
    r['janelas'][die]=windows
for m in [8,40,120,180]:
    r['recuperacao_por_maximo'][str(m)]={name:{'por_uso':ganho(m,pct),'total_maximo_sem_novo_descanso':limit*ganho(m,pct)} for name,(limit,pct) in GANHOS.items()}
# Exact checks and a second enumeration for short sequences.
from itertools import product
for q in [Fraction(1,4),Fraction(1,6),Fraction(1,8)]:
    for n in range(1,7):
        brute=defaultdict(Fraction)
        for seq in product([False,True],repeat=n):
            zeros=sum(seq);count=sum(seq[i-1] and not seq[i] for i in range(1,n))
            brute[count]+=q**zeros*(1-q)**(n-zeros)
        got=oportunidades(q,n)
        assert all(got[k]==brute[k] for k in set(got)|set(brute))
assert cap(8,0)==0 and cap(8,25)==2 and cap(0,25)==0 and ganho(0,25)==0
assert profile(10,4,DISTRIBUICOES['d6'])['tetos']==[0,10,20,30,40,40]
assert profile(10,4,DISTRIBUICOES['d6'])['custos']['liberacao_maxima']==14
assert oportunidades(Fraction(1,6),3)[1]==Fraction(5,18)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'janelas':r['janelas'],'recuperacao':r['recuperacao_por_maximo'],'resumo':r['resumo_58_perfis']},ensure_ascii=False,indent=2))

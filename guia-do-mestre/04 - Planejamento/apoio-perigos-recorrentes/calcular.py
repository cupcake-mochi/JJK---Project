"""Contas finitas e cronologia do exemplo; não é um motor completo da R53.
Sem --salvar, imprime apenas. Com --salvar, grava somente resultados.json.
"""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import argparse, json, math

def distribution(n,bonus=3,cd=14):
    one=defaultdict(Fraction)
    for die in range(1,21):
        for damage in range(1,7):
            one[damage if die+bonus<cd else 0]+=Fraction(1,120)
    total={0:Fraction(1)}
    for _ in range(n):
        nxt=defaultdict(Fraction)
        for a,pa in total.items():
            for b,pb in one.items():nxt[a+b]+=pa*pb
        total=dict(nxt)
    assert sum(total.values())==1
    return total

def main():
    checks=[]
    def check(name,truth):
        if not truth:raise AssertionError(name)
        checks.append(name)
    exposure_fail=8+3<14
    hp=max(0,44-4) if exposure_fail else 44
    check('fase1: falha causa4 e vida40',hp==40)
    poisoned=exposure_fail
    check('saídaR2:9+3falha',9+3<14)
    hp=min(44,hp+sum([1,1,2,3]))
    healer_pe=30-6
    check('cura limita ao máximo44 e não remove condição',hp==44 and poisoned)
    check('Akira paga6PE',healer_pe==24)
    if 12+3>=14:poisoned=False
    check('saídaR3:12+3encerra',not poisoned)
    # Posição ao fim da rodada, alimentação/exaustor e ordem de exposição→limpeza.
    progress=0; cloud=True; phases=[]
    for round_no,inside in [(1,True),(2,False)]:
        cloud_before=cloud
        exposed=inside and cloud
        before=progress
        progress+=1
        if progress>=2:cloud=False
        phases.append({'rodada':round_no,'nuvem_antes':cloud_before,'exposto':exposed,'limpeza_antes':before,'limpeza_depois':progress,'nuvem_depois':cloud})
    check('fase1 expõe antes de avançarlimpeza',phases[0]['exposto'] and phases[0]['nuvem_depois'])
    check('fase2 limpa mesmo sem ninguémexposto',not phases[1]['exposto'] and not phases[1]['nuvem_depois'])
    # O caso adverso mantém ocupante dentro até a última fase.
    last_exposure=phases[1]['nuvem_antes'] and True
    check('ficar dentro nafase2 ainda permite exposição',last_exposure and not phases[1]['nuvem_depois'])
    per_round_seconds=6; condition_start=1; condition_expiry=11
    check('dez ciclos completos=60segundos',(condition_expiry-condition_start)*per_round_seconds==60)
    # Tratamento da queda: o golpe inicial não consome rodada adicional.
    threshold=min(math.ceil(44/3),15*2)
    window=3; fallen_hp=max(0,3-4)
    check('queda inicial:0PV janela3',fallen_hp==0 and window==3)
    check('Insistirprimeiro:15tratamento',threshold==15)
    heal=sum([2,3,4,6]); rescued=heal>=threshold
    check('cura15encerraqueda antesdo próximo ponto',rescued and heal==15)
    adverse_window=window-1-1
    check('semretirada:tempoedano3para2para1',adverse_window==1)
    # Interações publicadas, sem atribuir estas proteções ao perfil deMei.
    protection_cases={
      'sem_protecao':{'dano':4,'condicao':True},
      'resistencia_veneno':{'dano':math.ceil(4/2),'condicao':True},
      'imunidade_dano':{'dano':0,'condicao':True},
      'imunidade_condicao':{'dano':4,'condicao':False}}
    check('pino compatível:7+5acerta12 e5d8mínimoquebra2',7+5==12 and 5>=2)
    refs={}
    for n in [1,2,3]:
        d=distribution(n)
        refs[str(n)]={'exposicoes':n,'dano_medio_antes_protecoes':float(sum(k*v for k,v in d.items())),
          'prob_algum_dano':float(sum(v for k,v in d.items() if k>0)),
          'prob_chegar_zero_com6PV':float(sum(v for k,v in d.items() if k>=6))}
    check('médias crescem comfrequência',[refs[str(n)]['dano_medio_antes_protecoes'] for n in [1,2,3]]==[1.75,3.5,5.25])
    return {'conferencias':checks,'percurso_principal':{'Mei':{'PV':hp,'PE':36,'Integridade':55,'Envenenado':poisoned,'Sequelas':0},'Akira':{'PV':51,'PE':healer_pe,'Integridade':65},'fases':phases},
      'ramo_queda':{'maximo_referencia':44,'tratamento':threshold,'PV_apos_socorro':15,'Sequelas':1,'PE_Akira':healer_pe,'janela_sem_retirada_apos_fase2':adverse_window},
      'protecoes':protection_cases,'exposicoes_independentes':refs,
      'limites':'Contas, distribuição de dano condicionada a exposição e cronologia escolhida. Não modela estratégias, todosos corpos/capacidades, desempenho de leitores ou dificuldade de missão.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--salvar',action='store_true');args=parser.parse_args()
    out=main();result=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    if args.salvar:Path(__file__).with_name('resultados.json').write_text(result)
    else:print(result,end='')

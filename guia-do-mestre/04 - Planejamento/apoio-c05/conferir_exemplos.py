"""Conferência aritmética dos exemplos de C05, sem simular uma partida."""
from pathlib import Path
from fractions import Fraction
import json
import math

checks=[]
def check(label,actual,expected):
    assert actual==expected,(label,actual,expected)
    checks.append({'caso':label,'resultado':actual})
def treatment(maximum,choice,highest_class):
    if choice=='Aguentar':return math.ceil(Fraction(maximum,4))
    return min(math.ceil(Fraction(maximum,3 if choice=='primeiro' else 2)),15*highest_class)
def short_rest(maximum,current,degree,propitious=False):
    rate=Fraction(1,4) if propitious else [Fraction(1,4),Fraction(15,100),Fraction(5,100),Fraction(0)][degree]
    amount=max(1,math.floor(maximum*rate)) if maximum>0 and rate>0 else 0
    return min(maximum,current+amount)
def long_outside(maximum,current):
    floor=max(1,math.floor(Fraction(maximum,2))) if maximum>0 else 0
    return max(current,floor)
check('vida 23 menos 5',23-5,18)
check('dano21 resistencia',math.ceil(Fraction(21,2)),11)
check('dano apos RD4 e temporarios3',11-4-3,4)
check('vida18 apos dano4',18-4,14)
check('teto temporario vida23',math.floor(Fraction(23,2)),11)
check('temporarios3 substituidos por9',max(3,9),9)
check('perda6 integridade26 abaixo1quarto',Fraction(6,26)<Fraction(1,4),True)
check('perda7 integridade26 atinge1quarto',Fraction(7,26)>=Fraction(1,4),True)
for maximum,hclass,expected in [(23,1,[6,8,12]),(93,3,[24,31,45]),(395,7,[99,105,105])]:
    for choice,answer in zip(['Aguentar','primeiro','posterior'],expected):
        check(f'tratamento {maximum} classe{hclass} {choice}',treatment(maximum,choice,hclass),answer)
check('tratamento31 acumulado18 faltante',31-18,13)
check('tratamento5+4 converte todo total',5+4,9)
check('estavel18 mais1 especial',18+1,19)
check('piloto total7+5',7+5,12)
check('piloto janela segundaqueda',3-1,2)
check('piloto volta ao ponto',2-1,1)
check('piloto dano posterior janela1',1-1,0)
check('corpo60kg volume',60/12,5)
check('carga propria2 corpo5 equipamento1',2+5+1,8)
check('limite Forca2',5+2,7)
check('carga8 entre normal7 e dobro14',7<8<=14,True)
check('deslocamento9 reduzido',9/2,4.5)
check('curto max10 saldo1',short_rest(10,1,0),3)
check('curto respeita maximo10 saldo9',short_rest(10,9,0),10)
for degree,expected in enumerate([2,1,1,0]):check(f'curto fora max8 degrau{degree}',short_rest(8,0,degree),expected)
for degree in range(4):check(f'curto propicio max8 degrau{degree}',short_rest(8,0,degree,True),2)
check('curto maxzero',short_rest(0,0,0),0)
check('longo fora vida23 saldo3',long_outside(23,3),11)
check('longo fora vida23 saldo18 nao reduz',long_outside(23,18),18)
check('longo fora PE60 saldo8',long_outside(60,8),30)
check('longo fora maxzero',long_outside(0,0),0)
check('integridade e Exaustao deslocamento9',min(4.5,9/2),4.5)
check('integridade e Exaustao deslocamento6',min(4.5,6/2),3)
result={'completo':True,'tipo':'aritmetica e casos de limite, nao teste de mesa','quantidade':len(checks),'casos':checks}
(Path(__file__).parent/'resultado-exemplos.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'completo':True,'conferencias':len(checks)},ensure_ascii=False))

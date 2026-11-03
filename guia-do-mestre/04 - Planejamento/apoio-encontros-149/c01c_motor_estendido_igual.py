"""C01c — o motor estendido, com os valores padrão, tem de dar o mesmo resultado do piloto em cada semente."""
from motor_estendido import simulate2, V
ok=True
for e,size,ini,seq in (('amontoado',3,1,0),('amontoado',2,1,0),('amontoado',3,.5,2),('vigia',3,1,0)):
    grupo=('frente','conjurador','apoio') if size==3 else ('frente','apoio')
    for blocked in (False,True):
        for mode in ('Insistir','Aguentar'):
            for i in range(2000):
                a=V.simulate([e],730000+i,mode,blocked,size,ini,seq,False); b=simulate2(grupo,(e,),730000+i,mode,blocked,ini,seq)
                if (a['outcome'],a['rounds'],a['derrotados'],a['morrendo'],a.get('quedas',0))!=(b['outcome'],b['rounds'],b['derrotados'],b['morrendo'],b.get('quedas',0)):
                    ok=False; print('diverge',e,size,ini,seq,blocked,mode,i,a,b); break
print('C01c:','IGUAL AO PILOTO em 32.000 combates' if ok else 'DIVERGE')

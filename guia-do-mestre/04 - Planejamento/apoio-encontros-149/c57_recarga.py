"""Refaz os números publicados no caso 57 (registro 15) com o Impacto em Recarga (5–6), mesmas sementes e premissas."""
import statistics
from motor_estendido import simulate2
for nome,ini,seq in (('trio cheio',1,0),('trio com metade da vida e 2 Sequelas',.5,2)):
    for rec in ('pe','recarga56'):
        rs=[simulate2(seed=730000+i,initial=ini,sequelas=seq,recurso=rec) for i in range(5000)]
        print(f"{nome:<38} {rec:<10} mediana {statistics.median(r['rounds'] for r in rs)}  queda {100*sum(r.get('quedas',0)>0 for r in rs)/5000:.2f}%  Derrotado {100*sum(r['derrotados']>0 for r in rs)/5000:.2f}%")

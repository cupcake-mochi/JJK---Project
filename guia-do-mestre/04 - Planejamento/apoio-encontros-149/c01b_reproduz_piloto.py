"""C01b — portão da simulação: o motor do piloto (registro 15, apoio-piloto/validar_base.py, copiado sem mudança
para motor/) precisa reproduzir os números publicados no registro 15 e no caso 57, com as mesmas sementes."""
import sys, statistics; from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'motor'))
import validar_base as V
pub={('amontoado',3,1,0):(2,20.36,0.34),('amontoado',2,1,0):(3,34.90,5.38),('amontoado',3,.5,2):(2,60.50,24.40),
     ('rastejante',3,1,0):(1,0.00,0.00),('vigia',3,1,0):(1,10.66,0.08)}
ok=True
for (e,size,ini,seq),(med,q,der) in pub.items():
    runs=[V.simulate([e],730000+i,'Insistir',False,size,ini,seq,False) for i in range(5000)]
    m=statistics.median(r['rounds'] for r in runs); qq=round(100*sum(r.get('quedas',0)>0 for r in runs)/5000,2); dd=round(100*sum(r['derrotados']>0 for r in runs)/5000,2)
    b=(m==med and qq==q and dd==der); ok&=b
    print(f"{e:<11} grupo {size} vida {ini} sequelas {seq}: publicado {med} rod · {q}% queda · {der}% Derrotado | motor {m} · {qq}% · {dd}%  {'OK' if b else 'DIVERGE'}")
print('PORTÃO C01b:','PASSOU' if ok else 'FALHOU')

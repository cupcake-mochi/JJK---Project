from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json,itertools
E=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial/equipamento');B=E/'lote-06'
W=json.loads((E/'lote-04-r3/ARMAS.json').read_text())
# Sensitivity recorded before selecting the new candidate.
values=[]
for v,r,n,strength,traje in itertools.product([3,4,5,7],[.5,1,1.5],[0,1,2,3],[0,3,4,5,6],[.1,2]):
 total=F(str(v))+n*F(str(r))+F('1.2')+F(str(traje));values.append({'volume_arma':v,'volume_reserva':r,'reservas':n,'forca':strength,'traje':traje,'carga':float(total),'cabe':total<=5+strength,'cumpre_manejo':strength>=3})
(B/'evidencias/sensibilidade-metralhadora.json').write_text(json.dumps(values,ensure_ascii=False,indent=2)+'\n')
for v,r in [(7,1.5),(5,1),(4,1),(4,.5),(3,.5)]:
 t=F(str(v))+2*F(str(r))+F('1.3');print('Metralhadora',v,'reserva',r,'conjunto',float(t),'folga Força3',float(8-t))

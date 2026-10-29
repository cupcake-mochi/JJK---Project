import json,sys
from pathlib import Path
A=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/04 - Planejamento/apoio-revisao-integral-94')
p=A/'segunda-leitura/manifesto.json';d=json.loads(p.read_text());d['lidas']=sorted(set(d['lidas'])|set(range(int(sys.argv[1]),int(sys.argv[2])+1)));d['correcoes'].append({'paginas':[int(sys.argv[1]),int(sys.argv[2])],'observacao':sys.argv[3]});p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

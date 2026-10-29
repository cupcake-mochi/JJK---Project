from pathlib import Path
import json,hashlib,sys
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/04 - Planejamento/apoio-revisao-integral-94/visual-prova-2');p=r/'inspecao.json';v=json.loads(p.read_text()) if p.exists() else {'paginas':{},'notas':[]}
for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
 f=r/f'p-{n:03}.png';v['paginas'][str(n)]={'sha256_png':hashlib.sha256(f.read_bytes()).hexdigest(),'conferida':True}
v['notas'].append({'paginas':[int(sys.argv[1]),int(sys.argv[2])],'observacao':sys.argv[3]});p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

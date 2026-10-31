from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];R=B/'revisao-r48'
a=json.loads((R/'ensaio-04/FONTES-E-VALIDACAO.json').read_text());b=json.loads((B/'FONTES-E-VALIDACAO.json').read_text())
def sig(m,p):
 return json.dumps([{k:v for k,v in e.items() if k not in {'pagina','faixa'}} for e in m['eventos'] if e['pagina']==p],ensure_ascii=False,sort_keys=True)
old={sig(a,p):p for p in range(1,a['paginas']+1)};same=[];changed=[]
for p in range(1,b['paginas']+1):
 q=old.get(sig(b,p))
 if q:same.append({'atual':p,'ensaio_anterior':q})
 else:changed.append(p)
r={'paginas':b['paginas'],'mesma_composicao_ja_vista':same,'conferir_novamente':changed}
(R/'COMPARACAO-ENSAIO-FINAL.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Sem alteração de composição:',len(same),'Conferir:',len(changed));print(changed)

from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r56'
def aplicar(textos,blocos,capitulos,meta):
    base=json.loads((B/'revisao-r55/BLOCOS-R55.json').read_text())
    assert textos==base
    final=json.loads((R/'TEXTOS-TRABALHO.json').read_text())
    assert set(base)==set(final)
    for k,t in final.items():
        assert re.findall(r'^#+ .+',t,re.M)==re.findall(r'^#+ .+',base[k],re.M)
        blocos[k].text=t
    textos.clear();textos.update(final)
    (R/'BLOCOS-R56.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
    return json.loads((B/'ALTERACOES-R55-para-R56.json').read_text())

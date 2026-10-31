"""R55: segunda conferência integral, clareza e destinos do índice."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r55'
def aplicar(textos,blocos,capitulos,meta):
    base=json.loads((B/'revisao-r54/BLOCOS-R54.json').read_text())
    assert textos==base,'Base R54 divergente'
    final=json.loads((R/'TEXTOS-TRABALHO.json').read_text())
    assert set(base)==set(final)
    for k,t in final.items():
        assert re.findall(r'^#+ .+',t,re.M)==re.findall(r'^#+ .+',base[k],re.M),k
        blocos[k].text=t
    ip=B/'revisao-de-estrutura/DESTINOS-INDICE.json'
    index=json.loads(ip.read_text());extra=json.loads((R/'ALIASES-INDICE.json').read_text())
    known={r['alias'] for r in index}
    index.extend(r for r in extra if r['alias'] not in known)
    ip.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    valid=set(final)|set(json.loads((B/'revisao-r53/ALIASES-RESOLVIDOS.json').read_text()))|{r['alias'] for r in index}
    assert not [(k,a) for k,t in final.items() for a in re.findall(r'\]\(#([^)]+)\)',t) if a not in valid]
    textos.clear();textos.update(final)
    (R/'BLOCOS-R55.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
    return json.loads((B/'ALTERACOES-R54-para-R55.json').read_text())

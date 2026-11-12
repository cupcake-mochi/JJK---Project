"""R54: introdução dos conceitos antes de seu uso e remissões locais."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r54'
def aplicar(textos,blocos,capitulos,meta):
    base=json.loads((B/'revisao-r53/BLOCOS-R53.json').read_text())
    assert textos==base,'Base R53 divergente'
    final=json.loads((R/'TEXTOS-TRABALHO.json').read_text())
    assert set(base)==set(final)
    for k,t in final.items():
        assert re.findall(r'^#+ .+',t,re.M)==re.findall(r'^#+ .+',base[k],re.M),k
        blocos[k].text=t
    aliases=json.loads((B/'revisao-r53/ALIASES-RESOLVIDOS.json').read_text())
    index=json.loads((B/'revisao-de-estrutura/DESTINOS-INDICE.json').read_text())
    valid=set(final)|set(aliases)|{r['alias'] for r in index}
    missing=[(k,a) for k,t in final.items() for a in re.findall(r'\]\(#([^)]+)\)',t) if a not in valid]
    assert not missing,missing
    invpath=B/'DESTAQUES-CATALOGO.json'
    inv=json.loads(invpath.read_text());known={(n['bloco'],n['texto']) for n in inv}
    for k,t in final.items():
        for line in t.splitlines():
            if line.startswith('> ') and (k,line[2:]) not in known:
                inv.append(dict(id=f'R54-NOTA-{len(inv)+1}',bloco=k,texto=line[2:],tipo='exemplo' if 'Exemplo' in line[:20] else 'regra-chave',motivo='R54: conservar o tratamento do destaque revisado.'))
                known.add((k,line[2:]))
    invpath.write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
    textos.clear();textos.update(final)
    (R/'BLOCOS-R54.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
    return json.loads((B/'ALTERACOES-R53-para-R54.json').read_text())

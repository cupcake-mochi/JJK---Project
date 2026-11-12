from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r57'
def aplicar(textos,blocos,capitulos,meta):
    base=json.loads((B/'revisao-r56/BLOCOS-R56.json').read_text())
    assert textos==base
    final=json.loads((R/'TEXTOS-TRABALHO.json').read_text())
    assert set(base)==set(final)
    for k,t in final.items():
        assert re.findall(r'^#+ .+',t,re.M)==re.findall(r'^#+ .+',base[k],re.M)
        blocos[k].text=t
    invpath=B/'DESTAQUES-CATALOGO.json'
    inv=json.loads(invpath.read_text());known={(n['bloco'],n['texto']) for n in inv}
    for k,t in final.items():
        for line in t.splitlines():
            if line.startswith('> ') and (k,line[2:]) not in known:
                inv.append(dict(id=f'R57-NOTA-{len(inv)+1}',bloco=k,texto=line[2:],tipo='exemplo' if 'Exemplo' in line[:20] else 'regra-chave',motivo='R57: conservar o tratamento do destaque revisado.'))
                known.add((k,line[2:]))
    invpath.write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
    textos.clear();textos.update(final)
    (R/'BLOCOS-R57.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
    return json.loads((B/'ALTERACOES-R56-para-R57.json').read_text())

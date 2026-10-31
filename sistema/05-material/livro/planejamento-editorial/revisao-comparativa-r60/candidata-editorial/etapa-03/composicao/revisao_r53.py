"""Integra o capítulo Fundamento v8 aprovado, com migração das dependências."""
from pathlib import Path
import json,re,hashlib,copy
B=Path(__file__).resolve().parent;R=B/'revisao-r53'
def read(name):return json.loads((R/name).read_text())
def save(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def aplicar(textos,blocos,capitulos,meta):
    base=dict(textos)
    assert base==read('BLOCOS-R52.json'),'A base de integração mudou'
    final=read('TEXTOS-TRABALHO.json');specs=read('META-NOVA.json');aliases=read('ALIASES.json');notes=read('NOTAS-DEPENDENCIAS.json')
    rows=[]
    for key in sorted(set(base)|set(final)):
        a=base.get(key,'');z=final.get(key,'')
        if a==z:continue
        reason='Integrar o texto do capítulo Fundamento v8 aprovado pelo autor, preservando seus custos, permissões e exemplos.' if key in specs else 'Adaptar as referências e montagens dependentes ao capítulo aprovado.'
        if key in notes:reason+=' '+' '.join(dict.fromkeys(notes[key]))
        if not z:reason='Entrada substituída pela organização do catálogo aprovado. Seu destino anterior é preservado por alias explícito.'
        rows.append(dict(id=f'R53-{len(rows)+1:03d}',bloco=key,antes=a,depois=z,motivo=reason,item='Fundamento, integração do capítulo v8 aprovado em 18/10/2026'))
    save(B/'ALTERACOES-R52-para-R53.json',rows)
    for key in list(blocos):
        if key not in final:blocos.pop(key);meta.pop(key,None)
    Block=type(next(iter(blocos.values())))
    for key,z in final.items():
        if key not in blocos:
            doc,anchor=key.split('--',1);blocos[key]=Block(doc,anchor,re.sub(r'^#+ ','',z.splitlines()[0]),z)
        blocos[key].title=re.sub(r'^#+ ','',z.splitlines()[0]);blocos[key].text=z
        if key in specs:
            cfg=specs[key];hs=[{'titulo':h['titulo'],'nivel':h['nivel_editorial'],'papel':'procedimento ou entrada'} for h in cfg['titulos']]
            meta[key]={'bloco':key,'capitulo':cfg['capitulo'],'titulo_original':blocos[key].title,'papel':'procedimento ou entrada','contexto':cfg['contexto'],'parent':None,'marcador':None,'sem_titulo_inicial':False,'titulos':hs,'nivel_primeiro':hs[0]['nivel']}
    textos.clear();textos.update(final)
    orders=read('ORDEM-NOVA.json')
    for ch in capitulos:
        for group in ch['grupos']:
            if group['doc'] in orders:group['blocks']=[blocos[k] for k in orders[group['doc']]]
            else:group['blocks']=[blocos[b.key] for b in group['blocks'] if b.key in blocos]
    classification=json.loads((B/'revisao-r45/CLASSIFICACAO.json').read_text())
    classification=[r for r in classification if r['bloco'] not in specs and r['bloco'] in final]
    for key,cfg in specs.items():
        for h in cfg['titulos']:
            if h['tratamento']:
                classification.append(dict(bloco=key,titulo=h['titulo'],tipo_original=h['tipo'],tratamento=h['tratamento'],nivel_editorial=h['nivel_editorial'],motivo='R53: preservar a função visual do título no capítulo aprovado.'))
    save(B/'revisao-r45/CLASSIFICACAO.json',classification)
    save(B/'revisao-de-estrutura/HIERARQUIA.json',meta)
    nav=json.loads((B/'revisao-r45/NAVEGACAO.json').read_text())
    nav=[r for r in nav if r['capitulo'] not in {10,11}]
    for doc,chno in [('fundamento',10),('catalogo',11)]:
        for key in orders[doc]:
            if key in {'fundamento--fundamento','catalogo--cat-catalogo'}:continue
            if doc=='catalogo' and key.startswith(('catalogo--melhoria-','catalogo--restricao-')):continue
            if doc=='catalogo' and key.startswith('catalogo--grupo-'):continue
            title=blocos[key].title
            nav.append(dict(capitulo=chno,destino=key,titulo=title,nivel=2))
    nav.sort(key=lambda x:x['capitulo']);save(B/'revisao-r45/NAVEGACAO.json',nav)
    # Preservar os destinos de leitores que já usavam a navegação anterior.
    original=read('DESTINOS-INDICE-R52.json')
    entries=read('ENTRADAS.json');known={k:{h['titulo'] for h in cfg['titulos']} for k,cfg in specs.items()}
    rename={'Dívida':'Sobrecusto','Corpo a Corpo':'Queima-Roupa','Puxa':'Empurrão','Adianta':'Precisão','Muito Longe':'Longe','Muito Maior':'Maior','Junto':'Mais Um'}
    kept=[]
    for row in original:
        block=row['bloco'];title=row.get('titulo',row['termo']);name=rename.get(title,title)
        if block not in specs and block in final:kept.append(row);continue
        if block in final and title in known.get(block,set()):kept.append(row);continue
        if name in entries:aliases[row['alias']]={'bloco':entries[name],'titulo':name}
        elif title=='Certeiro':aliases[row['alias']]={'bloco':'fundamento--conjurar','titulo':'Conjurar'}
        elif title in {'Onda','Apoio','Cura'}:aliases[row['alias']]={'bloco':'fundamento--funcoes','titulo':'Funções e saldo'}
        elif block in aliases:aliases[row['alias']]=dict(aliases[block])
        elif block in final:aliases[row['alias']]={'bloco':block,'titulo':blocos[block].title}
    save(B/'revisao-de-estrutura/DESTINOS-INDICE.json',kept)
    save(R/'ALIASES-RESOLVIDOS.json',aliases)
    inventory=json.loads((B/'DESTAQUES-CATALOGO.json').read_text())
    sig=lambda k,t:hashlib.sha256(json.dumps([k,t],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    existing={sig(n['bloco'],n['texto']):n for n in inventory}
    for key,text in final.items():
        for l in text.splitlines():
            if not l.startswith('> '):continue
            t=l[2:];s=sig(key,t)
            if s not in existing:
                n={'id':f'R53-NOTA-{len(existing)+1}','bloco':key,'texto':t,'tipo':'ficha de exemplo' if t.startswith('**Na ficha') else 'regra-chave' if t.startswith('**Restrição paga') else 'exemplo','motivo':'Exemplo e destaque de consulta do capítulo aprovado.'};existing[s]=n
    save(B/'DESTAQUES-CATALOGO.json',list(existing.values()))
    valid=set(final)|set(aliases)|{r['alias'] for r in kept}
    missing=[(k,t) for k,v in final.items() for t in re.findall(r'\]\(#([^)]+)\)',v) if t not in valid]
    assert not missing,missing
    save(R/'BLOCOS-R53.json',final)
    return rows

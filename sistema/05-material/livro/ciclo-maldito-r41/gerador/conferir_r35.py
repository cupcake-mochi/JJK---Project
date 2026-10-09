"""Texto, classificação, continuidade e registro integral da diagramação R35."""
from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json,difflib
B=Path(__file__).resolve().parent;OLD=B.parent/'livro-diagramado-r34';R=B/'revisao-de-hierarquia'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=read(B/'FONTES-E-VALIDACAO.json');old=read(OLD/'FONTES-E-VALIDACAO.json')
assert sha(B/m['pdf'])==m['sha256_pdf']
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(OLD/'LIVRO-COMPLETO.md').read_bytes(),'Texto mudou'
assert all(sha(OLD/f)==h for f,h in read(R/'BASE-R34-HASHES.json').items()),'Base R34 mudou'
for f in ['ESTUDO-DENSIDADE.json','ESTUDO-TABELAS.json','ESTUDO-SECAO.json','ESTUDO-CAPITULO.json','revisao-de-regras/ALTERACOES-REGRAS.json','CREDITOS.json','CAPA-E-ABERTURAS.json']:
    assert (B/f).read_bytes()==(OLD/f).read_bytes(),f
source=lambda z:[(e['bloco'],e['tipo'],e['texto']) for e in z['eventos'] if not e['gerado']]
assert source(m)==source(old),'Ordem ou conteúdo dos elementos mudou'
assert set(m['ancoras'])==set(old['ancoras']),'Âncoras mudaram'
for field in ['imagens','alteracoes_regras']:
    assert m[field]==old[field],field
cover=lambda z:[{k:v for k,v in r.items() if k!='pagina'} for r in z['capas_e_aberturas']]
assert cover(m)==cover(old),'Capas alteradas'
# A área reservada ao texto pode variar, mas o desenho das artes é invariável.
art=lambda z:[{k:v for k,v in r.items() if k not in {'pagina','topo_texto_livre'}} for r in z['posicionamento_imagens']]
assert art(m)==art(old),'Artes ou seus recortes mudaram'
heads={'h1','h2','h3','major','marker'}
classified=read(R/'CLASSIFICACAO.json');lookup={(r['bloco'],r['titulo']):r for r in classified}
applied=[];orphans=[];same=[];by=defaultdict(list)
for e in m['eventos']:by[e['pagina']].append(e)
for i,e in enumerate(m['eventos']):
    if not e['gerado'] and e['tipo'] in heads:
        row=lookup.get((e['bloco'],str(e['texto']).strip('*')))
        if row:
            assert e['tratamento_hierarquia']==row['tratamento'],row
            applied.append({'bloco':e['bloco'],'titulo':str(e['texto']).strip('*'),'tratamento':e['tratamento_hierarquia'],'pagina':e['pagina']})
        if i+1<len(m['eventos']):
            nxt=m['eventos'][i+1]
            if nxt['gerado'] and nxt['tipo']=='small':orphans.append(e)
            elif nxt['pagina']!=e['pagina']:orphans.append(e)
            elif nxt['x']!=e['x'] and e['largura']<300:orphans.append(e)
            elif nxt['tipo'] in heads and (e.get('tratamento_hierarquia') or e['tipo'])==(nxt.get('tratamento_hierarquia') or nxt['tipo']):same.append([e,nxt])
assert len(applied)==len(classified),(len(applied),len(classified))
assert not orphans,orphans
assert not same,same
multiple=[]
for pn,es in by.items():
    bands={e['faixa'] for e in es if e['modo']=='duas-colunas'}
    if len(bands)>1:multiple.append(pn)
assert not multiple,multiple
bound=[]
for a in read(B/'revisao-de-continuidade/ABERTURAS.json'):
    if a['ligacao']!='abertura completa' or 'unidos' not in a['resultado']:continue
    es=m['eventos'];parents=[i for i,e in enumerate(es) if e['bloco']==a['bloco'] and e['tipo'] in heads and e['texto']==a['titulo']]
    good=False
    for i in parents:
        children=[e for e in es[i+1:] if e['bloco']==a['bloco_entrada'] and e['tipo'] in heads and e['texto']==a['primeira_entrada']]
        if children and es[i]['pagina']==children[0]['pagina'] and es[i]['x']==children[0]['x']:good=True;break
    assert good,a
    bound.append(a)
def group(z):
    d=defaultdict(list)
    for e in z['eventos']:d[e['bloco'] or '__elementos_gerados__'].append(e)
    return d
before,after=group(old),group(m);changes=[]
for block in dict.fromkeys([*before,*after]):
    if before[block]==after[block]:continue
    changes.append({'id':f'D35-{len(changes)+1:03}','bloco':block,'antes':before[block],'depois':after[block],
        'motivo':'Aplicação do tratamento B aprovado aos grupos, subtópicos e exemplos; classificação de capacidades nomeadas como entradas. Recomposição e paginação decorrentes, preservando texto, regras e ordem de leitura.'})
save(R/'ALTERACOES-DIAGRAMACAO.json',changes);save(R/'ALTERACOES-TEXTO.json',[]);save(R/'TITULOS-APLICADOS.json',applied)
files=['gerar_livro.py','fluxo_continuo.py','titulos_intermediarios.py','ESTUDO-HIERARQUIA.json'];patch=[];impl=[]
for f in files:
    a=OLD/f;b=B/f
    impl.append({'arquivo':f,'sha256_antes':sha(a) if a.exists() else None,'sha256_depois':sha(b)})
    patch.extend(difflib.unified_diff(a.read_text().splitlines(keepends=True) if a.exists() else [],b.read_text().splitlines(keepends=True),fromfile='R34/'+f,tofile='R35/'+f))
save(R/'REGISTRO-IMPLEMENTACAO.json',impl);(R/'IMPLEMENTACAO.patch').write_text(''.join(patch))
summary={'edicao':'R35','base':'R34','opcao':'B','paginas_antes':old['paginas'],'paginas':m['paginas'],'sha256_pdf':m['sha256_pdf'],'sha256_texto':sha(B/'LIVRO-COMPLETO.md'),'r34_preservada':True,'texto_identico':True,'elementos_editoriais_identicos_em_ordem':len(source(m)),'titulos_aplicados':len(applied),'tratamentos':dict(Counter(e['tratamento'] for e in applied)),'blocos_registrados':len(changes),'aberturas_verificadas_na_mesma_coluna':len(bound),'titulos_consecutivos_com_mesmo_tratamento':0,'titulos_isolados':0,'paginas_com_multiplos_pares_de_colunas':multiple,'capas_artes_creditos_preservados':True,'problemas':[],'revisao_visual':'Registro separado em REVISAO-PAGINAS.json.'}
save(R/'CONFERENCIA.json',summary);print(json.dumps(summary,ensure_ascii=False))

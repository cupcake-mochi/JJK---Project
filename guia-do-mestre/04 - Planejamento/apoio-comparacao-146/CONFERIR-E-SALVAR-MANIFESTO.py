"""Conferência de preservação e união do registro 146. Executar uma única vez."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup
import hashlib, json, re, markdown

A=Path(__file__).resolve().parent
R=A.parents[1]
M=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
load=lambda p:json.loads(p.read_text())
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

def main():
    base=load(A/'antes/manifesto-entrega.json')
    assert len(base)==6363 and load(M)==base
    cfg=load(A/'arquivos-do-lote.json')
    allowed=set(cfg['controles'])
    assert len(allowed)==12
    assert cfg['fontes_alteradas']==cfg['html_alterados']==cfg['pdfs_alterados']==[]
    changed=[];fail=[]
    def check(item):
        rel,old=item;p=R/rel
        if not p.is_file():return rel,None
        return rel,sha(p)
    actual={}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for i,(rel,digest) in enumerate(pool.map(check,base.items()),1):
            actual[rel]=digest
            if digest is None:fail.append('Ausente: '+rel)
            elif digest!=base[rel]:
                changed.append(rel)
                if rel not in allowed:fail.append('Alteração não declarada: '+rel)
            if i%1500==0:print('Entradas anteriores conferidas:',i,flush=True)
    assert not fail,fail
    assert set(changed)==allowed,changed
    sources=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')['fontes']
    assert len(sources)==104
    assert all(actual.get(x['fonte'])==x['sha256'] for x in sources)
    coverage=load(R/'04 - Planejamento/apoio-leitura-144/cobertura-da-leitura-continua.json')['fontes']
    assert len(coverage)==99
    assert all(actual.get(x['fonte'])==x['sha256_atual'] for x in coverage)
    html=[k for k in base if k.startswith('07 - Edicao de Leitura/edicao-integrada-136/') and k.endswith('.html')]
    assert len(html)==99 and all(actual[k]==base[k] for k in html)
    refs=load(A/'fontes-consultadas.json')
    for key in ['guia_atual','guia_anterior']:
        x=refs[key];assert actual[x['arquivo']]==x['sha256']
    assert refs['guia_atual']['sha256']=='fce0184a2d944e2afac552627b13878361421157126eb9ebb7d614296ca129d2'
    for x in refs['livros']:
        assert sha(R/x['arquivo'])==x['sha256']
        assert all(1<=n<=x['paginas_totais'] for n in x['paginas_usadas_na_avaliacao'])
    report=R/cfg['relatorio']
    matrix=(A/'matriz-de-resultados.md').read_text()
    ids=re.findall(r'^\| (P\d\d) ',matrix,re.M)
    assert ids==[f'P{n:02}' for n in range(1,21)],ids
    for heading in ['## Falta algo','## Está no mesmo patamar','## Temos o que faz bons guias serem úteis']:
        assert heading in report.read_text()
    prospective={A/'conferencia-do-manifesto.json',A/'revisao-do-parecer.json'}
    docs=[report]+list(A.glob('*.md'))
    links=0
    for p in docs+[R/c for c in allowed]:
        body=p.read_text()
        if p not in docs:
            assert body.count('Fila vigente - registro 146')==1
            assert 'Fila vigente - registro 145' not in body
            body=next(x for x in body.split('\n\n') if x.startswith('> **Fila vigente - registro 146'))
        tags=BeautifulSoup(markdown.markdown(body,extensions=['tables']),'html.parser').find_all('a',href=True)
        for tag in tags:
            u=urlsplit(tag['href'])
            if not u.scheme and u.path:
                dest=(p.parent/unquote(u.path)).resolve()
                assert dest.is_file() or dest in prospective,(p,tag['href'])
                links+=1
    pairs=load(A/'visuais/pares.json');assert len(pairs)==7
    for name,*_ in pairs:assert (A/'visuais'/(name+'.png')).is_file()
    save(A/'revisao-do-parecer.json',{
        'registro':146,'passagens':[
            'Redação confrontada com tarefas, páginas e referências selecionadas.',
            'Releitura integral do parecer, matriz e notas após a redação; fila do plano 98 conferida.'],
        'correcoes_na_releitura':[
            'Incluída a página 8 entre as ampliações efetivamente inspecionadas.',
            'Acrescentada relação legível das sete obras, edições e páginas.',
            'Removida frase que poderia sugerir participação de leitor externo.',
            'Substituída a próxima tarefa antiga da seção 7 do plano 98 pela fila atual.'],
        'competencias_com_destino':ids,'links_locais_conferidos':links,
        'metodo_visual':'Sete pares examinados, mais páginas 8, 115 e 120 em ampliações do apoio 145.',
        'nova_inspecao_integral_do_pdf':False,'novas_regras':False,
        'limites':'Consulta comparativa interna, sem participantes externos, mesa real ou validação geral de equilíbrio.'})
    audit={
        'registro':146,'entradas_anteriores':len(base),'controles_atualizados':sorted(changed),
        'fontes_originais_preservadas':104,'fontes_integradas_preservadas':99,'html_preservados':99,
        'pdf_atual_preservado':refs['guia_atual'],'pdf_anterior_preservado':refs['guia_anterior'],
        'referencias_locais_conferidas':7,'competencias_com_destino':20,'links_locais_conferidos':links,
        'demais_arquivos_anteriores_preservados':len(base)-len(changed),'falhas':[],
        'salvamento':'Local; último envio remoto conhecido: registro 141.'}
    out=A/'conferencia-do-manifesto.json'
    save(out,audit)
    files=[R/c for c in allowed]+[report]+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    additions={p.relative_to(R).as_posix() for p in files}-set(base)
    audit['novas_entradas']=len(additions)
    audit['entradas_finais']=len(base)+len(additions)
    save(out,audit)
    updated=dict(base)
    for p in files:updated[p.relative_to(R).as_posix()]=sha(p)
    assert set(base)<=set(updated) and len(updated)==audit['entradas_finais']
    assert load(M)==base,'Manifesto mudou durante a auditoria.'
    save(M,updated);assert load(M)==updated
    print(json.dumps({k:audit[k] for k in ['entradas_anteriores','novas_entradas','entradas_finais','falhas']},ensure_ascii=False),flush=True)

if __name__=='__main__':main()

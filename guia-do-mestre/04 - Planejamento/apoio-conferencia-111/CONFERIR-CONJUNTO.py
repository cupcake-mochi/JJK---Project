"""Preservação documental e navegação; a leitura dirigida fica registrada separadamente."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
from bs4 import BeautifulSoup
import hashlib, json, markdown
A=Path(__file__).resolve().parent
R=A.parents[1]
BEFORE=A/'antes'
P105=R/'04 - Planejamento/apoio-consultas-105'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def read(p): return json.loads(p.read_text())
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def soup(p):
    t=p.read_text()
    return BeautifulSoup(t if p.suffix=='.html' else markdown.markdown(t,extensions=['tables','toc']),'html.parser')
def main():
    previous=read(BEFORE/'04 - Planejamento/apoio-piloto/manifesto-entrega.json')
    structure=read(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json')
    sources={s['fonte']:s for s in structure['fontes']}
    assert len(sources)==104
    for rel,s in sources.items(): assert sha(R/rel)==s['sha256'],rel
    before=read(BEFORE/'04 - Planejamento/apoio-consultas-105/destinos-e-fontes.json')
    after=read(P105/'destinos-e-fontes.json')
    assert before['fontes']==after['fontes'] and before['casos']==after['casos']
    counts={k:len(v) for k,v in after['casos'].items()}
    assert list(counts.values())==[9,23,9,6,12] and sum(counts.values())==59
    coverage=read(P105/'conferencia-de-cobertura.json')
    assert (P105/'conferencia-de-cobertura.json').read_bytes()==(BEFORE/'04 - Planejamento/apoio-consultas-105/conferencia-de-cobertura.json').read_bytes()
    sections={}; targets=[]; preserved=[]
    for n,folder in [(6,'inimigos-106'),(7,'personagens-107'),(8,'entre-missoes-108'),(9,'pactos-entidades-109'),(10,'guilda-110')]:
        d=R/('04 - Planejamento/apoio-'+folder)
        meta=read(d/'amostra.json')
        for key,hashkey in [('fonte','fonte_sha256'),('pdf','pdf_sha256'),('livro_de_regras','livro_de_regras_sha256')]:
            assert sha(R/meta[key])==meta[hashkey],meta[key]
        for file in [R/meta['fonte'],R/meta['pdf'],d/f'capitulo-{n}.html',d/'consulta-de-regras.html']:
            rel=str(file.relative_to(R));assert sha(file)==previous[rel],rel;preserved.append(rel)
        targets.extend([R/meta['fonte'],d/f'capitulo-{n}.html',d/'consulta-de-regras.html'])
        for s in read(d/'mapa-do-capitulo.json')['secoes']:
            sections[s['destino']]=str((d/f'capitulo-{n}.html').relative_to(R))+'#'+s['ancora']
    finalcov={'registro':111,'metodo':'Preservação de evidências e destinos documentais; estados herdados não reavaliados como aprendizagem ou equilíbrio.','pontos':[],'competencias':[]}
    for kind,prefix,total in [('pontos','M',130),('competencias','P',20)]:
        assert [x['id'] for x in coverage[kind]]==[f'{prefix}{i:03d}' if prefix=='M' else f'{prefix}{i:02d}' for i in range(1,total+1)]
        for item in coverage[kind]:
            methods=set()
            for source in item['fontes_preservadas']:
                assert sha(R/source['fonte'])==source['sha256_atual']
                for code in [source['destino_principal']]+source['usos_complementares']:
                    if code in sections: methods.add(sections[code])
            finalcov[kind].append(dict(item,metodos_6_a_10_localizados=sorted(methods),tipo='preservação documental; leitura dirigida separada'))
    write(A/'cobertura-e-destinos.json',finalcov)
    meta=read(P105/'amostra.json')
    for s in meta['fontes']:assert sha(R/s['fonte'])==s['sha256']
    for key in ['pdf','estilo']:
        assert sha(R/meta[key])==meta[key+'_sha256']
    assert sha(R/meta['html'])==meta['html_sha256']
    assert sha(R/meta['guia_de_escolha']['fonte'])==meta['guia_de_escolha']['sha256']
    oldhtml=soup(BEFORE/'04 - Planejamento/apoio-consultas-105/folhas-para-a-mesa.html');newhtml=soup(P105/'folhas-para-a-mesa.html')
    assert str(oldhtml.main)==str(newhtml.main)
    assert [s.get_text() for s in oldhtml.find_all('style')]==[s.get_text() for s in newhtml.find_all('style')]
    assert sha(R/meta['pdf'])==previous[meta['pdf']]
    book='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
    assert sha(R/book)==structure['pdf_base']['sha256']==previous[book]
    routes=read(A/'rotas-de-consulta.json')
    hub=soup(P105/'casos-completos.html')
    for group,route in routes['grupos'].items():
        assert any(route['metodo'].split('/')[-2] in x['href'] for x in hub.find_all('a',href=True)),group
    assert routes['avisos']['s089'] in hub.get_text(' ',strip=True)
    originalmap=read(R/'07 - Edicao de Leitura/mapa-editorial.json')
    byid={x['id']:x for x in originalmap['fontes']}
    for route in routes['grupos'].values():
        for sid in route['folhas']+[route['consulta_publicada']] if 'consulta_publicada' in route else route['folhas']:
            assert any(x['href'].endswith('#'+sid) for x in hub.find_all('a',href=True)),sid
    # Escala fixa publicada: a CD 16 do caso não tem justificativa de CD por criador.
    base=(R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md').read_text()
    difficulty=base.split('##### Dificuldade',1)[1].split('Quando a dificuldade',1)[0]
    fixed=[int(line.split('|')[2].strip()) for line in difficulty.splitlines() if line.startswith('| ') and line.split('|')[2].strip().isdigit()]
    assert fixed==[6,10,14,18,22,26] and 16 not in fixed
    assert 'História CD 16, dificuldade local anunciada pelo mestre' in (R/byid['s089']['fonte']).read_text()
    # Inspeção de arquivos e âncoras; não executa um navegador.
    targets.extend([P105/'casos-completos.html',P105/'folhas-para-a-mesa.html',P105/'destinos-dos-casos.md',R/meta['guia_de_escolha']['fonte'],R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md',R/'04 - Planejamento/111-conferencia-conjunta-das-consultas.md'])
    targets.extend(R/s['fonte'] for s in meta['fontes'])
    cache={}; links=[]
    for p in targets:
        doc=soup(p);ids=[x['id'] for x in doc.find_all(id=True)];assert len(ids)==len(set(ids)),p
        for tag in doc.find_all('a',href=True):
            u=urlsplit(tag['href'])
            if u.scheme: continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
            assert target.is_file() or target==A/'conferencias.json',(p,tag['href'])
            if u.fragment:
                if target not in cache:cache[target]=soup(target)
                assert cache[target].find(id=unquote(u.fragment)),(p,tag['href'])
            links.append({'origem':str(p.relative_to(R)),'destino':tag['href']})
    result={'registro':111,'fontes_antigas_preservadas':104,'casos_preservados':59,'casos_por_grupo':counts,'pontos_preservados':130,'competencias_preservadas':20,'estados_de_cobertura':'históricos, preservados sem promoção','links_locais_conferidos':len(links),'links':links,'capitulos_e_derivados_preservados':preserved,'pdf_das_folhas_preservado':sha(R/meta['pdf']),'corpo_imprimivel_das_folhas_preservado':True,'pdf_integrado_preservado':True,'pendencias':[{'id':'Arata-CD','fonte':byid['s089']['fonte'],'constatacao':'CD 16 fora da coluna fixa publicada; não há criador indicado para justificar CD variável.','tratamento':'Aviso no índice; corrigir na consolidação textual da etapa 6, conservando condições e resultado do exemplo. Nenhum valor foi substituído neste lote.'}],'limites':['Conferência documental dos 130 pontos/20 competências; não é releitura semântica de todas as evidências.','Leitura dirigida de P14–P20 registrada em leitura-dirigida.json.','Sem teste interativo de navegador, teste humano ou validação geral de equilíbrio.']}
    write(A/'conferencias.json',result)
    assert (A/'conferencias.json').is_file()
    print(json.dumps({k:v for k,v in result.items() if k not in ['links','capitulos_e_derivados_preservados']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

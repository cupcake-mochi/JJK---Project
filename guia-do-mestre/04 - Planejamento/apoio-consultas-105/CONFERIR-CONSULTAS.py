"""Verificações de entrega; não comprovam aprendizagem ou equilíbrio."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,math,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent
R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def soup(p):return BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
def tokens(s):
    s=unicodedata.normalize('NFKC',s).lower();s=re.sub(r'(?<=\w)-\s*(?=\w)','',s)
    return re.findall(r'[^\W_]+',s)
def main():
    d=json.loads((A/'amostra.json').read_text());pdf=R/d['pdf'];assert sha(pdf)==d['pdf_sha256']
    targets=[A/'folhas-para-a-mesa.html',A/'casos-completos.html',A/'destinos-dos-casos.md',R/'04 - Planejamento/105-folhas-para-a-mesa-e-acesso-aos-casos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
    for f in d['fontes']+[d['guia_de_escolha']]:
        p=R/f['fonte'];assert sha(p)==f['sha256'];targets.append(p)
    docs={};links=[]
    for p in targets:
        doc=soup(p);ids=[n['id'] for n in doc.find_all(id=True)];assert len(ids)==len(set(ids)),p
        for node in doc.find_all('a',href=True):
            u=urlsplit(node['href'])
            if u.scheme:continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert target.is_file(),(p,node['href'])
            if u.fragment:
                if target not in docs:docs[target]=soup(target)
                assert docs[target].find(id=unquote(u.fragment)),(p,node['href'])
            links.append({'origem':str(p.relative_to(R)),'destino':node['href']})
    doc=soup(A/'folhas-para-a-mesa.html');expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','FOLHAS PARA A MESA','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    ns={'x':'http://www.w3.org/1999/xhtml'};root=ET.parse(A/'limites.html').getroot();pages=[];outside=[]
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        pages.append({'pagina':i,'palavras':len(words)})
    assert len(pages)==5==d['paginas'];assert not outside,outside
    old=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    prior=[p for p in old if p.startswith('06 - Redacao do Guia/revisao-98/') and p.endswith('.md') and not p.endswith('/LEIA-ME.md')]
    for rel in prior:assert sha(R/rel)==old[rel],rel
    bases=['04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf']
    for rel in bases:assert sha(R/rel)==old[rel],rel
    m=json.loads((A/'destinos-e-fontes.json').read_text());assert len(m['fontes'])==104
    for f in m['fontes']:assert sha(R/f['fonte'])==f['sha256'],f['fonte']
    c=json.loads((A/'conferencia-de-cobertura.json').read_text());assert len(c['pontos'])==130 and len(c['competencias'])==20
    assert len({x['id'] for x in c['pontos']})==130 and len({x['id'] for x in c['competencias']})==20
    conta={'maximo_referencia':44,'primeiro_insistir':math.ceil(44/3),'maior_classe':2,'teto':15*2,'exigencia':min(math.ceil(44/3),15*2),'tratamento_acumulado':0,'janela_inicial':3-0,'voltas_completas_apos_queda':0,'danos_posteriores':0,'janela_atual':3}
    result={'registro':105,'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'fontes_antigas_preservadas':len(m['fontes']),'fontes_novas_anteriores_preservadas':len(prior),'bases_preservadas':bases,'pontos_localizados':130,'competencias_localizadas':20,'socorro_do_exemplo':conta,'limite':'Conferência interna de arquivos, referência e renderização; não é nova leitura semântica das 130 aplicações nem passagem real entre mestres.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links','socorro_do_exemplo']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

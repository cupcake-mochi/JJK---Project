"""Confere presença de texto, remissões e preservação; não avalia aprendizagem."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent
R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tokens(s):
    s=unicodedata.normalize('NFKC',s).lower()
    s=re.sub(r'(?<=\w)-\s*(?=\w)','',s)
    return re.findall(r'[^\W_]+',s)
def ids(soup):
    allids=[x['id'] for x in soup.find_all(id=True)]; assert len(allids)==len(set(allids)),Counter(allids)
    return set(allids)
def main():
    d=json.loads((A/'amostra.json').read_text());pdf=R/d['pdf'];base=R/d['livro_de_regras']
    assert sha(pdf)==d['pdf_sha256'];assert sha(R/d['fonte'])==d['fonte_sha256'];assert sha(base)==d['livro_de_regras_sha256']
    docs={};links=[]
    targets=[A/'ideias-para-aventuras.html',A/'consulta-de-regras.html']
    sources=[R/d['fonte'],R/'04 - Planejamento/104-ideias-combinaveis-e-exemplos.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
    for p in targets+sources:
        soup=BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser');ids(soup)
        for a in soup.find_all('a',href=True):
            u=urlsplit(a['href'])
            if u.scheme:continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve(); assert target.is_file(),(p,a['href'])
            if u.fragment:
                if target not in docs:
                    text=target.read_text();docs[target]=BeautifulSoup(text if target.suffix=='.html' else markdown.markdown(text,extensions=['tables','toc']),'html.parser')
                assert docs[target].find(id=unquote(u.fragment)),(p,a['href'])
            links.append({'origem':str(p.relative_to(R)),'destino':a['href']})
    doc=BeautifulSoup((A/'ideias-para-aventuras.html').read_text(),'html.parser')
    expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','IDEIAS PARA AVENTURAS','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    ns={'x':'http://www.w3.org/1999/xhtml'};root=ET.parse(A/'conferencia-de-limites.html').getroot();pages=[];outside=[];nwords=0
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns);nwords+=len(words)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        body=[x for x in words if 50<float(x.attrib['yMin'])<790]
        pages.append({'pagina':i,'palavras':len(words),'fim_corpo':max(float(x.attrib['yMax']) for x in body)})
    assert len(pages)==5,len(pages);assert not outside,outside
    rule=BeautifulSoup((A/'consulta-de-regras.html').read_text(),'html.parser');lines=base.read_text().splitlines()
    for b in d['consultas']:
        raw='\n'.join(lines[b['inicio_linha']-1:b['fim_linha']])
        ref=BeautifulSoup(markdown.markdown(raw,extensions=['tables','sane_lists']),'html.parser').get_text(' ',strip=True)
        got=rule.find(id=b['id']).get_text(' ',strip=True)
        assert ref==got,b['titulo']
    old=json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']
    for f in old:assert sha(R/f['fonte'])==f['sha256'],f['fonte']
    cap1=json.loads((R/'04 - Planejamento/apoio-primeira-missao-100/amostra.json').read_text())
    assert sha(R/cap1['fonte'])==cap1['fonte_sha256']
    for f in json.loads((R/'04 - Planejamento/apoio-mundo-e-preparo-101/amostra.json').read_text())['fontes']:assert sha(R/f['caminho'])==f['sha256']
    anterior=json.loads((R/'04 - Planejamento/apoio-conducao-102/amostra.json').read_text())
    assert sha(R/anterior['fonte'])==anterior['fonte_sha256']
    assert sha(R/anterior['pdf'])==anterior['pdf_sha256']
    anterior5=json.loads((R/'04 - Planejamento/apoio-campanha-103/amostra.json').read_text())
    assert sha(R/anterior5['fonte'])==anterior5['fonte_sha256']
    assert sha(R/anterior5['pdf'])==anterior5['pdf_sha256']
    for tag in doc.find_all('img',src=True):
        assert (A/unquote(tag['src'])).resolve().is_file(),tag['src']
    mapa=A/'canal-das-hortas.svg'
    assert sha(mapa)==d['mapa_sha256']
    for f in json.loads((R/'04 - Planejamento/apoio-mundo-e-preparo-101/amostra.json').read_text())['fontes']:
        assert sha(R/f['caminho'])==f['sha256']
    original=R/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
    assert sha(original)=='0050d7cf2426ce3eba555ab2010deaeb6d62e023a5dba67ec43f0495e79cbd3b'
    result={'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_posicionadas':nwords,'palavras_fora_da_pagina':outside,'trechos_de_regras_fieis_a_base':len(d['consultas']),'fontes_antigas_preservadas':len(old),'capitulos_novos_anteriores_preservados':5,'pdf_integrado_preservado':True,'livro_de_regras_sha256':sha(base),'limite':'Presença textual e integridade não substituem revisão visual e leitura externa.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

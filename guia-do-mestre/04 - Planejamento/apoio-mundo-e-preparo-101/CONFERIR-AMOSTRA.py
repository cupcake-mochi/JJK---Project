"""Conferências documentais da prova; não substituem leitura ou revisão visual."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
import hashlib,json,re,subprocess,unicodedata
A=Path(__file__).resolve().parent
R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tokens(s):
    s=unicodedata.normalize('NFKC',s).lower()
    s=re.sub(r'(?<=\w)-\s*(?=\w)','',s)
    return re.findall(r'[^\W_]+',s)
def main():
    dados=json.loads((A/'amostra.json').read_text());pdf=R/dados['pdf']
    for f in dados['fontes']: assert sha(R/f['caminho'])==f['sha256']
    assert sha(pdf)==dados['pdf_sha256']
    doc=BeautifulSoup((A/'capitulos-2-e-3.html').read_text(),'html.parser')
    ids=[t['id'] for t in doc.find_all(id=True)]; assert len(ids)==len(set(ids))
    links=[]
    for tag in doc.find_all('a',href=True):
        u=urlsplit(tag['href']); assert not u.scheme,tag['href']
        p=(A/unquote(u.path)).resolve() if u.path else A/'capitulos-2-e-3.html'
        assert p.is_file(),p
        if u.fragment and p.suffix=='.html':
            target=BeautifulSoup(p.read_text(),'html.parser'); assert target.find(id=unquote(u.fragment)),tag['href']
        links.append(tag['href'])
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for x in ['CICLO MALDITO / GUIA DO MESTRE','MUNDO E PREPARO','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(x,'')
    esperado=Counter(tokens(doc.main.get_text(' '))); presente=Counter(tokens(plain)); faltantes=esperado-presente
    assert not faltantes,faltantes
    root=ET.parse(A/'conferencia-de-limites.html').getroot();ns={'x':'http://www.w3.org/1999/xhtml'}
    paginas=[];fora=[];nwords=0
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns);nwords+=len(words)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:fora.append({'pagina':i,'palavra':word.text})
        body=[word for word in words if 50<float(word.attrib['yMin'])<790]
        paginas.append({'pagina':i,'palavras':len(words),'topo_corpo':min(float(x.attrib['yMin']) for x in body),'fim_corpo':max(float(x.attrib['yMax']) for x in body)})
    assert not fora,fora
    assert len(paginas)==8,len(paginas)
    fonts=json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']
    assert len(fonts)==104
    for f in fonts: assert sha(R/f['fonte'])==f['sha256'],f['fonte']
    result={'pdf_sha256':sha(pdf),'paginas':paginas,'links_html_conferidos':len(links),'links':links,'palavras_html_conferidas_por_contagem':sum(esperado.values()),'palavras_ausentes_no_pdf':dict(faltantes),'palavras_posicionadas':nwords,'palavras_fora_da_pagina':fora,'fontes_antigas_preservadas':len(fonts),'limite':'Conferência de presença de texto, links e limites; revisão visual registrada separadamente.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

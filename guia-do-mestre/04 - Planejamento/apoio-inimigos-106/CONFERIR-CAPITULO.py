"""Conferências editoriais, de referências e de números herdados; sem rebalancear."""
from pathlib import Path
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,re,subprocess,unicodedata,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parent
R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def soup(p):return BeautifulSoup(p.read_text() if p.suffix=='.html' else markdown.markdown(p.read_text(),extensions=['tables','toc']),'html.parser')
def tokens(s):
    s=unicodedata.normalize('NFKC',s).lower();s=re.sub(r'(?<=\w)-\s*(?=\w)','',s)
    return re.findall(r'[^\W_]+',s)
def nums(s):return re.findall(r'[+-]?\d+(?:,\d+)?',s)
def rows(table):return [[c.get_text(' ',strip=True) for c in tr.find_all(['td','th'])] for tr in table.find_all('tr')][1:]
def main():
    d=json.loads((A/'amostra.json').read_text());f=R/d['fonte'];pdf=R/d['pdf'];base=R/d['livro_de_regras']
    assert sha(f)==d['fonte_sha256'] and sha(pdf)==d['pdf_sha256'] and sha(base)==d['livro_de_regras_sha256']
    docs={};links=[]
    targets=[A/'capitulo-6.html',A/'consulta-de-regras.html',f,R/'04 - Planejamento/106-inimigos-perigos-e-consultas.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
    for p in targets:
        doc=soup(p);ids=[x['id'] for x in doc.find_all(id=True)];assert len(ids)==len(set(ids)),p
        for a in doc.find_all('a',href=True):
            u=urlsplit(a['href'])
            if u.scheme:continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve();assert target.is_file(),(p,a['href'])
            if u.fragment:
                if target not in docs:docs[target]=soup(target)
                assert docs[target].find(id=unquote(u.fragment)),(p,a['href'])
            links.append({'origem':str(p.relative_to(R)),'destino':a['href']})
    doc=soup(A/'capitulo-6.html');expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','INIMIGOS E PERIGOS','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    root=ET.parse(A/'limites.html').getroot();ns={'x':'http://www.w3.org/1999/xhtml'};pages=[];outside=[]
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        pages.append({'pagina':i,'palavras':len(words)})
    assert len(pages)==d['paginas']==7 and not outside,(len(pages),outside)
    ref=soup(R/'06 - Redacao do Guia/74-regua-inicial-de-inimigos.md');new=soup(f)
    oldvalues=next(t for t in ref.find_all('table') if t.th.get_text()=='Campo de rascunho')
    newvalues=next(t for t in new.find_all('table') if [h.get_text() for h in t.find_all('th')]==['Campo','Nível 2','Nível 6'])
    comparacoes=[]
    for before,after in zip(rows(oldvalues)[:6],rows(newvalues)):
        assert [nums(x) for x in before[1:]]==[nums(x) for x in after[1:]],(before,after)
        comparacoes.append({'fonte':before,'capitulo':after})
    olddamage=next(t for t in ref.find_all('table') if t.th.get_text()=='Aplicação')
    newdamage=next(t for t in new.find_all('table') if t.th.get_text()=='Golpe')
    assert len(rows(olddamage))==len(rows(newdamage))==3
    for before,after in zip(rows(olddamage),rows(newdamage)):
        assert nums(' '.join(before[1:3]))==nums(' '.join(after[1:])),(before,after)
        comparacoes.append({'fonte':before[:3],'capitulo':after})
    rule=soup(A/'consulta-de-regras.html');lines=base.read_text().splitlines()
    for b in d['consultas']:
        raw='\n'.join(lines[b['inicio_linha']-1:b['fim_linha']]);expectedrule=BeautifulSoup(markdown.markdown(raw,extensions=['tables','sane_lists']),'html.parser').get_text(' ',strip=True)
        assert expectedrule==rule.find(id=b['id']).get_text(' ',strip=True),b['titulo']
    m=json.loads((R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text());related=[]
    for old in m['fontes']:
        assert sha(R/old['fonte'])==old['sha256'],old['fonte']
        if any(x.startswith('N06') for x in [old['destino_principal']]+old['usos_complementares']):related.append({k:old[k] for k in ['id','fonte','sha256','destino_principal','usos_complementares']})
    prior=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    prev=[p for p in prior if p.startswith('06 - Redacao do Guia/revisao-98/') and p.endswith('.md') and not p.endswith('/LEIA-ME.md')]
    for rel in prev:assert sha(R/rel)==prior[rel],rel
    original='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/original)==prior[original]
    result={'registro':106,'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'trechos_de_regras_fieis_a_base':len(d['consultas']),'linhas_numericas_preservadas':comparacoes,'fontes_antigas_preservadas':len(m['fontes']),'fontes_novas_anteriores_preservadas':len(prev),'fontes_relacionadas_ao_capitulo':related,'pdf_integrado_preservado':True,'limite':'Conferência de texto, contas herdadas e arquivos; não é nova simulação integral, teste de aprendizagem ou validação de equilíbrio.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links','linhas_numericas_preservadas','fontes_relacionadas_ao_capitulo']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

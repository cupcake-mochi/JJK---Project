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
    targets=[A/'capitulo-10.html',A/'consulta-de-regras.html',f,R/'04 - Planejamento/110-guilda-registros-e-passagem.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
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
    doc=soup(A/'capitulo-10.html');expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','JOGAR EM GUILDA','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    root=ET.parse(A/'limites.html').getroot();ns={'x':'http://www.w3.org/1999/xhtml'};pages=[];outside=[]
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        pages.append({'pagina':i,'palavras':len(words)})
    assert len(pages)==d['paginas']==4 and not outside,(len(pages),outside)
    import math
    body=soup(f).get_text(' ',strip=True)
    cases=[
      ('Tratamento de Insistir','exige 15 de tratamento',math.ceil(44/3),15),
      ('Teto por Classe','abaixo do teto de 30',15*2,30),
      ('Janela inicial','três rodadas de janela',3-0,3),
      ('TR de Mei 2','9 + 3 = 12',9+3,12),
      ('Cura válida','2 + 3 + 4 + 6 = 15',sum([2,3,4,6]),15),
      ('PE de Akira','Akira fica com 24 PE',30-6,24),
      ('TR de Mei 3','12 + 3 = 15',12+3,15),
      ('Prazo do perigo','fase da rodada 11',1+10,11)
    ]
    comparacoes=[]
    for name,excerpt,computed,want in cases:
        assert excerpt in body,(name,excerpt)
        assert computed==want,(name,computed,want)
        comparacoes.append({'caso':name,'trecho':excerpt,'resultado':computed,'esperado':want})
    for excerpt in ['28 horas novas por ficha a cada sete dias','O XP semanal é contado por jogador','Nenhum descanso foi concluído','não é subtraído da cura','Isso não remove Envenenado','As Reações não foram gastas','nenhum desses eventos aconteceu durante a troca de mestre','Este exemplo não traz o tamanho anunciado','Uma sugestão não é tarefa assumida']:
        assert excerpt.lower() in body.lower(),excerpt
    assert 'R53' not in body
    assert '4 × Essência' not in body and '2 × Essência' not in body
    rule=soup(A/'consulta-de-regras.html');lines=base.read_text().splitlines()
    for b in d['consultas']:
        raw='\n'.join(lines[b['inicio_linha']-1:b['fim_linha']]);expectedrule=BeautifulSoup(markdown.markdown(raw,extensions=['tables','sane_lists']),'html.parser').get_text(' ',strip=True)
        assert expectedrule==rule.find(id=b['id']).get_text(' ',strip=True),b['titulo']
    new=soup(f);old=soup(R/'06 - Redacao do Guia/81-passar-a-missao-entre-mestres.md')
    def table_by(doc,headers):return next(x for x in doc.find_all('table') if [h.get_text(' ',strip=True) for h in x.find_all('th')]==headers)
    oldinitial=rows(table_by(old,['Campo','Mei','Akira']))
    newinitial=dict(rows(table_by(new,['O que continua','Estado na pausa'])))
    oldfinal=dict(rows(table_by(old,['Personagem','Estado para a continuidade'])))
    newfinal=dict(rows(table_by(new,['Ao fim do percurso','O que registrar'])))
    states=[]
    labels=['Vida atual/máxima','Energia atual/máxima','Integridade atual/máxima']
    for col,name in [(1,'Mei'),(2,'Akira')]:
        initial=[re.findall(r'\d+/\d+',next(row for row in oldinitial if row[0]==label)[col])[0] for label in labels]
        current=re.findall(r'\d+/\d+',newinitial[name]);assert initial==current,(name,initial,current)
        finalold=re.findall(r'\d+/\d+',oldfinal[name]);finalnew=re.findall(r'\d+/\d+',newfinal[name]);assert finalold==finalnew,(name,finalold,finalnew)
        posold=re.search(r'\b[AB]\d+\b',oldfinal[name]).group();posnew=re.search(r'\b[AB]\d+\b',newfinal[name]).group();assert posold==posnew
        states.append({'personagem':name,'reservas_antes':current,'reservas_depois':finalnew,'posicao_final':posnew,'comparada_com':'fonte 81'})
    m=json.loads((R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text());related=[]
    for old in m['fontes']:
        assert sha(R/old['fonte'])==old['sha256'],old['fonte']
        if any(x.startswith('N10') for x in [old['destino_principal']]+old['usos_complementares']):related.append({k:old[k] for k in ['id','fonte','sha256','destino_principal','usos_complementares']})
    prior=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    prev=[p for p in prior if p.startswith('06 - Redacao do Guia/revisao-98/') and p.endswith('.md') and not p.endswith('/LEIA-ME.md')]
    for rel in prev:assert sha(R/rel)==prior[rel],rel
    original='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/original)==prior[original]
    result={'registro':110,'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'trechos_de_regras_fieis_a_base':len(d['consultas']),'contas_e_parametros_conferidos':comparacoes,'estados_comparados':states,'fontes_antigas_preservadas':len(m['fontes']),'fontes_novas_anteriores_preservadas':len(prev),'fontes_relacionadas_ao_capitulo':related,'pdf_integrado_preservado':True,'limite':'Conferência de texto, contas herdadas e arquivos; não é nova simulação integral, teste de aprendizagem ou validação de equilíbrio.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links','contas_e_parametros_conferidos','fontes_relacionadas_ao_capitulo']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

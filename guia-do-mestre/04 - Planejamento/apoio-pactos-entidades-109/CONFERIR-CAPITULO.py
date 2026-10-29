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
    targets=[A/'capitulo-9.html',A/'consulta-de-regras.html',f,R/'04 - Planejamento/109-pactos-projetos-e-continuidade.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
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
    doc=soup(A/'capitulo-9.html');expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','PACTOS E ENTIDADES','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    root=ET.parse(A/'limites.html').getroot();ns={'x':'http://www.w3.org/1999/xhtml'};pages=[];outside=[]
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        pages.append({'pagina':i,'palavras':len(words)})
    assert len(pages)==d['paginas']==6 and not outside,(len(pages),outside)
    import math
    body=soup(f).get_text(' ',strip=True)
    cases=[
      ('Vagas','Essência 5 permite duas vagas',5//2,2),
      ('Overtime: percentual','Oito horas correspondem a 20%',8*2.5,20),
      ('Overtime: jornada','máximo durante a jornada é 32',math.floor(40*.8),32),
      ('Overtime: hora extra','na hora extra, 48',math.floor(40*1.2),48),
      ('Overtime: diferença e saldo','saldo 12 passa a 28',12+48-32,28),
      ('Liberação: teto','face 2 dá teto 10',math.floor(40*.25),10),
      ('Liberação: restante','Pagar 9 deixa apenas 1',10-9,1),
      ('Doma: excedente sem destruição','excedente 22',30-8,22),
      ('Doma: metade do máximo','abaixo da metade do máximo',52/2,26),
      ('Doma: excedente com destruição','excedente 27',35-8,27),
      ('Criação: CD','8 + 4 + 2 − 2 = CD 12',8+4+2-2,12),
      ('Criação: rolagem falha','tira 5 e alcança 11',5+4+2,11),
      ('Criação: rolagem autorizada','chega a 14: sucesso',max(2,8)+4+2,14),
      ('Retomada: uma falha','Foram 48 horas',32+math.ceil(32*.5),48),
      ('Retomada: duas falhas','64 após duas',32+2*math.ceil(32*.5),64),
      ('Materiais do exemplo','¥36.000',24000+2*6000,36000),
      ('Reconstrução: trabalho','referência é 24 horas',48/2,24),
      ('Reconstrução: retomada','com 12 por falha',math.ceil(24*.5),12),
      ('Passagens: 1 a 4','8 + 16 + 24 = 48 horas',8+16+24,48),
      ('Passagens: falha na segunda','dá 56 horas de reconstrução',8+16+8+24,56),
      ('Transferência: Classe 3','referência de Classe 3 é 4 horas',max(2,math.ceil(32/8)),4),
      ('Transferência: Classe 5','Classe 5 pede 9',max(2,math.ceil(72/8)),9),
      ('Transferência: retomada Classe 5','sua retomada é 5',max(1,math.ceil(9*.5)),5)
    ]
    comparacoes=[]
    for name,excerpt,computed,want in cases:
        assert excerpt in body,(name,excerpt)
        assert computed==want,(name,computed,want)
        comparacoes.append({'caso':name,'trecho':excerpt,'resultado':computed,'esperado':want})
    for excerpt in ['0/25/50/75/100/100%','30 dias da ficção','por três dias','18 m','posição atual conhecida','não exige decisão intermediária','todos os PE comuns e temporários','os PE continuam zerados até uma recuperação válida','sem a redução de reconstrução','sem carga','0,5 Volume','um teste por Classe','Inconsciência não é morte']:
        assert excerpt.lower() in body.lower(),excerpt
    assert 'R53' not in body
    assert '4 × Essência' not in body and '2 × Essência' not in body
    rule=soup(A/'consulta-de-regras.html');lines=base.read_text().splitlines()
    for b in d['consultas']:
        raw='\n'.join(lines[b['inicio_linha']-1:b['fim_linha']]);expectedrule=BeautifulSoup(markdown.markdown(raw,extensions=['tables','sane_lists']),'html.parser').get_text(' ',strip=True)
        assert expectedrule==rule.find(id=b['id']).get_text(' ',strip=True),b['titulo']
    new=soup(f)
    def table_by(doc,headers):return next(x for x in doc.find_all('table') if [h.get_text(' ',strip=True) for h in x.find_all('th')]==headers)
    def integer(s):return int(re.search(r'[−-]?\d+',s).group().replace('−','-'))
    times=rows(table_by(new,['Classe','Criar','Reconstruir','Transferir']))
    create=soup(R/'06 - Redacao do Guia/45-tempo-materiais-e-retomada-de-entidades.md')
    change=soup(R/'06 - Redacao do Guia/46-reconstruir-transferir-e-herdar-entidades.md')
    oldcreate=rows(table_by(create,['Classe da entidade','Dedicação de quem cria']))
    oldrebuild=rows(table_by(change,['Passagem','Trabalho de reconstrução','Retomada após cada falha']))
    oldtransfer=rows(table_by(change,['Classe da entidade','Trabalho de transferência','Retomada após cada falha']))
    assert len(times)==len(oldcreate)==len(oldtransfer)==7 and len(oldrebuild)==6
    tablecomparisons=[]
    for i,row in enumerate(times):
        assert integer(row[0])==i+1
        assert integer(row[1])==integer(oldcreate[i][1])
        assert row[2]=='-' if i==0 else integer(row[2])==integer(oldrebuild[i-1][1])
        assert integer(row[3])==integer(oldtransfer[i][1])
        tablecomparisons.append({'classe':i+1,'criar':row[1],'reconstruir':row[2],'transferir':row[3]})
    matrix=rows(table_by(new,['Relação de Classes','Criar ou transferir','Reconstruir']))
    rulecreation=rule.find(id=next(b['id'] for b in d['consultas'] if b['titulo']=='Criação de entidades'))
    first=rows(rulecreation.find('table'))
    refrebuild=rows(table_by(change,['Nova Classe em relação ao responsável','Ajuste à base da CD']))
    assert len(matrix)==len(first)==len(refrebuild)==3
    for row,before,rb in zip(matrix,first,refrebuild):
        assert integer(row[1])==integer(before[-1]) and integer(row[2])==integer(rb[-1])
    m=json.loads((R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text());related=[]
    for old in m['fontes']:
        assert sha(R/old['fonte'])==old['sha256'],old['fonte']
        if any(x.startswith('N09') for x in [old['destino_principal']]+old['usos_complementares']):related.append({k:old[k] for k in ['id','fonte','sha256','destino_principal','usos_complementares']})
    prior=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    prev=[p for p in prior if p.startswith('06 - Redacao do Guia/revisao-98/') and p.endswith('.md') and not p.endswith('/LEIA-ME.md')]
    for rel in prev:assert sha(R/rel)==prior[rel],rel
    original='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/original)==prior[original]
    result={'registro':109,'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'trechos_de_regras_fieis_a_base':len(d['consultas']),'contas_e_parametros_conferidos':comparacoes,'tempos_comparados':tablecomparisons,'matriz_de_cd_preservada':True,'fontes_antigas_preservadas':len(m['fontes']),'fontes_novas_anteriores_preservadas':len(prev),'fontes_relacionadas_ao_capitulo':related,'pdf_integrado_preservado':True,'limite':'Conferência de texto, contas herdadas e arquivos; não é nova simulação integral, teste de aprendizagem ou validação de equilíbrio.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links','contas_e_parametros_conferidos','fontes_relacionadas_ao_capitulo']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

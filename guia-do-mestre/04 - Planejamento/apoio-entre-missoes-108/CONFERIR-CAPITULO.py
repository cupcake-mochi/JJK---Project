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
    targets=[A/'capitulo-8.html',A/'consulta-de-regras.html',f,R/'04 - Planejamento/108-rotina-trabalho-e-recompensas.md',R/'06 - Redacao do Guia/revisao-98/LEIA-ME.md']
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
    doc=soup(A/'capitulo-8.html');expected=Counter(tokens(doc.main.get_text(' ')))
    plain=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
    for h in ['CICLO MALDITO / GUIA DO MESTRE','ENTRE MISSÕES','PRÉ-1.0 · AMOSTRA DE LEITURA']:plain=plain.replace(h,'')
    missing=expected-Counter(tokens(plain));assert not missing,missing
    root=ET.parse(A/'limites.html').getroot();ns={'x':'http://www.w3.org/1999/xhtml'};pages=[];outside=[]
    for i,page in enumerate(root.findall('.//x:page',ns),1):
        w=float(page.attrib['width']);h=float(page.attrib['height']);words=page.findall('x:word',ns)
        for word in words:
            x0,y0,x1,y1=[float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            if x0<0 or y0<0 or x1>w or y1>h:outside.append([i,word.text])
        pages.append({'pagina':i,'palavras':len(words)})
    assert len(pages)==d['paginas']==7 and not outside,(len(pages),outside)
    import math
    body=soup(f).get_text(' ',strip=True)
    cases=[
      ('Curto: recuperação e saldo','recupera 2 e fica com 3',1+math.floor(10*.25),3),
      ('Longo: metade mínima','saldo 3 passa a 11',max(3,23//2),11),
      ('Longo: saldo acima da metade','saldo 18 continua 18',max(18,23//2),18),
      ('Entrada proporcional','3 × 4 = 12 horas',3*4,12),
      ('Ciclo de sete dias','28 horas novas por ficha',7*4,28),
      ('Limite na abertura','no máximo 56 horas',28+28,56),
      ('Rina: saldo novo','Restam 18 novas',28-(20-10),18),
      ('Rina: saldo que expira','6 antigas restantes expirariam',18-12,6),
      ('Mei: horas distintas','10 horas confirmadas, 8 reservadas e 10 livres',10+8+10,28),
      ('Mei: abertura seguinte','abre com 38 disponíveis',28+10,38),
      ('Ciclo de quinze dias','15 dão 60',15*4,60),
      ('Abertura de quinze dias','chegar a 120 horas',2*15*4,120),
      ('Arrombamento mecânico','dá +5',4+1,5),
      ('Arrombamento eletrônico','dar +3',2+1,3),
      ('Dados para CD 14','precisa de 9 ou 11',[14-5,14-3],[9,11]),
      ('Traje: dedicação','faltam duas horas',4-2,2),
      ('Compra: saldo','deixa ¥12.000',150000-90000-48000,12000),
      ('Reposição: custo','custam ¥8.000',4500+3000+500,8000),
      ('Anel: custo com retomada','falha custa ¥38.000',4000+6000+2000+18000+8000,38000),
      ('Anel: dedicação pessoal','de 28, restam 22',28-6,22),
      ('Venda: diferença','¥14.000 a menos',38000-24000,14000),
      ('Venda: saldo financeiro','passa a ¥26.000',2000+24000,26000),
      ('Instrução: dedicação','22 horas disponíveis passam a 20',22-2,20),
      ('Pastilha: duração restante','uma hora e meia',(17*60)-(15*60+30),90),
      ('XP: quinta longa','200 × 1/8',math.floor(200/8),25),
      ('XP: quinta padrão','100 × 1/8 = 12,5',math.floor(100/8),12),
      ('XP: terceira longa, falha com metade','200 × 1/2 × 1/2',math.floor(200*.5*.5),50),
      ('Nível 2: saldo','conserva 50 XP',150+100-200,50),
      ('Limiar: saldo','guarda 1.000',4000-1500-1500,1000),
      ('Salário: duas participações','75% de ¥300.000 = ¥225.000',300000*.75,225000)
    ]
    comparacoes=[]
    for name,excerpt,computed,want in cases:
        assert excerpt in body,(name,excerpt)
        assert computed==want,(name,computed,want)
        comparacoes.append({'caso':name,'trecho':excerpt,'resultado':computed,'esperado':want})
    for excerpt in ['por jogador, dentro da campanha','uma posição semanal de XP','duas participações','não aumenta a dedicação','resultado pendente ainda não pode ser usado','sem receber de novo as horas dos dias já cobertos','não equivale automaticamente a descanso longo','retrabalho e a vantagem próprios da criação de entidades não se tornam regras gerais de fabricação']:
        assert excerpt.lower() in body.lower(),excerpt
    assert 'R53' not in body
    assert '4 × Essência' not in body and '2 × Essência' not in body
    rule=soup(A/'consulta-de-regras.html');lines=base.read_text().splitlines()
    for b in d['consultas']:
        raw='\n'.join(lines[b['inicio_linha']-1:b['fim_linha']]);expectedrule=BeautifulSoup(markdown.markdown(raw,extensions=['tables','sane_lists']),'html.parser').get_text(' ',strip=True)
        assert expectedrule==rule.find(id=b['id']).get_text(' ',strip=True),b['titulo']
    new=soup(f);tables=[]
    def table_by(doc,headers):return next(x for x in doc.find_all('table') if [h.get_text(' ',strip=True) for h in x.find_all('th')]==headers)
    dedication=table_by(new,['Fechamento','Abertura seguinte']);ref=soup(R/'06 - Redacao do Guia/39-atividades-e-tempo-entre-missoes.md')
    olddedication=next(x for x in ref.find_all('table') if x.th.get_text().startswith('Fechamento'))
    assert len(rows(dedication))==len(rows(olddedication))==3
    for before,after in zip(rows(olddedication),rows(dedication)):
        assert nums(before[-1])==nums(after[-1]),(before,after)
    tables.append('Três aberturas de dedicação: valores preservados da fonte 39')
    def rule_section(title):return rule.find(id=next(b['id'] for b in d['consultas'] if b['titulo']==title))
    reward=table_by(new,['Missão anunciada','XP base']);ref=rule_section('Recompensas e custos').find('table')
    assert rows(reward)==[x[:2] for x in rows(ref)]
    tables.append('Quatro recompensas base iguais à regra publicada')
    salary=table_by(new,['Grau','Salário mensal de referência']);ref=rule_section('Recompensas da guilda').find('table')
    assert len(rows(salary))==len(rows(ref))==5
    for before,after in zip(rows(ref),rows(salary)):
        assert before[0]==after[0] and nums(before[1])==nums(after[1]),(before,after)
    tables.append('Cinco referências de salário iguais à regra publicada')
    grade=table_by(new,['Grau','Nível mínimo do efeito'])
    assert rows(grade)==[['4','Nenhum; não possui efeito especial'],['3','Nenhum'],['2','7'],['1 ou especial','13']]
    ref=rows(rule_section('Graus das ferramentas').find('table'));assert [r[-1] for r in ref]==['Nenhum','Nenhum','7','13','13']
    tables.append('Níveis de efeitos iguais à regra; graus 1 e especial reunidos sem alterar o mínimo')
    m=json.loads((R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text());related=[]
    for old in m['fontes']:
        assert sha(R/old['fonte'])==old['sha256'],old['fonte']
        if any(x.startswith('N08') for x in [old['destino_principal']]+old['usos_complementares']):related.append({k:old[k] for k in ['id','fonte','sha256','destino_principal','usos_complementares']})
    prior=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    prev=[p for p in prior if p.startswith('06 - Redacao do Guia/revisao-98/') and p.endswith('.md') and not p.endswith('/LEIA-ME.md')]
    for rel in prev:assert sha(R/rel)==prior[rel],rel
    original='08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf';assert sha(R/original)==prior[original]
    result={'registro':108,'pdf_sha256':sha(pdf),'paginas':pages,'links_locais_conferidos':len(links),'links':links,'palavras_html_conferidas':sum(expected.values()),'palavras_ausentes_no_pdf':dict(missing),'palavras_fora_da_pagina':outside,'trechos_de_regras_fieis_a_base':len(d['consultas']),'contas_e_parametros_conferidos':comparacoes,'tabelas_comparadas':tables,'fontes_antigas_preservadas':len(m['fontes']),'fontes_novas_anteriores_preservadas':len(prev),'fontes_relacionadas_ao_capitulo':related,'pdf_integrado_preservado':True,'limite':'Conferência de texto, contas herdadas e arquivos; não é nova simulação integral, teste de aprendizagem ou validação de equilíbrio.'}
    (A/'conferencias.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paginas','links','contas_e_parametros_conferidos','fontes_relacionadas_ao_capitulo']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

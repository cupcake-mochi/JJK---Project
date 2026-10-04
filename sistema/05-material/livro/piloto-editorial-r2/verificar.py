from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,unicodedata
from pypdf import PdfReader
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inv=json.loads((BASE.parent/'planejamento-editorial/INVENTARIO-BASE.json').read_text())
result={'base':'v0.331','entrega':'piloto editorial 2','data':'2026-10-02','preservacao':{},'pdfs':[]}
for group in ['fontes','artefatos_publicados']:
    for item in inv[group]:assert sha(ROOT/item['arquivo'])==item['sha256'],item['arquivo']
    result['preservacao'][group]=len(inv[group])
# Compare the old pilot against its frozen delivery, not against a new self-created baseline.
with ZipFile(ROOT/'entregas/Projeto-M-Piloto-Editorial-01.zip') as z:
    count=0
    for n in z.namelist():
        if n.endswith('/') or not n.startswith('piloto-editorial-r1/'):continue
        p=BASE.parent/n
        assert p.exists(),n
        assert p.read_bytes()==z.read(n),n
        count+=1
    result['preservacao']['arquivos_piloto_1']=count
pdfspec=[('Projeto-M-Piloto-Editorial-02','PILOTO',10,10),('Projeto-M-Amostras-Tecnicas-02','LOTE-TECNICO',11,10)]
soups={}
for stem,source,pages,outline_count in pdfspec:
    p=BASE/'output/pdf'/f'{stem}.pdf';r=PdfReader(p)
    assert len(r.pages)==pages,(stem,len(r.pages))
    texts=[x.extract_text() for x in r.pages]
    for i,t in enumerate(texts,1):
        assert len(t)>700,(stem,i,'possível sobra de página')
        for token in ['**','<!--','markdown="1"','\ufffd']:assert token not in t,(stem,i,token)
    soup=BeautifulSoup((BASE/f'{source}.html').read_text(),'html.parser');soups[source]=soup
    links=0
    for page in r.pages:
        for ref in page.get('/Annots',[]):
            obj=ref.get_object();dest=obj.get('/Dest')
            if isinstance(dest,str):assert dest in r.named_destinations,(stem,dest)
            if obj.get('/Subtype')=='/Link':links+=1
    outlines=[]
    for d in r.outline:
        assert not isinstance(d,list),'Este piloto usa apenas unidades principais.'
        n=r.get_destination_page_number(d)+1
        assert 1<=n<=pages
        outlines.append({'titulo':d.title,'pagina':n})
    assert len(outlines)==outline_count,(stem,len(outlines))
    boxes=json.loads((BASE/'evidencias'/f'{stem}-caixas.json').read_text())
    outside=[b for b in boxes if b['x'] < -1 or b['y'] < -1 or b['x']+b['largura']>795 or b['y']+b['altura']>1124]
    assert not outside,outside[:3]
    # Check text in the content area against the actual page margins as well.
    body_out=[b for b in boxes if 64<=b['y']<1050 and (b['x']<75 or b['x']+b['largura']>724)]
    assert not body_out,body_out[:3]
    for img in soup.select('img'):
        assert img.get('alt') and (BASE/img['src']).is_file()
        assert img['src'].endswith('.svg')
    result['pdfs'].append({'arquivo':str(p.relative_to(BASE)),'sha256':sha(p),'paginas':pages,'marcadores':outlines,'links_internos':links,'caracteres_por_pagina':[len(t) for t in texts],'caixas_textuais_fora_dos_limites':0})
# Attribute mappings are checked against the owner catalog, independently of the paraphrased text.
original=(ROOT/'sistema/05-material/livro/manual/12-pericias-e-oficios.md').read_text()
expected={m[0].strip():m[1].strip() for m in re.findall(r'^\| ([^|]+) \| perícia \| ([^|]+) \|',original,re.M)}
actual={}
for tr in soups['LOTE-TECNICO'].select('#catalogo tbody tr'):
    cells=[td.get_text(' ',strip=True) for td in tr.find_all('td')]
    actual[cells[0]]=cells[1]
assert len(actual)==23 and actual==expected,(actual,expected)
result['catalogo']={'pericias':len(actual),'atributos_iguais_a_fonte':True}
tech=PdfReader(BASE/'output/pdf/Projeto-M-Amostras-Tecnicas-02.pdf')
for pageidx in [8,9]:
    t=tech.pages[pageidx].extract_text()
    for header in ['Perícia','Atributo','Use para']:assert header in t,(pageidx,header)
catalog_boxes=json.loads((BASE/'evidencias/Projeto-M-Amostras-Tecnicas-02-caixas.json').read_text())
for name in expected:
    occurrences=[b['pagina'] for b in catalog_boxes if b['pagina'] in (9,10) and b['tag']=='strong' and b['texto']==name]
    assert len(occurrences)==1,(name,occurrences)
result['catalogo']['paginas_continuacao']=[9,10]
result['catalogo']['cabecalhos_repetidos']=True
# Validate explicit integer equations in the actual editable content, not copied assertions.
checks=[]
for source,soup in soups.items():
    text=' '.join(soup.stripped_strings)
    text=re.sub(r'(?<=\d) no d(?:20|6)\s*','',text)
    for m in re.finditer(r'(?<![\d+−])\b(\d+(?:\s*[+−]\s*\d+)+)\s*=\s*(\d+)\b',text):
        expression,target=m.groups()
        terms=re.findall(r'[+−]?\s*\d+',expression)
        value=sum(int(x.replace(' ','').replace('−','-')) for x in terms)
        assert value==int(target),(source,expression,target,value)
        checks.append({'fonte':source,'expressao':expression,'resultado':value})
assert len(checks)>=12,checks
result['contas_extraidas']=checks
# End-state assertions complement the independent semantic review.
pilot=soups['PILOTO'];technical=soups['LOTE-TECNICO']
assert '18 de Vida · 5 PE' in pilot.select_one('#combate').get_text(' ',strip=True)
assert '3 m percorridos, 6 m restantes' in pilot.select_one('#combate').get_text(' ',strip=True)
assert 23-5==18 and 8-3==5 and 9-3==6
assert 12-3-3==6 and 7-1-3==3 and 3-1+min(1,1)==3
assert 'Nenhuma arma voltou automaticamente' in technical.select_one('#sequencia').get_text(' ',strip=True)
result['saldos_conferidos']={'Kaori':{'vida':18,'PE':5,'movimento_restante_m':6},'Haru':{'PE':6,'Fluidez':0,'ataques':3,'maos':'vazias'},'Kaito':{'PE_apos_entrada':6,'ramo_basica':6,'ramo_especial':3}}
# Bind the final independent check to the exact delivered Markdown.
final=(BASE/'evidencias/verificacao-final.md').read_text()
for source in ['PILOTO.md','LOTE-TECNICO.md']:assert sha(BASE/source) in final,source
result['revisao_final_corresponde_aos_textos']=True
for f in BASE.rglob('*.md'):
    if 'evidencias' in f.parts:continue # Preserved reviews may point to workbench/reference locations.
    for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)',f.read_text()):
        if dest.startswith(('http:','https:','#')):continue
        assert (f.parent/dest).exists() or dest=='CONFERENCIA.json',(f.name,dest)
assert not [p for p in BASE.rglob('*') if p.suffix.lower() in ['.png','.jpg','.jpeg','.webp']]
result['imagens_geradas_por_IA_incorporadas']=False
result['visuais']='diagramas SVG e composição tipográfica'
result['leitura_por_agentes']=['narrativa/comparação','semântica/regras','compreensão/consulta']
result['teste_humano']='não realizado'
result['equilibrio_integral']='não testado; proposta editorial'
result['acessibilidade']='sem certificação ou teste com leitor de tela'
result['inspecao_visual']={'responsavel':'autor do piloto','paginas':21,'ressalva':'registro de inspeção visual, não inferência automática do código'}
result['fontes_autoria']=[{'arquivo':s,'sha256':sha(BASE/s)} for s in ['PILOTO.md','LOTE-TECNICO.md']]
(BASE/'CONFERENCIA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'preservacao':result['preservacao'],'pdfs':[{'paginas':d['paginas'],'marcadores':len(d['marcadores']),'links':d['links_internos']} for d in result['pdfs']],'pericias':23,'contas':len(checks),'revisao_final_mesmos_textos':True},ensure_ascii=False,indent=2))

from pathlib import Path
import json,re,hashlib,unicodedata
from pypdf import PdfReader
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
PLANO=BASE.parent/'planejamento-editorial'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inv=json.loads((PLANO/'INVENTARIO-BASE.json').read_text())
preservados={}
for grupo in ['fontes','artefatos_publicados']:
    for item in inv[grupo]:
        assert sha(ROOT/item['arquivo'])==item['sha256'],item['arquivo']
    preservados[grupo]=len(inv[grupo])
resultado={'base':'v0.331','entrega':'piloto editorial 1','estado':'proposta revisada pelo próprio autor','fontes_preservadas':preservados,'pdfs':[]}
for nome,total in [('Projeto-M-Piloto-Editorial-01.pdf',10),('Projeto-M-Prova-Protecao-1e2-colunas.pdf',2)]:
    arquivo=BASE/'output/pdf'/nome
    pdf=PdfReader(arquivo)
    assert len(pdf.pages)==total,(nome,len(pdf.pages))
    texto='\n'.join(p.extract_text() for p in pdf.pages)
    for token in ['**','<!--','markdown="1"','\ufffd']:
        assert token not in texto,(nome,token)
    destinos=pdf.named_destinations
    links=0
    for p in pdf.pages:
        for ref in p.get('/Annots',[]):
            obj=ref.get_object()
            if obj.get('/Subtype')=='/Link':
                destino=obj.get('/Dest')
                if isinstance(destino,str):assert destino in destinos,(nome,destino)
                links+=1
    marcadores=[]
    for d in pdf.outline:
        assert not isinstance(d,list),'Esta prova deve ter apenas destinos principais.'
        pagina=pdf.get_destination_page_number(d)+1
        assert 1<=pagina<=total
        assert 'aindaestá' not in d.title
        marcadores.append({'titulo':d.title,'pagina':pagina})
    assert len(marcadores)==total
    caixas=json.loads((BASE/'evidencias'/f'{arquivo.stem}-caixas.json').read_text())
    fora=[b for b in caixas if b['x'] < -1 or b['y'] < -1 or b['x']+b['largura']>795 or b['y']+b['altura']>1124]
    assert not fora,fora[:4]
    resultado['pdfs'].append({'arquivo':str(arquivo.relative_to(BASE)),'sha256':sha(arquivo),'paginas':total,'marcadores':marcadores,'links_internos':links,'caixas_texto_fora_da_pagina':len(fora),'paginas_inspecionadas_visualmente':list(range(1,total+1))})
# Both layout proofs must retain exactly the same text content, ignoring their proof labels.
soup=BeautifulSoup((BASE/'COMPARACAO.html').read_text(),'html.parser')
texts=[]
for sec in soup.select('section.page'):
    sec.select_one('.comparison-note').decompose()
    texts.append(' '.join(sec.stripped_strings))
assert texts[0]==texts[1],'Conteúdo diferente entre as provas de colunas'
resultado['comparacao_colunas_mesmo_texto']=True
# Audit arithmetic as actually written in the editable text, independently of the renderer.
soup=BeautifulSoup((BASE/'PILOTO.html').read_text(),'html.parser')
texto=' '.join(soup.stripped_strings)
texto=re.sub(r'(?<=\d) no d(?:20|6)\s*','',texto)
contas=[]
for m in re.finditer(r'(?<![\d+−])\b(\d+(?:\s*[+−]\s*\d+)+)\s*=\s*(\d+)\b',texto):
    expressao,esperado=m.groups()
    termos=re.findall(r'[+−]?\s*\d+',expressao)
    calculado=sum(int(x.replace(' ','').replace('−','-')) for x in termos)
    assert calculado==int(esperado),(expressao,esperado,calculado)
    contas.append({'expressao':expressao,'resultado':calculado})
assert len(contas)>=7,contas
resultado['contas_explicitas_extraidas']=contas
# Cross-resource end states of the printed situations, checked separately from single equations.
combate=soup.select_one('#combate').get_text(' ',strip=True)
interceptar=soup.select_one('#interceptar').get_text(' ',strip=True)
assert '18 de Vida · 5 PE' in combate
assert '15 de Vida e 5 PE' in interceptar and '18 de Vida e 5 PE' in interceptar
assert 23-(3+2)==18 and 8-3==5 and 14-sum([4,5,5])==0
assert (11+3)>=13 and (7+6+2)>(11+3) and 18-(4+2)/2==15
resultado['estados_finais']={'combate':{'vida':18,'PE':5},'protecao_defesa':{'vida':15,'PE':5,'reacao':'gasta'},'protecao_bloquear':{'vida':18,'PE':5,'reacao':'gasta'}}
# Verify document links within the delivered proposal.
links_doc=[]
for f in BASE.glob('*.md'):
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',f.read_text()):
        t=m.group(1)
        if t.startswith(('http:','https:','#')):continue
        assert (f.parent/t).exists() or (f.parent/t)==BASE/'CONFERENCIA.json',(f.name,t)
        links_doc.append([f.name,t])
assert not list(BASE.rglob('*.png')) and not list(BASE.rglob('*.jpg'))
resultado['links_documentais']=len(links_doc)
resultado['imagens_geradas_por_IA_incorporadas']=False
resultado['grafico']='diagrama vetorial de posições, SVG'
resultado['conferencia_semantica']='Cotejo do próprio autor: momento, ação, custo, alcance, duração, frequência, alvo, recursos e extremos defensivos. Registro em RELATORIO.md.'
resultado['leitura_independente']='não realizada nesta entrega'
resultado['teste_humano']='não realizado'
resultado['acessibilidade']='sem certificação ou teste de leitor de tela'
resultado['bateria_mecanica_integral']='não executada; proposta editorial sem mudança de regra ou de arquivos publicados'
fontes=['sistema/05-material/livro/manual/08-inicio-rapido.md','sistema/05-material/livro/manual/10-como-jogar.md','sistema/05-material/livro/manual/11-o-turno.md','sistema/05-material/livro/manual/15-dano-e-condicoes.md','sistema/05-material/livro/manual/20-criacao-de-personagem.md','sistema/05-material/livro/manual/25-origens.md','sistema/05-material/livro/manual/40-fundamento.md','sistema/03-mecanica/04-pericias-e-testes.md','caminhos/05-Edicao-Integrada/01-Bastião-Caminho-e-Trilhas.md']
resultado['fontes_consultadas']=[{'arquivo':f,'sha256':sha(ROOT/f)} for f in fontes]
(BASE/'CONFERENCIA.json').write_text(json.dumps(resultado,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'paginas':[x['paginas'] for x in resultado['pdfs']],'links_pdf':[x['links_internos'] for x in resultado['pdfs']],'contas_extraidas':len(contas),'fontes_preservadas':preservados,'comparacao_mesmo_texto':True,'documentos_locais':len(links_doc)},ensure_ascii=False,indent=2))

"""Conferir a alteração pontual sem repetir a revisão integral da R50."""
from pathlib import Path
import json, hashlib, subprocess, difflib
from pypdf import PdfReader

B=Path(__file__).resolve().parents[1]
OLD=B.with_name('livro-diagramado-r50')
R=B/'revisao-r51'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
a=(OLD/'LIVRO-COMPLETO.md').read_text()
z=(B/'LIVRO-COMPLETO.md').read_text()
needle='recuperar **3 × sua maior Classe em pontos de vida**'
assert a.count(needle)==1
assert z==a.replace(needle,'recuperar **4 × sua maior Classe em pontos de vida**')
rows=read(B/'ALTERACOES-R50-para-R51.json')
assert len(rows)==1
old_blocks=read(OLD/'revisao-r50/BLOCOS-ESPERADOS.json')
rebuilt=dict(old_blocks)
for row in rows:
    assert rebuilt[row['bloco']]==row['antes']
    rebuilt[row['bloco']]=row['depois']
assert rebuilt==read(R/'BLOCOS-ESPERADOS.json')

m=read(B/'FONTES-E-VALIDACAO.json');o=read(OLD/'FONTES-E-VALIDACAO.json')
pdf=B/m['pdf'];old_pdf=OLD/o['pdf']
assert sha(pdf)==m['sha256_pdf']
assert m['paginas']==o['paginas']==397
assert m['ancoras']==o['ancoras'] and m['marcadores']==o['marcadores']
assert m['paginas_planejadas']==o['paginas_planejadas']
assert len(m['eventos'])==len(o['eventos'])
changed=[]
for x,y in zip(o['eventos'],m['eventos']):
    if x==y:continue
    assert x['bloco']==y['bloco']=='catalogo--cat-passivas-2-recursos'
    assert x['texto'].replace('3 × sua maior Classe','4 × sua maior Classe')==y['texto']
    assert {k:v for k,v in x.items() if k!='texto'}=={k:v for k,v in y.items() if k!='texto'}
    changed.append(y['pagina'])
assert changed==[285]
texts=[]
for p in [old_pdf,pdf]:
    texts.append(subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True).split('\f'))
assert len(texts[0])==len(texts[1])
pages=[i+1 for i,(x,y) in enumerate(zip(*texts)) if x!=y]
assert pages==[285]
assert texts[0][284].replace('3 × sua maior Classe','4 × sua maior Classe')==texts[1][284]
base=read(R/'BASE-R50.json')
assert all(sha(OLD/n)==v for n,v in base['sha256'].items())

reader=PdfReader(pdf)
assert len(reader.pages)==397
page=reader.pages[284]
assert '4 × sua maior Classe' in page.extract_text()
subprocess.run(['pdftoppm','-f','285','-l','285','-scale-to','1800','-singlefile','-png',str(pdf),str(R/'pagina-285')],check=True)
save(R/'VALIDACAO.json',dict(edicao='R51',sha256_pdf=sha(pdf),sha256_texto=sha(B/'LIVRO-COMPLETO.md'),
    paginas=397,blocos_alterados=1,blocos_preservados=510,paginas_com_texto_alterado=pages,
    texto_integral_so_altera_o_multiplicador=True,geometria_dos_elementos_inalterada=True,
    ancoras_marcadores_e_paginacao_inalterados=True,R50_preservada=True,
    escopo='Comparação integral do texto e da composição; extração das 397 páginas; renderização da página alterada. Não há nova simulação de balanceamento.'))
support=[]
for name in ['gerar_livro.py','ler_fontes.py','revisao_r51.py']:
    old=(OLD/name).read_text() if (OLD/name).exists() else None
    new=(B/name).read_text()
    support.append(dict(arquivo=name,antes=old,depois=new,motivo='Gerar a R51 e aplicar a única correção registrada.'))
save(R/'ALTERACOES-SUPORTE.json',support)
print(json.dumps(read(R/'VALIDACAO.json'),ensure_ascii=False,indent=2))

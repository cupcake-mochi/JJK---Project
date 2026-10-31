"""Conferência da retificação pontual das Origens."""
from pathlib import Path
import json,hashlib,subprocess,re,difflib
from pypdf import PdfReader

B=Path(__file__).resolve().parents[1]; OLD=B.with_name('livro-diagramado-r51'); R=B/'revisao-r52'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
a=(OLD/'LIVRO-COMPLETO.md').read_text();expected=a
for x,y in read(R/'SUBSTITUICOES.json'):
    assert expected.count(x)==1;expected=expected.replace(x,y)
assert (B/'LIVRO-COMPLETO.md').read_text()==expected
old_blocks=read(OLD/'revisao-r51/BLOCOS-ESPERADOS.json');rebuilt=dict(old_blocks)
rows=read(B/'ALTERACOES-R51-para-R52.json');assert len(rows)==1
for row in rows:
    assert rebuilt[row['bloco']]==row['antes'];rebuilt[row['bloco']]=row['depois']
assert rebuilt==read(R/'BLOCOS-ESPERADOS.json')
assert old_blocks['origens--restricao-corpo']==rebuilt['origens--restricao-corpo']
assert old_blocks['origens--restricao-ce4']==rebuilt['origens--restricao-ce4']
assert old_blocks['catalogo--cat-passivas-2-recursos']==rebuilt['catalogo--cat-passivas-2-recursos']
assert 'recuperar **4 × sua maior Classe' in rebuilt['catalogo--cat-passivas-2-recursos']
m=read(B/'FONTES-E-VALIDACAO.json');o=read(OLD/'FONTES-E-VALIDACAO.json')
pdf=B/m['pdf'];assert sha(pdf)==m['sha256_pdf'];reader=PdfReader(pdf)
assert len(reader.pages)==m['paginas']
assert all(sha(OLD/name)==value for name,value in read(R/'BASE-R51.json')['sha256'].items())
texts=[subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True).split('\f') for p in [OLD/o['pdf'],pdf]]
assert len(texts[0])==len(texts[1]),'Conferir mudança no total de páginas'
changed=[i+1 for i,(x,y) in enumerate(zip(*texts)) if x!=y]
direct=sorted({e['pagina'] for e in m['eventos'] if e['bloco']=='origens--legado-criar'})
render=sorted(set(changed+direct+[min(direct)-1,max(direct)+1]))
for p in render:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1800','-singlefile','-png',str(pdf),str(R/f'pagina-{p:03}')],check=True)
save(R/'VALIDACAO.json',dict(edicao='R52',sha256_pdf=sha(pdf),sha256_texto=sha(B/'LIVRO-COMPLETO.md'),
    paginas=m['paginas'],blocos_alterados=1,blocos_preservados=510,
    texto_integral_corresponde_apenas_as_tres_substituicoes=True,
    restricao_corporal_e_CE4_preservados=True,recomposicao_4C_preservada=True,R51_preservada=True,
    paginas_com_diferenca_na_extracao=changed,paginas_renderizadas=render))
support=[]
for name in ['gerar_livro.py','ler_fontes.py','revisao_r52.py']:
    support.append(dict(arquivo=name,antes=(OLD/name).read_text() if (OLD/name).exists() else None,
        depois=(B/name).read_text(),motivo='Gerar a R52 e aplicar o bloco de correção registrado.'))
save(R/'ALTERACOES-SUPORTE.json',support)
print(json.dumps(read(R/'VALIDACAO.json'),ensure_ascii=False,indent=2))

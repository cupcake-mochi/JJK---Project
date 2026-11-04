from pathlib import Path
import json,re,sys
from trocas_r64 import T,NUMEROS_NOVOS

H=Path(__file__).resolve().parent
BASE=Path('/home/mizuki/JJK-v0.341-para-subir/sistema/05-material/livro/ciclo-maldito-r41')
BASELINE=BASE/'revisao-de-regras/editorial-r63'
texto=(BASELINE/'LIVRO-COMPLETO-R63.md').read_text()
snap=json.loads((BASELINE/'BLOCOS-R63.json').read_text())
def visivel(texto):
    texto=re.sub(r'<!--.*?-->|<a [^>]*></a>','',texto,flags=re.S)
    return re.sub(r'\]\([^)]*\)',']',texto)
def numeros(texto):
    return re.findall(r'\d+(?:[,.]\d+)*',visivel(texto))
def marcas(texto):
    return re.findall(r'<a id="[^"]+"></a>|<!--.*?-->|\]\([^)]*\)',texto,flags=re.S)
def gravar(nome,conteudo):
    p=H/nome
    temp=p.with_suffix(p.suffix+'.novo')
    temp.write_text(conteudo)
    temp.replace(p)
novo=texto
ops=[]
for i,(ids,bloco,antes,depois) in enumerate(T,1):
    assert novo.count(antes)==1,ids
    assert numeros(antes)==numeros(depois) or i in NUMEROS_NOVOS,ids
    assert marcas(antes)==marcas(depois),ids
    if bloco=='capitulo-6':
        assert antes in novo.split('## 6. Caminhos e Trilhas',1)[1].split('<!-- fonte:',1)[0]
    else:
        assert snap[bloco].count(antes)==1,ids
        snap[bloco]=snap[bloco].replace(antes,depois,1)
    novo=novo.replace(antes,depois,1)
    ops.append({'id':f'R64-{i:03d}','propostas':ids,'bloco':bloco,'antes':antes,'depois':depois,
                'motivo':'Linguagem simples aprovada em 04/11/2026. Troca de “registre” e/ou “conforme” conforme o contexto.'})
assert marcas(texto)==marcas(novo)
ancoras=r'<a id="[^"]+"></a>'
assert [numeros(b) for b in re.split(ancoras,texto)]==[numeros(b) for b in re.split(ancoras,novo)]
for pattern,quant in [(r'\bregistrem?\b',139),(r'\bconforme\b',163)]:
    assert len(re.findall(pattern,visivel(texto),re.I))==quant
    assert not re.search(pattern,visivel(novo),re.I)
assert re.findall(r'\bRequisitos?\b',visivel(texto))==re.findall(r'\bRequisitos?\b',visivel(novo))
assert len(ops)==293
print(len(ops),'trocas em',len({op['bloco'] for op in ops}),'blocos e abertura de capítulo; números, âncoras, links e Requisito conferidos.')
if '--gravar' in sys.argv:
    gravar('LIVRO-CANDIDATA.md',novo)
    gravar('TROCAS-R64.json',json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
    gravar('BLOCOS-R64.json',json.dumps(snap,ensure_ascii=False,indent=2)+'\n')

from pathlib import Path
import hashlib,json,re
H=Path(__file__).resolve().parent
S=Path('/home/mizuki/JJK-v0.341-para-subir')
B=S/'sistema/05-material/livro/ciclo-maldito-r41'
R=B/'revisao-de-regras'
E=R/'editorial-r64'

def write(p,text):
    p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_suffix(p.suffix+'.novo')
    temp.write_text(text)
    temp.replace(p)

def dump(p,x):
    write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def edit(p,a,b):
    old=p.read_text()
    assert old.count(a)==1,(p,a)
    write(p,old.replace(a,b))

ops=json.loads((H/'TROCAS-R64.json').read_text())
snapshot=json.loads((R/'editorial-r63/BLOCOS-R63.json').read_text())
current=(B/'LIVRO-COMPLETO.md').read_text()
assert current==(R/'editorial-r63/LIVRO-COMPLETO-R63.md').read_text()
for op in ops:
    a,d,k=op['antes'],op['depois'],op['bloco']
    assert current.count(a)==1,op['id']
    current=current.replace(a,d,1)
    if k!='capitulo-6':
        assert snapshot[k].count(a)==1,op['id']
        snapshot[k]=snapshot[k].replace(a,d,1)
assert current==(H/'LIVRO-CANDIDATA.md').read_text()
assert snapshot==json.loads((H/'BLOCOS-R64.json').read_text())
write(B/'LIVRO-COMPLETO.md',current)
write(E/'LIVRO-COMPLETO-R64.md',current)
dump(E/'BLOCOS-R64.json',snapshot)
dump(R/'alteracoes/R63-para-R64.json',ops)
dump(E/'FONTE-PUBLICADA.json',{
    'revisao':'R64','sha256_texto':hashlib.sha256(current.encode()).hexdigest(),
    'blocos':len(snapshot),'composicao_local':str(H/'composicao'),'registros':len(ops),
    'tipo':'Linguagem simples aprovada em 04/11/2026. Revisão de “registre” e “conforme”, incluindo dois títulos.',
})
p=S/'conferir-repositorio.py'
s=p.read_text()
i=s.index("bloco('12. FONTE R63")
j=s.index('# ----',i)
t=s[i:j].replace('R63','R64').replace('editorial-r63','editorial-r64').replace('range(54, 64)','range(54, 65)')
before="""        _reaplicado57 = dict(_fim53)
        for _r57 in _registro57:
"""
after="""        _reaplicado57 = dict(_fim53)
        if _n57 == 64:
            # A abertura do capítulo 6 pertence à fonte consolidada, fora dos blocos de Caminho.
            _prefacios64 = [r for r in _registro57 if r['bloco'] == 'capitulo-6']
            _registro57 = [r for r in _registro57 if r['bloco'] != 'capitulo-6']
            _fonte_anterior64 = open(os.path.join(_BASE53, 'revisao-de-regras', 'editorial-r63', 'LIVRO-COMPLETO-R63.md'), encoding='utf-8').read()
            _marco64 = '## 6. Caminhos e Trilhas\\n'
            _abertura_anterior64 = _fonte_anterior64.split(_marco64, 1)[1].split('<!-- fonte:', 1)[0]
            _abertura_atual64 = _md53.split(_marco64, 1)[1].split('<!-- fonte:', 1)[0]
            if len(_prefacios64) != 1:
                erro('12: falta o registro único da abertura do capítulo 6 na R64')
            else:
                _ant64, _dep64 = _prefacios64[0]['antes'], _prefacios64[0]['depois']
                if _abertura_anterior64.count(_ant64) != 1 or _abertura_anterior64.replace(_ant64, _dep64, 1) != _abertura_atual64:
                    erro('12: registro R63-para-R64 não reconstrói a abertura do capítulo 6')
            _registros57 += len(_prefacios64)
        for _r57 in _registro57:
"""
assert t.count(before)==1
t=t.replace(before,after)
write(p,(s[:i]+t+s[j:]).replace("'EDICAO-ATUAL.json', 'REVISAO-R63.json')","'EDICAO-ATUAL.json', 'REVISAO-R64.json')"))
for edition in ['editorial-r57','fundamento-r53']:
    f=R/edition/'testar-integridade.py'
    edit(f,"bloco('12. FONTE R63","bloco('12. FONTE R64")
edit(R/'editorial-r57/testar-integridade.py','R62-para-R63.json','R63-para-R64.json')
edit(R/'fundamento-r53/testar-integridade.py','fonte corrente R63','fonte corrente R64')
edit(S/'sistema/03-mecanica/conferir-fundamento.py','editorial-r63/BLOCOS-R63.json','editorial-r64/BLOCOS-R64.json')
edit(S/'sistema/03-mecanica/livro.py','edição atual, R63','edição atual, R64')
print('Texto e cadeia R64 integrados.',len(ops),'trocas')

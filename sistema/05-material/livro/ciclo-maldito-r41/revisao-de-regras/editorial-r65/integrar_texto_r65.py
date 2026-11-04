from pathlib import Path
import hashlib,json,re,sys

H=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve()
B=R/'sistema/05-material/livro/ciclo-maldito-r41'
E=B/'revisao-de-regras'
O=E/'editorial-r65'

def write(p,text):
    p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+'.novo')
    tmp.write_text(text)
    tmp.replace(p)

def dump(p,obj):
    write(p,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def edit(p,before,after):
    text=p.read_text()
    assert text.count(before)==1,(p,before)
    write(p,text.replace(before,after,1))

base=(E/'editorial-r64/LIVRO-COMPLETO-R64.md').read_text()
final=(H/'LIVRO-CANDIDATA.md').read_text()
src=B/'LIVRO-COMPLETO.md'
assert src.read_text() in (base,final)
ops=json.loads((H/'TROCAS-R65.json').read_text())
snap=json.loads((E/'editorial-r64/BLOCOS-R64.json').read_text())
replay=base
for item in ops:
    k,a,b=item['bloco'],item['antes'],item['depois']
    assert replay.count(a)==snap[k].count(a)==1,item['id']
    replay=replay.replace(a,b,1)
    snap[k]=snap[k].replace(a,b,1)
assert replay==final and snap==json.loads((H/'BLOCOS-R65.json').read_text())
write(src,final)
write(O/'LIVRO-COMPLETO-R65.md',final)
dump(O/'BLOCOS-R65.json',snap)
dump(E/'alteracoes/R64-para-R65.json',ops)
dump(O/'FONTE-PUBLICADA.json',{'revisao':'R65','sha256_texto':hashlib.sha256(final.encode()).hexdigest(),
    'blocos':len(snap),'composicao_local':str(H/'composicao'),'registros':len(ops),
    'tipo':'Linguagem simples em Caminhos e Trilhas, preservando regras e rótulos.'})
p=R/'conferir-repositorio.py'
text=p.read_text()
a=text.index("bloco('12. FONTE R64")
b=text.index('# ----',a)
part=text[a:b]
for old,new in [
    ("FONTE R64 E CADEIA","FONTE R65 E CADEIA"),
    ("'revisao-de-regras', 'editorial-r64'","'revisao-de-regras', 'editorial-r65'"),
    ('da fonte R64 difere','da fonte R65 difere'),
    ('range(54, 65)','range(54, 66)'),
    ('diferem da edição R64','diferem da edição R65'),
    ('da cadeia R52 a R64','da cadeia R52 a R65'),
    ('os registros da R64:', 'os registros da R65:'),
]:
    assert part.count(old)==1,old
    part=part.replace(old,new,1)
text=text[:a]+part+text[b:]
old="'EDICAO-ATUAL.json', 'REVISAO-R64.json')"
assert text.count(old)==1
write(p,text.replace(old,"'EDICAO-ATUAL.json', 'REVISAO-R65.json')",1))
for dirname in ('editorial-r57','fundamento-r53'):
    edit(E/dirname/'testar-integridade.py',"bloco('12. FONTE R64","bloco('12. FONTE R65")
edit(E/'editorial-r57/testar-integridade.py','R63-para-R64.json','R64-para-R65.json')
edit(E/'fundamento-r53/testar-integridade.py','fonte corrente R64','fonte corrente R65')
guard=R/'sistema/03-mecanica/conferir-fundamento.py'
edit(guard,'editorial-r64/BLOCOS-R64.json','editorial-r65/BLOCOS-R65.json')
old='Queima-Roupa conserva seus alvos'
new='Queima-Roupa ainda limita seus alvos'
assert new in final
if old in guard.read_text():
    edit(guard,old,new)
else:
    assert guard.read_text().count(new)==1
edit(R/'sistema/03-mecanica/livro.py','edição atual, R64','edição atual, R65')
print(f'R65 integrada em {R}. Cadeia reproduz {len(ops)} trocas, {len(snap)} blocos.')

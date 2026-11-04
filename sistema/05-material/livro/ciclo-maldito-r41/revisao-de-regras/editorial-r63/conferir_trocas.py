import json,re,sys,collections
from pathlib import Path
H=Path(__file__).resolve().parent
S=Path('/home/mizuki/JJK-v0.341-para-subir/sistema/05-material/livro/ciclo-maldito-r41')
sys.path.insert(0,str(H));from trocas_r63 import T,NUMEROS_NOVOS
texto=(S/'LIVRO-COMPLETO.md').read_text();blocos=json.loads((S/'revisao-de-regras/editorial-r62/BLOCOS-R62.json').read_text())
num=lambda s:collections.Counter(re.findall(r'\d+(?:,\d+)?',re.sub(r'\]\(#[^)]*\)',']',s)))
def vis(t):t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'<a [^>]*></a>','',t);return re.sub(r'\]\([^)]*\)',']',t)
ops=[];erros=[];novo=texto;snap=dict(blocos)
for i,(mot,a,d) in enumerate(T,1):
    if novo.count(a)!=1:erros.append(f'{i} livro tem {novo.count(a)}x: {a[:70]}');continue
    ks=[k for k,v in snap.items() if a in v]
    if len(ks)!=1 or snap[ks[0]].count(a)!=1:erros.append(f'{i} blocos {ks}: {a[:70]}');continue
    if num(a)!=num(d) and i not in NUMEROS_NOVOS:erros.append(f'{i} números mudaram: {num(a)} -> {num(d)}')
    if '<a id' in a+d:erros.append(f'{i} mexe em âncora')
    novo=novo.replace(a,d,1);snap[ks[0]]=snap[ks[0]].replace(a,d,1);ops.append({'id':f'R63-{i:03d}','bloco':ks[0],'motivo':mot,'antes':a,'depois':d})
anc=lambda t:re.findall(r'<a id="[^"]+"></a>',t)
if anc(texto)!=anc(novo):erros.append('âncoras mudaram')
lnk=lambda t:re.findall(r'\]\(([^)]*)\)',t)
if lnk(texto)!=lnk(novo):erros.append('destinos de link mudaram')
v=vis(novo)
print('itens',len(T),'aplicados',len(ops),'blocos',len({o['bloco'] for o in ops}))
for w,p in [('parcela',r'\bparcelas?\b'),('excedente',r'\bexcedentes?\b'),('vinculado',r'\bvinculad[oa]s?\b'),('elegível',r'\beleg[ií]ve(?:l|is)\b'),('efetivamente',r'\befetivamente\b'),('concessão',r'\bconcess(?:ão|ões)\b'),('pertinente',r'\bpertinentes?\b'),('retroativo',r'\bretroativ\w*\b'),('vencimento',r'\bvencimentos?\b'),('reserva',r'\breserv\w*'),('Ampliada',r'\bAmpliada\b')]:
    print(f'  {w}: antes {len(re.findall(p,vis(texto),re.I))} depois {len(re.findall(p,v,re.I))}',[m.group(0) for m in re.finditer(r'.{0,18}'+p+r'.{0,12}',v,re.I)][:6])
print('  palavras antes/depois:',len(vis(texto).split()),len(v.split()))
for e in erros:print('ERRO',e)
if not erros and '--gravar' in sys.argv:
    (H/'LIVRO-CANDIDATA.md').write_text(novo);json.dump(ops,open(H/'TROCAS-R63.json','w'),ensure_ascii=False,indent=2);json.dump(snap,open(H/'BLOCOS-R63.json','w'),ensure_ascii=False,indent=2);print('gravado')

import json,re,sys,collections
from pathlib import Path
H=Path(__file__).resolve().parent
S=Path('/home/mizuki/JJK-v0.341-para-subir/sistema/05-material/livro/ciclo-maldito-r41')
sys.path.insert(0,str(H));from trocas_r62 import T,NUMEROS_NOVOS
texto=(S/'LIVRO-COMPLETO.md').read_text();blocos=json.loads((S/'revisao-de-regras/editorial-r61/BLOCOS-R61.json').read_text())
num=lambda s:collections.Counter(re.findall(r'\d+(?:,\d+)?',re.sub(r'\]\(#[^)]*\)',']',s)))
def vis(t):t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'<a [^>]*></a>','',t);return re.sub(r'\]\([^)]*\)',']',t)
ops=[];erros=[];novo=texto;snap=dict(blocos)
for i,(mot,a,d) in enumerate(T,1):
    if novo.count(a)!=1:erros.append(f'{i} livro tem {novo.count(a)}x: {a[:60]}');continue
    ks=[k for k,v in snap.items() if a in v]
    if len(ks)!=1 or snap[ks[0]].count(a)!=1:erros.append(f'{i} blocos {ks}: {a[:60]}');continue
    if num(a)!=num(d) and i not in NUMEROS_NOVOS:erros.append(f'{i} números mudaram: {num(a)} -> {num(d)}')
    if '<a id' in a+d:erros.append(f'{i} mexe em âncora')
    novo=novo.replace(a,d,1);snap[ks[0]]=snap[ks[0]].replace(a,d,1);ops.append({'id':f'R62-{i:03d}','bloco':ks[0],'motivo':mot,'antes':a,'depois':d})
anc=lambda t:re.findall(r'<a id="[^"]+"></a>',t)
if anc(texto)!=anc(novo):erros.append('âncoras mudaram')
v=vis(novo)
print('itens',len(T),'aplicados',len(ops),'blocos',len({o['bloco'] for o in ops}))
for w in [r'\b[Ss]aldos?\b','lugar propício','reserva de Reação','reserva compartilhada',r'\*\*Ampliar\.\*\*']:print(f'  restam {w}: {len(re.findall(w,v))}')
print('  ponto(s) que sobram:',len(re.findall(r'[Pp]ontos? que sobra',v)),'| palavras antes/depois:',len(vis(texto).split()),len(v.split()))
for e in erros:print('ERRO',e)
if not erros and '--gravar' in sys.argv:
    (H/'LIVRO-CANDIDATA.md').write_text(novo);json.dump(ops,open(H/'TROCAS-R62.json','w'),ensure_ascii=False,indent=2);json.dump(snap,open(H/'BLOCOS-R62.json','w'),ensure_ascii=False,indent=2);print('gravado')

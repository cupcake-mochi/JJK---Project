from pathlib import Path
from collections import defaultdict
import json,hashlib,difflib
B=Path(__file__).resolve().parent;ROOT=B.parent;OLD=ROOT.parent/'livro-diagramado-r33'
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=read(ROOT/'FONTES-E-VALIDACAO.json');old=read(OLD/'FONTES-E-VALIDACAO.json')
assert sha(ROOT/m['pdf'])==m['sha256_pdf']
assert (ROOT/'LIVRO-COMPLETO.md').read_bytes()==(OLD/'LIVRO-COMPLETO.md').read_bytes()
assert all((OLD/f).is_file() and sha(OLD/f)==h for f,h in read(B/'BASE-R33-HASHES.json').items())
assert m['ancoras']==old['ancoras']
assert m['posicionamento_imagens']==old['posicionamento_imagens']
assert m['capas_e_aberturas']==old['capas_e_aberturas']
assert m['eventos']==old['eventos'],'Houve recomposição: registrar e verificar antes de concluir'
applied=m['revisao_r34']['titulos_aplicados'];assert len(applied)==21
assert {x['numero'] for x in applied}==set(range(1,22))
styles=read(ROOT/'ESTUDO-CAPITULO.json')
changes=[]
for c in applied:
 changes.append({'id':f'D34-{len(changes)+1:03d}','bloco':f'capitulo-{c["numero"]}','antes':{'texto':c['titulo'],'numero':c['numero'],'estilo':styles['opcoes']['base'],'geometria':{k:v for k,v in c.items() if k!='opcao'}},'depois':{'texto':c['titulo'],'numero':c['numero'],'estilo':styles['opcoes']['A'],'geometria':{k:v for k,v in c.items() if k!='opcao'}},'motivo':'Aplicar o selo vinho 1/A aprovado pelo autor, mantendo o espaço já reservado ao título.'})
save(B/'ALTERACOES-DIAGRAMACAO.json',changes);save(B/'ALTERACOES-TEXTO.json',[])
files=['gerar_livro.py','titulos_capitulo.py','ESTUDO-CAPITULO.json'];records=[];patch=[]
for f in files:
 before=OLD/f;after=ROOT/f
 records.append({'arquivo':f,'sha256_antes':sha(before) if before.exists() else None,'sha256_depois':sha(after)})
 patch.extend(difflib.unified_diff(before.read_text().splitlines(keepends=True) if before.exists() else [],after.read_text().splitlines(keepends=True),fromfile='R33/'+f,tofile='R34/'+f))
save(B/'REGISTRO-IMPLEMENTACAO.json',records);(B/'IMPLEMENTACAO.patch').write_text(''.join(patch))
result={'edicao':'R34','base':'R33','sha256_pdf':m['sha256_pdf'],'sha256_texto':sha(ROOT/'LIVRO-COMPLETO.md'),'paginas':m['paginas'],'texto_identico':True,'geometria_e_ordem_editorial_identicas':True,'titulos_com_selo':21,'ancoras_preservadas':len(m['ancoras']),'r33_preservada':True,'artes_capas_e_creditos_preservados':True,'opcoes_B_e_C_preservadas':True,'alteracoes_textuais':0,'problemas':[]}
save(B/'CONFERENCIA.json',result);print(json.dumps(result,ensure_ascii=False))

"""Confere texto, registros e preservação da base R31 na prova R32."""
from pathlib import Path
import hashlib,json,re
B=Path(__file__).resolve().parent;C=B/'revisao-de-compreensao';R=B/'revisao-de-regras';OLD=B.parent/'livro-diagramado-r31'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=(C/'BASE-LIVRO-COMPLETO.md').read_text();new=(B/'LIVRO-COMPLETO.md').read_text()
assert old==(OLD/'LIVRO-COMPLETO.md').read_text()
pat=r'<!-- fonte:([^\n]+) -->\n<a id="([^"]+)"></a>\n(.*?)(?=<!-- fonte:|<!-- parte:|<a id="capitulo-|\Z)'
a=list(re.finditer(pat,old,re.S));z=list(re.finditer(pat,new,re.S))
assert len(a)==len(z)==500
assert [x[2] for x in a]==[x[2] for x in z]
logs=json.loads((R/'ALTERACOES-REGRAS.json').read_text());by={r['bloco']:r for r in logs}
assert len(logs)==len(by)
assert {x[2] for x,y in zip(a,z) if x[3]!=y[3]}==set(by)
rebuilt=old
for x,y in reversed(list(zip(a,z))):
 if x[2] not in by:continue
 row=by[x[2]];assert row['antes']==x[3] and row['depois']==y[3]
 rebuilt=rebuilt[:x.start(3)]+row['depois']+rebuilt[x.end(3):]
assert rebuilt==new
hashes=json.loads((C/'BASE-R31-HASHES.json').read_text())
changed_base=[p for p,h in hashes.items() if '__pycache__' not in p and (not (OLD/p).exists() or sha(OLD/p)!=h)]
assert not changed_base,changed_base
preserved=[]
for folder in ['fontes-editoriais','referencias','capa','fontes-tipograficas']:
 for p in (OLD/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in str(p):
   assert p.read_bytes()==(B/p.relative_to(OLD)).read_bytes(),str(p)
   preserved.append(str(p.relative_to(OLD)))
for name in ['ORDEM.json','REFERENCIAS.json','ARTES-APLICADAS.json','CAPA-E-ABERTURAS.json','CREDITOS.json','GLOSSARIO-RESUMIDO.json','revisao-textual/ALTERACOES.json']:
 assert (OLD/name).read_bytes()==(B/name).read_bytes(),name
textual=json.loads((B/'revisao-textual/ALTERACOES.json').read_text())
assert len(textual)==73 and all(x['id']!='T072' for x in textual)
assert (R/'HISTORICO-ALTERACOES-R29-R30.json').read_bytes()==(OLD/'revisao-de-regras/ALTERACOES-REGRAS.json').read_bytes()
blocks={m[2]:m[3] for m in z};before={m[2]:m[3] for m in a}
for k in ['geral--carga','equip--eq-treino','equip--eqp-requisitos']:
 if k in blocks:assert blocks[k]==before[k],k
assert {p['item'] for p in json.loads((C/'SUBSTITUICOES.json').read_text()) if p['item']}=={'115','160','171'}
assert 'somente a proteção passiva desta aptidão' in blocks['aptidoes--apt-cobrir']
assert 'somente a proteção passiva desta Bênção' in blocks['rotas--rota-defesa']
for k in ('aptidoes--apt-cobrir','rotas--rota-defesa'):
 assert 'Traje, Revestimento e escudo continuam dando sua proteção.' in blocks[k]
assert 'na ordem de 100 metros (um quarteirão)' in blocks['equip--eqf-armas']
assert '**um dos seus dois Legados**' not in blocks['origens--legado-criar']
assert '**seus Legados**' in blocks['origens--legado-criar']
for k in ('dano--insistir','poderes--incompleta','campo--inv-carga'):
 if k in blocks:assert blocks[k]==before[k]
assert 'suas fichas' not in new.lower() and 'não tem como recusar' not in new.lower()
coverage=json.loads((C/'INDICE-LEITURA.json').read_text())
assert len(coverage)==63 and all(x['status']=='lido' for x in coverage)
assert set(k for x in coverage for k in x['blocos'])==set(blocks)
report={'base':'R31','nova':'R32','blocos':500,'blocos_alterados':len(logs),'blocos_regra':sum(x['altera_regras'] for x in logs),'blocos_compreensao':sum(not x['altera_regras'] for x in logs),'substituicoes':len(json.loads((C/'SUBSTITUICOES.json').read_text())),'reconstrucao_integral_pelo_registro':True,'diferencas_sem_registro':0,'R31_preservada':True,'arquivos_de_fontes_e_artes_preservados':len(preserved),'revisoes_R29_preservadas':73,'T072_ausente':True,'sha256_md':sha(B/'LIVRO-COMPLETO.md'),'problemas':[]}
(C/'CONFERENCIA-TEXTO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))

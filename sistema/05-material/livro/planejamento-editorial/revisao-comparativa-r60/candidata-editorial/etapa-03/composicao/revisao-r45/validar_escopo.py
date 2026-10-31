from pathlib import Path
import json,hashlib,runpy,re,sys
R=Path(__file__).resolve().parent;B=R.parent;old=B.parent/'livro-diagramado-r44'
sys.path.insert(0,str(B))
base=json.loads((R/'BASE-R44-SHA256.json').read_text());dif=[]
for name,h in base.items():
 p=old/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:dif.append(name)
assert not dif,dif
before=json.loads((R/'BLOCOS-BASE.json').read_text());rows=json.loads((B/'ALTERACOES-R44-para-R45.json').read_text());expected=json.loads((R/'BLOCOS-ESPERADOS.json').read_text());registered={r['bloco'] for r in rows}
g=runpy.run_path(str(B/'ler_fontes.py'));after=g['enriched']
assert set(after)==set(expected),(set(after)-set(expected),set(expected)-set(after))
assert all(after[k].strip()==expected[k].strip() for k in expected)
delta={k for k in set(before)|set(after) if before.get(k,'').strip()!=after.get(k,'').strip()}
assert delta==registered,(delta-registered,registered-delta)
for r in rows:assert r['antes']==before.get(r['bloco'],'') and r['depois']==after.get(r['bloco'],'')
unchanged=[k for k in before if k not in registered];assert all(before[k]==after[k] for k in unchanged)
# Regras recentes continuam presentes, inclusive exceções confirmadas no chat.
checks={
'CE4 criação':all(x in after['origens--restricao-corpo'] for x in ['na criação','cinco Talentos pagos','sem ocupar espaço conhecido']),
'Reparo acima':all(x in after['campo--inv-reparo'] for x in ['Uma acima','Duas ou mais acima','terço','quarto']),
'Bloquear pré-rolagem':any('antes' in v and 'rolagem' in v for k,v in after.items() if k.startswith('geral--') and 'Bloquear' in v),
'Promessa sem vaga':any('Promessas' in v and 'não entram' in v for k,v in after.items() if k.startswith('ritual--')),
'7 núcleos':sum(1 for k,v in after.items() if k.startswith('origens--origem-') and v.startswith('# ') and v.splitlines()[0] in ['# Latente','#Receptáculo','# Descendente','# Encarnado','# Híbrido','# Corpo Amaldiçoado','# Restrição Celestial'])==6,
'Nenhuma nomenclatura Feto visível':not any(re.search(r'\bFeto\b',v) for v in after.values()),
'Sem frases proibidas nas novas entradas':not any(x in r['depois'] for r in rows for x in ['suas fichas','não tem como recusar'])}
# Contar explicitamente as sete aberturas, sem depender do padrão dos IDs.
checks['7 núcleos']=len({v.splitlines()[0] for k,v in after.items() if k.startswith('origens--')}&{'# Latente','# Receptáculo','# Descendente','# Encarnado','# Híbrido','# Corpo Amaldiçoado','# Restrição Celestial'})==7
assert all(checks.values()),checks
result=dict(R44_arquivos_conferidos=len(base),R44_divergencias=dif,blocos_alterados=len(registered),blocos_inalterados=len(unchanged),blocos_novos=len(set(after)-set(before)),checagens=checks,metodo='Comparação integral por bloco contra registro antes/depois e hash de todos os arquivos fotografados da R44.')
(R/'VALIDACAO-DE-ESCOPO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(result)

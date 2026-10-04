from pathlib import Path
import json,hashlib,shutil,difflib
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');M=P/'consolidacao/lote-01/migracao-nomes';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=[]
for path,repls in {'aptidoes/lote-01/APTIDOES-E-REFINO.md': [('Classe 1, se esse vestígio','Categoria 1, se esse vestígio'),('Classe 2. Tem gatilho','Categoria 2. Tem gatilho'),('Dano e Condições','Dano e recuperação'),('Reencarnado','Encarnado')],'origens/lote-01/ORIGENS-E-LEGADOS.md':[('Dano e Condições','Dano e recuperação')]}.items():
 f=P/path;old=f.read_text();oldhash=sha(f);new=old
 for a,b in repls:
  assert a in new,(path,a);new=new.replace(a,b)
 backup=M/'antes-complemento'/path;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,backup);f.write_text(new)
 record.append({'arquivo':path,'antes':oldhash,'depois':sha(f),'substituicoes':repls,'diff':''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True))),'motivo':'Fechamento de dois exemplos remanescentes de Categoria e sincronização de títulos/Origem com os donos finais. Nenhuma regra ou número mudou.'})
 for name in ['LOCALIZACAO-EDITORIAL.json','REVISAO-EDITORIAL.json']:
  q=f.parent/'evidencias'/name;data=json.loads(q.read_text());data['sha256_texto']=sha(f);data['revisao_complemento_nomes']={'revisor':'/root/compatibilidade','hash_antes':oldhash,'hash_depois':sha(f),'nota':record[-1]['motivo']}
  # exact contextual exceptions are altered only where corresponding literal was renamed.
  for ex in data.get('excecoes_localizacao',[]):
   for a,b in repls:ex['trecho']=ex.get('trecho','').replace(a,b)
  q.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 if 'origens' in path:
  q=f.parent/'INVENTARIO.json';d=json.loads(q.read_text());
  for key in ['sha256_texto','sha256_manuscrito']:
   if key in d:d[key]=sha(f)
  q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(M/'COMPLEMENTO.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))

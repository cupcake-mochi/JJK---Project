from pathlib import Path
import json,hashlib,shutil,difflib,re
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');M=P/'consolidacao/lote-01/migracao-nomes';C=M/'remissoes';C.mkdir(exist_ok=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j=json.loads((P/'consolidacao/lote-01/evidencias/REMISSOES-TEXTUAIS.json').read_text());items=next(v for k,v in j.items() if isinstance(v,list) and v and isinstance(v[0],dict) and 'id' in v[0]);ids={'REM-01','REM-02','REM-08','REM-09','REM-10','REM-13','REM-14','REM-15','REM-16','REM-17'}
selected=[x for x in items if x['id'] in ids];paths=set(x['arquivo'] for x in selected);records=[]
for path in paths:
 f=P/path;b=f.parent;old=f.read_text();h=sha(f);backup=C/'antes'/path;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,backup)
 config=json.loads((b/'VALIDACAO.json').read_text())
 for q in list(b.glob('*.json'))+list((b/'evidencias').glob('*.json'))+[b/'output/pdf'/config['pdf']]:
  dest=C/'qa-antes'/b.relative_to(P)/q.relative_to(b);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(q,dest)
 s=old;changes=[]
 for item in [x for x in selected if x['arquivo']==path]:
  before=item['trecho'];assert s.count(before)==1,(path,item['id']);after=before.replace(item['expressao_anterior'],item['proposta'])
  if item['id'] in ['REM-14','REM-15']:
   after=after.replace('de Ataques e Dano e crítico, em Regras gerais','das seções **Ataques** e **Dano e crítico**, em Regras gerais').replace('está em Ataques e Dano e crítico, em Regras gerais','está nas seções **Ataques** e **Dano e crítico**, em Regras gerais')
  elif item['id']=='REM-16':after=after.replace('ficam em Alcance e Defesa e cobertura, em Regras gerais','ficam nas seções **Alcance** e **Defesa e cobertura**, em Regras gerais')
  s=s.replace(before,after);changes.append({'id':item['id'],'antes':before,'depois':after,'motivo':item['motivo']})
 if 'equipamento/' in path:
  before='ainda não recupera a proteção passiva de energia:';after='ainda não recupera a proteção passiva disponível na ficha:';assert s.count(before)==1;s=s.replace(before,after);changes.append({'id':'REM-UNIFORME','antes':before,'depois':after,'motivo':'Exemplo serve também a rota sem energia; não altera o cálculo.'})
 assert re.findall(r'\d+(?:[.,]\d+)?',s)==re.findall(r'\d+(?:[.,]\d+)?',old)
 f.write_text(s)
 for name in ['LOCALIZACAO-EDITORIAL.json','REVISAO-EDITORIAL.json']:
  q=b/'evidencias'/name;data=json.loads(q.read_text());data['sha256_texto']=sha(f);data['revisao_remissoes']={'revisor':'/root/compatibilidade','sha256_antes':h,'sha256_depois':sha(f),'ids':[c['id'] for c in changes],'independente':'/root aprovou o relatório de /root/rotas_didatica e os antes/depois.'}
  q.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 if 'origens/' in path:
  q=b/'INVENTARIO.json';data=json.loads(q.read_text());data['sha256_texto']=sha(f);q.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 records.append({'arquivo':path,'sha256_antes':h,'sha256_depois':sha(f),'alteracoes':changes,'diff':''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True)))})
(C/'ALTERACOES.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');print(json.dumps(records,ensure_ascii=False,indent=2))

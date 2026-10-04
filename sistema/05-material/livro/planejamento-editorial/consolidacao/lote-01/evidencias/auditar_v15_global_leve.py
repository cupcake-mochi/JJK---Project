from pathlib import Path
import json,hashlib,re,datetime
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'consolidacao/lote-01';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();order=json.loads((B/'ORDEM.json').read_text());trans={'dano','rotas','campo','emanador','evocador','ritual'};reports=[]
def read(p):
 try:return json.loads(p.read_text())
 except FileNotFoundError:return None
 except json.JSONDecodeError:return {'_gravacao_em_curso':True}
for key,ref in order['fontes'].items():
 source=P/ref;folder=source.parent;h=sha(source);conf=read(folder/'VALIDACAO.json') or {};pdf=folder/'output/pdf'/conf.get('pdf','ausente.pdf');ph=sha(pdf) if pdf.is_file() else None;v=read(folder/'VALIDADORES.json');c=read(folder/'CONFERENCIA.json');m=read(folder/'MANIFESTO.json');issues=[]
 if v is None:issues.append('VALIDADORES.json ausente')
 else:
  vals=v.get('validadores',[]);ids=[x.get('id') for x in vals] if isinstance(vals,list) else list(vals);missing=[f'V{i:02}' for i in range(1,16) if f'V{i:02}' not in ids]
  if missing:issues.append('Validadores ausentes: '+', '.join(missing))
  if v.get('sha256_texto')!=h:issues.append('VALIDADORES com hash de texto anterior')
  if v.get('sha256_pdf') not in [None,ph]:issues.append('VALIDADORES com hash de PDF anterior')
 if c is None:issues.append('CONFERENCIA ausente')
 else:
  if c.get('ok') is not True:issues.append('CONFERENCIA não aprovada')
  if c.get('sha256_texto')!=h:issues.append('CONFERENCIA com texto anterior')
  if c.get('sha256_pdf')!=ph:issues.append('CONFERENCIA com PDF anterior')
 if m is None:issues.append('MANIFESTO ausente')
 else:
  indexed={x['arquivo']:x['sha256'] for x in m.get('arquivos',[]) if isinstance(x,dict) and 'arquivo' in x and 'sha256' in x} if 'arquivos' in m else {k:(v.get('sha256') if isinstance(v,dict) else v) for k,v in m.items()}
  for rel,expected in [(source.name,h),('output/pdf/'+conf.get('pdf',''),ph),('VALIDADORES.json',sha(folder/'VALIDADORES.json') if v else None),('CONFERENCIA.json',sha(folder/'CONFERENCIA.json') if c else None)]:
   if expected and indexed.get(rel)!=expected:issues.append('MANIFESTO desatualizado/sem '+rel)
 a=read(folder/'ALTERACOES.json');rows=a if isinstance(a,list) else next((a[k] for k in ['decisoes','alteracoes'] if a and k in a),[]);compact=[]
 for row in rows:
  title=next((str(row[k]) for k in ['assunto','nome','secao','ancora','pagina'] if row.get(k)),None)
  if not title:title=next((str(row[k]).split('. ')[0][:120] for k in ['depois','candidata','motivo'] if row.get(k)),'Sem título')
  compact.append({'id':row.get('id'),'tema':title,'tipo':row.get('tipo',row.get('natureza','não marcado'))})
 report={'id':key,'arquivo':ref,'sha256_texto':h,'sha256_pdf':ph,'paginas':conf.get('paginas'),'validadores_presentes':len(ids) if v else 0,'conferencia_checks':c.get('verificacoes') if c else None,'conferencia_ok':bool(c and c.get('ok')),'decisoes':len(rows) if a is not None else None,'resumo_decisoes':compact,'achados':issues,'estado':'transiente informado pela raiz' if issues and key in trans else 'pendência documental' if issues else 'metadados coerentes nesta fotografia','gravacao_em_curso':key in trans}
 if not a:
  other=folder/'REVISAO-E-FONTES.md';report['alternativa_registro']=str(other.relative_to(P)) if other.exists() else None;report['contagem_limite']='Não foi inventada uma contagem de decisões a partir de prosa.'
 reports.append(report)
r={'data_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'escopo':'Auditoria leve de metadados dos23donos de ORDEM.json; valida presença V01–V15, hashes do texto/PDF e índice crítico do manifesto. Não relê regras, não executa testes novamente e não altera documentos de outros donos.','sha256_ordem':sha(B/'ORDEM.json'),'fontes':len(reports),'decisoes_registradas':sum(x['decisoes'] or 0 for x in reports),'donos_com_registro_contavel':sum(x['decisoes'] is not None for x in reports),'checks_registrados':sum(x['conferencia_checks'] or 0 for x in reports),'unidades':reports,'limites':['Fotografia suscetível a gravações concorrentes identificadas.','O número de decisões inclui editoriais, sincronizações e alterações mecânicas; não equivale a quantidade de mudanças de regra.','Registros transversais de nomes/remissões são adicionais e não foram somados para evitar duplicação.']}
(B/'evidencias/V15-GLOBAL-LEVE.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
lines=['# Auditoria documental global','',r['escopo'],'',f"{r['decisoes_registradas']} registros de decisões em {r['donos_com_registro_contavel']} arquivos; {r['fontes']} fontes selecionadas.",'','| Dono | V01–V15 | Decisões | Estado | Achados |','|---|---:|---:|---|---|']
for x in reports:lines.append(f"| {x['id']} | {x['validadores_presentes']} | {x['decisoes'] if x['decisoes'] is not None else 'não contado'} | {x['estado']} | {'; '.join(x['achados']) or '—'} |")
lines+=['','## Limites','']+['- '+x for x in r['limites']]
(B/'evidencias/V15-GLOBAL-LEVE.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:r[k] for k in ['fontes','decisoes_registradas','donos_com_registro_contavel','checks_registrados']},ensure_ascii=False))
for x in reports:
 if x['achados']:print(x['id'],x['estado'],x['achados'])

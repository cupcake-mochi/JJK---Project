from pathlib import Path
import json,collections
B=Path('/home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r57');out={}
for edition in ['r56','r57']:
 m=json.loads((B.parent/f'livro-diagramado-{edition}/FONTES-E-VALIDACAO.json').read_text());es=collections.defaultdict(list);chs=collections.defaultdict(list)
 for e in m['eventos']:es[e['pagina']].append(e)
 for p in m['paginas_planejadas']:
  if p['tipo']=='content':chs[p['capitulo']].append(p['pagina'])
 rows=[]
 for p in m['paginas_planejadas']:
  if p['tipo']!='content' or not any(not e['gerado'] for e in es[p['pagina']]):continue
  vals=[]
  for right in [False,True]:
   q=[e for e in es[p['pagina']] if not e['gerado'] and (e['x']+e['largura']>300 if right else e['x']<290)]
   vals.append(max(0,(min((e['y'] for e in q),default=777)-102)/675))
  rows.append(dict(pagina=p['pagina'],branco_medio=round(sum(vals)/2,4),diferenca=round(abs(vals[0]-vals[1]),4),colunas=vals,borda=p['pagina'] in [min(chs[p['capitulo']]),max(chs[p['capitulo']])],grupo=p['grupo']))
 middle=[r for r in rows if not r['borda']]
 out[edition]=dict(paginas=m['paginas'],branco_equivalente=round(sum(r['branco_medio'] for r in rows),2),desigualdade=sum(r['diferenca']>.35 for r in middle),acima_terco=[r['pagina'] for r in middle if r['branco_medio']>1/3],diferencas=[(r['pagina'],r['diferenca']) for r in middle if r['diferenca']>.35],todas=rows)
 print(edition,{k:v for k,v in out[edition].items() if k!='todas'})
(B/'revisao-r57/METRICAS-COMPARADAS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))

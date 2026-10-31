from pathlib import Path
import json,sys
B=Path(__file__).resolve().parents[1];tag=sys.argv[1];base=B.with_name('livro-diagramado-r49') if tag=='base' else B
m=json.loads((base/'FONTES-E-VALIDACAO.json').read_text());T=776.693;F=102.047;CAP=T-F
ps=m['paginas_planejadas'];events=m['eventos'];heads={'major','h1','h2','h3','marker'}
ch={}
for p in ps:
 if p['tipo']=='content':ch.setdefault(p['capitulo'],[]).append(p['pagina'])
rows=[]
for p in ps:
 if p['tipo']!='content':continue
 es=[e for e in events if e['pagina']==p['pagina'] and e['tipo'] not in {'small'}]
 if not es:continue
 bottoms=[T,T]
 for e in es:
  if e['largura']>300:bottoms=[min(x,e['y']) for x in bottoms]
  else:
   col=int(e['x']>250);bottoms[col]=min(bottoms[col],e['y'])
 empty=[max(0,x-F) for x in bottoms];mid=p['pagina'] not in {ch[p['capitulo']][0],ch[p['capitulo']][-1]}
 nxt=[e for e in events if e['pagina']==p['pagina']+1 and not e['gerado']]
 fitting=None
 if nxt and nxt[0]['capitulo']==p['capitulo'] and nxt[0]['tipo'] in heads and nxt[0]['largura']<300:
  tail=[]
  for e in nxt:
   if tail and (e['tipo'] in heads or e['largura']>300):break
   tail.append(e)
  nh=sum(e['altura']+6 for e in tail)
  if len(tail)>1 and nh<empty[1]:fitting={'titulo':nxt[0]['texto'],'altura_aprox':round(nh,1)}
 rows.append({'pagina':p['pagina'],'capitulo':p['capitulo'],'meio_capitulo':mid,'vazio_esquerda_pt':round(empty[0],1),'vazio_direita_pt':round(empty[1],1),'vazio_fracao':round(sum(empty)/(2*CAP),3),'desequilibrio':round(abs(empty[0]-empty[1])/CAP,3),'proxima_entrada_parece_caber':fitting})
r={'edicao':tag,'paginas':m['paginas'],'sha256_pdf':m['sha256_pdf'],'metodo':'Vazio abaixo do último elemento em cada coluna; elemento largo conta nas duas. Exclui capas, artes, sumário, índice e modelos. Não mede entrelinhas. Triagem de entrada seguinte usa altura aproximada e precisa de inspeção.','vazio_equivalente_paginas':round(sum(x['vazio_fracao'] for x in rows),2),'vazio_meio_capitulo':round(sum(x['vazio_fracao'] for x in rows if x['meio_capitulo']),2),'mais_de_um_terco_meio':[x['pagina'] for x in rows if x['meio_capitulo'] and x['vazio_fracao']>1/3],'proxima_entrada_parece_caber':[x for x in rows if x['proxima_entrada_parece_caber']],'paginas_detalhes':rows}
(B/'revisao-r50'/f'METRICAS-{tag}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(tag,r['paginas'],r['vazio_equivalente_paginas'],r['vazio_meio_capitulo'],'candidatas',len(r['proxima_entrada_parece_caber']));print([(x['pagina'],x['proxima_entrada_parece_caber']['titulo']) for x in r['proxima_entrada_parece_caber']])

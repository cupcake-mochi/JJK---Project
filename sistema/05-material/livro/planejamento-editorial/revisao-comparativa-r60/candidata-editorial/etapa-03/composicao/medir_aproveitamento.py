from pathlib import Path
from collections import defaultdict
import json
B=Path(__file__).resolve().parent;OUT=B/'revisao-r38'
TOP=(297-23)*72/25.4;BOT=36*72/25.4;CAP=TOP-BOT;MID=210/2*72/25.4
for edition in ['r37','r38']:
 m=json.loads((B.parent/f'livro-diagramado-{edition}/FONTES-E-VALIDACAO.json').read_text());es=defaultdict(list)
 for e in m['eventos']:es[e['pagina']].append(e)
 chpages=defaultdict(list)
 for p in m['paginas_planejadas']:
  if p['tipo']!='cover':chpages[p['capitulo']].append(p['pagina'])
 rows=[]
 for p in m['paginas_planejadas']:
  n=p['pagina'];events=es[n];left=[e['y'] for e in events if e['x']<MID-1];right=[e['y'] for e in events if e['x']+e['largura']>MID+1]
  blank=[max(0,min(CAP,min(v)-BOT if v else CAP)) for v in [left,right]]
  edge=p['tipo']=='cover' or n in (min(chpages[p['capitulo']]),max(chpages[p['capitulo']]))
  rows.append({'pagina':n,'capitulo':p['capitulo'],'grupo':p['grupo'],'tipo':p['tipo'],'borda_capitulo':edge,'branco_esquerda':round(blank[0]/CAP,4),'branco_direita':round(blank[1]/CAP,4),'branco_medio':round(sum(blank)/2/CAP,4),'blocos':list(dict.fromkeys(e['bloco'] for e in events if e['bloco']))})
 body=[p for p in rows if p['tipo']=='content'];middle=[p for p in body if not p['borda_capitulo']]
 result={'paginas':m['paginas'],'sha256_pdf':m['sha256_pdf'],'altura_util_pt':CAP,'metodo':'Branco abaixo do último elemento de texto/tabela em cada metade da área útil. Elementos de largura inteira contam nas duas metades. Inclui títulos/contextos; exclui capa, arte e modelos da soma de páginas de conteúdo. Para meio de capítulo, exclui primeira e última página após a capa de cada capítulo.','branco_equivalente':round(sum(p['branco_medio'] for p in body),2),'branco_meio_capitulo':round(sum(p['branco_medio'] for p in middle),2),'paginas_acima_terco':[p for p in middle if p['branco_medio']>1/3],'bordas_acima_terco':[p for p in body if p['borda_capitulo'] and p['branco_medio']>1/3],'alguma_coluna_acima_terco':[p for p in middle if max(p['branco_esquerda'],p['branco_direita'])>1/3],'todas':rows}
 (OUT/f'APROVEITAMENTO-{edition.upper()}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(edition,m['paginas'],result['branco_equivalente'],result['branco_meio_capitulo'],[(p['pagina'],p['branco_medio']) for p in result['paginas_acima_terco']])

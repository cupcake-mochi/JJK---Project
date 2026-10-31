from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];R=B/'revisao-r54';d=json.loads((R/'TEXTOS-TRABALHO.json').read_text());ops=[]
def rep(k,a,z,m):
 assert d[k].count(a)==1,(k,a)
 d[k]=d[k].replace(a,z);ops.append(dict(bloco=k,antes=a,depois=z,motivo=m,passada=3))
rep('origens--restricao-sem-energia','que reforça ataques desarmados com esforço','que acrescenta dano a ataques com arma ou desarmados e oferece vantagem em testes escolhidos','Conferir o resumo contra a entrada completa: o adicional não cobra esforço e também abrange armas.')
rep('ab--ab-kaori','ligada à cura e à proteção','ligada à cura e à vida temporária','Distinguir Amparo de Guarda, que pertence a Auxiliares.')
rep('dano--condicoes','(#catalogo--melhoria-concentrada)', '(#catalogo--melhoria-concentrada-duradoura)', 'Corrigir a remissão para a entrada conjunta de duração.')
rep('dano--condicoes','(#catalogo--melhoria-duradoura)', '(#catalogo--melhoria-concentrada-duradoura)', 'Corrigir a remissão para a entrada conjunta de duração.')
(R/'TEXTOS-TRABALHO.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'OPERACOES-PASSADA-3.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
base=json.loads((B.parent/'livro-diagramado-r53/revisao-r53/BLOCOS-R53.json').read_text());allops=[]
for n in (1,2,3):allops+=json.loads((R/f'OPERACOES-PASSADA-{n}.json').read_text())
rows=[]
for k in base:
 assert re.findall(r'^#+ .+',base[k],re.M)==re.findall(r'^#+ .+',d[k],re.M),k
 if base[k]!=d[k]:
  rows.append(dict(id=f'R54-{len(rows)+1:03d}',bloco=k,antes=base[k],depois=d[k],motivo=' '.join(dict.fromkeys(o['motivo'] for o in allops if o['bloco']==k)),item='Revisão de clareza e ordem de apresentação, 25/10/2026',altera_regras=False))
(B/'ALTERACOES-R53-para-R54.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
replay=dict(base)
for o in allops:
 assert replay[o['bloco']].count(o['antes'])==1
 replay[o['bloco']]=replay[o['bloco']].replace(o['antes'],o['depois'])
assert replay==d
print(len(allops),'operações,',len(rows),'blocos; reconstrução exata; títulos preservados')

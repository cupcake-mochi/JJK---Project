from pathlib import Path
import json,sys
B=Path(__file__).resolve().parents[1]; mode=sys.argv[1];D=B.with_name('livro-diagramado-r47') if mode=='base' else B
m=json.loads((D/'FONTES-E-VALIDACAO.json').read_text());rows=[e for e in m['eventos'] if not e['gerado']];heads={'h1','h2','h3','major','marker'}
report=[];heading=''
for i,e in enumerate(rows):
 if e['tipo'] in heads:heading=e['texto']
 if i==0:continue
 prev=rows[i-1]
 if e['pagina']==prev['pagina'] or e['bloco']!=prev['bloco'] or e['tipo'] in heads:continue
 tail=[]
 for q in rows[i:]:
  if q['bloco']!=e['bloco'] or q['tipo'] in heads:break
  tail.append(q)
 h=sum(q['altura']+4 for q in tail)
 fits=e['largura']==prev['largura'] and prev['y']-100>=e['altura']+4
 if len(tail)<=2 or fits:
  report.append({'de':prev['pagina'],'para':e['pagina'],'titulo':heading,'bloco':e['bloco'],'paragrafos_finais':len(tail),'altura_final':round(h,1),'primeiro_cabia_antes':fits,'livre_antes':round(prev['y']-100,1),'comeco':str(e['texto'])[:150]})
(B/'revisao-r48'/f'QUEBRAS-{mode.upper()}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(mode,'finais curtos ou parágrafo que cabia',len(report),'cabia',sum(r['primeiro_cabia_antes'] for r in report))
for r in report:print(r['de'],r['para'],r['titulo'],r['paragrafos_finais'],'CABIA' if r['primeiro_cabia_antes'] else '')

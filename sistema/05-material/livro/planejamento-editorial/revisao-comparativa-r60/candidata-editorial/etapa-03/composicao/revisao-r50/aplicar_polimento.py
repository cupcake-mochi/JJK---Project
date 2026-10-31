from pathlib import Path
import json,difflib
B=Path(__file__).resolve().parents[1]
base=json.loads((B/'revisao-r50/BLOCOS-R49.json').read_text())
rows=json.loads((B/'ALTERACOES-R49-para-R50.json').read_text())
current=dict(base);meta={r['bloco']:r for r in rows}
for r in rows:current[r['bloco']]=r['depois']
def edit(k,a,z,why):
 assert current[k].count(a)==1,(k,a)
 current[k]=current[k].replace(a,z)
 if k not in meta:meta[k]={'id':f'R50-{len(meta)+1:03}','bloco':k,'antes':base[k],'motivo':why,'item':'Revisão de compreensão e decisões anteriores do autor'}
 elif why not in meta[k]['motivo']:meta[k]['motivo']+=' '+why
 meta[k]['depois']=current[k]
draft=json.loads((B.parent/'rascunho-polimento-legados-sobre-r46-2026-10-13/ALTERACOES-R46-para-R47.json').read_text())
for r in draft:
 a=r['antes'].splitlines(keepends=True);z=r['depois'].splitlines(keepends=True)
 for tag,i,j,x,y in reversed(list(difflib.SequenceMatcher(None,a,z,autojunk=False).get_opcodes())):
  if tag=='equal':continue
  old=''.join(a[i:j]);new=''.join(z[x:y])
  if not old:
   start=i-1
   while start>0 and not a[start].strip():start-=1
   old=''.join(a[start:i]);new=old+new
  edit(r['bloco'],old,new,'Integrar o polimento de Legados e remissões já solicitado, preservado no rascunho sobre a R46; sem trocar as regras posteriores.')
edit('origens--feto-beneficios','Enquanto estiver exposto, você pode enxergar por ele, com **visão noturna a 9 m**.','Enquanto estiver exposto, você pode enxergar por ele. A até **9 m**, enxerga na penumbra e na escuridão comum sem a penalidade por falta de luz, mas não distingue cores no escuro. Os demais impedimentos de visão continuam valendo.','Aplicar a definição de visão noturna expressamente aprovada pelo autor e ainda pendente na R49.')
edit('dano--socorro','Sair de Morrendo não devolve ações, coloca você automaticamente de pé ou reabre um efeito que terminou na queda.','Sair de Morrendo não devolve ações, não coloca você automaticamente de pé nem reabre um efeito que terminou na queda.','Repetir a negação para evitar leitura ambígua, sem mudar o funcionamento.')
edit('origens--origem-feto','Não recupera Integridade, remove condições ou Sequelas, nem recompõe partes perdidas.','Não recupera Integridade, não remove condições ou Sequelas nem recompõe partes perdidas.','Repetir a negação para evitar leitura ambígua, sem mudar o funcionamento.')
edit('origens--origem-receptaculo','Amparo não encerra Inconsciente, recupera reservas ou devolve ações gastas ou perdidas em turnos anteriores.','Amparo não encerra Inconsciente, não recupera reservas nem devolve ações gastas ou perdidas em turnos anteriores.','Repetir a negação para evitar leitura ambígua, sem mudar o funcionamento.')
edit('dano--cura','Um efeito que ignore o limiar normal de recuperação','Um efeito que dispense o tratamento necessário para sair de Morrendo','Uniformizar a remissão ao tratamento de Morrendo, sem mudar os limites da fonte de cura.')
edit('dano--temporarios','não encerra Insistir e não conta como tratamento.','não encerra Morrendo e não conta como tratamento.','Nomear a condição para deixar claro que vida temporária não a encerra em nenhuma das duas escolhas.')
(B/'ALTERACOES-R49-para-R50.json').write_text(json.dumps(list(meta.values()),ensure_ascii=False,indent=2)+'\n')
(B/'revisao-r50/BLOCOS-ESPERADOS.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
p=B/'revisao-r45/CLASSIFICACAO.json';j=json.loads(p.read_text());r=dict(next(r for r in j if r['bloco']=='dano--socorro' and r['titulo']=='Estabilizar'))
r.update(titulo='Resgates expressos',motivo='R50: subtópico novo de Socorro com o mesmo tratamento B dos demais detalhes.');r.pop('pagina_r34',None)
j.append(r);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(len(meta),'blocos finais, incluindo integração e compreensão')

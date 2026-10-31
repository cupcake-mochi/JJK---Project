from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];R=B/'revisao-r41';base=json.loads((R/'BASE-BLOCOS.json').read_text());rows=[]
def change(key,subs,why,item):
 old=base[key];new=old
 for a,b in subs:
  assert new.count(a)==1,(key,a,new.count(a))
  new=new.replace(a,b,1)
 rows.append({'id':f'R41-T{len(rows)+1:03d}','bloco':key,'antes':old,'depois':new,'motivo':why,'item':item})
change('evocador--evocador',[("| 7 | Atuação Complementar. |","| 7 | Dificultar a Resistência, Ajustar a Preparação, Recolher sob Ataque e Atuação Complementar. |")],'Completar a linha do nível 7 com as quatro capacidades já concedidas pelo texto.','Evocador 1')
change('evocador--ev-principal-protecao',[("## Intervenções da principal","## Intervenções da Invocação Principal")],'Usar no título o mesmo nome completo presente na tabela de progressão.','Evocador 2')
change('evocador--ev-multiplas-protecao',[("## Proteção do conjunto","## Intervenções do Conjunto")],'Usar no título o mesmo nome presente na tabela; o grupo contém quatro intervenções.','Evocador 2')
change('rotas--rota-bencaos',[("| Represália | 2 | Destreza 4. |","| Represália | 2 | Força 4 ou Destreza 4. |")],'Atualizar o requisito da Represália na tabela Escolhas disponíveis. Basta um dos dois atributos.','Bênçãos 2')
change('rotas--rota-combate',[
 ("**Requisito adicional: Destreza 4.** Quando uma criatura","**Requisito adicional: Força 4 ou Destreza 4.** Fora do seu turno, quando uma criatura"),
 ("Manter um efeito já ativo não oferece um novo gatilho.","Manter um efeito já ativo não oferece um novo gatilho.\n\nAbrir ou manter uma Expansão de Domínio e o Acerto de uma Expansão incompleta não ativam esta Bênção; feitiços conjurados dentro de um domínio continuam contando normalmente."),
 ("Mantenha a CD, os modificadores e a vantagem ou desvantagem aplicável.","Role um único d20, sem a vantagem desta Bênção, e mantenha a CD e os modificadores."),
 ("A repetição também exige que a criatura esteja a até 3 m.","A repetição também exige que a criatura esteja a até 3 m.\n\nA vantagem e a repetição não se aplicam à abertura ou manutenção de uma Expansão de Domínio, nem ao Acerto de uma Expansão incompleta; feitiços conjurados dentro de um domínio continuam contando normalmente.")
],'Aplicar exclusivamente os quatro acertos autorizados nas entradas Represália e Sangue Frio, preservando as demais Bênçãos.','Bênçãos 1, 2, 3 e 4')
for name in ['ALTERACOES-TEXTO.json','ALTERACOES-REGRAS.json']:(R/name).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'blocos registrados')

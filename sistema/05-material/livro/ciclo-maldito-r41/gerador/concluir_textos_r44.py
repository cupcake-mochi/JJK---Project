from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B/'revisao-r44'
base=json.loads((R/'BASE-BLOCOS-R43.json').read_text());rows=json.loads((R/'RASCUNHO-ALTERACOES.json').read_text())
def change(k,z,item,motivo):
 a=base.get(k,'');assert a!=z
 existing=next((r for r in rows if r['bloco']==k),None)
 if existing:existing.update(depois=z,item=item,motivo=motivo)
 else:rows.append({'id':f'R44-R{len(rows)+1:03d}','bloco':k,'antes':a,'depois':z,'motivo':motivo,'item':item})
def current(k):return next((r['depois'] for r in rows if r['bloco']==k),base.get(k,''))
def amend(k,a,z,item,motivo):
 s=current(k);assert s.count(a)==1,(k,a);change(k,s.replace(a,z,1),item,motivo)
amend('construcao--entidades-tipos','Criadas e domadas mantêm seus níveis, mesmo que você avance na campanha.','A criada acompanha o nível do invocador até o último nível da Classe dela; passar à Classe seguinte exige reconstrução. A domada mantém o nível em que foi domada.','189','Frase adicional identificada na auditoria e autorizada pelo autor: distinguir a evolução da criada do nível fixo da domada.')
amend('construcao--entidades-progressao','Isso não concede níveis de evolução a uma domada ou criada depois da aquisição.','A domada conserva o nível em que foi domada. A criada acompanha o nível do invocador até o último nível da Classe dela; passar à Classe seguinte exige reconstrução.','189','Frase adicional identificada na auditoria e autorizada pelo autor: atualizar a evolução após a aquisição sem alterar a progressão ou a domada.')
amend('ritual--pactos','| Temporário | No seu turno, como Ação Bônus ou Reação. | Benefício até o fim da cena. A perda segue o acordo. |','| Temporário | No seu turno, com Ação Bônus; fora dele, com Reação a um gatilho percebido. | Benefício até o fim da cena. A perda segue o acordo. |','151, 192','Acrescentar a régua do ganho e atualizar a linha Temporário para Ação Bônus no próprio turno ou Reação fora dele, conforme nova decisão do autor.')
amend('ritual--pacto-temporario','No seu turno, use **Ação Bônus ou Reação** para propor e firmar um pacto temporário aprovado pelo mestre. Declare a perda, o benefício e o prazo antes de resolver a ação que pretende melhorar. Gastar Reação aqui não permite agir fora do turno nem alterar uma rolagem já resolvida.','No seu turno, use **Ação Bônus** para propor e firmar um pacto temporário. **Fora do seu turno, use Reação em resposta a um gatilho que perceba:** um ataque recebido, uma ação do inimigo ou outro evento. O gatilho é obrigatório. Declare a perda, o benefício e o prazo; o mestre precisa aprovar a troca na hora.\n\nA Reação responde ao gatilho **depois de os dados dele serem rolados e antes de as consequências serem aplicadas**, como a Reação de Cobrir-se de Energia. O pacto não refaz nem muda uma rolagem: muda o que acontece a partir dali.','191, 192','Explicitar ganho temporário e perda possivelmente permanente, sem vaga; permitir Ação Bônus no próprio turno e Reação fora dele, depois dos dados e antes das consequências, preservando os demais limites e Mei.')
change('ritual--pacto-exemplos','''## Exemplos de pacto

Os exemplos mostram o que se entrega e o que se recebe. Nos cinco primeiros, o tamanho do ganho segue a régua do câmbio. Nas Promessas, a troca é entre duas partes: cada uma entrega o que ficou escrito no acordo.

### 1. Sukuna: o corte que parte o mundo

**Forma: temporário. Ganho: Enorme.**

**Dá:** daí em diante, aquele feitiço exige o gesto com as duas mãos, a recitação e apontar a direção. Essas exigências são permanentes e não devolvem pontos.

**Recebe:** lançar aquele feitiço uma vez, na hora, sem cumprir o Selo nem as Restrições dele naquela conjuração. É um ganho temporário pago com uma perda permanente.

### 2. Hakari: o braço

**Forma: temporário. Ganho: Enorme.**

**Dá:** a proteção de um braço, que perde de forma permanente, como consequência combinada com o mestre.

**Recebe:** quando um golpe o levaria a zero de vida, gasta sua **Reação**, depois dos dados e antes das consequências, para ficar com **1 de vida**. O benefício vale para aquele golpe; o mestre aprova o pacto na hora.

### 3. Mostrar a mão

**Forma: temporário. Ganho: Pequeno.**

**Dá:** com a **Ação Bônus** do pacto temporário, você explica sua técnica a uma criatura que ouve e entende. A informação precisa ser **nova e verdadeira**.

**Recebe:** no turno da revelação, suas rolagens de acerto dos feitiços daquela técnica contra ela têm **vantagem**, e os TRs dela contra esses feitiços têm **desvantagem**. Feitiços Automáticos não mudam.

Conte os turnos de quem revelou: **no turno seguinte, tudo normal**; no terceiro, a troca se inverte a favor dela, com **desvantagem nas rolagens de acerto desses feitiços e vantagem nos TRs dela** contra eles. Depois acaba.

### 4. Nanami: Overtime

**Forma: permanente, pacto de energia. Ocupa vaga. Ganho: Grande.**

Combine com o mestre uma **jornada em horas de trabalho**, na criação do pacto. Essa jornada fica fixa e não muda depois. O percentual é **2,5% por hora**: 4 horas dão 10%; 8 horas, a jornada normal, dão 20%; 12 horas dão 30%.

**Dá:** durante a jornada, seu **PE máximo** conta esse percentual a menos. No começo do dia de missões, você está com o máximo reduzido.

**Recebe:** passada a jornada, na hora extra, seu PE máximo conta esse percentual a mais. Ao entrar na hora extra, receba imediatamente **a diferença entre os dois máximos**. Arredonde para baixo.

A jornada conta a partir do começo das missões do dia, a qualquer hora do relógio. O **descanso curto não conta como hora de trabalho**. O **descanso longo encerra a hora extra e zera a contagem**, que recomeça na jornada seguinte.

Com PE máximo 40 e jornada de 8 horas, seu máximo é **32 durante a jornada** e **48 na hora extra**. Ao passar de um para o outro, você recebe **16 PE**, a diferença entre os máximos.

### 5. Movimento direcional

**Forma: permanente. Ocupa vaga. Ganho: Médio.**

**Dá:** você só se desloca em linha reta, até gastar os metros ou bater em alguma coisa, sem curva e sem parar no meio.

**Recebe:** esse movimento não provoca ataque de oportunidade.

### 6. Mahito e Mechamaru

**Forma: Promessa.**

**Mechamaru dá informação e recebe a cura do corpo. Mahito entrega a cura e recebe a informação.** Mechamaru acrescenta uma cláusula ao acordo: **ninguém de Kyoto seria tocado**.

### 7. Sukuna e Itadori

**Forma: Promessa.**

**Itadori dá um minuto do próprio corpo e recebe a volta à vida. Sukuna devolve sua vida e recebe esse minuto**, cobrado quando quiser, com a condição de **não ferir ninguém durante ele**.

### 8. Yuta e os superiores

**Forma: Promessa.**

**Yuta dá o juramento de executar Itadori e recebe o posto de carrasco. Os superiores entregam o posto e recebem esse compromisso.** A outra parte é uma instituição.

### 9. Kenjaku e os feiticeiros antigos

**Forma: Promessa.**

**Os feiticeiros antigos deixam de viver e se tornam objetos amaldiçoados; recebem a garantia de voltar no futuro. Kenjaku recebe os feiticeiros nessa forma e garante sua volta.** É uma Promessa que dura mais que a vida de quem fechou.''','40, 151, 191, 192','Inserir os nove exemplos autorizados: tamanho apenas nos cinco pactos, troca de ambas as partes nas quatro Promessas, ganho temporário com preço permanente e gatilho reativo de Hakari.')
# A ordem do registro acompanha a do texto publicado; o bloco novo vem após Pactos na criação.
order=list(base);order.insert(order.index('ritual--pacto-restricao')+1,'ritual--pacto-exemplos')
rows.sort(key=lambda r:order.index(r['bloco']))
for i,r in enumerate(rows,1):r['id']=f'R44-R{i:03d}'
(B/'ALTERACOES-R43-para-R44.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
# Atualizar só o destaque cujo exemplo precisou acompanhar a nova escolha de Classe.
p=B/'DESTAQUES-CATALOGO.json';catalog=json.loads((B.parent/'livro-diagramado-r43'/'DESTAQUES-CATALOGO.json').read_text());changes=[]
for row in rows:
 a=[l[2:] for l in row['antes'].splitlines() if l.startswith('> ')];z=[l[2:] for l in row['depois'].splitlines() if l.startswith('> ')]
 if a==z:continue
 if not row['depois']:continue
 for old,new in zip(a,z):
  if old==new:continue
  entry=next(v for v in catalog if v['bloco']==row['bloco'] and v['texto']==old)
  before=dict(entry);entry['texto']=new;entry['palavras']=len(new.split());changes.append({'antes':before,'depois':dict(entry),'motivo':'O exemplo da calígrafa explicita Classe escolhida e nível do futuro invocador; CDs e resultados mínimos preservados.'})
p.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
(R/'REFERENCIAS-DE-EXEMPLOS.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'blocos registrados; itens:',sorted({int(n.strip()) for r in rows for n in r['item'].split(',')}));print('Destaques ajustados:',len(changes))

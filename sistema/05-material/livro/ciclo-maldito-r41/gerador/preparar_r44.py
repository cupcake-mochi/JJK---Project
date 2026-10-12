from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r44'
base=json.loads((R/'BASE-BLOCOS-R43.json').read_text());textos=dict(base);rows=[]
def change(k,z,item,motivo):
 a=base.get(k,'');assert a!=z,k
 textos[k]=z
 rows.append({'id':f'R44-R{len(rows)+1:03d}','bloco':k,'antes':a,'depois':z,'motivo':motivo,'item':item})
def repl(k,a,z):
 assert textos[k].count(a)==1,(k,a[:90],textos[k].count(a))
 textos[k]=textos[k].replace(a,z,1)
def done(k,item,motivo):change(k,textos[k],item,motivo)
# Reparo: somente a escolha do ofício e as parcelas autorizadas.
k='origens--origem-corpo'
a='**Perícia da Origem:** escolha Atletismo, Percepção, Ocultismo ou Intimidação. **Criação:** Técnica Marcial, em Rotas de criação.'
repl(k,a,a+' Na criação do personagem, escolha também o **ofício compatível com seu corpo** e anote-o na ficha, conforme Reparo do corpo.')
done(k,'188','Registrar a escolha do ofício compatível na criação do personagem Corpo Amaldiçoado, conforme esclarecimento do autor.')
for k in ['origens--origem-reparo','campo--inv-reparo']:
 repl(k,'**Entalhador ou Forja**','**ofício compatível com o corpo, anotado na ficha**')
 ls=textos[k].splitlines();out=[];inside=False
 for l in ls:
  if l.startswith('| Classe do '):
   out.extend(['| Classe do corpo em relação a quem repara | Dificuldade | Ajuste | No sucesso recupera |','|---|---|---|---|','| Igual | Difícil | 0 | Metade da vida máxima. |','| Uma abaixo | Média | −2 | Metade da vida máxima. |','| Duas ou mais abaixo | Fácil | −4 | Metade da vida máxima. |','| Uma acima | Difícil | 0 | Um terço da vida máxima. |','| Duas ou mais acima | Difícil | 0 | Um quarto da vida máxima. |']);inside=True
  elif inside and l.startswith('|'):continue
  else:inside=False;out.append(l)
 textos[k]='\n'.join(out)
 if k.startswith('origens'):
  repl(k,'No sucesso, recupere **metade da vida máxima**, arredondada para baixo, sem ultrapassar o máximo.','No sucesso, recupere a parcela de vida máxima indicada na tabela, **arredondada para baixo**, sem ultrapassar o máximo.')
  a='Há **uma tentativa por corpo a cada descanso curto**, mesmo que mais de uma pessoa possa reparar.'
  repl(k,a,a+'\n\nO ofício é escolhido na criação do personagem e fica registrado na ficha. Por exemplo, Entalhador pode atender a madeira, pedra ou osso; Forja, a metal; Alfaiate, a pano. A escolha depende do corpo, sem uma lista fechada de materiais.')
 else:
  repl(k,'Sucesso recupera metade da vida máxima, para baixo, sem ultrapassar o máximo.','Sucesso recupera a parcela da tabela, arredondada para baixo, sem ultrapassar o máximo.')
 done(k,'24, 188','Usar o ofício compatível registrado e permitir reparo de corpos de Classe superior, com um terço ou um quarto da vida máxima. Preservar o exemplo e os demais limites de reparo.')
k='dano--socorro';repl(k,'Para um corpo construído, use Entalhador ou Forja em lugar de Medicina.','Para um corpo construído, use o ofício compatível com o corpo em lugar de Medicina.');done(k,'188','Trocar apenas o ofício usado para estabilizar um corpo construído, sem mudar Morte, Integridade ou socorro.')
k='construcao--entidades-criar'
a='6. **Registro.** Anote custos, alcances, requisitos e comunicação. Confira a ficha antes de levá-la à sessão.'
repl(k,a,a+'\n\nToda entidade de criação, em talismã ou corpo, e todo corpo amaldiçoado registra na ficha o campo **ofício compatível**, escolhido na criação. A escolha depende do trabalho e dos materiais: Entalhador para madeira, pedra ou osso; Forja para metal; Alfaiate para pano; Caligrafia para o talismã de um shikigami de criação são exemplos, não uma lista fechada. Nos shikigamis de criação, o campo serve ao teste de criação; só corpos recuperam vida por reparo.')
done(k,'188','Acrescentar o campo ofício compatível às fichas indicadas, com exemplos abertos e distinção entre criação de shikigami e reparo de corpo.')
# Aquisição e seção de criação.
k='construcao--entidades-aquisicao';repl(k,'| Criação | Tempo, testes e materiais de fabricação. | Conserva o nível em que foi criada. |','| Criação | Teste de criação, quando o mestre permitir. | Acompanha seu nível até o último nível da Classe dela; passar disso pede reconstruir. |');done(k,'33, 189','Atualizar a linha Criação com o investimento e a evolução definidos pelo autor.')
k='construcao--entidades-lista-criacao'
repl(k,'Shikigamis de criação ficam ligados a talismãs. Corpos amaldiçoados de criação são construídos com peças. Ambos dependem de tempo, testes e materiais, conforme **Fabricação de entidades**. Caligrafia é o ofício dos talismãs. Entalhador ou Forja atende aos corpos, conforme o material e o trabalho.','Shikigamis de criação ficam ligados a talismãs. Corpos amaldiçoados de criação são construídos com peças. Ambos usam o ofício compatível registrado na ficha, conforme [Criação de entidades](#fabricacao--fab-entidades). O mestre decide quando podem ser criados e o custo em tempo e materiais.')
repl(k,'Registre o nível e a ficha resultantes da fabricação. Subir de nível com o invocador não melhora automaticamente essa criatura.','Registre a Classe e a ficha da entidade. Ela acompanha o nível do invocador até o último nível da sua Classe; passar à Classe seguinte exige reconstruí-la.')
done(k,'33, 188, 189','Adequar o ofício, a remissão e a evolução da aquisição por criação, preservando a lista de ritual e a independência de técnica de invocação.')
k='campo--inv-morte';repl(k,'Herdar um talismã ou corpo criado depende das regras de aquisição e criação, sem transferir automaticamente o vínculo.','Herdar um talismã ou corpo criado segue [Transferência e herança](#fabricacao--fab-conclusao), em Criação de entidades, sem transferir automaticamente o vínculo.');done(k,'33, 189','Apontar a herança para o procedimento atualizado, sem mudar as regras de morte.')
change('fabricacao--fab-entidades','''# Criação de entidades

Você pode criar um talismã que guarda um shikigami ou construir um corpo amaldiçoado. Escolha a entidade e prepare sua ficha em **Criar uma invocação**. Criar é uma aquisição: **não exige técnica de invocação nem ocupa espaço conhecido**.

O mestre decide quando você pode criar e o que isso custa em tempo e materiais; o livro de mestres vai tratar dessas decisões.

Uma pessoa **treinada no ofício compatível registrado na ficha** conduz o trabalho e faz o teste. Pode criar para si ou para outro invocador, definido antes do teste. **Cada entidade pede a própria tentativa.**

Na criação, escolha a **Classe da entidade**. Ela não pode superar a Classe de quem cria nem a do invocador. O nível da entidade é o do invocador, limitado ao último nível da Classe escolhida.''','33, 188, 189','Enxugar a abertura, substituir o ofício fixo e os requisitos de projeto pelos critérios autorizados, e definir a Classe escolhida e o nível inicial.')
change('fabricacao--fab-projeto','','33','Remover Projeto de fabricação, Materiais e custo e Prazo, conforme pedido expresso; tempo e materiais passam à decisão do mestre.')
change('fabricacao--fab-teste','''## Teste de criação

Quando o mestre permitir a criação e o trabalho combinado estiver cumprido, o responsável faz **um teste do ofício compatível**.

Use o atributo adequado ao trabalho e a Maestria do responsável. A base da dificuldade é **8 + esse atributo + essa Maestria**. Compare a Classe escolhida para a entidade com a Classe de quem cria, usando a Progressão da entidade.

| Classe da entidade em relação a quem cria | Dificuldade | Ajuste |
|---|---|---|
| Igual | Difícil | 0 |
| Uma abaixo | Média | −2 |
| Duas ou mais abaixo | Fácil | −4 |

**Role d20 + atributo + Maestria.** Igualar a CD é sucesso. Especialização e outros modificadores alteram o teste conforme suas próprias regras; não entram novamente na base da CD.

> **Exemplo:** uma calígrafa de nível 13, Destreza 4 e Maestria 2 cria uma entidade de Classe 3 para um invocador de nível 9. A entidade começa no nível 9. As Classes comparadas são 4 e 3: a dificuldade é Média. A CD fica **8 + 4 + 2 − 2 = 12**. Seu teste é d20 + 6; um 6 no dado basta. Se criasse uma entidade de Classe 4 para um invocador de nível 13, ela começaria no nível 13, a CD seria 14 e precisaria de 8.

### Vantagem nos testes

Nos testes para **criar, reconstruir ou transferir**, a vantagem só pode vir de **um ajudante treinado no ofício compatível**, com permissão do mestre e dedicando o mesmo tempo que o responsável, ou de **uma habilidade que conceda vantagem permanente nesse teste**. Vantagem ativada, por cena ou temporária não vale. Esta é uma exceção ao Ajudar de Regras gerais, que não exige treino do ajudante.

A vantagem da tentativa seguinte a uma falha vem da própria regra e continua valendo nos três testes.

### Sucesso e falha

No sucesso, conclua a entidade com a ficha combinada e registre seu invocador. Na falha, ela ainda não funciona. Uma nova tentativa acontece quando o mestre permitir e tem vantagem.''','33, 189, 190','Preservar a conta de criação, restringir as fontes de vantagem e substituir retrabalho por nova tentativa permitida pelo mestre. Adequar o exemplo da calígrafa sem mudar CD 12, CD 14 ou os resultados mínimos.')
change('fabricacao--fab-conclusao','''## Conclusão, evolução e transferência

Uma entidade nova começa com a **vida máxima**. O shikigami fica recolhido em seu talismã, **sem carga**; o corpo permanece inativo onde foi construído. O talismã ocupa **0,5 de Volume**. Manifestar, ativar, transportar e controlar a entidade seguem **Invocações em campo**.

### Evolução e reconstrução

A entidade de criação **acompanha o nível do invocador até o último nível da Classe dela**. As faixas da Progressão da entidade são: Classe 1, níveis 1–4; Classe 2, 5–8; Classe 3, 9–12; Classe 4, 13–16; Classe 5, 17–20; Classe 6, 21–25; e Classe 7, 26–30.

Para passar à Classe seguinte, é preciso **reconstruir a entidade** ou criar outra do zero. Reconstruir usa o mesmo teste de criação, comparando a **nova Classe** com a de quem reconstrói, e reduz a dificuldade em um degrau: Igual vira **Média (−2)**; Uma abaixo vira **Fácil (−4)**; Duas ou mais abaixo continua **Fácil (−4)**. A nova Classe não pode superar a de quem reconstrói nem a do invocador. **É um teste por Classe.**

Na falha, a entidade continua onde está. A nova tentativa acontece quando o mestre permitir e tem vantagem.

### Transferência e herança

Passar um talismã ou corpo criado a outro invocador, ou herdá-lo, pede **o mesmo teste de criação, fora de combate**, com o consentimento do dono anterior ou a morte dele. O novo invocador precisa ter **Classe igual ou maior que a da entidade**.

No sucesso, registre o novo invocador. A transferência conserva **Classe, ficha, vida atual e usos gastos**, além da queda e da carga do talismã. Depois dela, a entidade acompanha o nível do novo invocador dentro da Classe dela; atualize os valores que dependem dele. A transferência não recupera energia, não concede outra atuação no ciclo nem religa um corpo Desligado.

Na falha, o vínculo anterior permanece, ou o objeto continua sem invocador vivo, conforme o caso. A nova tentativa acontece quando o mestre permitir e tem vantagem.

**Uma entidade destruída exige criar outra.** A maldição domada conserva o nível em que foi domada; esta evolução pertence às entidades de criação.''','33, 189, 190','Enxugar conclusão e transferência; estabelecer evolução dentro da Classe, reconstrução por Classe e vantagem depois de falha, conservando vida atual e recursos da transferência.')
change('fabricacao--fab-exemplo','','33','Retirar integralmente Exemplo: Talismã de vigia, inclusive projeto, preços, prazos e retrabalho.')
# Pactos.
k='ritual--pactos'
textos[k]+='''

### Régua do câmbio

A régua mede **o ganho**; o preço acompanha. Ela é uma referência para o mestre aprovar ou negar um pacto, não uma tabela de conversão entre sacrifícios e resultados.

| Tamanho | O que o pacto entrega |
|---|---|
| Pequeno | Muda uma conjuração, ou vale uma cena. |
| Médio | Muda de forma permanente como um feitiço ou uma ação sua funciona. |
| Grande | Muda de forma permanente como a sua energia ou um Estilo inteiro funciona. |
| Enorme | Quebra um limite do sistema, uma vez. |

Promessa pequena, ganho pequeno; quem arrisca a vida pode pedir um ganho enorme.'''
done(k,'151','Acrescentar a régua do ganho como referência de aprovação, preservando Preço real e a proibição de converter qualquer sacrifício em qualquer resultado.')
k='ritual--pacto-permanente';repl(k,'O Overtime é o modelo dessa troca.','O [exemplo 4, Nanami e Overtime](#ritual--pacto-exemplos), mostra essa troca.');done(k,'40','Remeter ao exemplo numérico de Overtime, conservando vagas, restrições a bônus e pacto de energia.')
k='ritual--pacto-temporario'
repl(k,'O benefício termina, no máximo, **no fim da cena**. O preço pode durar mais: energia gasta não volta ao encerrar o combate e um ferimento não se cura apenas porque o prazo do benefício acabou.','O pacto temporário dá um **ganho temporário** e pode cobrar uma **perda permanente**. Combine separadamente o prazo do benefício e o prazo do preço. O benefício termina, no máximo, **no fim da cena**; o preço pode durar para sempre. **Pacto temporário nunca ocupa vaga**, mesmo com preço permanente. Energia gasta não volta ao encerrar o combate e um ferimento não se cura apenas porque o prazo do benefício acabou. O [exemplo 1, o corte de Sukuna](#ritual--pacto-exemplos), mostra essa troca.')
done(k,'191','Explicitar ganho temporário, preço possivelmente permanente, prazos separados e ausência de vaga, preservando o exemplo de Mei e os limites gerais.')
k='ritual--pacto-restricao';repl(k,'| Movimento direcional | Como o deslocamento lida com obstáculos, interrupções e apoio? |\n','');done(k,'40','Retirar só Movimento direcional da tabela de ideias, pois passa a exemplo pronto; preservar as outras sete linhas.')
# Ritual: duas tabelas formam as dezesseis entradas.
for k in ['ritual--rit-melhorias','ritual--rit-beneficios']:
 if k.endswith('rit-melhorias'):
  repl(k,'Você pode escolher uma vez cada entrada, salvo Acerto e Dificuldade, que permitem duas compras.','Acerto, Dificuldade, Alcance, Tamanho e Rerrolagem permitem **até duas compras cada**. As outras onze entradas só podem ser escolhidas uma vez.')
 ls=[]
 for l in textos[k].splitlines():
  if l=='| Melhoria | Benefício | Pontos |':l='| Melhoria | Benefício | Pontos | Repete |'
  elif l=='|---|---|---:|':l='|---|---|---:|---|'
  elif l.startswith('| Ritual de '):
   name=l.split('|')[1].strip();repeat=name in ['Ritual de Acerto','Ritual de Dificuldade','Ritual de Alcance','Ritual de Tamanho','Ritual de Rerrolagem']
   l=l+(' Sim, até 2. |' if repeat else ' Não. |')
  ls.append(l)
 textos[k]='\n'.join(ls)
 if k.endswith('rit-melhorias'):
  repl(k,'**Rerrolagem:** fica o segundo resultado.','**Rerrolagem:** fica o segundo resultado. Com duas compras, rerrole também os dados que caírem um ponto acima do mínimo, como o 1 e o 2 de um d8, até **2 × (Classe + 1) dados**.\n\n**Alcance e Tamanho:** duas compras sobem **dois degraus** nas respectivas escalas.')
 done(k,'46','Adicionar Repete às dezesseis Melhorias de Ritual e autorizar duas compras nas cinco indicadas, com efeitos cumulativos definidos; preservar preços e a regra de Defesa.')
# Cortina.
k='aptidoes--apt-cortina'
repl(k,'**O ponto mais distante da borda deve estar a até 90 m de você ao concluir.** Essa medida limita a Cortina inteira, não cada trecho isolado.','**Ao concluir, a distância de você até o ponto mais distante da borda não pode ultrapassar o teto do seu Refino.** O lugar e as bordas continuam definidos pela descrição; a medida limita a Cortina inteira, não cada trecho isolado.\n\n| Refino | O que cobre | De você até o ponto mais distante da borda |\n|---|---|---|\n| 1 a 3 | Uma escola inteira, um hospital, um prédio com o terreno. | Até 150 m. |\n| 4 a 6 | Um quarteirão. | Até 300 m. |\n| 7 ou mais | O entorno de uma estação, um bairro pequeno. | Até 400 m. |')
done(k,'101','Substituir o teto fixo de 90 m pelas três faixas de Refino, mantendo vida, preparação, condições e exemplo de Haru.')
# Índice: mover o assunto de F para C, conservando sua âncora.
old='[Fabricação de entidades](#fabricacao--fab-entidades)';new='[Criação de entidades](#fabricacao--fab-entidades)'
k=next(k for k,t in textos.items() if k.startswith('consulta--consulta-indice') and old in t)
repl(k,old+'\n','');done(k,'33','Retirar a entrada antiga Fabricação de entidades do índice após a mudança do nome da seção.')
k=next(k for k,t in textos.items() if k.startswith('consulta--consulta-indice') and '[Crítico]' in t)
ls=textos[k].splitlines();i=next(i for i,l in enumerate(ls) if l.startswith('[Crítico]'));ls.insert(i,new);textos[k]='\n'.join(ls);done(k,'33','Inserir Criação de entidades no índice em C, apontando para a seção atualizada.')
(R/'RASCUNHO-ALTERACOES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'blocos preparados; exemplos de pacto e frases externas aguardam integração das respostas.')

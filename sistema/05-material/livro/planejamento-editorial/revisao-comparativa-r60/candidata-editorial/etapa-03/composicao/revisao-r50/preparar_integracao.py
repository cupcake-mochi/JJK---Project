from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
b=json.loads((B/'revisao-r50/BLOCOS-R49.json').read_text()); out=dict(b); reasons={}
def setblock(k,v,why):
 out[k]=v.strip(); reasons[k]=why
def replace(k,a,z,why):
 assert a in out[k],(k,a)
 out[k]=out[k].replace(a,z); reasons[k]=why
setblock('dano--zero','''# Vida a zero

Ao chegar a **zero de vida**, você entra na condição **Morrendo**. Confira sua janela de socorro: se não restar nenhuma rodada, fica **Derrotado imediatamente**. Uma capacidade disparada pela queda só supera essa derrota se disser expressamente que pode fazê-lo.

Se ainda houver janela, resolva primeiro as capacidades disparadas pela própria queda. Se uma delas encerrar Morrendo, não precisa escolher; caso contrário, escolha **Aguentar** ou **Insistir**. Cura que não encerre Morrendo por uma permissão expressa entra no tratamento; confira se ela basta depois de definir sua escolha.

Estas regras são para personagens jogadores. Entidades seguem Invocações em campo. Um inimigo a zero de vida ou de Integridade é derrotado, e o mestre descreve o desfecho, como morte, fuga ou exorcismo, salvo uma regra da ficha dele.

Anote a vida máxima que tinha ao cair, sem vida temporária. Esse é o **máximo de referência** até aquela queda terminar. Registre também o tratamento necessário, o tratamento já recebido e sua janela de socorro.

| Escolha | Estado | Tratamento necessário |
|---|---|---|
| Aguentar | Fica Inconsciente e espera socorro. | 1/4 do máximo de referência, para cima, sem teto. |
| Insistir pela primeira vez na cena | Permanece consciente e conserva as ações e os recursos disponíveis. | 1/3 do máximo de referência, para cima, até 15 × sua maior Classe. |
| Insistir pela segunda vez ou mais na cena | Permanece consciente e conserva as ações e os recursos disponíveis. | 1/2 do máximo de referência, para cima, até 15 × sua maior Classe. |

As duas escolhas conservam sua vida máxima. Insistir não consome uma rodada como custo; o tempo e o dano continuam reduzindo a janela normalmente.

## Janela de socorro

A janela começa com **3 rodadas, menos 1 por Sequela que você já tenha**. As duas escolhas usam essa mesma janela. Com três ou mais Sequelas, você fica Derrotado imediatamente, conforme **Derrota e morte**.

Marque o ponto da iniciativa em que caiu. Cada volta completa até esse ponto consome uma rodada da janela. A janela não concede turnos extras e não muda a iniciativa. Quando chegar a zero, você fica Derrotado. Uma ação de socorro que só começaria naquele ponto não antecede o prazo já esgotado; capacidades com gatilho próprio conservam seu momento de resolução.

Se a queda ocorrer fora de combate, organize turnos pelas regras de Iniciativa para resolver o socorro. Marque o começo dessa primeira rodada como ponto da queda. A primeira volta completa consome uma rodada da janela; uma tentativa de atendimento segue seus custos normais.

Cada **ocorrência posterior de dano** que alcance sua vida consome mais **uma rodada da janela**, depois das defesas e da vida temporária. Um mesmo golpe com vários tipos de dano conta uma vez. Ataques distintos contam separadamente. Dano reduzido a zero ou totalmente absorvido pela vida temporária não consome uma rodada.

O golpe que levou sua vida a zero inicia a queda. Seu excesso não consome outra rodada. **Dano posterior não desconta tratamento acumulado nem aumenta o tratamento necessário.** Isso vale tanto para Aguentar quanto para Insistir.

> **Exemplo:** você precisa de 31 de tratamento e já recebeu 18. Tem duas rodadas restantes. Sofre 7 de dano depois das proteções: conserva os 18 de tratamento e passa a ter uma rodada. Ainda faltam 13 de tratamento, mas há menos tempo para recebê-los.

## Aguentar

Você fica Inconsciente. Pode receber cura ou ser estabilizado conforme **Socorro**, mas não age para se proteger ou tratar os próprios ferimentos.

Escolher Aguentar não permite mudar para Insistir mais tarde naquela queda. Se já estava Inconsciente antes de perder o último ponto de vida, você Aguenta. Insistir não remove outra causa de inconsciência.''','Integrar condição própria, escolhas, tratamento, dano e prioridade da derrota com Sequelas esgotadas; substituir o exemplo pelo tratamento e prazo aprovados.')
setblock('dano--insistir','''## Insistir

Ao escolher Insistir, você continua a zero de vida e conserva as ações, os recursos e as respostas que ainda puder usar. A escolha não devolve uma ação já gasta nem encerra outras condições. Pode tratar a si mesmo enquanto conseguir agir e cumprir os requisitos da fonte.

Conte **uma escolha de Insistir por queda**. Continuar agindo ou sofrer dano nessa mesma queda não aumenta a contagem. Uma queda em que escolha Aguentar não aumenta nem zera essa contagem. Na próxima cena, a contagem de Insistir volta a zero; as Sequelas e os recursos gastos conservam seus próprios prazos.

Na primeira escolha de Insistir da cena, o tratamento necessário é **1/3 do máximo de referência**. Na segunda e nas seguintes, é **1/2**. Arredonde para cima. Se o resultado superar **15 × sua maior Classe**, use esse teto. Esse limite não reduz sua vida máxima nem limita a quantidade de cura recebida.

Pode passar de Insistir para Aguentar **sem ação**. Fica Inconsciente, mas conserva o tratamento necessário definido na queda, o que já acumulou e o tempo restante. Não pode voltar a Insistir naquela ocorrência.

### Socorro durante Insistir

Acumule a cura conforme **Socorro**. Recuperar apenas 1 de vida não encerra essa queda, salvo uma capacidade com permissão expressa para encerrar Morrendo abaixo do tratamento necessário.

Quando a janela termina, você fica Derrotado. Não recebe uma segunda janela por desabar. Dano à vida enquanto Insiste também consome rodadas dessa janela.

> **Exemplo:** com máximo de referência 93 e maior Classe 3, Aguentar pede 24 de tratamento. A primeira escolha de Insistir na cena pede 31. Na segunda e nas seguintes, metade daria 47, mas o teto de 45 reduz a exigência para 45. Se escolher Insistir e depois desistir de agir, conserva o requisito daquela queda. Sua vida máxima permanece 93.

> **Exemplo do teto:** com máximo de referência 395 e maior Classe 7, Aguentar pede 99. O primeiro Insistir daria 132 e o segundo, 198; ambos ficam limitados a 105. Mesmo com a mesma exigência de tratamento, as Sequelas de quedas anteriores encurtam a janela de socorro. Sua vida máxima continua 395.''','Substituir a perda de vida máxima pelas frações e teto direto aprovados; registrar contagem por cena, persistência do requisito e exemplos recalculados.')
setblock('dano--socorro','''## Socorro

Uma pessoa Morrendo pode ser curada ou estabilizada antes de sua janela acabar. Vida temporária não conta como tratamento.

### Cura

Enquanto estiver Morrendo, sua vida permanece zero. Acumule separadamente toda **cura válida** recebida. Ela pode vir de várias fontes, pessoas e turnos, inclusive durante Insistir. Calcule a quantidade pelo efeito usado, com seus modificadores e impedimentos, antes de aplicar o limite da vida máxima.

Ao alcançar o tratamento necessário para sua escolha, encerre Morrendo e transforme **todo o tratamento acumulado em vida**, até o máximo atual. O requisito não é um custo subtraído dessa quantidade. O excesso sobre a vida máxima é perdido. A contagem daquela queda termina e você recebe uma Sequela.

A inconsciência causada apenas por Aguentar termina com esse socorro. Outras condições conservam suas regras. Sair de Morrendo não devolve ações, coloca você automaticamente de pé ou reabre um efeito que terminou na queda.

> **Exemplo:** Mei caiu com máximo 23 e escolheu Aguentar. Precisa de 6. Recebe 3 de cura e continua a zero. Outra cura de 3 completa 6: sai de Morrendo com 6 de vida e uma Sequela. Se tivesse escolhido Insistir pela primeira vez na cena, precisaria de 8 e ainda faltariam 2.

Cura insuficiente não renova o prazo nem devolve rodadas. Vida temporária protege contra dano, mas não conta como tratamento. Uma fonte impedida ou incompatível não entra no total. Uma capacidade que exige vida positiva, como Regeneração Orgânica, continua indisponível a zero.

### Resgates expressos

**Morrendo só termina pelo procedimento desta condição ou por uma capacidade que diga expressamente que permite encerrá-lo.** Remoção genérica de condições, incluindo Limpa Fundo, não substitui esse socorro. Morrendo não entra na lista de condições compráveis.

Uma capacidade que permita levantar abaixo do tratamento necessário, como **Levanta** ou **Ainda Há Tempo**, conserva essa permissão mesmo para quem escolheu Insistir. Use o valor de cura da capacidade, some o tratamento válido já recebido e aplique o máximo atual. A saída concede a Sequela normalmente.

Cada capacidade conserva alvos, alcance, ação, frequência, preparação e impedimentos próprios. Essa permissão não ressuscita alguém morto nem reabre participação na cena depois de Derrotado, salvo regra que diga isso expressamente.

### Estabilizar

Uma criatura a até **1,5 m**, com acesso físico ao alvo, pode gastar **Ação Padrão**, com uma mão livre e meios adequados de atendimento, para fazer **Medicina CD 14**. Para um corpo construído, use o ofício compatível com o corpo em lugar de Medicina, respeitando seus requisitos. O alvo precisa estar **Inconsciente e Morrendo**. Quem Insiste pode escolher Aguentar antes do atendimento, conservando seu requisito de tratamento.

No sucesso, a pessoa fica **estável**: o tempo deixa de diminuir a janela. Não recupera vida, não acorda, não reduz o requisito e conserva o tratamento acumulado e o prazo restante. Uma falha apenas gasta a ação. Outra tentativa é possível enquanto houver tempo.

Dano positivo que alcance a vida encerra a estabilidade e consome uma rodada. Marque esse novo ponto para retomar a contagem temporal com o prazo que restar. Estabilizar de novo não devolve rodadas.

Depois de sair do perigo, uma pessoa estável que conclua um descanso curto recupera **1 de vida** e encerra Morrendo, recebendo uma Sequela. Essa é uma saída excepcional, mesmo abaixo do tratamento necessário. Some o tratamento válido anterior a esse ponto de vida, até o máximo atual. Impedimentos de cura continuam valendo. Estabilizar, por si só, não é cura.''','Integrar acúmulo de tratamento, saída expressa, estabilização e recuperação segura; recalcular o exemplo da Mei.')
replace('dano--sequelas','inclusive com cura própria ou uma exceção ao limiar.','inclusive com cura própria, uma exceção ao tratamento necessário ou a recuperação segura depois de estabilizar.','Explicitar saídas que geram Sequela e a ordem aprovada do descanso longo.')
replace('dano--sequelas','Elas são removidas no descanso longo.','Elas são removidas no descanso longo: resolva primeiro a recuperação e registre a Sequela se ela encerrar a queda ou a derrota por vida a zero; depois, remova todas as Sequelas, inclusive essa.','Explicitar saídas que geram Sequela e a ordem aprovada do descanso longo.')
replace('dano--derrota','sem exigir o limiar de 20%.','sem exigir o tratamento necessário para sair de Morrendo.','Retirar o limiar antigo e aplicar a recuperação antes de remover Sequelas no descanso longo.')
replace('dano--derrota','Aplique a recuperação desse descanso, incluindo a remoção das Sequelas.','Resolva primeiro a recuperação, registrando a Sequela se essa derrota envolveu vida a zero; depois, remova todas as Sequelas, inclusive a recebida nessa recuperação.','Retirar o limiar antigo e aplicar a recuperação antes de remover Sequelas no descanso longo.')
replace('dano--descansos','| Sequelas e máximo perdido por Insistir | Sequelas são removidas; máximo é restaurado. | Sequelas são removidas; máximo é restaurado. |','| Sequelas | São removidas depois da recuperação. | São removidas depois da recuperação. |','Excluir recuperação da perda de máximo removida; explicitar a ordem do descanso longo.')
replace('dano--descansos','Restaure o máximo perdido por Insistir antes de calcular a vida recuperada. ','Resolva primeiro a recuperação. Se ela encerrar uma queda ou uma derrota por vida a zero, registre a Sequela correspondente; depois, remova todas as Sequelas, inclusive essa.\n\n','Excluir recuperação da perda de máximo removida; explicitar a ordem do descanso longo.')
replace('rotas--rota-passivas-resposta','''**Uma vez por descanso longo**, ao escolher **Insistir**, você pode dispensar o **primeiro custo de vida máxima**, correspondente a **1/8 do máximo de referência** daquela queda.

Os custos posteriores e a janela de socorro continuam normais. O Talento não concede rodada ou ação adicional nem recupera vida ou Integridade. A escolha, os pagamentos seguintes e o socorro seguem **Insistir, em Dano e recuperação**.''','''**Uma vez por descanso longo**, ao escolher **Insistir**, você pode usar **1/4 do máximo de referência**, arredondado para cima, como tratamento necessário naquela queda, em vez do requisito normal de Insistir. Anuncie nessa escolha. O uso continua contando como uma escolha de Insistir na cena. O requisito de 1/4 permanece até a queda terminar, mesmo que depois passe a Aguentar.

O Talento não recupera vida ou Integridade, não concede ação ou rodada adicional e não protege contra o agravamento por dano. Os demais procedimentos de **Morrendo, em Dano e recuperação**, continuam valendo.''','Aplicar a adaptação aprovada de Segundo Fôlego: requisito de 1/4, sem cura ou prazo adicional, mantendo categoria e frequência.')
replace('catalogo--cat-passivas-2-recursos','para recuperar **5 × sua maior Classe em pontos de vida**','para recuperar **3 × sua maior Classe em pontos de vida**','Aplicar a redução aprovada de Recomposição para 3 × a maior Classe, preservando custos e frequência.')
replace('catalogo--cat-amparo','O efeito não é uma imunidade nem remove todas as condições do aliado de uma vez.','O efeito não é uma imunidade nem remove todas as condições do aliado de uma vez. **Morrendo** exige seu próprio procedimento ou uma permissão expressa; Limpa Fundo não o encerra.','Explicitar a exclusão aprovada de Morrendo da remoção genérica e a saída expressa de Levanta.')
replace('catalogo--cat-amparo','e pode voltar a agir mesmo abaixo do limiar normal de recuperação.','e **encerra Morrendo** mesmo abaixo do tratamento necessário.','Explicitar a exclusão aprovada de Morrendo da remoção genérica e a saída expressa de Levanta.')
replace('guia--guia-emergencia-cuidado','esta cura encerra a queda mesmo abaixo do limiar normal de recuperação.','esta cura **encerra Morrendo** mesmo abaixo do tratamento necessário.','Conservar o resgate expresso de Ainda Há Tempo, sem autorizar retorno de Derrotado, usando os termos do procedimento novo.')
replace('consulta--consulta-glossario-4','Situação resolvida pelas regras de queda e recuperação em Vida a zero.','Condição de quem caiu a zero de vida, resolvida pelo tratamento e pela janela de socorro de Vida a zero.','Atualizar Morrendo como condição própria no glossário.')
rows=[{'id':f'R50-{i:03}','bloco':k,'antes':b[k],'depois':v,'motivo':reasons[k],'item':'Morrendo — decisões consolidadas v0.17'} for i,(k,v) in enumerate(((k,v) for k,v in out.items() if v!=b[k]),1)]
(B/'ALTERACOES-R49-para-R50.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'blocos registrados')

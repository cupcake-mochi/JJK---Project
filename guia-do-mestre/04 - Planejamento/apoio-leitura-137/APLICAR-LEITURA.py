"""Aplicar ajustes de leitura a partir das cópias preservadas do registro 136."""
from pathlib import Path
import json,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';log=[]
names=['01-sua-primeira-missao.md','02-o-mundo-dos-feiticeiros.md','03-preparar-aventuras.md','03a-ideias-para-aventuras.md']
states={n:(A/'antes'/T.relative_to(R)/n).read_text() for n in names}
def edit(name,before,after,why):
 s=states[name];assert s.count(before)==1,(name,before[:120],s.count(before));states[name]=s.replace(before,after,1)
 log.append({'fonte':str((T/name).relative_to(R)),'antes':before,'depois':after,'motivo':why})
name=names[0]
edit(name,'Antes de jogar, leia a missão inteira. Durante a sessão, use a planta, a ficha da ameaça e o resumo de preparo no final.', 'Antes de jogar, leia a missão inteira. Durante a sessão, tenha à mão a [planta do anexo](<#pessoas-e-lugar>), a [ficha do Amontoado](<#amontoado-do-deposito>) e o [resumo de preparo](<#as-batidas-no-anexo-preparo-para-consulta>).','Encontrar diretamente os três apoios de consulta anunciados na abertura.')
edit(name,'Uma figura de papelões dobrados e fitas, com duas pernas, dois braços e mãos articuladas. Acumula caixas e as move pelo chão.', 'Uma figura de papelões dobrados e fitas, com duas pernas, dois braços e mãos articuladas. Acumula caixas e as move pelo chão.\n\nPara conduzir o encontro, consulte os ataques, as defesas e o comportamento abaixo. A nota de montagem mostra como o feitiço foi criado; você pode voltar a ela quando quiser conferir essa criação.','Distinguir o uso imediato da ficha da explicação técnica de sua criação.')
edit(name,'### O que anotar quando alguém cai\n\n', '### O que anotar quando alguém cai\n\nAnote os campos abaixo junto da ficha. Se quiser uma folha para preenchê-los, use o [Registro de estado e socorro](<consultas/24-registro-de-estado-e-socorro.md#se-houver-queda-em-andamento>).\n\n','Oferecer a folha existente no momento em que o capítulo ensina o registro, sem copiar outro formulário.')
edit(name,'A Doma tem regras próprias; o capítulo de Pactos e entidades explica seu uso.', 'A Doma tem regras próprias; [Obter uma entidade](<09-pactos-e-entidades.md#94-obter-uma-entidade>) explica seu uso.','Transformar a menção ao capítulo em acesso direto à seção pertinente.')
name=names[1]
edit(name,'O capítulo Inimigos e perigos ensina esse trabalho.', '[Inimigos e perigos](<06-inimigos-e-perigos.md>) ensina esse trabalho.','Permitir consultar o preparo da ameaça a partir do capítulo de mundo.')
edit(name,'Uma criação que altere o funcionamento de uma capacidade segue a avaliação explicada em Personagens e técnicas.', 'Uma criação que altere o funcionamento de uma capacidade segue a avaliação explicada em [Personagens e técnicas](<07-personagens-e-tecnicas.md#74-avaliar-uma-capacidade>).','Levar ao assunto citado, sem exigir busca no capítulo inteiro.')
edit(name,'A recomendação do Guia é o mestre interpretá-la mediante acordo, com alternativas explicadas em Personagens e técnicas.', 'A recomendação do Guia é o mestre interpretá-la mediante acordo, com alternativas explicadas em [A outra voz do Receptáculo](<07-personagens-e-tecnicas.md#a-outra-voz-do-receptaculo>).','Aproximar o recorte de Origem de suas alternativas, preservando a escolha aprovada.')
name=names[2]
edit(name,'Para acompanhar a preparação de uma ameaça já pronta, volte a [Sua primeira missão](<01-sua-primeira-missao.md>).', 'Para acompanhar a preparação de uma ameaça já pronta, volte a [Sua primeira missão](<01-sua-primeira-missao.md>). Se já conhece o método e quer preparar a próxima sessão, vá a [Quando há pouco tempo](<#37-quando-ha-pouco-tempo>) e use a [folha curta de preparo](<consultas/A1-preparar-a-missao.md>).','Oferecer um caminho curto antes do catálogo de ideias, sem mudar a sequência dos métodos.')
edit(name,'A folha ao final do capítulo reúne o necessário para começar.', 'O [preparo reunido de Antes que o trem parta](<#antes-que-o-trem-parta>) mostra essas notas prontas para usar.','Atualizar a posição do exemplo e tornar explícito o que significa preparo preenchido.')
edit(name,'Se houver confronto com essa pessoa no preparo, acrescente sua ficha. Para conversar, as notas de interpretação podem bastar.', 'Se essa pessoa puder participar de um confronto, prepare também sua ficha. Para uma conversa, as notas de interpretação podem bastar.','Simplificar a frase sem alterar o momento em que a ficha de combate é necessária.')
edit(name,'Na despedida, uma promessa de contato pode gerar um próximo encontro.', 'Na despedida, combinar um contato pode levar a outro encontro.','Usar linguagem de conversa para o compromisso comum, evitando aproximação desnecessária com Promessas de Pacto.')
edit(name,'Uma promessa cria um compromisso a registrar; um pedido recusado pode levar a outra proposta.', 'Anote os contatos combinados; um pedido recusado pode levar a outra proposta.','Indicar o que registrar no exemplo cotidiano, sem sugerir uma regra de Pacto.')
# Mover o exemplo completo sem reescrever seu conteúdo; apenas os ajustes acima são textuais.
s=states[name];marker='<!-- folha: despedida -->\n\n';start=s.index(marker);block=s[start:];assert block.count('## Antes que o trem parta')==1
before=s;body=s[:start].rstrip();at=body.index('## 3.6 Ideias para sua próxima missão');states[name]=body[:at]+block.rstrip()+'\n\n'+body[at:]+'\n'
log.append({'fonte':str((T/name).relative_to(R)),'tipo':'movimento','trecho':block,'antes_de':'## 3.6 Ideias para sua próxima missão','motivo':'Ler o exemplo completo logo após os métodos de preparo, antes de abrir o catálogo de ideias.'})
edit(name,'Em uma folha, anote **a abertura, o que está acontecendo, quem quer o quê, o lugar e o que pode mudar**.', 'Use a [folha curta de preparo](<consultas/A1-preparar-a-missao.md>) para anotar **a abertura, o que está acontecendo, quem quer o quê, o lugar e o que pode mudar**. Se quiser conferir um exemplo pronto, volte a [Antes que o trem parta](<#antes-que-o-trem-parta>).','Completar o caminho de preparo rápido com a folha e o exemplo já existentes.')
edit(name,'O preparo permite responder ao grupo sem decidir quem fará uma promessa ou como a conversa terminará.', 'O preparo ajuda a responder ao grupo; os jogadores decidem o que dizer e fazer na despedida.','Segunda passagem: dizer diretamente quem escolhe as ações, com linguagem de conversa.')
edit(name,'Use a [folha curta de preparo](<consultas/A1-preparar-a-missao.md>) para anotar **a abertura, o que está acontecendo, quem quer o quê, o lugar e o que pode mudar**. Se quiser conferir um exemplo pronto, volte a [Antes que o trem parta](<#antes-que-o-trem-parta>). Acrescente as referências das regras e fichas de que realmente precisará. Você pode aprofundar um assunto entre sessões quando ele passar a importar.', 'Use a [folha curta de preparo](<consultas/A1-preparar-a-missao.md>) para anotar **a abertura, o que está acontecendo, quem quer o quê, o lugar e o que pode mudar**. Acrescente as referências das regras e fichas de que realmente precisará. Você pode aprofundar um assunto entre sessões quando ele passar a importar.\n\nPara conferir um exemplo pronto, consulte [Antes que o trem parta](<#antes-que-o-trem-parta>).','Segunda passagem: manter os passos de preparo juntos e dar ao exemplo seu próprio parágrafo.')
name=names[3]
before=states[name].split('\n\n## Oito situações para começar')[0]
after='''# Ideias para aventuras

As opções abaixo são originais, sem revelações da trama de Jujutsu Kaisen.

**Escolha o que precisa:** [situações](<#oito-situacoes-para-comecar>), [pessoas](<#seis-pessoas-para-encontrar>), [lugares](<#quatro-lugares-para-usar>) ou [complicações](<#seis-complicacoes-possiveis>). Para acompanhar uma combinação pronta, siga para [A assinatura no coreto](<#combinacao-1-a-assinatura-no-coreto>) ou [Ensaio na outra margem](<#combinacao-2-ensaio-na-outra-margem>).

Os perfis ajudam a interpretar pessoas; prepare fichas antes de usar suas capacidades em jogo. Uma ameaça também precisa de efeitos e meios de enfrentamento definidos, incluindo a conversão se puder ser obtida como entidade.'''
edit(name,before,after,'Retirar a repetição da introdução de 3.6 e permitir escolher as partes do catálogo sem percorrê-lo inteiro.')
for n,s in states.items():(T/n).write_text(s)
(A/'alteracoes.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
# Nova execução do gerador, com metadados separados; o gerador e as conferências 136 ficam históricos.
s=(A/'base-GERAR-LEITURA.py').read_text().replace("(A/'fontes-reunidas.json')","(A/'base-fontes-reunidas.json')").replace("'registro':136","'registro':137")
(A/'GERAR-LEITURA.py').write_text(s)
print(json.dumps({'fontes_alteradas':len(states),'registros_de_alteracao':len(log),'regras_novas':0},ensure_ascii=False))

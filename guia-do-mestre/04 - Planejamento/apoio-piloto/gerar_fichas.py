"""Gera os quadros consultáveis a partir da fonte numérica única do piloto."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
data=json.loads((HERE/'base-inimigos.json').read_text())
attrs={'forca':'Força','destreza':'Destreza','constituicao':'Constituição','inteligencia':'Inteligência','essencia':'Essência'}
trnames={'fisico':'Físico','vigor':'Vigor','intelecto':'Intelecto','espirito':'Espírito'}
descriptions={
 'rastejante':('Um corpo pequeno de papel amassado, com duas pernas, dois braços e mãos articuladas. Procura abrigo e golpeia quem o encurrala.', 'Demonstra uma ameaça frágil. Pode ser usado sozinho numa ocorrência menor. Dois exemplares permitem observar o efeito de haver mais turnos inimigos. Não aparece junto do Amontoado no encontro principal do piloto.'),
 'amontoado':('Uma figura de papelões dobrados e fitas, com duas pernas e dois braços terminados em mãos. Acumula caixas no depósito e as empurra com o corpo; os ruídos vêm dessas ações.', 'É o inimigo do piloto. Primeiro observa a invasão do seu espaço. Quando atacado ou quando alguém tenta desmontar sua pilha, combate a criatura consciente mais próxima; em empate, prioriza quem o atacou por último. Não golpeia pessoas inconscientes. Pode perseguir dentro do anexo, mas não sai dele nesta ocorrência. Essa preferência não torna a área externa uma barreira.'),
 'vigia':('Uma figura estreita de madeira e papel, com dois braços, mãos articuladas e duas pernas. Dispara farpas pela sua técnica e procura conservar distância.', 'Demonstra uma ameaça à distância. Com PE, dispara; sem PE suficiente, pode Desengajar, recuar ou usar a Pancada se for alcançado. Não tem projétil gratuito nem ataques adicionais. Não aparece no encontro principal do piloto.')
}
out=['''# Base pequena de inimigos para o piloto da R53

Versão piloto 1, de 21 de outubro de 2026. Três maldições originais para desenvolver e avaliar exemplos do Guia, autorizadas por Mizuki. Os números novos são propostas de trabalho desta base. O Bestiário antigo não foi usado como referência numérica.

O encontro principal de [As batidas no anexo](13-piloto-editorial-ocorrencia-sobrenatural.md) usa **um Amontoado do depósito**. A referência inicial é um grupo de três personagens de nível 2, com fichas válidas da R53, recursos disponíveis e sem Sequelas. A [verificação](15-verificacao-da-base-e-do-piloto.md) mostra também condições diferentes. A escolha não estabelece uma dificuldade universal por nível ou Grau.

## O que vem da R53 e o que está sendo proposto

Aplicam-se as regras atuais de turnos, testes, ataques, Bloquear, crítico, dano, Integridade, socorro e derrota. O nível 2 fornece Maestria 1; ataque físico usa Força, a Defesa sem proteção usa Destreza e as conjurações usam o atributo registrado. As montagens ofensivas de Classe 1 têm três pontos, custo de 3 PE e nenhuma Melhoria ou Restrição: os três pontos viram 3d8. Toque não produz um quarto dado quando não há Melhoria paga para recuperar.

**Escolhas novas desta base:** os totais de vida, as reservas de PE dos inimigos, as distribuições de atributos, treinos, anatomias e comportamentos. A R53 não fornece aqui uma fórmula geral de vida ou orçamento de inimigo que justifique esses totais como escala oficial. Eles serão avaliados para estes exemplos. Os nove pontos de atributos e o conjunto restrito de perícias são escolhas de organização desta base; não impõem um construtor universal aos inimigos futuros.

O nível das fichas serve aos efeitos que comparam nível, inclusive aquisição. Ele não concede patente nem garante equivalência a um personagem jogador. **Integridade dos inimigos = metade da vida máxima, para baixo**, conforme Dano na alma. Os estágios de Integridade se aplicam; o aumento de custo das conjurações pode reduzir a quantidade de usos disponíveis.

Os quadros abaixo e as conversões são gerados da mesma [fonte de produção](apoio-piloto/base-inimigos.json). A fonte não é uma regra adicional para a mesa.

## Regras comuns das três fichas

- Cada inimigo tem uma Padrão, um Movimento, uma Bônus e uma Reação, com renovação e conversão conforme Turnos. Um ataque por Ação Atacar; nenhuma ação de chefe, ataque extra ou contra-ataque gratuito.
- Podem usar as ações gerais que sua anatomia e percepção permitirem. Agarrar, Derrubar e Empurrar substituem o ataque da Ação Atacar e não causam o dano da Pancada. Precisam cumprir alcance, tamanho e requisitos de mãos.
- Bloquear é gratuito, escolhido antes do ataque e não gasta Reação. Aparar e Brecha conservam seus gatilhos e custos; um revide usa a Pancada, nunca a conjuração sem permissão.
- Têm visão e audição comuns. Não têm visão no escuro, percepção através de paredes, voo, teleporte ou capacidade de atravessar objetos. Compreendem frases simples no idioma usado pelo grupo; comunicam-se por gestos e ruídos, sem fala ou telepatia.
- Têm alma. Não recebem resistência, vulnerabilidade, imunidade ou Redução de Dano adicional por esta ficha. A aparência não concede imunidades a condições. Energia Reversa contra maldições conserva os requisitos e a resolução da R53.
- Não carregam equipamento nem possuem Ofícios. Sua forma permite segurar objetos compatíveis, abrir portas comuns e executar o Selo descrito. Uma mão ocupada numa contenção não fica livre para outra exigência.
- Ao chegar a zero de vida ou de Integridade, são derrotados. Não escolhem Insistir nem recebem janela de socorro de personagem jogador. O desfecho respeita a intenção da ação e os procedimentos de aquisição e destruição pertinentes.

**Leitura, Talento CE1 presente nas três fichas:** identifica Classe e Forma de feitiços conjurados a até 18 m. Não revela montagem, pensamentos ou alvos ocultos. Não causa dano, não concede ação e não faz uma reação acontecer sem gatilho.

## Consulta rápida

| Inimigo | Nível | PV | Integridade | PE | Defesa | Bloquear | Deslocamento |
|---|---|---|---|---|---|---|---|
''']
for e in data['enemies']:
    out.append(f"| {e['nome']} | {e['nivel']} | {e['pv']} | {e['pv']//2} | {e['pe']} | {e['defesa']} | 2d10 + {e['defesa']-11} | {e['deslocamento']} m |\n")
for e in data['enemies']:
    a=e['atributos'];b=e['basica'];m=e['magia'];desc,use=descriptions[e['id']]
    out.append(f"\n## {e['nome']}\n\n{desc}\n\n{use}\n\n**Tamanho:** {e['tamanho']}. **Iniciativa:** d20 + {a['destreza']}.\n\n")
    out.append('| Força | Destreza | Constituição | Inteligência | Essência |\n|---|---|---|---|---|\n'+ '| '+' | '.join(str(a[k]) for k in attrs)+' |\n\n')
    trattrs=dict(fisico=e['fisico'],vigor='constituicao',intelecto='inteligencia',espirito='essencia')
    trtext=[f"{trnames[t]} +{a[k]+int(t==e['tr_treinado'])}" for t,k in trattrs.items()]
    out.append('**TRs:** '+ '; '.join(trtext)+f". Físico usa {attrs[e['fisico']]}; o treino é em {trnames[e['tr_treinado']]}.\n\n")
    out.append('**Perícias treinadas:** '+ '; '.join(f'{p} +{a[k]+1}' for p,k in e['pericias'].items())+'. As demais usam somente seu atributo, respeitando requisitos.\n\n')
    dmg=f"{b['dados']}d{b['faces']}"+(f" + {b['fixo']}" if b['fixo'] else '')
    out.append(f"**Pancada — Ação Atacar, um ataque corpo a corpo, 1,5 m.** Ataque +{a[b['atributo']]+1}. No acerto, {dmg} de {b['tipo']}. Crítico: 2d4"+(f" + {b['fixo']}" if b['fixo'] else '')+'. Sem custo de PE. Não impõe condição.\n\n')
    out.append(f"**Manobras da Ação Atacar:** CD {8+a['forca']+1}, substituindo a Pancada, conforme as regras comuns.\n\n")
    if m:
        alcance=str(m['alcance']).replace('.',',')
        out.append(f"**{m['nome']} — Classe 1, Ação Padrão, {m['custo']} PE, {m['forma']}, {alcance} m.** Selo: {m['selo'].lower()}. Precisa enxergar o alvo e cumprir o alcance. Ataque de técnica +{a[m['atributo']]+1}; acerto causa {m['dados']}d{m['faces']} de {m['tipo']}. Crítico: 6d8. Não soma atributo ao dano nem o dano da Pancada. Não há TR, condição, área ou efeito no erro. O erro gasta ação e PE.\n\n")
        out.append(f"**Fundamento registrado:** atributo {attrs[m['atributo']]}; dano {m['tipo']}; Livres: {', '.join(m['livres'])}; Fechadas: {', '.join(m['fechadas'])}. Expressão visual: as marcas do corpo se acendem brevemente, sem efeito mecânico. A ficha conhece apenas a aplicação acima. Não recebe repertório, Aptidões, Caminho ou recursos adicionais por analogia a um personagem jogador.\n\n")
        out.append(f"Com a reserva inicial de {e['pe']} PE, são no máximo dois usos pelo custo normal. Os PE não se renovam por rodada. Se algum efeito mudar o custo ou impedir a execução, use o custo atual. Sem poder conjurar, continua dispondo da Pancada e das ações gerais.\n")
    else:
        out.append('**Conjuração:** não possui técnica ofensiva nem reserva de PE. Leitura continua sendo apenas o Talento descrito.\n')

out.append('''
## Conversões conhecidas para maldições domadas

Estas conversões permitem mostrar o resultado antes de uma tentativa de submissão. Elas mantêm identidade e funções dentro da escala de Construir invocações. Não transferem a vida ampliada do encontro nem o orçamento pessoal de Fundamento. A aquisição exige nível permitido, derrota sem destruição e o TR Espírito previsto na R53. O sucesso no TR exorciza; a falha permite domar. Não se repete a tentativa sobre o mesmo alvo até conseguir uma falha.

**Regras comuns da conversão:** conservam nível 2, atributos, tamanho, anatomia, comunicação, sentidos, deslocamento e Leitura. Usam a Maestria do invocador. A Defesa sem equipamento é **10 + Destreza da entidade + metade da Essência ou Inteligência escolhida pelo invocador, para baixo**. Denominaremos essa última parcela **B** e a Maestria **M**. Conservam o TR treinado e as perícias indicadas; substitua o +1 de treino por M. Outros TRs usam apenas o atributo da criatura.

| Domada | Vida máxima | Integridade | Defesa | Ataque da básica | Reserva própria máxima |
|---|---|---|---|---|---|
''')
for e in data['enemies']:
    a=e['atributos'];c=a['constituicao'];hp=5+c+(3+c)*(e['nivel']-1)
    ac=a[e['magia']['atributo']] if e['magia'] else a['forca']
    reserve=e['nivel']*(1+a['essencia']//3) if e['magia'] else 0
    out.append(f"| {e['nome']} | {hp} | {hp//2} | {10+a['destreza']} + B | +{ac} + M | {reserve} PE |\n")
out.append('''
A básica própria de cada conversão é **Toque, 1,5 m, ataque pelo atributo indicado, 1d6 de Concussão, sem somar atributo**, sem Melhoria ou Restrição e sem PE. Consome a atuação básica da entidade. No Vigia, a básica usa Essência como atributo de acerto da entidade; isso não modifica o acerto de uma arma que ele venha a empunhar.

Cada conversão tem uma vaga de especial de nível 2 e um Talento CE1, Leitura. O Rastejante deixa a vaga de especial vazia; não ganha uma especial nova por ser adquirido. No Amontoado e no Vigia, a especial conhecida usa **dois pontos**, sem Melhoria ou Restrição, causando **2d8** do tipo e pela Forma da conjuração original: Toque 1,5 m no Amontoado; Projétil 18 m no Vigia. Ataque pelo atributo registrado + M. Sem Selo, atributo no dano, TR ou condição. No crítico, 4d8. O custo total é **3 PE**.

Comandar uma especial custa a Padrão do invocador e a atuação básica da entidade. O invocador paga 2 PE e a domada paga 1, enquanto houver reserva; se faltar, ele cobre o restante. A reserva máxima segue **nível × (1 + Essência ÷ 3, para baixo)**. Entrada, retorno e a Reação coletiva seguem Invocações em campo. A domada não conserva um turno independente de inimigo nem ganha uma especial além da básica no mesmo ciclo por esta ficha.

Famílias abertas e Livre para cada conversão:

''')
for e in data['enemies']:
    d=e['domada']
    out.append(f"- **{e['nome']}:** {', '.join(d['abertas'])}; {d['livre']} Livre. As outras seis ficam Fechadas.\n")
out.append('''
Os máximos da conversão não restauram reservas nem removem a queda. Registre valores atuais sem exceder os novos máximos e aplique Queda e destruição e Retorno e corpos caídos quando pertinentes. Cura comum de entidade não funciona a zero de vida. A aquisição não permite voltar à cena ignorando os custos de entrada ou retorno.

**Antes do golpe final para aquisição:** a R53 manda conferir destruição. Uma ocorrência direta que alcance a vida máxima ou cujo excedente além de zero supere metade da máxima destrói a entidade; dano em área não destrói por si. No Amontoado, os limites de referência do encontro são 48 e metade 24; igualar o excedente de 24 não é superar. Essa conferência usa a ficha do encontro, antes da conversão. A equipe deve conhecer essa diferença ao tentar capturar.

## Uso e revisão

Use o Amontoado isolado no piloto. Os outros dois inimigos fornecem comparações; reuni-los com ele cria outro encontro. Não multiplique vida ou ataques silenciosamente para compensar decisões boas do grupo. Para outros tamanhos de equipe, faixas de nível, reservas já gastas ou composições com entidades, reavalie o encontro usando as fichas reais.

Registrar em jogo: recursos iniciais, duração até neutralizar a ameaça, quedas, ações durante Insistir, socorros, retirada, dúvidas de regra e estado no encerramento. Números conferidos ou simulados não equivalem a teste de mesa realizado.

Referência principal: [texto completo da R53](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md>), em Atributos, Turnos, Ataques, Dano na alma, Vida a zero, Fundamento, Invocações em campo e Construir invocações. O [relatório de verificação](15-verificacao-da-base-e-do-piloto.md) registra os cálculos, hipóteses e limites.
''')
(HERE.parent/'14-base-pequena-de-inimigos-r53.md').write_text(''.join(out))
print('Fichas e conversões geradas da fonte única.')

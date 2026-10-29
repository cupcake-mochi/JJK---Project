from revisar_guia94 import *
for p in (R/'06 - Redacao do Guia').glob('*.md'):
 rel=str(p.relative_to(R)); t=p.read_text();pairs=[]
 for old,new in [('queda de jogador','queda de personagem jogador'),('vestíbulo limpo','entrada limpa'),('Vestíbulo limpo','Entrada limpa')]:
  if old in t:pairs.append((old,new))
 if pairs:edit(rel,pairs)
rel='04 - Planejamento/12-piloto-editorial-cotidiano.md'
t=(R/rel).read_text(); old=t[t.index('## O que este piloto permite avaliar'):]
new='''## Levar o exemplo para sua mesa

O exemplo mostra como partir de uma necessidade cotidiana, dar objetivos às pessoas e oferecer mais de um caminho para resolver um problema. Ao adaptá-lo, deixe os jogadores escolherem o que merece uma cena e o que pode ser resolvido brevemente.

[As batidas no anexo](13-piloto-editorial-ocorrencia-sobrenatural.md) acompanha uma ocorrência sobrenatural até o fechamento, com inimigos e confronto comentado. Você pode reutilizar o centro cultural nos dois exemplos. Buscar o uniforme, porém, não obriga o personagem a aceitar essa missão.
'''
edit(rel,[(old,new)],'Segunda leitura: transformar notas de avaliação editorial em orientação ao mestre')
rel='04 - Planejamento/13-piloto-editorial-ocorrencia-sobrenatural.md';t=(R/rel).read_text();old=t[t.index('**Estado de desenvolvimento:**'):t.index('**Para consultar durante a sessão:**')]
new='''**Exemplo experimental.** O encontro usa um Amontoado do depósito, apresentado em [Três maldições para a missão](14-base-pequena-de-inimigos-r53.md), contra três personagens de nível 2, com fichas conferidas, recursos disponíveis e sem Sequelas iniciais. As contas e a simulação foram conferidas; ainda não houve teste de mesa. Os números novos são propostas para este encontro.

'''
edit(rel,[(old,new),('Sua ficha está na base pequena de inimigos.', 'Sua ficha está em Três maldições para a missão.'),('Este piloto não utiliza', 'Este exemplo não utiliza'),('Usaremos três referências parciais de cálculo, descritas na [verificação](15-verificacao-da-base-e-do-piloto.md).', 'Usaremos os três perfis resumidos no quadro abaixo.'),('## Critérios para a revisão','## Ao adaptar esta missão'),('O leitor deve conseguir distinguir fatos, receios e testemunhos; oferecer meios diferentes de obter informação; reconhecer quando uma conversa dispensa teste; deixar descobertas mudarem prioridades; conduzir o inimigo pela ficha; acompanhar quedas, socorro e encerramento; e registrar o que permanece. A revisão com leitores e o uso em mesa avaliarão se a extensão e os comentários ajudam na consulta.', 'Prepare os fatos e o que cada testemunha sabe. Ofereça caminhos diferentes para investigar e deixe as descobertas mudarem as prioridades do grupo. Durante um confronto, acompanhe as fichas, as quedas e o socorro. Ao encerrar, registre o que mudou e o que ainda precisa ser resolvido.')])
rel='04 - Planejamento/14-base-pequena-de-inimigos-r53.md';t=(R/rel).read_text();pairs=[]
for old,new in [('do piloto','de As batidas no anexo'),('no piloto','em As batidas no anexo'),('Os quadros abaixo e as conversões são gerados da mesma fonte de produção. A fonte não é uma regra adicional para a mesa.','Confira a ficha de inimigo durante o encontro e a conversão correspondente antes de oferecer uma tentativa de Doma.')]:
 if old in t:pairs.append((old,new))
edit(rel,pairs)
p=R/'07 - Edicao de Leitura/GERAR-EDICAO.py';t=p.read_text().replace('As batidas no anexo, com preparo comentado, confronto, socorro e as fichas experimentais do piloto.', 'Cenas comentadas, do cotidiano ao confronto, com socorro e fichas de inimigos.').replace('Leia o piloto comentado com as fichas do encontro.','Leia a missão comentada com as fichas do encontro.');p.write_text(t)

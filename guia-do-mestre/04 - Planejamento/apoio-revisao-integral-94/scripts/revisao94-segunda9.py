from revisar_guia94 import *
edit(source(67),[('Recursos do cenário, aliados e ações e recursos exclusivos do chefe','Elementos do cenário, aliados, ações e recursos exclusivos do chefe')],'Segundo pente-fino, página 104: repetição')
edit(source(57),[('[base experimental]','[Três maldições para a missão]'),('**Escolha do piloto:**','**Por que usar o Amontoado:**'),('No piloto continua havendo','Neste encontro continua havendo'),('O [relatório do piloto](<../04 - Planejamento/15-verificacao-da-base-e-do-piloto.md>) usou','A simulação usou')],'Segundo pente-fino, páginas 107–109')
edit(source(63),[('**Ficha experimental, versão 1.**','**Ficha experimental.**')],'Segundo pente-fino, página 117: versão interna dispensável')
for n in [63,64]:
 p=R/source(n); t=p.read_text()
 # Retira somente a frase de referência ao arquivo de produção, preservado no acervo.
 patterns=[r' O \[registro 66\]\([^\n]+?\) guarda fontes, histórico e alcance da conferência\.',r' O registro de produção e as conferências estão no \[documento 67\]\([^\n]+?\)\.']
 for pattern in patterns:
  for m in re.finditer(pattern,t):edit(source(n),[(m.group(), '')],'Segundo pente-fino, página 121: referência de produção fora do livro')

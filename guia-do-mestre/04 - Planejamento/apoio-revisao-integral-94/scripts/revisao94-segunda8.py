from revisar_guia94 import *
edit(source(59),[('(60-construir-capacidades-de-inimigos.md)','(60-montar-habilidades-de-inimigos.md)')],'Corrigir destino da remissão')
edit(source(60),[('Essa regra de recarga permanece experimental no [estudo 64](<../04 - Planejamento/64-prototipos-de-recursos-dos-inimigos.md>). Esse ensaio não autoriza aplicar a mesma dispensa a todos os feitiços ou copiá-la para uma personagem.','Essa recarga é experimental e vale apenas para a variante descrita. Não dispensa o custo dos demais feitiços nem se aplica automaticamente a personagens jogadores.')],'Segundo pente-fino, página 92')
edit(source(74),[('depois delas','depois desses ataques'),('resolver a queda de jogador','resolver a queda do personagem jogador')],'Segundo pente-fino, páginas 95–96')
for p in (R/'06 - Redacao do Guia').glob('*.md'):
 if '[ficha única de construção e encontro]' in p.read_text():edit(str(p.relative_to(R)),[('[ficha única de construção e encontro]','[ficha de inimigo e encontro]')],'Nome consistente da ficha')

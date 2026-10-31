"""Fechar as fontes restantes e tornar as consultas diretas, sem ampliar regras."""
from pathlib import Path
import json,shutil,hashlib,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
names=['casos/72-sineiro-consulta-e-doma.md','consultas/05-folha-de-conducao.md','consultas/87-casos-da-obra-para-preparar-situacoes.md','consultas/88-indice-de-termos-do-mundo.md','referencias.md']
states={n:(A/'antes'/T.relative_to(R)/n).read_text() for n in names};logs=[]
def edit(name,before,after,reason):
 s=states[name];assert s.count(before)==1,(name,before,s.count(before));states[name]=s.replace(before,after,1)
 logs.append({'fonte':(T/name).relative_to(R).as_posix(),'antes':before,'depois':after,'motivo':reason})
n=names[0]
edit(n,'A vida inimiga mudou de 72 para 108, mas a construção domada continua em 38 PV e 19 de Integridade; o nível e suas escolhas foram preservados.','O Sineiro tem 108 PV na ficha do confronto. Depois da Doma, seu máximo é 38 PV, com 19 de Integridade; o nível e as escolhas de construção continuam os da conversão acima.','Apresentar a comparação entre as fichas atuais e retirar um número histórico que não pertence à criatura oferecida ao leitor.')
# A mesma legenda de consulta leva ao trecho correspondente, inclusive nas tabelas.
anchors={
 ('../02-o-mundo-dos-feiticeiros.md','Escolas, famílias e contatos'):'23-escolas-familias-e-contatos',
 ('../02-o-mundo-dos-feiticeiros.md','Funções e apoio'):'23-escolas-familias-e-contatos',
 ('../02-o-mundo-dos-feiticeiros.md','Modos de vida'):'24-diferentes-formas-de-viver',
 ('../02-o-mundo-dos-feiticeiros.md','Perguntas de cotidiano'):'24-diferentes-formas-de-viver',
 ('../05-criar-uma-campanha.md','A sessão zero'):'51-a-sessao-zero',
 ('../05-criar-uma-campanha.md','Vínculos e interesses dos personagens'):'52-vinculos-e-interesses-dos-personagens',
 ('../05-criar-uma-campanha.md','Vínculos'):'52-vinculos-e-interesses-dos-personagens',
 ('../05-criar-uma-campanha.md','Facções'):'54-faccoes',
 ('../07-personagens-e-tecnicas.md','Conferir a ficha'):'71-conferir-a-ficha',
 ('../07-personagens-e-tecnicas.md','Avaliar uma capacidade'):'74-avaliar-uma-capacidade',
 ('../07-personagens-e-tecnicas.md','Personagens e seus cuidados'):'72-personagens-e-seus-cuidados',
 ('../07-personagens-e-tecnicas.md','Personagens'):'72-personagens-e-seus-cuidados',
 ('../08-entre-missoes.md','Comprar, emprestar e contratar'):'84-comprar-emprestar-e-contratar',
 ('../08-entre-missoes.md','Recompensas e progressão'):'86-recompensas-e-progressao',
 ('../03-preparar-aventuras.md','Pistas e investigações'):'34-pistas-e-investigacoes',
 ('../04-na-mesa-de-jogo.md','Combate, socorro e retirada'):'47-combate-socorro-e-retirada',
 ('../04-na-mesa-de-jogo.md','conduzir uma investigação'):'44-conduzir-uma-investigacao',
 ('../04-na-mesa-de-jogo.md','acompanhar recursos'):'47-combate-socorro-e-retirada',
 ('../casos/31-avaliar-poderes-avancados.md','Poderes avançados'):'dominio-aparencia-acerto-e-efeito',
}
n=names[2]
edit(n,'Para preparar sem revelações, use [Escolas, famílias e contatos](<../02-o-mundo-dos-feiticeiros.md>).','Para preparar sem revelações, use [O mundo dos feiticeiros](<../02-o-mundo-dos-feiticeiros.md>).','Nomear o capítulo de entrada sem revelações, que é o destino da referência.')
for n in names[1:4]:
 for line in states[n].splitlines():
  new=line
  for (path,label),anchor in anchors.items():new=new.replace(f'[{label}](<{path}>)',f'[{label}](<{path}#{anchor}>)')
  if new!=line:edit(n,line,new,'Levar a consulta ao trecho indicado pela legenda, preservando o texto das definições e os valores.')
n=names[3]
line=next(x for x in states[n].splitlines() if x.startswith('| Barreira e Cortina |'))
new=line.replace('[Poderes avançados](<../casos/31-avaliar-poderes-avancados.md#dominio-aparencia-acerto-e-efeito>)','[Preparar uma Cortina](<../casos/33-casos-especificos-de-avaliacao.md#definir-os-limites-de-uma-cortina>)')
assert new!=line
edit(n,line,new,'Corrigir a referência de Cortina: o exemplo próprio está no caso de dúvidas sobre técnicas, e não no aprofundamento de Domínios.')
n=names[4]
additions={
 '- **Cairn, segunda edição. Warden\'s Guide.** Princípios de exploração, acessos, sinais, facções e ferramentas para construir lugares.':' [Guia no site oficial](https://cairnrpg.com/second-edition/wardens-guide/).',
 '- **Evil Hat Productions. Fate Core System.** Preparação de situações, perguntas de aventura e campanha, condução e encerramento de cenas.':' [Condução](https://fate-srd.com/fate-core/running-game) e [cenas e aventuras](https://fate-srd.com/fate-core/scenes-sessions-scenarios), no SRD.',
 '- **Justin Alexander, The Alexandrian. Three Clue Rule; The Art of Pacing; Don\'t Prep Plots: The Principles of RPG Villainy.** Caminhos de investigação, ritmo, oposição e resultados abertos às escolhas dos jogadores.':' [Pistas](https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule), [ritmo](https://thealexandrian.net/wordpress/31509/roleplaying-games/the-art-of-pacing) e [antagonistas](https://thealexandrian.net/wordpress/36383/roleplaying-games/dont-prep-plots-you-will-rue-this-day-heroes-the-principles-of-rpg-villainy).',
 '- **Kevin Crawford. Worlds Without Number, Free Edition.** Preparação de pessoas, lugares, complicações e facções.':' [Apresentação da editora](https://sinenominepublishing.com/products/worlds-without-number-deluxe-pdf), que distingue o conteúdo gratuito dos acréscimos da edição Deluxe.',
 '- **Michael E. Shea, Sly Flourish. Ending Campaigns.** Fios de interesse e espaço para o futuro dos personagens no encerramento da campanha.':' [Artigo original](https://slyflourish.com/ending_campaigns.html).',
 '- **Pathfinder, segunda edição. GM Core: Building Creatures.** Referência oficial consultada para funções, ações e capacidades reativas. Sua consulta é distinta da leitura do Livro Básico usado na comparação editorial.':' [Texto no Archives of Nethys](https://2e.aonprd.com/Rules.aspx?ID=2874).',
 '- **D&D Beyond. How to Use a Monster, Basic Rules 2024.** Referência sobre leitura e uso de fichas e ações de inimigos.':' [Regras oficiais](https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster).',
}
for before,extra in additions.items():edit(n,before,before+extra,'Oferecer acesso direto à fonte identificada na bibliografia; conservar o alcance da atribuição e da comparação.')
for name,s in states.items():(T/name).write_text(s)
(A/'alteracoes.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
composition=json.loads((A/'base-composicao.json').read_text())['ordem'];routes=[]
for name in names:
 rel=(T/name).relative_to(R).as_posix();row=next(x for x in composition if x['fonte']==rel);p=E/row['pagina'];q=A/'antes'/p.relative_to(R)
 if not q.exists():q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
 routes.append({'fonte':rel,'pagina':row['pagina'],'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
(A/'destinos-alterados.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2)+'\n')
print(len(logs),'ajustes em',len(names),'fontes.')

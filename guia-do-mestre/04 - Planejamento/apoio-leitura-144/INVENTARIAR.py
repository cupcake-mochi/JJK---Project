"""Delimitar a leitura concluída e guardar as fontes online conferidas."""
from pathlib import Path
import hashlib,json
A=Path(__file__).resolve().parent;R=A.parents[1];P=R/'04 - Planejamento';T=R/'06 - Redacao do Guia/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):(A/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
names=['casos/101-haru-vigia-e-tessa.md','casos/102-o-arquivo-e-as-oportunidades-de-agir.md','casos/11-espaco-e-usos-criativos.md','casos/14-tres-maldicoes-para-a-missao.md','casos/57-avaliar-o-encontro-do-amontoado.md','casos/64-a-passarela-e-o-guincho.md','casos/67-preparar-chefes-e-confrontos-maiores.md','casos/72-sineiro-consulta-e-doma.md','consultas/02-ficha-de-preparacao.md','consultas/05-folha-de-conducao.md','consultas/61-ficha-de-habilidade-de-inimigo.md','consultas/87-casos-da-obra-para-preparar-situacoes.md','consultas/88-indice-de-termos-do-mundo.md','consultas/A1-exemplo-despedida.md','indice-de-casos.md','referencias.md']
changed={x['fonte'] for x in json.loads((A/'destinos-alterados.json').read_text())};rows=[]
for n in names:
 p=T/n;rel=p.relative_to(R).as_posix();rows.append({'fonte':rel,'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa e segunda leitura completa após os ajustes.' if rel in changed else 'Leitura completa e comparação com o conjunto, sem alteração neste lote.'})
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
save('leitura-realizada.json',{'registro':144,'data':'2026-10-30','fontes_lidas':rows,'trechos_comparados':[{'fonte':(T/'casos/33-casos-especificos-de-avaliacao.md').relative_to(R).as_posix(),'sha256':sha(T/'casos/33-casos-especificos-de-avaliacao.md'),'alcance':'Definir os limites de uma Cortina; conferência do destino, do assunto e da distinção de ocultação.'}],'fonte_tecnica_preservada':primary.relative_to(R).as_posix(),'sha256_fonte_tecnica':sha(primary),'limite':'Leitura editorial e conferência de consultas, contas selecionadas e fontes citadas. Não é teste com jogadores, revisão visual do PDF ou nova leitura integral dos livros comparados.'})
read={}
for n in range(137,145):
 d=json.loads((P/f'apoio-leitura-{n}/leitura-realizada.json').read_text())
 for x in d.get('nucleo',[])+d.get('fontes_lidas',[]):read[x['fonte']]={'registro':n,**x}
coverage=[]
for p in sorted(T.rglob('*.md')):
 rel=p.relative_to(R).as_posix();digest=sha(p);previous=read.get(rel)
 assert previous and previous['sha256']==digest,(rel,previous)
 coverage.append({'fonte':rel,'sha256_atual':digest,'leitura_recente':previous['registro'],'estado':'leitura integral recente e hash vigente'})
assert len(coverage)==99
save('cobertura-da-leitura-continua.json',{'registro':144,'alcance':'As 99 fontes da edição integrada possuem leitura integral identificada nos registros 137–144 e hash vigente. As fontes alteradas foram relidas no lote que as alterou. Não equivale a revisão visual ou avaliação externa.','contagens':{'leitura integral recente e hash vigente':99},'fontes':coverage})
online=[
 ('Jujutsu Kaisen — episódio 48','https://jujutsukaisen.jp/episodes/48.php','Sinopse compatível com o caso Ordens em conflito.'),
 ('Jujutsu Kaisen — episódio 50','https://jujutsukaisen.jp/episodes/50.php','Sinopse compatível com a procura de Tengen e a informação buscada.'),
 ('Jujutsu Kaisen — episódio 51','https://jujutsukaisen.jp/episodes/51.php','Sinopse compatível com Maki buscando ferramentas e encontrando Mai e o pai.'),
 ('Jujutsu Kaisen — episódio 55','https://jujutsukaisen.jp/episodes/55.php','Sinopse compatível com Higuruma advogado e os relatos divergentes de localização.'),
 ('Jujutsu Kaisen — volume 18','https://www.shueisha.co.jp/books/items/contents_amp.html?jdcn=08X10000000018964300','Apresentação editorial compatível com a busca da cooperação de Hakari.'),
 ("Cairn 2e — Warden’s Guide",'https://cairnrpg.com/second-edition/wardens-guide/','Destino oficial do guia e acesso às ferramentas; não nova leitura integral do livro.'),
 ('Fate Core — Running the Game','https://fate-srd.com/fate-core/running-game','Texto e identificação da referência de condução.'),
 ('Fate Core — Scenes, Sessions, and Scenarios','https://fate-srd.com/fate-core/scenes-sessions-scenarios','Índice do capítulo de preparação de cenas e aventuras.'),
 ('Three Clue Rule','https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule','Título e conteúdo do artigo sobre pistas.'),
 ('The Art of Pacing','https://thealexandrian.net/wordpress/31509/roleplaying-games/the-art-of-pacing','Título e conteúdo do artigo sobre ritmo.'),
 ('The Principles of RPG Villainy','https://thealexandrian.net/wordpress/36383/roleplaying-games/dont-prep-plots-you-will-rue-this-day-heroes-the-principles-of-rpg-villainy','Título e conteúdo do artigo citado; não confundir com o vídeo posterior.'),
 ('Worlds Without Number — editora','https://sinenominepublishing.com/products/worlds-without-number-deluxe-pdf','Apresentação distingue material gratuito e conteúdo adicional Deluxe; o link não é apresentado como download da edição gratuita.'),
 ('Ending Campaigns','https://slyflourish.com/ending_campaigns.html','Título e conteúdo do artigo sobre encerramento.'),
 ("The Lazy GM’s Resource Document",'https://slyflourish.com/lazy_gm_resource_document.html','Título, autor e atribuição exigida no próprio documento; não altera o alcance das demais licenças.'),
 ('GM Core — Building Creatures','https://2e.aonprd.com/Rules.aspx?ID=2874','Texto identificado como GM Core, distinto do Livro Básico anterior ao Remaster.'),
 ('Basic Rules 2024 — How to Use a Monster','https://www.dndbeyond.com/sources/dnd/br-2024/how-to-use-a-monster','Destino e identificação das regras de uso de inimigos.'),
]
save('fontes-online-conferidas.json',{'registro':144,'data':'2026-10-30','metodo':'Consulta pelo navegador de pesquisa às páginas citadas e aos destinos bibliográficos. Resumos próprios, sem reprodução integral dos textos.','fontes':[{'titulo':t,'url':u,'conferencia':c} for t,u,c in online],'consulta_sem_acesso':{'url':'https://www.drivethrurpg.com/en/product/348809/worlds-without-number-free-edition','resultado':'Resposta 403; não usado como conteúdo consultado nem acrescentado ao livro.'},'limite':'Não houve nova leitura integral do mangá ou de todos os guias. D&D 2014/2024 e Livro Básico de Pathfinder conservam a comparação anterior no acervo; não receberam links improvisados.'})
print('16 fontes lidas; 99/99 com leitura integral recente e hash vigente; 16 destinos online conferidos.')

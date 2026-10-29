from revisar_guia94 import *
import markdown
from bs4 import BeautifulSoup
from markdown.extensions.toc import slugify
# Preserve old heading targets while the displayed text changes.
entries=json.loads(LOG.read_text());allrels=sorted({x['fonte'] for x in entries if x['fonte'].endswith('.md')})
aliases={};main_titles={}
for rel in allrels:
 oldpath=A/'antes'/rel
 if not oldpath.exists():continue
 before=oldpath.read_text();after=(R/rel).read_text()
 oldheads=BeautifulSoup(markdown.markdown(before,extensions=['toc']),'html.parser').find_all(re.compile('^h[1-6]$'))
 newheads=BeautifulSoup(markdown.markdown(after,extensions=['toc']),'html.parser').find_all(re.compile('^h[1-6]$'))
 new_by_text={h.get_text():h['id'] for h in newheads};changes=[x for x in entries if x['fonte']==rel]
 local={}
 for h in oldheads[1:]:
  title=h.get_text();changed=title
  for e in changes:
   a,b=e['antes'],e['depois']
   if a.startswith('#') and b.startswith('#'):a=a.lstrip('# ').strip();b=b.lstrip('# ').strip()
   changed=changed.replace(a,b)
  if changed in new_by_text:
   cur=new_by_text[changed]
   if cur!=h['id']:local[cur]=h['id']
  elif title in new_by_text:pass
  elif h['id'] not in ['historico-da-proposta']:
   print('CHECK ALIAS',rel,h['id'],changed)
 if local:aliases[rel]=local
 a=before.splitlines()[0].lstrip('# ').strip();b=after.splitlines()[0].lstrip('# ').strip()
 if a!=b:main_titles[a]=b
(R/'07 - Edicao de Leitura/titulos-estaveis.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
# Update exact displayed link labels, never source paths/fragments.
for rel in allrels:
 text=(R/rel).read_text();pairs=[]
 for a,b in main_titles.items():
  if '['+a+'](' in text:pairs.append(('['+a+'](', '['+b+']('))
 if pairs:edit(rel,pairs,'Nome visível da referência atualizado; destino preservado')
p=R/'07 - Edicao de Leitura/GERAR-EDICAO.py';t=p.read_text()
t=t.replace("sections={};pages=[];cuts=[];refs={};broken=[]", "sections={};pages=[];cuts=[];refs={};broken=[]\nALIASES=json.loads((HERE/'titulos-estaveis.json').read_text()) if (HERE/'titulos-estaveis.json').exists() else {}")
t=t.replace("old=node['id'];new=key+'--'+old;anchors[old]=new;node['id']=new", "old=node['id'];stable=ALIASES.get(rel,{}).get(old,old);new=key+'--'+stable;anchors[old]=new;anchors[stable]=new;node['id']=new")
# The revised source already supplies the reader-facing introduction.
t='\n'.join(line for line in t.splitlines() if not line.startswith("  old=body.split('\\n\\n',1)[0];new='Esta consulta"))+'\n'
repls=[
('Mundo, cotidiano e grupo','O mundo e seu grupo'),('Preparar missões e campanhas','Missões e campanhas'),('Conduzir a sessão','Na mesa de jogo'),('Recursos, derrota e continuidade','Recursos e socorro'),('Inimigos, encontros e perigos','Inimigos e perigos'),('Personagens, vínculos e cuidados','Os personagens'),('Ofícios, equipamento e tempo','Entre missões'),('Consulta e passagem entre mestres','Registros da campanha'),
('Descreva, resolva tentativas, distribua participação e torne informação e espaço utilizáveis.','Descreva a cena, resolva as ações e dê espaço às escolhas de todos.'),('Transforme uma ideia em proposta verificável e acompanhe custos, limites, usos e ajustes.','Avalie uma ideia de poder, seus custos, seus limites e seus efeitos no jogo.'),('Conduza trocas, aquisições e projetos com requisitos, estados e encerramentos definidos.','Prepare Pactos e acompanhe a criação, a conquista e o uso de entidades.'),('Escolha os registros necessários e entregue o estado que permite continuar uma missão.','Anote o que mudou e prepare a próxima sessão, mesmo quando houver troca de mestre.'),
('Fichas e exemplos de registro','Fichas para a mesa'),('Índice de termos do mundo','Termos do mundo'),('Cotidiano e missão acompanhados','Exemplos de jogo'),('Casos da obra — contém revelações','Ideias da obra — contém revelações'),('A entrega trocada: cotidiano acompanhado','A entrega trocada'),('Fichas do piloto: três inimigos','Três maldições para a missão'),
('revisão de leitura 2','revisão de leitura 3'),('26 de outubro de 2026','28 de outubro de 2026'),("data='2026-10-26'","data='2026-10-28'"),('segunda revisão de leitura','terceira revisão de leitura'),
('Os procedimentos também atendem campanhas fechadas: mantenha o que ajuda sua mesa e ajuste a administração ao formato escolhido.','As orientações também servem a campanhas fechadas. Adapte a organização dos registros à sua mesa.'),
('Siga o procedimento e acompanhe As batidas no anexo.','Siga os passos e acompanhe As batidas no anexo.'),('Como usar as remissões','Como encontrar um assunto'),('para que remissões como','para que referências como'),('o alcance de um parecer','a quem uma avaliação se aplica'),('nomes e recortes de personagem','nomes de personagens'),
('Quando houver incerteza relevante, use o procedimento correspondente da R53 e descreva o resultado. Escolhas e consequências atualizam o estado da missão.','Quando o resultado for incerto e a falha fizer diferença, consulte a regra no Livro de Regras 1.0. Descreva o resultado e o que mudou na missão.'),('têm procedimentos próprios','têm regras próprias'),('remete ao Livro do Jogador','indica onde consultar o Livro de Regras 1.0'),
('A R53 é a referência mecânica. Orientações de preparo explicam como conduzir situações; parâmetros próprios de inimigos, perigos e outros casos conservam a identificação de proposta experimental.','O Livro de Regras 1.0 contém as regras do jogo. Este Guia ajuda você a usá-las e a preparar suas sessões. Inimigos, perigos e outras criações em avaliação aparecem como exemplos experimentais.'),
('e os procedimentos do Guia','e as orientações do Guia'),('R53 é a base mecânica.','As regras vêm do Livro de Regras 1.0.'),
('O Livro do Jogador R53 fundamenta os procedimentos. Esta integração organiza textos existentes, remissões e caminhos de leitura. Ela não altera a R53, aprova uma escala de dificuldade ou certifica equilíbrio. Reserva Condensada conserva o acordo por personagem publicado; os modelos numéricos descartados não foram incorporados.','As regras vêm do Livro de Regras 1.0. O Guia reúne orientações de mestragem e exemplos para consulta. As propostas experimentais precisam ser avaliadas em jogo; não formam uma escala geral de dificuldade. Reserva Condensada segue o acordo por personagem previsto no livro de regras.'),
("limites='Integração estrutural e navegação. Sem nova revisão semântica integral de cada passagem, sessão humana, equilíbrio certificado ou alteração da R53.'","limites='Revisão textual e visual registrada no relatório 94. Não representa teste de mesa, equilíbrio certificado ou alteração do livro de regras.'")]
for a,b in repls:
 assert a in t or b in t,a
 t=t.replace(a,b)
p.write_text(t)
# PDF front matter is explicitly rewritten, preserving the mechanical explanation.
p=R/'08 - Diagramacao do Guia/GERAR-PDF.py';t=p.read_text()
start=t.index('def front_items():');end=t.index('\ndef build():',start)
front='''def front_items():
 return [
  para('Como usar este livro','major','inicio'),
  para('Pré-1.0 · edição de leitura · 28 de outubro de 2026','small'),
  para('Este livro ensina você a mestrar Ciclo Maldito: preparar uma missão, apresentar o mundo e acompanhar as escolhas dos jogadores. O sistema foi pensado principalmente para guildas, onde vários mestres e personagens compartilham a mesma história. Você também pode usar estas orientações numa campanha fechada.'),
  para('Não é preciso conhecer Jujutsu Kaisen. O primeiro capítulo apresenta o mundo e a vida de um feiticeiro. Se você já conhece a obra, pode seguir para os acordos do grupo. O apêndice D traz exemplos com revelações da trama; sua leitura é opcional.'),
  para('Como funciona uma sessão','h2'),
  para('Você descreve a situação e o que os personagens percebem. Os jogadores dizem o que querem fazer. Se o resultado for incerto e a falha fizer diferença, consulte a regra no Livro de Regras 1.0. Num teste comum, role um dado de vinte faces (d20) e some o bônus indicado. O teste tem sucesso se alcançar ou superar a Classe de Dificuldade (CD). Ataques e testes de resistência (TRs) seguem suas próprias regras.'),
  para('Depois, descreva o resultado e dê espaço à próxima escolha. Nem tudo exige dados: uma conversa pode resolver um problema. Num combate, use os turnos e as ações de cada participante. Consulte a ficha para saber quais capacidades, equipamentos e recursos cada personagem possui, como pontos de vida (PV) e pontos de energia (PE).'),
  para('Por onde começar','h2'),
  para('Para sua primeira missão, leia <link href="#s007" color="#9e2358">A sessão zero</link>, <link href="#s001" color="#9e2358">Preparar uma missão</link> e <link href="#s004" color="#9e2358">Conduzir uma sessão</link>. Depois, acompanhe <link href="#x001" color="#9e2358">As batidas no anexo</link>, no apêndice C. Durante o jogo, as fichas do apêndice A ajudam a consultar e anotar o que importa.'),
  para('Regras, dicas e exemplos','h2'),
  para('<b>Regras do jogo.</b> Estão no Livro de Regras 1.0. Este Guia mostra como usá-las em situações de jogo e onde consultá-las.<br/><b>Dicas para o mestre.</b> Ajudam a preparar e conduzir a sessão. Adapte-as ao seu grupo e avise quando uma mudança afetar os jogadores.<br/><b>Exemplos experimentais.</b> São inimigos, perigos e outras criações que ainda precisam ser avaliados em jogo. Seus avisos indicam o que está sendo proposto. Os exemplos não são regras obrigatórias para toda a guilda.'),
  para('Encontre o que precisa','h2'),
  para('O sumário, as referências e os botões no rodapé são clicáveis. As páginas indicadas levam a trechos deste PDF. O Livro de Regras 1.0 é um volume separado. Use o índice para procurar um assunto e leia os exemplos conforme sua necessidade.')]
'''
t=t[:start]+front+t[end:]
repls=[('Sociedade, apoio e modos de vida','A sociedade jujutsu'),('Fichas do piloto: três inimigos','Três maldições para a missão'),('A entrega trocada: cotidiano acompanhado','A entrega trocada'),('reparos da R53','reparos do Livro de Regras 1.0'),("'Como usar este Guia'","'Como usar este livro'"),('Pareceres, montagem e poderes avançados.','Avaliação, montagem e poderes avançados.'),('os procedimentos do Guia','as orientações do Guia'),
('Livro de regras Ciclo Maldito, revisão R53. O Guia conserva a separação entre regras publicadas, orientações da campanha e exemplos experimentais. O Bestiário antigo não forneceu os números das novas fichas. Os procedimentos de dedicação e os exemplos aprovados permanecem no escopo registrado pelo autor.','Ciclo Maldito — Livro de Regras 1.0. Este Guia distingue as regras do jogo, as orientações para a campanha e os exemplos experimentais. Os inimigos novos usam fichas próprias, preparadas a partir do livro de regras; seus números não vêm do Bestiário antigo.'),
('acervo da R53','acervo do Livro de Regras 1.0'),('para a R53','para o Livro de Regras 1.0'),('perfil de densidade da R53','formato do Livro de Regras 1.0'),
('A revisão organiza o percurso, corrige remissões e distingue procedimentos concluídos de expansões ainda pendentes.','A revisão simplifica a linguagem, organiza os títulos e confere as referências.'),('passagens confrontadas com a R53','conferências de texto'),('referência R53','referência Livro de Regras 1.0')]
for a,b in repls:
 assert a in t or b in t,a
 t=t.replace(a,b)
p.write_text(t)
print('aliases',sum(map(len,aliases.values())),'titles',len(main_titles))

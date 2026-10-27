#!/usr/bin/env python3
"""Organiza a edição local de leitura; preserva regras e registra as fontes e cortes editoriais."""
from pathlib import Path
from urllib.parse import urlsplit,unquote,quote
import argparse,hashlib,html,json,os,re
import markdown
from bs4 import BeautifulSoup
from markdown.extensions.toc import slugify

AP=argparse.ArgumentParser(description=__doc__);AP.add_argument('--raiz',type=Path);AP.add_argument('--preparado',type=Path);AP.add_argument('--saida',type=Path);args=AP.parse_args()
HERE=Path(__file__).absolute().parent;R=args.raiz or HERE.parent;E=args.saida or HERE;G='06 - Redacao do Guia';P='04 - Planejamento';E.mkdir(parents=True,exist_ok=True)
def src(rel):return args.preparado/rel if args.preparado and (args.preparado/rel).is_file() else R/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def esc(s):return html.escape(str(s),quote=True)
def wr(rel,t):p=E/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t)
def jw(rel,x):wr(rel,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
CHAPTERS=[
 ('C01','Mundo, cotidiano e grupo',[6,86,7,9],'Entre pelo cotidiano e combine o que o grupo quer jogar. Quem conhece a obra pode avançar para a formação do grupo.'),
 ('C02','Preparar missões e campanhas',[1,3,13,14,15,17,18,19],'Prepare uma situação, encontre pessoas e acessos, e acompanhe as consequências entre missões.'),
 ('C03','Conduzir a sessão',[4,82,10,83,11,84,85],'Descreva, resolva tentativas, distribua participação e torne informação e espaço utilizáveis.'),
 ('C04','Inimigos, encontros e perigos',[56,57,59,60,74,100,62,63,64,65,66,67,71,72,73,75,76,101,102,78,79,103],'Escolha a função da ameaça, prepare respostas e objetivo, e confira recursos e oportunidades de agir.'),
 ('C05','Recursos, derrota e continuidade',[21,22,23],'Acompanhe custos e condições, resolva socorro e organize retirada e recuperação.'),
 ('C06','Personagens, vínculos e cuidados',[25,26,27,89,90,91,92],'Confira fichas, relações e meios de agir; combine convivências e cuidados de cada personagem.'),
 ('C07','Avaliar técnicas e criações',[29,30,31,33,93,94,95],'Transforme uma ideia em proposta verificável e acompanhe custos, limites, usos e ajustes.'),
 ('C08','Ofícios, equipamento e tempo',[34,35,36,96,97,98,37,99,39],'Prepare projetos e serviços, reconheça recompensas e registre atividades fora de missão.'),
 ('C09','Pactos e entidades',[41,47,48,49,50,43,51,52,53,54,45,46,55],'Conduza trocas, aquisições e projetos com requisitos, estados e encerramentos definidos.'),
 ('C10','Consulta e passagem entre mestres',[80,81],'Escolha os registros necessários e entregue o estado que permite continuar uma missão.')]
TOOLS=[8,2,5,12,16,20,24,28,32,38,40,42,44,58,77,61,68]
ESSENTIAL=[6,7,1,4,13,56,21,22,25,29,34,39,41,43,80]
files={int(p.name.split('-')[0]):str(p.relative_to(R)) for p in (R/G).glob('*.md') if p.name.split('-')[0].isdigit()}
assert set(files)==set(range(1,104))
flat=[n for _,_,ns,_ in CHAPTERS for n in ns]+TOOLS+[88,87,69,70];assert len(flat)==len(set(flat))==103
sections={};pages=[];cuts=[];refs={};broken=[]
def clean(rel,key):
 t=src(rel).read_text();lines=t.splitlines();title=lines[0].lstrip('# ').strip();body='\n'.join(lines[1:]).strip()
 if key=='s092':
  a=body.index('## Histórico da proposta');cuts.append(dict(fonte=rel,motivo='Histórico de modelos descartados permanece na produção, fora da consulta de leitura.',trecho=body[a:]));body=body[:a].rstrip()
  old=body.split('\n\n',1)[0];new='Esta consulta orienta o acordo por personagem previsto na R53. O Guia mantém a habilidade publicada e não adota um modelo numérico geral para ela.';cuts.append(dict(fonte=rel,motivo='Abertura dirigida ao leitor; decisão autoral preservada no registro de produção.',trecho=old));body=body.replace(old,new,1)
 blocks=re.split(r'\n\s*\n',body);kept=[]
 for b in blocks:
  if re.match(r'^(?:\*\*(?:Próxima tarefa(?: recomendada)?|Estado da produção|Cobertura vigente):\*\*|Versão piloto \d)',b):cuts.append(dict(fonte=rel,motivo='Recado de produção, preservado na fonte.',trecho=b));continue
  kept.append(b)
 body='\n\n'.join(kept)
 return title,body
def register(key,rel,page,group,kind):
 title,body=clean(rel,key);soup=BeautifulSoup(markdown.markdown(body,extensions=['tables','fenced_code','sane_lists','toc']), 'html.parser');anchors={};heads=[]
 for node in soup.find_all(attrs={'id':True}):
  old=node['id'];new=key+'--'+old;anchors[old]=new;node['id']=new
 for h in soup.find_all(re.compile('^h[1-6]$')):
  heads.append(dict(texto=h.get_text(' ',strip=True),id=h.get('id')));h.name='h'+str(min(6,int(h.name[1])+1))
 sections[key]=dict(id=key,fonte=rel,sha256=sha(src(rel)),titulo=title,corpo_md=body,soup=soup,ancoras=anchors,cabecalhos=heads,pagina=page,grupo=group,tipo=kind)
 return key
for code,title,ns,desc in CHAPTERS:
 page='capitulos/'+code.lower()+'.html';keys=[register(f's{n:03}',files[n],page,code,'capitulo') for n in ns];pages.append(dict(path=page,code=code,title=title,desc=desc,keys=keys))
keys=[register(f's{n:03}',files[n],'consultas/fichas-de-mesa.html','FICHAS','ferramenta') for n in TOOLS];pages.append(dict(path='consultas/fichas-de-mesa.html',code='FICHAS',title='Fichas e exemplos de registro',desc='Escolha uma folha pelo trabalho que precisa acompanhar. As duas conferências específicas e o exemplo de encontro são aprofundamentos opcionais.',keys=keys))
register('s088',files[88],'consultas/termos-do-mundo.html','TERMOS','indice');pages.append(dict(path='consultas/termos-do-mundo.html',code='TERMOS',title='Índice de termos do mundo',desc='Consulta sem revelações da trama.',keys=['s088']))
pilot=[register('x001',P+'/13-piloto-editorial-ocorrencia-sobrenatural.md','consultas/piloto-comentado.html','PILOTO','exemplo'),register('x002',P+'/14-base-pequena-de-inimigos-r53.md','consultas/piloto-comentado.html','PILOTO','fichas')];pages.append(dict(path='consultas/piloto-comentado.html',code='PILOTO',title='Uma missão acompanhada',desc='As batidas no anexo, com preparo comentado, confronto, socorro e as fichas experimentais do piloto.',keys=pilot))
register('s087',files[87],'aprofundamentos/casos-da-obra-com-revelacoes.html','OBRA','revelacoes');pages.append(dict(path='aprofundamentos/casos-da-obra-com-revelacoes.html',code='OBRA',title='Casos da obra — contém revelações',desc='Leitura opcional. Discute acontecimentos posteriores a Shibuya e o Jogo do Abate. O corpo desta consulta fica fora da busca geral e do manuscrito principal.',keys=['s087']))
by_source={os.path.normpath(str(R/s['fonte'])):s for s in sections.values()}
history={os.path.normpath(str(R/files[n])):f'estudo-s{n:03}' for n in [69,70]}
def relative(page,target):return quote(os.path.relpath(E/target,(E/page).parent),safe='/#')
def section_link(page,key,fragment='',md=False):
 s=sections[key];anchor=s['ancoras'].get(fragment) if fragment else key
 if fragment and not anchor:
  normalized=slugify(fragment,'-');anchor=s['ancoras'].get(normalized)
  if not anchor:broken.append(dict(fonte=key,fragmento=fragment,motivo='fragmento não localizado'));anchor=key
 return ((s['pagina']+'#'+anchor) if s['tipo']=='revelacoes' else '#'+anchor) if md else relative(page,s['pagina'])+'#'+anchor
def target_for(rel,target,page,key,md=False):
 if re.match(r'^(?:https?|mailto|tel|data):',target):return target
 u=urlsplit(target)
 if not u.path:return section_link(page,key,unquote(u.fragment),md)
 absolute=os.path.normpath(str((R/rel).parent/unquote(u.path)))
 if absolute in by_source:return section_link(page,by_source[absolute]['id'],unquote(u.fragment),md)
 if absolute in history:return ('fontes-e-limites.html' if md else relative(page,'fontes-e-limites.html'))+'#'+history[absolute]
 if absolute not in refs:
  exists=Path(absolute).is_file()
  refs[absolute]=dict(id=f'ref-{len(refs)+1:03}',arquivo=absolute,origens=[rel],existe=exists)
  if not exists:broken.append(dict(fonte=rel,destino=target,motivo='arquivo não localizado'))
 elif rel not in refs[absolute]['origens']:refs[absolute]['origens'].append(rel)
 return ('fontes-e-limites.html' if md else relative(page,'fontes-e-limites.html'))+'#'+refs[absolute]['id']
for s in sections.values():
 for a in s['soup'].find_all('a',href=True):a['href']=target_for(s['fonte'],a['href'],s['pagina'],s['id'])
 for table in s['soup'].find_all('table'):
  wrap=s['soup'].new_tag('div',attrs={'class':'tabela','tabindex':'0','role':'region','aria-label':'Tabela; role horizontalmente se necessário'});table.wrap(wrap)
 for a in s['soup'].find_all('a',href=re.compile('^https?://')):a['rel']='noopener noreferrer'

def nav(page):
 entries=[('index.html','Início')]+[(p['path'],p['code']+' · '+p['title']) for p in pages if p['code']!='OBRA']+[('fontes-e-limites.html','Fontes e limites')]
 return '<nav class="lateral" aria-label="Capítulos"><strong>Guia do Mestre</strong><span>Pré-1.0 · revisão de leitura 1</span>'+''.join('<a '+('aria-current="page" ' if p==page else '')+'href="'+relative(page,p)+'">'+esc(t)+'</a>' for p,t in entries)+'</nav>'
def frame(page,title,content,code=''):
 return '<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' · Ciclo Maldito</title><link rel="stylesheet" href="'+relative(page,'estilos.css')+'"></head><body><a class="pular" href="#conteudo">Ir ao conteúdo</a>'+nav(page)+'<div class="pagina"><header class="barra"><a href="'+relative(page,'index.html')+'">Ciclo Maldito · Guia do Mestre</a><form id="busca" role="search"><label for="consulta">Buscar no Guia</label><input id="consulta" type="search" placeholder="Socorro, dedicação, Doma…" autocomplete="off"><button type="submit">Buscar</button></form></header><main id="conteudo" tabindex="-1"><p class="sobretitulo">'+esc(code or 'EDIÇÃO DE LEITURA')+'</p><h1>'+esc(title)+'</h1>'+content+'</main><footer>Pré-1.0 · revisão de leitura 1 · 26 de outubro de 2026. Propostas experimentais conservam a identificação em cada consulta. <a href="'+relative(page,'fontes-e-limites.html')+'">Fontes e limites</a></footer></div><dialog id="resultados" aria-labelledby="titulo-resultados"><div class="dialogo-topo"><h2 id="titulo-resultados">Resultados da busca</h2><button id="fechar-busca" type="button">Fechar</button></div><p id="resumo-busca" aria-live="polite"></p><ol id="lista-resultados"></ol></dialog><script>window.CM_ROOT='+json.dumps(relative(page,'index.html').rsplit('index.html',1)[0])+';</script><script src="'+relative(page,'dados-busca.js')+'"></script><script src="'+relative(page,'busca.js')+'"></script></body></html>'

for p in pages:
 page=p['path'];toc='<details class="sumario" open><summary>Nesta consulta</summary><ol>'+''.join('<li><a href="#'+k+'">'+esc(sections[k]['titulo'])+'</a></li>' for k in p['keys'])+'</ol></details>'
 warning='<aside class="aviso"><strong>Revelações importantes da trama.</strong> Abra esta consulta somente se quiser conhecer os acontecimentos discutidos. <a href="'+relative(page,'capitulos/c01.html')+'">Voltar à entrada sem revelações</a>.</aside>' if p['code']=='OBRA' else ''
 content='<p class="abertura">'+esc(p['desc'])+'</p>'+warning+toc
 for k in p['keys']:
  s=sections[k];badge=('Consulta '+str(int(k[1:]))) if k.startswith('s') else 'Piloto acompanhado'
  content+='<section class="consulta" id="'+k+'"><p class="etiqueta">'+badge+'</p><h2>'+esc(s['titulo'])+'</h2>'+str(s['soup'])+'</section>'
 if p['code'].startswith('C'):
  i=int(p['code'][1:]);links=[]
  if i>1:links.append('<a href="'+relative(page,f'capitulos/c{i-1:02}.html')+'">← Capítulo anterior</a>')
  if i<10:links.append('<a href="'+relative(page,f'capitulos/c{i+1:02}.html')+'">Próximo capítulo →</a>')
  content+='<nav class="sequencia" aria-label="Continuar leitura">'+''.join(links)+'</nav>'
 wr(page,frame(page,p['title'],content,p['code']))

front='''<p class="abertura">Este Guia ensina a mestrar Ciclo Maldito: preparar situações, conduzir escolhas e acompanhar o que muda na vida de quem enfrenta o sobrenatural.</p>
<p>O sistema tem a guilda como referência principal de organização. Personagens, missões e mestres podem compartilhar continuidade. Os procedimentos também atendem campanhas fechadas: mantenha o que ajuda sua mesa e ajuste a administração ao formato escolhido.</p>
<h2>Comece pelo que precisa fazer</h2><div class="rotas">'''
routes=[('Não conheço Jujutsu Kaisen','Conheça o cotidiano e as pessoas deste mundo. A entrada dispensa saber a trama.','capitulos/c01.html#s006'),('Já conheço a obra','Combine o grupo e avance para o preparo da missão.','capitulos/c01.html#s007'),('Quero preparar a primeira missão','Siga o procedimento e acompanhe As batidas no anexo.','capitulos/c02.html#s001'),('Preciso consultar durante a mesa','Abra as fichas e os registros; escolha uma folha por necessidade.','consultas/fichas-de-mesa.html'),('Quero ver uma missão completa','Leia o piloto comentado com as fichas do encontro.','consultas/piloto-comentado.html'),('Quero propor uma criação','Comece pelo resultado pretendido e confira aquisição, custos e limites.','capitulos/c07.html#s029')]
for title,desc,url in routes:front+='<a class="cartao" href="'+url+'"><strong>'+esc(title)+'</strong><span>'+esc(desc)+'</span></a>'
front+='</div><h2>Como o jogo avança</h2><p>Você apresenta uma situação e as informações que os personagens conseguem perceber. Os jogadores decidem o que tentar. Quando houver incerteza relevante, use o procedimento correspondente da R53 e descreva o resultado. Escolhas e consequências atualizam o estado da missão.</p><p>Num teste comum, role d20 e some o modificador pertinente. Igualar ou superar a dificuldade é sucesso. Ataques e testes de resistência têm procedimentos próprios; o Guia os explica nos casos de condução e remete ao Livro do Jogador. Custos, alcance, ações e condições pertencem à capacidade utilizada.</p><p>Antes de uma decisão, apresente o que os personagens podem reconhecer: acesso, sinais de perigo, meios disponíveis e objetivos. Depois de resolvê-la, registre o que efetivamente mudou. Uma solução eficiente também faz a história avançar.</p><h2>Um caminho essencial</h2><p>Leia as consultas abaixo conforme sua necessidade. Os demais casos aprofundam decisões específicas; o livro não exige passar por todos os exemplos antes de começar.</p><ol class="caminho">'
for n in ESSENTIAL:
 s=sections[f's{n:03}'];front+='<li><a href="'+s['pagina']+'#'+s['id']+'">'+esc(s['titulo'])+'</a></li>'
front+='</ol><h2>Capítulos</h2><ol class="capitulos">'
for p in pages:
 if p['code'].startswith('C'):front+='<li><a href="'+p['path']+'"><strong>'+p['code']+' · '+esc(p['title'])+'</strong></a><p>'+esc(p['desc'])+'</p></li>'
front+='</ol><h2>Como usar as remissões</h2><p>C01 a C10 identificam capítulos. Os números das consultas foram preservados para que remissões como “consulta 39” continuem fáceis de localizar; eles não determinam a ordem de leitura. A busca encontra títulos, termos e trechos do corpo das consultas. Os casos da obra com revelações ficam fora dessa busca.</p><h2>Regras, escolhas e exemplos</h2><p>A R53 é a referência mecânica. Orientações de preparo explicam como conduzir situações; parâmetros próprios de inimigos, perigos e outros casos conservam a identificação de proposta experimental. Uma escolha feita para um exemplo não se torna regra universal da guilda. Consulte as fontes e os limites quando precisar avaliar o alcance de um parecer.</p><p>Os exemplos usam nomes e recortes de personagem em diferentes níveis. Na mesa, utilize a versão efetiva de cada ficha. As referências parciais de cálculo não substituem personagens completos.</p><p>Esta é a primeira organização completa para leitura e revisão. Os casos receberam conferências documentais e de contas conforme seus registros. A compreensão por leitores e o funcionamento em mesa ainda precisam ser observados. O desenvolvimento mecânico de treinamentos e a atualização integral do Bestiário continuam para etapas próprias.</p><p class="opcional"><strong>Aprofundamento opcional:</strong> <a href="aprofundamentos/casos-da-obra-com-revelacoes.html">casos da obra com revelações importantes da trama</a>. A entrada do mundo e os procedimentos do Guia dispensam essa leitura.</p><p><a href="GUIA-DO-MESTRE-PRE-1.0.md">Manuscrito editável em Markdown</a> · <a href="fontes-e-limites.html">Fontes, propostas e histórico</a></p>'
wr('index.html',frame('index.html','Guia do Mestre — Ciclo Maldito',front))

# Uma versão editável contém os mesmos capítulos e consultas, sem o corpo dos casos com revelações.
book=['# Guia do Mestre — Ciclo Maldito','', '**Pré-1.0 · revisão de leitura 1 · 26 de outubro de 2026.**','', 'Ensina a mestrar Ciclo Maldito, com a guilda como referência principal e aplicações em campanhas fechadas. R53 é a base mecânica. Exemplos experimentais conservam seus avisos; não representam aprovação universal.','', 'Para navegação, busca e percurso essencial, abra [a edição de leitura](index.html). Os casos da obra com revelações ficam em [consulta opcional sinalizada](aprofundamentos/casos-da-obra-com-revelacoes.html), fora deste manuscrito principal.','', '## Sumário','']
main_pages=[p for p in pages if p['code']!='OBRA']
for p in main_pages:book.append('- ['+p['code']+' — '+p['title']+'](#cap-'+p['code'].lower()+')')
for p in main_pages:
 book+=['','<a id="cap-'+p['code'].lower()+'"></a>','', '# '+p['code']+' — '+p['title'],'',p['desc'],'']
 for key in p['keys']:
  s=sections[key];body=s['corpo_md']
  body=re.sub(r'\[([^\]\n]+)\]\((<[^>]+>|[^)]+)\)',lambda m:'['+m[1]+']('+target_for(s['fonte'],m[2].strip('<>'),'GUIA-DO-MESTRE-PRE-1.0.md',key,True)+')',body)
  used={};lines=[];code=False
  for line in body.splitlines():
   if line.startswith('```'):code=not code
   m=re.match(r'^(#{1,6}) (.+)',line) if not code else None
   if m:
    base=slugify(re.sub('<[^>]+>','',m[2]),'-');count=used.get(base,0);used[base]=count+1;oid=base+(f'_{count}' if count else '');aid=s['ancoras'].get(oid)
    if aid:lines+=['<a id="'+aid+'"></a>','']
    line='#'*min(6,len(m[1])+1)+' '+m[2]
   lines.append(line)
  book+=['<a id="'+key+'"></a>','', '## '+s['titulo'],'','\n'.join(lines),'']
wr('GUIA-DO-MESTRE-PRE-1.0.md','\n'.join(book))

sources='<p class="abertura">Base mecânica, alcance dos exemplos e referências de consulta.</p><h2>Base e limites da edição</h2><p>O Livro do Jogador R53 fundamenta os procedimentos. Esta integração organiza textos existentes, remissões e caminhos de leitura. Ela não altera a R53, aprova uma escala de dificuldade ou certifica equilíbrio. Reserva Condensada conserva o acordo por personagem publicado; os modelos numéricos descartados não foram incorporados.</p><p>Fichas, perigos, Pactos e projetos próprios mantêm as escolhas e os avisos experimentais em seus textos. Decisões para uma ocorrência não se tornam regras gerais por aparecerem neste livro. Consulte a versão usada na missão.</p><h2>Estudos preservados fora da leitura principal</h2>'
for n in [69,70]:sources+='<section id="estudo-s'+f'{n:03}'+'"><h3>'+esc(src(files[n]).read_text().splitlines()[0].lstrip('# '))+'</h3><p>Estudo histórico de movimento reservado, retirado da recomendação principal de chefe após a revisão autoral. A leitura principal apresenta o Sineiro e as comparações posteriores. O estudo continua preservado na pasta de produção.</p></section>'
sources+='<h2>Materiais de estudo e produção citados</h2><p>Estas remissões levam às fontes locais que acompanham o projeto. O livro de leitura funciona sem abrir o histórico; uma ficha ou regra necessária à aplicação permanece no corpo da consulta correspondente.</p><dl class="referencias">'
for absolute,r in refs.items():
 url=quote(os.path.relpath(absolute,R/'07 - Edicao de Leitura'),safe='/');label=os.path.relpath(absolute,R) if absolute.startswith(str(R)+os.sep) else absolute
 sources+='<div id="'+r['id']+'"><dt><a href="'+url+'">'+esc(label)+'</a></dt><dd>Referência de estudo ou produção; consulte para origem, contas e alcance da conferência.</dd></div>'
sources+='</dl><h2>Fontes da obra</h2><p>As fontes primárias e seus limites permanecem junto das passagens que as usam, nas consultas de mundo e nos aprofundamentos sinalizados. Esta integração não acrescenta pesquisa de lore ou novas interpretações canônicas.</p><h2>Como enviar uma observação</h2><p>Registre a revisão lida, o capítulo e a consulta, o trecho que gerou dificuldade e o que aconteceu na leitura ou na mesa. Se houver uma sugestão, anote-a separadamente. Assim é possível avaliar uma explicação confusa sem assumir automaticamente uma mudança de regra.</p><p>Treinamentos novos, escala geral de dificuldade e Bestiário integral têm desenvolvimento posterior. O retorno de leitores pode chegar durante a revisão do manuscrito.</p>'
wr('fontes-e-limites.html',frame('fontes-e-limites.html','Fontes e limites',sources))
index=[]
for s in sections.values():
 if s['tipo']=='revelacoes':continue
 text=s['soup'].get_text(' ',strip=True);index.append(dict(id=s['id'],titulo=s['titulo'],grupo=s['grupo'],url=s['pagina']+'#'+s['id'],texto=text))
wr('dados-busca.js','window.CM_SEARCH='+json.dumps(index,ensure_ascii=False).replace('</','<\\/')+';\n')
jw('mapa-editorial.json',dict(edicao='pré-1.0 — revisão de leitura 1',data='2026-10-26',capitulos=[dict(codigo=p['code'],titulo=p['title'],pagina=p['path'],consultas=p['keys']) for p in pages],fontes=[{k:v for k,v in s.items() if k not in ['soup','corpo_md']} for s in sections.values()],historicos_excluidos=[dict(fonte=files[n],sha256=sha(src(files[n])),motivo='Estudo de chefe retirado da recomendação principal por revisão autoral.') for n in [69,70]],cortes_editoriais=cuts,referencias_externas=list(refs.values()),problemas=broken,limites='Integração estrutural e navegação. Sem nova revisão semântica integral de cada passagem, sessão humana, equilíbrio certificado ou alteração da R53.'))
print(json.dumps(dict(fontes_incorporadas=len(sections),consultas_busca=len(index),capitulos=10,paginas_consulta=len(pages)-10,historicos_fora_do_corpo=2,cortes_editoriais=len(cuts),problemas=broken),ensure_ascii=False,indent=2))
assert not broken,broken

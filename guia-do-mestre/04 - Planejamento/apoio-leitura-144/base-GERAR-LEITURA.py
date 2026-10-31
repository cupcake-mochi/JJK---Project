"""Reunir a edição local sem ligações ao acervo de trabalho; manter 3a dentro de 3.6."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from html import escape
import json,re,os,hashlib,shutil,markdown
from bs4 import BeautifulSoup

A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def title(p):return re.search(r'^#\s+(.+)$',p.read_text(),re.M).group(1)
def save(name,x):(A/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def main():
 entries=json.loads((A/'base-fontes-reunidas.json').read_text());old=json.loads((R/'04 - Planejamento/apoio-conferencia-135/destinos-e-fontes.json').read_text())
 groups={'B1':'Testes, percepção e movimento','B2':'Confrontos e perigos','B3':'Personagens e técnicas','B4':'Objetos e recompensas','B5':'Pactos e entidades'}
 grouped={k:[T/'casos'/Path(row['fonte_revisada']).name for row in rows] for k,rows in old['casos'].items()}
 grouped['B2'].insert(0,T/'casos/14-tres-maldicoes-para-a-missao.md');grouped['B3'].insert(0,T/'casos/27-convivencia-do-receptaculo.md')
 grouped['B3'].append(T/'consultas/92-reserva-condensada-proposta-e-comparacao.md')
 text='# Casos por assunto\n\nEscolha a dúvida que precisa aprofundar. O capítulo principal apresenta o método; os casos mostram sua aplicação, seus limites e o que registrar. As fichas experimentais conservam esse alcance.\n\n'
 methods={'B1':'04-na-mesa-de-jogo.md','B2':'06-inimigos-e-perigos.md','B3':'07-personagens-e-tecnicas.md','B4':'08-entre-missoes.md','B5':'09-pactos-e-entidades.md'}
 for key,name in groups.items():
  text+=f'<a id="{key}"></a>\n\n## {name}\n\n[Explicação principal](<{methods[key]}>)\n\n'
  for p in grouped[key]:text+=f'- [{title(p)}](<{p.relative_to(T).as_posix()}>).\n'
  text+='\n'
 (T/'indice-de-casos.md').write_text(text)
 core=sorted([p for p in T.glob('*.md') if re.match(r'^\d',p.name)])
 cases=[p for rows in grouped.values() for p in rows if p.parent.name=='casos']
 leaves=sorted((T/'consultas').glob('*.md'))
 units=core+sorted(set(cases))+leaves+[T/'indice-de-casos.md',T/'referencias.md']
 assert len(units)==len(set(units))==99,len(units)
 docs={p:BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','toc','fenced_code']),'html.parser') for p in units}
 names={};roles={}
 for p in units:
  if p.parent==T and re.match(r'^\d',p.name):
   number=p.name.split('-')[0];names[p]='como-usar.html' if number=='00' else ('capitulo-03.html' if number=='03a' else f'capitulo-{number}.html');roles[p]='Comece a mestrar' if number[:2]<='05' else 'Ferramentas de Ciclo Maldito'
  elif p.name=='indice-de-casos.md':names[p]='casos.html';roles[p]='Apêndice B'
  elif p.name=='referencias.md':names[p]='referencias.html';roles[p]='Referências'
  elif p.name=='LEIA-ME.md':names[p]='folhas.html';roles[p]='Apêndice A'
  elif p.name.startswith('87-'):names[p]='apendice-d.html';roles[p]='Aprofundamento com revelações'
  elif p.name.startswith('88-'):names[p]='apendice-c.html';roles[p]='Apêndice C'
  else:
   names[p]=('caso-' if p.parent.name=='casos' else 'consulta-')+p.stem+'.html';roles[p]='Apêndice B' if p.parent.name=='casos' or p.name.startswith('92-') else 'Apêndice A'
 special=next(p for p in core if p.name.startswith('03a-'));chapter3=T/'03-preparar-aventuras.md'
 # Os IDs do complemento têm prefixo porque agora compartilham a página do capítulo 3.
 ids={p:{tag['id']:tag['id'] for tag in soup.find_all(id=True)} for p,soup in docs.items()}
 for tag in docs[special].find_all(id=True):
  oldid=tag['id'];tag['id']='ideias--'+oldid;ids[special][oldid]=tag['id']
 linklog=[]
 for p,soup in docs.items():
  for tag in soup.find_all(['a','img']):
   attribute='href' if tag.name=='a' else 'src';value=tag.get(attribute)
   if not value:continue
   u=urlsplit(value)
   if u.scheme:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   if target in names:
    fragment=ids[target].get(unquote(u.fragment),unquote(u.fragment)) if u.fragment else ('ideias' if target==special else '')
    tag[attribute]=names[target]+('#'+fragment if fragment else '')
    if names[target]=='apendice-d.html' and names[p]!='apendice-d.html':
     tag['class']=tag.get('class',[])+['spoiler-link'];tag['title']='Contém revelações da trama'
     if 'revelaç' not in tag.get_text().lower():tag.append(' (revelações)')
   elif target.is_relative_to(E.resolve()):tag[attribute]=os.path.relpath(target,E)
   else:raise AssertionError((p,value,target))
   linklog.append({'fonte':p.relative_to(T).as_posix(),'antes':value,'depois':tag[attribute]})
  for table in soup.find_all('table'):
   wrapper=soup.new_tag('div',attrs={'class':'quadro'});table.wrap(wrapper)
  for pre in soup.find_all('pre'):pre['class']=pre.get('class',[])+['esquema']
 maps={
  '62-o-carregador-e-o-corredor-de-entulho.md':('carregador','Duas rotas até o recuo. Distâncias físicas; o entulho altera o custo de movimento.'),
  '64-a-passarela-e-o-guincho.md':('passarela','Passarela, guincho e caminho inferior, com as medidas usadas no exemplo.'),
  '66-o-carregador-e-a-saida-que-fecha.md':('portao','Portão, caixa e rota de serviço. Os dois caminhos conservam suas distâncias.'),
  '73-ensaio-guiado-do-sineiro.md':('sineiro','Posições iniciais do ensaio. Cada célula mede 1,5 m.'),
  '76-confronto-de-ren-e-sora.md':('dupla','Toru e Sayo nas posições iniciais do confronto. Cada célula mede 1,5 m.'),
  '79-o-po-na-sala-de-conservacao.md':('po','Sala de conservação, fecho, pino e exaustor, com Mei e Akira na entrada.'),
  '102-o-arquivo-e-as-oportunidades-de-agir.md':('arquivo','Escolha uma versão: Daigo sozinho ou Vigia e Tessa. O grupo começa na linha 0.')}
 for p,soup in docs.items():
  if p.name not in maps:continue
  name,caption=maps[p.name];assert (E/f'assets/mapas/{name}.svg').is_file(),name
  figure=soup.new_tag('figure');figure.append(soup.new_tag('img',src=f'assets/mapas/{name}.svg',alt=caption))
  legend=soup.new_tag('figcaption');legend.string=caption;figure.append(legend)
  pre=soup.find('pre')
  if pre:pre.replace_with(figure)
  else:
   firsttable=soup.find('div',class_='quadro');assert firsttable,p.name;firsttable.insert_after(figure)
 # Inserção sem duplicação do capítulo de ideias.
 mainhead=docs[special].find('h1');headid=mainhead.get('id');mainhead.decompose()
 for h in docs[special].find_all(re.compile('^h[2-5]$')):h.name='h'+str(int(h.name[1])+1)
 addon=docs[chapter3].new_tag('section',id='ideias',attrs={'class':'ideias'})
 if headid:addon.append(docs[chapter3].new_tag('span',id=headid))
 for child in list(docs[special].contents):addon.append(child.extract())
 nextsection=docs[chapter3].find(id='37-quando-ha-pouco-tempo');assert nextsection
 nextsection.insert_before(addon)
 # Copiar somente fontes e licenças necessárias à leitura portátil.
 fontdir=E/'assets/fontes';fontdir.mkdir(parents=True,exist_ok=True)
 sourcefonts=R/'08 - Diagramacao do Guia/fontes'
 for name in ['Spectral-Regular.ttf','Spectral-SemiBold.ttf','Spectral-Italic.ttf','BarlowCondensed-Bold.ttf','BreeSerif.ttf']:
  shutil.copyfile(sourcefonts/name,fontdir/name)
 for p in sourcefonts.glob('*'):
  if p.suffix.lower() in ['.txt','.md']:shutil.copyfile(p,fontdir/p.name)
 css='''@font-face{font-family:Spectral;src:url(assets/fontes/Spectral-Regular.ttf)}@font-face{font-family:Spectral;src:url(assets/fontes/Spectral-SemiBold.ttf);font-weight:600}@font-face{font-family:Spectral;src:url(assets/fontes/Spectral-Italic.ttf);font-style:italic}@font-face{font-family:Barlow;src:url(assets/fontes/BarlowCondensed-Bold.ttf);font-weight:700}@font-face{font-family:Bree;src:url(assets/fontes/BreeSerif.ttf)}
 :root{--tinta:#251727;--acento:#9e2358;--claro:#f8f1f4}*{box-sizing:border-box}body{margin:0;background:#f1edf0;color:var(--tinta);font:19px/1.65 Spectral,Georgia,serif}a{color:var(--acento);text-underline-offset:.15em}header{background:#251727;color:white;padding:18px max(20px,calc((100vw - 1050px)/2));font:16px/1.5 system-ui,sans-serif}header a{color:white;margin-right:22px;display:inline-block}main{background:white;max-width:1050px;margin:28px auto;padding:42px 64px;box-shadow:0 2px 12px #25172712}article{max-width:82ch;margin:auto}h1,h2{font-family:Barlow,sans-serif;line-height:1.13;color:var(--acento)}h1{font-size:44px;margin:0 0 24px}h2{font-size:32px;margin:36px 0 16px}h3{font:24px/1.25 Bree,serif;margin:26px 0 12px}h4{font:600 20px/1.3 Spectral,serif;margin:24px 0 10px}p{margin:0 0 18px}li{margin:6px 0}strong{font-weight:600}.parte{font:14px/1.4 system-ui,sans-serif;letter-spacing:.03em;color:#765f70;margin-bottom:12px}.quadro{overflow-x:auto;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:17px;line-height:1.45}th,td{padding:10px 12px;border-bottom:1px solid #ded4d9;text-align:left;vertical-align:top}th{background:var(--claro);font-weight:600}tbody tr:nth-child(even){background:#fcf9fb}blockquote{border-left:3px solid var(--acento);background:var(--claro);padding:14px 18px;margin:22px 0}blockquote p:last-child{margin-bottom:0}.esquema{overflow-x:auto;white-space:pre;background:#f8f5f7;padding:18px;font:14px/1.5 monospace}img{display:block;max-width:100%;height:auto;margin:24px auto}footer{border-top:1px solid #ded4d9;margin-top:40px;padding-top:18px;font:15px/1.7 system-ui,sans-serif;display:flex;gap:24px;justify-content:space-between}.sumario{background:var(--claro);padding:16px 22px;margin:20px 0 30px;font-size:17px}.sumario ul{margin:5px 0;padding-left:22px}.spoiler-link{font-weight:600}.aviso{border:1px solid var(--acento);padding:20px;background:var(--claro)}.portas{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.portas section{background:var(--claro);padding:20px}.portas h2{font-size:26px;margin:0 0 12px}.portas p{font-size:17px}figcaption{font-size:15px;color:#665261;margin:-12px 0 24px}button{font:inherit}.ideias>p{margin-bottom:18px}
 @media(max-width:760px){body{font-size:18px}main{margin:0;padding:28px 22px;box-shadow:none}h1{font-size:37px}h2{font-size:29px}.portas{grid-template-columns:1fr}table{font-size:16px}}
 @media print{@page{size:A4;margin:19mm}body{background:white;font-size:10.25pt;line-height:13.2pt}header,footer,.sumario{display:none}main{margin:0;padding:0;box-shadow:none;max-width:none}h1{font-size:27pt}h2{font-size:18pt}h3{font-size:12.5pt}h1,h2,h3{break-after:avoid}table{font-size:9.2pt;line-height:11.5pt}tr{break-inside:avoid}.quadro{overflow:visible}p{orphans:3;widows:3}.esquema{font-size:8pt}}
 '''
 (E/'leitura.css').write_text(css)
 def document(heading,body,role='Guia do Mestre',previous=None,next_=None):
  nav='<header><a href="index.html">Ciclo Maldito · Guia do Mestre</a><a href="folhas.html">Folhas para a mesa</a><a href="casos.html">Casos por assunto</a><a href="apendice-c.html">Termos do mundo</a></header>'
  next_label='Aprofundamento com revelações →' if next_=='apendice-d.html' else 'Próxima leitura →'
  previous_label='← Aprofundamento com revelações' if previous=='apendice-d.html' else '← Leitura anterior'
  foot='<footer>'+('<a href="'+previous+'">'+previous_label+'</a>' if previous else '<a href="index.html">Voltar ao sumário</a>')+('<a href="'+next_+'">'+next_label+'</a>' if next_ else '<a href="index.html">Voltar ao sumário</a>')+'</footer>'
  return '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(heading)+' | Ciclo Maldito</title><link rel="stylesheet" href="leitura.css"></head><body>'+nav+'<main><p class="parte">'+escape(role)+'</p><article>'+body+'</article>'+foot+'</main></body></html>'
 reading=[p for p in core if p!=special]+[T/'consultas/LEIA-ME.md',T/'indice-de-casos.md']
 reading+=list(dict.fromkeys(p for rows in grouped.values() for p in rows))
 reading+=[p for p in leaves if p not in reading and not p.name.startswith(('87-','88-'))]
 reading+=[T/'consultas/88-indice-de-termos-do-mundo.md',T/'consultas/87-casos-da-obra-para-preparar-situacoes.md',T/'referencias.md']
 assert len(reading)==98 and len(set(reading))==98,len(reading)
 for i,p in enumerate(reading):
  soup=docs[p]
  toc=[h for h in soup.find_all('h2',id=True)]
  if toc:
   nav=soup.new_tag('nav',attrs={'class':'sumario','aria-label':'Nesta leitura'})
   nav.append(BeautifulSoup('<strong>Nesta leitura</strong><ul>'+''.join('<li><a href="#'+h['id']+'">'+escape(h.get_text())+'</a></li>' for h in toc)+'</ul>','html.parser'))
   soup.find('h1').insert_after(nav)
  if names[p]=='apendice-d.html':
   warning=soup.new_tag('p',attrs={'class':'aviso'});warning.string='Este aprofundamento contém revelações da trama. A entrada sobre o mundo e os demais capítulos podem ser usados sem esta leitura.';soup.find('h1').insert_before(warning)
  (E/names[p]).write_text(document(title(p),str(soup),roles[p],names[reading[i-1]] if i else None,names[reading[i+1]] if i+1<len(reading) else None))
 front='<h1>Ciclo Maldito<br>Guia do Mestre</h1><p>Prepare sua primeira missão, acompanhe as escolhas do grupo e encontre as ferramentas de que precisa para continuar. O Guia ensina a mestrar o sistema com atenção à vida dos feiticeiros e ao jogo em guilda; as orientações também servem a campanhas fechadas.</p><div class="portas"><section><h2>Vou começar</h2><p>Uma missão reúne preparo, descrição, escolhas, combate e socorro.</p><a href="capitulo-01.html">Sua primeira missão</a></section><section><h2>Vou preparar</h2><p>Crie outra aventura e escolha uma folha para organizar o necessário.</p><a href="capitulo-03.html">Preparar aventuras</a></section><section><h2>Quero consultar</h2><p>Encontre o assunto e acompanhe um exemplo completo.</p><a href="casos.html">Casos por assunto</a></section></div><h2>Como usar</h2><p><a href="como-usar.html">Escolha seu caminho de leitura</a>. Quem ainda não conhece Jujutsu Kaisen encontra uma entrada sobre o mundo sem depender da trama.</p><h2>Comece a mestrar</h2><ol>'
 for p in core:
  if p.name.startswith(('00-','03a-')):continue
  n=int(p.name[:2])
  if n==6:front+='</ol><h2>Ferramentas de Ciclo Maldito</h2><ol start="6">'
  front+='<li><a href="'+names[p]+'">'+escape(title(p))+'</a></li>'
 front+='</ol><h2>Consulta</h2><ul><li><a href="folhas.html">A · Folhas para a mesa</a></li><li><a href="casos.html">B · Casos por assunto</a></li><li><a href="apendice-c.html">C · Termos do mundo</a></li><li><a href="apendice-d.html" class="spoiler-link">D · Ideias da obra para suas missões (revelações da trama)</a></li><li><a href="referencias.html">Referências</a></li></ul>'
 (E/'index.html').write_text(document('Guia do Mestre',front,previous=None,next_='como-usar.html'))
 result={'registro':143,'fontes_reunidas':97,'fontes_geradas':['indice-de-casos.md','referencias.md'],'fontes_em_leitura':len(units),'paginas_de_conteudo':len(reading),'indice_geral':'index.html','ordem':[{'fonte':p.relative_to(R).as_posix(),'pagina':names[p],'titulo':title(p),'parte':roles[p],'sha256':sha(p)} for p in reading],'complemento_incluido':{'fonte':special.relative_to(R).as_posix(),'pagina':names[special],'ancora':'ideias','entre':'3.6 e 3.7'},'rotas':[{'fonte':p.relative_to(R).as_posix(),'pagina':names[p],'ancoras':ids[p]} for p in units],'links_convertidos':len(linklog)}
 save('composicao.json',result);save('remissoes-renderizadas.json',linklog)
 print(json.dumps({k:result[k] for k in ['fontes_reunidas','fontes_em_leitura','paginas_de_conteudo','links_convertidos']},ensure_ascii=False))

if __name__=='__main__':main()

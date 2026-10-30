"""Criar índice atual sem alterar os pacotes e filas históricos."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
from html import escape
import hashlib,json,markdown,os
A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,d):(A/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def local(target):
 path,sep,frag=target.partition('#');return os.path.relpath(R/path,A)+('#'+frag if sep else '')
MOTIVO='Duas passagens de clareza; remissões apontadas para os capítulos novos e cópias revistas; linhas de preenchimento na prova. Campos e números preservados.'
def main():
 data=load(R/'04 - Planejamento/apoio-revisao-textual-130/destinos-e-fontes.json');meta=load(A/'amostra.json');new={f['fonte_id']:f for f in meta['fontes']}
 data['registro']=131;data['revisao_das_rotas']=131;data['limite']='Os 59 casos têm cópias revistas nos registros 114 e 117–130; as consultas complementares começam a ser revistas no 131. Outros casos, consultas e integração continuam pendentes.'
 routes=load(R/'04 - Planejamento/apoio-revisao-textual-130/rotas-de-consulta.json');routes['registro']=131
 routes.setdefault('consultas_revisadas',{})
 for f in meta['fontes']:
  routes['consultas_revisadas'][f['fonte_id']]={'fonte_revisada':f['fonte'],'consulta_atual':meta['html']+'#'+f['id'],'motivo':MOTIVO}
 data['rotas']=routes;save('destinos-e-fontes.json',data);save('rotas-de-consulta.json',routes)
 css=BeautifulSoup((R/'04 - Planejamento/apoio-consultas-105/casos-completos.html').read_text(),'html.parser').style.get_text();groups={'B1':'Testes, percepção e movimento','B2':'Confrontos e perigos','B3':'Personagens e técnicas','B4':'Objetos e recompensas','B5':'Pactos e entidades'}
 structure=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json');old={f['fonte']:f for f in load(R/'07 - Edicao de Leitura/mapa-editorial.json')['fontes']};sections=[]
 md='# Casos por assunto — registro 131\n\nOs 59 casos revistos; consultas complementares em revisão. Nenhum caso ainda na edição anterior até sua revisão. Métodos 112–115 e folhas 116 permanecem atuais.\n\n'
 for code,title in groups.items():
  route=routes['grupos'][code];refs=[]
  for ident in route['folhas']:
   f=next(f for f in structure['fontes'] if f['id']==ident);o=old[f['fonte']];cr=routes.get('consultas_revisadas',{}).get(ident);refs.append('<a href="'+escape(local(cr['consulta_atual']) if cr else local('07 - Edicao de Leitura/'+o['pagina']+'#'+o['id']),quote=True)+'">'+escape(f['titulo_atual'])+'</a>'+(' — revista' if cr else ''))
  intro='<p><a href="'+escape(local(route['metodo']),quote=True)+'">Ler a explicação principal</a></p><p>Folhas completas: '+' · '.join(refs)+'.</p>'
  if route.get('consulta_publicada'):
   f=next(f for f in structure['fontes'] if f['id']==route['consulta_publicada']);o=old[f['fonte']];intro+='<p><a href="'+escape(local('07 - Edicao de Leitura/'+o['pagina']+'#'+o['id']),quote=True)+'">Reserva Condensada: habilidade publicada</a></p>'
  cards=[];md+='## '+title+'\n\n[Explicação principal](<'+local(route['metodo'])+'>)\n\n'
  for f in data['casos'][code]:
   suffix=' — texto revisto' if f.get('fonte_revisada') else ''
   cards.append('<li><a href="'+escape(local(f['consulta_atual']),quote=True)+'">'+escape(f['titulo'])+'</a>'+suffix+'</li>')
   md+='- ['+f['titulo']+'](<'+local(f['consulta_atual'])+'>)'+suffix+'.\n'
  sections.append('<section id="'+code+'"><h2>'+title+'</h2>'+intro+'<ul>'+''.join(cards)+'</ul></section>');md+='\n'
 nav='<a href="guia-de-consulta.html">Escolher uma folha</a>'+''.join('<a href="#'+k+'">'+v+'</a>' for k,v in groups.items())+'<a href="'+escape(local(routes['guilda']),quote=True)+'">Jogar em guilda</a>'
 doc='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Casos por assunto | Ciclo Maldito</title><style>'+css+'</style></head><body><nav>'+nav+'</nav><main><h1>Casos por assunto</h1><p>Escolha a dúvida, consulte a explicação e acompanhe um caso completo. Textos já revistos estão identificados; os demais continuam na edição anterior até a integração. Exemplos experimentais conservam seus limites.</p>'+''.join(sections)+'</main></body></html>'
 (A/'casos-completos.html').write_text(doc);(A/'destinos-dos-casos.md').write_text(md)
 oldabs={str((R/k).resolve()):v for k,v in old.items()}
 guide=S/'consultas/LEIA-ME.md';body=BeautifulSoup(markdown.markdown(guide.read_text(),extensions=['tables','toc']),'html.parser');forms={str((R/f['fonte']).resolve()):f['id'] for f in load(R/'04 - Planejamento/apoio-revisao-textual-116/amostra.json')['fontes']};cases={str((R/f[k]).resolve()):f['consulta_atual'] for rows in data['casos'].values() for f in rows for k in ['fonte','fonte_revisada'] if k in f};cases.update({str((R/v['fonte_revisada']).resolve()):v['consulta_atual'] for v in routes.get('consultas_revisadas',{}).values()})
 for tag in body.find_all('a',href=True):
  u=urlsplit(tag['href'])
  if u.scheme or not u.path:continue
  dest=(guide.parent/unquote(u.path)).resolve();assert dest.is_file(),tag['href']
  if str(dest) in forms:tag['href']='../apoio-revisao-textual-116/prova-textual.html#'+forms[str(dest)]+('--'+u.fragment if u.fragment else '')
  elif str(dest) in cases:tag['href']=local(cases[str(dest)])
  elif dest.name=='casos-completos.html':tag['href']='casos-completos.html'
  elif dest.parent==S and dest.name[:2].isdigit():
   num=dest.name.split('-')[0];n=int(num[:2]);folder=112 if n<=3 else 113 if n<=5 else 114 if n<=7 else 115;tag['href']=f'../apoio-revisao-textual-{folder}/prova-textual.html#c'+num+('--'+u.fragment if u.fragment else '')
  elif str(dest) in oldabs:
   o=oldabs[str(dest)];anchor=o['ancoras'].get(u.fragment,u.fragment) if u.fragment else o['id'];tag['href']=local('07 - Edicao de Leitura/'+o['pagina']+'#'+anchor)
  else:tag['href']=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
 (A/'guia-de-consulta.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Escolher uma folha</title><style>'+css+'</style><main><p><a href="casos-completos.html">Casos por assunto</a> · <a href="../apoio-revisao-textual-116/prova-textual.html">Folhas curtas</a></p>'+str(body)+'</main></html>')
 q=load(R/'04 - Planejamento/apoio-revisao-textual-130/fila-dos-casos.json');q['registro']=131;q['base']=str((A/'destinos-e-fontes.json').relative_to(R));q['base_sha256']=sha(A/'destinos-e-fontes.json')
 new={f['fonte_id']:f for f in meta['fontes']}
 for c in q['outras_consultas_pendentes']:
  if c['id'] in new:
   n=new[c['id']];c.update({'fonte_revisada':n['fonte'],'sha256_revisado':n['sha256'],'consulta_atual':meta['html']+'#'+n['id'],'estado':'duas passagens locais no registro 131; conferir na integração','registro_revisao':131})
 q['consultas_revistas']=[*q.get('consultas_revistas',[]),*new]
 q['lotes_consultas']=[
  {'lote':'C-01','titulo':'Fichas de mesa','consultas':['s002','s005','s024','s016'],'estado':'duas passagens locais concluídas no registro 131'},
  {'lote':'C-02','titulo':'Registros de campanha','consultas':['s008','s012','s020','s028','s032','s038'],'estado':'planejado; não executado'},
  {'lote':'C-03','titulo':'Personagens, entidades e inimigos','consultas':['s040','s042','s044','s058','s061'],'estado':'planejado; não executado'},
  {'lote':'C-04','titulo':'Mundo e obra','consultas':['s088','s087'],'estado':'planejado; não executado'}]
 q['proximo_lote']='C-02'
 save('fila-dos-casos.json',q)
 lines='# Fila editorial — registro 131\n\n59 casos distintos, todos com duas passagens locais. As 17 consultas complementares foram divididas em quatro lotes por assunto; C-01 foi revisto neste lote. Quatro consultas revistas, 13 pendentes.\n\n## Casos\n\n| Lote | Assunto | Estado |\n|---|---|---|\n'
 for f in q['lotes_planejados']:lines+='| '+f['lote']+' | '+f['titulo']+' | '+f['estado']+' |\n'
 lines+='\n## Consultas complementares\n\n| Lote | Assunto | Estado |\n|---|---|---|\n'
 for f in q['lotes_consultas']:lines+='| '+f['lote']+' | '+f['titulo']+' | '+f['estado']+' |\n'
 lines+='\n'
 for f in q['outras_consultas_pendentes']:
  alvo=f.get('fonte_revisada',f['fonte']);lines+='- '+f['destino']+': ['+f['titulo']+'](<'+os.path.relpath(R/alvo,A)+'>)'+(' — revista no registro 131' if f.get('fonte_revisada') else '')+'.\n'
 lines+='\n## Próxima tarefa\n\nC-02: registros de campanha (acordos, descobertas, facção, convivência, avaliação de capacidade, projeto). **Claude Opus 5.5 ou GPT-6.1 Sol, esforço alto.** Depois de C-02 a C-04: conferência do conjunto, integração e revisão visual do livro completo.\n';(A/'fila-dos-casos.md').write_text(lines)
 print(json.dumps({'casos':59,'consultas_revistas':4,'consultas_pendentes':13,'consulta_guia_sha256':sha(guide)},ensure_ascii=False))
if __name__=='__main__':main()

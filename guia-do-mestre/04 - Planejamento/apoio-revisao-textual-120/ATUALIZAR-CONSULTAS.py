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
def main():
 data=load(R/'04 - Planejamento/apoio-revisao-textual-119/destinos-e-fontes.json');meta=load(A/'amostra.json');new={f['fonte_id']:f for f in meta['fontes']}
 data['registro']=120;data['revisao_das_rotas']=120;data['limite']='Dezenove casos têm cópias revistas: Arata no registro 114, quatro casos no 117, cinco no 118, cinco no 119 e quatro no 120. Demais casos, consultas e integração continuam pendentes.'
 routes=load(R/'04 - Planejamento/apoio-revisao-textual-119/rotas-de-consulta.json');routes['registro']=120
 for rows in data['casos'].values():
  for f in rows:
   if f['id'] in new:
    n=new[f['id']];revised={'fonte_revisada':n['fonte'],'sha256_revisado':n['sha256'],'consulta_atual':meta['html']+'#'+n['id'],'motivo':'Duas passagens de clareza e remissões, sem alterar números; instruções e títulos simplificados, remissão às três fichas restaurada e estados de queda esclarecidos. Propostas experimentais preservadas.'}
    f.update(revised);routes['casos_revisados'][f['id']]={k:v for k,v in revised.items() if k!='sha256_revisado'}
 data['rotas']=routes;save('destinos-e-fontes.json',data);save('rotas-de-consulta.json',routes)
 css=BeautifulSoup((R/'04 - Planejamento/apoio-consultas-105/casos-completos.html').read_text(),'html.parser').style.get_text();groups={'B1':'Testes, percepção e movimento','B2':'Confrontos e perigos','B3':'Personagens e técnicas','B4':'Objetos e recompensas','B5':'Pactos e entidades'}
 structure=load(R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json');old={f['fonte']:f for f in load(R/'07 - Edicao de Leitura/mapa-editorial.json')['fontes']};sections=[]
 md='# Casos por assunto — registro 120\n\nDezenove casos revistos e 40 ainda na edição anterior até sua revisão. Métodos 112–115 e folhas 116 permanecem atuais.\n\n'
 for code,title in groups.items():
  route=routes['grupos'][code];refs=[]
  for ident in route['folhas']:
   f=next(f for f in structure['fontes'] if f['id']==ident);o=old[f['fonte']];refs.append('<a href="'+escape(local('07 - Edicao de Leitura/'+o['pagina']+'#'+o['id']),quote=True)+'">'+escape(f['titulo_atual'])+'</a>')
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
 guide=S/'consultas/LEIA-ME.md';body=BeautifulSoup(markdown.markdown(guide.read_text(),extensions=['tables','toc']),'html.parser');forms={str((R/f['fonte']).resolve()):f['id'] for f in load(R/'04 - Planejamento/apoio-revisao-textual-116/amostra.json')['fontes']};cases={str((R/f[k]).resolve()):f['consulta_atual'] for rows in data['casos'].values() for f in rows for k in ['fonte','fonte_revisada'] if k in f}
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
 q=load(R/'04 - Planejamento/apoio-revisao-textual-119/fila-dos-casos.json');q['registro']=120;q['base']=str((A/'destinos-e-fontes.json').relative_to(R));q['base_sha256']=sha(A/'destinos-e-fontes.json');q['casos_pendentes']=40;q['casos_ja_revistos']=[*q['casos_ja_revistos'],*new];q.pop('caso_ja_revisto',None);q['proximo_lote']='B2-03';q['lotes_pendentes']=10
 for f in q['casos']:
  if f['id'] in new:
   n=new[f['id']];f.update({'fonte_revisada':n['fonte'],'sha256_revisado':n['sha256'],'consulta_atual':meta['html']+'#'+n['id'],'estado':'duas passagens locais no registro 120; conferir na integração','registro_revisao':120})
 for f in q['lotes_planejados']:
  if f['lote']=='B2-02':f['estado']='duas passagens locais concluídas no registro 120'
 save('fila-dos-casos.json',q)
 lines='# Fila editorial — registro 120\n\n59 casos distintos; dezenove com duas passagens locais, 40 pendentes. B2-02 foi revisto neste lote; os lotes B1 e Arata conservam as revisões anteriores. As 17 consultas complementares continuam pendentes.\n\n| Lote | Assunto | Estado |\n|---|---|---|\n'
 for f in q['lotes_planejados']:lines+='| '+f['lote']+' | '+f['titulo']+' | '+f['estado']+' |\n'
 lines+='\n## Consultas complementares\n\n'
 for f in q['outras_consultas_pendentes']:lines+='- '+f['destino']+': ['+f['titulo']+'](<'+os.path.relpath(R/f['fonte'],A)+'>).\n'
 lines+='\n## Próxima tarefa\n\nB2-03: terreno, saída e Sineiro; revisar os quatro casos previstos na fila. Manter os limites dos exemplos experimentais. **GPT-6.1 Sol, esforço alto.** Preservar os originais e conferir cada cópia. Depois dos lotes e consultas, conferir o conjunto antes de integrar e revisar visualmente o livro completo.\n';(A/'fila-dos-casos.md').write_text(lines)
 print(json.dumps({'casos':59,'casos_revistos':19,'casos_pendentes':40,'lotes_pendentes':10,'consulta_guia_sha256':sha(guide)},ensure_ascii=False))
if __name__=='__main__':main()

"""Conferir os ajustes de leitura, a preservação mecânica e as remissões do conjunto."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import hashlib,json,re,collections,markdown
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 fail=[];baseline=A/'antes'/T.relative_to(R);logs=json.loads((A/'alteracoes.json').read_text())
 states={p.relative_to(baseline).as_posix():p.read_text() for p in baseline.rglob('*.md')}
 assert len(states)==99
 for edit in logs:
  rel=Path(edit['fonte']).relative_to(T.relative_to(R)).as_posix();s=states[rel]
  if edit.get('tipo')=='movimento':
   block=edit['trecho'];assert s.count(block)==1
   start=s.index(block);assert not s[start+len(block):].strip()
   body=s[:start].rstrip();at=body.index(edit['antes_de']);s=body[:at]+block.rstrip()+'\n\n'+body[at:]+'\n'
  else:
   assert s.count(edit['antes'])==1,(rel,edit['antes'][:80]);s=s.replace(edit['antes'],edit['depois'],1)
  states[rel]=s
 changed=[];tables=0
 def numbers(t):
  t=re.sub(r'\]\(<?[^)]*\)|<!--.*?-->|<[^>]*>','',t,flags=re.S)
  return collections.Counter(re.findall(r'\d+(?:[.,]\d+)?',t))
 def tablelines(s):return [line for line in s.splitlines() if line.lstrip().startswith('|')]
 for rel,state in states.items():
  p=T/rel;old=(baseline/rel).read_text();assert p.read_text()==state,rel
  if p.read_text()!=old:changed.append(p.relative_to(R).as_posix())
  if numbers(old)!=numbers(state):fail.append({'fonte':rel,'erro':'conjunto de números alterado'})
  if tablelines(old)!=tablelines(state):fail.append({'fonte':rel,'erro':'quadro alterado'})
  tables+=sum(1 for line in state.splitlines() if line.startswith('|---'))
 assert len(changed)==4,changed
 # Destinos de leitura e âncoras: a verificação é de arquivos, não de navegador.
 htmlfiles=sorted(E.glob('*.html'));soups={p.resolve():BeautifulSoup(p.read_text(),'html.parser') for p in htmlfiles}
 ids={p:{tag['id'] for tag in s.find_all(id=True)} for p,s in soups.items()};links=images=external=0
 for p,soup in soups.items():
  allids=[tag['id'] for tag in soup.find_all(id=True)]
  if len(allids)!=len(set(allids)):fail.append({'arquivo':p.name,'erro':'ID duplicado'})
  if len(soup.select('article h1'))!=1:fail.append({'arquivo':p.name,'erro':'título principal ausente ou duplicado'})
  for tag in soup.find_all(['a','img','link']):
   value=tag.get('src') if tag.name=='img' else tag.get('href')
   if not value:continue
   u=urlsplit(value);links+=tag.name=='a';images+=tag.name=='img'
   if u.scheme in ['http','https','mailto']:external+=1;continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   if u.scheme or not target.is_relative_to(E.resolve()) or not target.is_file():fail.append({'arquivo':p.name,'erro':'destino ausente ou fora da edição','link':value});continue
   if u.fragment and target.suffix=='.html' and unquote(u.fragment) not in ids[target]:fail.append({'arquivo':p.name,'erro':'âncora ausente','link':value})
   if target.name=='apendice-d.html' and p.name!='apendice-d.html' and 'revelaç' not in tag.get_text().lower():fail.append({'arquivo':p.name,'erro':'acesso sem aviso de revelações'})
 for name in ['capitulo-01.html','capitulo-02.html','capitulo-03.html']:
  old=BeautifulSoup((A/'antes'/E.relative_to(R)/name).read_text(),'html.parser');oldids={tag['id'] for tag in old.find_all(id=True)}
  if not oldids<=ids[(E/name).resolve()]:fail.append({'arquivo':name,'erro':'âncora anterior perdida','ids':sorted(oldids-ids[(E/name).resolve()])})
 c3=soups[(E/'capitulo-03.html').resolve()];article=c3.article
 ordered=list(article.descendants)
 for id_ in ['antes-que-o-trem-parta','36-ideias-para-sua-proxima-missao','ideias','37-quando-ha-pouco-tempo']:
  assert len(article.find_all(id=id_))==1,id_
 sequence=[ordered.index(article.find(id=id_)) for id_ in ['antes-que-o-trem-parta','36-ideias-para-sua-proxima-missao','ideias','37-quando-ha-pouco-tempo']]
 assert sequence==sorted(sequence)
 assert len(htmlfiles)==99
 # Markdown continua sendo uma fonte útil, inclusive nos acessos internos novos.
 mds={p.resolve():BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','toc','fenced_code']),'html.parser') for p in T.rglob('*.md')}
 for p,s in mds.items():
  for a in s.find_all(['a','img']):
   value=a.get('href') if a.name=='a' else a.get('src')
   if not value:continue
   u=urlsplit(value)
   if u.scheme:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   if not target.is_file():fail.append({'fonte':p.name,'erro':'destino Markdown ausente','link':value});continue
   if u.fragment and target in mds and not mds[target].find(id=unquote(u.fragment)):fail.append({'fonte':p.name,'erro':'âncora Markdown ausente','link':value})
 out={'registro':137,'fontes_no_conjunto':99,'fontes_com_alteracao':changed,'alteracoes_reproduzidas':len(logs),'quadros_preservados':tables,'numeros_preservados':not any(f.get('erro')=='conjunto de números alterado' for f in fail),'documentos_html':len(htmlfiles),'links_html':links,'imagens_html':images,'links_externos':external,'ancoras_anteriores_dos_capitulos_preservadas':True,'exemplo_antes_do_catalogo':sequence==sorted(sequence),'falhas':fail,'limite':'Conferência de fontes e da estrutura HTML; não inspeção visual em navegador ou do futuro PDF completo.'}
 (A/'conferencia.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert not fail,fail
if __name__=='__main__':main()

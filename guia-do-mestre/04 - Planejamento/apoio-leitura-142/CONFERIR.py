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
  expected_numbers=numbers(old)
  if expected_numbers!=numbers(state):fail.append({'fonte':rel,'erro':'conjunto de números alterado'})
  expected_tables=old
  if rel=='09-pactos-e-entidades.md':
   expected_tables=old.replace('| Classe | Criar | Reconstruir | Transferir |','| Classe | Criar (horas) | Reconstruir (horas) | Transferir (horas) |').replace('| Relação de Classes | Criar ou transferir | Reconstruir |','| Relação de Classes | Ajuste para criar ou transferir | Ajuste para reconstruir |')
  if tablelines(expected_tables)!=tablelines(state):fail.append({'fonte':rel,'erro':'tabela alterada além dos cabeçalhos declarados'})
  tables+=sum(1 for line in state.splitlines() if line.startswith('|---'))
 assert len(changed)==3,changed
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
 for name in [row['pagina'] for row in json.loads((A/'destinos-alterados.json').read_text())]:
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
 # As decisões e os exemplos completos permanecem preservados.
 for rel in ['casos/45-tempo-materiais-e-retomada-de-entidades.md','casos/46-reconstruir-transferir-e-herdar-entidades.md','casos/48-pacifismo-impraticavel-minuta.md','casos/50-promessa-do-arquivo.md','casos/51-ritual-do-cao-de-sombra.md','casos/52-domar-o-amontoado.md','casos/54-transporte-e-continuidade-das-entidades.md','casos/55-fabricar-e-evoluir-o-vigia-do-deposito.md','consultas/42-registro-de-pactos-e-promessas.md','consultas/44-registro-de-aquisicao-e-estado-de-entidade.md']:
  assert (baseline/rel).read_bytes()==(T/rel).read_bytes(),rel
 retomado=json.loads((A/'escriba-retomado.json').read_text());assert sha(R/retomado['fonte'])==retomado['sha256']
 text9=(T/'09-pactos-e-entidades.md').read_text()
 assert 'Pode modificar um Estilo que a personagem já possua, mas não concede outro.' in text9
 assert '0/25/50/75/100/100%' in text9
 assert 'cada falha pede mais 50% do trabalho inicial daquela operação' in text9
 assert 'Esse sorteio não prepara Refluxo.' in text9
 assert 'Ativar um corpo inativo e religar um corpo Desligado são operações diferentes.' in text9
 assert 'casos/45-tempo-materiais-e-retomada-de-entidades.md' in text9
 assert 'sem recarregá-lo pela troca de ficha' not in (T/'casos/49-liberacao-irregular-minuta.md').read_text()
 assert not json.loads((A/'contas-conferidas.json').read_text())['falhas']
 out={'registro':142,'fontes_no_conjunto':99,'fontes_com_alteracao':changed,'alteracoes_reproduzidas':len(logs),'quadros_com_parametros_preservados':tables,'rotulos_de_quadro_ajustados':5,'cabecalhos_de_tabelas_alterados':2,'numeros_preservados':not any(f.get('erro')=='conjunto de números alterado' for f in fail),'documentos_html':len(htmlfiles),'links_html':links,'imagens_html':images,'links_externos':external,'ancoras_anteriores_dos_capitulos_preservadas':True,'exemplo_antes_do_catalogo':sequence==sorted(sequence),'decisoes_de_pactos_e_projetos_preservadas':True,'estados_e_limite_de_corpos_explicados':True,'escriba_retomado_sem_alteracao':True,'falhas':fail,'limite':'Conferência de fontes e da estrutura HTML; não inspeção visual em navegador ou do futuro PDF completo.'}
 (A/'conferencia.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert not fail,fail
if __name__=='__main__':main()

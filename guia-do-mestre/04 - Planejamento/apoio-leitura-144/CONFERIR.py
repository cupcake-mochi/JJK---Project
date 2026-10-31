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
 def tablelines(s):return [re.sub(r'\]\(<?[^)]*\)',']',line) for line in s.splitlines() if line.lstrip().startswith('|')]
 for rel,state in states.items():
  p=T/rel;old=(baseline/rel).read_text();assert p.read_text()==state,rel
  if p.read_text()!=old:changed.append(p.relative_to(R).as_posix())
  expected_numbers=numbers(old)
  if rel=='casos/72-sineiro-consulta-e-doma.md':expected_numbers.subtract({'72':1});expected_numbers=+expected_numbers
  if expected_numbers!=numbers(state):fail.append({'fonte':rel,'erro':'conjunto de números alterado'})
  expected_tables=old
  if rel=='consultas/88-indice-de-termos-do-mundo.md':
   row=next(line for line in old.splitlines() if line.startswith('| Barreira e Cortina |'))
   expected_tables=old.replace(row,row.replace('[Poderes avançados]','[Preparar uma Cortina]'),1)
  if tablelines(expected_tables)!=tablelines(state):fail.append({'fonte':rel,'erro':'tabela alterada além dos cabeçalhos declarados'})
  tables+=sum(1 for line in state.splitlines() if line.startswith('|---'))
 assert len(changed)==5,changed
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
 # A cobertura integral fecha o recorte 137–144; não pressupõe inspeção visual.
 coverage=json.loads((A/'cobertura-da-leitura-continua.json').read_text())
 assert len(coverage['fontes'])==99
 assert all(x['estado']=='leitura integral recente e hash vigente' for x in coverage['fontes'])
 for row in coverage['fontes']:assert sha(R/row['fonte'])==row['sha256_atual'],row['fonte']
 index=(T/'consultas/88-indice-de-termos-do-mundo.md').read_text()
 assert '33-casos-especificos-de-avaliacao.md#definir-os-limites-de-uma-cortina' in index
 assert 'A vida inimiga mudou de 72' not in (T/'casos/72-sineiro-consulta-e-doma.md').read_text()
 assert 'O Sineiro tem 108 PV na ficha do confronto.' in (T/'casos/72-sineiro-consulta-e-doma.md').read_text()
 assert 'REVELAÇÕES IMPORTANTES DA TRAMA.' in (T/'consultas/87-casos-da-obra-para-preparar-situacoes.md').read_text()
 assert 'Consulta sem revelações da trama.' in index
 assert not json.loads((A/'contas-conferidas.json').read_text())['falhas']
 out={'registro':144,'fontes_no_conjunto':99,'fontes_com_alteracao':changed,'alteracoes_reproduzidas':len(logs),'quadros_com_parametros_preservados':tables,'rotulos_de_quadro_ajustados':1,'cabecalhos_de_tabelas_alterados':0,'numeros_vigentes_preservados':not any(f.get('erro')=='conjunto de números alterado' for f in fail),'numeros_preservados':not any(f.get('erro')=='conjunto de números alterado' for f in fail),'excecao_numerica':'Retirada apenas a menção histórica a 72 PV do Sineiro; atuais 108/38/19 preservados.','documentos_html':len(htmlfiles),'links_html':links,'imagens_html':images,'links_externos':external,'ancoras_anteriores_preservadas':True,'exemplo_antes_do_catalogo':sequence==sorted(sequence),'fontes_com_leitura_integral_recente_e_hash_vigente':99,'falhas':fail,'limite':'Conferência de fontes e da estrutura HTML; não inspeção visual em navegador ou do futuro PDF completo.'}
 (A/'conferencia.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert not fail,fail
if __name__=='__main__':main()

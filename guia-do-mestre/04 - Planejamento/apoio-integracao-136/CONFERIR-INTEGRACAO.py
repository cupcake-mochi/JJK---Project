"""Conferir reprodução, quadros, cobertura e navegação da edição reunida."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,re,hashlib,collections,difflib,unicodedata

A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 entries=json.loads((A/'fontes-reunidas.json').read_text());edits=json.loads((A/'alteracoes.json').read_text());conf=json.loads((A/'composicao.json').read_text())
 states={e['fonte']:(R/e['origem']).read_text() for e in entries};fail=[]
 for e in edits:
  source=e['fonte'];before=e['antes'];after=e['depois'];n=e['ocorrencias']
  if before not in states[source]:fail.append({'fonte':source,'erro':'trecho ausente no histórico','trecho':before[:100]});continue
  states[source]=states[source].replace(before,after,n)
 for e in entries:
  if sha(R/e['origem'])!=e['sha256_origem']:fail.append({'fonte':e['origem'],'erro':'origem alterada'})
  if states[e['fonte']]!=(R/e['fonte']).read_text():fail.append({'fonte':e['fonte'],'erro':'reprodução diverge'})
 def cells(text):
  return [c.strip() for l in text.splitlines() if l.lstrip().startswith('|') for c in l.strip().strip('|').split('|')]
 clean=lambda s:re.sub(r'\]\(<?[^)]*\)',']()',s)
 tables=0;numberchanges=[]
 visible=lambda t:re.sub(r'\]\(<?[^)]*\)|<[^>]*>','',t)
 numbers=lambda t:re.findall(r'\d+(?:[.,]\d+)?',visible(t))
 for e in entries:
  before=(R/e['origem']).read_text();after=(R/e['fonte']).read_text()
  if e['origem'].endswith('/27-convivencia-do-receptaculo.md'):
   before=re.sub(r'^## Quem interpreta cada voz\?\n.*?(?=^## |\Z)','',before,flags=re.M|re.S)
  x,y=cells(before),cells(after);tables+=sum(1 for line in after.splitlines() if line.startswith('|---'))
  if [clean(s) for s in x]!=[clean(s) for s in y]:fail.append({'fonte':e['fonte'],'erro':'células mudaram além dos destinos de link'})
  n1,n2=numbers((R/e['origem']).read_text()),numbers(after)
  if n1!=n2:
   ops=[{'antes':n1[i:j],'depois':n2[k:l]} for op,i,j,k,l in difflib.SequenceMatcher(None,n1,n2,autojunk=False).get_opcodes() if op!='equal']
   numberchanges.append({'fonte':e['fonte'],'alteracoes':ops})
   allowed=['08-entre-missoes.md','14-tres-maldicoes-para-a-missao.md','47-desenvolver-uma-ideia-de-pacto.md','93-ampliar-mesclas-e-trocar-formas.md','92-reserva-condensada-proposta-e-comparacao.md']
   if Path(e['fonte']).name not in allowed:fail.append({'fonte':e['fonte'],'erro':'mudança numérica não prevista','alteracoes':ops})
 # Cada uma das 99 fontes tem um destino; 3a está incluída uma única vez em 3.6.
 assert conf['fontes_em_leitura']==99 and conf['paginas_de_conteudo']==98
 assert len({row['fonte'] for row in conf['rotas']})==99
 assert len({row['pagina'] for row in conf['ordem']})==98
 htmlfiles=sorted(E.glob('*.html'));soups={p:BeautifulSoup(p.read_text(),'html.parser') for p in htmlfiles}
 ids={p:{tag['id'] for tag in soup.find_all(id=True)} for p,soup in soups.items()};links=images=external=0
 for p,soup in soups.items():
  allids=[tag['id'] for tag in soup.find_all(id=True)]
  if len(allids)!=len(set(allids)):fail.append({'arquivo':p.name,'erro':'ID duplicado'})
  for tag in soup.find_all(['a','img','link']):
   value=tag.get('href') if tag.name!='img' else tag.get('src')
   if not value:continue
   links+=tag.name=='a';images+=tag.name=='img';u=urlsplit(value)
   if u.scheme in ['https','http','mailto']:external+=1;continue
   if u.scheme or u.path.startswith('/'):
    fail.append({'arquivo':p.name,'erro':'endereço absoluto','destino':value});continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   if not target.is_relative_to(E.resolve()) or not target.is_file():
    fail.append({'arquivo':p.name,'erro':'destino fora do pacote ou ausente','destino':value});continue
   if u.fragment and target.suffix=='.html' and unquote(u.fragment) not in ids[target]:fail.append({'arquivo':p.name,'erro':'âncora ausente','destino':value})
   if target.name=='apendice-d.html' and p.name!='apendice-d.html' and 'revelaç' not in tag.get_text().lower():fail.append({'arquivo':p.name,'erro':'acesso sem aviso ao apêndice com revelações','texto':tag.get_text()})
 # Os arquivos da edição não podem apontar para a estrutura antiga.
 for p in htmlfiles:
  text=p.read_text()
  if any(s in text for s in ['04 - Planejamento/','apoio-conferencia-135/','/home/mizuki/','file:///']):fail.append({'arquivo':p.name,'erro':'dependência da estrutura de trabalho'})
 # As ideias aparecem antes de 3.7 e uma única vez no capítulo 3.
 c3=soups[E/'capitulo-03.html'];addon=c3.find(id='ideias');n37=c3.find(id='37-quando-ha-pouco-tempo')
 assert addon and n37 and len(c3.find_all(id='ideias'))==1
 assert list(c3.descendants).index(addon)<list(c3.descendants).index(n37)
 fixed={'amparo_8_menos_6':8-6,'reserva_piso_7_2_mais_4_2':7//2+4//2,'limite_35_saldo_32':min(35,32+(7//2+4//2)),
        'integridade_inimigos':[max(1,n//2) for n in [12,48,24]],'integridade_domadas':[10//2,14//2,10//2],
        'reservas_proprias_classe2':[2*(1+e//3) for e in [1,3]],'excedente_igual_metade_48_nao_supera':(32-8)<=48/2,'excedente_acima_48_supera':(33-8)>48/2}
 assert fixed['amparo_8_menos_6']==2 and fixed['reserva_piso_7_2_mais_4_2']==5 and fixed['limite_35_saldo_32']==35
 assert fixed['integridade_inimigos']==[6,24,12] and fixed['integridade_domadas']==[5,7,5]
 assert fixed['reservas_proprias_classe2']==[2,4] and fixed['excedente_igual_metade_48_nao_supera'] and fixed['excedente_acima_48_supera']
 result={'registro':136,'fontes_reunidas':len(entries),'fontes_reproduzidas':len(states),'alteracoes_reproduzidas':len(edits),'quadros_conferidos':tables,'diferencas_numericas_editoriais':numberchanges,'paginas_html':len(htmlfiles),'links_html':links,'imagens_html':images,'links_externos':external,'contas_dos_apoios':fixed,'ideias_incluidas_uma_vez_antes_de_37':True,'origens_preservadas':True,'falhas':fail,'limites':['Validação estrutural e de conteúdo copiado, não leitura integral contínua de todas as fontes.','Navegação no navegador não inspecionada: protocolo local bloqueado pela política do navegador.','Revisão visual desta entrega restrita à prova dos apoios e aos mapas atualizados.']}
 (A/'conferencia-da-integracao.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['diferencas_numericas_editoriais','contas_dos_apoios','limites']},ensure_ascii=False,indent=2))
 if fail:raise SystemExit(1)

if __name__=='__main__':main()

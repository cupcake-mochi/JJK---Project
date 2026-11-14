from pathlib import Path
from collections import defaultdict
import re,json,hashlib,sys
from pypdf import PdfReader
B=Path(__file__).resolve().parent;R=B/'revisao-r41';base=B.parent/'livro-diagramado-r40';issues=[]
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def check(ok,label):
 if not ok:issues.append(label)
def blocks(p):
 out={}
 for m in re.finditer(r'<!-- fonte:[^\n]+ -->\n<a id="([^"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\Z)',p.read_text(),re.S):out[m[1]]=re.split(r'\n<a id="capitulo-|\n<!-- parte:',m[2])[0].strip()
 return out
old=blocks(base/'LIVRO-COMPLETO.md');new=blocks(B/'LIVRO-COMPLETO.md');rows=read(R/'ALTERACOES-TEXTO.json');changed={k for k in old if old[k]!=new.get(k)}
check(set(old)==set(new),'Conjunto dos 500 blocos preservado')
check(changed=={r['bloco'] for r in rows},'Exatamente cinco blocos alterados, todos registrados')
# Todas as Bênçãos fora das duas entradas devem ser idênticas.
key='rotas--rota-combate'
for name,body in re.findall(r'^##### ([^\n]+)\n(.*?)(?=^##### |\Z)',old[key],re.M|re.S):
 if name not in {'Represália','Sangue Frio'}:
  match=re.search(r'^##### '+re.escape(name)+r'\n(.*?)(?=^##### |\Z)',new[key],re.M|re.S)
  check(match and match[1]==body,'Outra Bênção preservada: '+name)
rep=re.search(r'##### Represália\n(.*?)(?=##### Sangue Frio)',new[key],re.S)[1]
san=re.search(r'##### Sangue Frio\n(.*?)(?=##### Campo)',new[key],re.S)[1]
for s in ['Categoria de Efeito: 2','Força 4 ou Destreza 4','Fora do seu turno','1,5 m','depois do uso','não interrompe nem desfaz','Manter um efeito já ativo não oferece um novo gatilho','Acerto de uma Expansão incompleta','feitiços conjurados dentro de um domínio continuam contando normalmente']:check(s in rep,'Represália: '+s)
for s in ['Categoria de Efeito: 3','Constituição 4','vantagem nos TRs','3 m','Uma vez por cena','um único d20, sem a vantagem desta Bênção','mantenha a CD e os modificadores','O novo resultado é obrigatório','A repetição também exige que a criatura esteja a até 3 m','Acerto de uma Expansão incompleta','feitiços conjurados dentro de um domínio continuam contando normalmente']:check(s in san,'Sangue Frio: '+s)
check('| Represália | 2 | Força 4 ou Destreza 4. |' in new['rotas--rota-bencaos'],'Requisito também na tabela')
check('| 7 | Dificultar a Resistência, Ajustar a Preparação, Recolher sob Ataque e Atuação Complementar. |' in new['evocador--evocador'],'Quatro capacidades na progressão do Evocador')
for k,title in [('evocador--ev-principal-protecao','Intervenções da Invocação Principal'),('evocador--ev-multiplas-protecao','Intervenções do Conjunto')]:check('#### '+title in new[k],'Título padronizado: '+title)
for k,h in read(R/'BASE-R40-SHA256.json').items():
 p=base/k;check(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h,'R40 intacta: '+k)
for f in ['ESTUDO-DENSIDADE.json','ESTUDO-CAPITULO.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-HIERARQUIA.json','CREDITOS.json','CAPA-E-ABERTURAS.json']:check((B/f).read_bytes()==(base/f).read_bytes(),'Estilo, arte e créditos mantidos: '+f)
m=read(B/'FONTES-E-VALIDACAO.json');prior=read(base/'FONTES-E-VALIDACAO.json');pdf=PdfReader(B/m['pdf'])
# Diferenças geométricas por página, ignorando só numeração final e referências atualizadas.
def pageevents(manifest):
 out=defaultdict(list)
 for e in manifest['eventos']:out[e['pagina']].append({k:v for k,v in e.items() if k not in {'pagina','faixa'}})
 return out
a=pageevents(prior);z=pageevents(m);diffpages=[p for p in z if z[p]!=a.get(p)]
# Registro de cada bloco recomposto ou movido, mesmo quando seu texto não mudou.
a=defaultdict(list);z=defaultdict(list)
for e in prior['eventos']:a[e.get('bloco') or '__elementos_gerados__'].append(e)
for e in m['eventos']:z[e.get('bloco') or '__elementos_gerados__'].append(e)
diagram=[]
for k in sorted(a.keys()|z.keys()):
 if a[k]!=z[k]:diagram.append({'id':f'R41-D{len(diagram)+1:03d}','bloco':k,'antes':a[k],'depois':z[k],'motivo':'Recomposição decorrente dos cinco blocos autorizados na R41; inclui mudanças de paginação e contextos dos títulos padronizados.'})
save(R/'ALTERACOES-DIAGRAMACAO.json',diagram)
# Revalidar cada linha do sumário contra sua anotação clicável.
pageids={p.indirect_reference.idnum:i+1 for i,p in enumerate(pdf.pages)};navcount=0
for page in read(B/'revisao-r40/SUMARIO-PAGINADO.json'):
 links=[x.get_object() for x in pdf.pages[page['pagina']-1].get('/Annots',[]) if x.get_object().get('/Dest')]
 for row in page['entradas']:
  if not row['destino']:continue
  navcount+=1;target=m['ancoras'][row['destino']]['pagina']
  near=[x for x in links if float(x['/Rect'][1])<=row['y'] and float(x['/Rect'][3])>=row['y']-row['altura'] and float(x['/Rect'][0])<(300 if row['coluna']==0 else 600) and float(x['/Rect'][0])>=(0 if row['coluna']==0 else 300)]
  check(any(pageids.get(x['/Dest'][0].idnum)==target for x in near),'Link do sumário: '+row['titulo'] if 'titulo' in row else 'Link do sumário')
report={'paginas':len(pdf.pages),'blocos_textuais_alterados':len(rows),'blocos_alterados':sorted(changed),'registros_diagramacao':len(diagram),'paginas_com_composicao_diferente':diffpages,'links_sumario_conferidos':navcount,'r40_intacta':not any(s.startswith('R40 intacta') for s in issues),'texto_identico_fora_dos_registros':changed=={r['bloco'] for r in rows},'problemas':issues,'sha256_pdf':hashlib.sha256((B/m['pdf']).read_bytes()).hexdigest()}
save(R/'CONFERENCIA.json',report);print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(issues))

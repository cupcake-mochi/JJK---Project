from pathlib import Path
import json,re,hashlib,sys
from collections import defaultdict,Counter
from pypdf import PdfReader
B=Path(__file__).resolve().parent;R=B/'revisao-r40';base=B.parent/'livro-diagramado-r39';issues=[]
def check(ok,label,detail=None):
 if not ok:issues.append({'verificacao':label,'detalhe':detail})
def blocks(p):
 t=p.read_text();res={}
 for m in re.finditer(r'<!-- fonte:[^\n]+ -->\n<a id="([^"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\Z)',t,re.S):
  s=re.split(r'\n<a id="capitulo-|\n<!-- parte:',m[2])[0].strip();res[m[1]]=s
 return res
old=blocks(base/'LIVRO-COMPLETO.md');new=blocks(B/'LIVRO-COMPLETO.md');rows=json.loads((R/'ALTERACOES-TEXTO.json').read_text());recorded={r['bloco'] for r in rows}
changed={k for k in old if new.get(k)!=old[k]}
check(set(old)==set(new),'Mesmos blocos no livro')
check(changed==recorded,'Toda diferença textual registrada',{'nao_registradas':sorted(changed-recorded),'sem_diferenca':sorted(recorded-changed)})
hashes=json.loads((R/'BASE-R39-SHA256.json').read_text());preserved=True
for k,h in hashes.items():
 p=base/k
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:preserved=False;issues.append({'verificacao':'R39 intacta','arquivo':k})
for f in ['ESTUDO-DENSIDADE.json','ESTUDO-CAPITULO.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-HIERARQUIA.json','CREDITOS.json']:
 check((base/f).read_bytes()==(B/f).read_bytes(),'Estilo, tamanho e créditos mantidos',f)
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text());pdf=PdfReader(B/m['pdf']);nav=json.loads((R/'NAVEGACAO.json').read_text());toc=json.loads((R/'SUMARIO-PAGINADO.json').read_text())
for row in nav:check(row['destino'] in m['ancoras'],'Destino de navegação',row)
# Conferir página do link e número impresso, linha a linha, com a mesma posição vertical.
pageids={p.indirect_reference.idnum:i+1 for i,p in enumerate(pdf.pages)}
navchecks=0
for page in toc:
 p=pdf.pages[page['pagina']-1]
 links=[r.get_object() for r in p.get('/Annots',[]) if r.get_object().get('/Dest')]
 for row in page['entradas']:
  if not row['destino']:continue
  target=m['ancoras'][row['destino']]['pagina'];navchecks+=1
  near=[a for a in links if float(a['/Rect'][1])<=row['y'] and float(a['/Rect'][3])>=row['y']-row['altura'] and float(a['/Rect'][0])<(300 if row['coluna']==0 else 600) and float(a['/Rect'][0])>=(0 if row['coluna']==0 else 300)]
  check(any(pageids.get(a['/Dest'][0].idnum)==target for a in near),'Link do sumário na linha correta',row)
# Inventário dos seis Caminhos, de todas as Trilhas e das rotas do Batedor.
texts=json.loads((R/'TEXTOS-PROPOSTOS.json').read_text());inventory=[]
roots={'bastiao--bas-bastiao','vanguarda--van-base','guia--guia','emanador--ema-base','evocador--evocador','incursor--inc-caminho'}
for row in nav:
 if row['capitulo']!=6:continue
 k=row.get('bloco',row['destino']);t=texts[k];isroot=k in roots
 if k in ['vanguarda--van-besta','vanguarda--van-fogo'] or row['destino']=='r40-nav-yumi':tablekey='vanguarda--van-yumi'
 elif k=='guia--guia':tablekey='guia--guia-progressao'
 else:tablekey=k
 table=texts[tablekey];found='| Nível |' in table
 check(found,'Tabela de progressão para Caminho/Trilha/rota',row['titulo'])
 inventory.append({'nome':row['titulo'],'tipo':'Caminho' if isroot else 'rota do Batedor' if row['nivel']==4 else 'Trilha','bloco':k,'tabela_em':tablekey,'pagina':m['ancoras'][row['destino']]['pagina']})
# Todas as habilidades com nível explícito usam entrada (exceto agrupadores identificados).
for e in m['eventos']:
 if e.get('gerado') or e.get('capitulo')!=6:continue
 if e['tipo'] in ['h2','h3','marker']:
  check(bool(e.get('tratamento_hierarquia')),'Título do capítulo 6 classificado',e['texto'])
# Ordem de leitura das entradas do Assassino.
alltext=(B/'LIVRO-COMPLETO.md').read_text();a=alltext.index('### Assassino');z=alltext.index('### Pugilista',a);ass=alltext[a:z]
levels=[int(n) for n in re.findall(r'^\*\*Nível (\d+)\.\*\*$',ass,re.M)]
check(levels==sorted(levels),'Assassino em ordem de nível',levels)
check('Rajada Marcial a partir' not in alltext and 'A partir do **nível 7**, Corpo Treinado ganha esta melhoria.' in alltext,'Rajada esclarecida no texto')
check('#### Tratar e Retomar\n\n**Nível 11.**' in alltext,'Tratar e Retomar no nível de habilidade')
# Verificar todas as sequências, incluindo evoluções com nível no título/texto.
chapter=alltext[alltext.index('## 6. Caminhos'):alltext.index('## 7. Perícias')]
order=re.findall(r'<a id="([^"\n]+)"></a>',chapter);sequences={};scope=None
for key in order:
 if key not in texts:continue
 paragraphs=texts[key].split('\n\n')
 for i,para in enumerate(paragraphs):
  if para.startswith('# '):scope=para[2:];sequences[scope]=[]
  heading=re.match(r'^#{2,3} (.+)$',para)
  if not heading or i+1>=len(paragraphs):continue
  following=paragraphs[i+1];match=re.match(r'^\*\*Nível (\d+)\.\*\*',following)
  level=int(match[1]) if match else None
  if heading[1]=='Rajada Marcial':level=7
  elif re.search(r'Fluidez no nível (\d+)',heading[1]):level=int(re.search(r'nível (\d+)',heading[1])[1])
  if level is not None:sequences[scope].append({'nivel':level,'habilidade':heading[1],'bloco':key})
for name,seq in sequences.items():
 levels=[x['nivel'] for x in seq]
 check(levels==sorted(levels),'Ordem de níveis em cada Caminho, Trilha e rota',{'nome':name,'niveis':levels})
(R/'SEQUENCIAS-DE-NIVEL.json').write_text(json.dumps(sequences,ensure_ascii=False,indent=2)+'\n')
# Títulos adjacentes: só podem compartilhar uma aparência se não forem distintos (continuação).
heads={'major','compactmajor','h1','h2','h3','marker'};prev=None;adjacent=[]
for e in m['eventos']:
 if e['gerado'] or not e.get('bloco'):continue
 if e['tipo'] in heads:
  if prev:
   style=lambda q:q.get('tratamento_hierarquia') or q['tipo']
   if style(prev)==style(e):adjacent.append({'pagina':e['pagina'],'antes':prev['texto'],'depois':e['texto'],'estilo':style(e)})
  prev=e
 elif e['tipo'] not in {'cost','small'}:prev=None
(R/'TITULOS-ADJACENTES.json').write_text(json.dumps(adjacent,ensure_ascii=False,indent=2)+'\n')
(R/'INVENTARIO-CAMINHOS-E-TRILHAS.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
report={'paginas':len(pdf.pages),'paginas_sumario':[p['pagina'] for p in toc],'secoes_sumario':len(nav),'links_sumario_conferidos':navchecks,'blocos_alterados':len(rows),'texto_identico_fora_dos_registros':changed==recorded,'r39_intacta':preserved,'inventario_caminhos_trilhas_rotas':len(inventory),'titulos_adjacentes_para_revisar':adjacent,'problemas':issues,'sha256_pdf':hashlib.sha256((B/m['pdf']).read_bytes()).hexdigest()}
(R/'CONFERENCIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(issues))

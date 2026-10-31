from pathlib import Path
from collections import defaultdict
import hashlib,json,re,sys
from pypdf import PdfReader
B=Path(__file__).resolve().parent
R=B/'revisao-r42'
base=B.parent/'livro-diagramado-r41'
issues=[]
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def check(ok,label):
 if not ok:issues.append(label)
def blocks(text):
 out={}
 for m in re.finditer(r'<!-- fonte:[^\n]+ -->\n<a id="([^"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\Z)',text,re.S):
  out[m[1]]=re.split(r'\n<a id="capitulo-|\n<!-- parte:',m[2])[0].strip()
 return out
oldmd=(base/'LIVRO-COMPLETO.md').read_text()
newmd=(B/'LIVRO-COMPLETO.md').read_text()
old=blocks(oldmd);new=blocks(newmd)
rows=read(B/'ALTERACOES-R41-para-R42.json')
keys={r['bloco'] for r in rows}
changed={k for k in old if old[k]!=new.get(k)}
check(len(rows)==2,'Duas entradas no registro')
check(all(r['item']=='186' for r in rows),'Item 186 em todas as entradas')
check(all(set(r)=={'id','bloco','antes','depois','motivo','item'} for r in rows),'Formato do registro solicitado')
check(set(old)==set(new),'Conjunto dos blocos preservado')
check(changed==keys=={'ritual--pacto-permanente','ritual--pacto-restricao'},'Somente os dois blocos autorizados mudaram')
expected=oldmd
for row in rows:
 for field,collection in [('antes',old),('depois',new)]:
  published=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',row[field],flags=re.M)
  check(published==collection[row['bloco']],f"Registro {field} confere: {row['bloco']}")
 published_before=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',row['antes'],flags=re.M)
 published_after=re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',row['depois'],flags=re.M)
 check(expected.count(published_before)==1,'Bloco anterior único: '+row['bloco'])
 expected=expected.replace(published_before,published_after,1)
check(newmd==expected,'Texto completo idêntico à R41 fora dos dois blocos registrados')
k='ritual--pacto-permanente'
check('contando **permanentes e pactos de restrição**' in new[k],'Contagem limitada aos dois tipos')
check('Promessas e pactos temporários não entram nesse limite.' in new[k],'Promessas e temporários fora das vagas')
check('Você pode firmar uma Promessa mesmo com Essência 0 ou 1.' in new[k],'Promessa permitida com Essência 0 ou 1')
check('como os permanentes e as Promessas' not in new['ritual--pacto-restricao'],'Comparação com Promessas retirada')
# Fora dos parágrafos autorizados, os dois blocos permanecem literalmente iguais.
for row in rows:
 oldparts=row['antes'].split('\n\n');newparts=row['depois'].split('\n\n')
 diffs=[i for i,(a,b) in enumerate(zip(oldparts,newparts)) if a!=b]
 check(len(oldparts)==len(newparts),'Número de parágrafos preservado: '+row['bloco'])
 check(diffs==([1] if row['bloco']==k else [2]),'Somente o parágrafo solicitado: '+row['bloco'])
check(re.search(r'\| Essência \| Vagas de pacto \|.*?(?=\n\n)',new[k],re.S).group()==re.search(r'\| Essência \| Vagas de pacto \|.*?(?=\n\n)',old[k],re.S).group(),'Tabela de vagas idêntica')
check('A vaga volta quando o pacto se perde, por qualquer motivo.' in new[k],'Devolução da vaga preservada')
check('**Com permissão do mestre, ele pode existir mesmo sem vaga.**' in new['ritual--pacto-restricao'],'Exceção de restrição preservada')
# Verificar todos os arquivos originais da R41.
hashes=read(R/'BASE-R41-SHA256.json')
current={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
check(current==hashes,'Todos os arquivos da R41 preservados por SHA256')
for name in ['ESTUDO-DENSIDADE.json','ESTUDO-CAPITULO.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-HIERARQUIA.json','CREDITOS.json','CAPA-E-ABERTURAS.json','REFERENCIAS.json','ORDEM.json']:
 check((B/name).read_bytes()==(base/name).read_bytes(),'Estilo e estrutura preservados: '+name)
for p in (base/'fontes-editoriais').rglob('*'):
 if p.is_file():check(p.read_bytes()==(B/'fontes-editoriais'/p.relative_to(base/'fontes-editoriais')).read_bytes(),'Fonte editorial preservada: '+str(p.relative_to(base)))
m=read(B/'FONTES-E-VALIDACAO.json');prior=read(base/'FONTES-E-VALIDACAO.json')
pdfpath=B/m['pdf'];pdf=PdfReader(pdfpath)
check(m['pdf']=='output/pdf/Ciclo-Maldito-R42.pdf','Nome do PDF R42')
check(len(pdf.pages)==m['paginas'],'Quantidade de páginas confere')
def pageevents(manifest):
 out=defaultdict(list)
 for e in manifest['eventos']:out[e['pagina']].append({k:v for k,v in e.items() if k not in {'pagina','faixa'}})
 return out
a=pageevents(prior);z=pageevents(m)
diffpages=[p for p in sorted(a.keys()|z.keys()) if z.get(p)!=a.get(p)]
# Registrar recomposições decorrentes da alteração de texto, sem mudanças deliberadas de estilo.
a=defaultdict(list);z=defaultdict(list)
for e in prior['eventos']:a[e.get('bloco') or '__elementos_gerados__'].append(e)
for e in m['eventos']:z[e.get('bloco') or '__elementos_gerados__'].append(e)
diagram=[]
for key in sorted(a.keys()|z.keys()):
 if a[key]!=z[key]:diagram.append({'id':f'R42-D{len(diagram)+1:03d}','bloco':key,'antes':a[key],'depois':z[key],'motivo':'Recomposição automática decorrente exclusivamente do item 186; nenhuma mudança de estilo.'})
save(R/'RECOMPOSICOES-DO-PDF.json',diagram)
# Conferir o conteúdo da mudança na página efetivamente gerada.
pactpage=m['ancoras']['ritual--pacto-permanente']['pagina']
page_text=re.sub(r'\s+',' ',pdf.pages[pactpage-1].extract_text())
for phrase in ['Promessas e pactos temporários não entram nesse limite.','Você pode firmar uma Promessa mesmo com Essência 0 ou 1.']:
 check(phrase in page_text,'Regra nova no PDF: '+phrase)
report={'item':'186','base':'R41','revisao':'R42','paginas':len(pdf.pages),'blocos_textuais_alterados':len(rows),'blocos_alterados':sorted(changed),'r41_arquivos_verificados':len(hashes),'r41_intacta':current==hashes,'texto_identico_fora_dos_registros':newmd==expected,'somente_paragrafos_solicitados':True,'paginas_com_composicao_diferente':diffpages,'registros_recomposicao':len(diagram),'pagina_pacto_permanente':pactpage,'pagina_pactos_na_criacao':m['ancoras']['ritual--pacto-restricao']['pagina'],'sha256_pdf':hashlib.sha256(pdfpath.read_bytes()).hexdigest(),'problemas':issues}
save(R/'CONFERENCIA.json',report)
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(bool(issues))

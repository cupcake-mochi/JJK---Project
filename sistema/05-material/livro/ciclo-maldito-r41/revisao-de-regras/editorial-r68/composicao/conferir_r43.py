from pathlib import Path
from collections import defaultdict
import json,re,hashlib,sys
from pypdf import PdfReader
B=Path(__file__).resolve().parent
R=B/'revisao-r43';base=B.parent/'livro-diagramado-r42';issues=[]
def read(p):return json.loads(p.read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def check(ok,label):
 if not ok:issues.append(label)
def blocks(text):
 return {m[1]:re.split(r'\n<a id="capitulo-|\n<!-- parte:',m[2])[0].strip() for m in re.finditer(r'<!-- fonte:[^\n]+ -->\n<a id="([^"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\Z)',text,re.S)}
oldmd=(base/'LIVRO-COMPLETO.md').read_text();newmd=(B/'LIVRO-COMPLETO.md').read_text()
old=blocks(oldmd);new=blocks(newmd);rows=read(B/'ALTERACOES-R42-para-R43.json')
changed={k for k in old if old[k]!=new.get(k)}
expectedkeys={'geral--ataques','geral--bloquear','bastiao--bas-olhos','incursor--inc-fluidez','incursor--inc-redirecionar-resolucao','consulta--consulta-ataques'}
check(len(rows)==6,'Seis entradas no registro')
check(set(old)==set(new),'Conjunto dos blocos preservado')
check(changed=={r['bloco'] for r in rows}==expectedkeys,'Somente os seis blocos registrados mudaram')
expected=oldmd
for row in rows:
 check(set(row)=={'id','bloco','antes','depois','motivo','item'},'Formato do registro: '+row['id'])
 def pub(s):return re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',s,flags=re.M)
 a,z=pub(row['antes']),pub(row['depois'])
 check(a==old[row['bloco']],'Antes confere: '+row['bloco'])
 check(z==new[row['bloco']],'Depois confere: '+row['bloco'])
 check(expected.count(a)==1,'Bloco anterior único: '+row['bloco'])
 expected=expected.replace(a,z,1)
check(expected==newmd,'Texto integral idêntico à R42 fora das alterações registradas')
key='geral--bloquear'
check('**antes da rolagem de acerto do atacante**, sem conhecer seu resultado' in new[key],'Bloquear declarado antes da rolagem')
for sentence in ['> **Bloquear = 2d10 + (sua Defesa - 11)**.','Bloquear é gratuito, **não gasta Reação**','**O resultado substitui a Defesa, mesmo se for menor.**','**Guarda Aberta impede Bloquear.**','A propriedade **Talha** aplica **-1 ao resultado de Bloquear**']:
 check(sentence in new[key],'Procedimento preservado: '+sentence)
check(new['geral--aparar']==old['geral--aparar'],'Aparar e Brecha idênticos')
check('antes da rolagem de acerto' in new['geral--ataques'],'Sequência geral antecipada')
check('Ao assumir o golpe, escolha entre **sua Defesa** e **Bloquear**, antes da rolagem do atacante' in new['bastiao--bas-olhos'],'Olhos Em Mim acompanha declaração anterior')
check('Após rolar o d20 e antes de resolver a defesa do alvo, gaste Fluidez' in new['incursor--inc-fluidez'],'Instante Decisivo conserva gasto depois do d20 e antes da defesa')
red=new['incursor--inc-redirecionar-resolucao']
check('Não role novamente o ataque.' in red,'Redirecionar conserva a rolagem original')
check('Ele **não pode Bloquear** esse ataque.' in red,'Novo alvo usa somente Defesa')
check('O mesmo 17 supera a Defesa 15 do novo alvo, que não pode Bloquear: o ataque acerta.' in red,'Exemplo de redirecionamento atualizado')
check('que pode **Bloquear normalmente**' not in red and 'Bloquear e as respostas' not in red,'Permissões contraditórias removidas')
check('2. O alvo escolhe entre sua Defesa e Bloquear, quando permitido.' in new['consulta--consulta-ataques'],'Consulta rápida na mesma ordem')
for phrase in ['depois de conhecer a rolagem do atacante','antes de o alvo escolher entre a Defesa e Bloquear','Depois da rolagem, resolva contra **sua Defesa** ou escolha **Bloquear**']:
 check(phrase not in newmd,'Redação contraditória ausente: '+phrase)
# Preservar a decisão anterior das Promessas.
for k in ['ritual--pacto-permanente','ritual--pacto-restricao']:
 check(old[k]==new[k],'Item 186 preservado: '+k)
hashes=read(R/'BASE-R42-SHA256.json')
now={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
check(now==hashes,'R42 integralmente preservada por SHA256')
for name in ['ESTUDO-DENSIDADE.json','ESTUDO-CAPITULO.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-HIERARQUIA.json','CREDITOS.json','CAPA-E-ABERTURAS.json','REFERENCIAS.json','ORDEM.json']:
 check((B/name).read_bytes()==(base/name).read_bytes(),'Estilo, créditos e estrutura preservados: '+name)
for p in (base/'fontes-editoriais').rglob('*'):
 if p.is_file():check(p.read_bytes()==(B/'fontes-editoriais'/p.relative_to(base/'fontes-editoriais')).read_bytes(),'Fonte editorial preservada: '+str(p.relative_to(base)))
m=read(B/'FONTES-E-VALIDACAO.json');prior=read(base/'FONTES-E-VALIDACAO.json');pdf=PdfReader(B/m['pdf'])
check(m['pdf']=='output/pdf/Ciclo-Maldito-R43.pdf','PDF R43 identificado')
check(len(pdf.pages)==m['paginas'],'Contagem de páginas confere')
def bypage(data):
 out=defaultdict(list)
 for e in data['eventos']:out[e['pagina']].append({k:v for k,v in e.items() if k not in {'pagina','faixa'}})
 return out
a,z=bypage(prior),bypage(m)
diffpages=[p for p in sorted(a.keys()|z.keys()) if a.get(p)!=z.get(p)]
a,z=defaultdict(list),defaultdict(list)
for e in prior['eventos']:a[e.get('bloco') or '__elementos_gerados__'].append(e)
for e in m['eventos']:z[e.get('bloco') or '__elementos_gerados__'].append(e)
recomps=[]
for k in sorted(a.keys()|z.keys()):
 if a[k]!=z[k]:recomps.append({'id':f'R43-D{len(recomps)+1:03d}','bloco':k,'antes':a[k],'depois':z[k],'motivo':'Recomposição automática decorrente da mudança de Bloquear e da decisão sobre Redirecionar a Força, sem mudança de estilo.'})
save(R/'RECOMPOSICOES-DO-PDF.json',recomps)
pageskeys={k:m['ancoras'][k]['pagina'] for k in sorted(expectedkeys)}
page=m['ancoras']['geral--bloquear']['pagina'];text=' '.join(pdf.pages[page-1].extract_text().split())
check('antes da rolagem de acerto do atacante' in text,'Bloquear novo no PDF')
page=m['ancoras']['incursor--inc-redirecionar-resolucao']['pagina'];text=' '.join(pdf.pages[page-1].extract_text().split())
check('não pode Bloquear' in text and 'Não role novamente o ataque.' in text,'Decisão de Redirecionar no PDF')
report={'base':'R42','revisao':'R43','data':'2026-10-10','paginas':len(pdf.pages),'blocos_textuais_alterados':len(rows),'blocos_alterados':sorted(changed),'exemplos_ajustados':['Ataques: Sousuke e Defesa 17','Bloquear: Rina e ataque 18','Redirecionar a Força: resultado 17 contra Defesa 15'],'r42_arquivos_verificados':len(hashes),'r42_intacta':now==hashes,'texto_identico_fora_dos_registros':expected==newmd,'paginas_com_composicao_diferente':diffpages,'paginas_dos_blocos':pageskeys,'recomposicoes_registradas':len(recomps),'sha256_pdf':hashlib.sha256((B/m['pdf']).read_bytes()).hexdigest(),'problemas':issues}
save(R/'CONFERENCIA.json',report)
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(bool(issues))

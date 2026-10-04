from pathlib import Path
import re,json,hashlib,difflib,collections
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'consolidacao/lote-01/migracao-nomes';files=json.loads((P/'consolidacao/lote-01/ORDEM.json').read_text())['fontes']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[];reports=[]
def ck(n,a,b):checks.append({'teste':n,'obtido':a,'esperado':b,'ok':a==b})
def display(t):return re.sub(r'\]\(#[^)]+\)',']',re.sub(r'<!-- page:[^|]+\|','',t))
def rows(t):return [len(l.strip('|').split('|')) for l in t.splitlines() if l.startswith('|')]
protected=['Incursor','Pugilista','Malabarista','Refino','Lapidação','Fundamento']
for key,n in files.items():
 if key=='consulta':continue
 p=P/n;b=B/'antes'/n;before=b.read_text();after=p.read_text()
 ck(key+'-ancoras',re.findall(r'<!-- page:([^|]+)',after),re.findall(r'<!-- page:([^|]+)',before))
 ck(key+'-destinos-links',re.findall(r'\]\(#([^)]+)\)',after),re.findall(r'\]\(#([^)]+)\)',before))
 ck(key+'-numeros-na-ordem',re.findall(r'\d+(?:[.,]\d+)?',after),re.findall(r'\d+(?:[.,]\d+)?',before))
 ck(key+'-estrutura-tabelas',rows(after),rows(before))
 ck(key+'-adjetivos-comuns',re.findall(r'(?i)\b(?:proteção|CD|benefício|efeito) passiv[ao]s?\b',after),re.findall(r'(?i)\b(?:proteção|CD|benefício|efeito) passiv[ao]s?\b',before))
 for term in protected:ck(key+'-preservar-'+term,len(re.findall(r'\b'+term+r'\b',after)),len(re.findall(r'\b'+term+r'\b',before)))
 public=display(after)
 ck(key+'-antigos-centrais-ausentes',re.findall(r'\b(?:Incapacitad[oa]|Classe Passiva|Classes Passivas|CP[123]?|Passiva Livre)\b',public),[])
 # Category names can no longer occur; common adjectives intentionally remain.
 rest=re.sub(r'(?i)\b(?:proteção|CD|benefício|efeito) passiv[ao]s?\b','',public)
 ck(key+'-categoria-passiva-ausente',re.findall(r'\b[Pp]assivas?\b',rest),[])
 clean=public.replace('**','').replace('[','').replace(']','')
 bad=re.findall(r'\b(?:a|as|uma|umas|da|das|na|nas|pela|pelas|essa|essas|esta|estas|aquela|aquelas|sua|suas|toda|todas|numa) [Tt]alentos?\b',clean)
 ck(key+'-concordancia-anterior',bad,[])
 ck(key+'-concordancia-posterior',re.findall(r'\b[Tt]alentos? (?:própria|pagas?|específica|criada|adquiridas?|concedidas?|reativa|permitidas)\b',clean),[])
 ck(key+'-sem-rótulo-classe-talento',re.findall(r'\b[Tt]alentos? (?:de |da mesma )Classes?\b',clean),[])
 oldlines=before.splitlines();newlines=after.splitlines();changes=[]
 for tag,i,j,k,l in difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False).get_opcodes():
  if tag!='equal':changes.append({'linha_antes':i+1,'linha_depois':k+1,'antes':oldlines[i:j],'depois':newlines[k:l],'contexto_anterior':oldlines[max(0,i-1):i],'contexto_posterior':oldlines[j:j+1]})
 d='\n'.join(difflib.unified_diff(oldlines,newlines,n,n,n=2))+'\n'
 if changes:
  dp=B/'diffs'/(key+'.diff');dp.parent.mkdir(exist_ok=True);dp.write_text(d)
 reports.append({'chave':key,'arquivo':n,'sha256_antes':sha(b),'sha256_depois':sha(p),'alterado':bool(changes),'hunks':len(changes),'linhas_antes_alteradas':sum(len(c['antes']) for c in changes),'linhas_depois_alteradas':sum(len(c['depois']) for c in changes),'alteracoes':changes,'diff':str(dp.relative_to(B)) if changes else None})
cat=(P/files['catalogo']).read_text();fun=(P/files['fundamento']).read_text();rot=(P/files['rotas']).read_text();inc=(P/files['incursor']).read_text();dmg=(P/files['dano']).read_text()
for title in ['Identificar Feitiço  -  Leve','Leitura de Feitiços','Talento Próprio','Talentos de Categoria 1','Talentos de Categoria 2','Talentos de Categoria 3']:ck('titulo-'+title,'# '+title in cat,True)
ck('efeito-identificar-preservado','Você descobre qual foi o último feitiço conjurado pelo alvo e sua Classe.' in cat,True)
ck('leitura-nao-promete-classe','Leitura de Feitiços não informa a Classe.' in cat,True)
ck('CE-definida-em-fundamento','Categorias de Efeito (CE)' in fun,True)
ck('expressao-nao-ocupa','A Expressão da técnica não ocupa espaço' in fun,True)
ck('guarda-acoes-preservadas','Você conserva suas ações e sua Defesa estática.' in dmg,True)
ck('guarda-criticos-preservados','Ataques corpo a corpo com arma ou desarmados **que acertarem você** são críticos.' in dmg,True)
ck('guarda-fluidez-gatilho','Enquanto estiver com a Guarda Aberta, não pode ganhar ou manter Fluidez.' in inc,True)
ck('remissao-socorro','Consulte Socorro para as consequências da queda.' in cat,True)
ck('remissao-derrota','conforme Derrota e morte.' in (P/files['progressao']).read_text(),True)
r={'data':'2026-10-03','estado':'fontes migradas, PDFs e evidências das unidades ainda pendentes de atualização','ok':all(x['ok'] for x in checks),'verificacoes':len(checks),'arquivos_examinados':len(reports),'arquivos_alterados':sum(r['alterado'] for r in reports),'hunks_total':sum(r['hunks'] for r in reports),'linhas_alteradas':sum(r['linhas_depois_alteradas'] for r in reports),'consulta':'Excluída desta escrita; migração e aliases de Consulta pertencem a /root/maxima.','checks':checks,'arquivos':reports,'limites':['Revisão contextual de todas as linhas alteradas, com ajuste de gênero e pronomes.','Igualdade de números, tabelas e âncoras não substitui nova revisão editorial/independente e nova inspeção do PDF.','Scripts e evidências anteriores não foram retocados para fingir validação do texto novo.','Sem novos efeitos mecânicos; duas correções de remissão expressamente autorizadas foram incluídas.']}
(B/'MIGRACAO.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['ok','verificacoes','arquivos_examinados','arquivos_alterados','hunks_total','linhas_alteradas']},ensure_ascii=False));print(json.dumps([c for c in checks if not c['ok']],ensure_ascii=False))
raise SystemExit(0 if r['ok'] else 1)

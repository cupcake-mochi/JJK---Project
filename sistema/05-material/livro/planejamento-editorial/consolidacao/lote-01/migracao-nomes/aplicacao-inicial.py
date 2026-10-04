from pathlib import Path
import re,json,hashlib,difflib
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'consolidacao/lote-01/migracao-nomes';B.mkdir(exist_ok=True)
files=json.loads((P/'consolidacao/lote-01/ORDEM.json').read_text())['fontes']
for k,n in files.items():
 if k=='consulta':continue
 p=P/n;backup=B/'antes'/n;backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():backup.write_bytes(p.read_bytes())
 # Always begin from stored original, not a partly migrated source.
 s=backup.read_text()
 # Protect identifiers and common adjectives; this migration changes display prose only.
 holds={}
 def hold(m):
  key=f'ZZKEEP{len(holds)}ZZ';holds[key]=m[0];return key
 s=re.sub(r'(?<=page:)[^|\n]+|(?<=\]\(#)[^)]+',hold,s)
 s=re.sub(r'(?i)\b(?:proteção|CD|benefício|efeito) passiv[ao]s?\b',hold,s)
 s=re.sub(r'Classes Passivas','Categorias de Efeito',s)
 s=re.sub(r'Classe Passiva','Categoria de Efeito',s)
 s=re.sub(r'\bCP(?=\b|[123])','CE',s)
 s=re.sub(r'Passivas de Classes','Talentos de Categorias',s)
 s=re.sub(r'Passivas de Classe','Talentos de Categoria',s)
 s=re.sub(r'Passiva de Classe','Talento de Categoria',s)
 s=s.replace('Passiva Livre','Expressão da técnica')
 s=re.sub(r'\bPassivas\b','Talentos',s);s=re.sub(r'\bPassiva\b','Talento',s)
 s=re.sub(r'\bpassivas\b','talentos',s);s=re.sub(r'\bpassiva\b','talento',s)
 # Gender directly connected to the acquired category, not other feminine referents.
 feminine={'a':'o','as':'os','uma':'um','umas':'uns','da':'do','das':'dos','na':'no','nas':'nos','pela':'pelo','pelas':'pelos','essa':'esse','essas':'esses','esta':'este','estas':'estes','aquela':'aquele','aquelas':'aqueles','sua':'seu','suas':'seus','minha':'meu','minhas':'meus','nossa':'nosso','nossas':'nossos','qual':'qual','outra':'outro','outras':'outros','nova':'novo','novas':'novos','nenhuma':'nenhum','nenhumas':'nenhuns','mesma':'mesmo','mesmas':'mesmos','primeira':'primeiro','segunda':'segundo','terceira':'terceiro','única':'único','únicas':'únicos','própria':'próprio','próprias':'próprios','à':'ao','às':'aos'}
 # multiword premodifiers up to three words before the target
 rx=re.compile(r'\b('+'|'.join(sorted(feminine,key=len,reverse=True))+r')(?=\s+(?:\*\*)?(?:(?:primeira|segunda|terceira|única|únicas|própria|próprias|outra|outras|nova|novas|mesma|mesmas|sua|suas)\s+){0,3}[Tt]alentos?\b)',re.I)
 def masculine(m):
  v=feminine[m[0].lower()];return v[0].upper()+v[1:] if m[0][0].isupper() else v
 s=rx.sub(masculine,s)
 # premodifier changed from feminine in first pass: fix the determinant now
 rx2=re.compile(r'\b('+'|'.join(sorted(feminine,key=len,reverse=True))+r')(?=\s+(?:\*\*)?(?:(?:primeiro|segundo|terceiro|único|únicos|próprio|próprios|outro|outros|novo|novos|mesmo|mesmos|seu|seus)\s+){0,3}[Tt]alentos?\b)',re.I)
 s=rx2.sub(masculine,s)
 for a,b in [('Própria','Próprio'),('própria','próprio'),('próprias','próprios'),('pagas','pagos'),('paga','pago'),('compradas','comprados'),('comprada','comprado'),('adquiridas','adquiridos'),('adquirida','adquirido'),('antigas','antigos'),('concedida','concedido'),('concedidas','concedidos'),('reativa','reativo'),('permitidas','permitidos'),('escolhidas','escolhidos')]:
  s=re.sub(r'(\b[Tt]alentos?\s+)'+a+r'\b',lambda m:m[1]+b,s)
 s=s.replace('uma de seus talentos','um de seus talentos').replace('uma de seus Talentos','um de seus Talentos')
 # Guard state: grammatical form selected from context.
 s=re.sub(r'\bIncapacitada?\b','Guarda Aberta',s) if False else s
 s=re.sub(r'(?<=ficar )Incapacitad[oa]\b','com a Guarda Aberta',s)
 s=re.sub(r'(?<=estiver )Incapacitad[oa]\b','com a Guarda Aberta',s)
 s=s.replace('inimigo Incapacitado','inimigo com a Guarda Aberta')
 s=re.sub(r'\bIncapacitad[oa]\b','Guarda Aberta',s)
 if k=='catalogo':
  s=s.replace('## Aviso  -  Leve','## Identificar Feitiço  -  Leve').replace('Aviso é uma informação obtida','Identificar Feitiço fornece uma informação obtida')
  s=s.replace('## Aviso\n','## Leitura de Feitiços\n')
  s=s.replace('Esta é o Talento Aviso. A Melhoria de mesmo nome tem outro efeito e é comprada separadamente.','Leitura de Feitiços não informa a Classe. A Melhoria Identificar Feitiço tem efeito e aquisição próprios.')
  s=s.replace('Consulte Recuperação para as consequências da queda.','Consulte Socorro para as consequências da queda.')
 if k=='construcao':
  s=s.replace('| Aviso |','| Leitura de Feitiços |')
  s=s.replace('**Aviso, o Talento, e Aviso, a Melhoria de Marca, são escolhas diferentes.** Uma não compra a outra.','**Leitura de Feitiços é um Talento; Identificar Feitiço é uma Melhoria de Marca.** Adquirir um desses efeitos não concede o outro.')
 if k=='progressao':
  s=s.replace('conforme Recuperação.','conforme Derrota e morte.')
 for h,orig in holds.items():s=s.replace(h,orig)
 assert re.findall(r'<!-- page:([^|]+)',s)==re.findall(r'<!-- page:([^|]+)',backup.read_text())
 p.write_text(s)
print('Primeira aplicação salva. Gramática e categoria contextual ainda serão revisadas; não exportar.')

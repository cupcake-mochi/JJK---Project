from pathlib import Path
import re,json,unicodedata,difflib

B=Path(__file__).resolve().parents[1]
R=B/'revisao-r53'
ROOT=B.parents[1]
SOURCE=ROOT/'desenvolvimento-fundamentos/capitulo-para-avaliacao-v8/FUNDAMENTO-CAPITULO.md'
raw=SOURCE.read_text()
old=json.loads((R/'BLOCOS-R52.json').read_text())
texts=dict(old);specs={};group_orders={};origins={};aliases={}

def slug(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().casefold()
 return re.sub(r'[^a-z0-9]+','-',s).strip('-')

heads=[{'start':m.start(),'end':m.end(),'level':len(m[1]),'title':m[2]} for m in re.finditer(r'^(#{1,5}) (.+)$',raw,re.M)]
def segment(title,level=None):
 match=[h for h in heads if h['title']==title and (level is None or h['level']==level)]
 assert len(match)==1,(title,level,len(match))
 a=match[0];end=next((h['start'] for h in heads if h['start']>a['start'] and h['level']<=a['level']),len(raw))
 return raw[a['start']:end].strip()

def body(s):return s.split('\n',1)[1].strip() if '\n' in s else ''

def register(key,s,chapter,context,entries=False,first_override=None):
 rows=[];out=[]
 for line in s.splitlines():
  m=re.match(r'^(#{1,5}) (.+)',line)
  if not m:out.append(line);continue
  lv=len(m[1]);title=m[2]
  if lv==1:kind='h1';style=None
  elif lv==2:kind='h1';style=None
  elif lv==3:kind='h2';style='grupo'
  else:
   kind='h2' if entries and lv==4 else 'h3';style='entrada' if entries and lv==4 else 'subtopico'
   if title.startswith('Exemplo:'):style='exemplo'
  if not rows and first_override:kind,style=first_override
  mdlevel=int(kind[1:])
  rows.append({'titulo':title,'tipo':kind,'tratamento':style,'nivel_editorial':mdlevel})
  out.append('#'*mdlevel+' '+title)
 texts[key]='\n'.join(out).strip()
 if chapter==10 and context.startswith('Fundamento / '):context=context[len('Fundamento / '):]
 specs[key]={'capitulo':chapter,'contexto':context,'titulos':rows,'origem':'Capítulo aprovado v8'}
 origins[key]=s

# Fundamento completo, mantendo as identidades já usadas nas remissões.
first=raw[:next(h['start'] for h in heads if h['title']=='Sua técnica' and h['level']==3)].strip()
first=first.replace('Este capítulo apresenta as regras de criação de feitiços e suas aplicações nas outras rotas. Consulte o livro para as regras gerais de combate, de Dano e recuperação e de aquisição de entidades. Esta versão foi preparada para avaliação dos leitores.','Este capítulo apresenta as regras de criação de feitiços e suas aplicações nas outras rotas. As regras gerais de combate, de Dano e recuperação e de aquisição de entidades estão nos capítulos correspondentes.')
register('fundamento--fundamento',first,10,'Fundamento')
foundation=[('Sua técnica','tecnica'),('Seu primeiro feitiço','primeiro'),('Famílias','familias'),('Selo e Talentos','selo'),('Feitiços conhecidos','repertorio'),('Pontos e preços','pontos'),('Funções e saldo','funcoes'),('Formas','formas'),('Alcance e área','alcance'),('Conjurar','conjurar'),('Restrições','restricoes'),('Combinar peças','combinacoes'),('Três mesclas prontas','mesclas'),('Controle','controle'),('Outras aplicações','aplicacoes'),('Dano e repetições','danolimites'),('Áreas persistentes','persistente'),('Uso Livre','livre'),('Efeitos fora de combate','efeito'),('Ampliar um feitiço','ampliar'),('Feitiços de Classe 0','classezero'),('Efeitos próprios','proprio'),('Liberação Máxima','liberacao'),('Técnica Máxima','maxima'),('Exemplo: Passagem de Papel','passagem'),('Exemplo: Retirada de Emergência','retirada'),('Ficha de feitiço','ficha')]
foundation_order=['fundamento--fundamento']
for title,anchor in foundation:
 key='fundamento--'+anchor;register(key,segment(title,3),10,'Fundamento / '+title);foundation_order.append(key)
for k in [k for k in old if k.startswith('fundamento--') and k not in foundation_order]:texts.pop(k)
group_orders['fundamento']=foundation_order
aliases.update({'fundamento--amparoformas':{'bloco':'fundamento--funcoes','titulo':'Cura e vida temporária'},'fundamento--maximadano':{'bloco':'fundamento--maxima','titulo':'Ataque, cura e utilidade'},'fundamento--limitesmaxima':{'bloco':'fundamento--maxima','titulo':'Melhorias da Técnica Máxima'}})

# Catálogo: efeitos e modificadores na ordem aprovada, com destino por entrada.
for k in [k for k in texts if k.startswith('catalogo--')]:texts.pop(k)
cat_order=[]
intro=segment('Catálogo de Melhorias',2)
intro=intro[:intro.index('### Efeitos: acrescentar uma função')].strip()
intro='# Catálogo de criação\n\n'+body(intro)
register('catalogo--cat-catalogo',intro,11,'Catálogo de criação');cat_order.append('catalogo--cat-catalogo')
entry_keys={}
for title,key in [('Efeitos: acrescentar uma função','cat-efeitos'),('Modificadores: ajustar a aplicação','cat-modificadores'),('Criação própria','cat-proprio')]:
 s=segment(title,3)
 split=re.split(r'(?=^#### )',s,flags=re.M)
 section_key='catalogo--'+key
 register(section_key,split[0].strip(),11,title,first_override=('h1',None));cat_order.append(section_key)
 for piece in split[1:]:
  name=re.match(r'^#### (.+)',piece)[1]
  ek='catalogo--melhoria-'+slug(name)
  register(ek,piece.strip(),11,title,entries=True);cat_order.append(ek);entry_keys[name]=ek
rest=segment('Catálogo de Restrições',2)
# A faixa principal apresenta os quatro grupos de consulta.
register('catalogo--cat-restricoes','# Catálogo de Restrições\n\nEscolha as Restrições compatíveis com sua montagem. As regras de devolução e de quantidade estão em [Restrições](#restricoes).',11,'Catálogo de Restrições');cat_order.append('catalogo--cat-restricoes')
for title in ['Restrições de conjuração','Custos e consequências','Condições de uso','Exposição e novas Restrições']:
 s=segment(title,3);pieces=re.split(r'(?=^#### )',s,flags=re.M)
 key='catalogo--grupo-'+slug(title);register(key,pieces[0].strip(),11,'Catálogo de Restrições',first_override=('h2','grupo'));cat_order.append(key)
 for piece in pieces[1:]:
  name=re.match(r'^#### (.+)',piece)[1];ek='catalogo--restricao-'+slug(name)
  register(ek,piece.strip(),11,'Catálogo de Restrições',entries=True);cat_order.append(ek);entry_keys[name]=ek
register('catalogo--cat-talentos','## Talentos e Regra Própria\n\nOs Talentos pagos usam as categorias, os requisitos e os espaços definidos em [Selo e Talentos](#selo).',11,'Talentos e Regra Própria',first_override=('h1',None));cat_order.append('catalogo--cat-talentos')
for title,key in [('Talentos de Categoria 1','cat-passivas-1'),('Talentos de Categoria 2','cat-passivas-2-recursos'),('Talentos de Categoria 3','cat-passivas-3'),('Regra Própria','cat-regra-propria'),('Talento Próprio','cat-passiva-propria')]:
 ek='catalogo--'+key;register(ek,segment(title,3),11,'Talentos e Regra Própria',entries=title.startswith('Talentos de Categoria'));cat_order.append(ek)
group_orders['catalogo']=cat_order
legacy={
 'cat-alcance':'Longe','cat-movimento':'Passo','cat-area':'Maior','cat-area-continua':'Fica','cat-mira':'Precisão','cat-defesas':'Fura','cat-controle':'Condição','cat-obstaculos':'Anteparo','cat-auxiliares':'Impulso','cat-auxiliares-apoio':'Guarda','cat-castigo':'Queima','cat-castigo-dano':'Remate','cat-tempo':'Rápido','cat-tempo-duracao':'Silencioso','cat-marca':'Marca','cat-marca-recursos':'Sugar','cat-amparo':'Limpa','cat-amparo-protecao':'Divide','cat-restricoes-conjuracao':'Queima-Roupa','cat-restricoes-consequencias':'Sangra','cat-restricoes-uso':'Uma Vez','cat-restricoes-proprias':'Barulho','cat-passivas-2-protecao':'Costura'}
for anchor,title in legacy.items():
 key=entry_keys.get(title,'catalogo--cat-passivas-2-recursos')
 aliases['catalogo--'+anchor]={'bloco':key,'titulo':title}

# Rotas e entidades: só os trechos montados pelo capítulo aprovado.
for title,level,key,ch in [
 ('Sem Técnica',3,'rotas--rota-sem-tecnica',13),('Sementes',4,'rotas--rota-sementes',13),
 ('Técnica Marcial',3,'rotas--rota-marcial',13),('Armas',4,'rotas--rota-armas',13),('Ferramenta',4,'rotas--rota-ferramenta',13),
 ('Famílias da entidade',4,'construcao--entidades-familias',17),('Habilidades básicas',3,'construcao--entidades-basicas',17),
 ('Habilidades especiais',3,'construcao--entidades-especiais',17),('Funções e Formas da entidade',4,'construcao--entidades-formas',17),
 ('Alcance e área',4,'construcao--entidades-medidas',17),('Efeitos reduzidos',4,'construcao--entidades-efeitos-reduzidos',17),
 ('Saldo e limites',4,'construcao--entidades-saldo',17),('Controle e utilidade',4,'construcao--entidades-controle',17),
 ('Restrições da entidade',4,'construcao--entidades-restricoes',17),('Ampliar uma especial',3,'construcao--entidades-ampliacao',17)]:
 s=segment(title,level)
 # As seções aninhadas têm blocos próprios no livro.
 if key=='rotas--rota-sem-tecnica':s=s[:s.index('#### Sementes')].strip()
 if key=='rotas--rota-marcial':s=s[:s.index('#### Armas')].strip()
 if key=='construcao--entidades-especiais':s=s[:s.index('#### Funções e Formas da entidade')].strip()
 register(key,s,ch,('Construir invocações' if ch==17 else 'Rotas de criação'),first_override=('h1',None) if key in ['rotas--rota-sem-tecnica','rotas--rota-marcial'] else None)
# Reunir as orientações de rota no capítulo próprio do livro.
route_intro=body(segment('Outras rotas e entidades',2)).split('### Sem Técnica')[0].strip()
route_intro=route_intro.replace('deste capítulo','de [Fundamento](#fundamento--fundamento)').replace('apresentados adiante','apresentados em Construir invocações')
texts['rotas--rotas'] += '\n\n## A mesma montagem, outras aplicações\n\n'+body(route_intro)
entity_intro=body(segment('Montar habilidades da entidade',3)).split('#### Famílias da entidade')[0].strip()
k='construcao--entidades-familias'
first,tail=texts[k].split('\n',1)
texts[k]=first+'\n\n'+entity_intro+'\n'+tail
for title,lev,key in [('Atuação básica',4,'campo--inv-basica'),('Especiais de execução rápida',4,'campo--inv-tempo'),('Especiais com preparação prolongada',4,'campo--inv-restricoes-tempo')]:
    register(key,segment(title,lev),16,'Invocações em campo',first_override=('h1',None))

# Sementes foi extraída de dentro de Sem Técnica; as quatro opções seguem no próprio bloco.
for key in ['construcao--entidades-saldo','construcao--entidades-controle','construcao--entidades-restricoes']:
 pass

# A síntese de interfaces permanece no Fundamento; procedimentos de comando
# ficam em Invocações em campo, evitando duplicar regras em capítulos diferentes.
register('fundamento--interfaces',segment('Caminhos e usos especiais',3),10,'Fundamento / Caminhos e usos especiais')
foundation_order.append('fundamento--interfaces')

# Regras de condição: preservar o texto geral e ajustar só o que o rework exige.
# As treze condições completas ficam em Dano e recuperação, como na R52.
# Remissões curtas da candidata passam aos destinos integrais do livro.
short={
 'conceitos':('fundamento--fundamento','As palavras da montagem'),
 'sua-tecnica':('fundamento--tecnica','Sua técnica'),
 'guia-familias':('fundamento--fundamento','Conheça as Famílias'),
 'familias':('fundamento--familias','Famílias'),
 'fios-de-tensao':('fundamento--tecnica','Fios de Tensão'),
 'funcoes':('fundamento--funcoes','Funções e saldo'),
 'formas':('fundamento--formas','Formas'),
 'melhorias':('catalogo--cat-catalogo','Catálogo de criação'),
 'restricoes':('fundamento--restricoes','Restrições'),
 'pontos-e-precos':('fundamento--pontos','Pontos e preços'),
 'saldo':('fundamento--pontos','Cálculo dos pontos'),
 'selo':('fundamento--selo','Selo e Talentos'),
 'conjurar':('fundamento--conjurar','Conjurar'),
 'catalogo-efeitos':('catalogo--cat-efeitos','Efeitos: acrescentar uma função'),
 'catalogo-modificadores':('catalogo--cat-modificadores','Modificadores: ajustar a aplicação'),
 'empurrao':(entry_keys['Empurrão'],'Empurrão'),
 'condicoes':('dano--condicoes','Condições'),
 'talentos':('catalogo--cat-talentos','Talentos e Regra Própria'),
 'catalogo-restricoes':('catalogo--cat-restricoes','Catálogo de Restrições')}
for alias,(key,title) in short.items():
 target=key if title==specs.get(key,{}).get('titulos',[{}])[0].get('titulo') or key=='dano--condicoes' else 'fundamento-link-'+alias
 if target!=key:aliases[target]={'bloco':key,'titulo':title}
 for k in specs:texts[k]=texts[k].replace('](#'+alias+')','](#'+target+')')

# Qualquer referência da base a uma entrada removida tem destino conservado
# por um alias explícito; os rótulos de índice serão revistos separadamente.
for k in old:
 if k not in texts and k not in aliases:
  raise ValueError(('Bloco removido sem migração de destino',k))

(R/'TEXTOS-TRABALHO.json').write_text(json.dumps(texts,ensure_ascii=False,indent=2)+'\n')
(R/'META-NOVA.json').write_text(json.dumps(specs,ensure_ascii=False,indent=2)+'\n')
(R/'ORDEM-NOVA.json').write_text(json.dumps(group_orders,ensure_ascii=False,indent=2)+'\n')
(R/'ALIASES.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
(R/'ENTRADAS.json').write_text(json.dumps(entry_keys,ensure_ascii=False,indent=2)+'\n')
(R/'ORIGEM-DOS-BLOCOS.json').write_text(json.dumps({k:{'fonte':str(SOURCE),'trecho_aprovado':v} for k,v in origins.items()},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'blocos_base':len(old),'blocos_trabalho':len(texts),'blocos_importados':len(specs),'entradas_catalogo':len(entry_keys),'aliases':len(aliases)},ensure_ascii=False))

exec((Path(__file__).resolve().parent/'r23-redigir.py').read_text())
manual=(R/'sistema/05-material/livro/manual/07-glossario.md').read_text()
old=[];category=''
for n,line in enumerate(manual.splitlines(),1):
 if line.startswith('## '):category=line[3:]
 if line.startswith('| **'):
  for term in re.findall(r'\*\*`?([^*`]+)`?\*\*',line.split('|')[1]):old.append(dict(termo=term,categoria=category,linha=n))
idx={};cover=[]
def add(term,key=None,anchor=None,search=None,note=None,dest=None):
 t=dest or target(key,anchor,search)
 idx[term]={'termo':term,'destino':t,'nota':note}
 return t
for row in G:add(row['termo'],dest=row['destino'])
overrides={
'Promessa':('ritual','promessa'),'Teste':('testes','testes'),'Bloquear':('ataques','bloquear'),'Aparar':('ataques','aparar'),'Brecha':('ataques','aparar'),'Arredondamento':('fundamento','pontos'),'Pontos de vida':('dano','dano'),'Pontos de energia':('rotas','rotas'),'Vida temporária':('recuperacao','temporarios'),'Energia temporária':('recuperacao','temporarios'),'Integridade':('dano','integridade'),'Condição':('dano','condicoes'),'Exaustão':('recuperacao','exaustao'),'Sequela':('recuperacao','sequelas'),'Cicatriz':('recuperacao','sequelas'),'Morrendo':('recuperacao','zero'),'Inconsciente':('recuperacao','inconsciente'),'Cena':('recuperacao','usos'),'Essência':('testes','atributos'),
'Fluidez':('incursor','inc-fluidez'),'Canalizar em Golpe':('aptidoes','apt-canalizar'),'Pontos de Vínculo':('evocador',None),'Básica':('campo','inv-basica'),'Regra':('fundamento','tecnica'),'Pontos':('fundamento','pontos'),'Teto':('fundamento','danolimites'),'Espaço de feitiço':('fundamento','repertorio'),'Liberação Máxima':('fundamento','liberacao'),'Uso Livre':('fundamento','livre'),'Expansão de Domínio':('poderes',None),'Expansão sem Barreiras':('poderes',None),'Dano na alma':('dano','alma'),'Ruptura':('rotas','rota-marcial'),'Ōgi':('rotas','rota-marcial'),'Defesa sem Armadura':('rotas','rota-defesa'),'Estímulo Muscular':('rotas','rota-estimulo'),'Corpo':('progressao','prog-marcos'),'Leque':('progressao','prog-marcos'),'Rodada inteira':('testes','turnos'),'Estudar':('comuns','estudar'),'Cobertura':('ataques','defesa'),'Agarrar':('comuns','manobras'),'Grau':('ferramentas','graus'),'Patente':('progressao','prog-patentes'),
'Estigma':('ferramentas','graus'),'Desgaste':('ferramentas',None),'Oculta':('equipamento','oculta'),'Projétil':('fundamento','formas'),'Toque':('fundamento','formas'),'Explosão':('fundamento','formas'),'Aura':('fundamento','formas'),'Cone':('fundamento','formas'),'Linha':('fundamento','formas'),'Cura':('fundamento','amparoformas'),'Apoio':('fundamento','amparoformas'),'Onda':('fundamento','amparoformas'),'Efeito':('fundamento','amparoformas'),'Versado':('vanguarda',None),
}
catalog_terms='Rápido|Aquecer|Levanta|Fica|Rajada|Inescapável|Anteparo|Toca a Alma|Remenda|Dívida|Escolher|Guarda|Queima|Armado|Efeito Próprio|Mão Firme|Fluxo|Passiva Própria|Concentrada|Duradoura|Alvo de Caça|Corpo a Corpo|Atrasar|Condicional|Gesto|Parado|Uma Vez|Fura|Longe|Maior|Precisão'.split('|')
conditions='Agarrado|Amedrontado|Atordoado|Calado|Cego|Derrubado|Desarmado|Enfeitiçado|Envenenado|Impedido|Incapacitado|Lento|Surdo'.split('|')
props='Emaranha|Fineza|Longo Alcance|Par|Rompe|Talha|Versátil|Vestida|Volumosa'.split('|')
def findentry(key,term):
 # Prefer an exact heading/bold lead or a table row, not an earlier incidental mention.
 pat=r'(?m)^(?:#{1,3} |\*\*|\| \*\*|\| )'+re.escape(term)+r'(?:\*\*|\s*[—:|.]|\s*$)'
 matches=[x for x in sections[key] if re.search(pat,x['texto'])]
 if not matches:
  pat=r'(?m)^#{1,3} .*'+re.escape(term)
  matches=[x for x in sections[key] if re.search(pat,x['texto'])]
 if not matches:raise ValueError((key,term))
 return {k:v for k,v in matches[0].items() if k!='texto'}
for x in old:
 term=x['termo']
 if term=='Passiva Própria':
  t=add('Talento Próprio',dest=findentry('catalogo','Talento Próprio'));add('Passiva Própria (nome anterior)',dest=t)
 elif term in ['Passiva','Classe Passiva']:
  current={'Passiva':'Talento','Classe Passiva':'Categoria de Efeito'}[term];t=idx[current]['destino'];add(term+' (nome anterior)',dest=t)
 elif term in catalog_terms:t=add(term,dest=findentry('catalogo',term))
 elif term in conditions:
  current='Guarda Aberta' if term=='Incapacitado' and '# Guarda Aberta' in (P/files['dano']).read_text() else term
  t=add(current,dest=findentry('dano',current))
  if current!=term:add(term+' (nome anterior)',dest=t)

 elif term in props:t=add(term,'equipamento','oculta' if term=='Volumosa' else 'propriedades')
 elif term in ['Leve','Média','Pesada']:t=add(term,'fundamento','pontos',note='Preço de montagem; categoria de condição em Condições.'+(' Propriedade de arma em Equipamento.' if term=='Leve' else ''))
 elif term in overrides:
  key,a=overrides[term]
  if a is None:
   if term=='Expansão sem Barreiras':t=add(term,'poderes',search='# Expansão sem')
   elif term=='Pontos de Vínculo':t=add(term,'evocador',search='# Pontos de Vínculo')
   else:t=add(term,dest=findentry(key,term))
  else:t=add(term,key,a)
 elif term in idx:t=idx[term]['destino']
 else:raise ValueError('Sem destino: '+term)
 cover.append({**x,'decisao':'Definição breve no glossário' if term in [z['termo'] for z in G] else 'Entrada de índice; regra completa permanece no dono','destino':t})
# Additional current queries important for navigation.
for term,key,anchor in [
 ('Ajudar','testes','ajudar'),('Atacar','ataques','ataques'),('Preparar','comuns','preparar'),('Esconder','comuns','esconder'),('Vasculhar','comuns','procurar'),('Saltos','comuns','saltos'),('Quedas','comuns','quedas'),('Sentir Energia','comuns','mundo'),('Munição','municao',None),('Inventário','equipamento','equipamento'),('Ferramentas e reparo','pericias','reparos'),('Fabricação de entidades','fabricacao',None),('Manifestar','campo','inv-entrada'),('Trocar de entidade','campo','inv-troca'),('Ordem antecipada','campo','inv-antecipada'),('Domar','entidades','entidades-domar'),('Corpo amaldiçoado','campo','inv-corpos'),('XP','progressao','prog-xp'),('Experiência semanal','progressao','prog-semana'),('Trocar de Trilha','progressao','prog-trilhas'),('Bastião','bastiao',None),('Vanguarda','vanguarda',None),('Guia','guia',None),('Emanador','emanador',None),('Evocador','evocador',None),('Incursor','incursor','inc-caminho'),('Assassino','incursor','inc-assassino'),('Pugilista','incursor','inc-pugilista'),('Malabarista','incursor','inc-malabarista'),
]:add(term,key,anchor)
add('CE','fundamento','selo',note='Categoria de Efeito.')
add('CP (sigla anterior)','fundamento','selo',note='Categoria de Efeito; sigla atual: CE.')
add('Passiva Livre (nome anterior)','fundamento','selo',note='Expressão da técnica.')
add('Identificar Feitiço',dest=findentry('catalogo','Identificar Feitiço'))
add('Leitura de Feitiços',dest=findentry('catalogo','Leitura de Feitiços'))
add('Aviso (Melhoria; nome anterior)',dest=idx['Identificar Feitiço']['destino'])
add('Aviso (Talento; nome anterior)',dest=idx['Leitura de Feitiços']['destino'])
add('Ágil (nome anterior)','incursor','inc-caminho')
add('Monge (nome anterior)','incursor','inc-pugilista')
add('Corpo Amaldiçoado (Origem)','origens',search='# Corpo Amaldiçoado')
add('Grau (patente)','progressao','prog-patentes')
add('Força (atributo)','testes','atributos')
add('Força (dano)','dano','tipos')
add('Energia amaldiçoada pura (dano)','dano','tipos',note='Tipo Força.')
# Desambiguação de Cura e destinos específicos do procedimento de recuperação.
former_cure=idx.pop('Cura')
add('Cura (Forma)',dest=former_cure['destino'])
add('Cura (recuperação)','recuperacao','cura')
add('Estágios de Integridade','dano','integridade')
add('Integridade máxima','dano','alma')
add('Socorro','recuperacao','socorro')
add('Aguentar','recuperacao','zero')
add('Insistir','recuperacao','insistir')
idx['Estigma']['nota']='Efeitos das ferramentas, na organização atual.'
idx['Rodada inteira']['nota']='Ação Completa.'
# Include all current subclass names without reproducing their benefits.
for key in ['bastiao','vanguarda','guia','emanador','evocador']:
 for sec in sections[key]:
  if re.search(r'^## (?:Nível 2|Nível 2 —)',sec['texto'],re.M) and len(sec['titulo'].split())<=3:
   add(sec['titulo'],dest={k:v for k,v in sec.items() if k!='texto'})
rows=sorted(idx.values(),key=lambda x:norm(x['termo']))
owner_labels={'fundamento':'Fundamento','catalogo':'Catálogo','dano':'Dano e Recuperação','recuperacao':'Dano e Recuperação','testes':'Regras gerais','ataques':'Regras gerais','comuns':'Regras gerais','movimento':'Regras gerais','campo':'Invocações','entidades':'Montagem de entidades','rotas':'Rotas','ferramentas':'Equipamento','equipamento':'Equipamento','progressao':'Progressão'}
revfiles={v:k for k,v in files.items()}
for r in rows:
 t=r['destino'];key=revfiles[t['arquivo']];r['consulta']=owner_labels.get(key,'')
 if r['consulta'] and norm(r['consulta'])!=norm(t['titulo']):r['consulta']+=': '+t['titulo']
 else:r['consulta']=t['titulo']
 if r['nota']:r['consulta']+='. '+r['nota']
# Each printed index row is generated from its machine-verifiable destination.
index_parts=[]
for i in range(0,len(rows),26):
 c=rows[i:i+26];first=c[0]['termo'][0].upper();last=c[-1]['termo'][0].upper();title='Índice: '+first+('–'+last if last!=first else '');id='consulta-indice-'+str(i//26+1)
 body='| Assunto | Consulta |\n|---|---|\n'+'\n'.join('| '+r['termo']+' | '+r['consulta']+' |' for r in c)
 index_parts.append(f'<!-- page:{id}|{title} -->\n# {title}\n\n'+body+'\n')
with (B/'CONSULTA.md').open('a') as f:f.write('\n'+'\n'.join(index_parts))
(E/'INDICE.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(E/'COBERTURA-GLOSSARIO-ANTIGO.json').write_text(json.dumps(cover,ensure_ascii=False,indent=2)+'\n')
(E/'DESTINOS.json').write_text(json.dumps({'glossario':G,'indice':rows,'paginas_fisicas':'resolver na integração','dependencias':['Patente em Progressão: prog-patentes, integrada pela raiz.','R01-R03 reconciliados em Regras gerais e Dano e Recuperação; qualquer alteração posterior exige nova conferência de destinos.','Equipamento consolidado fornece a propriedade Leve; a consulta remete ao seu dono sem repetir a lista de armas.']},ensure_ascii=False,indent=2)+'\n')
print(len(rows),'entradas no índice;',len(old),'ocorrências antigas rastreadas;',len(parts)+len(index_parts),'páginas')

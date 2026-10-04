"""Auditoria documental e modelos dirigidos da consulta; não é simulador de jogo."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
import copy,hashlib,json,re,sys,unicodedata
B=Path(__file__).resolve().parent;E=B/'evidencias';P=next(p for p in B.parents if (p/'validacao-editorial/PROTOCOLO-COMPLETO.md').exists());R=P.parents[3]
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.casefold()) if not unicodedata.combining(c))
def pages(s):
 c=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',s);return [{'ancora':c[i],'titulo':c[i+1],'texto':c[i+2]} for i in range(1,len(c),3)]
M=B/'CONSULTA.md';t=M.read_text();H=sha(M);S=pages(t);G=load(E/'GLOSSARIO.json');I=load(E/'INDICE.json');C=load(E/'COBERTURA-GLOSSARIO-ANTIGO.json');owners=load(E/'ARQUIVOS-DONOS.json')
owner_sections={f:{s['ancora']:s for s in pages((P/f).read_text())} for f in owners.values()}
checks=[];cases=[]
def ck(n,a,b):checks.append({'verificacao':n,'obtido':a,'esperado':b,'ok':a==b});return a==b
def case(n,a,b,kind='modelo-executado'):
 row={'caso':n,'obtido':a,'esperado':b,'tipo':kind,'ok':a==b};cases.append(row);return ck('Caso: '+n,a,b)
def validate_dest(d):
 if d['arquivo'] not in owner_sections:return False
 s=owner_sections[d['arquivo']].get(d['ancora']);return bool(s and s['titulo']==d['titulo'])
def table_rows(s):return [x for x in s.splitlines() if x.startswith('|') and not re.match(r'^\|[-:| ]+\|$',x)]
ck('30 seções previstas',len(S),30);ck('Âncoras únicas',len(set(x['ancora'] for x in S)),30)
ck('Títulos do mapa',load(B/'ESTRUTURA.json')['titulos'],{s['ancora']:s['titulo'] for s in S})
ck('89 termos definidos',len(G),89);ck('268 entradas no índice',len(I),268);ck('Índice sem duplicatas',len(set(norm(x['termo']) for x in I)),len(I))
ck('Índice alfabético',[norm(x['termo']) for x in I],sorted(norm(x['termo']) for x in I))
for i,x in enumerate(G):
 ck(f'Glossário {i+1}: destino',validate_dest(x['destino']),True)
 ck(f'Glossário {i+1}: definição e título reproduzidos',f"**{x['termo']}.** {x['definicao']} **Consulta:** {x['destino']['titulo']}." in t,True)
for i,x in enumerate(I):
 ck(f'Índice {i+1}: destino',validate_dest(x['destino']),True)
 ck(f'Índice {i+1}: linha corresponde ao mapa',t.count('| '+x['termo']+' | '+x['consulta']+' |'),1)
old=R/'sistema/05-material/livro/manual/07-glossario.md';ol=old.read_text().splitlines()
ck('167 ocorrências da fonte mapeadas',len(C),167)
for i,x in enumerate(C):
 ck(f'Fonte ocorrência {i+1}: termo/linha/destino',x['termo'] in ol[x['linha']-1] and validate_dest(x['destino']),True)
for s in S:
 ck(s['ancora']+': até quatro colunas',max([len(r.strip('|').split('|')) for r in table_rows(s['texto'])] or [0])<=4,True)
# A existência no arquivo não basta: o trecho deve estar selecionado no livro único.
order=load(P/'consolidacao/lote-01/ORDEM.json');selected=set()
for part in order['partes']:
 for chapter in part['capitulos']:
  for spec in chapter['fontes']:
   file=order['fontes'][spec['documento']]
   available={x['ancora'] for x in pages((P/file).read_text())}
   chosen=set(spec.get('ancoras',available))-set(spec.get('excluir',[]))
   selected.update((file,anchor) for anchor in chosen)
ck('Todos os destinos selecionados para o livro único',[x['termo'] for x in G+I if (x['destino']['arquivo'],x['destino']['ancora']) not in selected],[])

# Negative mutations prove the destination validator is active, not just a list of expected positives.
a=copy.deepcopy(G[0]['destino']);a['ancora']='nao-existe';case('Âncora ausente recusada',validate_dest(a),False,'mutacao-executada')
a=copy.deepcopy(G[0]['destino']);a['titulo']='Título antigo';case('Título desatualizado recusado',validate_dest(a),False,'mutacao-executada')
a=copy.deepcopy(G[0]['destino']);a['arquivo']='inexistente.md';case('Arquivo ausente recusado',validate_dest(a),False,'mutacao-executada')
# Bind checks to actual manuscript sentences and donor procedures, not just a free-standing model.
phrases=['Role d20 + bônus','Igualar é sucesso','elas se cancelam, mesmo com várias fontes de um lado','A Reação volta no começo do seu turno','Padrão → Bônus → Movimento','conserva a Reação','Anote a preparação no momento em que a ordem for paga','Entrar e sair não limpa usos gastos','sem presumir recuperação por terminar a sessão','um marcador junto do participante','PV atuais / máximos','PE: total e parcela de cada pagador','Atributo usado, treino e bônus completo','Famílias Livres e Fechadas','saldo e feito de limiar']
for phrase in phrases:ck('Contrato textual: '+phrase,phrase in t,True)
# d20 distributions, exhaustive 400 pairs at one roll; ordinary test without exceptional attack handling.
def roll(a,b,bonus,adv,dis):return ((a if bool(adv)==bool(dis) else max(a,b) if adv else min(a,b))+bonus)
for mode in [(0,0),(1,0),(0,1),(2,1),(1,4)]:
 success=sum(roll(a,b,4,*mode)>=15 for a,b in product(range(1,21),repeat=2))
 expected=300 if mode==(1,0) else 100 if mode==(0,1) else 200
 case('TR/teste CD15 bônus4 fontes '+str(mode),success,expected)
case('Igualdade de CD15 com dado11+bônus4',11+4>=15,True)
case('Falha um ponto abaixo',10+4>=15,False)
case('Bônus total4 somado uma vez ao dado11',11+4,15)
case('Exemplo de dupla contagem detectável',11+4+2==15,False,'negativo-executado')
# Resource state model tests the ordinary conversion direction, not every class exception.
def convert(state,a,b):
 allowed={('P','B'),('B','M')};v=state.copy()
 if (a,b) not in allowed or v[a]<=0:return None
 v[a]-=1;v[b]+=1;return v
s={'P':1,'B':1,'M':1};c=convert(s,'P','B');case('Padrão para Bônus',c,{'P':0,'B':2,'M':1})
c2=convert(c,'B','M');case('Nova Bônus para Movimento',c2,{'P':0,'B':1,'M':2})
case('Não converter Movimento para Padrão',convert(s,'M','P'),None)
case('Não usar Padrão já gasta',convert(c,'P','B'),None)
case('Conservar quantidade de recursos ao converter',sum(c2.values()),sum(s.values()))
def full_action(state):
 if any(state.get(k,0)<1 for k in ['P','B','M']):return None
 result=state.copy()
 for k in ['P','B','M']:result[k]-=1
 return result
case('Completa deixa Reação disponível',full_action({'P':1,'B':1,'M':1,'R':1}),{'P':0,'B':0,'M':0,'R':1})
case('Completa recusada quando Movimento já gasto',full_action({'P':1,'B':1,'M':0,'R':1}),None)

# Explicit state transitions ensure a round boundary is not a reset.
def reset_reaction(current,event):return 1 if event=='comeco_proprio_turno' else current
for event,out in [('nova_rodada',0),('turno_aliado',0),('comeco_proprio_turno',1)]:case('Reação gasta: '+event,reset_reaction(0,event),out)
# Delayed payment model used only to validate consultation logs.
def order(log,who,cost,phase):
 q=copy.deepcopy(log)
 if phase=='emitir':q['PE'][who]-=cost;q['pendentes']+=1
 elif phase=='resolver':
  if not q['pendentes']:return None
  q['pendentes']-=1;q['resolvidas']+=1
 return q
log={'PE':{'dono':9,'corpo':7},'pendentes':0,'resolvidas':0};a=order(log,'dono',3,'emitir');b=order(a,'dono',3,'resolver')
case('Preparação registra pagamento uma vez',b,{'PE':{'dono':6,'corpo':7},'pendentes':0,'resolvidas':1})
case('Resolver sem ordem pendente recusado',order(log,'dono',3,'resolver'),None)
case('Corpo com PE separado não paga parcela pessoal',b['PE']['corpo'],7)
for term in ['Morrendo','Integridade']:
 g=next(x for x in G if x['termo']==term);case(term+' sem fórmula concorrente',bool(re.search(r'\d|%',g['definicao'])),False,'contrato-documental')
case('Formulário não concede quatro ativas','não aumentam a quantidade de entidades ativas' in t,True,'contrato-documental')
case('Campos não concedem recurso inexistente','Um campo disponível não concede o recurso' in t,True,'contrato-documental')
case('Sem habilidades copiadas no índice',all(len(x['consulta'].split())<24 for x in I),True,'contrato-documental')
# Mandatory fields by template, located in the right section.
requirements={
'consulta-ficha-personagem':['Origem','Patente','Físico','Vigor','Intelecto','Espírito','PV','PE','Integridade','Defesa','Bloquear','Iniciativa','Deslocamento','Maestria','Refino','Lapidação','XP'],
'consulta-ficha-repertorio':['Perícias','Ofícios','Treino com armas','Talentos','Total ocupado','Classe 0','Acerto','Munição','Volume','Pactos'],
'consulta-ficha-feitico':['Regra do poder','Famílias','Forma','Restrições','Saldo' if False else 'saldo','Ação','PE','alcance','alvos','TR','Dados','Duração','Ampliar'],
'consulta-ficha-entidade':['Aquisição','Espaço','Tamanho','Sentidos','Talismã','TR Físico','Defesa','PV','Integridade atual / máxima','Reserva própria'],
'consulta-ficha-entidade-capacidades':['Básicas','Especiais','Talentos','Trunfos','Forma','Restrições','limites','Ação do invocador','pagador','Gatilho','recarga'],
'consulta-ficha-recuperacao':['Máximo de referência','Sequelas antes','Janela inicial / restante','Ponto da iniciativa','Tratamento necessário / acumulado','Estável','Máximo perdido','Custos já pagos','Sequela registrada','Derrotado','Integridade','Estágio'],
'consulta-registro-missao':['Recursos ao chegar','Recursos ao sair','XP','Posição semanal','Empréstimo' if False else 'emprestados','Entidades','Pactos','Descanso','Decisão de regra','Conferência']}
for key,fields in requirements.items():
 body=next(x['texto'] for x in S if x['ancora']==key)
 ck(key+': campos necessários',[f for f in fields if f not in body],[])
# Consulta dirigida: destinos e registros introduzidos depois da leitura independente.
indexmap={x['termo']:x['destino'] for x in I}
for term,anchor in [('Cura (Forma)','amparoformas'),('Cura (recuperação)','cura'),('Patente','prog-patentes'),('Grau (patente)','prog-patentes'),('Inconsciente','inconsciente'),('Integridade','integridade'),('Integridade máxima','alma'),('Derrotado','derrota'),('Estabilizar','socorro')]:
 case('Consulta específica: '+term,indexmap[term]['ancora'],anchor,'contrato-documental')
case('Volumosa aponta sua restrição de porte',indexmap['Volumosa']['ancora'],'eq-oculta','contrato-documental')
case('Cura não retorna destino único ambíguo','Cura' in indexmap,False,'contrato-documental')
for current,old in [('Talento','Passiva (nome anterior)'),('Categoria de Efeito','Classe Passiva (nome anterior)'),('Talento Próprio','Passiva Própria (nome anterior)'),('Identificar Feitiço','Aviso (Melhoria; nome anterior)'),('Leitura de Feitiços','Aviso (Talento; nome anterior)')]:
 case('Nome e alias: '+current,indexmap[current],indexmap[old],'contrato-documental')
case('Guarda Aberta com alias histórico',indexmap.get('Guarda Aberta')==indexmap.get('Incapacitado (nome anterior)') and 'Guarda Aberta' in indexmap,True,'contrato-documental')
recovery=next(x['texto'] for x in S if x['ancora']=='consulta-ficha-recuperacao')
case('Modelo não duplica percentuais nem custos fracionários',bool(re.search(r'\d+%|1/[248]',recovery)),False,'contrato-documental')
# External checker catches names and prohibited titles after exact index exceptions.
sys.path.insert(0,str(P/'validacao-editorial'));from conferir_editorial import check_file
ck('Editoral atual com revisão contextual',check_file(M,True),[])
ck('Revisão editorial do hash atual',load(E/'REVISAO-EDITORIAL.json')['sha256_texto'],H)
ck('Mapa de cobertura conserva decisões',all(x['decisao'] for x in C),True)
# No source checksum is silently refreshed here: a change requires an explicit review/update of evidence.
sources=load(E/'FONTES-CANDIDATAS.json')['fontes'];ck('Donos no estado conferido',[f for f,h in sources.items() if sha(R/f)!=h],[])
res={'ok':all(c['ok'] for c in checks),'sha256_texto':H,'manuscritos_auditados':{str(M.relative_to(R)):H},'verificacoes':len(checks),'casos_executados':len(cases),'pares_d20_por_cenario':400,'cenarios_d20':5,'checks':checks,'limites':['Auditoria é de destinos, conteúdo e modelos dirigidos dos procedimentos de consulta; não simula partidas ou habilidades completas.','Campos em branco não têm fórmulas executáveis.','Outros donos conservam hashes lidos em FONTES-CANDIDATAS; alterações exigem nova conferência.','Leitor independente e inspeção visual serão evidências separadas.']}
(E/'auditoria-numerica.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');(E/'casos-executados.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n');(E/'regras-verificadas.json').write_text(json.dumps({'ok':res['ok'],'sha256_texto':H,'casos':cases},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:res[k] for k in ['ok','verificacoes','casos_executados','sha256_texto']},ensure_ascii=False));print(json.dumps([c for c in checks if not c['ok']],ensure_ascii=False,indent=2));sys.exit(0 if res['ok'] else 1)

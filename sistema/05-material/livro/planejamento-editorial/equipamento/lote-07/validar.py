from pathlib import Path
import re,json,hashlib,itertools
B=Path(__file__).resolve().parent;R=B.parents[5]
MD=B/'FERRAMENTAS-E-OBJETOS.md';text=MD.read_text();source=(R/'sistema/03-mecanica/16-ferramenta-amaldicoada.md').read_text();manual=(R/'sistema/05-material/livro/manual/55-ferramenta-amaldicoada.md').read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def plain(t):return re.sub(r'[*`]', '',t).strip()
def table(t):
 rows=[[plain(x) for x in line.strip().strip('|').split('|')] for line in t.splitlines() if line.startswith('|')]
 return [r for r in rows if not all(re.match(r'^:?-+:?$',v) for v in r)][1:]
def section(t,title,end):return t.split(title,1)[1].split(end,1)[0]
grade_owner=table(section(source,'## 3. A escada','### 3.1'))
grade=table(section(text,'# Graus e aquisição','As Classes'))
wear_owner=table(section(source,'## 4. `Desgaste`','**Grau 4'))
wear=table(section(text,'# Desgaste','Ferramentas de grau 4'))
checks=[]
def ck(n,a,b):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
def getnum(t):m=re.search(r'\d+',t);return int(m[0]) if m else 0
def normgrade(t):return t.lower().replace(' ou ',' e ')
def decoded(rows):return [(normgrade(r[0]),getnum(r[1]),getnum(r[2])) for r in rows]
ck('Graus, Classes e requisitos confrontados por linha e coluna',decoded(grade),decoded(grade_owner))
ck('Missões confrontadas por grau',[(normgrade(r[0]),int(r[1])) for r in wear],[(normgrade(r[0]),int(r[1])) for r in wear_owner])
ck('Fonte atual declara requisitos próprios','declara os próprios gates de nível' in source,True)
ck('Fonte atual mantém dispensa de Refino','Não existe gate de refino' in source,True)
ck('Ausência de sintonização preservada','Não é preciso sintonizar, descansar nem pagar PE' in text and 'Não há ritual, não há descanso, não há PE' in source,True)
ck('Dois apoios na fonte e na candidata','O apoio tem teto de duas' in source and 'até dois apoios ao mesmo tempo' in text,True)
limits=table(section(text,'## Limites','> **Exemplo:'))
ck('Exemplos de teto: uma arma mais dois; duas armas mais dois',[int(r[1]) for r in limits],[1+2,2+2])
ck('Uma ferramenta, no máximo um Estigma','**um Estigma**' in text and 'mais UM `Estigma`' in source,True)
ck('Grau 4 fora de Desgaste','Ferramentas de grau 4 não recebem Desgaste' in text and '**Grau 4 não entra**' in source,True)
ck('Propriedades de arma mantidas salvo exceção','conserva o dano, as propriedades, o Volume e os requisitos' in text,True)
ck('Guardada não suprime energia','não apaga a energia do item' in text,True)
ck('Frequência própria preservada','Os limites do próprio Estigma continuam valendo' in text,True)
ck('Troca não renova contador','entregá-lo a outra pessoa também não os recupera' in text,True)
ck('Última missão completa','Ele continua disponível até o fim dessa missão' in text,True)
ck('Permanente conta quando beneficia','receber seu benefício conta como uso' in text,True)
ck('Destino esgotado comum ou quebra','perde definitivamente a propriedade amaldiçoada e fica como item comum, ou se quebra' in text,True)
ck('Fonte principal esgota para arma comum','quando elas acabam, ela é arma comum, e não volta' in source,True)
ck('Contradição original registrada','corrente que fere maldição e nada mais' in manual,True)
ck('Sem receita automática','Escolher uma arma do catálogo e um Estigma não basta para produzir' in text,True)
ck('Sem benefício automático por ingestão','não concede automaticamente poderes, uma nova Origem' in text,True)
ck('Sem generalização antiga de acúmulo','juntando o que o selo empurrou' in text,False)
ck('Sem catálogo de Origens duplicado',any(x in text for x in ['| Receptáculo','| Feto','| Reencarnado']),False)
# Gate: all levels and grades, normal vs exception. Compare against source-derived oracle.
gates={g:lv for g,cl,lv in decoded(grade)};owner_gates={g:lv for g,cl,lv in decoded(grade_owner)};gate_cases=[]
for level,(g,cl,lv),exception in itertools.product(range(1,31),decoded(grade),[False,True]):
 available=bool(cl and (level>=gates[g] or exception))
 expected=bool(cl and (level>=owner_gates[g] or exception))
 gate_cases.append({'nivel':level,'grau':g,'desgaste':exception,'estigma':available,'ok':available==expected})
ck('300 combinações de nível, grau e exceção',all(x['ok'] for x in gate_cases),True)
# Desgaste only measures mission depletion, not per-scene activations. 0/1/10 are valid uses within effects' own limits.
amounts={normgrade(r[0]):int(r[1]) for r in wear};sequence_cases=[]
for g,n in amounts.items():
 for uses in itertools.product([0,1,10],repeat=5):
  remaining=n;trace=[]
  for use in uses:
   open_this_mission=remaining>0
   marked=False
   permitted=0
   for _ in range(use):
    if open_this_mission:
     permitted+=1
     if not marked:remaining-=1;marked=True
   trace.append({'restantes':remaining,'usos_permitidos':permitted})
  expected=max(0,n-sum(u>0 for u in uses))
  sequence_cases.append({'grau':g,'usos_por_missao':uses,'trace':trace,'ok':remaining==expected and all(t['restantes']>=0 for t in trace)})
ck('729 sequências de missões: nenhuma/uma/várias ativações',all(x['ok'] for x in sequence_cases),True)
example=table(section(text,'| Missão |','Ao terminar a quarta')) # header stripped deliberately
# Section begins after first header delimiter; parse full table instead.
example=table(text[text.index('| Missão |'):].split('Ao terminar a quarta')[0])
start=amounts['1 e especial'];expected=[]
for u in [1,0,1,1]:start-=u;expected.append(start)
ck('Exemplo de quatro missões',[int(r[2]) for r in example],expected)
ck('Última missão com dez ativações válidas não termina na primeira',next(x for x in sequence_cases if x['grau']=='3' and tuple(x['usos_por_missao'])==(10,0,0,0,0))['trace'][0],{'restantes':0,'usos_permitidos':10})
# Negative controls: changes in source-column agreement must fail.
mutants=[]
for name,old,new in [('nível de Classe 2','| 2 | Classe 2 | 7 |','| 2 | Classe 2 | 8 |'),('Classe de grau 1','| 1 | Classe 3 | 13 |','| 1 | Classe 2 | 13 |')]:
 mutated=text.replace(old,new);actual=decoded(table(section(mutated,'# Graus e aquisição','As Classes')))
 mutants.append({'mutacao':name,'detectada':actual!=decoded(grade_owner)})
mw=table(section(text.replace('| 2 | 2 |','| 2 | 5 |'),'# Desgaste','Ferramentas de grau 4'))
mutants.append({'mutacao':'missões de grau 2','detectada':[(normgrade(r[0]),int(r[1])) for r in mw]!=[(normgrade(r[0]),int(r[1])) for r in wear_owner]})
ck('Três perturbações numéricas detectadas',all(x['detectada'] for x in mutants),True)
# Editorial guard tested on this domain and real manuscript.
import sys
sys.path.insert(0,str(B.parents[1]/'validacao-editorial'))
from conferir_editorial import check_file,configuration,scan
ck('Títulos, localização e vocabulário',check_file(MD,True),[])
reg,_,blocks=configuration()
ck('Controle negativo: título Como ler detectado',any(x['codigo']=='E001' for x in scan(text+'\n# Como ler ferramentas\n','ferramentas',reg,blocks)),True)
ck('Controle negativo: habilidade de classe fora do dono detectada',any(x['codigo']=='E002' for x in scan(text+'\n**Movimento Acrobático** permite atravessar criaturas.\n','ferramentas',reg,blocks)),True)
result={'ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'manuscritos_auditados':{str(MD.relative_to(R)):sha(MD)},'casos':checks,'combinacoes_nivel':len(gate_cases),'sequencias_desgaste':len(sequence_cases),'mutacoes':mutants,'limites':['Sem simulação de dano do catálogo ou playtest. Estados de contador verificam coerência, não equilíbrio de poder.']}
(B/'evidencias/auditoria-numerica.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(B/'evidencias/cenarios-numericos.json').write_text(json.dumps({'requisitos':gate_cases,'desgaste':sequence_cases},ensure_ascii=False,indent=2)+'\n')
(B/'evidencias/regras-verificadas.json').write_text(json.dumps({'ok':result['ok'],'sha256_texto':sha(MD),'casos':checks,'catalogo_estigmas_validado':False},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':result['ok'],'verificacoes':len(checks),'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if result['ok'] else 1)

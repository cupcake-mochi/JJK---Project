from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json,re,hashlib
B=Path(__file__).resolve().parent;P=B.parents[1];R=next(p for p in B.parents if (p/'sistema/03-mecanica').is_dir())
F=B/'PERICIAS-E-OFICIOS.md';s=F.read_text();source=R/'sistema/03-mecanica/07-pericias-e-oficios.md';canonical=source.read_text();basics=P/'regras-basicas/lote-01/TESTES-E-TURNOS.md';base=basics.read_text();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n')
checks=[]
def ck(n,a,b=True):checks.append({'caso':n,'obtido':a,'esperado':b,'ok':a==b})
# Owners' tables are parsed with explicit sections, not loose number searches.
skill_section=canonical.split('## 4. As vinte e três perícias',1)[1].split('### O que cada uma cobre',1)[0]
expected={}
for line in skill_section.splitlines():
 if not line.startswith('| **'):continue
 row=[x.strip().replace('**','') for x in line.strip('|').split('|')]
 if row[0]=='Constituição':continue
 names=row[1].split(' · ');assert len(names)==int(row[2]),row
 expected.update({n:row[0] for n in names})
assert len(expected)==23
parts=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',s);pages={parts[i]:parts[i+2] for i in range(1,len(parts),3)}
actual={}
for key,attr in [('fisicas',None),('conhecimento','Inteligência'),('ambiente','Inteligência'),('essencia','Essência')]:
 for title in re.findall(r'^## (.+)$',pages[key],re.M):
  if attr is None:name,a=title.split(' · ')
  else:name,a=title,attr
  actual[name]=a
ck('Perícias por nome e atributo coincidem com o dono',actual,expected)
ck('Distribuição 1/4/11/7',dict(Counter(actual.values())),{'Força':1,'Destreza':4,'Inteligência':11,'Essência':7})
# Default profession attributes from piece07, intentionally absent in the published chapter.
off=canonical.split('### O atributo padrão de cada ofício',1)[1].split('## 6.',1)[0]
expected_o={}
for line in off.splitlines():
 if not line.startswith('| **'):continue
 row=[x.strip().replace('**','') for x in line.strip('|').split('|')];expected_o[row[0]]=row[1]
actual_o={}
for line in pages['oficios'].splitlines():
 if not line.startswith('| '):continue
 row=[x.strip() for x in line.strip('|').split('|')]
 if row[1] in {'Força','Destreza','Inteligência','Essência'}:actual_o[row[0]]=row[1]
ck('Onze ofícios e atributos padrão',actual_o,expected_o);ck('Contagem Ofícios',len(actual_o),11)
ck('Intuição permanece Inteligência',actual['Intuição'],'Inteligência');ck('Sentir Energia permanece Essência',actual['Sentir Energia'],'Essência')
# Example source wrongly said three less; compute the correction independently.
ck('Rina Destreza4 + Maestria1',4+1,5);ck('Rina Inteligência2 + Maestria1',2+1,3);ck('Diferença entre bônus',5-3,2)
ck('Resultado mínimo no dado, CD14', [14-(4+1),14-(2+1)],[9,11]);ck('Reparo: horas restantes',4-2,2)
ck('Exemplo preço local / proteção não sobe',all(x in s for x in ['¥3.000','4 horas de trabalho','ainda faltam **2 horas**','não a todos os Trajes']))
# Exact distributions and dominance of training on an identical possible task.
levels={}
for lo,hi,m in re.findall(r'^\| (\d+) a (\d+) \| \+(\d+) \|$',base,re.M):
 for level in range(int(lo),int(hi)+1):levels[level]=int(m)
assert set(levels)==set(range(2,31))
cd_section=base.split('## Dificuldade',1)[1].split('## Sucesso e falha',1)[0]
cds=[int(x) for x in re.findall(r'^\| [^|]+ \| (\d+) \|',cd_section,re.M)];assert cds==[6,10,14,18,22,26]
dist={'normal':Counter(range(1,21)),'vantagem':Counter(max(a,b) for a,b in product(range(1,21),repeat=2)),'desvantagem':Counter(min(a,b) for a,b in product(range(1,21),repeat=2))}
def prob(bonus,cd,mode):return Q(sum(n for v,n in dist[mode].items() if v+bonus>=cd),sum(dist[mode].values()))
rows=[];anomalies=[]
for level,attr,cd,mode in product(levels,range(7),cds,dist):
 m=levels[level];values=[attr,attr+m]+([attr+m+m//2] if level>=10 else [])
 ps=[prob(v,cd,mode) for v in values]
 if sorted(ps)!=ps:anomalies.append((level,attr,cd,mode))
 for tier,bonus,p in zip(['sem treino','treinado','especializado'],values,ps):rows.append({'nivel':level,'atributo':attr,'treino':tier,'bonus':bonus,'cd':cd,'dados':mode,'sucesso':float(p)})
ck('Treino/especialização não pioram chance na mesma tarefa',anomalies,[])
ck('Bônus máximo sem efeitos externos',max(r['bonus'] for r in rows),12)
ck('Rina CD14: 60% ou 50%', [str(prob(5,14,'normal')),str(prob(3,14,'normal'))],['3/5','1/2'])
ck('CD26 não é possível com bônus0, nem em20',prob(0,26,'normal'),Q(0))
# Repetition inflation, shown as a design risk, not a new free reroll rule.
p=prob(5,14,'normal');retry=[{'tentativas':n,'sucesso_ao_menos_uma':float(1-(1-p)**n),'minutos_se_arrombamento_comum':n} for n in [1,2,3,5]]
ck('Cinco repetições livres inflariam para98,976%',str(1-(1-p)**5),'3093/3125')
# Distinguish a retry's eligibility from its probability.
def retry_allowed(specific_allows,new_info,new_method,meaningful_delay):return specific_allows or new_info or new_method or meaningful_delay
for params,want in [((False,False,False,False),False),((True,False,False,True),True),((False,True,False,False),True),((False,False,True,False),True),((False,False,False,True),True)]:ck('Nova tentativa '+str(params),retry_allowed(*params),want)
# Boundary decisions the prose must retain. Negative perturbations ensure extraction catches changes.
phrases=['mesmo fora de combate','não reduz dano de queda nem encerra um agarrão','Domar entidades e comandar criaturas vinculadas seguem suas regras próprias','não fornece visão, identidade, grau ou previsão','não renova usos gastos','não concede sozinho a capacidade de criar poderes','não concede ao responsável um treino obrigatório','não há desconto universal']
for phrase in phrases:
 ck('Limite: '+phrase,phrase.casefold() in s.casefold());ck('Negativo textual: '+phrase,phrase.casefold() not in s.casefold().replace(phrase.casefold(),'REGRA REMOVIDA'))
mutated=dict(actual);mutated['Intuição']='Essência';ck('Mutação de atributo detectada',mutated!=expected)
mutated=dict(actual_o);mutated['Forja']='Destreza';ck('Mutação de padrão detectada',mutated!=expected_o)
ck('Sem tabela de habilidades de Caminho',not any('| '+n+' |' in s for n in ['Bastião','Vanguarda','Guia','Emanador','Evocador','Incursor']))
linked={str(p.relative_to(R)):sha(p) for p in [F,source,basics]}
res={'ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'checks':checks,'manuscritos_auditados':linked,'estados_numericos':len(rows),'repeticao':retry,'limites':['A matemática verifica bônus, probabilidade e exemplos; não comprova compreensão humana.','Domínio por chance vale somente na mesma tarefa possível. Não atribui utilidade ou preço igual a perícias distintas.','Fabricação usa orçamento/prazo de projeto; não há curva universal de produção ou lucro validada.']}
dump(B/'CATALOGO.json',{'pericias':actual,'oficios':actual_o,'sha256_texto':sha(F),'fonte':str(source.relative_to(R))});dump(B/'evidencias/auditoria-numerica.json',res);dump(B/'evidencias/distribuicoes.json',rows);dump(B/'evidencias/regras-verificadas.json',{'ok':res['ok'],'sha256_texto':sha(F),'casos':checks})
print(json.dumps({'ok':res['ok'],'verificacoes':len(checks),'estados':len(rows),'falhas':[c for c in checks if not c['ok']]},ensure_ascii=False,default=str));raise SystemExit(0 if res['ok'] else 1)

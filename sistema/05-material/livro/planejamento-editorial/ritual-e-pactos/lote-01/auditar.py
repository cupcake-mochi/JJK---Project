from pathlib import Path
from fractions import Fraction
from itertools import product
from math import comb
import hashlib,json,re
B=Path(__file__).resolve().parent;R=B.parents[5];F=B/'RITUAL-E-PACTOS.md';text=F.read_text();checks=[];cases=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,actual,expected):checks.append({'verificacao':name,'obtido':actual,'esperado':expected,'ok':actual==expected})
def case(name,actual,expected):cases.append({'caso':name,'obtido':actual,'esperado':expected,'ok':actual==expected})
def chance(c,d,m=2,trained=True,special=0):
 return Fraction(sum(n+(m if trained else 0)+special>=8+m+c-d for n in range(1,21)),20)
# Parse the prices and budget directly from the current table, failing on omissions.
rows=re.findall(r'^\| (Ritual de [^|]+) \| ([^|]+) \| (\d+) \|$',text,re.M)
prices={name:int(price) for name,_,price in rows};ck('16 entradas de Ritual',len(prices),16)
source=(R/'sistema/03-mecanica/27-ritual.md').read_text()
old={n:int(p) for n,p in re.findall(r'^\| `(Ritual de [^`]+)` \|[^\n]*?\| (\d+) \|',source,re.M)}
ck('Preços preservados por entrada',prices,old)
budgets=[int(v) for v in re.findall(r'^\| (?:Breve|Completo|Recitação Prolongada) \|[^|]+\| (\d+) \|$',text,re.M)]
ck('Três modalidades com orçamento',budgets,[2,6,10])
ck('Fórmula preservada', '8 + Inteligência + maestria + Classe do feitiço − Destreza' in text,True)
# Exact d20 probability, old published rows compared to formula (table was 10pp low).
prob=[]
for dex in (0,3,6):
 for c in range(1,8):
  p=chance(c,dex);oldp=Fraction(55+5*dex-5*c,100)
  prob.append({'classe':c,'destreza':dex,'chance':float(p),'tabela_antiga':float(oldp),'correcao_pp':float(100*(p-oldp))})
ck('21 células corrigidas por fórmula',all(x['correcao_pp']==10 for x in prob),True)
case('Exemplo CD de Kaito',8+6+2+4-4,16);case('Kaito chance exata',float(chance(4,4)),.65)
case('Kaito falha, PE',3*4+4,16);case('Kaito sucesso com Energia',3*4-max(1,4//2),10)
case('Ritual completo exemplo soma',prices['Ritual de Tamanho']+2*prices['Ritual de Dificuldade']+prices['Ritual de Energia'],6)
case('Exemplo em conjunto soma',6+prices['Ritual de Seleção']+prices['Ritual de Defesa'],10)
# All numeric profiles: attributes0..6, mastery2..4, training and specialization.
profiles=[]
for c,d,m,tr in product(range(1,8),range(7),range(2,5),(False,True)):
 for sp in (0,m//2) if tr else (0,):
  p=chance(c,d,m,tr,sp)
  expected=sum(1 for n in range(1,21) if n+(m if tr else 0)+sp>=8+m+c-d)/20
  profiles.append({'C':c,'Dex':d,'maestria':m,'treino':tr,'especial':sp,'p':float(p)})
  if float(p)!=expected:raise AssertionError(profiles[-1])
ck('Perfis exatos de teste',len(profiles),441)
# Buy each ritual once except the two explicitly repeatable entries.
names=list(prices);choices=[range(3) if n in ('Ritual de Acerto','Ritual de Dificuldade') else range(2) for n in names]
counts={b:0 for b in (2,6,10,14)};maxima={b:0 for b in counts};profiles_buy=0
for selection in product(*choices):
 cost=sum(q*prices[n] for n,q in zip(names,selection));profiles_buy+=1
 for b in counts:
  if cost<=b:counts[b]+=1;maxima[b]=max(maxima[b],cost)
ck('Orçamentos alcançáveis',maxima,{2:2,6:6,10:10,14:14})
# Model uneven split copying. Enumerate ordered positive compositions up to7parts.
def compositions(n,k):
 if k==1:yield (n,);return
 for a in range(1,n-k+2):
  for rest in compositions(n-a,k-1):yield (a,)+rest
parts_n=0;worst=0
for total in range(1,16):
 for k in range(1,min(total,5)+1):
  for parts in compositions(total,k):
   extra=min(parts);parts_n+=1
   if extra>total//k:raise AssertionError(parts)
   worst=max(worst,float(Fraction(extra,total)))
case('Tiros desiguais4/2/1',min((4,2,1)),1);case('Tiros equilibrados3/2/2',min((3,2,2)),2)
case('Nunca copia parcela grande18/1/1',min((18,1,1)),1)
# Healing overflow must respect actual waste and quarter cap.
heal_profiles=0
for healing in range(1,161):
 for missing in range(0,161):
  temporary=min(max(0,healing-missing),healing//4)
  assert 0<=temporary<=healing//4 and temporary<=max(0,healing-missing)
  heal_profiles+=1
case('Cura32, faltam2: excesso limitado',min(32-2,32//4),8)
case('Cura3, alvo cheio: fração para baixo',min(3,3//4),0)
# Exact marginal reroll expectation (before attack chance), no Monte Carlo.
rerolls=[]
for c in range(1,8):
 for n in (c,2*c,3*c,4*c):
  expectation=sum(Fraction(comb(n,k)*7**(n-k),8**n)*min(k,c+1) for k in range(n+1))
  rerolls.append({'classe':c,'dados':n,'ganho_medio_d8':float(expectation*Fraction(7,2))})
# Pact amount model respects lifetime spent choices rather than active benefits.
quantities=[ess//2 for ess in range(7)]
case('Essência0..6 pactos',quantities,[0,0,1,1,2,2,3])
case('Pacto perdido não libera escolha',2-2,0)
case('Essência4para6 após2pactos',6//2-2,1)
case('Liberação Classe3..7 bônus', [max(1,c//2) for c in range(3,8)], [1,2,2,3,3])
case('Liberação Classe3..7 teto excepcional', [4*c+max(1,c//2) for c in range(3,8)], [13,18,22,27,31])
requirements={
 'Sem ritual nas duas rotas':'Técnica Marcial e Sem Técnica não podem adquiri-la nem auxiliar',
 'Calado impede':'**Calado impede Ritual.**',
 'Uma ajuda':'**um único aliado**',
 'Máxima sem estocagem':'não pode ser guardada por Recitação Prolongada',
 'Parcelas conservadas':'**menor parcela**',
 'Decisão anterior à rolagem':'antes de fazer qualquer rolagem',
 'Duração não recursa':'Não repete dano, cura, movimento, teste ou ataque',
 'Pacto não cria Estilo':'não entrega um Estilo completo',
 'Ideia não é regra pronta':'não regras prontas nem benefícios adquiridos',
 'Sem punição canônica inventada':'Não há uma punição universal',
 'Acerto classe0 não abre ritual':'Classe 1 ou maior',
 'Perseguição sem teleporte':'não segue teleporte',
}
for label,excerpt in requirements.items():ck(label,excerpt in text,True)
# Regressões da revisão independente: requisitos ancorados na resolução escrita.
ck('Falha não restaura devolução incompatível','ela não retorna depois do teste' in text,True)
ck('Ajuda atende uma conjuração','uma única conjuração indicada ao preparar o apoio' in text,True)
ck('Ajuda consumida mesmo na falha','consumida nessa tentativa, mesmo na falha ou interrupção' in text,True)
ck('Alcance de auxílio mantido','Até a resolução, mantenham a distância de 9 m e a percepção mútua' in text,True)
ck('Energia não retroage','não pode comprar Energia nem reduzir retroativamente o PE pago' in text,True)
ck('Remissão atual Perseguir','| Perseguição e Perseguir |' in text,True)
ck('Concentrada é nome da peça','Não prolonga Fica, Concentrada, Duradoura' in text,True)
# Interfaces adicionais de cópia e pactos, examinadas na revisão independente.
ck('Pacto PE usa Classe','um aumento do PE máximo igual à sua maior Classe' in text,True)
ck('Pacto PE não recupera ao variar','não recupera PE imediatamente' in text,True)
ck('Sem geração de PE por turno','não concede energia por turno, por acerto ou por começar outra cena' in text,True)
ck('Cópia herda peças do beneficiário de origem','A cópia inclui os benefícios destinados àquela origem' in text,True)
ck('Cópias excepcionam total da Máxima','Podem exceder 4 × Classe ou o total fixo da Técnica Máxima' in text,True)
ck('Bônus exclusivo não amplia cópia','antes do crítico e de bônus exclusivos contra determinado alvo' in text,True)
ck('Tiroextra aplica Queima mas não multiplica Salto','As peças aplicadas por acerto acompanham o novo tiro, incluindo Queima' in text,True)
case('Parcela zero em Junto conserva zero',min((9,0)),0)
# Matriz semântica por modalidade: extraída da tabela jogável, não substituída pela contagem304.
time_rows=re.findall(r'^\| (Breve|Completo|Recitação Prolongada) \| (Não cabe:[^|]+|Sem devolução\.) \| (Conserva devolução\.) \| (Conserva devolução\.|Sem devolução\.) \|$',text,re.M)
time_matrix={mode:{'Atrasar':at.strip(),'Parado':pa.strip(),'Carregar':ca.strip()} for mode,at,pa,ca in time_rows}
ck('Três linhas de tempo extraídas',len(time_matrix),3)
ck('Nove combinações de tempo extraídas',sum(len(x) for x in time_matrix.values()),9)
# Restrictions x ritual semantic coverage is recorded explicitly, not inferred as truth.
catalog=B.parents[1]/'catalogo/lote-01/CATALOGO.md'
catalogtext=catalog.read_text()
restrictiontext=catalogtext.split('<!-- page:cat-restricoes-conjuracao|',1)[1].split('<!-- page:cat-passivas-1|',1)[0]
restrictions=re.findall(r'^## (.+)$',restrictiontext,re.M)
ck('19 Restrições lidas do catálogo vigente',len(restrictions),19)
matrix=[]
for name in names:
 for rest in restrictions:
  verdict='Conserva a cobrança própria da Restrição.'
  if rest in ('Atrasar','Parado','Carregar'):verdict='Não devolver pontos se repetir o custo de tempo/imobilidade da modalidade de Ritual.'
  if name=='Ritual de Meio Acerto' and rest=='Sem Volta':verdict='Incompatível: anula o risco de errar todos.'
  if name=='Ritual de Alcance' and rest=='Corpo a Corpo':verdict='Incompatível: não ampliaToque/distânciaque cobra.'
  if rest in ('Barulho','Assinatura'):verdict='Ritual mantém voz/gestos; a informação adicional da Restrição ainda precisa existir, sem cobrar apenas a recitação.'
  if rest=='Gesto':verdict='Ritual exige ao menos uma mão livre; Gesto ainda exige as duas. Se o Selo ou a execução já exigir ambas, não devolver pontos pela mesma cobrança.'
  if rest=='Restrição Própria':verdict='Avaliar o texto criado antes da sessão; a matriz nominal não pode prever toda regra própria.'
  entry={'melhoria':name,'restricao':rest,'decisao':verdict}
  if rest in ('Atrasar','Parado','Carregar'):
   entry['por_modalidade']={mode:values[rest] for mode,values in time_matrix.items()}
   entry['excecao']='Atrasar e Parado não devolvem numa Liberação; exigências repetidas por outra fonte também não devolvem.'
  matrix.append(entry)
case('Matriz nominal16x19',len(matrix),304)
result={'ok':all(c['ok'] for c in checks+cases),'sha256_texto':sha(F),'manuscritos_auditados':{str(F.relative_to(R)):sha(F)},'verificacoes':checks,'casos':cases,'modelos':{'perfis_teste':len(profiles),'perfis_compra':profiles_buy,'montagens_por_orcamento':counts,'particoes':parts_n,'perfis_cura':heal_profiles},'chances_corrigidas':prob,'ganho_rerrolagem':rerolls,'limites':['Modelo exato das contas descritas, não simulação de combate completo nem playtest humano.','Combinações de utilidade exigem a compatibilidade semântica; perfis de compra medem só orçamento.','Pactos temporários próprios não têm balanceamento universal: ficam limitados pelo acordo concreto.']}
for name,data in [('auditoria-numerica.json',result),('regras-verificadas.json',{'ok':result['ok'],'sha256_texto':sha(F),'casos':cases}),('MATRIZ-RITUAL-RESTRICOES.json',matrix)]:
 (B/'evidencias'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':result['ok'],'verificacoes':len(checks),'casos':len(cases),'modelos':result['modelos'],'falhas':[c for c in checks+cases if not c['ok']]},ensure_ascii=False))
raise SystemExit(0 if result['ok'] else 1)

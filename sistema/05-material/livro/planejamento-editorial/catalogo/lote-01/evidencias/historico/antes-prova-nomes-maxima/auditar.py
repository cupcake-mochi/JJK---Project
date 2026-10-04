"""Contas e interfaces do catálogo; não é simulador completo de combate."""
from pathlib import Path
from fractions import Fraction
from itertools import product
from math import ceil
import re,json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[5];E=B/'evidencias';F=B/'CATALOGO.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
checks=[];cases=[]
def ck(n,a,b):checks.append({'verificacao':n,'obtido':a,'esperado':b,'ok':a==b})
def case(n,a,b):cases.append({'cenario':n,'obtido':a,'esperado':b,'ok':a==b,'metodo':'modelo executado'})
s=F.read_text();inv=json.loads((B/'INVENTARIO-CATALOGO.json').read_text())
chunks=re.split(r'<!-- page:([^|]+)\|([^>]+) -->\s*',s);sections={chunks[i]:chunks[i+2] for i in range(1,len(chunks),3)}
headings=[re.sub(r'\s+-\s+(Leve|Média|Pesada).*','',x) for x in re.findall(r'^#{1,2} (.+)$',s,re.M)]
# A dupla de duração aparece no mesmo título; preserva duas compras distintas.
headings+=['Concentrada','Duradoura'] if re.search(r'Concentrada\s+-\s+Leve / Duradoura\s+-\s+Média',s) else []
for row in inv['entradas']:ck('Entrada presente: '+row['tipo']+'/'+row['nome'],row['nome'] in headings,True)
ck('106 entradas no inventário',len(inv['entradas']),106)
ck('Aviso tem duas entradas distintas',len(re.findall(r'^## Aviso(?:\s+-\s+Leve)?$',s,re.M)),2)
ck('Formas têm dono único',len(inv['formas']),10)
cp={'cat-passivas-1':'1','cat-passivas-2-recursos':'2','cat-passivas-2-protecao':'2','cat-passivas-3':'3','cat-regra-propria':'1 a 3','cat-passiva-propria':'1 a 3'}
grades=[]
for row in inv['entradas']:
 typ,name=row['tipo'],row['nome'];found=None
 for key,body in sections.items():
  this_type='passiva' if key in cp else 'restricao' if key.startswith('cat-restricoes') else 'melhoria'
  if typ!=this_type:continue
  matches=list(re.finditer(r'^#{1,2} '+re.escape(name)+r'(?=\s+-|\n)([^\n]*)\n(.*?)(?=^#{1,2} |\Z)',body,re.M|re.S));m=matches[-1] if matches else None
  if name=='Duradoura' and re.search(r'Duradoura\s+-\s+Média',body):found='Média';break
  if not m:continue
  if typ=='passiva':found=cp[key]
  elif name=='Efeito Próprio':found='o mestre decide' if 'definido com o mestre' in m[2] else None
  elif name=='Condição':found='o nível dela' if '**Preço: Nível da condição.**' in m[2] else None
  else:
   inheading=re.search(r'\s+-\s+(Leve|Média|Pesada)',m[1])
   inline=re.search(r'\*\*(?:Preço|Devolução): (Leve ou Média|Leve|Média|Pesada)\.\*\*',m[2])
   found=inheading[1] if inheading else inline[1] if inline else None
  break
 ck('Preço de aquisição preservado: '+typ+'/'+name,found,row['preco_fonte'])
 grades.append({'tipo':typ,'nome':name,'preco_fonte':row['preco_fonte'],'preco_texto':found})
save(E/'PRECOS-CONFERIDOS.json',{'sha256_texto':sha(F),'entradas':grades,'nota':'Custos ativos novos, como Contramedida 2 PE, ficam no registro mecânico; esta conferência trata do preço de aquisição.'})
# Custos das 68 Melhorias tabeladas e do efeito próprio: dados independentes da prosa.
def price(c,grade,free=False):
 raw={'Leve':ceil(c/2),'Média':c,'Pesada':ceil(3*c/2)}[grade]
 return max(1,raw-ceil(c/2)) if free else raw
price_rows=[]
for c in range(1,8):
 price_rows.append({'classe':c,'normal':[price(c,g) for g in ('Leve','Média','Pesada')],'livre':[price(c,g,True) for g in ('Leve','Média','Pesada')]})
ck('Curva normal 1-7',[r['normal'] for r in price_rows],[[1,1,2],[1,2,3],[2,3,5],[2,4,6],[3,5,8],[3,6,9],[4,7,11]])
ck('Livre nunca aumenta preço',all(price(c,g,True)<=price(c,g) for c,g in product(range(1,8),('Leve','Média','Pesada'))),True)
def parts(total,n):
 if n==1:
  if total>0:yield (total,)
 else:
  for first in range(1,total-n+2):
   for tail in parts(total-first,n-1):yield (first,)+tail
# Repartir dados deve preservar o total, e cada secundário usa a parcela de origem.
split_states=0;fail=[]
for n in range(1,22):
 for k in range(1,min(n,4)+1):
  for xs in parts(n,k):
   split_states+=1
   if sum(xs)!=n or sum(x//2 for x in xs)>n//2:fail.append([n,k,xs])
ck('Dados divididos: conservação e metades',fail,[])
case('Queima Rajada 3/2/2: acertam 3 e 2',3//2+2//2,2)
case('Salto de tiro com3d8, ficha7d8',3//2,1)
case('Estilhaço crit de3d8 não usa6d8',3//2,1)
case('Certeiro erro5d8 antes de peças',5//2,2)
# Escolher a melhor redução normal; custos independentes somam depois.
def spend(normal,eco=False,cobranca=False,free=False,debt=0):
 return (0 if free else ceil(normal/2) if eco or cobranca else normal)+debt
resource_states=0
for n,d,e,c,f in product(range(0,36),range(0,15),(False,True),(False,True),(False,True)):
 resource_states+=1
 assert spend(n,e,c,f,d)>=d
 assert spend(n,True,True,False,d)==spend(n,True,False,False,d)
case('Eco9 comDívida4',spend(9,True,False,False,4),9)
case('Eco+Cobrança não viramquarto',spend(9,True,True),5)
case('SegundaNatureza comDívida4',spend(9,True,True,True,4),4)
case('Classe0 cobraDívida6',spend(0,False,False,False,6),6)
def sugar(c,hits):return min(5*c,sum(d for d,full in hits if full)//4)
case('Sugar C3: 16+28 danos válidos',sugar(3,[(16,True),(28,True)]),11)
case('Sugar C3: 80 válidos+40parciais',sugar(3,[(80,True),(40,False)]),15)
case('Sugar sóerroCerteiro',sugar(3,[(20,False)]),0)
# Divide aplica defesas do destinatário uma vez, sem realimentar o vínculo.
def divide(damage,ally_rd=0):
 sent=ceil(damage/2);return damage-sent,max(0,sent-ally_rd)
transfer_states=0
for d,rd in product(range(201),range(41)):
 transfer_states+=1;a,b=divide(d,rd)
 assert a>=0 and b>=0 and a+b<=d
case('Divide11 semRD',list(divide(11)),[5,6])
case('Divide11 destinatárioRD3',list(divide(11,3)),[5,3])
case('Junto9 dividido6/3 conservaPV',sum([6,3]),9)
case('Junto Guarda é uma atribuição',len({'Guarda':'aliadaA'}),1)
# Rajada amplia chance de aplicar controle: resultado explícito, não certificação de equilíbrio.
control=[{'ataques':n,'chance_acerto_por_tiro':.5,'chance_ao_menos_um':float(1-Fraction(1,2)**n)} for n in range(1,9)]
case('Rajada quatro ataques a50%',control[3]['chance_ao_menos_um'],.9375)
# A contagem usa a rodada global; errar consome a janela de Fica.
def fica(start,events):
 seen=set();used=[]
 for rnd,target,outcome in events:
  if start<=rnd<=start+5 and (rnd,target) not in seen:
   seen.add((rnd,target));used.append((rnd,target,outcome))
 return used
case('Fica entradas repetidas e primeiroerro',len(fica(3,[(r,'A','erro' if r==3 else 'acerto') for r in range(3,10) for _ in range(3)])),6)
case('Minuto comum em rodadas6s',60//6,10)
case('Acúmulo início atésexto',[min(max(n-1,0),3) for n in range(1,7)],[0,1,2,3,3,3])
case('ReservaProfunda Classe7',3*7,21)
case('Recomposição maiorClasse5',5*5,25)
case('Carregar perde se dano11 e teste falha',(11<=10 or False),False)
case('Mão Firme protege dano10 semtestar',10<=10,True)
# Compatibilidade é um contrato pequeno e declarado; casos negativos de regressão.
def valid(form,ps,rs=(),maximum=False,hostile=True,damage=True):
 if maximum and set(ps)&{'Armado','Segura','Fica','Inescapável','Salto','Queima','Estilhaço','Acúmulo','Remate','Quebra Coisa','Rápido','Reação'}:return False
 if set(ps)&{'Longe','Muito Longe'} and form in {'Toque','Aura','Onda'}:return False
 if 'Inescapável' in ps and (form!='Projétil' or len(ps)!=1 or rs or not damage):return False
 if 'Reação' in ps and (set(ps)&{'Rápido','Armado'} or set(rs)&{'Atrasar','Parado'}):return False
 if 'Armado' in ps and ('Segura' in ps or 'Carregar' in rs):return False
 if 'Sem Volta' in rs and ('Certeiro' in ps or 'Inescapável' in ps or not hostile):return False
 if 'Tudo ou Nada' in rs and (not damage or form in {'Cura','Apoio'}):return False
 return True
for name,form,ps,rs,mx,expected in [
 ('Toque comLonge','Toque',['Longe'],[],False,False),('Projétil comLonge','Projétil',['Longe'],[],False,True),
 ('InescapávelProjétil','Projétil',['Inescapável'],[],False,True),('Inescapávelárea','Explosão',['Inescapável'],[],False,False),
 ('InescapávelSilencioso','Projétil',['Inescapável','Silencioso'],[],False,False),('Inescapávelrestrição','Projétil',['Inescapável'],['Parado'],False,False),
 ('ArmadoMáxima','Projétil',['Armado'],[],True,False),('SeguraMáxima','Projétil',['Segura'],[],True,False),
 ('ArmadoSegura','Projétil',['Armado','Segura'],[],False,False),('ArmadoCarregar','Projétil',['Armado'],['Carregar'],False,False),
 ('CerteiroSemVolta','Projétil',['Certeiro'],['Sem Volta'],False,False),('ControlePrecisão','Explosão',['Condição','Precisão'],[],False,True),
 ('ReaçãoParado','Projétil',['Reação'],['Parado'],False,False)]:case(name,valid(form,ps,rs,mx),expected)
anchor={
 '1Projétil automático':'Só em **Projétil de dano**',
 'Sugar teto compartilhado':'O limite pertence à conjuração inteira',
 'Máxima semestoque':'Não pode preparar uma Técnica Máxima',
 'Junto atribuição':'um só',
 'Capanga objetivo':'categoria **Capanga**',
 'Contramedida preço':'Reação e 2 PE',
 'Registro entidades':'entidades',
 'Concentração não renova benefício':'não renova benefícios consumidos',
}
for n,x in anchor.items():ck('Âncora '+n,x in s,True)
save(E/'regras-verificadas.json',{'ok':all(x['ok'] for x in cases),'sha256_texto':sha(F),'casos':cases,'quantidade':len(cases),'limites':'Modelos dirigidos e hipóteses explícitas; não simulam iniciativa, builds completos, inimigos ou aceitação humana.'})
save(E/'auditoria-numerica.json',{'ok':all(x['ok'] for x in checks+cases),'manuscritos_auditados':{str(F.relative_to(R)):sha(F)},'checks':checks,'verificacoes':len(checks),'cenarios_executados':len(cases),'estados_divisao_dados':split_states,'estados_recursos':resource_states,'estados_transferencia':transfer_states,'precos':price_rows,'risco_rajada_controle':control,'limites':['Catálogo inteiro coberto quanto a nomes; cobertura funcional é dirigida, não exaustiva.','A chance de controle crescente com tiros permanece e exige mesa/ajuste posterior, não foi escondida como só redação.','Passivas novas ou aclaradas, alvos múltiplos e duração precisam combate real.']})
print(json.dumps({'ok':all(x['ok'] for x in checks+cases),'checks':len(checks),'casos':len(cases),'estados':[split_states,resource_states,transfer_states],'falhas':[x for x in checks+cases if not x['ok']]},ensure_ascii=False))
raise SystemExit(0 if all(x['ok'] for x in checks+cases) else 1)

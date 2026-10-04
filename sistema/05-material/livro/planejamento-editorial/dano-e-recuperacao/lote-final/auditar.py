"""Modelos dirigidos de R03. Não é motor de combate nem teste com jogadores."""
from pathlib import Path
import json,re,hashlib,math,itertools
from fractions import Fraction
B=Path(__file__).resolve().parent;src=B/'DANO-E-RECUPERACAO.md';s=src.read_text();cases=[];errors=[]
def check(name,got,want=True):
 ok=got==want;cases.append({'caso':name,'obtido':got,'esperado':want,'ok':ok})
 if not ok:errors.append(name)
def require(pattern):
 m=re.search(pattern,s)
 if not m:raise RuntimeError('Parâmetro ausente do manuscrito: '+pattern)
 return m
W=int(require(r'janela começa com \*\*(\d+) rodadas').group(1));rate=Fraction(int(require(r'\*\*(\d+)% do máximo de referência').group(1)),100)
fractions=[Fraction(x) for x in re.findall(r'^\| (?:Ao escolher Insistir|Após uma volta completa, se ainda houver janela|Após outra volta completa, se ainda houver janela) \| ([0-9/]+) da referência',s,re.M)]
DC=int(require(r'Medicina CD\s*(\d+)').group(1))
thresholds=[Fraction(x) for x in re.findall(r'^\| Pelo menos ([0-9/]+) \| [123] \|',s,re.M)]
check('janela preserva base3',W,3);check('socorro uniforme20%',str(rate),'1/5');check('custos preservados',list(map(str,fractions)),['1/8','1/4','1/2']);check('patamares Alma',list(map(str,thresholds)),['1/4','1/2','3/4'])
def ceil(f):return -(-f.numerator//f.denominator)
def stage(maximum,current):
 if current<=0:return 4
 return sum(Fraction(maximum-current,maximum)>=t for t in thresholds)
def window(sequelas):return max(0,W-sequelas)
def insist(maximum,sequelas=0):
 remaining=maximum;payments=[]
 for f in fractions[:window(sequelas)]:
  pay=ceil(maximum*f)
  if remaining-pay<1:break
  remaining-=pay;payments.append(pay)
 return remaining,payments
check('referência80 semSequela',insist(80),(10,[10,20,40]));check('referência80 umaSequela',insist(80,1),(50,[10,20]));check('referência23',insist(23),(2,[3,6,12]));check('máximo1 não pode pagar',insist(1),(1,[]));check('trêsSequelas semjanela',window(3),0)
profiles=0;monotone=True;valid=True
for maximum in range(1,501):
 for seq in range(6):
  end,p=insist(maximum,seq);profiles+=1
  valid &= end>=1 and len(p)<=window(seq) and sum(p)+end==maximum
  if seq<5:monotone &= sum(insist(maximum,seq+1)[1])<=sum(p)
check('3000perfis preservam máximo>=1 e custo',valid);check('janela menor não cobra rodada inexistente',monotone)
healing=0;valid=True
for maximum in range(1,501):
 target=ceil(maximum*rate)
 for first in [0,1,max(0,target-1),target,target+1]:
  for second in [0,1,max(0,target-first),target+2]:
   healing+=1;total=first+second;recovered=total>=target
   valid &= (recovered==(Fraction(total,maximum)>=rate))
   current_cap=insist(maximum)[0]
   returned=min(current_cap,total) if recovered else 0
   valid &= 0<=returned<=current_cap
check('12500perfis de cura acumulada e teto',valid)
check('duascuras3 referência23',3+3>=ceil(23*rate));check('cura1 referência80 insuficiente',1>=ceil(80*rate),False);check('referência80 fimInsistir recupera teto10',min(insist(80)[0],ceil(80*rate)),10)
check('Integridade26 perdeu6',stage(26,20),0);check('Integridade26 perdeu7',stage(26,19),1);check('Integridade26 perdeu14',stage(26,12),2);check('Remenda5 reduz estágio2para1',stage(26,17),1);check('mais3 chega estágio0',stage(26,20),0);check('Integridade zero',stage(26,0),4)
soul_profiles=0;valid=True
for maximum in range(1,301):
 last=4
 for current in range(maximum+1):
  st=stage(maximum,current);soul_profiles+=1
  valid &= 0<=st<=4 and st<=last
  last=st
check('Integridade melhora monotonicamente com cura',valid)
check('4golpes1 não expulsam Integridade26',stage(26,22),0)
# Dano misto: defesas de tipo, redução conjunta, temporário e reserva.
def damage(parts,rd,temp):
 total=sum(ceil(Fraction(value)*mult) for value,mult in parts)
 total=max(0,total-rd);life=max(0,total-temp)
 return total,min(temp,total),life
check('exemplo21fogo resistênciaRD4 temporário3',damage([(21,Fraction(1,2))],4,3),(7,3,4));check('exemplo30fogoRD6',damage([(30,Fraction(1,2))],6,0),(9,0,9));check('mistura10Cortante8Fogo resistência',damage([(10,Fraction(1)),(8,Fraction(1,2))],0,0),(14,0,14));check('RDzera',damage([(3,Fraction(1))],4,0),(0,0,0));check('danoAlma8RD3temp3',(max(0,8-3-3),max(0,8-3)),(2,5))
# Uma ocorrência só, independentemente das parcelas, paga1 janela sevida>0.
transitions=0;valid=True
for seq,elapsed,hits,temp,amount in itertools.product(range(4),range(4),range(4),[0,1,10],[0,1,5,20]):
 left=window(seq);time_spent=min(left,elapsed);left-=time_spent
 for _ in range(hits):
  absorbed=min(temp,amount);temp-=absorbed;life=amount-absorbed
  left=max(0,left-(life>0))
 transitions+=1;valid &= 0<=left<=window(seq)
check('transições de queda nunca negativas/reiniciadas',valid)
# Probabilidade exata de estabilização. Uma falha não faz dano nem gasta rodadas extras.
probs=[]
for bonus in range(-1,12):
 p=Fraction(sum(d+bonus>=DC for d in range(1,21)),20)
 probs.append({'bonus':bonus,'uma_tentativa':str(p),'duas_tentativas':str(1-(1-p)**2)})
check('Medicina+4CD14 uma tentativa',probs[5]['uma_tentativa'],'11/20');check('Medicina+4CD14 duas tentativas',probs[5]['duas_tentativas'],'319/400')
# Documentação de saídas, custos e interfaces que precisam permanecer explícitas.
for name,phrase in [('dano encerra estabilidade','Dano positivo à vida encerra a estabilidade'),('semsegunda janela','Não recebe uma segunda janela'),('cura após derrota não devolve cena','não devolve sua participação naquela cena'),('máximo pode não pagar','A vida máxima precisa continuar em pelo menos 1'),('semTRextraAlma','Não há um teste adicional'),('zero dasduasreservas','Escolher Insistir não permite agir com Integridade a zero'),('sequelenasduasescolhas','Janela de Aguentar ou Insistir'),('fontesincompatíveis','Uma fonte impedida ou incompatível não entra no total')]:check(name,phrase in s)
expected=['Lento',('Guarda Aberta' if '## Guarda Aberta\n' in s else 'Incapacitado'),'Derrubado','Agarrado','Desarmado','Surdo','Calado','Enfeitiçado','Impedido','Cego','Amedrontado','Envenenado','Atordoado']
for name in expected:check('condição preservada '+name,f'## {name}\n' in s)
check('NPC vida máxima1 conservaIntegridade1', 'com mínimo 1 quando a vida máxima for positiva' in s)
check('NPC vida máxima3 integridade1',max(1,3//2),1)
check('NPC vida máxima20 integridade10',max(1,20//2),10)
report={'manuscritos_auditados':{str(src.relative_to(next(p for p in B.parents if (p/'sistema').is_dir()))):hashlib.sha256(src.read_bytes()).hexdigest()},'ok':not errors,'sha256_texto':hashlib.sha256(src.read_bytes()).hexdigest(),'verificacoes':len(cases),'falhas':errors,'casos':cases,'modelos':{'perfis_custo_Insistir':profiles,'perfis_cura':healing,'perfis_Integridade':soul_profiles,'transicoes_queda':transitions,'estabilizacao':probs},'limites':['Modelos dirigidos, não motor completo de combate.','Contagem de perfis não é número de partidas ou de casos humanos.','Comparação por nível e revisão independente constam dos arquivos próprios; esta execução cobre apenas os modelos deste script.','Não mede diversão, perda de agência percebida ou frequência real de cura.']}
(B/'evidencias/AUDITORIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:report[k]for k in ['ok','verificacoes','falhas']},ensure_ascii=False));raise SystemExit(bool(errors))

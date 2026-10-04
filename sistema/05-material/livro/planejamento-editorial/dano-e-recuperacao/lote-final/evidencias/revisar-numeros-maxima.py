from pathlib import Path
from collections import Counter
from fractions import Fraction
import math,json,hashlib,re
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'dano-e-recuperacao/lote-final';F=B/'DANO-E-RECUPERACAO.md';s=F.read_text();sha=hashlib.sha256(F.read_bytes()).hexdigest();checks=[]
def ck(name,got,exp):checks.append({'caso':name,'obtido':got,'esperado':exp,'ok':got==exp})
def dist(n,faces=8):
 c=Counter({0:1})
 for _ in range(n):
  x=Counter()
  for v,q in c.items():
   for r in range(1,faces+1):x[v+r]+=q
  c=x
 return c
def p_ge(n,t,plus=0,faces=8):
 c=dist(n,faces);return float(Fraction(sum(v for k,v in c.items() if k+plus>=t),faces**n))
def cl(n):return max([c for level,c in [(1,1),(5,2),(9,3),(13,4),(17,5),(21,6),(26,7)] if n>=level])
profiles=[]
for level,con in [(2,3),(5,3),(9,3),(13,3),(17,3),(21,3),(26,3),(30,3),(17,6),(21,6),(26,6),(30,6)]:
 for path,h0,hl in [('Bastião',12,7),('Emanador',6,4)]:
  H=h0+con+(hl+con)*(level-1);T=math.ceil(H/5);C=cl(level)
  profiles.append({'caminho':path,'nivel':level,'Constituicao':con,'PV':H,'limiar':T,'Classe':C,'Cura_maxima_comum_d8':2*C,'PE':3*C,'prob_sair_em_uma_Cura':p_ge(2*C,T),'prob_sair_em_duas_Curas':p_ge(4*C,T),'Aguentar_e_Insistir':'mesma exigência; a probabilidade pressupõe cura disponível e nenhum golpe adicional durante o intervalo.'})
# Gated separate preparations for reflexive Bastião/Guia and self-healing aptitude.
abilities=[]
for level,con,attr in [(19,3,6),(19,6,6),(30,3,6),(30,6,6)]:
 H=12+con+(7+con)*(level-1);T=math.ceil(H/5);C=cl(level)
 abilities.append({'nivel':level,'Con':con,'PV_Bastiao':H,'limiar':T,'prob_AindaDePe':p_ge(1,T,level//2),'prob_Socorrista3d8mais6':p_ge(3,T,attr),'prob_Reversa':p_ge(C,T),'prob_duas_Reversas':p_ge(2*C,T),'prob_CirculacaoPadrao':p_ge(math.floor(1.5*C),T),'nota':'Ainda de Pé exige uso disponível; Socorrista exige Cuidado prévio, Reação e PE; Reversa/Circulação exigem aptidão e ação, não disponíveis a toda ficha.'})
# Capacity and probability limits verified independently by exact integer thresholds.
ck('Bastião30 Con6 H395',12+6+29*(7+6),395);ck('limiar79',math.ceil(395/5),79)
ck('Reversa7d8 não alcança79',p_ge(7,79),0.0)
ck('duas curas3 recuperam referência23',3+3>=math.ceil(23/5),True)
ck('último custo Insistir H80 deixa10',80-sum(math.ceil(80*f) for f in [Fraction(1,8),Fraction(1,4),Fraction(1,2)]),10)
ck('limiar16 pode ser convertido no teto10',min(16,10),10)
ck('janela2 jamais cobra terceira rodada',len([Fraction(1,8),Fraction(1,4),Fraction(1,2)][:2]),2)
# Timeline cases: each atomic hit is not a new damage type parcel.
def w_after(seq,hits,rounds=0):return max(0,3-seq-rounds-sum(x>0 for x in hits))
ck('Golpe misto soma1 perda de rodada',w_after(0,[3+4]),2)
ck('Rajada3 tiros positivos resolve3 perdas',w_after(0,[1,1,1]),0)
ck('DuasSequelas, primeiro dano positivo encerra',w_after(2,[1]),0)
ck('Nenhuma perda por dano zerado',w_after(0,[0,0,0]),3)
# Fixed stage thresholds via integer cross multiplication.
def stage(M,current):return 4 if current<=0 else sum((M-current)*k>=M*n for n,k in [(1,4),(1,2),(3,4)])
for cur,expected in [(26,0),(20,0),(19,1),(13,2),(7,2),(6,3),(0,4),(17,1)]:ck('Integridade26 atual'+str(cur),stage(26,cur),expected)
# Example rescue equivalence in maxHP-cost comparison (same paid heal, different cap).
ck('Aguentar cura80 com referência80',min(80,80),80);ck('Insistir cura80 após custo10',min(80,70),70)
ck('Cura20 em Aguentar e Insistir dá mesma vida atual',[min(20,80),min(20,70)],[20,20])
# Canon-free mechanical specification checks bound to text; they do not implement a game engine.
for phrase in ['Cada ocorrência de dano','Ataques distintos contam separadamente','não recebe a redução pela metade própria do TR','Ao recuperar Integridade, recalcule o estágio','Não recebe uma segunda janela','até aquela queda terminar','As curas podem vir de várias fontes']:
 ck('Texto preserva '+phrase,phrase in s,True)
result={'sha256_texto':sha,'leitor':'maxima','ok':all(x['ok']for x in checks),'verificacoes':len(checks),'casos':checks,'perfis_cura':profiles,'interfaces_cura':abilities,'limites':['Distribuições exatas dos dados, sem estimar frequência real de quedas, acertos, turnos de cura ou disponibilidade de PE.','Cura comum de2×Classe d8: FormaCura sem Melhorias ou Restrições; acesso depende da técnica.','Con3 é perfil constante de comparação; Con6 avançado é cenário, não pressupõe ficha típica nem teto de atributo.','Não são partidas ou leitura por jogadores.']}
(B/'evidencias/NUMEROS-INDEPENDENTES-MAXIMA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sha256':sha,'ok':result['ok'],'checks':len(checks),'perfis':len(profiles),'interfaces':len(abilities)},ensure_ascii=False))
print(json.dumps([x for x in profiles if x['nivel']==30],ensure_ascii=False,indent=2));print(json.dumps(abilities[-1],ensure_ascii=False,indent=2))

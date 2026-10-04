from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json, math, hashlib, itertools
P=Path(__file__).resolve().parent
profiles=[]; checks=[]
def ck(label,value):checks.append({'caso':label,'passou':bool(value)})
def stage(mx,remaining):return 4 if remaining<=0 else sum(Fraction(mx-remaining,mx)>=Fraction(i,4) for i in [1,2,3])
# Exact d8 sums. No attack roll: conditional on a successful damaging delivery.
def dice(n):
 d={0:Fraction(1)}
 for _ in range(n):
  out=defaultdict(Fraction)
  for total,p in d.items():
   for face in range(1,9):out[total+face]+=p/8
  d=dict(out)
 return d
for level,cl in [(2,1),(5,2),(9,3),(13,4),(17,5),(21,6),(26,7),(30,7)]:
 d=dice(2*cl)
 for essence in [0,2,4,6]:
  mx=20+(essence+5)*(level-1)
  probs=[sum((p for damage,p in d.items() if stage(mx,max(0,mx-damage))>=k),Fraction()) for k in [1,2,3,4]]
  profiles.append({'nivel':level,'classe':cl,'essencia':essence,'integridade':mx,'dados_de_Alma':f'{2*cl}d8','dano_medio':9*cl,'fracao_media':str(Fraction(9*cl,mx)),'prob_estagio_pelo_menos_1_2_3_4':[str(p) for p in probs]})
  ck(f'Alma teto C{cl} N{level} E{essence} prob monotônica',all(0<=p<=1 for p in probs) and probs==sorted(probs,reverse=True))
# Previous extra-stage Spirit save: one hit per round, independent saves at a fixed failure rate.
# Resolve lost-fraction floor then +1 stage on failure, capped4. This is the aggressive source reading.
comparisons=[]
for mx,damage,rounds in itertools.product([26,100,194,281],[1,9,27,63],[1,2,3,4]):
 for fail in [Fraction(1,10),Fraction(1,2),Fraction(9,10)]:
  dist={0:Fraction(1)};remaining=mx
  for r in range(rounds):
   remaining=max(0,remaining-damage);base=stage(mx,remaining);out=defaultdict(Fraction)
   for st,p in dist.items():
    initial=max(st,base);out[initial]+=p*(1-fail);out[min(4,initial+1)]+=p*fail
   dist=dict(out)
  newstage=stage(mx,remaining)
  comparisons.append({'integridade':mx,'dano_por_rodada':damage,'rodadas':rounds,'falha_TR_antigo':str(fail),'prob_estagio4_antigo':str(dist.get(4,Fraction())),'estagio_novo':newstage})
  ck(f'remoção TR não piora efeito imediato {mx}/{damage}/{rounds}/{fail}',all(st>=newstage for st in dist))
# Steady max-reference and repeatfalls. Existing reductions persist; reference re-recorded only on a new fall.
falls=[]
for start in [23,60,100,200]:
 mx=start
 for seq in range(4):
  w=max(0,3-seq);target=math.ceil(mx/5)
  pays=[]
  if w:
   for fraction in [Fraction(1,8),Fraction(1,4),Fraction(1,2)][:w]:
    payment=math.ceil(mx*fraction)
    if mx-sum(pays)-payment<1:break
    pays.append(payment)
  after=mx-sum(pays)
  falls.append({'maximo_entrada':mx,'sequelas':seq,'janela':w,'limiar':target,'custos':pays,'maximo_final':after,'resultado':'derrota imediata' if not w else 'socorro exige limiar'})
  ck(f'requedas {start}/{seq}',after>=1 and sum(pays)<=mx-1)
  mx=after
# Rescue chances: guaranteed healing not assumed; d8 rolls at threshold by max-reference.
rescues=[]
for mx in [23,60,100,200]:
 for n in [1,2,4,8]:
  dist=dice(n);target=math.ceil(mx/5);p=sum((q for v,q in dist.items() if v>=target),Fraction())
  rescues.append({'referencia':mx,'limiar':target,'cura':f'{n}d8','prob_superar_limiar':str(p)})
  ck(f'socorro prob {mx}/{n}',0<=p<=1)
report={'sha256_texto':hashlib.sha256((P/'DANO-E-RECUPERACAO.md').read_bytes()).hexdigest(),'aprovado':all(x['passou'] for x in checks),'verificacoes':checks,'perfis_teto_Alma':profiles,'comparacoes_TR_antigo':comparisons,'sequencias_quedas':falls,'perfis_socorro':rescues,'premissas':['Dados d8 representativos e máximo2×Classe da fonte Toca a Alma; não são todas as fichas possíveis.','Entrega de dano e cura já bem-sucedida; não inclui ataque, Bloquear, RD ou PE.','Comparação antiga conserva fracão e avanço extra por TR; testa leitura mais severa da regra antiga, não afirma eliminar ambiguidade histórica.','Reflexo de feedback, diversão, composição de equipe e risco real de mesa não foram medidos.']}
(P/'evidencias/BALANCEAMENTO-POR-NIVEL.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Comparação dirigida — recuperação e Integridade','',f"{len(checks)} verificações; {len(profiles)} perfis de teto de Alma, {len(comparisons)} combinações da regra anterior, {len(falls)} estados de quatro sequências de quedas e {len(rescues)} perfis de cura. Todos os resultados numéricos estão no JSON.",'','## Consequências de design','','Remover o TR adicional elimina uma derrota obtida por quatro falhas de Espírito mesmo com apenas quatro pontos de dano. Com 26 de Integridade e quatro golpes de1, a candidata permanece no estágio0. Na interpretação antiga mais severa, quatro falhas seguidas com probabilidade50% tinham6,25% de chance de chegar ao estágio4; desvantagem de estágio3 pode piorar isso e não foi incluída na conta.','','Os dados máximos crescem com a Classe, enquanto Integridade cresce a cada nível e com Essência. O teto2d8 no nível2 retira em média9/25 da reserva com Essência0; 14d8 no nível30 retira63/165. Com Essência6, os mesmos pontos representam9/31 e63/339. Investir no atributo tem efeito persistente. As probabilidades por estágio constam do arquivo; uma média não garante cruzar patamar.','','Insistir conserva ações à custa da vida máxima, que não volta ao receber cura. Aguentar conserva esse máximo e aceita estabilização. Ambos sofrem dano na janela e precisam de20% de tratamento, evitando a vantagem antiga de encerrar Insistir com1PV. A escolha continua assimétrica: Insistir é valioso para agir no perigo; Aguentar é melhor para preservar recuperação e receber estabilização.','','Cura fraca ainda contribui por acumulação. Não garante levantar um personagem de máximo elevado numa única ação. Estabilizar oferece socorro sem curandeiro e conserva inconsciência; não devolve turnos no combate.','','Três resgates anteriores tornam a próxima queda derrota imediata. O custo de Insistir cresce dentro da queda, mas o máximo reduzido da queda anterior passa a ser a referência nova. A janela menor e a derrota na quarta queda impedem ciclos ilimitados.','','## Limites','','Esta rodada avalia os procedimentos propostos, não um motor completo do sistema. Custos dePE, repertórios concretos, aparar, condições, aliados e adversários alteram os resultados. A revisão independente pode exigir ajustes; estes números não constituem playtest humano.']
(P/'evidencias/BALANCEAMENTO-POR-NIVEL.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'aprovado':report['aprovado'],'checks':len(checks),'Alma':len(profiles),'antigo':len(comparisons),'quedas':len(falls),'socorro':len(rescues)}))

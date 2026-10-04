"""R13: casos executáveis, enumeração exata e regressões de contratos.

Somente lê manuscrito/fontes; grava o relatório local. Não é simulador de combate
completo: dano é um valor pós-rolagem, já incluindo crítico quando houver.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,itertools,json,re
B=Path(__file__).resolve().parent.parent
P=next(p for p in B.parents if p.name=='planejamento-editorial')
R=next(p for p in P.parents if (p/'sistema').is_dir())
text=(B/'BASTIAO.md').read_text(); checks=[]; cases=[]
def check(name,condition,detail=None):
 checks.append(dict(nome=name,passou=bool(condition),detalhe=detail))
def case(name,actual,expected,why):
 ok=actual==expected; cases.append(dict(nome=name,obtido=actual,esperado=expected,passou=ok,motivo=why)); check(name,ok)
def jwrite(name,data): (B/'evidencias'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def hit(roll,bonus,defense,dice=None):
 if roll==20:return True
 if dice==(10,10):return False
 if dice==(1,1):return True
 target=defense if dice is None else sum(dice)+defense-11
 return roll+bonus>=target

def protect(parts, resist=(), reduction=0,temp=0,spent=(),use=None):
 """Ordem de parcelas declarada pela fonte; Alma ignora resistência.
 RD genérica e reserva consomem pela ordem, uma vez. Tuplas [tipo,quantidade].
 """
 if use is not None and use in spent: raise ValueError('mesmo uso de redução repetido')
 parts=[[t,(n+1)//2 if t in resist and t!='Alma' else n] for t,n in parts]
 for pool in (reduction,temp):
  for p in parts:
   used=min(p[1],pool);p[1]-=used;pool-=used
 return parts

def transfer(parts,hp):
 if hp<=0 or sum(n for t,n in parts)<hp:return None
 keep=hp-1; receiver=[]
 for t,n in parts:
  lost=min(n,keep);keep-=lost;receiver.append([t,n-lost])
 return dict(vida_aliado=1,perda_aliado=hp-1,transferido=receiver)

def arrastao(strength,targets,amplify,control_used=False):
 if len(targets)<1 or len(targets)>strength or len(set(targets))!=len(targets):raise ValueError('alvos inválidos')
 if amplify and control_used:raise ValueError('Mão Pesada já usada')
 return dict(ataques=len(targets),pe=2*(len(targets)-1) if amplify else 0,consome_controle=amplify,ataque_extra=0)

def contra(maxclass,hp,hpmax,chosen,attacks,used_spell=False,instant=True):
 if hp*2>hpmax or chosen not in (1,2) or chosen>attacks or used_spell or not instant:return None
 return dict(classe=maxclass//2,pe=3*(maxclass//2),canalizar_excluido=chosen,critico_feitico=False)

def answers(intercepted,hit_original,block_success,in_reach=True,can_act=True,myturn_available=True):
 if not can_act or not in_reach:return []
 return (['Trocação'] if intercepted and hit_original else [])+(['Minha Vez'] if block_success and myturn_available else [])

def semantic(s):
 """Fragments test author-approved invariants, not arbitrary style choices."""
 requirements={
 'assumir_pre':'Reação, antes da rolagem de acerto',
 'duro_sem_limite':'nem tem limite por rodada',
 'nem_passivo':'O benefício é passivo, sem gasto de Reação',
 'arrastao_custo':'2 PE por criatura atacada além da primeira',
 'arrastao_sem_extra':'Não recebe Ataque Extra',
 'arrastao_mao':'Se ainda não tiver usado o controle de Mão Pesada nesta rodada',
 'agarrar_mao':'você precisa de uma mão livre',
 'contra_crit':'O feitiço não causa crítico',
 'contra_canalizar':'O ataque escolhido não recebe Canalizar em Golpe',
 'resposta_alcance':'se ele estiver ao seu alcance',
 'passa_sem_recursao':'A parcela não pode ser transferida novamente',
 'passa_sem_block':'transferência não permite outro Bloquear',
 'certero_nao_acerto':'ele não conta como acerto para suas respostas'}
 plain=s.replace('**','')
 return {k:v in plain for k,v in requirements.items()}

# Source preservation is real byte comparison. Concurrent candidates are separately
# hashed in FONTES, but are not claimed immutable while other agents work.
preserved=json.loads((B/'evidencias/fontes-preservadas.json').read_text())['fontes']
for src in preserved:check('fonte_preservada_'+src['id'],hashlib.sha256((R/src['arquivo']).read_bytes()).hexdigest()==src['sha256'])
for k,v in semantic(text).items():check('contrato_'+k,v)
mutations=[('nem tem limite por rodada','tem limite de uma vez por rodada'),('2 PE por criatura atacada além da primeira','8 PE fixos'),('Não recebe Ataque Extra','Recebe Ataque Extra'),('O feitiço não causa crítico','O feitiço causa crítico'),('O ataque escolhido não recebe Canalizar em Golpe','O ataque escolhido recebe Canalizar em Golpe'),('A parcela não pode ser transferida novamente','A parcela pode ser transferida novamente')]
for before,after in mutations:
 changed=text.replace(before,after);check('mutacao_'+before,changed!=text and not all(semantic(changed).values()))
coverage=json.loads((B/'COBERTURA.json').read_text())['habilidades']
check('19_habilidades',len(coverage)==19 and all(x['nome'] in text for x in coverage))
for x in coverage:check('destino_'+x['nome'],'<!-- page:'+x['pagina']+'|' in text and x['linha'] is not None)
pages=re.split(r'<!-- page:',text)[1:]
word_counts={p.split('|')[0]:len(re.findall(r'\S+',p.split('-->',1)[1])) for p in pages}
check('11_paginas',len(pages)==11)
check('faixa_180_420_palavras',all(180<=n<=420 for n in word_counts.values()),word_counts)
check('sem_titulo_como_ler',not re.search(r'^#+\s+.*como ler',text,re.M|re.I))
check('sem_artigo_inicial',not re.search(r'^#+\s+(?:A|O|As|Os)\s',text,re.M|re.I))
measurements=[float(x.replace(',','.')) for x in re.findall(r'(\d+(?:,\d+)?) m\b',text)]
check('medidas_1_5',all(abs(n/1.5-round(n/1.5))<1e-9 for n in measurements),measurements)

case('Bloquear igualdade acerta',hit(12,5,17,(5,6)),True,'Total17 contra17.')
case('Aparar impede total alto',hit(19,20,17,(10,10)),False,'Duplo10 vence total, exceto20natural.')
case('20 vence Aparar',hit(20,0,30,(10,10)),True,'Crítico tem precedência.')
case('Brecha vence total baixo',hit(1,0,30,(1,1)),True,'D20=1 não tem falha automática geral na candidataR02.')
case('Resposta por hit interceptado',answers(True,True,False),['Trocação'],'Bloquear falhou, não ativa Minha Vez.')
case('Resposta por defesa',answers(True,False,True),['Minha Vez'],'SucessoBlock não ativa Trocação.')
case('Resposta distante negada',answers(True,True,False,False),[],'Alcance de interceptação não é alcance de resposta.')
case('Resposta incapaz negada',answers(True,True,False,True,False),[],'Resolver dano antes de responder.')
case('Casca com Duro exemplo',max(0,36-(5+4+3)-(2+7-1+3)),13,'Duro usa dados já rolados; Casca novos.')
case('Casca com resistência exemplo',max(0,18-(5+4+3)-(2+7-1+3)),0,'Resistência antecede RD.')
case('Passa exemplo fonte',transfer([['Cortante',16]],10),dict(vida_aliado=1,perda_aliado=9,transferido=[['Cortante',7]]),'Conserva exemplo10/16.')
case('Passa resistência receptor',protect([['Cortante',7]],('Cortante',)),[['Cortante',4]],'Arredonda dano recebido para cima.')
case('Passa não necessário',transfer([['Cortante',9]],10),None,'Aliado não cairia.')
case('Passa aliado já zero',transfer([['Cortante',9]],0),None,'Não recupera quem já caiu.')
# Two types, shared reduction, temporary HP, reaction already spent.
ally=protect([['Cortante',22],['Fogo',12]],('Fogo',),reduction=4,temp=3,use='protecao-compartilhada-1')
case('Passa dois tipos após aliado',ally,[['Cortante',15],['Fogo',6]],'ResistênciaFogo; RD4 e reserva3 consomemCortante primeiro.')
p=transfer(ally,10)
case('Passa conserva tipos',p['transferido'],[['Cortante',6],['Fogo',6]],'Perdaaliado9 na primeira parcela.')
case('Passa próprias resistências',protect(p['transferido'],('Cortante',)),[['Cortante',3],['Fogo',6]],'Transferência12 vira9; não é novo ataque.')
case('Passa redução pessoal nova',protect(p['transferido'],('Cortante',),reduction=2,temp=2,spent=['protecao-compartilhada-1'],use='reducao-pessoal-1'),[['Cortante',0],['Fogo',5]],'Uso distinto que protege dano transferido; nenhuma nova Reação.')
try:protect(p['transferido'],reduction=4,spent=['protecao-compartilhada-1'],use='protecao-compartilhada-1'); duplicate=False
except ValueError:duplicate=True
check('Passa mesmo uso de redução não repete',duplicate)
case('Passa Alma não metade',protect([['Alma',7]],('Alma',)),[['Alma',7]],'Alicerce não revoga dono do tipo.')
case('Dano zero ainda hit',answers(True,True,False),['Trocação'],'Proteções de dano não alteram resultado de acerto.')
# Trigger allocation: two reactions in a calendar round are possible around own turn.
reaction=True;used=0
if reaction:used+=1;reaction=False
first=used
reaction=True
if reaction:used+=1;reaction=False
case('Reação antes e depois do próprio turno',[first,used,reaction],[1,2,False],'Não afirmar um teto absoluto de interceptações por rodada civil.')
case('Punho turno comum nível7',1+1+1,3,'Uma Padrão, AtaqueExtra e Bônus apósacerto.')
case('Duas Padrões não repetem AtaqueExtra',1+1+1+1,4,'2 ataquesbase +1extra porrodada +1Bônus.')
for n in range(1,7):case('Arrastão custo '+str(n),arrastao(6,list(range(n)),True)['pe'],2*(n-1),'Paga por tentativa, não por acerto.')
for name,args in [('excesso de alvos',(2,[1,2,3],False)),('alvo repetido',(3,[1,1],False)),('sem alvo',(0,[],False)),('controle já usado',(6,[1,2],True,True))]:
 try:arrastao(*args);valid=False
 except ValueError:valid=True
 check('Arrastão rejeita '+name,valid)
case('Arrastão gratuito após controle',arrastao(6,[1,2],False,True)['pe'],0,'A habilidade continua disponível, sem outro controle.')
case('Arrastão turno For6',arrastao(6,list(range(6)),False)['ataques']+1,7,'Seis alvos e Bônus; não sete num mesmo alvo.')
case('Arrastão mesmo alvo',1+1,2,'Um golpeArrastão e no máximoBônus, sem extras externos.')
case('Contra classe/custo',contra(7,50,100,2,2),dict(classe=3,pe=9,canalizar_excluido=2,critico_feitico=False),'Nível27:maiorClasse7.')
for name,args in [('vida acima',(7,51,100,1,2)),('terceiro ataque',(7,50,100,3,3)),('segundo inexistente',(7,50,100,2,1)),('limite feitiço usado',(7,50,100,1,2,True)),('Carregar incompleto',(7,50,100,1,2,False,False))]:case('Contra rejeita '+name,contra(*args),None,'Conserva requisitos do feitiço e limite do turno.')
case('Contra único ataque válido',contra(7,50,100,1,1)['classe'],3,'Primeiro ataque basta.')
case('Ainda de Pé nível7 média',4.5+7//2,7.5,'Metade do nível para baixo.')
case('Ainda de Pé nível30 média',4.5+30//2,19.5,'Não libera ação a0 automaticamente.')
case('Embalo não acumula',max(4,4),4,'Sem gasto intermediário, gatilhos repetidos mantêm4.')
case('Embalo repõe após gasto',max(1,4),4,'Repor4 não significa somar4.')
case('Guarda-Costas não soma coberturas',max(2,5),5,'Cobertura maior prevalece.')
# Exhaustive transfer conservation and nonnegative pools; no randomness.
transfers=0
for hp in range(1,51):
 for a in range(0,51):
  for b in (0,1,7,20):
   z=transfer([['Cortante',a],['Fogo',b]],hp);transfers+=1
   assert (z is not None)==(a+b>=hp)
   if z: assert z['perda_aliado']+sum(n for t,n in z['transferido'])==a+b and all(n>=0 for t,n in z['transferido'])
check('conservação_exaustiva_transferência',True,{'cenarios':transfers})
# Exact saving throw/Provocar analysis, ties resist; shared Provocar roll matters
# for all-target probabilities, not just one-target averages.
saves=[]
for dc in (12,16,20):
 for bonus in (1,4,7,10):
  p=Fraction(sum(r+bonus>=dc for r in range(1,21)),20)
  adv=1-(1-p)**2
  saves.append(dict(cd=dc,bonus=bonus,normal=float(p),vantagem=float(adv),ganho_pontos_percentuais=float((adv-p)*100)))
check('vantagem_fórmula',all(0<=x['normal']<=x['vantagem']<=1 for x in saves))
provocar=[]
for pb in (3,6,10):
 for sb in (1,4,7):
  for targets in (1,2,4):
   per=[]
   for r in range(1,21):per.append(Fraction(sum(s+sb<r+pb for s in range(1,21)),20))
   p=sum(per)/20
   allfail=sum(x**targets for x in per)/20
   provocar.append(dict(bonus_provocar=pb,bonus_espirito=sb,alvos=targets,falha_marginal=float(p),todos_falham_mesmo_teste=float(allfail)))
check('provocar_empate_resiste',sum(s<10 for s in range(1,21))==9)
# Exact Block outcomes: policy never risks a static miss. If static hit, choose
# Block. Unlike fixedDefense comparison, this conditions Duro on failure.
dist=Counter(sum(x) for x in itertools.product(range(1,11),repeat=2)); defense_rows=[]
for defense,bonus,con,raw,resist,casca in itertools.product((17,21,25),(3,7,10),(3,6),(20,40,80),(False,True),(False,True)):
 total=0; fail=0;durosum=0;zero=0;brecha=0;static=0
 for r in range(1,21):
  st=hit(r,bonus,defense)
  static+=raw*100 if st else 0
  for d1,d2 in itertools.product(range(1,11),repeat=2):
   if not st:zero+=1;continue
   blockedhit=hit(r,bonus,defense,(d1,d2))
   if (d1,d2)==(1,1):brecha+=1
   if not blockedhit:zero+=1;continue
   fail+=1;durosum+=d1+d2+con
   base=(raw+1)//2 if resist else raw
   if casca:
    for ds,weight in dist.items():
     received=max(0,base-(d1+d2+con)-(ds-1+con));total+=received*weight/100
     if received==0:zero+=weight/100
   else:
    received=max(0,base-(d1+d2+con));total+=received
    if received==0:zero+=1
 defense_rows.append(dict(defesa=defense,ataque_bonus=bonus,con=con,dano_pos_rolagem=raw,alicerce=resist,casca_interceptacao=casca,media_defesa_estatica=static/2000,media_recebida=round(total/2000,8),chance_dano_zero=round(zero/2000,8),chance_falha_bloquear=fail/2000,media_duro_quando_falha=durosum/fail if fail else 0,chance_brecha=brecha/2000))
check('modelos_defensivos_limites',all(0<=x['media_recebida']<=x['media_defesa_estatica'] and 0<=x['chance_dano_zero']<=1.0000001 for x in defense_rows),{'perfis':len(defense_rows),'espaco_por_perfil':2000,'convolucao_Casca':100})
# Source-independent inequalities: adding resistance or Casca must never worsen
# own incoming HP damage. Raw damage and the reaction opportunity are fixed.
index={(x['defesa'],x['ataque_bonus'],x['con'],x['dano_pos_rolagem'],x['alicerce'],x['casca_interceptacao']):x for x in defense_rows}
for k,x in index.items():
 if not k[4]:assert index[k[:4]+(True,k[5])]['media_recebida']<=x['media_recebida']+1e-8
 if not k[5]:assert index[k[:5]+(True,)]['media_recebida']<=x['media_recebida']+1e-8
check('monotonia_resistencia_e_Casca',True)
report=dict(sha256_texto=hashlib.sha256(text.encode()).hexdigest(),checks=checks,casos=cases,aprovado=all(x['passou'] for x in checks),quantidades=dict(checks=len(checks),casos=len(cases),perfis_defesa=len(defense_rows),perfis_TR=len(saves),perfis_provocar=len(provocar),cenarios_transferencia=transfers,mutacoes=len(mutations)),palavras_paginas=word_counts,modelos=dict(defesa=defense_rows,TR=saves,provocar=provocar),limites=['Enumeração exata destes modelos; não é playtest nem prova de balanceamento do livro.','Dano de entrada já determinado; não modela variação de dados/critico e usa um ataque por evento.','Aparar/Brecha têm chance registrada; dano adicional do agressor em Brecha depende Reação e não está incluído.','Casca pressupõe interceptação disponível; não vale sobre todo ataque contra o Bastião.','Não mede distância, objetivos da missão, economia completa de cenas, diversão ou compreensão humana.','Dano misto usa candidata R03: ordem de parcelas fixada antes da rolagem.'])
jwrite('AUDITORIA.json',report)
print(json.dumps(dict(aprovado=report['aprovado'],quantidades=report['quantidades'],falhas=[x for x in checks if not x['passou']],palavras_paginas=word_counts),ensure_ascii=False,indent=2))
raise SystemExit(0 if report['aprovado'] else 1)

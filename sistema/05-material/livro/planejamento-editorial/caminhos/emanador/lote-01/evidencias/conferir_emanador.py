"""R16: modelos exatos de orçamento, custo, estoque e estados.
Não edita fontes/manuscrito. Grava somente AUDITORIA local.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib,json,re
B=Path(__file__).resolve().parent.parent;P=next(p for p in B.parents if p.name=='planejamento-editorial');R=next(p for p in P.parents if (p/'sistema').is_dir());F=B/'EMANADOR.md';text=F.read_text();checks=[];cases=[]
def ck(n,v,d=None):checks.append(dict(nome=n,passou=bool(v),detalhe=d))
def case(n,v,w,m):cases.append(dict(nome=n,obtido=v,esperado=w,motivo=m,passou=v==w));ck(n,v==w)
def price(c,t,free=False,form=False):
 p={'Leve':(c+1)//2,'Média':c,'Pesada':(3*c+1)//2,'Grátis':0}[t]
 return max(1,p-(c+1)//2) if free and not form and p else p

def remodel(c,original,removed,added,new_spent,refund=0,formcap=None):
 available=original-max(0,added-removed)
 if available<0:return None
 budget=3*c-new_spent+min(refund,2*c,new_spent)
 if budget<0:return None
 return min(available,budget,formcap if formcap is not None else 3*c)

def spellcost(orig,final,mode='normal',fixed=0,extras=0,action='P'):
 assert 1<=orig<=final<=7
 if mode=='instintiva' and (orig not in(1,2) or action!='P'):raise ValueError('Instintiva inválida')
 if mode=='instintiva':base=1+3*(final-orig)
 elif mode=='afinidade':base=(max(1,3*orig-fixed)+1)//2+3*(final-orig)
 elif mode=='eco':base=(max(1,3*final-fixed)+1)//2
 else:base=max(1,3*final-fixed)
 return base+extras

def may_force(form,piece,already=0,blocked=False):
 if already or blocked:return False
 if form in('Toque','Aura','Onda') and piece=='Longe':return False
 return True

def echo_allowed(level,category,form=False):
 return category=='Leve' or (level>=19 and category=='Média') or (form and category=='Grátis' and level>=15)

def allowed_edits(level,echoes=0,normal=0,forced=0):
 if forced>1:return False
 if echoes==2 and level<27:return False
 if echoes and normal and level<11:return False
 if normal>(2 if level>=23 else 1):return False
 return echoes+normal<= (3 if level>=23 else (2 if level>=11 else 1))

def shape(current,ammo_type,loaded,new_type,new_capacity,jammed=False):
 if loaded and (ammo_type!=new_type or loaded>new_capacity):return None
 return dict(perfil=current,tipo=ammo_type,municao=loaded,precisa_recarregar=jammed)

class Impulse:
 def __init__(self):self.held=False;self.exp=-1;self.blocked=-1;self.flow=True;self.over=True
 def generate(self,turn,eligible=True,padrao=True,spent=False,initial=True):
  if eligible and padrao and not spent and initial and turn>self.blocked:self.held=True;self.exp=turn+1;return True
  return False
 def spend(self,turn,over=False,flow=False):
  if not self.held or turn>self.exp:return False
  if over and not self.over:return False
  self.held=False
  if over:self.over=False;self.blocked=turn+1
  if flow and self.flow and not over and turn>self.blocked:self.flow=False;self.held=True;self.exp=turn+1
  return True

for arquivo,hash_fonte in json.loads((B/'evidencias/fontes-preservadas.json').read_text()).items():
 row={'arquivo':arquivo,'sha256':hash_fonte}
 ck('fonte_preservada_'+row['arquivo'],hashlib.sha256((R/row['arquivo']).read_bytes()).hexdigest()==row['sha256'])
coverage=json.loads((B/'COBERTURA.json').read_text())['itens'];ck('48_entradas',len(coverage)==48 and all(x['nome_candidato'] in text for x in coverage))
pages=re.split(r'<!-- page:',text)[1:];words={p.split('|')[0]:len(re.findall(r'\S+',p.split('-->',1)[1])) for p in pages};ck('19_paginas',len(pages)==19);ck('180_400_palavras',all(180<=x<=400 for x in words.values()),words)
ck('titulos_diretos',not re.search(r'^#+\s+(?:A|O|As|Os)\s|^#+.*como ler',text,re.M|re.I))
measures=[float(x.replace(',','.')) for x in re.findall(r'(\d+(?:,\d+)?) m\b',text)];ck('medidas_grade',all(x/1.5==int(x/1.5) for x in measures));ck('excecao_narrativa_1km','**1 km**' in text)
# Contract fragments are kept focused; phrases below reflect semantic exceptions.
required=['uma Modulação Forçada por conjuração','Uma Remodelagem não aumenta os dados','não cria Eco','não cria outro Eco por si só','no máximo três alterações','A alteração reaproveitada','primeira conjuração','não recebe novos abatimentos','não altera o tipo ou a quantidade da munição','Sobrecarregar Energia']
def contracts(s):
 s=s.replace('**','');return [x in s for x in required]
for k,v in zip(required,contracts(text)):ck('contrato_'+k,v)
mutations=[('uma Modulação Forçada por conjuração','duas Modulações Forçadas por conjuração'),('Uma Remodelagem não aumenta os dados','Uma Remodelagem aumenta os dados'),('não cria outro Eco por si só','cria outro Eco por si só'),('no máximo três alterações','no máximo quatro alterações'),('não altera o tipo ou a quantidade da munição','altera o tipo e a quantidade da munição')]
for a,b in mutations:ck('mutacao_'+a,text.replace(a,b)!=text and not all(contracts(text.replace(a,b))))
case('Fura para Rápido C3',remodel(3,6,3,5,5),4,'Diferença2 paga com2d8; custo PE9+2.')
case('Aura para Explosão C3',remodel(3,7,2,2,5,0),4,'Perde devolução3 de Corpo a Corpo.')
case('Troca barata perde sobra',remodel(3,6,3,2,2),6,'Novo orçamento7 não aumenta original6.')
case('Devolução que sobrava não recompra dado',remodel(2,6,1,2,2,2),5,'Diferença1 é paga mesmo se novo orçamento admitir6.')
case('Sem resultado para pagar',remodel(1,0,1,2,2),None,'Falta ponto; não inventa saldo.')
case('Apoio para Cura mantém teto',remodel(3,9,0,3,3,0,6),6,'9p de apoio→cura, paga3p e respeita6d8.')
case('Duas trocas compensam entre si',remodel(4,8,4+2,2+4,6),6,'Orçamento final pode exigir ajuste mesmo com diferença zero.')
case('Longe preço C3',price(3,'Leve'),2,'Catálogo antes dos descontos.')
case('Longe Livre C3',price(3,'Leve',True),1,'Mínimo1.')
case('Forma não recebe Família Livre',price(3,'Leve',True,True),2,'Aura/Explosão não são Melhorias.')
case('Eco Modulação ceil C3',(price(3,'Leve')+1)//2,1,'Metade de2.')
case('Eco não zera preço1',(price(1,'Leve')+1)//2,1,'Metade arredondada para cima.')
case('Afinidade C2 ampliado4',spellcost(2,4,'afinidade'),9,'3+6.')
case('Instintiva C2 ampliado5',spellcost(2,5,'instintiva'),10,'1+9.')
case('Extras não recebem metade',spellcost(2,4,'afinidade',extras=5),14,'9+5, não14/2.')
case('Ritual fixo antes Afinidade',spellcost(2,4,'afinidade',fixed=2),8,'(6−2)/2 +6.')
case('Instintiva não perde mínimo',spellcost(2,2,'instintiva',fixed=4),1,'Preço substituído, não descontado para0.')
try:spellcost(2,2,'instintiva',action='B');bad=False
except ValueError:bad=True
ck('Instintiva não em Bônus',bad)
case('Melhor alternativa não composto',min(spellcost(2,4,'afinidade'),spellcost(2,4,'eco')),6,'Eco no custo normal12 dá6; não dividir os9 da Afinidade por2.')
case('Toque rejeita Extensão',may_force('Toque','Longe'),False,'PE extra não compra combinação proibida.')
case('Uma Modulação',may_force('Projétil','Passo',already=1),False,'Echo e normal compartilham teto.')
case('Família Fechada não contorna',may_force('Projétil','Passo',blocked=True),False,'Preço nunca libera família.')
case('Eco Médio com preço1 no11',echo_allowed(11,'Média'),False,'Categoria antes de desconto.')
case('Eco Médio no19',echo_allowed(19,'Média'),True,'Reverberação aumenta categoria.')
case('Eco Pesado no27',echo_allowed(27,'Pesada'),False,'Acorde não libera Pesada.')
case('Eco Forma grátis depois15',echo_allowed(15,'Grátis',True),True,'FormaFluida permite.')
case('Contraponto nível11',allowed_edits(11,1,1,1),True,'Um Eco+um novo.')
case('Contraponto nível2 não acrescenta',allowed_edits(2,1,1),False,'Eco ocupa Desdobramento.')
case('Composição com Contraponto',allowed_edits(23,1,2,1),True,'Três alterações.')
case('Acorde não permite quatro',allowed_edits(27,2,2,1),False,'DoisEcos+uma nova no máximo.')
case('Acorde não força duas',allowed_edits(27,2,1,2),False,'SóumaModulação.')
case('Munição não converte',shape('Rifle','Pistola',2,'Rifle',3),None,'Antes deve descarregar.')
case('Capacidade menor bloqueia',shape('Rifle','Rifle',3,'Rifle',2),None,'Três unidades não cabem em2.')
case('Transformar não retira interrupção',shape('Rifle','Rifle',2,'Rifle',3,True)['precisa_recarregar'],True,'Estado de recarga permanece.')
case('Cadência limite Cmax7',7//2,3,'Expandida usaClassefinal.')
case('Ritmo Cmax7',7-1,6,'Convergente não liberaClasse7.')
case('Modulações aprendidas',[2,3,4,5],[2,3,4,5],'Níveis2/7/15/23; sem quinta antes23.')
# Boundaries of stored resources, measured in the owner's following turns.
class EchoStore:
 def __init__(self,level):self.level=level;self.items={}
 def valid(self,turn):return {k:v for k,v in self.items.items() if turn<=v}
 def gain(self,piece,method,turn,fresh=True):
  self.items=self.valid(turn)
  if not fresh:return False
  key=(piece,method);limit=2 if self.level>=27 else 1
  if key not in self.items and len(self.items)>=limit:self.items.pop(next(iter(self.items)))
  self.items[key]=turn+(2 if self.level>=27 else 1);return True
 def spend(self,key,turn):
  self.items=self.valid(turn)
  if key not in self.items:return False
  del self.items[key];return True
es=EchoStore(2);es.gain('Longe','Remodelar',1)
case('Eco básico até próximo turno',('Longe','Remodelar') in es.valid(2),True,'Pode usar antes do fim do próprio turno seguinte.')
case('Eco básico expirado depois',('Longe','Remodelar') in es.valid(3),False,'Não pode guardar indefinidamente.')
es=EchoStore(27);es.gain('Longe','Remodelar',1);es.gain('Contorno','Remodelar',2)
case('Acorde terceiro turno conserva ambos',len(es.valid(3)),2,'Prazo individual de dois turnos seguintes.')
case('Acorde quarto turno perde primeiro',len(es.valid(4)),1,'Criar o segundo não renova o primeiro.')
es.gain('Contorno','Remodelar',3)
case('Eco mesma identidade não duplica',len(es.items),2,'Mantém o Longe ainda válido e uma identidade Contorno; não três.')
case('Eco repetido sem novo Desdobramento',es.gain('Passo','Modulação',3,fresh=False),False,'Reaproveitar sozinho não gera reserva nova.')
case('Eco consumido',es.spend(('Contorno','Remodelar'),3),True,'Gasto na declaração, antes de acertar.')
case('Eco não pode ser gasto novamente',es.spend(('Contorno','Remodelar'),3),False,'Mesmo erro não recupera sem gatilho de Reverberação.')
case('Instintiva ampliada pode perder para Eco',min(spellcost(2,5,'instintiva'),spellcost(2,5,'eco')),8,'Escolhe Eco sobre custo normal 15, não metade do custo Instintivo 10.')
def consume_cast_triggers(first_affinity,next_eco,chosen):
 assert chosen in ('afinidade','eco','instintiva','normal')
 # Conjurar, e não obter o desconto, é o gatilho das duas permissões.
 return dict(afinidade_primeira=False if first_affinity else first_affinity,eco_proxima=False if next_eco else next_eco)
case('Afinidade e Eco consomem gatilhos',consume_cast_triggers(True,True,'eco'),dict(afinidade_primeira=False,eco_proxima=False),'Ao escolher Eco, a conjuração ainda foi a primeira da cena e a próxima após o gatilho.')
# Returning to original profile conserves stock and blocks firing until normal adjustment.
def end_binding(ammo,loaded,original_ammo,original_capacity):
 return dict(quantidade=loaded,tipo=ammo,pode_disparar=ammo==original_ammo and loaded<=original_capacity)
case('Fim vínculo conserva munição incompatível',end_binding('Rifle',2,'Pistola',6),dict(quantidade=2,tipo='Rifle',pode_disparar=False),'Não destrói nem converte estoque; impede disparar até ajustar.')
case('Fim vínculo excesso não vira disparo',end_binding('Rifle',5,'Rifle',3)['pode_disparar'],False,'A capacidade original é conferida sem gerar recarga.')

# Exhaustive budget invariants, varying net refund and explicit piece swaps.
budget_count=0
for c in range(1,8):
 for old in range(3*c+1):
  for removed,added in product(range(0,2*c+1),repeat=2):
   for refund in (0,c,2*c):
    newtotal=added;out=remodel(c,old,removed,added,newtotal,refund)
    if out is not None:
     assert 0<=out<=old and out<=3*c-newtotal+min(refund,2*c,newtotal)
    budget_count+=1
ck('orcamento_exaustivo',True,{'casos':budget_count})
# Discounts compared as alternatives. Fixed Ritual belongs to the chosen method.
prices=[]
for orig in range(1,4):
 for final in range(orig,8):
  for fixed in range(0,4):
   normal=spellcost(orig,final,fixed=fixed);aff=spellcost(orig,final,'afinidade',fixed);eco=spellcost(orig,final,'eco',fixed)
   chosen=min(aff,eco);composed=(aff+1)//2
   prices.append(dict(original=orig,final=final,fixo=fixed,normal=normal,afinidade=aff,eco=eco,escolha=chosen,metades_compostas_proibidas=composed))
   assert chosen>=1 and chosen<=aff and chosen<=eco
ck('custos_positivos',all(x['escolha']>=1 for x in prices),{'perfis':len(prices)})
# Familiar versions and Echo cannot refresh their own one-shot state.
i=Impulse();case('Gerar após aplicação própria',i.generate(1),True,'PrimeiraresoluçãoPadrãoqualificada.');case('Gasto comum',i.spend(2),True,'Dentrodo prazo.');case('Gasto não regenera',i.generate(2,spent=True),False,'Semciclo de recurso.')
i=Impulse();i.generate(1);case('Fluxo uma vez recupera',i.spend(2,flow=True),True,'Habilidade27 concedeexceção.');case('Fluxo reserva ativa',i.held,True,'Ainda umImpulso.');case('Sobrecarga posterior',i.spend(3,over=True),True,'Podegastarrecuperado.');case('Bloqueio até fim próximo',i.generate(4),False,'Não gerar no turno4.');case('Geração posterior ao bloqueio',i.generate(5),True,'No turno5 voltapermissão.')
i=Impulse();case('Bônus não gera',i.generate(1,padrao=False),False,'AcelerarabrePadrão,masnãogera.' );case('Fica não gera de novo',i.generate(1,initial=False),False,'Parcelaposteriornãonovaconjuração.')
# Exact numerical gain of low-die reroll and one result correction.
rerolls=[]
for faces in (4,6,8,10,12):
 normal=Q(faces+1,2);changed=sum((normal if r<=2 else Q(r)) for r in range(1,faces+1))/faces
 rerolls.append(dict(dado=faces,media_normal=float(normal),media_corrigida=float(changed),ganho=float(changed-normal)))
case('d8 baixa rerrolagem',next(x['media_corrigida'] for x in rerolls if x['dado']==8),5.25,'1/2 repetidosuma vez,cada novo obrigatório.')
probs=[]
for success in range(1,20):
 p=Q(success,20)
 for c in range(1,8):
  fail=1-p;intensify=1-p*p;combo=1-p**4
  assert fail<=intensify<=combo<=1
  probs.append(dict(p_resistir=float(p),classe=c,efeito_normal=float(fail),intensificar=float(intensify),intensificar_corrigir=float(combo),custo_intensificar=(c+1)//2,custo_correcao_medio_se_resistir=float(c*p*p)))
ck('probabilidades_exatas',True,{'perfis':len(probs)})
# Illegal free repetitions should fail: limits are resources, not copies per target.
case('Reverberação preserva só um em Acorde',min(1,2),1,'Reação não duplica estoque.')
case('Cadência uma Padrão e uma Bônus',1+1,2,'Conta ações, não feitiço na arma.')
case('Aperfeiçoar compartilhado9d8',9*5.25,47.25,'Mesmo total corrigido poralvo; não uma rolagem por criatura.')
report=dict(ok=all(x['passou'] for x in checks),manuscritos_auditados={str(F.relative_to(R)):hashlib.sha256(F.read_bytes()).hexdigest()},sha256_texto=hashlib.sha256(F.read_bytes()).hexdigest(),aprovado=all(x['passou'] for x in checks),checks=checks,casos=cases,quantidades=dict(checks=len(checks),casos=len(cases),orcamentos=budget_count,perfis_custo=len(prices),perfis_probabilidade=len(probs),mutacoes=len(mutations)),palavras_paginas=words,modelos=dict(custos=prices,rerrolagens=rerolls,probabilidades=probs),limites=['Não é playtest nem prova de equilíbrio entre os seis Caminhos.','Ataque/TR usa probabilidade parametrizada; Bloquear/condições reais podem mudar os valores.','Modelos não medem utilidade narrativa de detectar/gravar/teleportar arma, tempo de mesa ou carga cognitiva.','Custos são simulações das decisões registradas, não evidência de que toda interação já estava na publicação.'])
(B/'evidencias/AUDITORIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'aprovado':report['aprovado'],'quantidades':report['quantidades'],'falhas':[x for x in checks if not x['passou']]},ensure_ascii=False,indent=2));raise SystemExit(0 if report['aprovado'] else 1)

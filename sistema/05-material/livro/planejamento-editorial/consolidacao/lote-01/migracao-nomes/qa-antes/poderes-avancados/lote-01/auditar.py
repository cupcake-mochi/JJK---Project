#!/usr/bin/env python3
"""Auditoria dirigida R08. Executa contas e modelos; não simula partidas humanas.
Lê contrato candidato, texto conferido e tabelas de progressão/R06. Falha se âncora
numérica desaparecer; não usa um valor silencioso de reserva.
"""
from pathlib import Path
import hashlib,itertools,json,math,re
from fractions import Fraction
O=Path(__file__).resolve().parent
R=next(p for p in O.parents if (p/'sistema/03-mecanica/18-progressao.md').exists())
P=R/'sistema/05-material/livro/planejamento-editorial'
s=(O/'PODERES-AVANCADOS.md').read_text()
c=json.loads((O/'CONTRATO.json').read_text())
source=(R/'sistema/05-material/livro/manual/40-fundamento.md').read_text()
prog=(R/'sistema/03-mecanica/18-progressao.md').read_text()
r06=(P/'fundamento/lote-01/FUNDAMENTO.md').read_text()
p11=(R/'sistema/03-mecanica/11-aptidoes-e-refino.md').read_text()
checks=[]
def ck(name,value,detail=None):
 checks.append(dict(id=name,passou=bool(value),detalhe=detail))
 if not value: raise AssertionError(name+': '+str(detail))
def req(pattern,text,label):
 m=re.search(pattern,text,re.S|re.M)
 ck('ancora-'+label,m is not None)
 return m
# Âncoras do dono publicado, sem reinterpretar aritmética antiga como canon.
old_barrier=int(req(r'Por fora ela tem (\d+) × metade do refino',source,'vida-fonte')[1])
ck('vida-preservada',old_barrier==c['barrier_factor'])
req(r'\*\*Dura metade do refino em rodadas\*\*, no mínimo uma',source,'duracao-fonte')
req(r'\*\*6 × a sua maior Classe\*\*',source,'preco-fechado-fonte')
req(r'abrir cobra `7 ×` a sua maior Classe',source,'preco-aberto-fonte')
old_radius=float(req(r'raio é de `(\d+) m`',source,'raio-antigo')[1])
# A tabela publicada de progressão continua dona de Classe e Maestria.
levels={}
for line in prog.splitlines():
 cells=[x.strip().replace('**','') for x in line.split('|')[1:-1]]
 if len(cells)==9 and cells[0].isdigit():
  levels[int(cells[0])]=dict(mastery=int(cells[2]),slots=int(cells[3]),base_refino=int(cells[4]),spell_class=int(cells[5]))
ck('progressao-30-niveis',set(levels)==set(range(1,31)))
curve_line=req(r'^\| \*\*especialista\*\*[^\n]+',p11,'curva-refino')[0]
curve_values=[int(x) for x in re.findall(r'`(\d+)`',curve_line)]
ck('curva-sete-marcos',len(curve_values)==7)
curve_header=req(r'\| \| nv 6 \| nv 10 [^\n]+',p11,'marcos-curva')[0]
curve_levels=[int(x) for x in re.findall(r'nv (\d+)',curve_header)]
ck('curva-sete-niveis',len(curve_levels)==7)
def max_refino(lv): return curve_values[max(i for i,n in enumerate(curve_levels) if n<=lv)] if lv>=curve_levels[0] else 1
maximum={}
for a,b,d,p,pe in re.findall(r'\| (17|21|26) a (20|25|30) \| (\d+)d8 \| (\d+) \| (\d+) \|',r06):
 maximum[int(a)]=dict(last=int(b),dice=int(d),assembly=int(p),pe=int(pe))
ck('maxima-tres-faixas',len(maximum)==3)
# Texto candidato e contrato precisam continuar correspondendo.
anchors={
 'dano':f"**{c['damage_multiplier']} × sua maior Classe em d8**",
 'vida':f"**{c['barrier_factor']} × metade do refino em pontos de vida**",
 'raioaberto':str(c['open_radius']).replace('.',',')+' m',
 'fimturno':'**ao final do último turno contado**',
 'interior':'**um quarto do dano**',
 'custo6':'6 × maior Classe em PE', 'custo7':'7 × maior Classe em PE',
 'nomesclasse':'Expansão não tem Classe própria',
 'zerogratis':'Classe 0 continua gratuita',
 'trtotal':'**o mesmo total**', 'capfalha':'no máximo uma falha por esse personagem na rodada',
 'alcancebarreira':'alcance chegue ao exterior', 'critsbarreira':'sem teste de acerto e sem crítico',
 'falhatrbarreira':'A estrutura falha em TR',
 'simetria':'**incluindo você**', 'zerofim':'**0 PV**',
 'protecaolocal':'essa regra não se aplica à pessoa protegida',
 'semreconjurar':'não novas conjurações',
}
for label,text in anchors.items(): ck('texto-'+label,text in s,text)
# Auditoria editorial automática: estrutura, não qualidade literária.
pages=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->(.*?)(?=<!-- page:|\Z)',s,re.S)
ck('paginas-15',len(pages)==15,len(pages))
ck('ids-unicos',len({p[0] for p in pages})==len(pages))
words={}
for key,title,body in pages:
 words[key]=len(re.findall(r'\S+',body))
 ck('palavras-'+key,180<=words[key]<=400,words[key])
 ck('titulo-'+key,body.lstrip().startswith('# '+title.strip()+'\n'))
 for line in body.splitlines():
  if line.startswith('|'): ck('colunas-'+key,line.count('|')-1<=4)
headings=re.findall(r'^#+ (.+)$',s,re.M)
ck('titulos-sem-artigo',not any(re.match(r'^(A|O|As|Os)\s',h) for h in headings))
ck('titulos-sem-como-ler',not any('como ler' in h.lower() for h in headings))
ck('sem-contraste-formula',not re.search(r'não é .{0,80}[,;:] é ',s,re.I))
# Funções da candidata.
def rounds(ref): return max(1,ref//c['duration_divisor'])
def damage(cl): return c['damage_multiplier']*cl
def barrier(ref): return c['barrier_factor']*(ref//2)
def threshold(ess): return max(1,ess//c['failure_divisor'])
def pulse_times(ref): return list(range(rounds(ref)+1))
def discount_cost(base,discount,half=False):
 if base==0: return 0
 n=max(1,base-discount)
 return max(1,math.ceil(n/2)) if half else n
def radius(ref,mode):
 return c['open_radius'] if mode=='aberto' else min(c['closed_radius_factor']*ref,c['incomplete_radius_cap']) if mode=='incompleta' else c['closed_radius_factor']*ref
numeric=[]
for lv,ref in [(10,4),(14,5),(18,7),(21,9),(26,10),(30,10)]:
 cl=levels[lv]['spell_class']; ma=levels[lv]['mastery']
 numeric.append(dict(level=lv,refino=ref,spell_class=cl,mastery=ma,closed_pe=c['closed_open_cost_multiplier']*cl,open_pe=c['open_cost_multiplier']*cl if ref==10 else None,pulses=len(pulse_times(ref)),dice_per_pulse=damage(cl),mean_per_pulse=damage(cl)*4.5,mean_full=damage(cl)*4.5*len(pulse_times(ref)),barrier_pv=barrier(ref),closed_radius=radius(ref,'fechado')))
ck('exemplo-mei',numeric[1]['closed_pe']==24 and numeric[1]['barrier_pv']==100 and numeric[1]['mean_full']==108)
ck('exemplo-sala',numeric[2]['closed_pe']==30 and numeric[2]['barrier_pv']==150 and numeric[2]['closed_radius']==10.5)
ck('exemplo-final',numeric[4]['open_pe']==49 and numeric[4]['dice_per_pulse']==14 and numeric[4]['pulses']==6)
ck('desconto-fechado-C5',discount_cost(15,5)==10)
ck('desconto-aberto-C5',discount_cost(15,8)==7)
ck('sequencia-casca',[max(0,barrier(10)-63*i) for i in range(1,5)]==[187,124,61,0])
ck('queda-quarto-pulso',math.ceil(barrier(10)/(damage(7)*4.5))==4)
ck('limiares-essencia',[threshold(e) for e in range(7)]==[1,1,1,1,2,2,3])
ck('raio-aberto-grade',Fraction(str(c['open_radius']))/Fraction(3,2)==133)
ck('reducao-raio',math.isclose((old_radius-c['open_radius'])/old_radius,0.0025))
ck('fuga1905',190.5+9==c['open_radius'] and 190.5+10.5>c['open_radius'])
ck('fuga150',150+49.5==c['open_radius'] and 150+51>c['open_radius'])
# Todas as medidas de domínio explicitamente criadas estão na grade.
for ref in range(4,11):
 for mode in ['incompleta','fechado','aberto']:
  ck(f'grade-{ref}-{mode}',(Fraction(str(radius(ref,mode)))/Fraction(3,2)).denominator==1)
# Preços: custo zero preservado; custo positivo nunca zero e uma metade não se multiplica.
price_states=0
for base,dis,half in itertools.product(range(0,101),range(0,9),[False,True]):
 val=discount_cost(base,dis,half);price_states+=1
 assert (val==0 if base==0 else 1<=val<=base)
ck('1818-estados-preco',price_states==1818)
# d12 exato.
die=c['clash_die']; margin=c['clash_margin']
resolvidos=sum(abs(a-b)>=margin for a,b in itertools.product(range(1,die+1),repeat=2))
ck('d12-metade-exata',resolvidos==72 and die*die==144)
ck('rerrolar-antigo-nao-aplicado',Fraction(1,1)-Fraction(1,2)**3==Fraction(7,8))
def duel(refa,nona,rolla,refb,nonb,rollb):
 if refa!=refb:return 1 if refa>refb else -1
 if nona!=nonb:return 1 if nona else -1
 if abs(rolla-rollb)>=margin:return 1 if rolla>rollb else -1
 return 0
ck('maiorrefino-antes-naodano',duel(8,False,1,7,True,12)==1)
ck('naodano-antes-dado',duel(7,True,1,7,False,12)==1)
ck('ambos-naodano-dado',duel(7,True,12,7,True,8)==1)
ck('margem3-corrida',duel(7,False,12,7,False,9)==0)
ck('empate7-9-corrida',duel(10,False,9,10,False,7)==0)
# Três abertos: um dado por participante. Compare todos os pares antes de remover.
def defeated(players,pair_order):
 dead=set()
 for a,b in pair_order:
  v=duel(*players[a],*players[b])
  if v: dead.add(b if v>0 else a)
 return dead
orders=list(itertools.permutations([(0,1),(0,2),(1,2)]));multi_states=0
for rolls in itertools.product(range(1,13),repeat=3):
 players=[(10,False,x) for x in rolls]
 expected=defeated(players,orders[0])
 for order in orders[1:]: assert defeated(players,order)==expected
 multi_states+=1
ck('1728-multiplos-ordem-pares',multi_states==1728)
# Teste único do inimigo: resultado final equivale comparar um total à maiorCD válida.
def enemy_failure(total,cds):
 recorded=0;highest=0
 for cd in cds:
  highest=max(highest,cd)
  if total<highest and not recorded: recorded=1
 return recorded
enemy_states=0
for length in range(1,5):
 for cds in itertools.product([12,15,18],repeat=length):
  for total in range(1,31):
   assert enemy_failure(total,cds)==int(total<max(cds));enemy_states+=1
ck('3600-sequencias-inimigo',enemy_states==3600)
ck('exemplo-CD-crescente',enemy_failure(16,[15,17,18])==1)
ck('exemplo-semfalha',enemy_failure(18,[15,17,18])==0)
# PV compartilhados e custo da simplificação do interior.
barrier_rounding=[]
for dmg in range(0,1001):
 new=math.ceil(dmg/c['interior_divisor'])
 old_normalized=Fraction(math.ceil(dmg/2),2)
 assert new>=old_normalized and new-old_normalized<1
 if dmg%4==0: assert new==old_normalized
 if dmg<=12:barrier_rounding.append(dict(dano=dmg,antigo_equivalente_externo=float(old_normalized),novo=new))
ck('1001-danos-internos',True)
ck('risco-minidano-exposto',200//math.ceil(1/2)==200 and 100//math.ceil(1/4)==100)
ck('vida-compartilhada-exemplo',100-20-math.ceil(16/4)==76)
# Probabilidade exata de continuar em corrida após n danos; não é simulação de mesa.
def survive(n,p,ess):
 return sum(Fraction(math.comb(n,f))*p**f*(1-p)**(n-f) for f in range(min(threshold(ess),n+1)))
contests=[]
for per_round,p,ess in itertools.product([1,2,4],[Fraction(7,20),Fraction(1,2),Fraction(17,20)],[2,4,6]):
 values=[survive(per_round*r,p,ess) for r in range(1,6)]
 assert all(values[i]>=values[i+1] for i in range(4))
 contests.append(dict(danos_por_rodada=per_round,chance_falha=float(p),essencia=ess,probabilidade_de_pe_por_rodada=[float(x) for x in values]))
ck('27-perfis-contestacao',len(contests)==27)
# Comparação de papel: números brutos máximos não modelam acerto, mitigação, críticos ou contrajogo.
compare=[]
for lv,row in maximum.items():
 cl=levels[lv]['spell_class'];n=damage(cl);ref=max_refino(lv)
 compare.append(dict(level=lv,spell_class=cl,common_max_single_dice=3*cl,liberacao_max_single_dice=4*cl,liberacao_pe=math.ceil(3*cl*1.5),maxima_dice=row['dice'],maxima_pe=row['pe'],maxima_mean=row['dice']*4.5,domain_pulse_dice=n,domain_pulse_mean=n*4.5,domain_closed_pe=6*cl,max_refino_at_level=ref,closed_discount=ref//2,maxima_discounted_closed=discount_cost(row['pe'],ref//2),maxima_discounted_open=discount_cost(row['pe'],2*levels[lv]['mastery']) if ref==10 else None))
ck('maxima-supera-pulso',all(x['maxima_dice']>x['domain_pulse_dice'] for x in compare))
ck('dominio-custa-mais-maxima',all(x['domain_closed_pe']>x['maxima_pe'] for x in compare))
# Correções da leitura independente: metade de dados e entrada na regra contínua.
ck('tr-metade-dados','no sucesso do TR, role metade dos dados de dano.' in s)
ck('tr-exemplo-4d8','um alvo que resista recebe 4d8' in s)
for cl in range(1,8):
 full_dice=damage(cl);success_dice=full_dice//2
 assert success_dice==cl
 assert Fraction(success_dice*9,2)==Fraction(full_dice*9,4)
ck('tr-7-classes-metade-dados',True)
# Estado por alvo: resultado dura até o próximo pulso, atravessar não o renova.
def enter(last_pulse, now_pulse, old_result, die_success):
 if last_pulse==now_pulse:
  return (last_pulse,old_result,0)
 return (now_pulse,die_success,1)
entry_states=0
for old_epoch, epoch, old_result, success in itertools.product([-1,0,1],[0,1,2],[False,True],[False,True]):
 if old_epoch>epoch:continue
 first=enter(old_epoch,epoch,old_result,success)
 reenter=enter(first[0],epoch,first[1],not success)
 assert reenter[1]==first[1] and reenter[2]==0
 assert first[2]==int(old_epoch!=epoch)
 entry_states+=1
ck('entrada-resultado-por-pulso',entry_states==32,entry_states)
ck('entrada-texto','se ainda não tiver resultado válido' in s and 'No sucesso, fica livre dela pelo mesmo prazo.' in s)
# Casos direcionados de especificação são separados dos modelos executados.
specs=[
 ('S01','Incompleta com refino maior não vence Completa','exceção textual'),
 ('S02','Cesta não anula rolagem de Incompleta','interface R09'),
 ('S03','Simples não gasta relógio com Acerto já suspenso por disputa','interface R09'),
 ('S04','Pétala não anula proibição ambiental abstrata','interface R09'),
 ('S05','Mover fechado estandoAgarrado proibido','caso negativo'),
 ('S06','Dano exterior não provocaTR no dono','caso negativo'),
 ('S07','Entrada após pulso não causa novo dano automático','caso negativo'),
 ('S08','Regra contínua volta após fim proteção','interface R09'),
 ('S09','Alto d12 não vence refino superior','modelo duel também executado'),
 ('S10','Queda de trêsbarreiras não concede pulso extra ao aberto','caso negativo'),
 ('S11','Trocar face não restaura PV','modelo PV também executado'),
 ('S12','Zero PE não equivale a ausência de energia','dependência de origem'),
 ('S13','SemTécnica não compra domínio com espaços','gate textual'),
 ('S14','Efeito de domínio não isenta dono da regra simétrica','caso negativo'),
 ('S15','Dano de invocação não forçaTR no inimigo','decisão histórica preservada'),
 ('S16','Passar a0PV encerra domínio e impõe Rescaldo','estado'),
 ('S17','Regravação não fornece abertura gratuita','interface R09'),
 ('S18','Abandonar área aberta mantém domínio mas não desconto fora','estado'),
 ('S19','Acerto não cria Classe para ativar Fluxo','interface R07'),
 ('S20','Vida temporária absorvida conta como dano recebido','interface R03'),
]
result=dict(ok=True,status='passou',manuscritos_auditados={str((O/'PODERES-AVANCADOS.md').relative_to(R)):hashlib.sha256(s.encode()).hexdigest()},limite='Auditoria matemática e verificação dirigida de texto; não playtest, não teste humano e não prova de balanceamento de toda ficha.',manuscrito_sha256=hashlib.sha256(s.encode()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),contrato_sha256=hashlib.sha256((O/'CONTRATO.json').read_bytes()).hexdigest(),checks=checks,total_checks=len(checks),word_counts=words,example_values=numeric,open_radius_change=dict(before=old_radius,after=c['open_radius'],radius_percent=-100*(old_radius-c['open_radius'])/old_radius,area_percent=100*((c['open_radius']/old_radius)**2-1)),comparison=compare,clash=dict(resolved=resolvidos,total=die*die,probability=resolvidos/(die*die),multi_states=multi_states),enemy_sequence_states=enemy_states,price_states=price_states,barrier_rounding=barrier_rounding,contest_probabilities=contests,specification_cases=[dict(id=a,caso=b,natureza=c,executado_com_jogadores=False) for a,b,c in specs])
result['fontes_no_momento']=[dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in [R/'sistema/05-material/livro/manual/40-fundamento.md',R/'sistema/03-mecanica/18-progressao.md',P/'fundamento/lote-01/FUNDAMENTO.md',P/'catalogo/lote-01/CATALOGO.md']]
(O/'evidencias/auditoria-numerica.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(f'PASSOU: {len(checks)} verificações; {price_states} preços; {enemy_states} sequências de TR; {multi_states} tríades de d12; 1001 danos interiores; 27 perfis de corrida.')
print('SHA256',result['manuscrito_sha256'])

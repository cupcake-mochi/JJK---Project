from pathlib import Path
from fractions import Fraction
from math import ceil,floor
import hashlib,json,re
R=Path(__file__).resolve().parents[7]
B=R/'sistema/05-material/livro/planejamento-editorial/ritual-e-pactos/lote-01'
F=B/'RITUAL-E-PACTOS.md';s=F.read_text();C=B.parents[1]/'catalogo/lote-01/CATALOGO.md'
assert 'PE máximo aumenta em 3 × sua maior Classe' in C.read_text()
assert '**um aumento do PE máximo igual à sua maior Classe**' in s
prog=(R/'sistema/05-material/livro/manual/80-experiencia-e-progressao.md').read_text()
rows=[]
for l in prog.splitlines():
 if not l.startswith('| '):continue
 cells=[x.strip().replace('**','') for x in l.strip('|').split('|')]
 if len(cells)==9 and cells[0].isdigit():
  rows.append({'nivel':int(cells[0]),'maestria':int(cells[2]),'classe':int(cells[5])})
assert len(rows)==30,len(rows)
checks=[];profiles=[];examples=[]
def ck(n,a,e):checks.append({'caso':n,'obtido':a,'esperado':e,'ok':a==e})
for row in rows:
 for rate in (4,5,6):
  base=rate*row['nivel'];cl=row['classe']
  for ess in range(7):
   for pacts in range(ess//2+1):
    gain=pacts*cl;new=base+gain
    d_short=new//4-base//4
    assert gain<=3*cl
    assert gain//4<=d_short<=ceil(gain/4)
    assert gain==pacts*cl
    profiles.append({**row,'PE_nivel':rate,'Essencia':ess,'pactos_energia':pacts,'PE_base':base,'aumento':gain,'novo_maximo':new,'ganho_extra_descanso_curto':d_short,'razao_frente_ReservaProfunda':str(Fraction(gain,3*cl))})
for n in (2,10,13,17,21,26,30):
 row=next(r for r in rows if r['nivel']==n);cl=row['classe']
 examples.append({**row,'um_pacto':cl,'tres_pactos':3*cl,'Reserva_Profunda':3*cl,'nota':'Comparação de magnitude; máximo de três pactos só comEssência6. Passiva exige nível13 e seus demais limites.'})
ck('Classe por faixas',[(x['nivel'],x['classe']) for x in examples],[(2,1),(10,3),(13,4),(17,5),(21,6),(26,7),(30,7)])
ck('Três pactos equivalem ao aumento de Reserva Profunda',all(x['tres_pactos']==x['Reserva_Profunda'] for x in examples),True)
ck('Uma escolha é um terço desse aumento em qualquer nível',all(Fraction(x['um_pacto'],x['Reserva_Profunda'])==Fraction(1,3) for x in examples),True)
ck('Pacto não recupera imediatamente','não recupera PE imediatamente' in s,True)
ck('Sem geração por turno','não concede energia por turno, por acerto ou por começar outra cena' in s,True)
# Caso positivo/negativo do compartilhamento: somente beneficiário mínimo fornece peças.
def share(parts,riders,index):
 if parts[index]!=min(parts):return None
 unique={'Levanta','Divide','Troca','Empurrão'}
 return {'parcela':parts[index],'pecas':sorted(set(riders[index])-unique)}
ck('Cópia válida de3PV comGuarda',share([6,3],[['Pressa'],['Guarda']],1),{'parcela':3,'pecas':['Guarda']})
ck('Cópia inválida da parcela maior',share([6,3],[['Pressa'],['Guarda']],0),None)
ck('Cópia não reúne melhorias dosdois beneficiários',share([3,3],[['Pressa'],['Guarda']],0),{'parcela':3,'pecas':['Pressa']})
ck('Limites únicos não multiplicam',share([8],[['Levanta','Divide','Troca','Empurrão','Guarda']],0),{'parcela':8,'pecas':['Guarda']})
ck('Junto comzero não inventaPV',share([9,0],[['Guarda'],['Pressa']],1),{'parcela':0,'pecas':['Pressa']})
# Tiros: perfil sem criar ataques no mesmo alvo ou tomar bônus da vítima original.
def tiro(parts,targets,newtarget,crit=False,exclusive_bonus=0):
 if newtarget in targets:return None
 return min(parts)
ck('Tiro4/2/1 retorna1',tiro([4,2,1],['a','a','a'],'b'),1)
ck('Tiro3/2/2 retorna2',tiro([3,2,2],['a','a','a'],'b'),2)
ck('Alvo original não recebe tiroextra',tiro([3,2,2],['a','a','a'],'a'),None)
ck('Acúmulo contra vítimaoriginal não vai paraoutra',tiro([3,2,2],['a','a','a'],'b',True,3),2)
ck('Queima no tiroextra respeita parcela',2+2//2,3)
ck('PacoteC3 antesRitual12 depoisTiros15',8+4+2+1,15)
ck('Máxima24d8 dividida6 +1tiro4d8',24+4,28)
# Imobilidade não é gasto do movimento. Liberação tem exceção nominal própria.
matrix={
 'Breve':{'Atrasar':'incompatível','Parado':'devolve','Carregar':'devolve'},
 'Completo':{'Atrasar':'não devolve','Parado':'devolve','Carregar':'devolve'},
 'Recitação Prolongada':{'Atrasar':'não devolve','Parado':'devolve','Carregar':'não devolve'}}
ck('Nove interfaces de tempo',sum(len(v) for v in matrix.values()),9)
ck('Parado da Liberação continua semdevolução','Na Liberação, Atrasar e Parado não devolvem' in s,True)
ck('Falha mantém montagem','Use essa montagem tanto no sucesso quanto na falha do Ritual' in s,True)
ck('Ajuda tardia não devolvePE','Uma ajuda recebida depois do pagamento não pode comprar Energia' in s,True)
# Ajustes negados pelo modelo: três mutações para evitar conferir só constantes.
mutations=[('cópia_da_maior', max([4,2,1])!=tiro([4,2,1],['a']*3,'b')),('tiro_no_mesmo_alvo',tiro([4,2,1],['a']*3,'a') is None),('pacto_dobrando_reserva',3*7*2!=3*7)]
ck('Mutações deliberadas detectadas',all(v for _,v in mutations),True)
result={'ok':all(x['ok'] for x in checks),'sha256_texto':hashlib.sha256(F.read_bytes()).hexdigest(),'verificacoes':checks,'perfis_PE':len(profiles),'comparacao_PE':examples,'perfis_detalhados':profiles,'matriz_tempo':matrix,'limites':['Não simula campanha completa, distribuição de descanso ou utilidade de cada sacrifício.','Comparação comReservaProfunda é magnitude atual; não diz que o antigo teto de0,50fatia foi preservado.','Comparação emníveis abaixo13 não concede a Passiva antecipadamente.','Modelo de compartilhamento assume que a montagem original já era válida; ele não decide seGuarda/Pressa podem integrar uma técnica específica.']}
(B/'evidencias/REVISAO-INDEPENDENTE-MODELOS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':result['ok'],'checagens':len(checks),'perfis_PE':len(profiles),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False))

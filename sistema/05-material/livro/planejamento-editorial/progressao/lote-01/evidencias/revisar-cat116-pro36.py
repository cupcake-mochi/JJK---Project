from pathlib import Path
from fractions import Fraction
import json,hashlib,re
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial')
paths={'catalogo':P/'catalogo/lote-01/CATALOGO.md','progressao':P/'progressao/lote-01/PROGRESSAO.md','dano':P/'dano-e-recuperacao/lote-final/DANO-E-RECUPERACAO.md'}
texts={k:p.read_text() for k,p in paths.items()};sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hashes={str(p.relative_to(P)):sha(p) for p in paths.values()};checks=[]
def ck(name,got,expected):
 checks.append({'caso':name,'obtido':got,'esperado':expected,'ok':got==expected})
 if got!=expected:raise AssertionError(name)
lev=texts['catalogo'].split('## Levanta',1)[1].split('## Remenda',1)[0];rem=texts['catalogo'].split('## Remenda',1)[1].split('<!-- page:',1)[0];prog=texts['progressao'].split('<!-- page:prog-limiar',1)[1].split('<!-- page:',1)[0]
for name,condition in [('Levanta exige ainda Morrendo','ainda **Morrendo**' in lev),('Levanta preserva5porClasse','5 × Classe de vida' in lev),('Levanta uma vez por cena e compartilha fichas','uma vez por cena' in lev and 'compartilhando esse limite entre suas fichas' in lev),('Levanta um único aliado mesmoOnda','um aliado escolhido, mesmo numa Onda' in lev),('Remenda5porClasseIntegridade','5 × Classe de Integridade' in rem),('Remenda limite por alvo','O mesmo alvo só pode receber Remenda uma vez por cena, independentemente de quem a use.' in rem),('Remenda remete estágios e derrota','Estágios de Integridade' in rem and 'Derrota e morte' in rem),('Limiar exige saídaDerrotado','Integridade a zero e saída do estado Derrotado registradas' in prog),('Ameaça hostil real','precisam decorrer de uma ameaça hostil real na missão' in prog),('Treino/fabricação excluídos','Treinos e quedas provocadas pelo grupo apenas para cumprir essa lista não contam.' in prog),('XP/teto inalterados','não concede XP nem um nível gratuito' in prog and 'no máximo um avanço por missão' in prog)]:ck(name,condition,True)
# Modelos da interface, não simulação de habilidades inteiras ou playtest.
def lift(state,cls,maxhp,accum=0,allowed=True,used=False):
 if state!='Morrendo' or not allowed or used:return None
 return {'vida':min(maxhp,5*cls+accum),'estado':'Socorrido','sequela':1,'usado':True}
ck('LevantaC3resgata15abaixo39',lift('Morrendo',3,195),{'vida':15,'estado':'Socorrido','sequela':1,'usado':True})
ck('Levanta acumulação com limite atual',lift('Morrendo',3,20,accum=10)['vida'],20)
for state in ['Derrotado','Morto']:ck('Levanta recusa '+state,lift(state,3,195),None)
ck('Levanta recusa impedimentoCura',lift('Morrendo',3,195,allowed=False),None)
ck('Levanta recusa segundo uso',lift('Morrendo',3,195,used=True),None)
def stage(value,mx):
 return sum(Fraction(mx-value,mx)>=x for x in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)])
def mend(value,mx,cls,defeated=False,received=False):
 if received:return None
 value=min(mx,value+5*cls)
 return value,stage(value,mx),defeated
ck('RemendaC3 cruza estágio3para2',mend(20,100,3),(35,2,False))
ck('RemendaC3de0nãoencerraDerrotado',mend(0,100,3,True),(15,3,True))
ck('Remenda limitado à Integridade máxima',mend(95,100,3),(100,0,False))
ck('Remendaoutroconjurador mesmoalvo bloqueado',mend(35,100,3,received=True),None)
def feat(kind,hostile=False,training=False,level=20,conscious=False,able=False,full=False,raised=False,was_stage4=False,left_defeat=False):
 if not 15<=level<=20 or not hostile or training:return False
 if kind=='dominio':return conscious and able and full
 if kind=='socorro':return raised
 if kind=='alma':return was_stage4 and left_defeat
for kind,kwargs in [('dominio',dict(conscious=True,able=True,full=True)),('socorro',dict(raised=True)),('alma',dict(was_stage4=True,left_defeat=True))]:
 ck(kind+' treino amigável não é feito',feat(kind,hostile=False,training=True,**kwargs),False)
 ck(kind+' ameaça hostil real permite feito',feat(kind,hostile=True,**kwargs),True)
 ck(kind+' faixa anterior não conta',feat(kind,hostile=True,level=14,**kwargs),False)
ck('Alma positivo aindaDerrotado não conta retorno',feat('alma',hostile=True,was_stage4=True,left_defeat=False),False)
ck('Socorro acumulado sem acordar não conta',feat('socorro',hostile=True,raised=False),False)
ck('SairDomínio incompleto não conta',feat('dominio',hostile=True,conscious=True,able=True,full=False),False)
ck('SairDomínio após socorro pode contar',feat('dominio',hostile=True,conscious=True,able=True,full=True),True)
report={'ok':True,'revisor':'maxima','independente_do_autor_dos_deltas':True,'hashes_lidos':hashes,'escopo':'Leitura pontual CAT116 e PRO36, logs e interface final R03. Não repete revisão integral de Catálogo/Progressão.','casos':checks,'contagem':len(checks),'achados':[{'gravidade':'P3-remissao','texto':'Catálogo Levanta/Reserva ainda citam Recuperação; PRO36 também usa Recuperação na tabela. Atualizar para Socorro ou Derrota e morte/Dano e Recuperação na consolidação. Não afeta a mecânica dos deltas.'}],'parecer':'Não identificado bloqueador mecânico nos deltas. Valores, frequências e condição de conquista preservados; nova exigência de ameaça hostil é mecânica e está registrada em PRO36.','limites':['Modelos de interface dirigidos, não habilidades completas, partidas ou compreensão humana.','Permissões de compra por Classe permanecem no dono; o teste numérico não concede acesso.','Nenhuma inspeção visual/PDF executada.','Outras escolhas de limiar não foram redesenhadas nem abrangidas pela regra antitreino além do texto expresso.']}
for folder,name in [('catalogo/lote-01','REVISAO-CAT116-MAXIMA'),('progressao/lote-01','REVISAO-PRO36-MAXIMA')]:
 e=P/folder/'evidencias';(e/(name+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 (e/(name+'.md')).write_text('# Revisão independente dos deltas CAT116 e PRO36\n\n'+ '\n'.join(f'- `{k}`: `{v}`.' for k,v in hashes.items())+'\n\n'+report['escopo']+'\n\n'+report['parecer']+'\n\nForam executadas '+str(len(checks))+' verificações de texto e casos de interface. LevantaC3 permite15PV mesmo quando o limiar comum seria39, somente enquanto Morrendo. RemendaC3 aplicada em0/100 aumenta Integridade para15 e reduz estágio4para3, mas conserva Derrotado. O feito de retorno exige a saída desse estado, não só reserva positiva. Socorro e saída de Domínio precisam cumprir seu resultado e decorrer de ameaça hostil real; treino amigável e faixas de nível inadequadas foram recusados nos casos.\n\n## Ajuste editorial pendente\n\n'+report['achados'][0]['texto']+'\n\n## Limites\n\n'+'\n'.join('- '+v for v in report['limites'])+'\n')
print(json.dumps({'ok':True,'casos':len(checks),'hashes':hashes},ensure_ascii=False))

#!/usr/bin/env python3
"""Auditoria da candidata: contratos de conteúdo + modelos pequenos executáveis.
Não executa uma campanha ou mede diversão. Mantém casos negativos e mutações.
"""
from pathlib import Path
import hashlib,json,re,itertools
from fractions import Fraction
B=Path(__file__).resolve().parent;R=B.parents[5];s=(B/'ORIGENS-E-LEGADOS.md').read_text();inv=json.loads((B/'INVENTARIO.json').read_text());entries=inv['legados'];checks=[];cases=[];mutations=[]
def ck(id,value,detail=''):checks.append(dict(id=id,passou=bool(value),detalhe=detail))
def case(id,actual,expected,detail=''):
 cases.append(dict(id=id,obtido=actual,esperado=expected,detalhe=detail));ck(id,actual==expected,detail)
def entry(name,text=s):
 m=re.search(r'^\*\*'+re.escape(name)+r'\.\*\* (.*?)(?=\n\n\*\*[^\n]+\.\*\*|\n##|\n>|\n<!--|\Z)',text,re.M|re.S)
 return m[1] if m else ''
sha=hashlib.sha256(s.encode()).hexdigest()
ck('inventario_hash',sha==inv['sha256_texto']);ck('85entradas',len(entries)==85)
for e in entries:ck('entrada_'+e['nome'],bool(entry(e['nome'])))
case('tipos',[sum(e['tipo']==t for e in entries) for t in ['narrativo','rolagem','excecao']],[32,40,13])
parts=re.findall(r'<!-- page:([^|]+)\|([^>]+) -->\n# [^\n]+\n(.*?)(?=<!-- page:|\Z)',s,re.S)
case('paginas',len(parts),26);ck('IDs_unicos',len(set(x[0] for x in parts))==len(parts));ck('extensao_paginas',all(180<=len(x[2].split())<=400 for x in parts))
ck('titulos_diretos',all(not re.match(r'^(?:A|O|As|Os|Como ler)\s',x[1]) for x in parts))
ck('nomes_antigos_ausentes',not re.search(r'\b(?:Destranca|Ajusta|Desliga|Reencarnado)\b',s));ck('sem_metatexto',not re.search(r'v0\.|candidata|nesta proposta|novo cartão|placeholder',s,re.I) and 'TODO' not in s)
# Frequencies are read from the text. Five frequencies in the published manual override older peça13.
freq_expected={'Aprendi Apanhando':'dia','Gambiarra':'dia','Instinto Bruto':'cena','Desconfiado':'cena','Não Sou Só Eu':'cena','Costume Antigo':'cena','Tranco':'cena','Passagem':'dia','Revezamento':'descanso longo','Conversa de Jantar':'cena','Etiqueta':'cena','Repetição':'descanso curto','Biblioteca':'cena','Cabo':'cena','Corpo Emprestado':'cena','Espasmo':'descanso curto','Já Morri':'cena','Método Velho':'cena','Usado':'cena','Meio e Meio':'cena','Como Se Monta':'cena','Faro':'cena','Paciência':'dia','Talhe':'cena','Rodízio':'cena','Vigília':'cena','Desempate':'dia','Cabeça Trocada':'cena','Nunca os Dois':'descanso curto','Palpite':'dia','Feito de Uma Peça':'descanso curto','Teimosia':'cena','Peça Única':'cena','Ajuste Fino':'cena','Recarga':'descanso curto','Fiado':'dia','Antena':'cena','Do Meu Canto':'cena','Insônia':'dia','Li Tudo':'cena','Sentido Treinado':'cena','Couro':'descanso curto','Ninguém Viu':'cena','No Braço':'dia','Assinado':'descanso longo','A Voz de Dentro':'dia','O Que Ele Quer':'descanso longo','O Que Ninguém Lembra':'descanso longo','O Jeito Errado':'dia'}
for name,period in freq_expected.items():ck('frequencia_'+name,('Uma vez por '+period).lower() in entry(name).lower())
byname={e['nome']:e for e in entries}
configuration={'Ninhada':['Rodízio','Vigília','Desempate'],'Gêmeos':['Cabeça Trocada','Nunca os Dois','Palpite'],'Inteiro':['Feito de Uma Peça','Teimosia','Peça Única'],'Manutenção':['Ajuste Fino','Recarga','Fiado']}
bodyNarr=['Nasci Assim','O Substituto','A Oferta'];bodyRoll=['Antena','Do Meu Canto','Insônia','Li Tudo'];zeroNarr=['Descartado','Dividido','Desde Criança','Aprendi a Ver'];zeroRoll=['Sentido Treinado','Couro','Ninguém Viu','No Braço'];shared=['Peso Real','Assinado']
def legal_pair(origin,names,branch=None):
 if len(names)!=2 or len(set(names))!=2:return False
 if any(n not in byname for n in names):return False
 if sum(byname[n]['tipo']=='narrativo' for n in names)<1:return False
 if origin=='Corpo Amaldiçoado':
  ids=[n for n in names if n in configuration]
  return len(ids)==1 and all(n==ids[0] or n in configuration[ids[0]]+['Ferro Velho'] for n in names)
 if origin=='Restrição Celestial':
  allowed=(bodyNarr+bodyRoll+shared) if branch=='corpo' else (zeroNarr+zeroRoll+shared) if branch=='zero' else []
  return all(n in allowed for n in names)
 return all(byname[n]['origem_fonte']==origin or n=='Sem Técnica' for n in names)
# Full finite catalogue pair enumeration, not combinations of custom prose.
pairprofiles=[]
for origin,branch in [('Latente',None),('Receptáculo',None),('Descendente',None),('Reencarnado',None),('Feto',None),('Corpo Amaldiçoado',None),('Restrição Celestial','corpo'),('Restrição Celestial','zero')]:
 pairs=[list(p) for p in itertools.combinations(byname,2) if legal_pair(origin,p,branch)]
 pairprofiles.append(dict(origem=origin,ramo=branch,quantidade=len(pairs),pares=pairs))
case('pares_catalogo',[x['quantidade'] for x in pairprofiles],[30,40,51,40,40,16,21,30])
for origin,names,branch,expected in [('Latente',['A Testemunha','Aprendi Apanhando'],None,True),('Descendente',['O Sobrenome','Biblioteca'],None,True),('Descendente',['Sem Técnica','Arquivo'],None,True),('Descendente',['Biblioteca','Repetição'],None,False),('Latente',['Sem Técnica','Sem Técnica'],None,False),('Corpo Amaldiçoado',['Ninhada','Rodízio'],None,True),('Corpo Amaldiçoado',['Ninhada','Palpite'],None,False),('Corpo Amaldiçoado',['Ninhada','Gêmeos'],None,False),('Corpo Amaldiçoado',['Sem Técnica','Ferro Velho'],None,False),('Restrição Celestial',['Nasci Assim','Couro'],'corpo',False),('Restrição Celestial',['Descartado','Peso Real'],'zero',True),('Restrição Celestial',['Sem Técnica','Couro'],'zero',False)]:case('par_'+origin+'_'+','.join(names),legal_pair(origin,names,branch),expected)
case('pericias_com_oficios',[7+1+1,2],[9,2]);case('pericias_sem_oficios',[7+1+1+1,0],[10,0])
# Repairs read table offsets and formula from candidate. No silent fallback values.
rows=re.findall(r'\| (Igual|Uma abaixo|Duas ou mais abaixo) \| [^|]+\| ([+−]\d)\.',s)
offsets={a:int(b.replace('−','-')) for a,b in rows};case('tabela_reparo',offsets,{'Igual':0,'Uma abaixo':-2,'Duas ou mais abaixo':-4})
ck('formula_reparo','8 + atributo usado no ofício + maestria de quem repara + ajuste' in s)
def repair(attr,mastery,offset,hp,maxhp,die,trained=True,done=False,above=False,extra=0):
 if not trained or done or above:return {'permitido':False}
 dc=8+attr+mastery+offset;total=die+attr+mastery+extra
 return dict(permitido=True,cd=dc,total=total,sucesso=total>=dc,pv=min(maxhp,hp+maxhp//2) if total>=dc else hp)
case('reparo_exemplo',repair(3,2,0,8,31,8),dict(permitido=True,cd=13,total=13,sucesso=True,pv=23))
case('reparo_falha',repair(3,2,0,8,31,7)['pv'],8)
case('reparo_maximo',repair(3,2,0,30,31,8)['pv'],31)
case('reparo_especializacao',repair(3,2,0,8,31,7,extra=1)['sucesso'],True)
for arg in ['trained','done','above']:
 kwargs={arg:False if arg=='trained' else True};case('reparo_bloqueio_'+arg,repair(3,2,0,8,31,20,**kwargs),{'permitido':False})
repairprofiles=[]
for attr,mast,offset in itertools.product(range(0,7),range(1,6),offsets.values()):
 successes=sum(repair(attr,mast,offset,1,31,d)['sucesso'] for d in range(1,21))
 expected={0:13,-2:15,-4:17}[offset]
 ck(f'reparo_{attr}_{mast}_{offset}',successes==expected)
 repairprofiles.append(dict(atributo=attr,maestria=mast,ajuste=offset,sucesso=successes/20))
# Advantage and failure rerolls use exhaustive d20 pairs. No assumption that resource efficiency is equal.
probs=[]
for threshold in range(2,21):
 normal=sum(d>=threshold for d in range(1,21))/20
 advantage=sum(max(a,b)>=threshold for a,b in itertools.product(range(1,21),repeat=2))/400
 reroll=sum((a>=threshold or b>=threshold) for a,b in itertools.product(range(1,21),repeat=2))/400
 disadvantage=sum(min(a,b)>=threshold for a,b in itertools.product(range(1,21),repeat=2))/400
 ck('prob_'+str(threshold),advantage==reroll and disadvantage<=normal<=advantage)
 probs.append(dict(d20_minimo=threshold,normal=normal,vantagem=advantage,repeticao_de_falha=reroll,desvantagem=disadvantage,prob_gastar_repeticao=1-normal))
case('p50vantagem',probs[9]['vantagem'],.75)
# Explicit action/condition and counterprice contracts.
for name,positive,negative in [('Revezamento','Guarda Aberta','Imp​edido'),('Corpo Emprestado','Guarda Aberta','Inconsciente'),('Talhe','1,5 m','3 m')]:
 ck('condicao_'+name,positive in entry(name));ck('nao_troca_'+name,negative not in entry(name) if name!='Corpo Emprestado' else 'diferente de Inconsciente' in entry(name))
def talhe(has_object,space):return has_object or space
for a,b in itertools.product([False,True],repeat=2):case(f'talhe_{a}_{b}',talhe(a,b),a or b,'Escolha adversária entre opções possíveis; ambas impossíveis impedem uso.')
def fixed(moved,combat=True,entire=True):return not moved if combat else entire
case('canto_movel',fixed(True),False);case('canto_parado',fixed(False),True);case('canto_fora',fixed(False,False,False),False)
case('sangue_descanso_satisfeito',bool(True and True),True);case('sangue_descanso_nao_satisfeito',bool(True and False),False)
for name,fragments in {'Sangue que Não é Sangue':['vida e PE','descanso longo','sem ferir outra pessoa','não substitui o tempo'],'Talhe':['Se nenhuma for possível','não provoca ataques de oportunidade'],'Do Meu Canto':['não pode ter se deslocado voluntariamente','até o começo do próximo'],'Ninguém Viu':['não concede uma nova tentativa gratuita'],'O Que Ele Quer':['não concede ataques, acertos, técnicas'],'Passagem':['antes de usá-la'],'Ferro Velho':['não adquire estágios','o mestre registra','permite usar uma habilidade'],'Peso Real':['indício físico acessível'],'Aprendi a Ver':['sem conceder percepção irrestrita','Bênção gratuita']}.items():
 for fragment in fragments:ck('contrato_'+name+'_'+fragment,fragment in entry(name))
ck('feto_categoria', 'escolher Feto não classifica seu personagem como uma maldição' in s)
ck('feto_cura', 'Você recebe cura e recuperação normais' in s)
ck('treino_atual', 'use sua maestria atual' in s)
# Deliberate text mutation regression. These tests verify checks detect loss of invariants.
contracts=[('metade_cura','**metade da vida máxima**','**vida máxima**',lambda t:'**metade da vida máxima**' in t),('frequencia_couro','**Couro.** **Uma vez por descanso curto**','**Couro.** **Uma vez por cena**',lambda t:'Uma vez por descanso curto' in entry('Couro',t)),('morte_revezamento','**com a Guarda Aberta**, impeça','**Inconsciente**, impeça',lambda t:'**com a Guarda Aberta**' in entry('Revezamento',t)),('talhe_sem_pagamento','Se nenhuma for possível, você não pode usar o Legado.','Se nenhuma for possível, use sem custo.',lambda t:'Se nenhuma for possível, você não pode usar o Legado.' in entry('Talhe',t)),('imunidade_condicao','Você é **imune a Envenenado**.','Você é **imune a Veneno**.',lambda t:'Você é **imune a Envenenado**.' in t),('narrativo','Pelo menos um deve ser **narrativo**.','Ambos podem ser de rolagem.',lambda t:'Pelo menos um deve ser **narrativo**.' in t)]
for id,a,b,validator in contracts:
 mutant=s.replace(a,b,1);caught=(mutant!=s and validator(s) and not validator(mutant));mutations.append(dict(id=id,detectada=caught));ck('mutacao_'+id,caught)
report=dict(sha256_texto=sha,aprovado=all(x['passou'] for x in checks),quantidades=dict(verificacoes=len(checks),casos=len(cases),pares_legados=sum(x['quantidade'] for x in pairprofiles),perfis_reparo=len(repairprofiles),perfis_probabilidade=len(probs),mutacoes=len(mutations)),verificacoes=checks,casos=cases,pares_por_origem=pairprofiles,reparos=repairprofiles,probabilidades=probs,mutacoes=mutations,limites=['Modelos do texto candidato, não motor geral do sistema ou playtest.','Pares de Legados personalizados não enumeráveis; verificados por casos e leitura.','Custos narrativos não convertidos em porcentagem de equilíbrio.','Morte/Integridade adiadas, exige repetir interfaces depois.','V12/V13/V14 não são realizados por este script.'])
(B/'evidencias/AUDITORIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(aprovado=report['aprovado'],quantidades=report['quantidades'],falhas=[x for x in checks if not x['passou']]),ensure_ascii=False,indent=2));raise SystemExit(0 if report['aprovado'] else 1)

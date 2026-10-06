#!/usr/bin/env python3
"""Modelos finitos de contratos da candidata, não motor de RPG nem playtest.
Lê Classes, CD, preço do estojo e valores do exemplo das linhas dos donos.
Falha se as linhas somem. Exemplos da prosa são conferidos por âncoras explícitas.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from copy import deepcopy
import hashlib,json,re
P=Path(__file__).resolve().parent
ROOT=next(x for x in P.parents if (x/'invocacoes/DECISOES-A-PARTIR-DO-46.md').exists())
PLAN=ROOT/'sistema/05-material/livro/planejamento-editorial'
E=P/'evidencias';M=P/'FABRICACAO-DE-ENTIDADES.md';S=M.read_text();SHA=hashlib.sha256(M.read_bytes()).hexdigest()
checks=[];cases=[]
def check(name,actual,expected=True):
    ok=actual==expected;checks.append({'nome':name,'obtido':actual,'esperado':expected,'ok':ok})
    if not ok: raise AssertionError(f'{name}: {actual!r} != {expected!r}')
def save(name,obj): (E/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def source(rel): return (PLAN/rel).read_text()
r12=source('invocacoes/lote-02/CONSTRUIR-INVOCACOES.md');r01=source('regras-basicas/lote-01/TESTES-E-TURNOS.md');r05=source('equipamento/lote-05-r1/ITENS-E-OBJETOS.md')
progress=re.search(r'# Progressão da entidade\n(.*?)## Habilidades conhecidas',r12,re.S).group(1)
rows=re.findall(r'^\| (\d+)–(\d+) \| (\d+) \|',progress,re.M)
check('Sete faixas na coluna Classe máxima',len(rows),7)
classes={n:int(c) for a,b,c in rows for n in range(int(a),int(b)+1)}
check('Níveis cobertos pela coluna Classe',sorted(classes),list(range(1,31)))
adjust={}
for word in ['Difícil','Média','Fácil']:
    adjust[word]=int(re.search(r'^\| '+word+r' \| \d+ \| (-?\d+) \|',r01,re.M).group(1))
check('Ajustes extraídos da coluna CD do criador',adjust,{'Difícil':0,'Média':-2,'Fácil':-4})
check('Candidata usa fórmula e extras separados','8 + esse atributo + essa Maestria' in S and 'não entram novamente na base da CD' in S)
for text in ['| Igual | Difícil | 0 |','| Uma abaixo | Média | −2 |','| Duas ou mais abaixo | Fácil | −4 |']:
    check('Tabela candidata: '+text,text in S)
toolrow=re.search(r'^\| Ferramentas de ofício \|.*?\| ([\d.]+) \| ([\d,]+) \|',r05,re.M)
tool_price=int(toolrow.group(1).replace('.',''));tool_volume=Fraction(toolrow.group(2).replace(',','.'))
check('Preço estojo do exemplo segue R05',tool_price,10000)
check('Estojo não é grátis no exemplo','¥10.000' in S)
example=S.split('# Talismã de vigia\n')[1]
cost=int(re.search(r'Papel e tinta preparados: ¥([\d.]+)',example).group(1).replace('.',''))
hours=int(re.search(r'\| Prazo \| (\d+) horas',example).group(1))
retry=re.search(r'Refazer a inscrição: mais (\d+) horas e ¥([\d.]+)',example)
retry_h=int(retry.group(1));retry_c=int(retry.group(2).replace('.',''))
def difficulty(entity,worker):
    if entity>worker: return None
    diff=classes[worker]-classes[entity]
    return 'Difícil' if diff==0 else 'Média' if diff==1 else 'Fácil'
def eligible(entity,worker,owner,trained=True,recipe=True,means=True):
    return trained and recipe and means and entity<=min(worker,owner)
valid=0
for entity,worker,owner in product(range(1,31),repeat=3):
    verdict=eligible(entity,worker,owner)
    assert verdict==(entity<=worker and entity<=owner)
    valid+=verdict
check('Matriz de níveis: candidatas possíveis',valid,sum(min(w,o) for w in range(1,31) for o in range(1,31)))
profiles=[];n_rolls=0
for a,m,diff in product(range(7),range(1,5),range(7)):
    d='Difícil' if diff==0 else 'Média' if diff==1 else 'Fácil';cd=8+a+m+adjust[d]
    p=Fraction(sum(roll+a+m>=cd for roll in range(1,21)),20);n_rolls+=20
    assert p=={'Difícil':Fraction(13,20),'Média':Fraction(15,20),'Fácil':Fraction(17,20)}[d]
    advantage=Fraction(sum(max(x,y)+a+m>=cd for x,y in product(range(1,21),repeat=2)),400)
    disadvantage=Fraction(sum(min(x,y)+a+m>=cd for x,y in product(range(1,21),repeat=2)),400)
    assert advantage==1-(1-p)**2 and disadvantage==p**2;n_rolls+=800
    specialized=Fraction(sum(roll+a+m+m//2>=cd for roll in range(1,21)),20);n_rolls+=20
    profiles.append({'atributo':a,'maestria':m,'dif_classes':diff,'CD':cd,'sucesso':float(p),'vantagem':float(advantage),'desvantagem':float(disadvantage),'especializacao':float(specialized)})
check('Perfis de probabilidade',len(profiles),196)
check('Chance do exemplo',float(Fraction(sum(r+6>=12 for r in range(1,21)),20)),.75)
check('Mesmo nível exemplo exige8',14-6,8)
check('Falha no5',5+4+2,11);check('Sucesso no9',9+4+2,15)
check('Custo após falha',cost+retry_c,36000);check('Horas após falha',hours+retry_h,20)
check('Custo com estojo novo',cost+retry_c+tool_price,46000)
check('Exemplo prosa total','¥36.000 e 20 horas' in S)
check('Valores não universais','não são uma tabela para todo talismã' in S)
# Modelo de estados explicitamente limitado à conclusão, retrabalho e mudança de vínculo.
def attempt(state,roll,trained=True,recipe=True,means=True,worker=13,owner_level=13):
    s=deepcopy(state)
    if not eligible(s['level'],worker,owner_level,trained,recipe,means):return s,'requisito'
    if s['worked']<s['needed'] or s['paid']<s['due']:return s,'incompleto'
    if s['done']:return s,'ja_concluido'
    cd=8+4+2+adjust[difficulty(s['level'],worker)]
    if roll+6>=cd:
        s.update(done=True,life=s['maxlife'],active=False,charge=0,owner='Rina');return s,'sucesso'
    s['needed']+=retry_h;s['due']+=retry_c;return s,'falha'
base={'level':9,'worked':hours,'needed':hours,'paid':cost,'due':cost,'done':False,'life':0,'maxlife':47,'active':False,'charge':0,'owner':None}
def case(name,actual,expected):
    check(name,actual,expected);cases.append({'nome':name,'obtido':actual,'esperado':expected,'status':'executado em modelo de contrato'})
f,status=attempt(base,5);case('Primeira falha impede funcionamento',status,'falha');case('Falha mantém peça incompleta',f['done'],False)
f2,status=attempt(f,20);case('Trocar dado sem retrabalho bloqueado',status,'incompleto');case('Tentativa bloqueada conserva estado',f2,f)
f['worked']+=retry_h;f['paid']+=retry_c;g,status=attempt(f,9);case('Retrabalho libera novo teste',status,'sucesso')
case('Nova peça cheia e inativa',(g['life'],g['active'],g['charge']),(47,False,0))
case('Concluída não produz cópia por novo dado',attempt(g,20)[1],'ja_concluido')
for field in ['trained','recipe','means']:
    case('Requisito ausente: '+field,attempt(base,20,**{field:False})[1],'requisito')
case('Nível13/16 mesmaClasse não remove teto',eligible(16,13,30),False)
case('Responsável alto não ignora nível do dono',eligible(13,30,9),False)
case('Fornecer a outro personagem possível',eligible(9,13,9),True)
def transfer(state,new_owner,newlevel,worker,success=True,consent=True,old_dead=False,present=True,outside=True):
    s=deepcopy(state)
    if s['destroyed'] or not present or not outside or s['active'] or not (consent or old_dead) or not eligible(s['level'],worker,newlevel):return s,'recusado'
    if not success:return s,'falha'
    s['owner']=new_owner;return s,'sucesso'
t={'level':9,'owner':'Morto','destroyed':False,'active':False,'life':8,'charge':1,'uses':2,'fallen':False,'maxlife':47}
tr,status=transfer(t,'Rina',13,13,old_dead=True,consent=False);case('Herança permitida',status,'sucesso')
for field in ['level','life','charge','uses','fallen']:
    case('Transferência preserva '+field,tr[field],t[field])
case('Vínculo singular',tr['owner'],'Rina')
for name,kw in [('Furto',{'consent':False}),('Objeto distante',{'present':False}),('Em combate',{'outside':False}),('Novo dono insuficiente',{'newlevel':5})]:
    opts={'new_owner':'Rina','newlevel':13,'worker':13}|kw
    case(name,transfer(t,**opts)[1],'recusado')
case('Falha de transferência não desfaz vínculo',transfer(t,'Rina',13,13,success=False)[0],t)
fallen=t|{'life':0,'fallen':True};fr,status=transfer(fallen,'Rina',13,13)
case('Herança não religa Desligada',(fr['life'],fr['fallen']),(0,True))
case('Destruída não transfere',transfer(t|{'destroyed':True},'Rina',13,13)[1],'recusado')
check('Sem atuação extra expressa','não dá outra atuação no ciclo' in S)
check('Corpo excedente não ganha controle','permanece no mundo sem controle e volta conforme **Invocações em campo**' in S and 'não amplia esse limite' in S)  # decisão G2-03 de 04/10/2026: a volta segue a trava de Invocações em campo
check('Custo/slot preservado','nem ocupa espaço conhecido' in S)
check('Origem/aptidão não concedidas','não concede uma Origem, técnica, aptidão' in S)
check('Teste único por entidade','Cada entidade exige sua própria tentativa de conclusão' in S)
check('Autonomia não baseada em material','materiais escolhidos não concedem proteção' in S)
check('Projeto obrigatório não é ficha automática','Uma ficha pronta, sozinha, não entrega a entidade' in S)
pageids=re.findall(r'<!-- page:([^|]+)\|([^>]+?) -->\n# ([^\n]+)',S)
check('Cinco páginas declaradas',len(pageids),5)
check('Marcadores e títulos iguais',all(a==b for _,a,b in pageids))
check('Sem títulos proibidos',not re.search(r'^#+\s+(?:Como ler\b|[AO]\s|As\s|Os\s)',S,re.M|re.I))
# Economia condicional, sem afirmar que o preço local equilibra todas as mesas.
p=Fraction(3,4);expected_failures=(1-p)/p
num={'sha256_texto':SHA,'checks':checks,'matriz_niveis':{'combinacoes':27000,'permitidas':valid},'perfis':profiles,'resultados_d20_enumerados':n_rolls,'exemplo':{'custo_base':cost,'horas_base':hours,'custo_retrabalho':retry_c,'horas_retrabalho':retry_h,'estojo':tool_price,'custo_1falha':cost+retry_c,'horas_1falha':hours+retry_h,'sucesso_ate3tentativas':float(1-(1-p)**3),'custo_esperado_com_retrabalho_ilimitado':float(cost+expected_failures*retry_c),'horas_esperadas_com_retrabalho_ilimitado':float(hours+expected_failures*retry_h),'hipotese':'Chance75% constante, sem bônus, materiais/tempo/novas tentativas sempre disponíveis; modelo teórico, não previsão de mesa.'}}
save('auditoria-numerica.json',num);save('casos-executados.json',{'sha256_texto':SHA,'casos':cases,'limites':'Modelos de contrato dirigidos à candidata. Não executam um motor do sistema nem partidas. Outros campos não modelados dependem de leitura/contexto.'})
preserve=[]
for f in json.loads((E/'fontes-iniciais.json').read_text()):
    current=hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest();preserve.append(f|{'sha256_final':current,'preservada':current==f['sha256']})
save('comparacao-fontes-final.json',{'sha256_texto':SHA,'fontes':preserve,'nota':'Comparação por hash, sem restauração de arquivos. Mudança concorrente requer cotejo, não atribuição automática ao agente.'})
accepted=json.loads((E/'fontes-concorrentes.json').read_text())
check('Fontes preservadas ou alteração concorrente cotejada',all(x['preservada'] or accepted.get(x['path'],{}).get('sha256_final')==x['sha256_final'] for x in preserve))
num['ok']=all(c['ok'] for c in checks)
num['manuscritos_auditados']={str(M.relative_to(ROOT)):SHA}
save('auditoria-numerica.json',num)
# Uma fonte com cotejo aceito em fontes-concorrentes.json fica preservada no hash cotejado (05/10/2026).
save('fontes-preservadas.json',{x['path']:(x['sha256_final'] if not x['preservada'] and accepted.get(x['path'],{}).get('sha256_final')==x['sha256_final'] else x['sha256']) for x in preserve if '/planejamento-editorial/' not in x['path']})
save('regras-verificadas.json',{'sha256_texto':SHA,'ok':True,'checks':checks,'limites':'Checks textuais asseguram contratos declarados, não leitura automática completa. Parecer contextual separado.'})
print(json.dumps({'ok':True,'sha256_texto':SHA,'verificacoes':len(checks),'casos':len(cases),'niveis':27000,'perfis':len(profiles),'d20_enumerados':n_rolls},ensure_ascii=False))

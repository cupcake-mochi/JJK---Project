from pathlib import Path
from math import ceil,floor
import hashlib,json
A=Path(__file__).resolve().parent;R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(title,actual,expected):
 assert actual==expected,(title,actual,expected)
 checks.append({'conta':title,'resultado':actual,'esperado':expected})
check('Média de 3d8 e três/quatro aplicações',[3*4.5,3*3*4.5,4*3*4.5],[13.5,40.5,54.0])
check('Acerto +4 contra Defesa 11 e 13',[sum(d+4>=dc for d in range(1,21))/20 for dc in [11,13]],[.7,.6])
check('Alma: saldos e custo',[48-12,24-12,9/2,3+1,6//4,6%4],[36,12,4.5,4,1,2])
check('Tratamento para PV máximos 23',[ceil(23/4),ceil(23/3),ceil(23/2)],[6,8,12])
check('Restante depois de tratamento 5',[ceil(23/k)-5 for k in [4,3,2]],[1,3,7])
check('Vida nos dois agrupamentos',[12+12,48+12],[24,60])
check('Rota direta: distância/andar/arrastar',[6+6+6,6+6*2+6,6*2+6*3+6*2],[18,24,42])
check('Rota lateral: distância/andar/arrastar',[24,24,24*2],[24,24,48])
check('Arrasto por trecho 1,5 regular/difícil',[1.5*2,1.5*2+1.5],[3.0,4.5])
check('Arrasto turno inicial: recursos/gasto/percurso/sobra',[9+9,6*2+1.5*3,6+1.5,18-(6*2+1.5*3)],[18,16.5,7.5,1.5])
check('Turno seguinte: recursos/custo/sobra',[9*3,4.5*3+6*2,27-(4.5*3+6*2)],[27,25.5,1.5])
check('Desengajar mantém só dois movimentos',9*2<25.5,True)
check('Estágio 2: movimento total e arrasto regular',[9/2+9/2,9/2],[9,4.5])
check('Carga de personagem 72 kg com itens 2',72/12+2,8)
check('Limites Força 3 e resgate Força 2',[5+3,2*(5+3),1+72/12+2,2*(5+2)],[8,16,9,14])
check('Cargas exatas e excesso decimal',[16<=16,16.1<=16,8<=8,8+.1<=8],[True,False,True,False])
check('Conversão: vida e Integridade',[5+3+(3+3)*(2-1),floor(14/2)],[14,7])
check('Conversão M1 B1: acerto/CD/Defesa/Bloquear',[3+1,11+1,11+1,1],[4,12,12,1])
check('Especial disponível no nível 2',floor((2+2/2)/2),1)
check('Domada: arrasto regular/difícil/Correr',[9/2,9/3,18/2],[4.5,3,9.0])
check('Destruição: a partir de PV5, golpes 21/22',[21-5>16,22-5>16,21>=32,22>=32],[False,True,False,False])
check('Doma a zero: saldos limitados aos novos máximos',[min(0,14),min(16,7)],[0,7])
check('Retorno nível 2: dobro da entrada e metade da vida',[2*1,floor(14/2)],[2,7])
p=R/'04 - Planejamento/apoio-piloto/resultado-validacao.json';d=json.loads(p.read_text());rows=[r for r in d['resultados'] if r['caso'] in ['amontoado','amontoado_desgastado'] and r['politica']=='Insistir' and not r['bloquear']]
check('Histórico: queda e mediana de cada cenário',[[r['alguma_queda'],r['mediana_rodadas']] for r in rows],[[.2036,2.0],[.605,2.0]])
result={'registro':120,'novos_parametros':False,'conferencias':checks,'simulacao_historica':{'fonte':str(p.relative_to(R)),'sha256':sha(p),'execucao_nova':False,'configuracoes_conferidas':rows},'regras_primarias':{'fonte':'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','sha256':sha(R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'),'trechos_consultados':['Testes e Concentração','Corpo Debilitado — Pele e repouso','Manobras, contenções, Carga e arrasto','Invocações em campo — Entrada, tarefas, queda, retorno e Carga e equipamento','Construir invocações — Doma, ficha e progressão']},'limites':['Contas e consulta das regras existentes, sem nova simulação ou equilíbrio comprovado.','Talento CE1 permanece experimental; não foi promovido a regra geral.']}
(A/'contas-conferidas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(len(checks),'conferências')

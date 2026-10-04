from pathlib import Path
from fractions import Fraction
from math import floor, ceil
import hashlib, json
B=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial')
files={'R19':B/'ritual-e-pactos/lote-01/RITUAL-E-PACTOS.md','R06':B/'fundamento/lote-01/FUNDAMENTO.md','R07':B/'catalogo/lote-01/CATALOGO.md'}
# Modelos independentes; não executa nem regrava auditar.py do autor.
checks=[]
def ck(n,a,e):
 checks.append({'caso':n,'obtido':a,'esperado':e,'ok':a==e})
def chance(c,d,trained=True,m=2,sp=0):
 # Inteligência cancela porque aparece nos dois lados, inclusive sem treino.
 return Fraction(sum(n+(m if trained else 0)+sp >= 8+m+c-d for n in range(1,21)),20)
ck('CD exemplo: INT6/DES4/M2/C4',8+6+2+4-4,16)
ck('Probabilidade por enumeração de vinte faces',str(chance(4,4)),'13/20')
ck('Custo médio C4, desconto2 no sucesso, penalidade4 na falha',str(chance(4,4)*10+(1-chance(4,4))*16),'121/10')
ck('Probabilidade C1/DES6',str(chance(1,6)),'9/10')
ck('Recitação não rola Ocultismo; energia antes de dano',12-2,10)
# Contraexemplo de devolução de Atrasar: o feitiço e os bônus estão separados.
normal=3*3-ceil(3/2)+min(3,ceil(3/2))
ritual=3*3-ceil(3/2)
ck('C3 Precisão+Atrasar normal',normal,9)
ck('Mesma montagem sem devolução de Atrasar',ritual,7)
# C3 Rajada+Queima, Gesto+UmaVez: três melhorias máximas, duas restrições válidas.
base=9-2-3+2+2
partes=[2,2,2,2]
package=sum(partes)+sum(x//2 for x in partes)
ritual_extra=min(partes)
ck('Montagem inicial dentro do teto C3',package,12)
ck('Tiros ritualizado, se repetir Queima no tiro novo',package+ritual_extra+ritual_extra//2,15)
# Todos os dados iniciais mais a cópia: equivale a exceção de orçamento, não redistribuição.
ck('Máxima C5,24d8 divididos6 vezes + Tiros',24+min([4]*6),28)
ck('Máxima C7,32d8 divididos8 vezes + Tiros',32+min([4]*8),36)
ck('Compartilhamento C4, Cura8d8 em dois aliados',8+8,16)
ck('Junto de9PV em parcelas9/0 produz cópia mínima0',min([9,0]),0)
# Rerrolar os dados1 do d8 aumenta média em3,5 por dado rerrolado, não4,5.
ck('Ganho condicional por rerrolar1d8=1',str(Fraction(9,2)-1),'7/2')
ck('Pacto, Essência0..6',[x//2 for x in range(7)],[0,0,1,1,2,2,3])
ck('PE por rodada de fonte histórica: 0,50 fatia com câmbio1,01',round(.50/1.01,4),.4950)
# Sensibilidade de interrupção, parâmetros ilustrativos explícitos, não NPC real.
sensitivity=[{'fontes_de_dano':n,'falha_TR_por_ocorrencia':p,'chance_manter':round((1-p)**n,6)} for p in (.2,.35,.5) for n in (0,1,2,3,5)]
result={'ok':all(x['ok'] for x in checks),'sha256':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in files.items()},'checagens':checks,'interrupcao_sensibilidade':sensitivity,'limites':['Não mede combate completo nem substitui playtest humano.','Tiros e Compartilhamento mostram necessidade de exceção explícita, não conclusão automática de excesso de poder.','O teto histórico de PE usa parâmetros antigos e não foi validado para todos os níveis atuais.']}
Path('/tmp/r19-auditoria-independente.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':result['ok'],'checagens':len(checks),'falhas':[x for x in checks if not x['ok']]},ensure_ascii=False))

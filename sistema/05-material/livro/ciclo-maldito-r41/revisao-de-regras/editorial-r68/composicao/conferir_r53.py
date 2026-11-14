from pathlib import Path
from collections import Counter
import json,re,hashlib,unicodedata
from pypdf import PdfReader
from pypdf.generic import ContentStream
B=Path(__file__).resolve().parent;R=B/'revisao-r53';checks=[]
def check(name,ok):
 assert ok,name
 checks.append(name)
old=json.loads((R/'BLOCOS-R52.json').read_text());new=json.loads((R/'BLOCOS-R53.json').read_text());rows=json.loads((B/'ALTERACOES-R52-para-R53.json').read_text())
base=json.loads((R/'PLANO-E-BASE.json').read_text())
for p,sha in base['arquivos_preservados'].items():check('Base preservada: '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha)
rebuilt=dict(old)
for r in rows:
 check(r['id']+': antes exato',rebuilt.get(r['bloco'],'')==r['antes'])
 if r['depois']:rebuilt[r['bloco']]=r['depois']
 else:rebuilt.pop(r['bloco'])
check('Registro reconstrói integralmente a R53',rebuilt==new)
for prefix in ['dano--','geral--','bastiao--','guia--','vanguarda--','incursor--']:
 check('Texto preservado: '+prefix,{k:v for k,v in old.items() if k.startswith(prefix)}=={k:v for k,v in new.items() if k.startswith(prefix)})
check('Bênçãos de combate preservadas',new['rotas--rota-combate']==old['rotas--rota-combate'])
check('Marcantes e demais Origens preservadas',all(new[k]==v for k,v in old.items() if k.startswith('origens--') and k!='origens--restricao-menores-corporais'))
check('Forma Fluida conserva funções e distribuição','As funções e a distribuição do saldo da ficha permanecem.' in new['emanador--ema-forma'])
check('Escolha das funções na criação está explícita','Escolha as funções quando montar a ficha do feitiço.' in new['fundamento--funcoes'])
check('Rotas apresentam o procedimento comum de montagem','## Como montar Manejos e Katas' in new['rotas--rotas'] and all(t in new['rotas--rotas'] for t in ['**Escolha as Famílias.**','**Escolha a função e a Forma de cada aplicação.**','**Monte na Classe disponível.**']))
check('Nomes de cada rota em tabela de consulta',all(t in new['rotas--rotas'] for t in ['Feitiço. | Manejo. | Kata.','Técnica Máxima. | Auge. | Ōgi.']))
check('Criação de Manejos e Katas remete ao procedimento comum',all('[Como montar Manejos e Katas](#rotas-link-montagem)' in new[k] for k in ['rotas--rota-sem-tecnica','rotas--rota-marcial']))
check('Sem Técnica explica a semente antes da montagem','Cada aplicação preparada dessa Regra é um Manejo, montado com funções, Forma, Melhorias e Restrições.' in new['rotas--rota-sem-tecnica'])
check('Recomposição continua em 4 vezes Classe',bool(re.search(r'4\s*×\s*(?:a\s*)?sua maior Classe',new['catalogo--cat-passivas-2-recursos'])))
check('Cura direta paga base Média','Cura direta | Média' in new['fundamento--funcoes'])
check('Vida temporária individual paga Leve','Vida temporária individual | Leve' in new['fundamento--funcoes'])
check('Mesclas pagam somente a maior base','pague somente a maior base exigida por elas' in new['fundamento--funcoes'])
check('Base de funções não recebe desconto nem devolução','A base não recebe desconto de Família nem pode ser recuperada por devoluções.' in new['fundamento--funcoes'])
check('Controle Livre conserva reforços ao descartar a sobra','Se Controle fosse Livre, o gasto cairia para 9. Registrando sem dano, a rede teria os mesmos reforços e descartaria os 3 pontos restantes.' in new['fundamento--controle'])
check('Saldo descartado de Controle não vira cura ou vida temporária','Os pontos descartados deixam de estar disponíveis para cura ou vida temporária e para a compra de Melhorias.' in new['fundamento--controle'])
check('Vida temporária de Classe 1 exemplificada em 6','que concedem **6 de vida temporária**' in new['fundamento--funcoes'])
check('Placas de apoio recalculadas em 3','**3 pontos de vida temporária**' in new['rotas--rota-bancada'] and '3 − 1 − 1 = 1 ponto' in new['rotas--rota-bancada'])
check('Tiras de resgate pagam a base e cumprem Parado','4 − 1 − 2 − 1 + 1 = 1 ponto' in new['construcao--entidade-vigia-habilidades'] and 'Restrição Parado' in new['construcao--entidade-vigia-habilidades'])
check('Orientação usa uma categoria válida de Firmeza','Firmeza: perícia' in new['construcao--entidade-vigia-habilidades'])
check('Orientação termina no começo do próximo turno da invocadora','no próximo teste de perícia que fizer até o começo do próximo turno de Bruna' in new['construcao--entidade-vigia-habilidades'])
check('Toque devolve Leve','Toque | Devolve Leve' in new['fundamento--formas'])
check('Aura custa Leve','Aura | Leve' in new['fundamento--formas'])
check('Explosão custa Média','Explosão | Média' in new['fundamento--formas'])
check('Cone e Linha com origem ao alcance',all(f'{shape} | Leve' in new['fundamento--formas'] for shape in ['Cone','Linha']) and new['fundamento--formas'].count('origem escolhida a até 18 m')==2)
check('Espinho recalculado em 5d8','6 − 2 + 1 = 5' in new['rotas--rota-espinho'] and '5d8 de Força' in new['rotas--rota-espinho'])
check('61 Melhorias e 19 Restrições',sum(k.startswith('catalogo--melhoria-') for k in new)==61 and sum(k.startswith('catalogo--restricao-') for k in new)==19)
old_terms=re.compile(r'\b(?:Certeiro|Muito Longe|Muito Maior|Dívida)\b|Forma (?:Cura|Apoio|Onda)|Corpo a Corpo devolve|Corpo a Corpo embutida|\bCom Junto\b')
check('Sem nomes de peças retiradas no texto publicado',not [(k,l) for k,v in new.items() for l in v.splitlines() if old_terms.search(re.sub(r'\]\([^)]+\)',']',l))])
m=json.loads((B/'FONTES-E-VALIDACAO.json').read_text())
flow=json.loads((B/'revisao-de-estrutura/FLUXO-COLUNAS.json').read_text())
inv=next(e for e in m['eventos'] if e['bloco']=='fundamento--repertorio' and e['texto']=='Invocação por espaço')
regs=[r for r in flow if r['pagina']==inv['pagina']]
check('Invocação por espaço aproveita as duas colunas',any(r['altura_esquerda']>0 and r['altura_direita']>0 for r in regs))
fun=next(e for e in m['eventos'] if e['bloco']=='fundamento--funcoes' and e['texto']=='Funções e saldo')
check('Após a tabela de funções as duas colunas são usadas',any(r['pagina']==fun['pagina'] and r['altura_esquerda']>0 and r['altura_direita']>0 for r in flow))
# Geometria e navegação já conferidas pelo validador geral. Registrar todos
# os nomes atuais com seus destinos e a seleção da paleta aprovada.
aliases=json.loads((R/'ALIASES-RESOLVIDOS.json').read_text())
check('Todos os aliases de migração resolvidos',set(aliases)<=set(m['ancoras']))
check('Sumário inclui funções e mesclas',all(t in [v['titulo'] for v in m['marcadores'].values()] for t in ['Funções e saldo','Três mesclas prontas']))
qa=json.loads((B/'evidencias/CONFERENCIA.json').read_text())
check('Conferência geral corresponde ao PDF atual',qa['sha256_pdf']==m['sha256_pdf'])
check('Conferência geral sem problemas',not qa['problemas'])
(R/'VALIDACAO-R53.json').write_text(json.dumps({'resultado':'aprovado','verificacoes':checks,'paginas':m['paginas'],'blocos_alterados':len(rows),'blocos_preservados':sum(new.get(k)==v for k,v in old.items()),'sha256_pdf':m['sha256_pdf'],'limites':'Integração, preservação, montagem, navegação e geometria. Revisão visual e testes de mesa têm registros próprios.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'resultado':'aprovado','verificacoes':len(checks),'paginas':m['paginas'],'alteracoes':len(rows)},ensure_ascii=False))

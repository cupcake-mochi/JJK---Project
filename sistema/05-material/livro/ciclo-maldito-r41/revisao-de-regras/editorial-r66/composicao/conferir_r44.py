from pathlib import Path
from collections import defaultdict,Counter
import json,re,hashlib,sys
from pypdf import PdfReader
B=Path(__file__).resolve().parent;R=B/'revisao-r44';base=B.parent/'livro-diagramado-r43';issues=[];checks=0
read=lambda p:json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def check(ok,label):
 global checks
 checks+=1
 if not ok:issues.append(label)
def blocks(text):
 return {m[1]:re.split(r'\n<a id="capitulo-|\n<!-- parte:',m[2])[0].strip() for m in re.finditer(r'<!-- fonte:[^\n]+ -->\n<a id="([^"]+)"></a>\n(.*?)(?=\n<!-- fonte:|\Z)',text,re.S)}
def pub(s):return re.sub(r'^(#{1,6}) ',lambda m:'#'*(len(m[1])+2)+' ',s,flags=re.M)
oldmd=(base/'LIVRO-COMPLETO.md').read_text();newmd=(B/'LIVRO-COMPLETO.md').read_text();old=blocks(oldmd);new=blocks(newmd);rows=read(B/'ALTERACOES-R43-para-R44.json');byid={r['bloco']:r for r in rows}
changed={k for k in old.keys()|new.keys() if old.get(k)!=new.get(k)}
check(len(rows)==25,'25 entradas no registro')
check(len(byid)==len(rows),'Uma entrada por bloco')
check(changed==set(byid),'Todas e somente as mudanças textuais estão registradas')
check(set(old)-set(new)=={'fabricacao--fab-projeto','fabricacao--fab-exemplo'},'Somente os dois blocos autorizados foram removidos')
check(set(new)-set(old)=={'ritual--pacto-exemplos'},'Somente o bloco de exemplos foi acrescentado')
check({int(n.strip()) for row in rows for n in row['item'].split(',')}=={24,33,40,46,101,151,188,189,190,191,192},'Todos os itens solicitados registrados, incluindo 192')
expected=oldmd;order=read(B/'ORDEM.json')
for row in rows:
 k=row['bloco'];a=pub(row['antes']);z=pub(row['depois'])
 check(set(row)=={'id','bloco','antes','depois','motivo','item'},'Formato: '+k)
 check(a==old.get(k,''),'Antes exato: '+k);check(z==new.get(k,''),'Depois exato: '+k)
 if not a:continue
 if z:
  check(expected.count(a)==1,'Ocorrência única: '+k);expected=expected.replace(a,z,1)
 else:
  doc,anchor=k.split('--',1);fragment=f'<!-- fonte:{order["fontes"][doc]}#{anchor} -->\n<a id="{k}"></a>\n'+a+'\n\n'
  check(expected.count(fragment)==1,'Fragmento removido único: '+k);expected=expected.replace(fragment,'',1)
k='ritual--pacto-exemplos';a=pub(byid['ritual--pacto-restricao']['depois'])+'\n\n'
addition=f'<!-- fonte:{order["fontes"]["ritual"]}#pacto-exemplos -->\n<a id="{k}"></a>\n'+pub(byid[k]['depois'])+'\n\n'
check(expected.count(a)==1,'Posição única dos novos exemplos');expected=expected.replace(a,a+addition,1)
check(expected==newmd,'Texto integral e ordem idênticos à R43 fora do registro')
# Reparos: frações e limites de Classe iguais nas duas ocorrências.
for k in ['origens--origem-reparo','campo--inv-reparo']:
 s=new[k]
 check('ofício compatível com o corpo, anotado na ficha' in s,'Ofício registrado: '+k)
 for row in ['| Igual | Difícil | 0 | Metade da vida máxima. |','| Uma abaixo | Média | −2 | Metade da vida máxima. |','| Duas ou mais abaixo | Fácil | −4 | Metade da vida máxima. |','| Uma acima | Difícil | 0 | Um terço da vida máxima. |','| Duas ou mais acima | Difícil | 0 | Um quarto da vida máxima. |']:
  check(row in s,'Tabela de reparo: '+k+' '+row)
 check('arredondada para baixo' in s,'Arredondamento de reparo: '+k)
 a=[l for l in old[k].splitlines() if l.startswith('> ')];z=[l for l in s.splitlines() if l.startswith('> ')];check(a==z,'Exemplo de reparo intacto: '+k)
check(new['dano--socorro']==old['dano--socorro'].replace('use Entalhador ou Forja em lugar de Medicina','use o ofício compatível com o corpo em lugar de Medicina'),'Somente o ofício de socorro foi alterado')
# Proteções explícitas do escopo.
for k in old:
 if k.startswith(('dano--','origens--')) and k not in ['dano--socorro','origens--origem-corpo','origens--origem-reparo']:check(old[k]==new[k],'Preservação: '+k)
for k in ['geral--bloquear','incursor--inc-redirecionar-resolucao','construcao--entidades-domar','ritual--rit-ajuda']:
 check(new[k]==old[k],'Regra/exemplo anterior intacto: '+k)
check('Criadas e domadas mantêm seus níveis' not in newmd and 'a uma domada ou criada depois da aquisição' not in newmd,'Duas contradições autorizadas removidas')
check('conserva o nível em que foi fabricada' not in newmd and 'Conserva o nível em que foi criada' not in newmd,'Evolução antiga ausente')
check('Entalhador ou Forja' not in newmd,'Ofícios fixos antigos ausentes')
cr=new['fabricacao--fab-entidades'];co=new['fabricacao--fab-conclusao'];te=new['fabricacao--fab-teste']
for phrase in ['não exige técnica de invocação nem ocupa espaço conhecido','Cada entidade pede a própria tentativa','não pode superar a Classe de quem cria nem a do invocador','limitado ao último nível da Classe escolhida']:
 check(phrase in cr,'Criação: '+phrase)
for phrase in ['Média (−2)','Fácil (−4)','É um teste por Classe','Uma entidade destruída exige criar outra','consentimento do dono anterior ou a morte dele','Classe igual ou maior que a da entidade','Classe, ficha, vida atual e usos gastos']:
 check(phrase in co,'Reconstrução e transferência: '+phrase)
for phrase in ['ajudante treinado no ofício compatível','mesmo tempo que o responsável','vantagem permanente nesse teste','Vantagem ativada, por cena ou temporária não vale','continua valendo nos três testes','8 + 4 + 2 − 2 = 12','a CD seria 14']:
 check(phrase in te,'Teste e exemplo: '+phrase)
# Ritual: 16 entradas, cinco repetíveis, preços preservados.
rs=[];oldrs=[]
for k in ['ritual--rit-melhorias','ritual--rit-beneficios']:
 rs += [[v.strip() for v in l.strip('|').split('|')] for l in new[k].splitlines() if l.startswith('| Ritual de ')]
 oldrs += [[v.strip() for v in l.strip('|').split('|')] for l in old[k].splitlines() if l.startswith('| Ritual de ')]
check(len(rs)==16 and all(len(r)==4 for r in rs),'16 Melhorias, todas com Repete')
check({r[0] for r in rs if r[3]=='Sim, até 2.'}=={'Ritual de Acerto','Ritual de Dificuldade','Ritual de Alcance','Ritual de Tamanho','Ritual de Rerrolagem'},'Somente as cinco Melhorias autorizadas repetem')
check([r[:3] for r in rs]==oldrs,'Benefícios-base e preços das 16 entradas preservados')
check('2 × (Classe + 1) dados' in new['ritual--rit-melhorias'] and 'um ponto acima do mínimo' in new['ritual--rit-melhorias'],'Rerrolagem dupla completa')
check('Benefícios repetidos de Defesa não se somam entre si.' in new['ritual--rit-melhorias'],'Ritual de Defesa preservado')
# Cortina e pactos.
s=new['aptidoes--apt-cortina'];check(all(x in s for x in ['Até 150 m.','Até 300 m.','Até 400 m.','40 × Refino pontos de vida']),'Cortina com três tetos e mesma vida')
check([l for l in old['aptidoes--apt-cortina'].splitlines() if l.startswith('> ')]==[l for l in s.splitlines() if l.startswith('> ')],'Haru intacto')
for k in ['ritual--pacto-permanente','ritual--pacto-temporario']:
 check([l for l in old[k].splitlines() if l.startswith('> ')]==[l for l in new[k].splitlines() if l.startswith('> ')],'Exemplo preservado: '+k)
for phrase in ['sem acrescentar diretamente um valor numérico','Não existe pacto por dano','Promessas e pactos temporários não entram nesse limite']:
 check(phrase in new['ritual--pacto-permanente'],'Limite de pacto preservado: '+phrase)
check('Não existe uma tabela que transforme qualquer sacrifício em qualquer resultado.' in new['ritual--pacto-temporario'],'Régua não é conversão')
check('depois de os dados dele serem rolados e antes de as consequências serem aplicadas' in new['ritual--pacto-temporario'],'Item 192: momento da Reação')
check('O pacto não refaz nem muda uma rolagem' in new['ritual--pacto-temporario'],'Item 192: rolagem preservada')
check('Gastar Reação aqui não permite agir fora do turno' not in newmd,'Proibição antiga ausente')
examples=new['ritual--pacto-exemplos'];parts=re.split(r'^##### (\d+)\. ',examples,flags=re.M)
check(len(parts)==19,'Nove exemplos numerados')
check(examples.count('Ganho:')==5,'Tamanho somente nos cinco primeiros exemplos')
check('**32 durante a jornada** e **48 na hora extra**' in examples and '**16 PE**' in examples,'Exemplo Overtime coerente: 40, 20%, 32, 48, diferença 16')
check('Feitiços Automáticos não mudam' in examples and 'no terceiro' in examples,'Mostrar a mão: automáticos e três turnos')
check(len([l for l in new['ritual--pacto-restricao'].splitlines() if l.startswith('| ') and 'Ideia' not in l])==7,'Sete ideias remanescentes')
visible=re.sub(r'<!--.*?-->','',newmd,flags=re.S)
check('Fabricação de entidades' not in visible,'Nome antigo ausente de título, índice e remissões')
check('[Criação de entidades](#fabricacao--fab-entidades)' in new['consulta--consulta-indice-3'],'Índice novo em C')
# Base e estilos preservados.
hashes=read(R/'BASE-R43-SHA256.json');now={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
check(hashes==now,'R43 integralmente intacta')
for name in ['ESTUDO-DENSIDADE.json','ESTUDO-CAPITULO.json','ESTUDO-SECAO.json','ESTUDO-TABELAS.json','ESTUDO-HIERARQUIA.json','CREDITOS.json','CAPA-E-ABERTURAS.json','REFERENCIAS.json','ORDEM.json']:
 check((B/name).read_bytes()==(base/name).read_bytes(),'Estilo/estrutura preservado: '+name)
for p in (base/'fontes-editoriais').rglob('*'):
 if p.is_file():check(p.read_bytes()==(B/'fontes-editoriais'/p.relative_to(base/'fontes-editoriais')).read_bytes(),'Fonte preservada: '+str(p.relative_to(base)))
m=read(B/'FONTES-E-VALIDACAO.json');prior=read(base/'FONTES-E-VALIDACAO.json');pdf=B/'output/pdf/Ciclo-Maldito-R44.pdf';reader=PdfReader(pdf);digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
check(m['pdf']=='output/pdf/Ciclo-Maldito-R44.pdf' and m['sha256_pdf']==digest,'Manifesto corresponde ao PDF R44')
check(len(reader.pages)==m['paginas'],'Contagem de páginas')
check(all(v['titulo']!='Fabricação de entidades' for v in m['marcadores'].values()),'Marcadores sem nome antigo')
toc=read(R/'SUMARIO-PAGINADO.json')
tocrows=[e for page in toc for e in page['entradas']]
check(any(e['titulo']=='Criação de entidades' and e['destino']=='fabricacao--fab-entidades' for e in tocrows),'Sumário publicado usa o nome novo')
check(not any(e['titulo']=='Fabricação de entidades' for e in tocrows),'Sumário publicado sem o nome antigo')
tocpdf=' '.join(reader.pages[i].extract_text() for i in [1,2,3])
check('Fabricação de entidades' not in tocpdf and 'Criação de entidades' in tocpdf,'Nome novo extraído do sumário do PDF')
# Comparar composição independentemente do deslocamento de páginas.
def bypage(data):
 out=defaultdict(list)
 for e in data['eventos']:out[e['pagina']].append({k:v for k,v in e.items() if k not in {'pagina','faixa'}})
 return out
oldp,newp=bypage(prior),bypage(m)
fingerprint=lambda es:hashlib.sha256(json.dumps(es,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
oldsignatures={fingerprint(es) for es in oldp.values()}
recomposed=[p for p,es in newp.items() if fingerprint(es) not in oldsignatures]
textpages=sorted({e['pagina'] for e in m['eventos'] if e.get('bloco') in changed})
navpages=[p['pagina'] for p in m['paginas_planejadas'] if p['tipo']=='toc' or p['capitulo']==21]
reviewpages=sorted(set(recomposed)|set(textpages)|set(navpages))
save(R/'PAGINAS-PARA-REVISAO.json',{'paginas_de_texto_alterado':textpages,'paginas_recompostas_sem_contar_apenas_mudanca_de_numero':sorted(recomposed),'paginas_de_navegacao':navpages,'revisar':reviewpages})
report={'base':'R43','revisao':'R44','data':'2026-10-12','paginas':len(reader.pages),'blocos_registrados':len(rows),'blocos_alterados':sorted(changed),'blocos_novos':sorted(set(new)-set(old)),'blocos_removidos':sorted(set(old)-set(new)),'texto_identico_fora_do_registro':expected==newmd,'r43_intacta':hashes==now,'arquivos_r43_verificados':len(hashes),'exemplo_reformulado':'Calígrafa: Classe escolhida e invocador explícitos; CD 12 e CD 14 preservadas.','paginas_para_revisao':reviewpages,'checagens':checks,'sha256_pdf':digest,'problemas':issues}
save(R/'CONFERENCIA.json',report);print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(issues))

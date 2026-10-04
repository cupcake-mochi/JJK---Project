from pathlib import Path
import json,shutil,hashlib
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial');B=P/'validacao-editorial';M=P/'consolidacao/lote-01/migracao-nomes';f=B/'DONOS.json';shutil.copy2(f,M/'DONOS-ANTES.json');j=json.loads(f.read_text())
x=next(x for x in j['termos'] if x['termo']=='Mão Firme');x['donos']=['fundamento'];x['fontes']=['sistema/05-material/livro/manual/40-fundamento.md:322 — Passiva histórica de Classe 1','catalogo/lote-01/CATALOGO.md — Talento de Categoria 1'];x.pop('nota_colisao',None);x['nota_auditoria']='Não há aptidão autônoma homônima no catálogo completo R09. As três menções em Aptidões são incompatibilidades expressas, não definições da capacidade. Tratadas por exceções contextuais exatas.'
for name in ['Identificar Feitiço','Leitura de Feitiços']:
 assert not any(x['termo']==name for x in j['termos'])
 j['termos'].append({'termo':name,'donos':['fundamento'],'fontes':['catalogo/lote-01/CATALOGO.md'],'somente_nome_marcado':True,'alias_historico':'Aviso','nota_alias':'A Melhoria e o Talento tinham o mesmo nome. O nome histórico não distingue os dois; consultar o tipo da entrada.'})
j['aliases_historicos']=[{'antes':'Aviso (Melhoria)','atual':'Identificar Feitiço','dono':'fundamento'}, {'antes':'Aviso (Passiva)','atual':'Leitura de Feitiços','dono':'fundamento'}, {'antes':'Incapacitado / Incapacitada','atual':'Guarda Aberta','dono':'condicoes','uso_compartilhado':True}, {'antes':'Passiva Livre','atual':'Expressão da técnica','dono':'fundamento','uso_compartilhado':True}, {'antes':'Passiva / Passivas (aquisição)','atual':'Talento / Talentos','dono':'fundamento','uso_compartilhado':True}, {'antes':'Classe Passiva / CP','atual':'Categoria de Efeito / CE','dono':'fundamento','uso_compartilhado':True}]
j['nota_conceitos_compartilhados']='Aliases de categorias, condições e recursos comuns documentam equivalências. Não bloqueiam menções legítimas fora do capítulo dono; somente capacidades específicas constam em termos. Adjetivos comuns como efeito passivo e CD passiva continuam válidos.'
f.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=B/'LEIA-ME.md';s=p.read_text();start=s.index('Mão Firme tem os donos');end=s.index('\n',start);s=s[:start]+'Mão Firme pertence ao **Fundamento**, onde aparece no catálogo de Talentos. A conferência do catálogo completo de Aptidões não encontrou aptidão autônoma homônima: as três menções são incompatibilidades, registradas como referências contextuais exatas. O cadastro anterior atribuía dois donos por engano. Identificar Feitiço e Leitura de Feitiços distinguem a Melhoria e o Talento antes chamados Aviso. `aliases_historicos` conserva as equivalências nominais; conceitos compartilhados (Talento, Categoria de Efeito, Guarda Aberta) não são tratados como capacidade de caminho por mera menção.'+s[end:];p.write_text(s)
# Three indispensable negative interfaces; no reproduction of the talent result.
p=P/'aptidoes/lote-01/evidencias/LOCALIZACAO-EDITORIAL.json';d=json.loads(p.read_text());lines=(P/'aptidoes/lote-01/APTIDOES-E-REFINO.md').read_text().splitlines()
import importlib.util
spec=importlib.util.spec_from_file_location('editorial',B/'conferir_editorial.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
for line in lines:
 if 'Mão Firme' in line:
  ex={'termo':'Mão Firme','trecho':mod.visible(line).strip(),'papel':'incompatibilidade','justificativa':'A proteção usa teste próprio, e a referência exclui a dispensa de concentração do Talento. Não reproduz seu efeito nem seu preço.','nao_reproduz_regra':True}
  if ex not in d.setdefault('excecoes_localizacao',[]):d['excecoes_localizacao'].append(ex)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('DONOS e três interfaces negativas de R09 atualizados')

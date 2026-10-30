"""Fechar a continuidade do registro 135 sem alterar provas ou índices históricos."""
from pathlib import Path
from html import escape
import hashlib,json,os,re
from bs4 import BeautifulSoup

A=Path(__file__).resolve().parent;R=A.parents[1];S=R/'06 - Redacao do Guia/revisao-98'
OLD=R/'04 - Planejamento/apoio-revisao-textual-134'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(name,x):(A/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rel(path,base=A):return os.path.relpath(R/path,base)
def title(path):return re.search(r'^#\s+(.+)$',(R/path).read_text(),re.M).group(1)

def main():
 data=load(OLD/'destinos-e-fontes.json');routes=load(OLD/'rotas-de-consulta.json');q=load(OLD/'fila-dos-casos.json')
 data.update(registro=135,revisao_das_rotas=135,limite='Conferência transversal dirigida e remissões atualizadas. As fontes editáveis são vigentes; provas anteriores preservam sua versão histórica. Integração e inspeção visual do livro completo pendentes.')
 routes['registro']=135
 methods={'B1':'04-na-mesa-de-jogo.md','B2':'06-inimigos-e-perigos.md','B3':'07-personagens-e-tecnicas.md','B4':'08-entre-missoes.md','B5':'09-pactos-e-entidades.md'}
 for group,row in routes['grupos'].items():
  row['prova_anterior']=row['metodo'];row['metodo']=str((S/methods[group]).relative_to(R))
 routes['guilda_anterior']=routes['guilda'];routes['guilda']=str((S/'10-jogar-em-guilda.md').relative_to(R))
 routes['avisos']['versao_vigente']='A consulta atual aponta para a fonte editável atualizada; as provas anteriores são históricas até a integração.'
 for group,rows in data['casos'].items():
  for row in rows:
   source=row['fonte_revisada'];row['prova_anterior']=row['consulta_atual'];row['consulta_atual']=source
   row['titulo']=title(source);row['sha256_revisado']=sha(R/source);row['conferencia_do_conjunto']=135
 for mapping in ['casos_revisados','consultas_revisadas']:
  for ident,row in routes[mapping].items():
   source=row['fonte_revisada'];row['prova_anterior']=row['consulta_atual'];row['consulta_atual']=source
   row['titulo']=title(source);row['sha256_revisado']=sha(R/source)
 data['rotas']=routes
 for rows in [q['casos'],q['outras_consultas_pendentes']]:
  for row in rows:
   source=row['fonte_revisada'];row['prova_anterior']=row['consulta_atual'];row['consulta_atual']=source
   row['titulo']=title(source);row['sha256_revisado']=sha(R/source);row['conferencia_do_conjunto']=135
 q.update(registro=135,base=str((A/'destinos-e-fontes.json').relative_to(R)),proximo_lote='Integração editorial e leitura contínua do conjunto',consultas_pendentes=0)
 save('rotas-de-consulta.json',routes);save('destinos-e-fontes.json',data);q['base_sha256']=sha(A/'destinos-e-fontes.json');save('fila-dos-casos.json',q)
 css=BeautifulSoup((OLD/'casos-completos.html').read_text(),'html.parser').style.get_text()
 groups={'B1':'Testes, percepção e movimento','B2':'Confrontos e perigos','B3':'Personagens e técnicas','B4':'Objetos e recompensas','B5':'Pactos e entidades'}
 body='<h1>Casos por assunto</h1><p>59 casos e 17 consultas com revisões locais concluídas. As ligações abaixo abrem as fontes editáveis vigentes, com os nomes e referências da conferência 135. As provas anteriores guardam suas versões históricas; o PDF integrado novo ainda será produzido.</p>'
 body+='<p><a href="guia-de-consulta.html">Escolher uma folha</a> · <a href="fila-dos-casos.md">Próximos trabalhos</a></p>'
 md='# Casos por assunto\n\nRegistro 135. Fontes editáveis vigentes; provas antigas históricas até a integração.\n\n'
 for code,name in groups.items():
  body+=f'<section id="{code}"><h2>{name}</h2><p><a href="{escape(rel(routes["grupos"][code]["metodo"]),quote=True)}">Explicação principal</a></p><ul>'
  md+='## '+name+'\n\n'
  for row in data['casos'][code]:
   target=rel(row['fonte_revisada']);body+=f'<li><a href="{escape(target,quote=True)}">{escape(row["titulo"])}</a></li>'
   md+=f'- [{row["titulo"]}](<{target}>).\n'
  body+='</ul></section>';md+='\n'
 body+='<section><h2>Consultas complementares</h2><ul>'
 for row in q['outras_consultas_pendentes']:body+=f'<li><a href="{escape(rel(row["fonte_revisada"]),quote=True)}">{escape(row["titulo"])}</a></li>'
 body+='</ul></section>'
 def html(title,body):return '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+css+'</style></head><body><main>'+body+'</main></body></html>'
 (A/'casos-completos.html').write_text(html('Casos por assunto | Ciclo Maldito',body));(A/'destinos-dos-casos.md').write_text(md)
 guide='<h1>Escolher uma folha</h1><p><a href="casos-completos.html">Casos por assunto</a>. Fontes editáveis atuais; use as folhas curtas para uma tarefa simples e os formulários completos quando precisar de mais campos.</p><h2>Folhas curtas</h2><ul>'
 for p in sorted((S/'consultas').glob('A*.md')):guide+=f'<li><a href="{escape(os.path.relpath(p,A),quote=True)}">{escape(title(str(p.relative_to(R))))}</a></li>'
 guide+='</ul><h2>Formulários e consultas completos</h2><ul>'
 for row in q['outras_consultas_pendentes']:guide+=f'<li><a href="{escape(rel(row["fonte_revisada"]),quote=True)}">{escape(row["titulo"])}</a></li>'
 guide+='</ul><p><a href="'+escape(os.path.relpath(S/'consultas/LEIA-ME.md',A),quote=True)+'">Guia de escolha com exemplos</a></p>'
 (A/'guia-de-consulta.html').write_text(html('Escolher uma folha | Ciclo Maldito',guide))
 lines='# Fila editorial\n\nRegistro 135. Os 59 casos e as 17 consultas têm revisões locais concluídas. A conferência transversal foi encerrada no escopo documentado; não substitui a leitura contínua e a inspeção do livro integrado.\n\n## Casos\n\n| Lote | Assunto | Estado |\n|---|---|---|\n'
 for row in q['lotes_planejados']:lines+=f'| {row["lote"]} | {row["titulo"]} | {row["estado"]} |\n'
 lines+='\n## Consultas\n\n| Lote | Assunto | Estado |\n|---|---|---|\n'
 for row in q['lotes_consultas']:lines+=f'| {row["lote"]} | {row["titulo"]} | {row["estado"]} |\n'
 lines+='\n## Próxima tarefa\n\nIntegração editorial: fechar o destino dos apoios externos, reunir capítulos, casos e folhas, eliminar duplicações e atualizar mapas, nomes, sumário e remissões. Fazer leitura contínua da prova consolidada antes da revisão visual global. GPT-6.1 Sol, esforço alto. Veja [as pendências com destino](pendencias-da-integracao.md).\n'
 (A/'fila-dos-casos.md').write_text(lines)
 report=R/'04 - Planejamento/135-conferencia-do-conjunto.md'
 controls=load(OLD/'arquivos-do-lote.json')['controles']
 for entry in controls[:7]:
  p=R/entry;t=p.read_text();assert t.count('Fila vigente - registro 134')==1,entry
  t=t.replace('Fila vigente - registro 134','Fila histórica - registro 134')
  banner='> **Fila vigente - registro 135, 30/10/2026:** conferência transversal retomada e fechada: elenco aprovado e referências atualizados, números e tabelas preservados. [Registro, prova e índice vigente](<'+os.path.relpath(report,p.parent)+'>). Os 59 casos e as 17 consultas têm revisões locais concluídas. Prova das alterações com 20 páginas inspecionadas. **Próximo: integração editorial e leitura contínua; GPT-6.1 Sol, esforço alto.** Apoios ainda externos têm destino documentado. PDF integrado anterior preservado; revisão visual global e comparação final continuam pendentes.\n\n'
  head,rest=t.split('\n',1);p.write_text(head+'\n\n'+banner+rest.lstrip('\n'))
 p=S/'LEIA-ME.md';t=p.read_text();paragraph='O [registro 135](<../../04 - Planejamento/135-conferencia-do-conjunto.md>) fecha a conferência transversal e a retomada do Claude. Use o [índice vigente](<../../04 - Planejamento/apoio-conferencia-135/casos-completos.html>), a [fila atual](<../../04 - Planejamento/apoio-conferencia-135/fila-dos-casos.md>) e as [pendências da integração](<../../04 - Planejamento/apoio-conferencia-135/pendencias-da-integracao.md>). Os nomes aprovados e as remissões estão nas fontes editáveis; provas anteriores permanecem históricas.\n\n'
 assert t.count('[Como usar este livro]')==1;t=t.replace('[Como usar este livro]',paragraph+'[Como usar este livro]',1)
 t=re.sub(r'\*\*Próxima tarefa:\*\* conferência do conjunto[^\n]+','**Próxima tarefa:** integração editorial e leitura contínua: fechar os destinos de apoio, reunir capítulos, casos e consultas sem duplicação e conferir o texto consolidado. Depois, revisão visual de cada página e comparação final. **GPT-6.1 Sol, esforço alto.**',t,count=1);p.write_text(t)
 p=R/'04 - Planejamento/apoio-piloto/RETOMADA.md';p.write_text(p.read_text()+'\n\n## Registro 135 — conferência do conjunto retomada\n\nAs mudanças do Claude estavam aplicadas em 67 arquivos, sem fechamento. A retomada conferiu o histórico, os links, as âncoras, os números, as tabelas e os originais; explicitou a falha de Estudar; reinspecionou as 20 páginas da prova e atualizou os destinos atuais. [Registro e limites](../135-conferencia-do-conjunto.md). São 59 casos e 17 consultas com revisões locais concluídas. Próximo: integração editorial e leitura contínua, com GPT-6.1 Sol, esforço alto. Apoios externos, mapas e fontes da obra têm pendências descritas. PDF integrado anterior preservado; sem novo envio ao GitHub nesta retomada.\n')
 p=S/'consultas/LEIA-ME.md';t=p.read_text();old='apoio-revisao-textual-134/casos-completos.html';new='apoio-conferencia-135/casos-completos.html';assert t.count(old)==1
 p.write_text(t.replace(old,new));log=load(A/'alteracoes.json');log.append({'arquivo':'consultas/LEIA-ME.md','antes':old,'depois':new,'vezes':1,'motivo':'Remissão: índice vigente da conferência 135; apenas o destino muda.'});save('alteracoes.json',log)
 changed=load(A/'retomada/antes-do-fechamento/fontes-alteradas-pelo-claude.json')
 save('arquivos-do-lote.json',{'controles':controls,'fontes_revisadas':[str((S/f).relative_to(R)) for f in changed if str((S/f).relative_to(R)) not in controls],'extras':[],'fontes_novas':[],'relatorio':str(report.relative_to(R))})
 print('Índice, fila, rotas e dez controles atualizados; fontes atuais preservam os registros de revisão anteriores.')

if __name__=='__main__':main()

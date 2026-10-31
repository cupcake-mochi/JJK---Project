from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,os,re
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');a=r/'04 - Planejamento/apoio-editorial-147';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();save=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
c=json.loads((a/'composicao.json').read_text());v=json.loads((a/'revisao-visual.json').read_text());assert len(v['paineis_inspecionados'])==len(json.loads((a/'renderizacao.json').read_text())['painel'])
audit=json.loads((a/'conferencia-do-pdf.json').read_text());assert not audit['falhas'];assert not audit.get('diferencas_de_extracao_a_examinar',[])
assert v['sha256_pdf']==c['sha256_pdf']==sha(r/c['pdf'])
assert v['paginas_inspecionadas']==list(range(1,c['paginas']+1))
assert not v['problemas_impeditivos_observados']
report=r/'04 - Planejamento/147-ajustes-de-consulta-e-leitura.md'
report.write_text(f'''# Ajustes de consulta e leitura

Registro 147, 30/10/2026. Os três ajustes do parecer 146 foram aplicados. A edição completa tem **{c['paginas']} páginas**. Há também um pacote de seis páginas para impressão das folhas curtas e seus exemplos.

[Livro atualizado](<../{c['pdf']}>) · [Folhas para impressão](<../08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa-Impressao.pdf>) · [HTML](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Revisão visual](apoio-editorial-147/revisao-visual.json) · [Conferência do PDF](apoio-editorial-147/conferencia-do-pdf.json).

## Consulta mais próxima

O apêndice começa pelo seletor e pelas folhas curtas de preparar, conduzir e retomar, com seus exemplos, antes dos formulários extensos. O HTML segue a mesma ordem. Cada modelo curto permanece em uma página; a retomada preenchida usa duas para conservar os dados de socorro.

O pacote de impressão conserva as páginas e as referências do livro completo. Seus números são os do livro, para facilitar consulta. Não reúne todas as regras e não tem navegação clicável; referências a capítulos e casos são consultadas no volume completo.

## Conversa e comentário

As falas têm recuo; decisões do mestre e comentários de condução usam fundo claro. A montagem técnica marcada para consulta também recebe destaque discreto. A tipografia acompanha o livro base, com corpo e entrelinha preservados. O tratamento distingue funções sem colocar toda a missão em caixas. A classificação visual também aparece no HTML.

O texto da primeira missão não mudou. A regra, a fala e o comentário continuam próximos; o destaque ajuda a reconhecer qual trecho ensina a decisão tomada.

## Ideias mais diretas

Oito alterações no complemento do capítulo 3 reuniram os lembretes gerais e reduziram interrupções nos perfis e cenas. Dara e Joana conservam interesses e formas de reagir. A travessia conserva distâncias, horários, carga, teste, movimento e consequência da falha. O registro de alterações está em [alterações textuais](apoio-editorial-147/alteracoes-textuais.json).

Os trechos alterados foram conferidos com contexto e relidos. A sequência numérica da fonte foi comparada com a anterior, sem diferenças. As outras 98 fontes integradas permanecem iguais. A revisão não define novos benefícios de treinamento ou estatísticas.

## Conferência

A conferência HTML verificou 1.926 ligações locais e suas âncoras. A composição compara os blocos com o texto visível e a conferência independente procura omissões por documento, sobreposições, limites de página e destinos inválidos. Os resultados efetivos ficam nos arquivos deste apoio.

Todas as páginas do PDF final foram examinadas nos painéis de nove páginas, com ampliações selecionadas dos diálogos, ideias e folhas. O registro visual identifica o hash da versão e as páginas ampliadas. Essa inspeção verifica a apresentação; não representa aprendizagem observada com leitores.

Os PDFs de 357 e 383 páginas dos registros anteriores foram preservados. Os geradores vigentes do HTML e do novo PDF ficam em `apoio-editorial-147`; não reaplicar preparadores antigos. O salvamento deste registro é local; o último envio remoto continua sendo o 141.

## Próximo trabalho

Os três ajustes delimitados no parecer 146 estão tratados. A pré-1.0 pode receber comentários usando os perfis e tarefas do plano 98. Não é necessário ampliar o livro para começar essa coleta.

A principal frente mecânica pendente é a dificuldade dos encontros. Recomendo preparar seu plano de avaliação, comparando tamanhos de grupo, recursos, terreno, controle, objetivos, socorro e retirada, antes de propor uma escala geral. **Modelo recomendado: GPT-6 Astra, esforço extra alto.** Para organizar retorno de leitura e correções pontuais, GPT-6.1 Sol, esforço alto.
''')
controls=json.loads((r/'04 - Planejamento/apoio-comparacao-146/arquivos-do-lote.json').read_text())['controles']
for rel in controls:
 p=r/rel;old=p.read_text();b=a/'antes'/rel;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes());old=re.sub(r'> \*\*Fila vigente','> **Fila histórica',old,count=1);first,rest=old.split('\n',1);target=os.path.relpath(report,p.parent)
 block=f'> **Fila vigente - registro 147, 30/10/2026:** três ajustes editoriais concluídos: folhas curtas primeiro, falas e comentários distintos, avisos repetidos reduzidos. [PDF de {c["paginas"]} páginas, pacote de impressão e revisão](<{target}>). Geradores HTML e PDF em `apoio-editorial-147`. Próximo: plano de avaliação da dificuldade dos encontros; GPT-6 Astra, esforço extra alto. Retorno da pré-1.0 pode ser incorporado desde já. Salvamento local; último GitHub: registro 141.\n\n'
 new=first+'\n\n'+block+rest.lstrip('\n')
 if rel.endswith('98-plano-de-melhoria-e-validacao-do-guia.md'):
  pos=new.index('## 7. Próxima tarefa e configuração');new=new[:pos]+'''## 7. Próxima tarefa e configuração

Os três ajustes delimitados no parecer 146 foram concluídos no [registro 147](147-ajustes-de-consulta-e-leitura.md). A edição atual e as folhas de impressão estão disponíveis para leitura e retorno. A comparação final continua parcial quanto à aprendizagem externa e à dificuldade geral dos encontros.

**Próxima frente mecânica:** preparar o plano de avaliação dos encontros, com perguntas, grupos e situações de comparação, sem antecipar uma escala geral. GPT-6 Astra, esforço extra alto. Os modelos e números atuais continuam experimentais.

Incorporar retorno da pré-1.0 pelas tarefas e perfis da seção 5, quando houver participantes. Para organizar observações e corrigir texto: GPT-6.1 Sol, esforço alto. O fechamento da 1.0 terá decisão própria sobre as limitações restantes.
'''
 p.write_text(new)
save(a/'arquivos-do-lote.json',{'registro':147,'controles':controls,'pdf':c['pdf'],'relatorio':report.relative_to(r).as_posix()})
base=json.loads((a/'antes/manifesto-entrega.json').read_text());assert len(base)==6396
allowed=set(controls)|{p.relative_to(r).as_posix() for p in (r/'07 - Edicao de Leitura/edicao-integrada-136').glob('*.html')}|{'07 - Edicao de Leitura/edicao-integrada-136/leitura.css','06 - Redacao do Guia/edicao-integrada-136/03a-ideias-para-aventuras.md'}
def check(item):
 rel,h=item;p=r/rel;assert p.is_file(),rel;actual=sha(p);assert actual==h or rel in allowed,rel;return rel,actual
with ThreadPoolExecutor(max_workers=4) as pool:actual=dict(pool.map(check,base.items()))
changed=[k for k in base if base[k]!=actual[k]]
assert len([x for x in changed if x.startswith('06 - Redacao do Guia/edicao-integrada-136/')])==1
sources=json.loads((r/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json').read_text())['fontes'];assert all(sha(r/x['fonte'])==x['sha256'] for x in sources)
save(a/'conferencia-do-manifesto.json',{'registro':147,'entradas_anteriores':len(base),'alteracoes':changed,'originais_preservados':104,'fontes_integradas_alteradas':1,'fontes_integradas_preservadas':98,'pdfs_anteriores_preservados':True,'falhas':[]})
files=[p for p in a.rglob('*') if p.is_file() and '__pycache__' not in p.parts]+[report,r/c['pdf'],r/'08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa-Impressao.pdf']
assert json.loads((r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())==base,'O manifesto foi alterado durante o fechamento'
updated=dict(base);updated.update({x:actual[x] for x in changed});updated.update({p.relative_to(r).as_posix():sha(p) for p in files});save(r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json',updated)
print(json.dumps({'entradas_finais':len(updated),'alterados':len(changed),'novos':len(updated)-len(base),'falhas':0}))

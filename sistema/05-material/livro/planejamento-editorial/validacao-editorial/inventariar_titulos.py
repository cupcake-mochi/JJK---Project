"""Inventário somente de leitura de E007, com sugestões para revisão humana."""
from pathlib import Path
import argparse, collections, datetime, hashlib, json, re
import conferir_editorial as editorial

SUGESTOES = {
 'O ataque revela você?': 'Ataques e posição revelada',
 'O que muda com uma Trilha': 'Trilhas e usos específicos',
 'O que ficou no lugar': 'Vestígios',
 'O corpo e o que ele carrega': 'Corpos e equipamento',
 'O que o sucesso entrega': 'Resultados',
 'O alvo não tem energia': 'Alvos sem energia',
 'Os apoios do Parkour': 'Apoios do Parkour',
 'A vítima como apoio': 'Vítima como apoio',
 'A criação': 'Criação',
 'As outras rotas': 'Outras rotas',
 'O que fica fora da conta': 'Aplicações fora do repertório',
 'A conta': 'Cálculo dos pontos',
 'O que cabe': 'Aplicações permitidas',
 'O que esta Máxima acrescenta': 'Recursos desta Máxima',
 'A ficha pronta': 'Ficha pronta',
}

def suggestion(title):
 if title in SUGESTOES:return SUGESTOES[title], 'proposta contextual; confirmar no capítulo'
 match=re.match(r'^(?P<prefixo>\d+(?:\.\d+)*[.)]?\s+(?:[—–-]\s*)?)?(?:A|O|As|Os)\s+(?P<resto>.*)$',title,re.I)
 if not match:return None, 'requer título novo'
 rest=match['resto']
 if rest.lower().startswith('que '):return None, 'pergunta exige escolher assunto; não basta retirar o artigo'
 return (match['prefixo'] or '')+rest[:1].upper()+rest[1:], 'sugestão inicial; revisar sentido, não aplicar automaticamente'

def inventory():
 docs=json.loads((editorial.B/'MANUSCRITOS.json').read_text())['documentos']
 current={(editorial.P/d['arquivo']).resolve():d for d in docs}
 basenames={p.name for p in current};files=set(editorial.P.rglob('*.md'))|set(current)
 result=[];errors=[]
 for p in sorted(files):
  try:text=p.read_text()
  except OSError as exc:errors.append({'arquivo':str(p),'erro':str(exc)});continue
  relative=str(p.relative_to(editorial.P));resolved=p.resolve()
  if resolved in current:category='corrente_cadastrado'
  elif p.name in basenames or '<!-- page:' in text or 'piloto' in relative.lower():category='historico_ou_piloto'
  else:category='documentacao_ou_evidencia'
  findings=[]
  for finding in editorial.scan_title_articles(text):
   after,reason=suggestion(finding['titulo'])
   findings.append({**finding,'antes':finding['titulo'],'depois_sugerido':after,'orientacao':reason,'aplicado':False})
  result.append({'arquivo':relative,'categoria':category,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'titulos_lidos':len(editorial.title_headings(text)),'quantidade':len(findings),'itens':findings})
 counts={}
 for category in ('corrente_cadastrado','historico_ou_piloto','documentacao_ou_evidencia'):
  subset=[x for x in result if x['categoria']==category]
  counts[category]={'arquivos':len(subset),'arquivos_com_achados':sum(bool(x['quantidade']) for x in subset),'titulos':sum(x['quantidade'] for x in subset)}
 return {'data':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'regra':'E007','escopo':'Todos os .md de planejamento-editorial, incluindo o cadastro corrente, versões anteriores/pilotos e documentação/evidências separados. Não altera os arquivos.','classificacao':'Corrente é determinado exclusivamente por MANUSCRITOS.json. Histórico/piloto usa nome de manuscrito corrente, marcador de página ou caminho contendo piloto; os demais permanecem em documentação/evidências, sem ocultar achados.','limites':'Sugestões são propostas para edição contextual. Não há troca automática, atualização de evidências ou aprovação global de conteúdo. Citações, código e comentários são ignorados. À e Às não são artigos desta regra.','contagens':counts,'arquivos':result,'erros':errors}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--saida',required=True);args=parser.parse_args()
 data=inventory();Path(args.saida).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'contagens':data['contagens'],'erros':data['erros'],'saida':args.saida},ensure_ascii=False,indent=2))

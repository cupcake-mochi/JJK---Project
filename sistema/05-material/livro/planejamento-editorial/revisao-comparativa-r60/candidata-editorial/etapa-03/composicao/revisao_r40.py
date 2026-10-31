"""R40: navegação e apresentação de habilidades; nenhuma regra alterada."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'revisao-r40'
PATHS={'bastiao','vanguarda','guia','emanador','evocador','incursor'}
def aplicar(textos,blocos,capitulos,meta):
 rows=json.loads((R/'ALTERACOES-TEXTO.json').read_text())
 for r in rows:
  assert textos[r['bloco']].strip()==r['antes'].strip(),r['bloco']
  textos[r['bloco']]=r['depois']
 # A classificação usa a função de cada título; os estilos aprovados são mantidos.
 src=json.loads((B/'revisao-de-hierarquia/CLASSIFICACAO.json').read_text());old={(r['bloco'],r['titulo']):r for r in src}
 result=[r for r in src if r['bloco'].split('--')[0] not in PATHS]
 entry_extra={
 'emanador--ema-remodelar':['Remodelar'], 'emanador--ema-modulacoes':['Forçar uma Modulação'],
 'emanador--ema-artes':['Cadência Marcial','Cadência Expandida'],
 'emanador--ema-propriedades':['Chamado da Arma','Forma Mutável','Retorno Vinculado','Passo da Arma'],
 'emanador--ema-propriedades-apoio':['Âncora Gravada','Vínculo Duplo','Sentido do Vínculo','Memória da Arma'],
 'evocador--ev-principal-protecao':['Proteger a Manifestação','Adaptar o Aprimoramento'],
 'evocador--ev-principal-continuidade':['Preservar o Aprimoramento'],
 'evocador--ev-parceria-aprimoramentos':['Acompanhar a Especial','Golpe Acompanhado','Resposta ao Agressor'],
 'evocador--ev-parceria-intervencoes':['Abrir Espaço para o Parceiro','Corrigir o Ataque Conjunto'],
 'evocador--ev-parceria-cobrir':['Cobrir o Parceiro'],
 'evocador--ev-multiplas-protecao':['Dificultar o Ataque','Proteger um Aliado'],
 'evocador--ev-multiplas-conduzir':['Conduzir a Especial'],
 'evocador--ev-multiplas-retirada':['Retirada em Conjunto'],
 'incursor--inc-fluidez':['Investida','Instante Decisivo','Passo Rápido'],
 'incursor--inc-respostas':['Evasão','Reflexo','Esquiva Instintiva'],
 }
 groups={'Progressão do Caminho','Progressão da Trilha','Características','Intervenções da principal','Intervenções de Parceria','Proteção do conjunto'}
 report=[]
 for k,t in textos.items():
  if k.split('--')[0] not in PATHS:continue
  cfg=meta[k];original=cfg.get('titulos',[]);heads=[];lines=t.splitlines()
  # Marcadores que viraram título deixam de ser reconhecidos como texto auxiliar.
  if cfg.get('marcador') and '**'+cfg['marcador']+'**' not in lines:cfg.pop('marcador',None)
  for i,line in enumerate(lines):
   m=re.match(r'^(#{1,6}) (.+)$',line)
   marker=(cfg.get('marcador') and line=='**'+cfg['marcador']+'**') or (k=='incursor--inc-continuacoes' and line=='**Continuações**')
   if not m and not marker:continue
   title=m[2] if m else line.strip('*');level=len(m[1]) if m else 0
   nextp=next((l for l in lines[i+1:] if l),'')
   role=('entrada' if re.match(r'^\*\*Nível \d+\.\*\*',nextp) or title in entry_extra.get(k,[]) else 'subtopico')
   if marker or title in groups:role='grupo'
   if title=='Rajada Marcial':role='entrada'
   prior=old.get((k,title))
   if prior and prior['tratamento']=='exemplo':role='exemplo'
   if title in {'Exemplos','Exemplos de jogo'}:role='grupo'
   heads.append({'titulo':title,'nivel':level,'papel':{'entrada':'habilidade','subtopico':'subtópico','grupo':'agrupador temático','exemplo':'exemplo'}[role]})
   if level!=1:
    row={'bloco':k,'titulo':title,'tipo_original':'marker' if marker else 'h'+str(level),'tratamento':role,'nivel_editorial':2 if role in {'entrada','grupo'} else 3,'motivo':'R40: função semântica do título conferida no contexto da habilidade e da progressão.'}
    result.append(row)
    if not prior or prior.get('tratamento')!=role:report.append({'bloco':k,'titulo':title,'antes':prior,'depois':row})
  cfg['titulos']=heads
  first=re.match(r'^(#{1,6}) ',t);cfg['nivel_primeiro']=len(first[1]) if first else 0
  # Novos títulos de nível deixam de herdar contexto de uma habilidade anterior.
  cfg['contextos_por_titulo']={re.sub(r'^Nível \d+ [—–-] ', '',title):context for title,context in cfg.get('contextos_por_titulo',{}).items()}
 (R/'CLASSIFICACAO.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (R/'ALTERACOES-HIERARQUIA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 (B/'revisao-de-estrutura/HIERARQUIA.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 return rows

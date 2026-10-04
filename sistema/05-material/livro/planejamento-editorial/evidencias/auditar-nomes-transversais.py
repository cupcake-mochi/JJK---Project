from pathlib import Path
import json,re,hashlib,unicodedata
P=Path('/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/planejamento-editorial')
registered=json.loads((P/'validacao-editorial/MANUSCRITOS.json').read_text())['documentos']
def current(n):
 return not n.startswith(('regras-basicas/','regras-comuns/')) and (not n.startswith('equipamento/') or n.startswith('equipamento/lote-final/'))
files=[x['arquivo'] for x in registered if current(x['arquivo'])]
terms=['Incapacitado','Incapacitada','Mão Firme','Aviso','Reflexo','Sentença Final','Passiva Livre','Passivas Livres','Passiva','Passivas','Classe Passiva','Classes Passivas','Classe','Classes','Fundamento','Fundamentos','Refino','Refinos','Lapidação','Selo','Legado','Guarda Aberta','Identificar Feitiço','Leitura de Feitiços','Expressão da técnica','Talento','Talentos','Categoria de Efeito','Potência','Controle de Energia','Revide','Técnica','Fundamento da Técnica','Incursor','Pugilista','Malabarista']
scan={};hashes={}
for n in files:
 p=P/n;text=unicodedata.normalize('NFC',p.read_text());hashes[n]=hashlib.sha256(p.read_bytes()).hexdigest()
 for term in terms:
  rx=re.compile(r'(?<!\w)'+re.escape(term)+r'(?!\w)',re.I)
  loc=[{'linha':i,'texto':line,'ocorrencias':len(rx.findall(line))} for i,line in enumerate(text.splitlines(),1) if rx.search(line)]
  if loc:scan.setdefault(term,{})[n]=loc
r={'metodo':'Busca UTF-8 NFC, expressão inteira sem distinção de caixa. Corpus seleciona os candidatos finais e demais unidades correntes, excluindo versões de Regras básicas/comuns e Equipamento substituídas pelas consolidações finais. Históricos, relatórios, scripts, PDFs e nomes de arquivo não entram. Ocorrência lexical não comprova colisão semântica. Classe Passiva está incluída nas ocorrências de Classe; Passiva Livre nas de Passiva. Não somar totais sobrepostos.','arquivos':files,'sha256':hashes,'contagens':{t:{'ocorrencias':sum(x['ocorrencias'] for loc in scan.get(t,{}).values() for x in loc),'arquivos':len(scan.get(t,{}))} for t in terms},'ocorrencias':scan}
(P/'evidencias/NOMES-TRANSVERSAIS-CORPUS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Corpus:',len(files),'arquivos')
for t in terms:print(t,r['contagens'][t])

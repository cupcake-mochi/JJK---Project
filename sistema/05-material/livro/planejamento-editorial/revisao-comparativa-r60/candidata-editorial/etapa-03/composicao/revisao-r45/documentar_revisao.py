from pathlib import Path
import json,re,shutil,hashlib
R=Path(__file__).resolve().parent;B=R.parent;P=B.parent/'integracao-origens-v178-2026-10-13/pacote'
def save(name,x): (R/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
refs=json.loads((R/'MAPA-FONTES-DESTINOS.json').read_text());rows=json.loads((B/'ALTERACOES-R44-para-R45.json').read_text());by={r['bloco']:r for r in rows}
groups={'01-escolhas.md':'Base e estrutura','02-latente.md':'Latente','03-receptaculo.md':'Receptáculo','04-encarnado.md':'Encarnado','05-descendente.md':'Descendente','06-hibrido.md':'Híbrido','07-corpo.md':'Corpo Amaldiçoado','08-restricao-sem-energia.md':'Restrição Celestial sem energia','09-restricao-corporal.md':'Restrição Celestial com limitação corporal','10-sem-tecnica-e-exemplos.md':'Base e estrutura'}
entries=[]
for f in sorted((R/'texto-final').glob('*.md')):
 for key,content in re.findall(r'<!-- bloco:([^>]+) -->\s*(.*?)(?=<!-- bloco:|\Z)',f.read_text(),re.S):
  for h in re.findall(r'^#{1,4} (.+)$',content,re.M):
   candidates=[r for r in refs if r['group'].casefold()==groups[f.name].casefold()]
   if not candidates:
    candidates=[r for r in refs if groups[f.name].casefold() in r['group'].casefold() or r['group'].casefold() in groups[f.name].casefold()]
   matched=[r for r in candidates if h.casefold() in (P/r['path']).read_text().casefold()]
   entries.append(dict(entrada=h,bloco=key,decisoes=by[key]['item'],fontes_da_montagem=[r['path'] for r in matched or candidates],texto='texto-final/'+f.name,ficha='ORIGENS R45!A4:H12 — registro manual de escolhas; estoques em campo próprio' if 'Regeneração' not in h else 'ORIGENS R45!A14:H28 + destaque FICHA!D26:I28',automacao='aviso de elegibilidade e impedimentos informados' if h=='Regeneração Orgânica' else 'registro manual; efeito não aplicado automaticamente',verificacao='autorrevisão mecânica e leitura; não revisor independente'))
save('MAPA-DECISAO-TEXTO-FICHA.json',entries)
# Fontes curtas relevantes à rastreabilidade, copiadas sem editar.
source_paths={r['path'] for r in refs}
source_paths|={str(p.relative_to(P)) for p in (P/'ANEXOS').glob('APROVACAO-A*.md')}
source_paths|={p for p in ['03-DECISOES-APROVADAS-ETAPAS-1-A-5.md','ENTREGA-PARA-O-LIVRO/01-INDICE-DAS-REGRAS-VIGENTES.md','ENTREGA-PARA-O-LIVRO/03-PENDENCIAS-E-LIMITES-DA-ENTREGA.md','ENTREGA-PARA-O-LIVRO/04-PLANO-DE-TESTES-E-ACEITE.md'] if (P/p).is_file()}
copied=[]
for rel in sorted(source_paths):
 source=P/rel;dest=R/'fontes-de-decisao'/rel
 if not source.is_file():continue
 dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
 copied.append(dict(arquivo=str(dest.relative_to(R)),sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
save('FONTES-DE-DECISAO-SHA256.json',copied)
# Achados realmente identificados e corrigidos na própria revisão.
findings=[
('E01','origens--restricao-prenuncio','Momento operacional: explicitar rolagem de acerto, para não parecer que a Reação vai até depois do d20.','antes da rolagem de acerto'),
('E02','origens--origem-reparo','Remissão do rascunho não coincidia com a âncora compartilhada do livro.','campo--inv-reparo'),
('E03','origens--restricao-quebradico','Coordenação negativa podia parecer permitir empurrar cargas.','não empurram nem arrastam'),
('E04','origens--encarnado-beneficios','Memória Testemunha: negar explicitamente revelação do imperceptível.','não revelam algo imperceptível'),
('E05','origens--feto-beneficios','Membro Extensível: negar explicitamente ataques extras.','não concede ataques extras'),
('E06','origens--corpo-existencia','Recuperação: negar explicitamente ressurreição.','não devolve a vida'),
('V01','origens--latente-beneficios','Cabeçalho e introdução de catálogo separados da primeira opção.','Regra de composição local R45 em fluxo_continuo.py'),
('V02','origens--descendente-zenin','Clã no pé da página, componentes da marcante só na próxima.','Regra de composição local R45 em fluxo_continuo.py'),
('V03','origens--restricao-saida','Tabela de pontos separada da apresentação.','Abertura e tabela mantidas juntas; sem mudar largura ou fonte'),
('V04','consulta--consulta-glossario-4','Termo novo foi inicialmente anexado fora da ordem alfabética.','Inserido antes de Marco'),
('V05','consulta--consulta-indice-6','Entradas novas inicialmente anexadas fora da posição de consulta.','Híbrido, Marcante, Reparar e CE4 inseridos em sua posição alfabética')]
res=[]
for id,k,problem,fix in findings:
 status='corrigido; aguarda prova final' if id.startswith('V') else 'corrigido e reconferido no texto consolidado'
 if not id.startswith('V'):assert fix in by[k]['depois'],id
 res.append(dict(id=id,bloco=k,achado=problem,correcao=fix,estado=status,tipo='autorrevisão'))
save('ACHADOS-E-CORRECOES.json',res)
scenarios=json.loads((R/'CENARIOS-DE-LEITURA.json').read_text())
for s in scenarios:s.update(estado='conferido no texto final por autorrevisão',resultado='Gabarito preservado; nenhum resultado de leitor humano atribuído.',metodo='Comparação das entradas finais e das exceções com as fontes vigentes.')
save('CENARIOS-DE-LEITURA.json',scenarios)
print(len(entries),'entradas mapeadas;',len(copied),'fontes de decisão preservadas.')

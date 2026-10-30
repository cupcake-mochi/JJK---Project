"""Preparar fontes independentes e registrar cada alteração editorial da integração."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import json,re,os,hashlib,shutil

A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
entries=json.loads((A/'fontes-reunidas.json').read_text());texts={e['fonte']:(R/e['origem']).read_text() for e in entries};log=[]
def path(rel):return (T/rel).relative_to(R).as_posix()
def change(rel,old,new,why,n=1):
 key=path(rel);assert texts[key].count(old)==n,(rel,old[:100],texts[key].count(old))
 texts[key]=texts[key].replace(old,new);log.append({'fonte':key,'antes':old,'depois':new,'ocorrencias':n,'motivo':why})
def section(text,heading):
 m=re.search(r'^## '+re.escape(heading)+r'\n.*?(?=^## |\Z)',text,re.M|re.S);assert m,heading;return m.group(0)

# Método no capítulo; conversas e usos específicos no caso de aprofundamento.
rel='casos/27-convivencia-do-receptaculo.md';original=texts[path(rel)]
prefix=original[:original.index('## Quem interpreta cada voz?')]
intro='# Maia e Taru: a presença em cena\n\nMaia divide o corpo com Taru, uma presença com desejos e conhecimentos próprios. Estes exemplos aprofundam a conversa, os limites das capacidades e o que registrar para a próxima sessão.\n\nCombine a distribuição de vozes e os limites antes da cena, como explicado em [A outra voz do Receptáculo](<../07-personagens-e-tecnicas.md#a-outra-voz-do-receptaculo>). Use a [ficha de convivência](<../consultas/28-ficha-de-convivencia.md>) para guardar o acordo. O jogador continua decidindo as ações de sua personagem, dentro das regras.\n\n'
change(rel,prefix,intro,'Separar o método de interpretação, que permanece no capítulo 7, dos exemplos aprofundados.')
change(rel,section(original,'Quem interpreta cada voz?'),'','Alternativas e distribuição de vozes já estão no capítulo 7; conservar a ligação explícita e evitar repetir a exposição.')

# Acordo publicado, sem o histórico das propostas numéricas rejeitadas.
rel='consultas/92-reserva-condensada-proposta-e-comparacao.md';old=section(texts[path(rel)],'Histórico da proposta')
change(rel,old,'','Histórico de desenvolvimento fica no relatório e nas fontes preservadas; o texto de leitura conserva apenas o acordo publicado.')

# O método de recompensas já está no capítulo 8. Trazer apenas um exemplo concreto de cada resultado.
rel='08-entre-missoes.md';source37=(R/'06 - Redacao do Guia/37-recompensas-e-fechamento.md').read_text()
start='Na falha, o mestre concede metade ou nada conforme o resultado; explique a decisão.'
assert start in texts[path(rel)]
half=next(p for p in source37.split('\n\n') if p.startswith('**Exemplo de metade, decidido para o caso.**'))
zero=next(p for p in source37.split('\n\n') if p.startswith('**Exemplo de zero, decidido para o caso.**'))
anchor='### A semana de cada jogador'
change(rel,anchor,half+'\n\n'+zero+'\n\n'+anchor,'Recuperar da fonte 37 os dois exemplos concretos, sem duplicar seu método de cálculo e fechamento.')
old='A [consulta de fechamento](../37-recompensas-e-fechamento.md) reúne outros exemplos e os campos de continuidade.'
new='Use a [linha de continuidade](<consultas/16-linha-de-continuidade.md>) para registrar o resultado e o que acompanha a equipe à próxima mesa.'
change(rel,old,new,'Os exemplos foram reunidos neste capítulo; os campos de continuidade têm destino próprio.')

# A comparação com Sem Ver cabe no caso existente, sem levar o histórico de aprovação ao livro.
rel='casos/48-pacifismo-impraticavel-minuta.md'
old=next(p for p in texts[path(rel)].split('\n\n') if p.startswith('A [proposta completa]'))
new='**Comparação com Sem Ver.** A Melhoria permite escolher um alvo de posição atual conhecida sem enxergá-lo, mas conserva a trajetória da Forma e não atravessa um obstáculo sólido. Condução pela matéria usa a própria estrutura como caminho, mediante toque, até um objeto já visto e de posição conhecida. É uma exceção proposta para este Pacto, não uma permissão normal de Projétil ou Sem Ver.\n\nA informação pode estar desatualizada: se a peça conhecida tiver sido removida, o uso não produz efeito e os custos permanecem, sem localizar outro alvo. A compatibilidade da montagem com o Livro de Regras 1.0 não demonstra equilíbrio entre esse ganho e o impedimento assumido.'
change(rel,old,new,'Reunir a comparação e o caso de informação desatualizada do registro 46, preservando os limites já descritos na minuta.')

# Fichas que já eram citadas pelos casos: conservar tabelas e todos os parâmetros.
rel='casos/14-tres-maldicoes-para-a-missao.md'
change(rel,'# Base pequena de inimigos para o piloto do Livro de Regras 1.0','# Três maldições para a missão','Título dirigido à consulta das fichas.')
old=next(p for p in texts[path(rel)].split('\n\n') if p.startswith('Versão piloto'))
change(rel,old,'Três maldições originais para os exemplos do Guia. Suas fichas e conversões são experimentais; foram preparadas com o Livro de Regras 1.0 e precisam ser avaliadas nas condições de cada encontro.','Retirar data e aprovação do processo; manter o alcance experimental das fichas.')
old='A [verificação](15-verificacao-da-base-e-do-piloto.md) mostra também condições diferentes. '
change(rel,old,'A [avaliação do encontro](<57-avaliar-o-encontro-do-amontoado.md>) compara também condições diferentes. ','Trocar o registro de trabalho pelo estudo que explica as condições e seus limites.')
old=next(p for p in texts[path(rel)].split('\n\n') if p.startswith('Os quadros abaixo e as conversões são gerados'))
change(rel,old,'','A fonte de produção fica no apoio editorial; não é necessária para usar as fichas.')
old=next(p for p in texts[path(rel)].split('\n\n') if p.startswith('Referência principal:'))
new='*Base: Livro de Regras 1.0, Atributos; Turnos; Ataques; Dano na alma; Vida a zero; Fundamento; Invocações em campo; Construir invocações. A avaliação do encontro explica hipóteses e limites.*'
change(rel,old,new,'Identificar as regras sem caminho do computador ou relatório de produção.')

# Ao reunir 3a em 3.6, a remissão deixa de mandar o leitor procurar outro capítulo.
rel='03-preparar-aventuras.md'
old='[Ideias para aventuras](03a-ideias-para-aventuras.md) oferece situações, pessoas e lugares para escolher e dois exemplos de como reuni-los.'
new='As opções e os dois exemplos a seguir oferecem situações, pessoas e lugares para escolher e combinar.'
change(rel,old,new,'O conteúdo de 3a será incluído na própria seção 3.6, antes de 3.7.')

# O guia das folhas é uma ferramenta de leitura, sem avisos sobre cópias de trabalho.
rel='consultas/LEIA-ME.md';old='Os casos e as consultas têm cópias revistas; o índice abre suas fontes atuais.'
change(rel,old,'Escolha um caso pelo assunto que deseja aprofundar.','Retirar estado de produção do guia dirigido ao leitor.')

# Pente fino dos apoios e uniformização do nome da referência.
for rel,old,new in [
 ('casos/27-convivencia-do-receptaculo.md','## Quem é a outra presença?','## Conheça a presença'),
 ('casos/27-convivencia-do-receptaculo.md','## A presença em mesas com outros mestres','## Entre mesas'),
 ('casos/14-tres-maldicoes-para-a-missao.md','## O que vem do Livro de Regras 1.0 e o que está sendo proposto','## Regras e escolhas do exemplo'),
 ('casos/14-tres-maldicoes-para-a-missao.md','## Conversões conhecidas para maldições domadas','## Depois da Doma'),
 ('casos/14-tres-maldicoes-para-a-missao.md','## Uso e revisão','## Usar estas fichas'),
 ('casos/47-desenvolver-uma-ideia-de-pacto.md','no livro-base','no Livro de Regras 1.0'),
 ('casos/93-ampliar-mesclas-e-trocar-formas.md','do livro-base','do Livro de Regras 1.0')]:
 change(rel,old,new,'Pente fino: título mais direto ou nome consistente do livro de regras; sem alteração mecânica.')

# Resolver remissões das fontes antigas antes de converter para HTML.
lookup={str((R/e['origem']).resolve()):R/e['fonte'] for e in entries}
for e in entries:
 original=R/e['origem'];lookup.setdefault(str((R/'06 - Redacao do Guia'/original.name).resolve()),R/e['fonte'])
lookup[str((R/'06 - Redacao do Guia/REFERENCIAS.md').resolve())]=T/'referencias.md'
lookup[str((R/'04 - Planejamento/13-piloto-editorial-ocorrencia-sobrenatural.md').resolve())]=T/'01-sua-primeira-missao.md'
lookup[str((R/'06 - Redacao do Guia/07-preparar-o-grupo.md').resolve())]=T/'05-criar-uma-campanha.md'
assets=[];unresolved=[]
oldhtml=json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())
byid={row['id']:R/row['fonte'] for row in oldhtml['fontes']}
regex=re.compile(r'(!?\[[^\]]*\])\(<?([^)>]+)>?\)')
for e in entries:
 key=e['fonte'];original=R/e['origem'];target=R/key
 def rewrite(m):
  text,url=m.groups();u=urlsplit(url)
  if u.scheme or not u.path:return m.group(0)
  forced_fragment=None
  # Links que acabaram de ser escritos já são relativos à nova estrutura.
  candidate=(target.parent/unquote(u.path)).resolve()
  if candidate.is_relative_to(T.resolve()) and candidate.is_file():
   destination=candidate
  else:
   source=(original.parent/unquote(u.path)).resolve()
   if source.name=='casos-completos.html':destination=T/'indice-de-casos.md'
   elif source.name=='casos-da-obra-com-revelacoes.html':
    destination=T/'consultas/87-casos-da-obra-para-preparar-situacoes.md';forced_fragment=''
   elif source.suffix=='.html' and u.fragment in byid:
    if u.fragment=='s026':destination=T/'05-criar-uma-campanha.md';forced_fragment='52-vinculos-e-interesses-dos-personagens'
    else:
     destination=lookup[str(byid[u.fragment].resolve())];forced_fragment=''
   elif str(source) in lookup:destination=lookup[str(source)]
   elif source.suffix=='.svg' and source.is_file():
    destination=E/'assets/mapas'/source.name;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,destination)
    assets.append({'origem':source.relative_to(R).as_posix(),'arquivo':destination.relative_to(R).as_posix(),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'alteracao':'nenhuma'})
   else:unresolved.append({'fonte':key,'destino':url});return m.group(0)
  frag=u.fragment if forced_fragment is None else forced_fragment
  if not frag and (original.parent/unquote(u.path)).resolve()==(R/'04 - Planejamento/13-piloto-editorial-ocorrencia-sobrenatural.md').resolve():frag='15-jogue-a-missao'
  result=text+'(<'+os.path.relpath(destination,target.parent)+('#'+frag if frag else '')+'>)'
  if result!=m.group(0):log.append({'fonte':key,'antes':m.group(0),'depois':result,'ocorrencias':1,'motivo':'Remissão: destino reunido na edição integrada, sem depender da estrutura de trabalho.'})
  return result
 texts[key]=regex.sub(rewrite,texts[key])
assert not unresolved,unresolved
for key,text in texts.items():(R/key).write_text(text)
(A/'alteracoes.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
(A/'assets-copiados.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2)+'\n')
print('Fontes preparadas:',len(entries),'registros de alteração:',len(log),'assets:',len(assets))

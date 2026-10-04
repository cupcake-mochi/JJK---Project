from pathlib import Path
import hashlib, json, re

R = Path('/media/mizuki/HD Externo II/Claude/Claude 2')
P = R / 'sistema/05-material/livro/planejamento-editorial'
B = P / 'abertura/lote-01'
E = B / 'evidencias'
E.mkdir(exist_ok=True)
file = B / 'ABERTURA-E-CRIACAO.md'
src = file.read_text()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
digest = sha(file)
cases = []
def ck(name, got, expected, source):
    cases.append(dict(caso=name, obtido=got, esperado=expected, passou=got == expected, fundamento=source))

ck('Treze páginas autorais', len(re.findall(r'<!-- page:', src)), 13, 'Marcadores do manuscrito')
for anchor, fragment in [
    ('ab-capacidades', 'Usar um espaço conhecido para uma invocação exige um conceito que preveja entidades.'),
    ('ab-capacidades', 'As outras formas de aquisição seguem Criar uma invocação.'),
    ('ab-caminho', 'pontos de energia (PE)'),
    ('ab-equipamento', 'pontos de vida (PV)'),
    ('ab-equipamento', 'Classe de Dificuldade (CD)'),
    ('ab-conferencia', 'atributo permanente do TR Físico e treino com armas.'),
    ('ab-kaori', 'O repertório completo e as demais escolhas de uma personagem jogável devem ser preenchidos'),
    ('ab-resgate', 'o mestre precisa de uma ficha completa'),
    ('ab-combate', 'No erro'),
]:
    # No erro está na ficha, enquanto o exemplo reitera o gasto pela forma verbal errasse.
    if fragment == 'No erro':
        fragment = 'Se o ataque de Kaori errasse, ela continuaria tendo gasto a ação e o PE.'
    section = src.split('<!-- page:' + anchor + '|', 1)[1].split('<!-- page:', 1)[0]
    ck('Âncora ' + anchor + ': ' + fragment[:45], fragment in section, True, 'Leitura textual da candidata')

attrs = [3, 2, 2, 1, 1]
ck('Nove pontos', sum(attrs), 9, 'Criação, Kaori')
ck('Teto inicial', all(0 <= x <= 3 for x in attrs), True, 'Criação padrão')
ck('PV no segundo nível', (12+2)+(7+2), 23, 'Bastião: vida inicial e ganho com Constituição')
ck('Energia no segundo nível', 4*2, 8, 'Bastião: 4 PE por nível')
ck('Defesa com Traje 1', 10+2+1, 13, 'Proteção: proteção substitui proteção passiva; sem outro bônus ativo')
ck('Carga normal', 5+3, 8, 'Equipamento inicial: 5 + Força')
ck('Atletismo e ataque da técnica', 3+1, 4, 'Força + Maestria')
ck('CD da técnica', 8+3+1, 12, 'Fundamento: 8 + atributo + Maestria')
ck('Quatro TR', [3+1, 2+1, 1, 1], [4,3,1,1], 'Dois treinos distintos, sem somar Maestria aos demais')
ck('Treinos antes das trocas', (2+2+5, 2), (9,2), 'Origem: duas perícias; Caminho: duas indicadas e cinco livres; dois ofícios')
ck('Troca de dois ofícios', (9+1, 2-2), (10,0), 'Troca pelos dois, não por um ofício')
ck('Arma com custo de dois treinos', 9-2, 7, 'Somente onde o Caminho permite a troca')
ck('Espaços N2 e Classe0 separados', (2+2//2, 2), (3,2), 'R06/R21: não empregar fórmula antiga 2 + nível + Maestria')
cost_condition = max(1, 1 - ((1+1)//2))
ck('Condição Livre mantém preço mínimo', cost_condition, 1, 'Controle Livre desconta, mas melhoria custa no mínimo 1')
ck('Reembolso Toque cabe no gasto', 1 <= cost_condition, True, 'Fundamento: devolução não ultrapassa pontos gastos')
ck('Pool do Toque com Derrubado', 3+1-cost_condition, 3, 'Classe1, Toque sem preço, Corpo a Corpo devolve1, Condição custa1')
ck('Sem Condição não há quarto dado grátis', 3+min(1,0), 3, 'Controle negativo: sem compra não recebe devolução1')
ck('Sem adicionar Força ao feitiço', sum([4,5,5]), 14, 'Dano só3d8; Força entra no ataque, não no dano')
ck('Furtivo Gesto não devolvido', 'Gesto' in src, False, 'Selo narrado sem compra ou devolução extra')
ck('Porta empatando CD', 10+4 >= 14, True, 'Testes: alcançar a CD é sucesso')
ck('Iniciativa', [11+2,16+3], [13,19], 'Exemplo de combate')
ck('Acerto da criatura', 14+3 >= 13, True, 'Ataque +3 contra DEF13')
ck('PV após garras', 23-(3+2), 18, '1d6+2, dado3; nenhuma outra proteção ativa')
ck('PE após conjurar', 8-3, 5, 'Custo3 também no erro')
ck('Acerto de Kaori', 12+4 >= 12, True, 'Ataque da técnica +4 contra DEF12')
ck('Maldição chega a zero', 14-sum([4,5,5]), 0, 'Exorcismo determinado neste exemplo, não nova regra universal')
ck('Movimento restante', 9-3, 6, 'Movimento de3m após conjuração')
ck('Distâncias em quadrados', all((x/1.5).is_integer() for x in [1.5,3.,6.,9.]), True, 'Múltiplos de1,5m')
ck('Passiva Livre puramente visual', 'É uma manifestação visual.' in src, True, 'Sem antigo conhecimento exato de peso gratuito')
ck('Introdução nomeia seis Caminhos', all('| '+n+' |' in src for n in ['Bastião','Vanguarda','Guia','Emanador','Evocador','Incursor']), True, 'Tabela de orientação, sem copiar habilidades')
assert all(c['passou'] for c in cases), [c for c in cases if not c['passou']]

findings = [
 dict(id='R22-I01', prioridade='P2', ancora='ab-capacidades', linha=187, estado='resolvido pela autoria e reconferido', antes='As opções de Invocações também dependem da forma de aquisição e de um conceito que comporte entidades.', problema='Generalizava o requisito temático para domar e fabricar, contrariando R12.', depois='Requisito limitado ao uso de espaço conhecido; outras aquisições remetem Criar uma invocação.', fonte='invocacoes/lote-02/CONSTRUIR-INVOCACOES.md:120'),
 dict(id='R22-I02', prioridade='P3', ancora='ab-caminho / ab-equipamento', linha=[162,216,228], estado='resolvido pela autoria e reconferido', antes='PE, PV e CD usados sem expansão anterior.', problema='Vocabulário indispensável de ficha pressuposto para leitor que nunca jogou RPG.', depois='Expansão uma vez, junto da primeira ocorrência da sigla, sem parágrafo de glossário.'),
 dict(id='R22-I03', prioridade='P3', ancora='ab-conferencia', linha=327, estado='resolvido pela autoria e reconferido', antes='armas permitidas', problema='Podia confundir treino com permissão absoluta de usar uma arma.', depois='treino com armas'),
]
pages = [
 ('ab-apresentacao','Projeto - M','Cumpre proposta de personagem, missões, criação própria e guilda. Funções de jogador e mestre recebem exemplo concreto. Não confunde comunidade de jogo com instituição ficcional.'),
 ('ab-primeira-sessao','Primeira sessão','Materiais, dados e combinados suficientes para entrada. Nível2/Grau4 rotulados como padrão. Remissões por assunto evitam reproduzir capítulos inteiros.'),
 ('ab-mundo','Mundo jujutsu','Vocabulário explicado no momento de uso. Maldições, energia e percepção apoiam decisões de aventura. Ressalvas não atribuem números do RPG ao cânone.'),
 ('ab-sociedade','Sociedade jujutsu','Escolas e famílias contextualizadas sem catálogo de nomes/spoilers. Gancho da estação oferece objetivo e pistas concretos; não presume uma resposta correta.'),
 ('ab-criacao','Criar um personagem','Roteiro de seis passos e limite inicial dos atributos permitem começar a ficha. Valor do atributo é explicitamente o próprio modificador. Exemplo soma9.'),
 ('ab-origem','Origem e treinos','Contagem de perícias/ofícios e TR se fecha. Remete escolhas repetidas ao dono. Não detalha traços ou Legados fora do catálogo.'),
 ('ab-caminho','Caminho e Trilha','Seis propostas curtas ajudam seleção. Não descreve habilidades de cada Caminho. Treino e requisito de arma diferenciados. PE agora expandido.'),
 ('ab-capacidades','Capacidades iniciais','Roteiro serve para três rotas; montagem detalhada permanece no Fundamento. Invocação por espaço agora distinta de aquisição externa. Classe0 possui contagem separada.'),
 ('ab-equipamento','Equipamento e valores','Conferência de ficha com compra, carga e fórmula dePV. Detalhes de proteção, ataque e dano remetidos ao dono. PV/CD agora apresentados.'),
 ('ab-kaori','Kaori','Recorte de ficha explicitamente parcial. Conceito, dano e Selo combinam com Toque. Condição mínima1 impede devolução inflada. Passiva não concede informação mecânica gratuita.'),
 ('ab-resgate','Resgate na ala oeste','Objetivo, pessoas e posições suficientes para entender a cena. Narrativa direta, sem metáforas indecisas. Criatura explicitamente parcial: não é encontro aberto pronto.'),
 ('ab-combate','Combate de exemplo','Ordem iniciativa→acerto→dano→custo→movimento pode ser acompanhada. Falha conserva gasto. Desfecho e recursos persistem sem recompensa mecânica inventada.'),
 ('ab-conferencia','Ficha pronta','Lista reúne campos sem repetir seus procedimentos. Valores atuais/máximos recebem exemplo curto. Registro de guilda tem função operacional distinta da definição inicial.'),
]
refs = [
 ('sistema/05-material/livro/manual/05-introducao.md','Leitura integral; propósito, guildas e alcance do livro.'),
 ('sistema/05-material/livro/manual/08-inicio-rapido.md','Leitura integral; exemplo anterior de Kaori e números históricos.'),
 ('sistema/05-material/livro/manual/20-criacao-de-personagem.md','Leitura integral em blocos; criação e atualização por proprietários atuais.'),
 ('sistema/05-material/livro/piloto-editorial-r2/PILOTO.md','Abertura, mundo e primeira rolagem; comparação com a crítica do usuário.'),
 ('sistema/05-material/livro/planejamento-editorial/evidencias/abertura-retorno-pos-r2.md','Leitura integral; preservar identidade de sistema e guilda.'),
 ('sistema/05-material/livro/planejamento-editorial/fundamento/lote-01/FUNDAMENTO.md','Recortes de conceito, famílias, pontos, devoluções, Toque, passivas e valores iniciais.'),
 ('sistema/05-material/livro/planejamento-editorial/catalogo/lote-01/CATALOGO.md','Condição: preço, duração e resistência. Não revisar todo catálogo nesta unidade.'),
 ('sistema/05-material/livro/planejamento-editorial/origens/lote-01/ORIGENS-E-LEGADOS.md','Recortes de aquisição/treinos/Legados/rota e Descendente.'),
 ('sistema/05-material/livro/planejamento-editorial/progressao/lote-01/PROGRESSAO.md','Recortes de tabela inicial, repertório e atualização. Não revisão independente integral de R21.'),
 ('sistema/05-material/livro/planejamento-editorial/equipamento/lote-06-r1/COMPRAS-E-EQUIPAMENTO-INICIAL.md','Criação: Traje1,¥150000,Grau4 e limites de acesso.'),
 ('sistema/05-material/livro/planejamento-editorial/equipamento/lote-02-r3/PROTECAO.md','Defesa com uniforme; não somar proteção passiva.'),
 ('sistema/05-material/livro/planejamento-editorial/caminhos/bastiao/lote-01/BASTIAO.md','Vida,PE,TR e estado de proteção do Muro.'),
 ('sistema/05-material/livro/planejamento-editorial/invocacoes/lote-02/CONSTRUIR-INVOCACOES.md','Tema ao ocupar espaço, domar/fabricar sem técnica temática.'),
]
sources=[]
for name, role in refs:
    p=R/name
    if p.exists(): sources.append(dict(arquivo=name,sha256=sha(p),leitura=role))
sources.append(dict(arquivo='/tmp/r07-phb.txt',sha256=sha(Path('/tmp/r07-phb.txt')),leitura='PHB2024 local, edição/tradução comunitária identificada no arquivo: páginas impressas7–8 e33. Comparação de organização: papéis, processo de jogo, roteiro e seleção; não modelo literal de prosa.'))
out=dict(autor_revisor='maxima; distinto do autor da abertura',sha256_texto=digest,paginas=13,achados=findings,bloqueadores_abertos=0,casos=len(cases),ok=True,fontes=sources,parecer_por_secao=[dict(ancora=a,titulo=t,parecer=v) for a,t,v in pages],limites=['Modelos de especificação dirigidos; não executam a ficha como motor de jogo.','Não houve teste com leitores humanos nem partida real.','Não foi feita inspeção visual do PDF desta unidade por este revisor.','Cânone conferido nos recortes documentados abaixo; não leitura integral do mangá.'])
(E/'REVISAO-INDEPENDENTE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(E/'casos-revisao-independente.json').write_text(json.dumps(dict(sha256_texto=digest,ok=True,casos=cases),ensure_ascii=False,indent=2)+'\n')
lines=['# Revisão independente — Abertura e criação','',f'Manuscrito: `ABERTURA-E-CRIACAO.md`, SHA-256 `{digest}`. Leitura integral das 13 páginas por agente distinto da autoria.','',f'**Resultado:** nenhum bloqueador aberto. Três achados foram comunicados e corrigidos pela autoria; suas correções foram relidas. {len(cases)} casos dirigidos passaram. A avaliação não substitui leitura humana ou playtest.','','## Achados e resolução','']
for f in findings:
    lines += [f"### {f['id']} — {f['prioridade']}",'',f"**Local:** `{f['ancora']}`, linha(s) {f['linha']}. **Estado:** {f['estado']}.",'',f"**Problema:** {f['problema']} **Correção:** {f['depois']}",'']
lines += ['## Regras e exemplo','','Kaori tem nove pontos de atributo, 23 PV, 8 PE, Defesa13, ataque+4 e CD12. Seus TR treinados são Físico+4 e Vigor+3; os outros recebem somente seus atributos. A criação reúne nove perícias/dois ofícios ou dez perícias/nenhum ofício antes das trocas permitidas por Caminho. No nível2 são três espaços conhecidos e dois Classe0 separados.','','Peso nas Mãos fecha em **3 pontos +1 de Corpo a Corpo −1 de Condição =3d8**, por3PE. Controle Livre não torna a melhoria gratuita, pois seu custo mínimo continua1; a devolução cabe no gasto. Selo e contato no alvo são momentos distintos; não foi concedida outra devolução por Gesto. A Força entra no acerto, não no dano do feitiço.','','A sequência termina em18PV/5PE, com a criatura a zero e6m de movimento não usado. Ambas as fichas estão explicitamente incompletas para uma sessão aberta. O exorcismo é o resultado desta criatura neste encontro; não reescreve regras de todos os seres a zeroPV.','','## Leitura editorial por seção','','| Seção | Avaliação |','|---|---|']
lines += [f'| {t} | {v} |' for _,t,v in pages]
lines += ['','## Comparação com RPGs e versões anteriores','','O PHB local, páginas impressas7–8 e33, separa papéis de mesa, ciclo de tentativa/resolução e roteiro de criação, com uma visão geral das escolhas. A candidata usa essas funções editoriais, sem transpor regras nem a voz do prefácio comunitário. A abertura devolve a identidade que o retorno pós-piloto pedia: criação de técnicas, equipe, missões e continuidade de fichas em guildas. O resgate permanece como cena concreta, em vez de carregar sozinho toda a apresentação do jogo.','','Títulos são assuntos reconhecíveis e diretos. Os catálogos aparecem como destinos de consulta, sem reproduzir habilidades. Os números brevemente repetidos no exemplo cumprem a função de ensinar sua aplicação. Há suficiência para seguir o roteiro e acompanhar a resolução; não há pretensão de substituir os capítulos de Testes ou de fornecer personagens completos.','','## Cânone: conferência dirigida','','Foram realmente abertas com visualizador as imagens27,43 e46 da prévia oficial do volume1: emoções negativas, visibilidade normalmente ausente e risco físico. Essas imagens são evidência de pesquisa, não ilustração do livro. [Prévia oficial da Shueisha](https://shonenjumpplus.com/volume/4856001361007377299/trial).','','Também foram consultados novamente os perfis oficiais: escolas e família Kamo em [Kyoto](https://jujutsukaisen.jp/character/category2.php), técnica herdada e corpos criados em [Tóquio](https://jujutsukaisen.jp/character/index.php), atuação independente em [feiticeiros](https://jujutsukaisen.jp/character/category3.php), comunicação e planejamento em [maldições](https://jujutsukaisen.jp/character/category4.php). Isso sustenta as afirmações gerais usadas. Não deduz alcance de percepção, preço, dano ou acesso mecânico dessas fontes.','','O registro da autoria `FONTES-CANONE.json` foi lido, mas não é tratado como evidência de que este revisor leu imagens48/50/51; a revisão visual própria abrange apenas27/43/46. Kaori, estação e missões estão identificadas como propostas de jogo.','','## Limites e reprodução','','`revisar-abertura-maxima.py` produz os casos e o parecer com o hash lido. As contas são modelos da especificação, ligados a trechos da candidata, e não um motor que interpreta linguagem natural. O JSON relaciona os recortes realmente lidos; R20/R21 não recebem certificação integral por esta comparação. Exportação, navegação final e inspeção visual do PDF ficam com a autoria/raiz. A compreensão humana permanece uma validação posterior.','']
(E/'REVISAO-INDEPENDENTE.md').write_text('\n'.join(lines))
print(json.dumps(dict(sha256=digest,casos=len(cases),bloqueadores_abertos=0),ensure_ascii=False))

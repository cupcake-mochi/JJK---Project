"""Etapa 2: papéis dos títulos e metadados, sem alteração de mecânica."""
from pathlib import Path
import json, re

B = Path(__file__).resolve().parent
R = B / 'revisao-de-estrutura'

FAMILIAS = ['Alcance', 'Área', 'Mira', 'Controle', 'Auxiliares', 'Castigo', 'Tempo', 'Marca', 'Amparo']
FAMILIA_BLOCOS = {
 'cat-alcance':'Alcance', 'cat-movimento':'Alcance',
 'cat-area':'Área', 'cat-area-continua':'Área',
 'cat-mira':'Mira', 'cat-defesas':'Mira',
 'cat-controle':'Controle', 'cat-obstaculos':'Controle',
 'cat-auxiliares':'Auxiliares', 'cat-auxiliares-apoio':'Auxiliares',
 'cat-castigo':'Castigo', 'cat-castigo-dano':'Castigo',
 'cat-tempo':'Tempo', 'cat-tempo-duracao':'Tempo',
 'cat-marca':'Marca', 'cat-marca-recursos':'Marca',
 'cat-amparo':'Amparo', 'cat-amparo-protecao':'Amparo',
}
CONTINUACOES_FAMILIA = {
 'cat-movimento', 'cat-area-continua', 'cat-defesas', 'cat-obstaculos',
 'cat-auxiliares-apoio', 'cat-castigo-dano', 'cat-tempo-duracao',
 'cat-marca-recursos', 'cat-amparo-protecao',
}
TEMATICOS_CAMINHOS = {
 'bas-defesa','bas-aliados','bas-casca','bas-mao','bas-oportunista',
 'van-conducoes','van-conclusoes','van-escola','van-avanco','van-feiticos',
 'van-bote','van-yumi-conducoes','van-yumi-avanco','van-besta-conducoes',
 'van-besta-avanco','van-fogo-conclusoes','van-fogo-avanco','van-executor-avanco',
 'guia-progressao','guia-aberturas','guia-planos','guia-modelos','guia-obras-maiores',
 'guia-emergencia','guia-tratamento','guia-emergencia-cuidado',
 'ema-modulacoes','ema-familiares','ema-forma','ema-artes','ema-propriedades',
 'ema-propriedades-apoio','ema-manifestacao','ema-repetir','ema-contraponto','ema-fluxo',
 'ev-usos','ev-aprimoramentos','ev-intervencoes','ev-posicao','ev-preparacao',
 'ev-principal-especial','ev-principal-protecao','ev-parceria-aprimoramentos',
 'ev-parceria-complementar','ev-parceria-intervencoes','ev-multiplas-protecao',
 'ev-multiplas-aprimoramentos','ev-turnos','inc-respostas','inc-fluidez-avancada',
 'inc-interceptar',
}
EXEMPLOS = {
 'ab--ab-kaori':'Kaori', 'ab--ab-resgate':'Resgate na ala oeste',
 'fundamento--passagem':'Passagem de Papel', 'fundamento--retirada':'Retirada de Emergência',
 'rotas--rota-fisga':'Fisga', 'rotas--rota-bancada':'Bancada',
 'rotas--rota-redoma':'Redoma', 'rotas--rota-sutura':'Sutura Fria', 'rotas--rota-espinho':'Espinho',
 'poderes--galeriavidro':'Galeria de Vidro', 'poderes--salatregua':'Sala de Trégua',
 'construcao--entidade-cao':'Cão de sombra', 'construcao--entidade-vigia':'Vigia de papel',
 'fabricacao--fab-exemplo':'Talismã de vigia',
}
PARENTES = {
 'aptidoes--apt-energia-positiva': ('aptidoes--apt-reversa','Energia Reversa'),
 'aptidoes--apt-simples-duracao': ('aptidoes--apt-simples','Domínio Simples'),
 'fundamento--maximadano': ('fundamento--maxima','Técnica Máxima'),
 'fundamento--limitesmaxima': ('fundamento--maxima','Técnica Máxima'),
 'incursor--inc-redirecionar-resolucao': ('incursor--inc-redirecionar','Corpo em Harmonia'),
 'construcao--entidade-cao-habilidades': ('construcao--entidade-cao','Exemplo: Cão de sombra'),
 'construcao--entidade-vigia-habilidades': ('construcao--entidade-vigia','Exemplo: Vigia de papel'),
}
RAIZES = {
 'geral': {'atributos','turnos','ataques','movimento','perceber','mundo'},
 'dano': {'dano','condicoes','cura','zero','descansos'},
 'ritual': {'ritual','pactos'},
 'campo': {'inv-campo','inv-ciclo','inv-especial','inv-defesa','inv-talisma','inv-queda','inv-carga'},
 'construcao': {'entidades-criar','entidades-aquisicao','entidades-definicao','entidades-basicas',
                'entidades-especiais','entidades-passivas','entidade-cao','entidade-vigia','entidades-conferencia'},
 'fabricacao': {'fab-entidades'},
 'rotas': {'rotas','rota-marcial','rota-sem-tecnica','rota-lapidacao','rota-bencaos'},
}
INDICE_ESPECIFICO = [
 ('Aguentar','dano--zero'),('Aquecer','catalogo--cat-restricoes-uso'),
 ('Atrasar','catalogo--cat-restricoes-conjuracao'),('Cena','dano--usos'),
 ('Cobertura','geral--defesa'),('Condicional','catalogo--cat-restricoes-uso'),
 ('Crítico','geral--critico'),('Dívida','catalogo--cat-restricoes-uso'),
 ('Estabilizar','dano--socorro'),('Fluxo','catalogo--cat-passivas-2-recursos'),
 ('Gesto','catalogo--cat-restricoes-conjuracao'),('Guarda','catalogo--cat-auxiliares-apoio'),
 ('Identificar Feitiço','catalogo--cat-marca-recursos'),('Onda','fundamento--amparoformas'),
 ('Parado','catalogo--cat-restricoes-conjuracao'),('Remenda','catalogo--cat-amparo'),
 ('Uma Vez','catalogo--cat-restricoes-uso'),
]

def aplicar(textos, blocos, capitulos):
    before = dict(textos)
    motives = {k:[] for k in textos}
    metadata = {}
    selections = json.loads((B/'MARCADORES.json').read_text())
    trilhas = set(selections['trilhas'])
    caminhos = {group['blocks'][0].key for ch in capitulos for group in ch['grupos'] if group['caminho']}
    caminho_docs = {blocos[k].doc for k in caminhos}

    # Um exemplo de Abre Ferida estava depois de Firmeza, no mesmo bloco.
    k = 'catalogo--cat-auxiliares'
    example = next(l for l in textos[k].splitlines() if l.startswith('> **Exemplo:') and 'Abre Ferida' in l)
    textos[k] = textos[k].replace('\n\n'+example, '', 1)
    textos[k] = textos[k].replace('\n\n## Sobrecarga', '\n\n'+example+'\n\n## Sobrecarga', 1)
    motives[k].append('Exemplo de Abre Ferida colocado imediatamente após essa Melhoria; texto e números preservados.')

    for ch in capitulos:
        route = ch['titulo']; origin = None; main = None; example_context = None
        for group in ch['grupos']:
            if group['caminho']: route = group['blocks'][0].title
            for block in group['blocks']:
                k, a, doc = block.key, block.anchor, block.doc
                lines = textos[k].splitlines(); title = lines[0][2:]
                first_level = 1; role = 'seção'; parent = None
                child_level = 2; context = route; remove_first = False; thematic = False
                if doc in caminho_docs:
                    if k in caminhos: role = 'Caminho'; first_level = 1; main = title
                    elif k in trilhas: role = 'Trilha'; first_level = 1; main = title
                    elif a in TEMATICOS_CAMINHOS:
                        role = 'marcador temático'; thematic = True; child_level = 2
                    else: role = 'habilidade ou procedimento'; first_level = 2; child_level = 3
                    context = route + (' / '+main if main and main != route else '')
                elif doc == 'catalogo':
                    if a in FAMILIA_BLOCOS:
                        family = FAMILIA_BLOCOS[a]; context = 'Família: '+family
                        role = 'Família' if a not in CONTINUACOES_FAMILIA else 'continuação de Família'
                        remove_first = a in CONTINUACOES_FAMILIA
                        child_level = 2
                        if remove_first:
                            parent = next('catalogo--'+x for x,v in FAMILIA_BLOCOS.items() if v == family)
                    elif a == 'cat-passivas-2-protecao':
                        remove_first = True; role = 'continuação do catálogo'; context = 'Talentos de Categoria 2'
                        parent = 'catalogo--cat-passivas-2-recursos'
                    else: context = title
                elif doc == 'origens':
                    if a.startswith('origem-') and a in {'origem-latente','origem-receptaculo','origem-descendente','origem-encarnado','origem-feto','origem-sem-tecnica','origem-corpo','origem-restricao'}:
                        origin = title; role = 'Origem'
                    elif a not in {'origens','origem-escolhas','legados','legado-criar','legados-exemplos'}:
                        first_level = 2; child_level = 3; role = 'detalhe da Origem'
                    context = ('Origem: '+origin) if origin and first_level == 2 else title
                elif doc == 'aptidoes':
                    if a not in {'apt-refino','apt-marcos','apt-catalogo','apt-protecao-dominios'}:
                        first_level = 2; child_level = 3; role = 'Aptidão'
                    context = title
                elif doc in RAIZES:
                    if a not in RAIZES[doc]: first_level = 2; child_level = 3; role = 'procedimento ou entrada'
                    elif k not in EXEMPLOS: main = title
                    context = main or route
                elif doc == 'fundamento' and a in {'maximadano','limitesmaxima'}:
                    first_level = 2; child_level = 3; role = 'detalhe da Técnica Máxima'
                if k in PARENTES:
                    parent, context = PARENTES[k]
                    first_level = 2 if doc not in {'aptidoes','incursor'} else 3
                    child_level = 3; role = 'continuação ou caso específico'
                    if k == 'incursor--inc-redirecionar-resolucao':
                        lines[0] = '# '+title+' (continuação)'
                        motives[k].append('Cabeçalho identifica a continuação da resolução, sem apresentar uma segunda habilidade.')
                if k in EXEMPLOS:
                    lines[0] = '# Exemplo: '+EXEMPLOS[k]
                    role = 'exemplo completo'; first_level = 1; child_level = 2
                    context = 'Exemplo: '+EXEMPLOS[k]; example_context = context
                    motives[k].append('O título identifica explicitamente um modelo de exemplo, preservando seu nome e conteúdo.')
                elif parent and parent in EXEMPLOS:
                    context = 'Exemplo: '+EXEMPLOS[parent]
                elif doc == 'ab' and a in {'ab-combate'}:
                    context = 'Exemplo: Resgate na ala oeste'
                if k == 'incursor--inc-continuacoes':
                    remove_first = True; child_level = 2; role = 'regras compartilhadas e habilidade'
                    motives[k].append('Remove o título duplicado de Lançamento Cruzado; mantém Continuações e a entrada própria da habilidade.')
                new_lines = []; headings = []
                for n, line in enumerate(lines):
                    if n == 0 and remove_first:
                        motives[k].append('Remove a divisão editorial intermediária; o bloco continua vinculado à categoria existente e conserva sua âncora.')
                        continue
                    match = re.match(r'^(#{1,6}) (.+)$', line)
                    if match:
                        label = match[2]; level = first_level if n == 0 else child_level + max(0, len(match[1])-2)
                        if doc=='catalogo' and label in {'Duração e usos','Ataques seguintes'}:level=3
                        if n == 0 and thematic:
                            new_lines.append('**'+label+'**')
                            headings.append({'titulo':label,'papel':'marcador temático','nivel':0})
                            motives[k].append('Agrupamento editorial vira marcador de contexto; habilidades mantêm títulos próprios.')
                            continue
                        if k == 'incursor--inc-continuacoes' and label == 'Continuações':
                            new_lines.append('**Continuações**'); continue
                        # Preço ocupa sempre a linha imediatamente abaixo do nome.
                        cost = None
                        if doc == 'catalogo' and a in FAMILIA_BLOCOS and n > 0:
                            special = re.fullmatch(r'Concentrada\s+-\s+Leve / Duradoura\s+-\s+Média', label)
                            priced = re.fullmatch(r'(.+?)\s+-\s+(Leve|Média|Pesada)', label)
                            if special: label = 'Concentrada / Duradoura'; cost = 'Concentrada - Leve; Duradoura - Média'
                            elif priced: label, cost = priced.groups()
                        if doc == 'rotas' and n > 0:
                            ce = re.fullmatch(r'(.+?)\s*[—–-]\s*Categoria de Efeito (\d+)', label)
                            if ce:
                                label, value = ce.groups(); cost = ('CE', value)
                        new_lines.append('#'*level+' '+label)
                        headings.append({'titulo':label,'papel':role if n==0 else 'entrada' if child_level==2 and doc=='catalogo' else 'subtópico','nivel':level})
                        if cost:
                            meta = '**Categoria de Efeito: '+cost[1]+'.**' if isinstance(cost,tuple) else '**Preço: '+cost+'.**'
                            new_lines.extend(['',meta]); motives[k].append('Metadado separado do título e colocado imediatamente abaixo do nome.')
                    elif doc == 'catalogo' and (a in FAMILIA_BLOCOS or a == 'cat-proprio') and re.match(r'^\*\*Preço: .*?\.\*\*\s+\S', line):
                        price, rest = re.match(r'^(\*\*Preço: .*?\.\*\*)\s+(.+)$',line).groups()
                        new_lines.extend([price,'',rest]); motives[k].append('Preço destacado em linha própria, sem misturar metadado e descrição.')
                    else: new_lines.append(line)
                revised = '\n'.join(new_lines)
                if revised != textos[k] and not motives[k]:
                    motives[k].append('Níveis dos títulos ajustados à relação entre categoria, entrada e procedimento, sem mudar os parágrafos.')
                textos[k] = revised
                metadata[k] = {'bloco':k,'capitulo':ch['numero'],'titulo_original':title,
                    'papel':role,'contexto':context,'parent':parent,'marcador':title if thematic else None,
                    'titulos':headings,'nivel_primeiro':first_level,'sem_titulo_inicial':remove_first}

    destinations=[]
    for i,(term,target) in enumerate(INDICE_ESPECIFICO,1):
        alias=f'indice-especifico-{i:02d}'
        occurrences=0
        for k in textos:
            if not k.startswith('consulta--consulta-indice-'):continue
            old=f'[{term}](#{target})'; new=f'[{term}](#{alias})'
            if old in textos[k]:
                occurrences+=textos[k].count(old);textos[k]=textos[k].replace(old,new)
                motives[k].append('Índice aponta para o título específico procurado, conservando o termo e recalculando a página.')
        assert occurrences==1,(term,occurrences)
        assert re.search(r'^#{1,6} '+re.escape(term)+r'\s*$',textos[target],re.M),(term,target)
        destinations.append({'termo':term,'bloco':target,'alias':alias})
    (R/'DESTINOS-INDICE.json').write_text(json.dumps(destinations,ensure_ascii=False,indent=2)+'\n')
    records=[]
    for k in before:
        if before[k] != textos[k]:
            records.append({'id':f'E{len(records)+1:03d}','bloco':k,'antes':before[k],'depois':textos[k],
                'motivo':' '.join(dict.fromkeys(motives[k])),'altera_regras':False})
    (R/'TRANSFORMACOES-TEXTO.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    (R/'HIERARQUIA.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
    return records, metadata

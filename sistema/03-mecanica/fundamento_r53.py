"""Contas da montagem comum R53, com preços lidos do livro atual.

O módulo confere orçamento, funções, distribuição e acessos. Uma aprovação
numérica ainda exige conferir os requisitos e os procedimentos das peças.
Classe 0 e máximas têm procedimentos próprios e não entram nesta conta.
"""
from functools import lru_cache
import livro

FUNCOES_VARIAVEIS = {'dano', 'cura', 'vida_temporaria'}
AREAS = {'Explosão', 'Aura', 'Cone', 'Linha'}


@lru_cache(maxsize=1)
def tabela_pessoal():
    return {int(r['Classe']): r for r in livro.tabela(
        livro.por_bloco('fundamento', 'pontos'), 'Classe', 'Pontos / PE', 'Leve', 'Média', 'Pesada')}


def preco(classe, faixa):
    if type(classe) is not int or classe not in range(1, 8):
        raise ValueError('A conta comum exige Classe inteira de 1 a 7.')
    return int(tabela_pessoal()[classe][faixa])


def desconto(classe, entidade=False):
    return max(1, classe // 2) if entidade else (classe + 1) // 2


@lru_cache(maxsize=14)
def orcamento(classe, entidade=False):
    if entidade:
        linhas = livro.tabela(livro.por_bloco('construcao', 'entidades-especiais'),
                             'Classe', 'Pontos', 'PE')
        return int(next(r['Pontos'] for r in linhas if int(r['Classe']) == classe))
    return int(tabela_pessoal()[classe]['Pontos / PE'])


def max_melhorias(classe):
    return 2 if classe <= 2 else 3 if classe <= 4 else 4


def calcular(dados):
    """Recebe uma ficha de conta; preços das peças precisam ser faixas publicadas.

    Melhorias: nome, faixa, família e opções relevantes. Para peças com preço
    variável, informe a modalidade/condição ou o preço aprovado. A saída mantém
    pontos sem uso e os limites, sem redistribuir parcelas automaticamente.
    """
    campos = {'nome', 'classe', 'forma', 'funcoes', 'entidade', 'coletivo',
              'somente_pessoal', 'livres', 'fechadas', 'melhorias', 'restricoes',
              'distribuicao', 'controle'}
    if set(dados) - campos:
        raise ValueError('Campos fora do esquema R53: ' + ', '.join(sorted(set(dados)-campos)))
    classe = dados['classe']
    preco(classe, 'Leve')
    forma = dados['forma']
    if forma not in livro.formas():
        raise ValueError(f'Forma indisponível: {forma}')
    funcoes = set(dados.get('funcoes', ['dano']))
    if funcoes - (FUNCOES_VARIAVEIS | {'guarda', 'impulso', 'firmeza', 'controle', 'efeito', 'movimento', 'parede'}):
        raise ValueError('Função desconhecida na conta comum.')
    entidade = dados.get('entidade', False)
    coletivo = dados.get('coletivo', forma in AREAS)
    pessoal = dados.get('somente_pessoal', False)
    livres, fechadas = set(dados.get('livres', [])), set(dados.get('fechadas', []))
    erros = []
    if livres & fechadas:
        erros.append('Uma Família aparece Livre e Fechada.')
    if not (livres | fechadas) <= set(livro.familias()):
        erros.append('Família desconhecida.')
    if {'cura', 'vida_temporaria'} & funcoes and 'Amparo' in fechadas:
        erros.append('Amparo Fechada impede a função escolhida.')
    if forma in AREAS and 'Área' in fechadas:
        erros.append('Área Fechada impede a Forma.')
    if coletivo and {'guarda', 'impulso', 'firmeza'} & funcoes and 'Área' in fechadas:
        erros.append('Área Fechada impede benefício coletivo.')
    cat = livro.catalogo()
    melhorias = dados.get('melhorias', [])
    restricoes = dados.get('restricoes', [])
    if len(melhorias) > max_melhorias(classe):
        erros.append('Quantidade de Melhorias excedida.')
    if len(restricoes) > 2:
        erros.append('Quantidade de Restrições excedida.')
    pago, compras = 0, []
    for m in melhorias:
        entrada = cat.get(m['nome'])
        if not entrada or entrada['tipo'] != 'Melhoria':
            erros.append(f'Melhoria desconhecida: {m["nome"]}')
            continue
        faixa = m.get('faixa', entrada['preco'])
        familia = entrada.get('familia')
        if m['nome'] == 'Efeito Próprio':
            familia = m.get('familia')
        elif 'familia' in m and m['familia'] != familia:
            erros.append(f'Família diferente da publicada: {m["nome"]}')
        if familia in fechadas:
            erros.append(f'Família Fechada na Melhoria {m["nome"]}.')
        modalidades = entrada.get('modalidades', {})
        if modalidades:
            if m.get('modalidade') not in modalidades:
                erros.append(f'{m["nome"]} exige escolher uma modalidade.')
                continue
            faixa = modalidades[m['modalidade']]
        elif m['nome'] == 'Condição':
            niveis = {n: tier for tier, nomes in livro.condicoes().items() for n in nomes}
            if m.get('condicao') not in niveis:
                erros.append('Condição precisa de uma condição comprável registrada.')
                continue
            faixa = niveis[m['condicao']]
        elif entrada['preco'] in ('Leve', 'Média', 'Pesada') and faixa != entrada['preco']:
            erros.append(f'Preço diferente do publicado: {m["nome"]}')
        valor = preco(classe, faixa)
        if familia in livres:
            valor = max(1, valor - desconto(classe, entidade))
        pago += valor
        compras.append((m['nome'], valor))
        if m['nome'] == 'Longe' and (forma in {'Toque', 'Aura'} or any(r['nome'] == 'Queima-Roupa' for r in restricoes)):
            erros.append('Longe incompatível com a proximidade.')
        if m['nome'] == 'Maior' and forma not in AREAS:
            erros.append('Maior exige uma área.')
    for f, nome in [('guarda', 'Guarda'), ('impulso', 'Impulso'), ('firmeza', 'Firmeza')]:
        if f in funcoes and not any(m['nome'] == nome for m in melhorias):
            erros.append(f'{nome} precisa ser comprado.')
    nomes_r = [r['nome'] for r in restricoes]
    if sum(n in {'Uma Vez', 'Condicional', 'Aquecer'} for n in nomes_r) > 1:
        erros.append('Mais de uma Restrição de frequência.')
    if {'Atrasar', 'Parado'} <= set(nomes_r):
        erros.append('Atrasar e Parado cobram o mesmo impedimento.')
    dev = preco(classe, 'Leve') if forma == 'Toque' and not pessoal else 0
    for r in restricoes:
        entrada = cat.get(r['nome'])
        if not entrada or entrada['tipo'] != 'Restrição':
            erros.append(f'Restrição desconhecida: {r["nome"]}')
            continue
        faixa = r.get('faixa', entrada['preco'])
        if r['nome'] == 'Queima-Roupa':
            if forma in {'Toque', 'Aura'} or pessoal:
                erros.append('Queima-Roupa incompatível com a Forma ou aplicação pessoal.')
                continue
            faixa = 'Média' if forma == 'Projétil' else 'Leve'
        elif entrada['preco'].startswith('Leve, limitada'):
            # Frágil devolve apenas o gasto declarado nas peças interrompíveis.
            valor = r.get('gasto_interrompivel')
            if type(valor) is not int or not 0 <= valor <= pago:
                erros.append('Frágil exige conferir o gasto interrompível.')
                continue
            dev += min(preco(classe, 'Leve'), valor)
            continue
        elif entrada['preco'] in ('Leve', 'Média') and faixa != entrada['preco']:
            erros.append(f'Devolução diferente da publicada: {r["nome"]}')
        dev += preco(classe, faixa)
    base = preco(classe, 'Média') if ('cura' in funcoes or
             coletivo and {'vida_temporaria', 'guarda', 'impulso', 'firmeza'} & funcoes) else (
             preco(classe, 'Leve') if 'vida_temporaria' in funcoes else 0)
    custo_forma = preco(classe, 'Média') if forma == 'Explosão' else (
        preco(classe, 'Leve') if forma in {'Aura', 'Cone', 'Linha'} else 0)
    devolucao = min(dev, pago, 2 * classe)
    pontos = orcamento(classe, entidade)
    saldo = pontos - base - custo_forma - pago + devolucao
    if saldo < 0:
        erros.append('Saldo negativo.')
    distribuicao = dados.get('distribuicao', {})
    if set(distribuicao) - (funcoes & FUNCOES_VARIAVEIS):
        erros.append('Distribuição para função ausente.')
    if any(type(v) is not int or v < 1 for v in distribuicao.values()):
        erros.append('Cada parcela variável exige pontos inteiros positivos.')
    if (funcoes & FUNCOES_VARIAVEIS) != set(distribuicao):
        erros.append('Falta registrar a distribuição das funções variáveis.')
    usados = sum(distribuicao.values())
    if usados > saldo:
        erros.append('Distribuição excede o saldo.')
    teto_cura = pontos - preco(classe, 'Média') if entidade else 2 * classe
    teto_coletivo = pontos - preco(classe, 'Pesada')
    if coletivo:
        if distribuicao.get('cura', 0) + distribuicao.get('vida_temporaria', 0) > teto_coletivo:
            erros.append('Teto coletivo de cura e vida temporária excedido.')
    elif distribuicao.get('cura', 0) > teto_cura:
        erros.append('Teto de cura individual excedido.')
    if distribuicao.get('dano', 0) > pontos:
        erros.append('Dano inicial excede o orçamento comum.')
    modo = dados.get('controle', 'sem_reforco')
    controle = any(cat.get(m['nome'], {}).get('familia') == 'Controle' for m in melhorias)
    reforco = 0
    if modo != 'sem_reforco':
        if not controle or modo not in {'limitado', 'sem_dano'}:
            erros.append('Opção de Controle indisponível.')
        elif modo == 'sem_dano' and set(distribuicao) - {'dano'}:
            erros.append('Saldo descartado de Controle não financia outra função.')
        elif modo == 'limitado' and set(distribuicao) - {'dano'}:
            raise ValueError('Mescla com Controle limitado exige revisão da origem das parcelas; esta conta não arbitra pontos descartados.')
        elif modo == 'sem_dano' and distribuicao:
            erros.append('Controle sem dano exige descartar todo o saldo.')
        elif modo == 'limitado' and distribuicao.get('dano', 0) > classe:
            erros.append('Dano de Controle excede a Classe.')
        else:
            tem_tr_controle = any(m['nome'] in {'Condição', 'Prende', 'Cerca'} for m in melhorias)
            reforco = 2 if modo == 'sem_dano' and tem_tr_controle else 0
    pe = 3 * classe + (2 * classe if 'Sobrecusto' in nomes_r else 0)
    return {'valida': not erros, 'erros': erros, 'pontos': pontos, 'base': base,
            'forma': custo_forma, 'melhorias': compras, 'devolucao': devolucao,
            'saldo': saldo, 'sem_uso': saldo - usados, 'pe': pe,
            'dano_d8': distribuicao.get('dano', 0), 'cura_d8': distribuicao.get('cura', 0),
            'vida_temporaria': 3 * distribuicao.get('vida_temporaria', 0),
            'cd_controle_adicional': reforco, 'limite_grupo': classe + 1,
            'escopo': 'Conta comum. Conferir opções, requisitos e resolução das peças no livro.'}

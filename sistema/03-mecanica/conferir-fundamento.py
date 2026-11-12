#!/usr/bin/env python3
"""Regressões da montagem R53 e das interfaces com rotas e entidades.

Exemplos do livro, contas esperadas independentes e rejeições de montagens
inválidas. A revisão de requisitos narrativos e o teste de mesa são separados.
"""
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
import livro
import fundamento_r53 as f

ERROS = []
CHECAGENS = 0


def bloco(titulo):
    print('\n' + titulo)


def check(nome, cond):
    global CHECAGENS
    CHECAGENS += 1
    if not cond:
        ERROS.append(nome)
        print('  ERRO:', nome)


def conta(dados, esperado, valida=True):
    r = f.calcular(dados)
    check(f'{dados.get("nome", "montagem")}: validade {r["erros"]}', r['valida'] == valida)
    for campo, valor in esperado.items():
        check(f'{dados.get("nome", "montagem")}: {campo} = {valor}, li {r[campo]}', r[campo] == valor)
    return r


bloco('1. FONTE ATUAL E CATÁLOGO')
cat = livro.catalogo()
check('Catálogo tem 62 opções de Melhoria em 61 entradas', sum(d['tipo'] == 'Melhoria' for d in cat.values()) == 62)
check('19 Restrições', sum(d['tipo'] == 'Restrição' for d in cat.values()) == 19)
check('18 Talentos, incluindo as duas criações próprias', sum(d['tipo'] == 'Talento' for d in cat.values()) == 18)
check('Seis Formas', set(livro.formas()) == {'Projétil', 'Toque', 'Explosão', 'Aura', 'Cone', 'Linha'})
check('Nove Famílias', len(set(livro.familias())) == 9)
check('Famílias das peças estão publicadas', all(d.get('familia') in livro.familias() or d.get('familia') is None for d in cat.values()))
check('Peças retiradas não são opções compráveis', not {'Troca', 'Cura', 'Onda', 'Apoio', 'Junto', 'Dívida', 'Corpo a Corpo', 'Muito Longe', 'Muito Maior', 'Adianta', 'Puxa'} & set(cat))
check('Longe e Maior têm preços por modalidade', cat['Longe']['modalidades'] == {'Um degrau': 'Leve', 'Três degraus': 'Média'} and cat['Maior']['modalidades'] == {'Um degrau': 'Leve', 'Três degraus': 'Pesada'})

bloco('2. PREÇOS E DESCONTOS NAS SETE CLASSES')
esperados = [(3,1,1,2,2),(6,1,2,3,2),(9,2,3,5,3),(12,2,4,6,3),(15,3,5,8,4),(18,3,6,9,4),(21,4,7,11,4)]
for c, (p,l,m,pe,q) in enumerate(esperados, 1):
    check(f'Classe {c}: preços e vagas', (f.orcamento(c), f.preco(c,'Leve'), f.preco(c,'Média'), f.preco(c,'Pesada'), f.max_melhorias(c)) == (p,l,m,pe,q))
    check(f'Classe {c}: descontos distintos', (f.desconto(c),f.desconto(c,True)) == [(1,1),(1,1),(2,1),(2,2),(3,2),(3,3),(4,3)][c-1])

bloco('3. BASE DE FUNÇÕES E DISTRIBUIÇÃO')
conta({'nome':'Reserva C1','classe':1,'forma':'Projétil','funcoes':['vida_temporaria'],'distribuicao':{'vida_temporaria':2}}, {'saldo':2,'base':1,'vida_temporaria':6})
conta({'nome':'Toque sem compra','classe':1,'forma':'Toque','funcoes':['vida_temporaria'],'distribuicao':{'vida_temporaria':2}}, {'saldo':2,'base':1,'devolucao':0})
conta({'nome':'Toque C3','classe':3,'forma':'Toque','melhorias':[{'nome':'Precisão'}],'distribuicao':{'dano':9}}, {'saldo':9,'devolucao':2,'dano_d8':9})
mix={'nome':'Ferir e recuperar','classe':3,'forma':'Projétil','funcoes':['dano','cura'],'melhorias':[{'nome':'Mais Um'}],'distribuicao':{'dano':2,'cura':2}}
conta(mix, {'saldo':4,'base':3,'dano_d8':2,'cura_d8':2,'pe':9})
ampliada=copy.deepcopy(mix);ampliada.update(classe=4,distribuicao={'dano':4,'cura':2})
conta(ampliada, {'saldo':6,'base':4,'dano_d8':4,'cura_d8':2,'pe':12})
conta({'nome':'Uma base na mescla','classe':3,'forma':'Projétil','funcoes':['cura','vida_temporaria'],'distribuicao':{'cura':4,'vida_temporaria':2}}, {'base':3,'saldo':6,'cura_d8':4,'vida_temporaria':6})
conta({'nome':'Guarda sem dados','classe':3,'forma':'Projétil','funcoes':['guarda'],'melhorias':[{'nome':'Guarda'}]}, {'base':0,'saldo':6,'sem_uso':6,'dano_d8':0})

bloco('4. ACESSOS E MONTAGENS INVÁLIDAS')
for alteracao in [{'voto':3}, {'funcoes':['cura_ilimitada']}]:
    x=copy.deepcopy(mix);x.update(alteracao)
    try:f.calcular(x);recusou=False
    except ValueError:recusou=True
    check('Campos antigos ou funções desconhecidas são recusados',recusou)
for alteracao in [{'fechadas':['Amparo']},{'distribuicao':{'dano':4,'cura':4}},{'distribuicao':{'dano':3}},{'distribuicao':{'dano':-1,'cura':5}}]:
    x=copy.deepcopy(mix);x.update(alteracao);conta(x,{},False)
conta({'nome':'Área Fechada','classe':3,'forma':'Cone','fechadas':['Área'],'distribuicao':{'dano':7}}, {},False)
conta({'nome':'Família adulterada','classe':3,'forma':'Projétil','melhorias':[{'nome':'Prende','familia':'Mira'}],'distribuicao':{'dano':6}}, {},False)
conta({'nome':'Toque com Queima-Roupa','classe':3,'forma':'Toque','restricoes':[{'nome':'Queima-Roupa'}],'distribuicao':{'dano':9}}, {},False)
conta({'nome':'Longe em Aura','classe':3,'forma':'Aura','melhorias':[{'nome':'Longe','modalidade':'Um degrau'}],'distribuicao':{'dano':5}}, {},False)

bloco('5. PROXIMIDADE E CONSERVAÇÃO DO ORÇAMENTO')
for c in range(1,8):
    for forma in livro.formas():
        x={'classe':c,'forma':forma,'funcoes':[],'melhorias':[{'nome':'Precisão'}], 'restricoes':[]}
        if forma in {'Projétil','Explosão','Cone','Linha'}:x['restricoes']=[{'nome':'Queima-Roupa'}]
        r=f.calcular(x)
        check(f'C{c} {forma}: devolução não cria saldo', r['valida'] and r['saldo'] <= r['pontos']-r['base']-r['forma'])
        check(f'C{c} {forma}: devolução respeita compras', r['devolucao'] <= sum(v for n,v in r['melhorias']) and r['devolucao'] <= 2*c)
conta({'nome':'Sobrecusto C3','classe':3,'forma':'Projétil','restricoes':[{'nome':'Sobrecusto'}],'distribuicao':{'dano':9}}, {'pe':15,'devolucao':0})

bloco('6. CONTROLE E INTERFACES')
ctrl={'nome':'Rede com Controle Livre','classe':4,'forma':'Explosão','livres':['Controle'],'funcoes':['controle'],'controle':'sem_dano','melhorias':[{'nome':'Condição','condicao':'Atordoado'},{'nome':'Terreno'}]}
conta(ctrl, {'saldo':3,'cd_controle_adicional':2,'dano_d8':0})
x=copy.deepcopy(ctrl);x['livres']=[]
conta(x, {'saldo':0,'cd_controle_adicional':2})
for nome in ['Terreno', 'Anteparo', 'Desarma o Feitiço']:
    conta({'nome':f'{nome} sem TR próprio','classe':4,'forma':'Projétil','funcoes':['controle'],
           'controle':'sem_dano','melhorias':[{'nome':nome}]}, {'cd_controle_adicional':0})
x=copy.deepcopy(ctrl);x.update(funcoes=['controle','cura'],distribuicao={'cura':1});conta(x,{},False)
for un,anc,trechos in [
    ('fundamento','ampliar',['A proporção pode ser diferente entre as linhas preparadas','Ela fica fixa em cada linha']),
    ('fundamento','conjurar',['No seu turno, você pode conjurar apenas um feitiço de Classe 1 ou maior','Uma conjuração de Reação fora do seu turno fica fora desse limite','não reduz as conjurações permitidas no seu próximo turno','Uma habilidade pode estabelecer uma exceção expressa']),
    ('catalogo','melhoria-reacao',['Fora do seu turno, esta conjuração fica fora do limite','Durante ele, siga o limite de [Conjurar](#fundamento--conjurar)']),
    ('fundamento','classezero',['Vida temporária permanece indisponível','sem criar pontos de montagem']),
    ('rotas','rotas',['mesma tabela de pontos e PE','O Restringido Sem Energia usa Técnica Marcial']),
    ('construcao','entidades-controle',['Condições Médias e Pesadas','especial comandada ativamente']),
    ('emanador','ema-forma',['As funções e a divisão dos pontos que sobram, registradas na ficha, continuam as mesmas','A troca não pode deixar a versão com mais pontos que sobram']),
    ('emanador','ema-manifestacao',['Aura permanece centrada em você','Queima-Roupa ainda limita seus alvos']),
    ('ritual','rit-parcelas',['Com Mais Um','menor parte','não amplia uma aplicação de cura ou apoio coletivo']),
    ('construcao','entidades-medidas',['A distância até um alvo ou ponto usa a Classe real','Classe real do uso + 1']),
    ('construcao','entidades-restricoes',['A dificuldade deve recair sobre quem executa']),
    ('construcao','entidade-vigia-habilidades',['Firmeza: perícia','começo do próximo turno de Bruna']),
]:
    corpo=livro.limpa(livro.por_bloco(un,anc))
    for trecho in trechos:check(f'{un}/{anc}: {trecho}',trecho in corpo)
conta({'nome':'Aura com Fura C3','classe':3,'forma':'Aura','melhorias':[{'nome':'Fura'}],'distribuicao':{'dano':4}}, {'dano_d8':4})
conta({'nome':'Explosão com Fura C3','classe':3,'forma':'Explosão','melhorias':[{'nome':'Fura'}],'distribuicao':{'dano':3}}, {'dano_d8':3})
check('Firmeza escolhe categoria e usa turno do conjurador', 'escolha uma categoria' in cat['Firmeza']['texto'] and 'começo do seu próximo turno' in cat['Firmeza']['texto'])
check('Impulso usa ataque e turno do beneficiário','próxima rolagem de ataque' in cat['Impulso']['texto'] and 'fim do próximo turno dele' in cat['Impulso']['texto'])

bloco('7. ORÇAMENTO E TETOS DAS ENTIDADES')
for c,p in enumerate([2,4,6,9,11,13,16],1):
    check(f'Entidade C{c}: orçamento próprio',f.orcamento(c,True)==p)
conta({'nome':'Reserva da entidade C1','classe':1,'entidade':True,'forma':'Projétil','funcoes':['vida_temporaria'],'distribuicao':{'vida_temporaria':1}}, {'pontos':2,'vida_temporaria':3,'base':1,'pe':3})
conta({'nome':'Cura coletiva C1 da entidade','classe':1,'entidade':True,'forma':'Aura','funcoes':['cura'],'distribuicao':{'cura':1}}, {},False)
conta({'nome':'Desconto da entidade C3','classe':3,'entidade':True,'forma':'Projétil','livres':['Mira'],'melhorias':[{'nome':'Fura'}],'distribuicao':{'dano':4}}, {'melhorias':[('Fura',2)],'saldo':4})
conta({'nome':'Desconto pessoal C3','classe':3,'forma':'Projétil','livres':['Mira'],'melhorias':[{'nome':'Fura'}],'distribuicao':{'dano':8}}, {'melhorias':[('Fura',1)],'saldo':8})

bloco('8. EXTRAÇÃO E INTEGRIDADE DA EDIÇÃO')
raw=livro.texto('catalogo')
mutado=raw.replace('**Família: Alcance.**','**Família removida.**',1)
try:livro._catalogo_r53(mutado);falhou=False
except livro.LivroMudou:falhou=True
check('Remover metadado de Família provoca erro de leitura',falhou)
base=Path(livro.R41).parent
snapshot=json.loads((base/'revisao-de-regras/editorial-r67/BLOCOS-R67.json').read_text())
check('Snapshot final inclui 576 blocos',len(snapshot)==576)
# R62 (03/11/2026): "saldo" saiu do texto do livro e a montagem diz "pontos que sobram".
# Âncoras (fundamento-link-saldo, construcao--entidades-saldo) e chaves de código continuam
# "saldo": o leitor não as vê. A conta ignora comentário, âncora e destino de link.
def _saldo_visivel(t):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'<a [^>]*></a>','',t);t=re.sub(r'\]\([^)]*\)',']',t)
    return len(re.findall(r'\b[Ss]aldos?\b',t))
_livro_md=Path(livro.R41).read_text(encoding='utf-8')
check('Nenhum "saldo" visível no livro (R62: virou pontos que sobram)',_saldo_visivel(_livro_md)==0)
check('Contra-teste: um "saldo" no texto é contado',_saldo_visivel(_livro_md+'\nO saldo volta.')==1)
check('Contra-teste: âncora e destino de link com saldo não contam',_saldo_visivel('<a id="fundamento-link-saldo"></a>[Pontos que sobram](#fundamento-link-saldo)')==0)
# R63 (03/11/2026): palavras raras saíram do texto. "Excedente" sobrevive só nos nomes Reserva Excedente e Ritual de Excedente.
_RARAS=r'\b(?:parcelas?|eleg[ií]ve(?:l|is)|efetivamente|concess(?:ão|ões)|pertinentes?|retroativ\w*|vencimentos?)\b|\bexcedentes?\b(?<!Reserva Excedente)(?<!Ritual de Excedente)(?<!^Excedente)|reserva (?:coletiva|de Reação)|\bAmpliada\b'
def _raras_visiveis(t):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'<a [^>]*></a>','',t);t=re.sub(r'\]\([^)]*\)',']',t)
    return re.findall(_RARAS,t,flags=re.M)
check('Nenhuma palavra rara visível no livro (R63)',_raras_visiveis(_livro_md)==[])
check('Contra-teste: uma "parcela" no texto é contada',len(_raras_visiveis(_livro_md+'\nUma parcela volta.'))==1)
check('Contra-teste: âncora e destino de link com parcelas não contam',_raras_visiveis('<a id="ritual--rit-parcelas"></a>[Partes adicionais](#ritual--rit-parcelas)')==[])
check('Fórmula publicada com o nome novo','**Pontos que sobram = 3 × Classe − base das funções − custo da Forma − Melhorias + devolução aproveitada.**' in _livro_md)
meta=json.loads((base.parent/'EDICAO-ATUAL.json').read_text())
for ed in ['claro','noturno']:
    p=base.parent/meta[ed]['arquivo']
    check(f'PDF {ed} idêntico ao revisado',hashlib.sha256(p.read_bytes()).hexdigest()==meta[ed]['sha256'])
# R66: as cinco habilidades usam a recuperação por cena definida no livro.
def _frequencia_cena(texto, chave):
    trecho=texto.split('<a id="'+chave+'"></a>',1)[1].split('<!-- fonte:',1)[0]
    return 'Uma vez por cena' in trecho and not re.search(r'\b(?:por|no) combate\b',trecho,re.I)
for chave in ['evocador--ev-combinada','evocador--ev-parceria-resposta','incursor--inc-ritmo','incursor--inc-brecha','incursor--inc-perfeita']:
    check('R66: frequência por cena em '+chave,_frequencia_cena(_livro_md,chave))
    pos=_livro_md.index('<a id="'+chave+'"></a>')
    alterado=_livro_md[:pos]+_livro_md[pos:].replace('Uma vez por cena','Uma vez por combate',1)
    check('Contra-teste: rejeita retorno a combate em '+chave,not _frequencia_cena(alterado,chave))
# R67 (12/11/2026, decisão do Mizuki): na Técnica Máxima a Forma e a base da função saem
# dos dados-base, 1 ponto de preço = 1d8; os pontos de montagem pagam só as Melhorias. A Máxima
# sem dano tem Efeito Próprio principal pago nos dados e o reforço de Controle; vida temporária
# vira função. As contas abaixo saem do preço do modelo (f.preco), não do texto.
bloco('9. TÉCNICA MÁXIMA: FORMA E FUNÇÃO NOS DADOS (R67)')
def _bloco_md(texto, chave):
    return texto.split('<a id="'+chave+'"></a>',1)[1].split('<!-- fonte:',1)[0]
_FAIXAS=[(5,24,8,25),(6,28,12,30),(7,32,16,35)]
_FORMA={'Projétil':'0','Aura':'Leve','Explosão':'Média'}
def _p(c,n): return 0 if n=='0' else f.preco(c,n)
def _max_dados(c,dados,forma,funcao):
    base={'dano':'0','cura':'Média','vida_ind':'Leve','coletiva':'Média'}[funcao]
    return dados-_p(c,_FORMA[forma])-_p(c,base)
def _maxima_ok(texto):
    mx=_bloco_md(texto,'fundamento--maxima');dom=_bloco_md(texto,'campo--inv-maxima')
    tabela=[tuple(map(int,m)) for m in re.findall(r'^\| (?:17 a 20|21 a 25|26 a 30) \| (\d+)d8 \| (\d+) \| (\d+) \|$',mx,re.M)]
    c5=_FAIXAS[0]
    exp=_max_dados(5,24,'Explosão','dano');cura=_max_dados(5,24,'Projétil','cura')
    vt=_max_dados(5,24,'Aura','coletiva');dexp=_max_dados(5,19,'Explosão','dano');dcura=_max_dados(5,19,'Projétil','cura')
    return {
     'tabela 24/28/32, 8/12/16, 25/30/35':tabela==[(d,p,pe) for _,d,p,pe in _FAIXAS],
     'dados-base pagam Forma e função':'Os **dados-base** pagam a Forma e a base da função' in mx,
     'pontos só para Melhorias':'**pontos de montagem** só para as Melhorias' in mx and 'pagar a Forma e as Melhorias' not in mx,
     f'exemplo Explosão {exp}d8':f'tira 5 dos 24 dados e causa {exp}d8' in mx,
     f'exemplo cura {cura}d8':f'tira os {_p(5,"Média")} dados da base Média e recupera {cura}d8' in mx,
     f'exemplo coletiva tira {_p(5,"Média")+_p(5,"Leve")} e sobram {vt}':f'tira {_p(5,"Média")+_p(5,"Leve")} dados, {_p(5,"Média")} da base Média e {_p(5,"Leve")} da Aura; sobram {vt}' in mx,
     'linha coletiva sem dividir':'1d8 de cura ou 3 de vida temporária. Cada aliado válido na região recebe o total, sem dividir.' in mx and 'A parte inteira para cada aliado' not in mx,
     f'exemplo vida temporária {vt} × 3 = {3*vt}':f'{vt} × 3 = {3*vt} de vida temporária' in mx,
     'vida temporária individual Leve':'| Vida temporária individual | Leve | 3 de vida temporária. Exige Amparo. |' in mx,
     'sem dano tem reforço de Controle':'recebe o **reforço de Controle**' in mx and 'fica indisponível nessa aplicação' not in mx,
     'Efeito principal nos dados':'**Efeito Próprio principal**' in mx and 'seu preço sai dos dados-base' in mx,
     'domada: Forma e função nos dados':'Os dados fixos pagam a Forma e a base da função' in dom and 'pagam Forma e Melhorias' not in dom,
     f'domada: Explosão {dexp}d8 e cura {dcura}d8':f'ou {dexp}d8 com Explosão' in dom and f'recupera {dcura}d8' in dom,
     'exemplos sem orçamento antigo':'Cabe nos orçamentos 8, 12 e 16' not in texto and 'dentro dos orçamentos 8/12/16' not in texto,
    }
for nome,ok in _maxima_ok(_livro_md).items():
    check('R67: '+nome,ok)
# Os dados que sobram sobem de faixa em faixa e nunca zeram, em toda Forma e função,
# inclusive com o Efeito Próprio Pesado da Máxima sem dano.
for forma in _FORMA:
    for funcao in ('dano','cura','vida_ind','coletiva'):
        if funcao=='coletiva' and forma=='Projétil':continue
        seq=[_max_dados(c,d,forma,funcao) for c,d,_,_ in _FAIXAS]
        check(f'R67: {forma}/{funcao} sobe de faixa e fica positivo {seq}',all(x>0 for x in seq) and seq==sorted(seq))
    efeito=[d-_p(c,_FORMA[forma])-f.preco(c,'Pesada') for c,d,_,_ in _FAIXAS]
    check(f'R67: sem dano com {forma} e Efeito Pesado cabe nos dados {efeito}',all(x>=0 for x in efeito))
# Contra-testes: o texto antigo e um número errado precisam reprovar.
def _reprova(antes,depois,chave):
    assert _livro_md.count(antes)==1,antes
    return not all(_maxima_ok(_livro_md.replace(antes,depois,1)).values())
check('Contra-teste R67: volta da Forma paga nos pontos',_reprova('Use a coluna de **pontos de montagem** só para as Melhorias.','Use a coluna de **pontos de montagem** para pagar a Forma e as Melhorias.','x'))
check('Contra-teste R67: Explosão com 24d8 no exemplo',_reprova('tira 5 dos 24 dados e causa 19d8','tira 5 dos 24 dados e causa 24d8','x'))
check('Contra-teste R67: reforço de Controle retirado',_reprova('Nessa aplicação, a Máxima recebe o **reforço de Controle**','Nessa aplicação, a Máxima não recebe o reforço','x'))
check('Contra-teste R67: domada volta a pagar Forma nos pontos',_reprova('Os dados fixos pagam a Forma e a base da função, como na Técnica Máxima pessoal.','Os pontos pagam Forma e Melhorias.','x'))
check('Contra-teste R67: exemplo coletivo com 18 dados',_reprova('; sobram 16, e cada aliado','; sobram 18, e cada aliado','x'))
check('Contra-teste R67: tabela com orçamento 8/8/12',_reprova('| 21 a 25 | 28d8 | 12 | 30 |','| 21 a 25 | 28d8 | 8 | 30 |','x'))
print(f'\n{CHECAGENS} verificações; {len(ERROS)} falhas.')
if ERROS:sys.exit(1)
print('>>> TUDO OK: montagem comum R53, fontes e interfaces conferidas.')

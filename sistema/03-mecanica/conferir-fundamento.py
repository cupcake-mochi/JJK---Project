#!/usr/bin/env python3
"""Regressões da montagem R53 e das interfaces com rotas e entidades.

Exemplos do livro, contas esperadas independentes e rejeições de montagens
inválidas. A revisão de requisitos narrativos e o teste de mesa são separados.
"""
import copy
import hashlib
import json
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
    ('emanador','ema-forma',['As funções e a distribuição do saldo da ficha permanecem','A versão não pode ganhar saldo pela troca']),
    ('emanador','ema-manifestacao',['Aura permanece centrada em você','Queima-Roupa conserva seus alvos']),
    ('ritual','rit-parcelas',['Com Mais Um','menor parcela','não amplia uma aplicação de cura ou apoio coletivo']),
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
snapshot=json.loads((base/'revisao-de-regras/editorial-r60/BLOCOS-R60.json').read_text())
check('Snapshot final inclui 576 blocos',len(snapshot)==576)
meta=json.loads((base.parent/'EDICAO-ATUAL.json').read_text())
for ed in ['claro','noturno']:
    p=base.parent/meta[ed]['arquivo']
    check(f'PDF {ed} idêntico ao revisado',hashlib.sha256(p.read_bytes()).hexdigest()==meta[ed]['sha256'])
print(f'\n{CHECAGENS} verificações; {len(ERROS)} falhas.')
if ERROS:sys.exit(1)
print('>>> TUDO OK: montagem comum R53, fontes e interfaces conferidas.')

"""Conferência de contas e dependências do exemplo escrito, sem simular uma mesa."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlparse
import hashlib
import json
import math
import re
from bs4 import BeautifulSoup

APOIO = Path(__file__).resolve().parent
RAIZ = APOIO.parents[1]


def main():
    dados = json.loads((RAIZ/'04 - Planejamento/apoio-piloto/base-inimigos.json').read_text())
    monstro = next(x for x in dados['enemies'] if x['id']=='amontoado')
    personagens = {x['id']:x for x in dados['players']}
    assert (monstro['pv'],monstro['pe'],monstro['defesa'],monstro['deslocamento'])==(48,6,11,9)
    assert monstro['pv']//2==24
    assert monstro['atributos']=={'forca':3,'destreza':1,'constituicao':3,'inteligencia':1,'essencia':1}
    assert monstro['atributos']['forca']+dados['maestria']==4
    assert 10+monstro['atributos']['destreza']==11
    assert 8+monstro['atributos']['forca']+dados['maestria']==12
    frente=personagens['frente'];apoio=personagens['apoio'];conj=personagens['conjurador']
    assert (frente['pv'],frente['pe'],apoio['pv'],apoio['pe'],conj['pv'],conj['pe'])==(23,8,17,10,14,12)
    vida=monstro['pv'];pe=monstro['pe'];fvida=frente['pv'];fpe=frente['pe'];ape=apoio['pe'];cpe=conj['pe']
    estados=[]
    # Duas rodadas com a mesma iniciativa e uma queda. Todos os dados estão
    # declarados para verificar o roteiro, não para estimar sua probabilidade.
    crit=[5,4,3,4,3,5];assert all(1<=x<=8 for x in crit)
    assert sum(crit)==24
    pe-=3;fvida=max(0,fvida-sum(crit));assert fvida==0
    requisito=min(math.ceil(frente['pv']/3),15);assert requisito==8
    janela=3;tratamento=0
    for ataque,rolos in [(12,[4,3,5]),(10,[6,3,5])]:
        assert ataque+4>=monstro['defesa']
        assert all(1<=x<=8 for x in rolos)
        vida-=sum(rolos)
    fpe-=3;ape-=3;cpe-=3;tratamento=sum([3,2]);assert tratamento==5<requisito
    assert vida==22 and pe==3 and janela==3
    estados.append({'rodada':1,'amontoado':{'pv':vida,'pe':pe},'frente':{'pv':fvida,'pe':fpe,'tratamento':tratamento,'janela':janela},'apoio_pe':ape,'conjuradora_pe':cpe})
    janela-=1;assert janela==2
    pe-=3;assert 4+4<frente['defesa']  # Segundo Impacto erra.
    assert 9+4>=monstro['defesa'];vida-=sum([4,5,3]);fpe-=3;assert vida==10
    tratamento+=sum([2,1]);ape-=3;assert tratamento==requisito
    fvida=min(tratamento,frente['pv']);sequelas=1;janela=None
    assert 11+4>=monstro['defesa'];vida=max(0,vida-sum([3,4,4]));cpe-=3
    assert (vida,pe,fvida,fpe,ape,cpe,sequelas)==(0,0,8,2,4,6,1)
    assert all(x>=0 for x in [vida,pe,fvida,fpe,ape,cpe])
    estados.append({'rodada':2,'amontoado':{'pv':vida,'pe':pe},'frente':{'pv':fvida,'pe':fpe,'morrendo':False,'sequelas':sequelas},'apoio_pe':ape,'conjuradora_pe':cpe})
    fonte=RAIZ/'06 - Redacao do Guia/revisao-98/01-sua-primeira-missao.md'
    texto=fonte.read_text()
    for frase in ['8/23 PV','2/8 PE','4/10 PE','6/12 PE','3 para 2 rodadas','3 + 2 = 5','2 + 1 = 3','3 + 4 + 4 = 11']:
        assert frase in texto,frase
    # Posições possíveis em metros: parede da porta em y=0, criatura em y=4,5.
    # Os dois apoios ficam abertos nas laterais, sem a frente entre alvo e ataque.
    pos={'amontoado':(3,4.5),'frente':(4.5,4.5),'apoio':(4,0.75),'conjuradora':(2.5,0.75)}
    assert math.dist(pos['frente'],pos['amontoado'])==1.5
    assert math.dist(pos['conjuradora'],pos['amontoado'])<=6
    assert math.dist(pos['apoio'],pos['frente'])<9
    # O segmento entre conjuradora e criatura fica em x <= 3; a frente está
    # inteiramente em x >= 3,75 se ocupar um espaço de 1,5 m.
    assert max(pos['conjuradora'][0],pos['amontoado'][0])<pos['frente'][0]-0.75
    # Conferir todos os caminhos e âncoras das duas páginas de leitura.
    problemas=[];links=0
    for nome in ['capitulo-1.html','consulta-de-regras.html']:
        path=APOIO/nome;soup=BeautifulSoup(path.read_text(),'html.parser')
        ids=[x['id'] for x in soup.find_all(id=True)]
        assert len(ids)==len(set(ids)),nome
        for tag,atributo in [('a','href'),('img','src')]:
            for el in soup.find_all(tag):
                href=el.get(atributo,'');u=urlparse(href)
                if not href or u.scheme in ['https','http','data']:continue
                links+=1
                dest=(path.parent/unquote(u.path)).resolve() if u.path else path
                if not dest.is_file():problemas.append([nome,href,'arquivo ausente']);continue
                if u.fragment and dest.suffix=='.html':
                    outro=soup if dest==path else BeautifulSoup(dest.read_text(),'html.parser')
                    if not outro.find(id=unquote(u.fragment)):problemas.append([nome,href,'âncora ausente'])
                if u.fragment and dest.suffix=='.md':
                    if f'id="{unquote(u.fragment)}"' not in dest.read_text():problemas.append([nome,href,'âncora explícita ausente'])
    assert not problemas,problemas
    # As 104 fontes da edição integrada e o livro de regras não foram reescritos.
    anterior=json.loads((RAIZ/'07 - Edicao de Leitura/mapa-editorial.json').read_text())
    alteradas=[x['id'] for x in anterior['fontes'] if hashlib.sha256((RAIZ/x['fonte']).read_bytes()).hexdigest()!=x['sha256']]
    assert not alteradas,alteradas
    base=RAIZ/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
    assert hashlib.sha256(base.read_bytes()).hexdigest()=='7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d'
    resultado={'registro':100,'confronto':estados,'rodadas_do_roteiro':2,'quedas_do_roteiro':1,
               'posicoes_possiveis_em_metros':pos,'links_locais_conferidos':links,'problemas_de_links':problemas,
               'fontes_integradas_preservadas':104,'regras_preservadas':True,
               'limite':'Conferência determinística do roteiro e dos arquivos; sem teste externo ou certificação de equilíbrio.'}
    (APOIO/'verificacao-do-exemplo.json').write_text(json.dumps(resultado,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(resultado,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()

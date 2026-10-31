"""Consolidar evidências já inspecionadas; não substitui a inspeção visual."""
from pathlib import Path
import hashlib, json, difflib, shutil

B=Path(__file__).resolve().parents[1]
R=B/'revisao-r50'
OLD=B.with_name('livro-diagramado-r49')
def read(p): return json.loads(p.read_text())
def save(p, v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
m=read(B/'FONTES-E-VALIDACAO.json')
proof=read(B/'evidencias/CONFERENCIA.json')
assert not proof['problemas'] and proof['sha256_pdf']==sha(B/m['pdf'])==m['sha256_pdf']
assert m['paginas']==397
shutil.copy2(B/'evidencias/CONFERENCIA.json',R/'final/CONFERENCIA.json')

# Inspeção efetivamente feita no chat: primeira passagem 1–397;
# fechamento 1–80 na segunda composição e 81–397 na terceira.
# As únicas diferenças de pixels posteriores foram abertas individualmente.
enlarged={52,53,54,55,56,57,58,59,78,83,84,85,134,279,280,285,307}
notes={
 52:'Entrada de Morrendo e distinção entre cura comum e resgate expresso legíveis.',
 53:'Tabela, janela e esquema completos; Aguentar começa inteiro na página seguinte.',
 54:'Aguentar reunido; Insistir segue da esquerda para a direita, com exemplos na mesma página.',
 55:'Resgates expressos recebeu o tratamento de subtópico aprovado; tabela de Sequelas preservada.',
 56:'Derrota, recuperação e exceção do Núcleo Dependente conferidas em ampliação.',
 58:'Ordem recuperar/registrar/remover Sequelas presente na tabela e no texto.',
 78:'Leitura a Dois termina na mesma coluna em que começa; preservada a correção anterior.',
 83:'Definição aprovada do Olho adicional legível; Regeneração conserva exigência de vida positiva.',
 84:'Locomoção Adaptada inteira abaixo da tabela; nenhuma opção isolada na página seguinte.',
 85:'Recomposta após reunir Locomoção; começa em Bolsa Orgânica.',
 105:'Muro mantém apresentação, tabela e início de Alicerce na mesma página.',
 134:'Ainda Há Tempo conserva gatilho de entrada; explicação prossegue na coluna direita da mesma página.',
 237:'Tabela de progressão longa prossegue na página 238 com cabeçalho repetido.',
 269:'Família Alcance acompanhada das primeiras Melhorias.',
 273:'Família Controle acompanhada de Condição; sem abertura de família isolada.',
 279:'Limpa Fundo cabe inteiro e explicita a exceção de Morrendo.',
 280:'Levanta e remissões de Reserva conferidos em ampliação.',
 285:'Recomposição com 3 × maior Classe; ação e frequência preservadas.',
 299:'Extensão de Domínio e Duração seguem a sequência esquerda/direita.',
 307:'Segundo Fôlego completo na coluna esquerda; sem custo antigo de vida máxima.',
 334:'Introdução de Melhorias de Ritual completa; a tabela larga inicia na página seguinte.',
 386:'Glossário de Morrendo e Legado atualizado.',
}
rows=[]
for p in range(1,398):
    final=R/'final'/f'p{p:03}.png'
    source='segunda' if p<=80 else 'terceira'
    if p in {55,84,85}: source='final'
    source_path=R/source/f'p{p:03}.png'
    assert sha(final)==sha(source_path),(p,source,'Falta inspeção da composição final')
    assert (R/'primeira'/f'p{p:03}.png').exists()
    rows.append(dict(pagina=p,primeira_passagem='primeira',
        fechamento_inspecionado=source,imagem_final_sha256=sha(final),
        composicao_final_identica_a_inspecionada=True,ampliacao_final=p in enlarged,
        painel_final=f'final/painel-{(p-1)//8+1:02}.jpg',
        observacao=notes.get(p,'Inspeção no painel sequencial: sem obstáculo de leitura identificado.')))
save(R/'REVISAO-VISUAL-PAGINAS.json',dict(sha256_pdf=m['sha256_pdf'],total_paginas=397,
    passagens_integrais=2,metodo='Todas as páginas examinadas em painéis sequenciais de oito páginas; páginas críticas também abertas individualmente. Equivalência por hash dos PNGs confirma a composição final das páginas já inspecionadas. Não é afirmação de leitura palavra por palavra de todo o livro.',paginas=rows))
save(R/'COMPARACAO-COMPOSICOES.json',dict(
    final_sha256=m['sha256_pdf'],
    segunda_para_final_primeiras_80=[p for p in range(1,81) if sha(R/'segunda'/f'p{p:03}.png')!=sha(R/'final'/f'p{p:03}.png')],
    terceira_para_final=[p for p in range(1,398) if sha(R/'terceira'/f'p{p:03}.png')!=sha(R/'final'/f'p{p:03}.png')]))

# Triagem geométrica adicional: título e primeiro conteúdo no mesmo espaço.
heads={'h1','h2','h3'}
events=[e for e in m['eventos'] if not e['gerado']]
candidates=[]; count=0
for i,e in enumerate(events):
    if e['tipo'] not in heads: continue
    body=next((v for v in events[i+1:] if v['tipo'] not in heads|{'marker','small','major'}),None)
    if body is None: continue
    count+=1
    same_page=e['pagina']==body['pagina']
    same_column=abs(e['x']-body['x'])<1 or max(e['largura'],body['largura'])>300
    if not(same_page and same_column):
        candidates.append(dict(pagina=e['pagina'],titulo=e['texto'],primeiro_conteudo_pagina=body['pagina']))
save(R/'TRIAGEM-TITULOS.json',dict(sha256_pdf=m['sha256_pdf'],titulos_conferidos=count,candidatos=candidates,
    limite='Triagem de título/primeiro conteúdo, não julgamento automático de introduções completas. Conferência visual separada.'))
print('Triagem',count,'títulos;',len(candidates),'candidatos')

# Registro completo dos arquivos de suporte que mudaram. Texto do livro tem
# seu registro próprio, por bloco; estes são apenas geração e composição.
names=['gerar_livro.py','ler_fontes.py','fluxo_continuo.py','revisao_r50.py',
       'DESTAQUES-CATALOGO.json','revisao-r45/CLASSIFICACAO.json']
reasons={
 'gerar_livro.py':'Nome do PDF de saída passa a R50; tamanhos e estilos existentes preservados.',
 'ler_fontes.py':'Aplicar o registro R50 depois das revisões anteriores.',
 'fluxo_continuo.py':'Manter Aguentar e a lista curta Locomoção Adaptada inteiros quando couberem em uma coluna.',
 'revisao_r50.py':'Aplicação exata dos 29 blocos e classificação persistente de Resgates expressos.',
 'DESTAQUES-CATALOGO.json':'Sincronizar as entradas de exemplos com o texto novo; sem acrescentar texto fora do registro.',
 'revisao-r45/CLASSIFICACAO.json':'Subtópico Resgates expressos usa o tratamento B aprovado, como Estabilizar.',
}
changes=[]
for n in names:
    a=(OLD/n).read_text() if (OLD/n).exists() else None
    z=(B/n).read_text()
    if a==z:continue
    changes.append(dict(id=f'R50-D{len(changes)+1:02}',arquivo=n,antes=a,depois=z,motivo=reasons[n]))
save(B/'ALTERACOES-COMPOSICAO-R49-para-R50.json',changes)
print('Composição:',len(changes),'arquivos; visual:',len(rows),'páginas')

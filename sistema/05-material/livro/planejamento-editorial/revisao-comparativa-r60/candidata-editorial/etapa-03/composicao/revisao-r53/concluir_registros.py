from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];R=B/'revisao-r53';D=B.parents[1]/'desenvolvimento-fundamentos'
def read(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
m=read(B/'FONTES-E-VALIDACAO.json');qa=read(B/'evidencias/CONFERENCIA.json');specific=read(R/'VALIDACAO-R53.json');night=read(R/'VALIDACAO-NOTURNO.json');visual=read(R/'REVISAO-VISUAL.json')
assert not qa['problemas'] and qa['sha256_pdf']==m['sha256_pdf']==specific['sha256_pdf']==visual['sha256_pdf']
assert night['resultado']=='aprovado' and night['sha256_pdf']==hashlib.sha256((B/'output/pdf/Ciclo-Maldito-R53-Noturno-Vinho-e-Pessego.pdf').read_bytes()).hexdigest()
assert visual['resultado']=='aprovado'
pages=m['paginas'];changes=len(read(B/'ALTERACOES-R52-para-R53.json'))
light=B/'output/pdf/Ciclo-Maldito-R53.pdf';dark=B/'output/pdf/Ciclo-Maldito-R53-Noturno-Vinho-e-Pessego.pdf'
(B/'LEIA-ME-R53.md').write_text(f'''# Ciclo Maldito R53

Integração do Fundamento v8 aprovado ao livro completo, com {pages} páginas. A R52 e os PDFs independentes do protótipo permanecem intactos.

O capítulo apresenta funções separadas das seis Formas e incorpora o catálogo de 61 Melhorias e 19 Restrições. As referências, exemplos, Rotas de criação, habilidades de entidades, Ritual e Emanador foram adaptados. Forma Fluida altera somente a Forma, conservando funções e distribuição dos pontos, conforme decisão do autor.

Sem Técnica e Técnica Marcial recebem uma apresentação comum da montagem, tabela dos termos e passos específicos para Manejos e Katas. Controle Livre conserva o reforço de +2 nas CDs aplicáveis quando a ficha registra a opção sem dano e descarta a sobra do desconto.

Vida temporária individual paga base Leve. Cada aplicação paga a maior base exigida por suas funções, uma única vez. Na Classe 1, Projétil sem Melhorias ou Restrições oferece 6 de vida temporária antes do teto da reserva. As devoluções cobrem somente Melhorias. Os exemplos dependentes foram recalculados; Tiras de resgate recebe a Restrição Parado, cumprida pela entidade.

O fluxo após elementos de largura inteira aproveita ambas as colunas quando a divisão cabe sem acrescentar páginas. A explicação da base foi dividida em parágrafos para permitir essa distribuição.

- PDF claro: `output/pdf/Ciclo-Maldito-R53.pdf`.
- PDF noturno: `output/pdf/Ciclo-Maldito-R53-Noturno-Vinho-e-Pessego.pdf`.
- Texto completo: `LIVRO-COMPLETO.md`.
- {changes} blocos com antes/depois: `ALTERACOES-R52-para-R53.json`.
- Conferências: `evidencias/CONFERENCIA.json`, `revisao-r53/VALIDACAO-R53.json`, `revisao-r53/CONTAS-VIDA-TEMPORARIA.json` e `revisao-r53/VALIDACAO-NOTURNO.json`.
- Revisão visual e seus limites: `revisao-r53/REVISAO-VISUAL.json`.

Todas as páginas claras foram inspecionadas em pranchas, com conferência individual das páginas registradas. A versão noturna conserva texto, geometria, imagens e navegação; recebe a paleta vinho e pêssego aprovada. A revisão editorial e as contas não constituem teste de equilíbrio em mesa.

Os arquivos de capítulo no Drive conservam as versões anteriormente publicadas. Esta entrega é local. Sem commit nem push.
''')
plan=read(R/'PLANO-E-BASE.json')
for step in plan['etapas']:step['estado']='concluída'
plan['resultado']={'revisao':'R53','paginas':pages,'texto':str(B/'LIVRO-COMPLETO.md'),'pdf':str(light),'noturno':str(dark),'sha256_pdf':m['sha256_pdf'],'alteracoes':changes}
plan['decisao_vida_temporaria']={'autor':'Vida temporária individual deveria custar Leve.','implementacao':'Base Leve; conservar base única nas mesclas pelo maior custo; sem desconto ou devolução da base.','exemplos_recalculados':['Socorro durante a retirada','Placas de apoio','Tiras de resgate']}
save(R/'PLANO-E-BASE.json',plan)
base=read(D/'BASE-E-DECISOES.json')
newdec=[{'id':'D22','data':'2026-10-18','decisao':'Integrar o protótipo aprovado ao livro em nova cópia R53.','resposta_do_autor':'aprovaram o prototipo, agora é passar pro livro né?','alcance':'Conferir dependências e leitura, preservando a R52 e o protótipo aprovado.'},{'id':'D23','data':'2026-10-18','decisao':'Forma Fluida altera somente a Forma. As funções e sua distribuição de pontos permanecem.','resposta_do_autor':'forma fluida n vai permitir feitiço mudar de cura pra pvt ou dano n','alcance':'Emanador e explicação do momento de escolha da função.'},{'id':'D24','data':'2026-10-18','decisao':'Vida temporária individual passa a pagar base Leve.','resposta_do_autor':'Eu acho q Vida temporária individual deveria custar leve [...] 9 de PvT nv1, é mt coisa','alcance':'R53; adaptar funções, entidades e exemplos. Conservar a base única das mesclas, pagando a maior exigida. Toque e Restrições não recuperam base.'}]
ids={x['id'] for x in base['decisoes_de_redesenho_aprovadas']}
base['decisoes_de_redesenho_aprovadas'].extend(x for x in newdec if x['id'] not in ids)
base['versao_do_estudo']='integracao-r53'
base['integracao_no_livro']={'estado':'concluída','revisao':'R53','pasta':str(B),'pdf':str(light),'paginas':pages,'base_preservada':'R52','validacao':str(R/'VALIDACAO-R53.json')}
base['etapa_atual']={'concluido':'Integração no livro, migração das dependências, clareza das rotas e custo Leve da vida temporária individual.','leitura':str(B/'LIVRO-COMPLETO.md'),'pdf':str(light),'noturno':str(dark),'validacao':str(R/'VALIDACAO-R53.json'),'revisao_visual':str(R/'REVISAO-VISUAL.json'),'proximo':'Receber observações de compreensão e de uso em mesa a partir da R53.','escopo_da_conclusao':'Integração e revisão editorial concluídas; equilíbrio em mesa depende de jogo.'}
base['estado_atual'].update(integrado_no_livro=True,revisao_do_livro='R53',capitulo_consolidado=str(B/'LIVRO-COMPLETO.md'),pdf=str(light),proxima_pendencia='Receber observações de compreensão e de uso em mesa a partir da R53.')
base.setdefault('historico_entregas_locais',[]).append(base['entrega_local_atual'])
base['entrega_local_atual']={'pdf':str(light),'noturno':str(dark),'paginas':pages,'sha256':m['sha256_pdf'],'drive_atualizado':False,'observacao':'Arquivos de capítulo do Drive permanecem nas versões já publicadas.'}
base['pdf_para_leitores']={'situacao':'Livro completo R53 integrado e revisado. Capítulo v8 preservado como histórico.','arquivo':str(light),'sha256':m['sha256_pdf'],'criterio':'Usar a R53 para as regras integradas, incluindo as decisões posteriores à v8.','publicacao':'Entrega local; sem atualização dos arquivos de capítulo no Drive.'}
save(D/'BASE-E-DECISOES.json',base)
head=f'''# Integração concluída no livro R53

A referência atual é `entregas/livro-diagramado-r53/`, com {pages} páginas. O protótipo v8 aprovado foi integrado ao livro, incluindo as dependências de rotas e entidades. Forma Fluida altera somente a Forma. A vida temporária individual paga base Leve, conforme ajuste posterior do autor. Sem Técnica e Técnica Marcial recebem uma explicação comum da montagem e passos específicos.

Texto, PDFs claro e noturno vinho e pêssego, antes/depois e validações ficam na pasta da R53. A R52 e as versões independentes do capítulo permanecem preservadas. Os arquivos de capítulo já publicados no Drive não foram substituídos nesta integração. Sem commit nem push.

Os estados abaixo preservam o histórico. Para regras integradas, consulte a R53.

---

'''
for p in [D/'README.md',D/'prototipos/resultado-e-entrega-v01/ESTADO-ATUAL.md']:
 p.write_text(head+p.read_text())
save(R/'RETOMADA.json',{'estado':'concluída','revisao':'R53','paginas':pages,'pdf':str(light),'noturno':str(dark),'validacao':str(R/'VALIDACAO-R53.json'),'revisao_visual':str(R/'REVISAO-VISUAL.json'),'sem_commit_ou_push':True,'drive':'Não alterado nesta integração.'})
print(json.dumps({'concluido':True,'paginas':pages,'alteracoes':changes},ensure_ascii=False))

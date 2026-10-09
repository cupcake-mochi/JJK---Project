"""Consolida evidências da revisão já realizada, sem regenerar o livro."""
from pathlib import Path
import json, hashlib, difflib

B=Path(__file__).resolve().parent; R=B/'revisao-r38'; O=B.parent/'livro-diagramado-r37'
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda name,data:(R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
m=read(B/'FONTES-E-VALIDACAO.json'); c=read(R/'CONFERENCIA.json')
a=read(R/'APROVEITAMENTO-R37.json'); z=read(R/'APROVEITAMENTO-R38.json')
scope=read(R/'ESCOPO-VISUAL.json'); changed=read(R/'PAGINAS-RECOMPOSTAS-ULTIMA-PROVA.json')
images=read(R/'PROVA-IMAGENS.json'); assert images['sha256_pdf']==sha(B/m['pdf'])==c['sha256_pdf']
assert all((p-1)//8+1 in scope['paineis_reinspecionados_prova_final'] for p in changed)
large=sorted({p for i in scope['duplas_ampliadas_prova_final'] for p in (2*i-1,2*i) if p<=m['paginas']})
visual=[]
for p in range(1,m['paginas']+1):
 panel=(p-1)//8+1
 visual.append({'pagina':p,'imagem':f'paginas/p-{p:03}.jpg','sha256_imagem':images['imagens'][f'p-{p:03}.jpg'],
  'visao_geral':'Prova final inspecionada' if panel in scope['paineis_reinspecionados_prova_final'] else 'Composição idêntica à prova anterior inspecionada; conferência por texto, geometria e tratamento',
  'inspecao_ampliada':p in large,'pendencia_visual_encontrada':False})
write('REVISAO-PAGINAS.json',visual)
write('REVISAO-VISUAL.json',{'sha256_pdf':c['sha256_pdf'],'paginas_visao_geral':m['paginas'],
 'paginas_recompostas_reinspecionadas':changed,'paginas_ampliadas':large,
 'escopo':'Composição, continuidade, tabelas, hierarquia e leitura das três alterações autorizadas. Visão geral integral e amostra ampliada dirigida; não é uma nova leitura editorial palavra por palavra das 367 páginas.',
 'achados_corrigidos':['Abertura curta de Balestra mantida com as primeiras linhas da tabela. A mesma proteção vale para aberturas equivalentes.'],
 'verificacoes':['Cada Família inicia na mesma página da primeira Melhoria.','Muro e sua primeira habilidade estão na mesma página, seguindo esquerda e depois direita.','Extensão de Domínio precede Duração e custo na coluna esquerda.','Sem pares sucessivos de colunas na mesma página.','Continuações de tabela têm cabeçalho repetido sem repetir dados.'],
 'pendencias_visuais':[],'folgas_aceitas':[x['pagina'] for x in z['paginas_acima_terco']]})
next_art={5:'Mundo jujutsu (p. 6)',67:'Receptáculo (p. 68)',74:'Corpo Amaldiçoado (p. 75)',78:'Restrição Celestial (p. 79)',103:'Guia (p. 104)',145:'Incursor (p. 146)',149:'Assassino (p. 150)',154:'Pugilista (p. 155)',159:'Malabarista (p. 160)',281:'Sem Técnica (p. 282)',286:'Bênçãos (p. 287)'}
rows=['| Página R38 | Branco médio no pé das colunas | Motivo |','|---|---:|---|']
for e in z['paginas_acima_terco']:
 rows.append(f"| {e['pagina']} | {e['branco_medio']:.1%} | Fim do trecho anterior à abertura ilustrada de {next_art[e['pagina']]}. A abertura e sua arte foram preservadas. |")
spaces='''# Espaços restantes — R38

A tabela abaixo usa a média das duas colunas: mais de um terço vazio na área útil da página. As porcentagens medem o espaço abaixo do último elemento, não o branco entre parágrafos, dentro de tabelas ou dentro de imagens. Todas as páginas usam a numeração da R38.

## Meio de capítulo

'''+ '\n'.join(rows)+'''

Essas onze páginas encerram trechos antes de páginas ilustradas. O fluxo não atravessa essas aberturas: fazê-lo exigiria deslocar texto para além da apresentação da próxima seção, ou recompor a própria abertura e arte. O branco remanescente foi aceito para preservar essa sequência. Isso não significa que seja impossível reduzir mais páginas mediante outro projeto das aberturas.

## Apenas uma coluna acima de um terço

Há ainda três páginas de meio de capítulo em que uma coluna passa de um terço vazio, mas a média da página não passa. Registradas para não esconder a assimetria:

| Página | Esquerda vazia | Direita vazia | Motivo |
|---|---:|---:|---|
'''
single_reasons={7:'Parágrafos inteiros e título ligado à abertura; redistribuir o par de colunas não elimina uma página.',77:'As entradas de Legados e seus parágrafos foram mantidos inteiros; a continuação segue na p. 78 antes da abertura ilustrada.',92:'A tabela de características/progressão e a abertura da Sequência de Condução mantêm sua ordem; os próximos parágrafos seguem na p. 93.'}
for e in z['alguma_coluna_acima_terco']:
 if e['branco_medio']<=1/3:spaces+=f"| {e['pagina']} | {e['branco_esquerda']:.1%} | {e['branco_direita']:.1%} | {single_reasons[e['pagina']]} |\n"
spaces+='''
## Começos e fins de capítulo

Permitidos pelo pedido e separados da lista de meio de capítulo. Páginas de conteúdo com média acima de um terço:

| Página | Branco médio | Conteúdo |
|---|---:|---|
'''
for e in z['bordas_acima_terco']:spaces+=f"| {e['pagina']} | {e['branco_medio']:.1%} | {e['grupo']} |\n"
spaces+='\nCapas, páginas de arte e modelos de ficha ficam fora deste indicador. A medição completa e os valores de cada coluna estão em APROVEITAMENTO-R38.json.\n'
(R/'ESPACOS-RESTANTES.md').write_text(spaces)
report=f'''# Entrega R38 — aproveitamento e duas Bênçãos

**367 páginas, 27 a menos que as 394 da R37.** A R37 foi preservada integralmente. Sem commit ou push.

## Texto

A frase «Gastar seus PE até chegar a zero não torna um feiticeiro uma criatura sem energia.» voltou ao ponto pedido, em geral--pressao, na p. 38, logo após a frase sobre a busca energética não encontrar uma criatura sem energia amaldiçoada.

As duas opções novas entram como Bênçãos adquiridas por Lapidação, na p. 291, e aparecem no catálogo da p. 288:

| Bênção | Acesso | Efeito |
|---|---|---|
| Represália | CE 2, Lapidação mínima 4, Destreza 4 | Reação para um ataque corpo a corpo contra criatura percebida a até 1,5 m que use aptidão amaldiçoada ativa ou conjure feitiço. Resolve depois do uso, sem cancelá-lo; exige que o alvo permaneça no alcance. |
| Sangue Frio | CE 3, Lapidação mínima 7, Constituição 4 | Vantagem em TR contra aptidões amaldiçoadas e feitiços de criatura a até 3 m; uma repetição de TR falho por combate, antes das consequências, com resultado obrigatório e o mesmo alcance. |

Não há custo adicional de PE. As decisões de balanceamento delegadas pelo autor estão em DECISOES-DE-BALANCEAMENTO.md. São decisões editoriais de projeto, ainda sem teste de mesa.

**O LIVRO-COMPLETO.md é idêntico ao da R37 fora da frase restaurada, das duas Bênçãos e de suas duas linhas no catálogo.** São três blocos alterados, todos com antes/depois e motivo em ALTERACOES-TEXTO.json. O pedido adicional de duas Bênçãos é a exceção autorizada à preservação textual. Nenhum exemplo foi reescrito. Os dados e a ordem das demais tabelas foram preservados.

## Aproveitamento

| Medida uniforme nesta auditoria | R37 | R38 |
|---|---:|---:|
| Páginas totais | 394 | 367 |
| Branco inferior somado, em páginas equivalentes de conteúdo | {a['branco_equivalente']:.2f} | {z['branco_equivalente']:.2f} |
| Branco inferior em meio de capítulo | {a['branco_meio_capitulo']:.2f} | {z['branco_meio_capitulo']:.2f} |
| Páginas de meio com média acima de um terço vazio | {len(a['paginas_acima_terco'])} | {len(z['paginas_acima_terco'])} |

O branco inferior de meio de capítulo caiu cerca de {100*(1-z['branco_meio_capitulo']/a['branco_meio_capitulo']):.1f}%, usando a mesma medição nas duas provas. Não apresento esses números como reprodução dos 83/72 informados pelo autor: aqui a área útil vai de 23 mm abaixo do topo a 36 mm acima do pé; capas, arte e modelos ficam fora, e a primeira/última página após cada capa é considerada borda de capítulo. Elementos largos contam para os dois lados.

Restam as páginas **{', '.join(str(e['pagina']) for e in z['paginas_acima_terco'])}**. Todas precedem aberturas ilustradas preservadas. A lista, a porcentagem e a justificativa individual estão em ESPACOS-RESTANTES.md; esse arquivo inclui também as três assimetrias de coluna e os começos/fins de capítulo.

## Continuidade e aparência

O gerador deixa o bloco continuar entre parágrafos e linhas de tabela. Mantém título, preço e primeiro parágrafo juntos; em aberturas curtas ligadas a tabelas, mantém também as primeiras linhas. Tabelas longas podem quebrar, repetindo o cabeçalho. As partes de uma tabela que couberem juntas voltam a formar uma única tabela, sem cabeçalhos duplicados dentro da mesma coluna.

Há no máximo um par de colunas por página: leitura integral da esquerda, depois integral da direita. Depois de um elemento largo, o par seguinte é equilibrado dentro das possibilidades dos parágrafos inteiros. Algumas diferenças de altura permanecem para preservar aberturas e unidades de leitura. Parágrafos não foram cortados no meio nesta rodada. Fontes, tamanhos, estilos aprovados, artes, capa e créditos foram mantidos. Corpo permanece 10,25 pt, entrelinha 13,2 pt.

Na inspeção apareceu uma abertura curta de Balestra sem a tabela. Foi corrigida; agora começa com a tabela na p. 190. Muro começa junto da primeira habilidade na p. 87, seguindo a ordem das colunas. Extensão de Domínio e Duração e custo estão na coluna esquerda da p. 271. As nove Famílias do catálogo começam na mesma página de sua primeira Melhoria.

## Validação e limites

- Comparação exata do Markdown: só os três blocos autorizados diferem.
- Arquivos da R37 conferidos contra o inventário inicial: nenhum foi alterado.
- Ordem dos parágrafos e linhas de tabelas preservada; 33 repetições de cabeçalho correspondem a continuações reais.
- Nenhum título isolado, retorno da coluna direita à esquerda ou segundo par de colunas na mesma página de fluxo.
- Validação geral: 108.108 verificações, 2.240 links internos, nenhum problema encontrado.
- Visão geral das 367 páginas, incluindo reinspeção das {len(changed)} páginas recompostas na última prova; inspeção ampliada de {len(large)} páginas selecionadas. Composições idênticas aproveitaram a inspeção anterior, com comparação de texto e geometria documentada. As imagens correspondem ao PDF final.

O exame visual desta rodada verifica composição e continuidade, com leitura das adições. Não substitui o pente-fino textual anterior nem representa uma nova leitura palavra por palavra de todas as páginas. Não foi realizado teste de mesa das novas Bênçãos.

## Arquivos de auditoria

- ALTERACOES-TEXTO.json: três blocos textuais completos.
- ALTERACOES-REGRAS.json: os dois blocos da adição de Bênçãos.
- ALTERACOES-DIAGRAMACAO.json: 502 registros com composição anterior/posterior, incluindo elementos gerados.
- CONFERENCIA.json, CONFERENCIA-GERAL.log e INDICE-CONFERIDO.json: verificações.
- REVISAO-PAGINAS.json e REVISAO-VISUAL.json: cobertura da inspeção visual.
- CORRESPONDENCIA-PAGINAS.json: localização na R38 dos conteúdos das 43 páginas apontadas da R37.
- APROVEITAMENTO-R37.json e APROVEITAMENTO-R38.json: medição completa.
- PROVA-R38.html: navegador das páginas renderizadas; abre nas Bênçãos.
- IMPLEMENTACAO.patch e REGISTRO-IMPLEMENTACAO.json: alterações do gerador e seus verificadores.

PDF final: output/pdf/Ciclo-Maldito-R38-Aproveitamento.pdf.

SHA-256 do PDF: {c['sha256_pdf']}.

SHA-256 do LIVRO-COMPLETO.md: {c['sha256_texto']}.

Próxima etapa da fila: leitura e aceite do autor sobre a R38. Para analisar os retornos, recomendação editorial: GPT-6 Astra, esforço alto. A documentação oficial o indica para trabalho complexo com documentos e oferece esforço high: https://developers.openai.com/api/docs/models/gpt-6-astra. A escolha de alto é julgamento para esta etapa, não uma comparação medida entre modelos neste livro.
'''
(R/'RELATORIO.md').write_text(report)
(R/'DUVIDAS.md').write_text('# Dúvidas e limites — R38\n\nNenhuma decisão de regra aguardando resposta. O autor esclareceu que são duas Bênçãos e delegou requisitos, alcance e balanceamento. As duas foram aplicadas.\n\nA redução adicional das onze folgas antes de aberturas ilustradas foi deixada de fora para preservar as aberturas e a ordem de apresentação; ver ESPACOS-RESTANTES.md.\n\nNão há exemplos refeitos. As novas Bênçãos ainda não passaram por teste de mesa.\n')
(B/'LEIA-ME-R38.md').write_text('''# Ciclo Maldito — R38

367 páginas (27 a menos que a R37). R37 intacta. Sem commit/push.

- [PDF](output/pdf/Ciclo-Maldito-R38-Aproveitamento.pdf)
- [Livro completo em texto](LIVRO-COMPLETO.md)
- [Relatório da entrega](revisao-r38/RELATORIO.md)
- [Espaços restantes e justificativas](revisao-r38/ESPACOS-RESTANTES.md)
- [Visualizar páginas](revisao-r38/PROVA-R38.html)
- [Alterações textuais](revisao-r38/ALTERACOES-TEXTO.json)
- [Decisões sobre as duas Bênçãos](revisao-r38/DECISOES-DE-BALANCEAMENTO.md)

O texto anterior foi preservado fora da frase restaurada em Sentir Energia, das duas Bênçãos e das duas linhas delas no catálogo. Nenhum exemplo foi refeito. Fontes, tamanhos, artes e créditos mantidos.

Os diretórios herdados da R37 são registros históricos. Os registros desta rodada estão exclusivamente em revisao-r38/. Use o PDF R38 indicado acima.
''')
names=['gerar_livro.py','ler_fontes.py','fluxo_continuo.py','tabelas_destaques.py','revisao_r38.py','revisao-de-hierarquia/CLASSIFICACAO.json','conferir_r38.py','medir_aproveitamento.py','renderizar_prova.py','fechar_relatorio_r38.py']
patch=[];records=[]
for name in names:
 prev=O/name;cur=B/name;old=prev.read_text() if prev.exists() else '';new=cur.read_text()
 records.append({'arquivo':name,'sha256_antes':sha(prev) if prev.exists() else None,'sha256_depois':sha(cur)})
 patch.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='R37/'+name,tofile='R38/'+name))
(R/'IMPLEMENTACAO.patch').write_text(''.join(patch));write('REGISTRO-IMPLEMENTACAO.json',records)
html=(R/'PROVA-R38.html').read_text().replace('p. 286 · branco 48%','p. 286 · branco 49%')
(R/'PROVA-R38.html').write_text(html)
print('Relatórios prontos;',len(visual),'registros visuais;',len(large),'páginas ampliadas.')

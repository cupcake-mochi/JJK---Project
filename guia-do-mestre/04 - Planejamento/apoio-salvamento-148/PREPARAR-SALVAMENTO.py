from pathlib import Path
import json,hashlib,os,re,shutil
r=Path('/media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem');a=r/'04 - Planejamento/apoio-salvamento-148';a.mkdir(exist_ok=False)
save=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mp=r/'04 - Planejamento/apoio-piloto/manifesto-entrega.json';base=json.loads(mp.read_text());assert len(base)==7061
(a/'antes').mkdir();shutil.copy2(mp,a/'antes/manifesto-entrega.json')
prompt=r/'RETOMADA-NUVEM-2026-10-31.txt'
prompt.write_text('''RETOMAR O GUIA DO MESTRE DE CICLO MALDITO — 31/10/2026

Continue o projeto existente, concluído editorialmente até o registro 147 e salvo para continuidade no 148. Não reinicie a redação nem repita as filas históricas.

REPOSITÓRIO E ENTRADA
Repositório: https://github.com/cupcake-mochi/JJK---Project
Branch com o trabalho: codex/guia-do-mestre-pre-1-2026-10-23
Pasta do projeto dentro do checkout: guia-do-mestre/
A partir daqui, todos os caminhos são relativos a essa pasta. O checkout da nuvem pode ter outro caminho absoluto. Confirme a branch e o estado atual antes de editar; preserve qualquer trabalho posterior ao salvamento.
Leia primeiro README.md, esta retomada, 04 - Planejamento/147-ajustes-de-consulta-e-leitura.md, 04 - Planejamento/146-comparacao-final-e-proximos-ajustes.md e a fila vigente e as seções 5–7 de 04 - Planejamento/98-plano-de-melhoria-e-validacao-do-guia.md. Os avisos de fila histórica e prompts de datas anteriores documentam etapas já concluídas. Os dizeres “salvamento local; último GitHub 141” nos relatórios descrevem o momento em que foram escritos; SALVAMENTO.json identifica o snapshot mais novo.

ESTADO ATUAL
A estrutura e a redação da pré-1.0 estão montadas. Os 59 casos e as 17 consultas foram revistos, o conjunto foi integrado no 136 e as 99 fontes tiveram leitura contínua nos registros 137–144. O PDF integrado foi recomposto e conferido no 145; a comparação com outros guias foi concluída no 146, com conclusões parciais sobre aprendizagem externa e dificuldade geral de encontros. O registro 147 resolveu os três ajustes delimitados dessa comparação: folhas curtas antes dos formulários completos, distinção visual entre fala e comentário do mestre e redução de lembretes genéricos repetidos nas ideias de aventuras.

Fontes vigentes: 06 - Redacao do Guia/edicao-integrada-136/
HTML vigente: 07 - Edicao de Leitura/edicao-integrada-136/index.html
PDF vigente: 08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Editorial.pdf — 383 páginas, SHA-256 dc5e892776bdc87501b9474dcd23be7107fdd35ad7442e898198cdafe17ec258.
Pacote para impressão: 08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa-Impressao.pdf — 6 páginas, SHA-256 277abc8248ef6c2cd4ad52e8f1258b3156ee68330d9c15c85df46f7cc736b48f. Mantém os números 82–87 e as referências ao volume completo; sem navegação clicável.
O PDF anterior “Revisado” de 383 páginas e o PDF antigo de 357 páginas são históricos, não a edição vigente.

CONFERÊNCIAS CONCLUÍDAS
No 147: oito alterações editoriais em 03a-ideias-para-aventuras.md; as outras 98 fontes integradas e a sequência numérica da fonte alterada foram preservadas. Houve duas passagens dirigidas dos trechos alterados; não duas novas releituras integrais do volume. O HTML teve 1.926 links locais conferidos. O PDF teve 2.553 links, 99 marcadores e nenhuma diferença de extração por resolver. A composição das 383 páginas foi examinada em 43 painéis, com ampliações das páginas 5, 7, 8, 9, 24, 30 e 82–87. Não houve inspeção individual ampliada de todas as páginas, leitura independente ou teste humano. As seis páginas de impressão foram comparadas em texto e imagem com o volume completo.
Evidências e hashes: 04 - Planejamento/apoio-editorial-147/{conferencia-editorial.json,conferencia-do-pdf.json,revisao-visual.json,cobertura-da-leitura.json,composicao.json,pacote-de-impressao.json}.

PRÓXIMA TAREFA
Preparar o plano de avaliação da dificuldade dos encontros. Esta frente ainda não foi executada: não confundir contas e ensaios internos anteriores com validação geral do equilíbrio.
1. Ler o capítulo 6 e os exemplos atuais de inimigos, recursos, confrontos e socorro, junto da matriz e das notas do apoio-comparacao-146.
2. Formular o que os exemplos ainda não respondem: tamanhos de grupo e níveis, composição e capacidade de proteção, PE e outros recursos, controle, terreno, informações, objetivo, duração, derrota, socorro e retirada.
3. Definir um conjunto finito de comparações, suas premissas, medidas observadas e limites. Registrar decisões e resultados além de dano médio e rodadas. Distinguir contas, simulações simplificadas e mesas reais.
4. Entregar o plano, os casos de comparação e a lista de limites atuais. Não inventar uma tabela geral, interpolar níveis nem alterar fichas para parecerem equilibradas antes das comparações.
5. Usar o próximo registro livre, guardar estados anteriores e atualizar a fila e o manifesto por união. Apresentar escolhas mecânicas novas ao autor com comparação concreta. Não pedir autorização para cada ajuste editorial já autorizado.
Configuração prevista pelo projeto: GPT-6 Astra, esforço extra alto, se disponível no ambiente. Para correções editoriais e incorporação de retorno: GPT-6.1 Sol, esforço alto. Essa indicação registra a preferência do planejamento, sem garantir quais modelos estarão disponíveis na conta.

OUTRAS PENDÊNCIAS
A pré-1.0 já pode receber comentários. O plano 98 prevê três perfis de leitores: iniciante sem JJK, iniciante que conhece a obra e mestre experiente. Não foi recrutada pessoa alguma. O assistente pode preparar as tarefas e organizar retorno real, mas não inventá-lo. Correções decorrentes e fechamento da 1.0 terão limites e decisão próprios. Bestiário completo, novos benefícios de treinamento e ideias de Pactos adiadas são frentes futuras, não condições automáticas para encerrar esta revisão.

DECISÕES A PRESERVAR
O Guia ensina a mestrar Ciclo Maldito com foco na guilda, mas seus ensinamentos também servem a campanhas fechadas. Oferecer um caminho recomendado e alternativas explicadas. Priorizar linguagem natural, títulos simples, exemplos e consulta fácil. No texto para o leitor, dizer Livro de Regras 1.0.
Referência técnica conferida: 04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md, SHA-256 7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d. Não migrar silenciosamente para outra revisão encontrada no repositório ou no PC. Os números do Bestiário antigo não estão atualizados.
Inimigos não precisam todos de PE: há referências com reserva, recarga, intervalo, preparo e outros limites. PE ou recarga isoladamente não criam motivo para guardar uma habilidade; conferir escolha, custo e resposta possível. As fichas experimentais não são equivalências garantidas de dificuldade.
Receptáculo: recomendar o mestre como outra voz mediante acordo com o jogador, preservando as decisões da personagem e explicando alternativas.
Dedicação: 28 horas novas por ficha em sete dias; aproximadamente dias reais. Fichas diferentes têm concessões independentes. Só horas novas livres passam ao ciclo seguinte uma vez; gastar as antigas primeiro. Não confundir dedicação por ficha com desconto de XP por jogador.
Treinamentos específicos não têm novo pacote numérico aprovado; não presumir atrofia por falta de postagem. Reserva Condensada permanece como habilidade publicada e acordo individual, sem os depósitos, tetos e retiradas numéricos descartados pelo autor.
Pactos e projetos de entidades têm escolhas autorais registradas. Consulte o texto e as decisões, sem reconstruí-los com novas recomendações por preferência. A entrada do mundo não tem revelações da trama; aprofundamentos do mangá ficam separados e sinalizados.

TRABALHAR NA NUVEM
Há fontes, pesquisas produzidas pelo projeto, históricos, PDFs, fontes tipográficas, mapas e provas visuais no Git. Os livros completos de terceiros e algumas extrações integrais externas continuam somente no acervo local, conforme as exclusões dos salvamentos anteriores. Não dizer que consultou um livro ausente. Começar pelos relatórios e evidências disponíveis; para lacunas, usar fontes primárias acessíveis e identificar exatamente o que foi consultado. Não reconstruir ou redistribuir livros de terceiros para preencher a ausência.
A produção local original ficava em /media/mizuki/HD Externo II/Claude/Pesquisa de Campo - Mestragem/. Pesquisas adicionais ficavam em /home/mizuki/CHAT-GPT/RPG -JJK/Conceitos de Ideias para o sistema/ e /media/mizuki/HD Externo II/Claude/Claude 2/. Esses caminhos são referências locais, não caminhos disponíveis garantidos na nuvem. O plano de encontros pode começar com o conteúdo salvo; pergunte por algo ausente somente quando ele realmente impedir uma conclusão necessária.
Geradores vigentes: 04 - Planejamento/apoio-editorial-147/GERAR-LEITURA.py e GERAR-PDF.py. Ambos localizam a raiz pela própria posição; preservar a estrutura de pastas. O gerador HTML escreve composicao.json; antes de compor PDF, copiar a configuração gerada para fontes-para-compor.json, que o PDF usa, preservando o registro anterior. A composição PDF também grava composicao.json. Não rodar geração para simplesmente retomar o planejamento.
Bibliotecas usadas: Python 3.12, beautifulsoup4, markdown, reportlab, svglib, Pillow, PyMuPDF e pypdf; arquivos tipográficos estão em 08 - Diagramacao do Guia/fontes. Os caminhos /tmp/ciclo-guia-pdf-145 e pacotes instalados no PC não fazem parte do Git. Preparar o ambiente apenas quando houver necessidade de executar geração ou renderização. Não executar os preparadores PREPARAR.py, FECHAR.py ou CONCLUIR-CONFERENCIA.py do 147: são registros da operação já concluída, não uma retomada idempotente. Scripts de conferência de registros antigos podem conter caminhos absolutos e hashes históricos; ler e adaptar em uma nova cópia antes de usar. Não rodar o antigo preparador 136 sobre as fontes vigentes.
Para conferir o snapshot, os conferidores CONFERIR-COPIA-GIT.py e CONFERIR-SALVAMENTO.py na raiz de guia-do-mestre são somente de leitura e descobrem a raiz pela própria localização. O primeiro usa SALVAMENTO.json; o segundo usa o manifesto da produção. O inventário é um snapshot anterior às próximas edições: divergências após mudanças deliberadas devem ser registradas, não “corrigidas” restaurando material antigo.

COMUNICAÇÃO E ENCERRAMENTO
Continuar autonomamente dentro do escopo autorizado. Trazer dúvidas reais sobre mecânica e decisões autorais com alternativas concretas. Ao fim de cada entrega, dizer o que foi feito, como foi conferido, o que falta e recomendar próxima tarefa, modelo e esforço. Não declarar igualdade geral com livros publicados, inspeção não realizada, teste humano ou equilíbrio certificado. Não abrir automaticamente outros chats ou agentes.
''')
report=r/'04 - Planejamento/148-salvamento-e-retomada-na-nuvem.md'
report.write_text('''# Salvamento e retomada na nuvem

Registro 148, 31/10/2026. O autor solicitou salvar o trabalho para possível continuidade pelo Codex na nuvem. Este registro prepara o salvamento dos registros 142–147 e não altera o conteúdo do livro nem suas regras.

A fila editorial principal está concluída. A edição vigente é o PDF Editorial de 383 páginas, com pacote de seis páginas para impressão. O próximo trabalho é o plano de avaliação da dificuldade dos encontros, conforme o plano 98. Retorno real de leitores pode ser incorporado em paralelo. O fechamento da 1.0, o bestiário completo, os benefícios de treinamento e Pactos adiados não foram concluídos por este salvamento.

A [retomada para a nuvem](../RETOMADA-NUVEM-2026-10-31.txt) identifica fontes, PDFs, geradores, evidências, decisões, limitações e a próxima tarefa. Os caminhos principais são relativos à pasta `guia-do-mestre` no repositório. Os livros completos e as extrações externas anteriormente excluídas continuam no acervo local; o salvamento não promete acesso a esses arquivos na nuvem.

Destino: `cupcake-mochi/JJK---Project`, branch `codex/guia-do-mestre-pre-1-2026-10-23`, pasta `guia-do-mestre`. A cópia é feita da produção para o checkout de salvamento, sem substituir a produção por uma versão antiga e sem excluir arquivos anteriores. Os PDFs e evidências anteriores permanecem preservados. `SALVAMENTO.json` e os conferidores na cópia Git registram a integridade do snapshot; o comprovante local da operação recebe o commit e o resultado da confirmação remota após o envio.

O registro 147 permanece a última alteração editorial. Avisos anteriores de salvamento local descrevem seu estado histórico. A conclusão do envio só deve ser anunciada após confirmar a mesma revisão na branch remota.

Próxima tarefa recomendada: elaborar o plano de avaliação dos encontros. Configuração prevista: GPT-6 Astra, esforço extra alto, quando disponível. Para correções de texto e retorno de leitores: GPT-6.1 Sol, esforço alto.
''')
controls=json.loads((r/'04 - Planejamento/apoio-editorial-147/arquivos-do-lote.json').read_text())['controles']
for rel in controls:
 p=r/rel;assert sha(p)==base[rel],rel;q=a/'antes'/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
 s=re.sub(r'> \*\*Fila vigente', '> **Fila histórica',p.read_text(),count=1);first,rest=s.split('\n',1)
 banner=f'> **Fila vigente - registro 148, 31/10/2026:** salvamento para retomada na nuvem até o registro editorial 147; [estado e retomada](<{os.path.relpath(report,p.parent)}>). Livro e pacote de impressão concluídos. Próximo: plano de avaliação da dificuldade dos encontros; GPT-6 Astra, esforço extra alto. Retorno de leitores pode acompanhar o trabalho. Confirmar envio em `SALVAMENTO.json` e no comprovante da operação; avisos anteriores são históricos.\n\n'
 p.write_text(first+'\n\n'+banner+rest.lstrip('\n'))
shutil.copy2(Path(__file__),a/'PREPARAR-SALVAMENTO.py')
save(a/'arquivos-do-lote.json',{'registro':148,'controles':controls,'retomada':prompt.relative_to(r).as_posix(),'relatorio':report.relative_to(r).as_posix(),'conteudo_editorial_alterado':False,'ultimo_registro_editorial':147})
updated=dict(base)
for rel in controls:updated[rel]=sha(r/rel)
for p in [prompt,report]+[p for p in a.rglob('*') if p.is_file()]:updated[p.relative_to(r).as_posix()]=sha(p)
save(mp,updated)
print(json.dumps({'registro':148,'entradas_anteriores':len(base),'entradas_manifesto':len(updated),'controles':len(controls),'livro_alterado':False},ensure_ascii=False))

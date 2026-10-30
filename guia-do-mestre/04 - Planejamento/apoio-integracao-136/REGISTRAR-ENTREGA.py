"""Registrar a integração local; não altera as 94 fontes da revisão 135."""
from pathlib import Path
import json,os,re,hashlib
A=Path(__file__).resolve().parent;R=A.parents[1]
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report=R/'04 - Planejamento/136-integracao-editorial-e-apoios.md'
config=json.loads((A/'arquivos-do-lote.json').read_text())
config['controles']=[p for p in config['controles'] if p!='06 - Redacao do Guia/revisao-98/consultas/LEIA-ME.md']
config['guia_de_consulta_vigente']='06 - Redacao do Guia/edicao-integrada-136/consultas/LEIA-ME.md'
config['relatorio']=report.relative_to(R).as_posix()
config['preservacao']='As 94 fontes da revisão 135 permanecem intactas, incluindo seu guia de consulta. Nove controles anteriores recebem indicação da edição nova; o guia vigente pertence à cópia integrada.'
save(A/'arquivos-do-lote.json',config)
report.write_text('''# Integração editorial e apoios recuperados

Registro 136, 30 de outubro de 2026. Continuação da conferência encerrada no registro 135. Esta entrega reúne a nova estrutura em uma edição local de leitura e recupera os apoios necessários aos exemplos. A leitura contínua do conjunto e o novo PDF completo ainda não estão concluídos.

[Abrir a edição reunida](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Fontes editáveis](<../06 - Redacao do Guia/edicao-integrada-136/00-como-usar-este-livro.md>) · [Prova dos três apoios](apoio-integracao-136/output/pdf/Ciclo-Maldito-Apoios-da-Integracao.pdf) · [Conferência da integração](apoio-integracao-136/conferencia-da-integracao.json) · [Revisão visual da prova](apoio-integracao-136/revisao-visual.json).

## O conjunto reunido

A cópia integrada parte das 94 fontes vigentes no fechamento anterior: abertura, dez capítulos e complemento de ideias, 59 casos, 17 consultas complementares, cinco folhas curtas e seu guia. Foram recuperados três textos adicionais: a convivência do Receptáculo, a base de três maldições e a orientação publicada para Reserva Condensada. São 97 fontes de entrada, com origem e resumo de integridade registrados.

O índice de casos e a bibliografia para o leitor acrescentam duas fontes geradas. As 99 unidades de fonte produzem 98 documentos HTML de conteúdo: o complemento de ideias foi inserido na seção 3.6, antes da 3.7, em vez de aparecer como capítulo separado. Com o índice geral, há 99 arquivos HTML. Essa contagem não é a paginação do futuro PDF.

A edição tem três entradas — aprender a mestrar, preparar a próxima sessão e consultar durante o jogo — e permite seguir a sequência dos capítulos. Depois vêm folhas, casos por assunto, termos do mundo, aprofundamento da obra e referências. Os acessos ao aprofundamento trazem aviso de revelações, inclusive no retorno pela página de referências. A abertura do mundo não exige conhecer a trama.

As fontes estão em `06 - Redacao do Guia/edicao-integrada-136/`; a leitura, em `07 - Edicao de Leitura/edicao-integrada-136/`. Cada ligação local da edição aponta para esta cópia. Não é necessário abrir documentos de planejamento para acompanhar um exemplo. A bibliografia distingue o Livro de Regras 1.0, as referências de outros RPGs e as fontes da obra; não incorpora regras de outros jogos ao sistema.

## Apoios e repetições

| Material encontrado | Destino na leitura reunida |
|---|---|
| Convivência do Receptáculo, fonte 27 | Caso “Maia e Taru: a presença em cena”. A distribuição das vozes e suas alternativas ficam no capítulo 7; o caso aprofunda cenas, capacidades e continuidade. |
| Base pequena, registro 14 | Caso “Três maldições para a missão”, junto dos confrontos. Fichas e conversões completas; valores experimentais preservados. |
| Reserva Condensada, fonte 92 | Consulta “Reserva Condensada: acordo por personagem”. Mantém os quatro campos do acordo e o exemplo de conferência; retira o histórico de desenvolvimento da leitura. |
| Recompensas, fonte 37 | O método já está no capítulo 8. Entram apenas os dois exemplos que faltavam, de metade e de nenhuma recompensa, sem publicar o mesmo texto duas vezes. |
| Comparação de Condução, registro 46 | A distinção em relação a Sem Ver e ao exemplo antigo foi incorporada ao caso de Pacifismo. O leitor não precisa do relatório de trabalho. |
| Piloto, registro 13 | Remissão para a missão do capítulo 1, que já reúne o conteúdo. |
| Referências antigas de pesquisa | Bibliografia própria para o leitor; o inventário de pesquisa continua no histórico. |
| Ligações antigas a HTML | Treze remissões antigas foram identificadas e encaminhadas às seções atuais correspondentes. |
| Complemento de ideias, fonte 03a | Incluído uma vez em 3.6, antes de “Quando há pouco tempo”. |

O texto de Reserva Condensada não adota depósitos, tetos, retiradas ou recargas propostos e depois descartados pelo autor. Continua sendo a menor opcional já existente da Restrição corporal, com o acordo exigido pelo Livro de Regras 1.0. Também não foi reaberta a escala de inimigos nem acrescentada progressão por treinamento.

## Conferência textual e das referências

O histórico tem 169 registros de alteração, reproduzidos a partir das 97 entradas originais. As 286 tabelas foram comparadas por célula, admitindo apenas mudanças de destino dos links; o quadro de distribuição de vozes retirado do caso permanece atendido no capítulo 7. As diferenças numéricas editoriais estão listadas: identificação da edição, retirada de números de registros e versão, e o exemplo de recompensa copiado da fonte. Nenhum custo, dado, distância ou parâmetro das fichas foi recalculado como regra nova.

A verificação estrutural percorreu 1.883 links nos 99 documentos HTML e suas âncoras, além das nove imagens locais. Não encontrou destino ou âncora ausente. As 99 unidades de fonte têm destino de leitura; o complemento de ideias não duplica seu conteúdo. Foram refeitas as contas dos apoios: Amparo Interior, Reserva Impregnada, Integridade das maldições, conversões e limites de destruição. A conferência final está no arquivo ligado no início.

A passagem de leitura dos três apoios recuperados foi seguida de uma nova passagem dirigida às alterações, aos títulos e às contas. Isso não equivale à releitura contínua das aproximadamente 181 mil palavras do levantamento anterior. A cópia integrada ainda precisa ser lida em sequência para avaliar transições, repetições entre textos completos e a facilidade de consulta do conjunto.

A sinopse oficial do volume 18, antes indisponível, foi consultada no [catálogo da Shueisha](https://www.shueisha.co.jp/books/items/contents_amp.html?jdcn=08X10000000018964300). Ela sustenta o recorte do encontro com Hakari usado no aprofundamento, sem fornecer um desfecho adicional. As sinopses oficiais dos episódios [48](https://jujutsukaisen.jp/episodes/48.php), [50](https://jujutsukaisen.jp/episodes/50.php), [51](https://jujutsukaisen.jp/episodes/51.php) e [55](https://jujutsukaisen.jp/episodes/55.php) foram reconferidas nos limites dos exemplos já escritos. Essa consulta não representa conferência integral do mangá.

## Mapas e prova visual

A edição reúne sete mapas de casos e as duas plantas já usadas nas fontes. Quatro mapas foram copiados sem alteração. No confronto da dupla, Ren e Sora passaram a Toru e Sayo; no arquivo, Haru passou a Daigo. As coordenadas e as distâncias foram preservadas. O mapa do Carregador usa a versão corrigida, com os três trechos da rota direta e a alternativa lateral claramente separados. Os três mapas atualizados foram inspecionados diretamente; origem e integridade estão em `mapas-reunidos.json`.

A prova PDF desta entrega contém somente os três apoios recuperados. A primeira composição tinha nove páginas, um quadro estreito e fechamentos quase vazios. As iterações ampliaram os quadros extensos, separaram melhor as colunas e mantiveram ataques inteiros. Os dois quadros curtos de Reserva permanecem dentro das colunas. A prova final tem sete páginas, todas renderizadas e inspecionadas diretamente. O corpo de texto foi mantido em 10,25 pontos; a redução de páginas veio do fluxo e dos quadros, sem suprimir texto. A comparação de palavras não encontrou ausência ou acréscimo no conteúdo; a conferência de coordenadas não encontrou texto fora das páginas.

Há continuações normais de parágrafos e hifenização na prova parcial. Ela não fixa os inícios de capítulo do futuro livro. As primeiras provas continuam preservadas para comparação. O arquivo de sete páginas não substitui o PDF integrado anterior de 357 páginas.

O navegador integrado bloqueou a abertura do protocolo de arquivos locais. A revisão desta entrega usou conferência dos arquivos e provas estáticas; não houve inspeção da navegação nem da apresentação HTML no navegador. Essa limitação permanece explícita e não foi contornada.

## Preservação e próxima tarefa

As 104 fontes originais, as 94 fontes da revisão 135 e o PDF anterior permanecem preservados. Nove arquivos de continuidade recebem o novo apontamento; o guia de consulta histórico da revisão 135 não é alterado, pois a edição nova tem sua própria cópia. O manifesto é atualizado por união, preservando as 4.104 entradas anteriores e acrescentando os artefatos deste registro. As mudanças de controles são declaradas separadamente dos textos do livro.

**Próxima tarefa: leitura contínua da edição reunida, começando pela abertura e pelos capítulos 1–3. Modelo: GPT-6.1 Sol; esforço alto.** Ler capítulo e casos citados juntos, anotar duplicações antes de remover trechos, conferir o que foi retomado longe demais e manter uma lista de intervenções. Em seguida, seguir pelos capítulos 4–10 e consultas. Só após essa passagem, compor o PDF completo, revisar visualmente cada página, corrigir e repetir a inspeção das páginas afetadas. A comparação final com o livro base e os guias de referência continua pendente; esta integração não declara equivalência de qualidade ou equilíbrio validado em mesa.
''')
# Atualizar somente os nove controles declarados; fontes de leitor antigas ficam intactas.
for rel in config['controles']:
 p=R/rel;before=A/'antes'/rel
 if not before.exists():before.parent.mkdir(parents=True,exist_ok=True);before.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 136,' in s:continue
 s=s.replace('**Fila vigente - registro 135,','**Fila histórica - registro 135,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 136, 30/10/2026:** cópia integrada de leitura montada, com apoios recuperados e referências conferidas. [Entrega e edição reunida](<{url}>). Prova parcial dos três apoios com sete páginas inspecionadas. **Próximo: leitura contínua do conjunto, começando pela abertura e pelos capítulos 1–3; GPT-6.1 Sol, esforço alto.** PDF completo novo, revisão visual global e comparação final ainda pendentes. Fontes anteriores e PDF de 357 páginas preservados.\n\n'
 first=s.find('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'\*\*Próxima tarefa:\*\* integração editorial e leitura contínua:.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** leitura contínua da cópia integrada, pela abertura e capítulos 1–3, seguida das demais partes. Depois, PDF completo e revisão visual global. **GPT-6.1 Sol, esforço alto.**',s,flags=re.S)
 p.write_text(s)
proof=json.loads((A/'revisao-visual.json').read_text());assert len(proof['paginas'])==7
save(A/'fontes-da-obra-conferidas.json',{'data':'2026-10-30','metodo':'Consulta primária dirigida às afirmações já usadas; não leitura integral do mangá.','fontes':[{'url':'https://www.shueisha.co.jp/books/items/contents_amp.html?jdcn=08X10000000018964300','verificado':'Volume 18: aproximação a Hakari, suspenso da escola e ligado às lutas com apostas; Megumi encontra outra técnica na infiltração. O recorte não acrescenta resultado da negociação.'}]+[{'url':f'https://jujutsukaisen.jp/episodes/{n}.php','verificado':t} for n,t in [(48,'Pós-Shibuya, Yuji e Choso; Naoya e a execução atribuída a Yuta.'),(50,'Procura por Tengen, selamento de Gojo e informações sobre o Jogo do Abate.'),(51,'Busca de ferramentas por Maki e confronto familiar envolvendo Mai.'),(55,'Higuruma advogado; Yuji e Megumi obtêm informações em locais diferentes.')]]})
print('Registro e nove controles atualizados; fontes de leitor anteriores preservadas.')

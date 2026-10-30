"""Registrar a leitura de inimigos e os ajustes editoriais do lote 139."""
from pathlib import Path
import json,hashlib,os,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
cases=['75-ren-e-sora-atacante-e-apoio.md','63-carregador-consulta-e-doma.md','60-montar-habilidades-de-inimigos.md','74-regua-inicial-de-inimigos.md','59-recursos-e-ritmo-dos-inimigos.md','100-comparar-inimigos-em-outras-faixas.md','76-confronto-de-ren-e-sora.md','77-ficha-preenchida-ren-e-sora.md','65-comparar-confronto-e-pressao-ambiental.md','66-o-carregador-e-a-saida-que-fecha.md','62-o-carregador-e-o-corredor-de-entulho.md','68-ficha-e-comparacao-de-chefes.md','71-sineiro-do-recolhimento.md','73-ensaio-guiado-do-sineiro.md','78-preparar-perigos-ambientais.md','79-o-po-na-sala-de-conservacao.md','103-a-febre-dos-fios.md']
assert len(cases)==17
files=['06-inimigos-e-perigos.md','consultas/58-ficha-de-inimigo-e-encontro.md']+['casos/'+name for name in cases]
rows=[{'fonte':(T/name).relative_to(R).as_posix(),'sha256':sha(T/name),'palavras_da_fonte':len((T/name).read_text().split()),'alcance':'Leitura completa e comparação com a explicação do capítulo. Capítulo 6 em duas passagens; trechos alterados dos apoios revistos em contexto.'} for name in files]
old137=json.loads((R/'04 - Planejamento/apoio-leitura-137/leitura-realizada.json').read_text());old138=json.loads((R/'04 - Planejamento/apoio-leitura-138/leitura-realizada.json').read_text())
previous={e['fonte']:(e,137) for e in old137['nucleo']};previous.update({e['fonte']:(e,138) for e in old138['fontes_lidas']})
reuse=[]
for name in ['01-sua-primeira-missao.md','04-na-mesa-de-jogo.md','consultas/24-registro-de-estado-e-socorro.md','consultas/A4-retomar-a-missao.md']:
 rel=(T/name).relative_to(R).as_posix();row,record=previous[rel];assert sha(T/name)==row['sha256']
 reuse.append({'fonte':rel,'sha256':row['sha256'],'leitura_integral_anterior':record,'alcance_atual':'Retomadas as referências usadas pelo capítulo 6; fonte inalterada, sem nova alegação de leitura integral neste lote.'})
save(A/'leitura-realizada.json',{'registro':139,'data':'2026-10-30','fontes_lidas':rows,'fontes_retomadas':reuse,'regras_consultadas':['Maestria','Bloquear','Agarrar, derrubar e empurrar','Integridade de criaturas e estágios','Categoria de Efeito e Classe','Leitura de Reservas','Envenenado e condições Pesadas'],'fonte_tecnica':'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','limite':'Leitura editorial, comparação de exemplos e cálculos selecionados. Não é sessão observada, avaliação completa de todos os percentuais do livro nem revisão visual do PDF completo.'})
report=R/'04 - Planejamento/139-leitura-de-inimigos-e-perigos.md'
report.write_text('''# Leitura de inimigos e perigos

Registro 139, 30 de outubro de 2026. A leitura contínua do capítulo 6 foi concluída junto das fichas, confrontos e perigos que ele usa. Os ajustes melhoram a explicação das classificações, a escolha dos limites de uso e o acesso às comparações. Não alteram vida, dano, custos ou regras de aquisição.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Inimigos e perigos](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-06.html>) · [Histórico dos ajustes](apoio-leitura-139/alteracoes.json) · [Conferência](apoio-leitura-139/conferencia.json) · [Contas selecionadas](apoio-leitura-139/contas-reconferidas.json).

## O que foi lido

Foram lidos por inteiro o capítulo 6, a ficha de inimigo e encontro e 17 casos: PE e limites de uso; montagem de habilidades; encontro e ficha do Carregador; combinação com o portão; conferência de chefes; ficha e dois percursos do Sineiro; referências numéricas; outras faixas de nível; ficha, confronto e registro de Toru e Sayo; preparo de perigos; sala de conservação; e febre dos fios.

O núcleo passou por uma segunda leitura completa. Os trechos modificados dos apoios foram relidos em contexto. O inventário `leitura-realizada.json` lista cada arquivo e sua integridade. A missão do anexo, o capítulo de condução e as folhas de estado e retomada foram consultados pelas referências pertinentes; permanecem iguais aos estados lidos nos registros 137–138.

## O que mudou

| Dificuldade encontrada | Ajuste |
|---|---|
| Classe, Categoria de Efeito e nível apareciam como classificações diferentes, sem explicar onde usá-las | O capítulo relaciona Classe à montagem e ao custo-base do feitiço, CE aos Talentos e capacidades que a usam e nível à criatura. |
| O comparativo de PE e recarga só era encontrado por meio de outra consulta | O capítulo agora leva diretamente aos exemplos de limites de uso. |
| Montar habilidades começava exigindo ler outra seção inteira | A consulta de limites passou a ser um aprofundamento indicado, permitindo abrir o caso diretamente pelo capítulo. |
| “Seção anterior” e “exemplo anterior” ficavam ambíguos na leitura por assunto | As referências agora identificam o destino. Trançar placas também recebe seu nome na primeira apresentação da proteção do Amontoado. |
| O estudo numérico dizia que um “estudo completo” calculava Bloquear, sem oferecer acesso ao leitor | A ligação passou para a comparação de capacidades que apresenta um caso com Bloquear. A tabela local continua explicitamente restrita à Defesa estática. |
| A coluna de ataque dos perfis de níveis maiores podia ser confundida com resultado ou quantidade | O cabeçalho passou a “Bônus de ataque”; os valores são os mesmos. |
| O fechamento da ficha do Sineiro contava o histórico do aumento de vida em um bloco longo | Agora apresenta a comparação útil ao mestre e separa observação em mesa, números e uso do ensaio. |
| A entrada da doença usava uma nota de histórico e “contaminação portátil” | A abertura explica a doença diretamente e aponta o pó como comparação de exposição repetida numa área. As regras das duas fontes continuam distintas. |
| A abertura do capítulo remetia ao estado de um Bestiário antigo do projeto | A orientação agora pede conferir e atualizar uma ficha de edição anterior. O acervo desatualizado continua excluído como fonte de números. |

São **13 registros de alteração em sete fontes**. Dois rótulos de quadros foram ajustados: uma célula de exemplo em Montar habilidades e o cabeçalho de bônus de ataque. Nenhum valor das tabelas foi alterado. As demais mudanças são explicações, referências e divisão de parágrafos.

## PE e as escolhas do inimigo

A leitura confirma a abordagem já adotada: PE não são obrigatórios para toda habilidade especial. A escolha parte do efeito desejado e da resposta do grupo. Usos, intervalo fixo, recarga, preparo, condição e reserva compartilhada continuam disponíveis, com seus limites definidos pela ficha.

A reserva do Amontoado permite uma sequência curta, mas não o faz poupar energia por si. O Carregador cria pressão com contenção e percurso sem usar PE. Toru e Sayo oferecem uma disputa real entre gasto ofensivo, proteção e cura; Sayo também escolhe o destino de sua única Padrão. O Sineiro usa preparo corporal e exposição posterior, com tempo para o grupo responder. Nenhum exemplo foi convertido para um único modelo de recursos.

Recarga continua podendo permitir usos consecutivos. A dispensa experimental do custo normal de Impacto mantém a Classe e os acréscimos previstos na proposta; não altera o feitiço original, outra capacidade ou as fichas dos jogadores. Doma mantém conversões e atuação próprias, sem herdar automaticamente exceções do inimigo.

## Objetivo, terreno e resposta

Foram comparados os estados do confronto de Toru e Sayo com a ficha preenchida: custos, posições, benefício já concedido, derrota do apoio e retirada do atacante continuam coerentes. O objetivo pode terminar antes de todos os adversários serem derrotados. Uma soma de PV não transforma dois corpos em um chefe equivalente.

No Carregador, 18 m de percurso direto continuam custando 42 m ao arrastar por causa dos trechos; a rota lateral conserva seus próprios custos. No portão, operar a parada disputa a Padrão e não desliga a criatura. O serviço permanece disponível. Os mapas não foram redesenhados ou reavaliados visualmente neste lote.

No Sineiro, o intervalo entre preparo e impacto conserva os turnos de Mei, Akira e Rina antes da próxima atuação do chefe. Interromper o preparo, soltar a presa e sair da área são soluções diferentes. O percurso de socorro mantém tratamento e janela separados; o fim da oposição não recupera automaticamente as fichas.

Na sala de conservação, dano, condição, limpeza e atendimento continuam separados. A fase ambiental ocorre uma vez por rodada e a condição pode durar após a saída. A febre dos fios conserva transmissão própria, crises por horas, atendimento e término; o tempo de socorro de uma queda continua em rodadas. Nenhuma dessas escolhas virou regra universal de perigos ou doenças.

## Contas e conferência

A reconferência independente reproduziu as seis linhas de sobrevivência dos níveis 2 e 6, as três médias de golpes corporais, as probabilidades de duas tentativas contra dois estados de vida e as duas probabilidades de escolha de alvo entre Toru e Sayo. Os resultados coincidem com as casas decimais publicadas. O método calcula distribuições discretas sob as hipóteses escritas, incluindo erros e críticos; não simula as decisões ou ações de um encontro completo.

A conferência não recalcula todos os percentuais do livro. Os cálculos de outras faixas, incluindo todas as interações de Duro de Matar, não recebem aqui uma nova certificação independente. As contas selecionadas também não validam equilíbrio em mesa nem convertem conjuntos de ataques em rodadas de combate.

O histórico é reproduzido a partir das cópias anteriores das 99 fontes. Os números são comparados, e os quadros só admitem os dois ajustes textuais declarados. A verificação percorre os documentos HTML, os destinos e âncoras, imagens e ligações das fontes Markdown. As âncoras anteriores dos sete documentos modificados são mantidas. A contagem e o resultado final estão em `conferencia.json`.

## Salvamento e próxima tarefa

O estado anterior das 99 fontes e dos sete arquivos HTML modificados está em `apoio-leitura-139/antes/`. O manifesto é atualizado por união a partir de **4.663 entradas**, admitindo apenas as sete fontes, sete documentos de leitura e nove controles anteriores alterados. Os demais textos, fontes originais, mapas, fontes tipográficas e PDFs anteriores ficam preservados. O salvamento é local.

A edição vigente continua nas pastas `edicao-integrada-136`; o gerador atual está no apoio do registro 139. Não reaplique preparadores antigos sobre essa edição, pois reconstruiriam estados anteriores aos ajustes de leitura.

**Próxima tarefa: capítulo 7, Personagens e técnicas, com seus exemplos. Modelo: GPT-6.1 Sol; esforço alto.** Conferir Origens, cuidados, personalização, avaliação de capacidades e poderes avançados. Manter as decisões aprovadas sobre a outra voz do Receptáculo e a habilidade publicada de Reserva Condensada, sem retomar o detalhamento descartado.

Depois seguem os capítulos 8–10 e as consultas ainda necessárias. O PDF completo será composto após a passagem textual, com inspeção visual de todas as páginas e nova inspeção depois das correções. Este lote não cria outro PDF parcial nem declara inspeção do HTML no navegador. A revisão visual global e a comparação final com o livro base e os demais guias continuam pendentes.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-138/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=139,base_manifesto=4663,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[r['fonte'] for r in routes],html_alterados=[(E/r['pagina']).relative_to(R).as_posix() for r in routes])
save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 139,' in s:continue
 s=s.replace('**Fila vigente - registro 138,','**Fila histórica - registro 138,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 139, 30/10/2026:** capítulo 6 e seus apoios lidos; limites de uso, fichas, confrontos e perigos comparados. [Registro e edição atual](<{url}>). Melhoradas as classificações, referências e consultas de recursos; probabilidades selecionadas reconferidas; valores das fichas preservados. **Próximo: capítulo 7 e seus exemplos; GPT-6.1 Sol, esforço alto.** Depois, capítulos 8–10, consultas e PDF completo com revisão visual global. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua do capítulo 6.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** leitura contínua do capítulo 7 e de seus exemplos de personagens e técnicas. Depois, capítulos 8–10, demais consultas e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 139 e continuidade atualizados; leitura completa de 19 fontes neste lote.')

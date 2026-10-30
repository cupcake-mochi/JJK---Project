"""Registrar a leitura de Entre missões e preservar a continuidade do projeto."""
from pathlib import Path
import json,hashlib,os,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not json.loads((A/'conferencia.json').read_text())['falhas']
names=['08-entre-missoes.md','casos/23-retirada-e-recuperacao.md','casos/34-oficios-fabricacao-e-reparos.md','casos/36-ferramentas-objetos-e-contencao.md','casos/85-trajetorias-ferramentas-e-improvisacao.md','casos/90-reparar-personagem-de-corpo-construido.md','casos/96-fabricar-e-identificar-o-anel.md','casos/97-emprestimo-familiar-e-negociacao.md','casos/98-objeto-selado-e-risco-de-ingestao.md','casos/99-limiar-feitos-e-promocao.md','casos/103-a-febre-dos-fios.md','consultas/16-linha-de-continuidade.md','consultas/24-registro-de-estado-e-socorro.md','consultas/38-ficha-de-projeto-e-entrega.md','consultas/40-registro-de-dedicacao-por-ficha.md']
changed={row['fonte'] for row in json.loads((A/'destinos-alterados.json').read_text())};rows=[]
for name in names:
 p=T/name;rel=p.relative_to(R).as_posix()
 rows.append({'fonte':rel,'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa e segunda leitura após os ajustes; redação final dos trechos novamente conferida.' if rel in changed else 'Leitura completa e comparação com as orientações do capítulo; sem alteração neste lote.'})
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
save(A/'leitura-realizada.json',{'registro':141,'data':'2026-10-30','fontes_lidas':rows,'fonte_tecnica':primary.relative_to(R).as_posix(),'sha256_fonte_tecnica':sha(primary),'regras_consultadas':['Descansos curto e longo; ambiente propício; Exaustão; recuperação de usos','Ofícios, atributo padrão, fabricação e reparos','Ajudar em tarefas','Equipamento restrito, compras, fundo inicial e reposição','Ferramentas: grau, nível do efeito, itens em uso, cópias, criação e Desgaste','Objetos amaldiçoados, atração e selos','Cofre da Família e Palavra Empenhada','XP de missão, desconto semanal, custo de nível e Limiar','Salário por participação, recompensa por mestrar e promoção'],'limite':'Leitura editorial com comparação de exemplos e conferência aritmética selecionada. Não é teste com jogadores, avaliação econômica completa ou revisão visual do PDF completo.'})
report=R/'04 - Planejamento/141-leitura-de-atividades-e-recompensas.md'
report.write_text('''# Leitura de atividades e recompensas

Registro 141, 30 de outubro de 2026. A leitura contínua do capítulo 8, Entre missões, foi concluída com seus exemplos e folhas. Os ajustes esclarecem dedicação e recompensas, completam a explicação de salário e melhoram o registro de fechamento. Durações, custos, valores das tabelas e decisões de dedicação foram preservados.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Entre missões](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-08.html>) · [Alterações](apoio-leitura-141/alteracoes.json) · [Conferência](apoio-leitura-141/conferencia.json) · [Contas selecionadas](apoio-leitura-141/contas-conferidas.json).

## O que foi lido

Foram lidos por inteiro **15 arquivos**: o capítulo, dez casos e quatro consultas. Os casos tratam de retirada e recuperação; Ofícios e reparos; ferramentas e objetos; ferramentas e improvisação; reparo de Ena; fabricação do Anel de Testemunho; empréstimo e venda de Kenji; Pastilha do Último Aviso; feito e promoção de Aoi; e febre dos fios. As consultas são linha de continuidade, estado e socorro, projeto e entrega e dedicação por ficha.

As seis fontes modificadas passaram por uma segunda leitura; os últimos ajustes de redação foram reconferidos em contexto. Os outros nove arquivos foram comparados sem mudança. O inventário `leitura-realizada.json` identifica cada arquivo e o estado final. A referência técnica foi consultada nas partes pertinentes, sem declarar uma releitura integral do livro de regras ou de todos os casos ligados indiretamente.

## O que mudou

| Dificuldade | Ajuste |
|---|---|
| Abertura repetia duas vezes a mesma referência às regras | A apresentação explica uma vez a base e identifica o ciclo de dedicação como recomendação do Guia. |
| Horas confirmadas podiam ser confundidas com horas disponíveis | Cada estado recebe sua definição: trabalho confirmado, trabalho reservado para conferência e horas livres. A reserva continua vinculada à atividade. |
| Combinar o trabalho não identificava bem o conteúdo da seção | O subtítulo passou a Planejar o projeto; a âncora antiga foi preservada. |
| Dois sentidos de selo apareciam próximos | O capítulo distingue selo de contenção de objeto e Selo de conjuração, como já fazia o exemplo da Pastilha. |
| Dedicação e XP usam critérios diferentes | A seção semanal explicita dedicação por ficha e desconto de XP por jogador. Trocar de ficha não reinicia a contagem de XP. |
| Salário com outro total de participações não tinha fórmula no Guia | Foi incluída a orientação publicada: dividir os três quartos restantes pelo total exigido e somar uma parcela por participação, até o salário completo. O exemplo com três permanece igual. |
| O caso de Ofícios citava o estado de aprovação de treinamentos futuros | A orientação agora fala diretamente ao leitor: uma prática só altera a ficha quando uma regra explica o ganho e seus requisitos. Nenhum benefício novo foi criado. |
| O caso do Limiar remetia ao início da conferência de ficha | Agora leva a Ao subir de nível, que explica atualização e saldos. |
| A linha de continuidade era indicada para o fechamento, mas não oferecia campo de recompensas | Foi acrescentado um campo para conclusão, XP e desconto individual, dinheiro, itens, feitos e promoções confirmados ou pendentes. |
| A ficha de projeto atribuía trabalho à ficha | Passou a dizer trabalho do personagem, separado do serviço contratado. |
| A folha de dedicação abria o capítulo inteiro | A ligação agora abre diretamente Tempo para as atividades. |

São **11 registros de alteração em seis fontes**, com seis documentos HTML atualizados. Nenhuma linha de tabela mudou. Foi retirada uma repetição do número de versão 1.0 na abertura; os demais números foram preservados.

## Dedicação, trabalho e espera

Permanecem as **28 horas novas por ficha a cada ciclo de sete dias**, separadas quando um jogador possui vários personagens. Mais missões não aumentam a concessão; falta de missões ou postagens não retira a disponibilidade básica. Entrada proporcional, afastamento formal, retorno e restrição ao tempo realmente disponível na história continuam iguais.

Somente horas novas livres passam ao ciclo seguinte, com prioridade de gasto da parcela antiga. Horas antigas restantes expiram; progresso não expira nem volta a ser saldo. Trabalho pendente de conferência permanece separado e não financia outro projeto. A tabela dos três ciclos de Rina e Mei foi reconferida linha a linha, incluindo as parcelas antigas que expiram.

O Traje conserva quatro horas e ¥3.000 de materiais, sem reiniciar o projeto na troca de mestre. No Anel, Kenji executa seis horas próprias, Aya executa doze e a secagem exige doze horas sem trabalho ativo. O atendimento da febre distingue horas do profissional, disponibilidade do paciente e espera entre tentativas. O reparo de Ena continua sendo tratamento de personagem com regras da Origem, sem converter PV em horas de fabricação.

A narrativa pode incluir estudo, prática e procura de professores. **O desenvolvimento de benefícios específicos de treinamento continua pendente** e não foi substituído por bônus, XP, perda por ausência de postagem ou capacidades concedidas por concluir um projeto.

## Recompensas, equipamento e recuperação

A distinção entre dedicação por ficha, desconto semanal de XP por jogador e participação para salário foi mantida. Uma missão longa continua ocupando uma posição semanal, contando duas participações no modelo de salário e sem conceder horas extras. A fórmula de salário acrescentada é a publicada, não uma política nova ou obrigatória.

No Anel, ¥30.000 iniciais e ¥8.000 de retomada produzem ¥38.000 de custo. A venda por ¥24.000 deixa ¥26.000 de saldo, partindo dos ¥2.000 restantes; há diferença de ¥14.000 em relação ao custo, sem lucro. A instrução de duas horas reduz de 22 para 20 as horas próprias disponíveis no mesmo ciclo. Serviço e espera não foram cobrados como trabalho de Kenji.

Os exemplos de descanso conservam recuperação, Sequelas e Exaustão conforme as regras e exceções. A Pastilha mantém prazos próprios, distintos do recipiente e do aviso do Anel. Desgaste não renova por sessão ou troca de portador e não é restaurado por conserto comum. O feito de Aoi, o avanço excepcional do Limiar e a promoção continuam sendo resultados separados.

A conferência aritmética reproduziu as seis linhas de dedicação, proporções de ciclo, exemplo de conferência pendente, orçamento e venda do Anel, quatro linhas de XP semanal, salário de Grau 3 e saldo final do Limiar. Os resultados correspondem aos exemplos. Isso não mede equilíbrio econômico, lucro esperado ou comportamento de jogadores.

## Conferência e salvamento

As alterações são reproduzidas a partir das 99 cópias anteriores. A verificação compara números e todas as tabelas, admitindo apenas a retirada da citação duplicada de versão. Percorre documentos HTML, ligações, âncoras e imagens; confere também destinos Markdown. As âncoras antigas dos seis documentos alterados são conservadas. Os resultados estão em `conferencia.json`.

A edição vigente continua nas pastas `edicao-integrada-136`. Use o gerador deste apoio; preparadores antigos reconstruiriam versões anteriores aos ajustes de leitura. Os estados anteriores das fontes, documentos HTML alterados e controles estão guardados no registro 141.

O manifesto é atualizado por união a partir de **4.929 entradas**. Só são admitidas alterações em seis fontes, seis páginas HTML e nove controles de continuidade. Originais, demais textos, mapas, fontes tipográficas, provas e PDF integrado anterior permanecem preservados. O salvamento é local.

## Próxima tarefa

**Capítulo 9, Pactos e entidades, com seus exemplos e fichas. Modelo recomendado: GPT-6.1 Sol; esforço alto.** Conferir preço e benefício, modelos de Pactos, reparação da Promessa e aquisição, criação, reconstrução, transferência e estado de entidades, sem reabrir escolhas aprovadas ou usar números do Bestiário antigo.

Depois seguem capítulo 10, consultas ainda necessárias, composição do PDF completo e revisão visual de todas as páginas, repetida após as correções. Este lote não cria outro PDF parcial nem declara inspeção do HTML em navegador. A comparação final com o livro base e os demais guias continua pendente.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-140/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=141,base_manifesto=4929,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[row['fonte'] for row in routes],html_alterados=[(E/row['pagina']).relative_to(R).as_posix() for row in routes]);save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 141,' in s:continue
 s=s.replace('**Fila vigente - registro 140,','**Fila histórica - registro 140,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 141, 30/10/2026:** capítulo 8, dez casos e quatro consultas lidos; seis fontes revistas em segunda passagem. [Registro e edição atual](<{url}>). Dedicação por ficha e XP por jogador esclarecidos; fórmula publicada de salário e campo de recompensas incluídos; contas selecionadas reconferidas; tabelas e valores preservados. **Próximo: capítulo 9, Pactos e entidades, e seus exemplos; GPT-6.1 Sol, esforço alto.** Depois, capítulo 10, consultas e PDF completo com revisão visual global. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua do capítulo 8.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** leitura contínua do capítulo 9, Pactos e entidades, e seus exemplos. Depois, capítulo 10, demais consultas e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 141 e continuidade atualizados; leitura completa de 15 fontes.')

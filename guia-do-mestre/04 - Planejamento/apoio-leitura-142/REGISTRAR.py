"""Registrar a leitura do capítulo 9 e preservar as escolhas aprovadas."""
from pathlib import Path
import json,hashlib,os,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not json.loads((A/'conferencia.json').read_text())['falhas']
names=['09-pactos-e-entidades.md','casos/43-aquisicao-e-projetos-de-entidades.md','casos/45-tempo-materiais-e-retomada-de-entidades.md','casos/46-reconstruir-transferir-e-herdar-entidades.md','casos/47-desenvolver-uma-ideia-de-pacto.md','casos/48-pacifismo-impraticavel-minuta.md','casos/49-liberacao-irregular-minuta.md','casos/50-promessa-do-arquivo.md','casos/51-ritual-do-cao-de-sombra.md','casos/52-domar-o-amontoado.md','casos/54-transporte-e-continuidade-das-entidades.md','casos/55-fabricar-e-evoluir-o-vigia-do-deposito.md','consultas/42-registro-de-pactos-e-promessas.md','consultas/44-registro-de-aquisicao-e-estado-de-entidade.md']
changed={row['fonte'] for row in json.loads((A/'destinos-alterados.json').read_text())};rows=[]
for name in names:
 p=T/name;rel=p.relative_to(R).as_posix();rows.append({'fonte':rel,'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa e segunda leitura completa depois dos ajustes.' if rel in changed else 'Leitura completa e comparação com o capítulo, sem mudança neste lote.'})
retomado=json.loads((A/'escriba-retomado.json').read_text());primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
save(A/'leitura-realizada.json',{'registro':142,'data':'2026-10-30','fontes_lidas':rows,'fontes_retomadas':[retomado],'fonte_tecnica':primary.relative_to(R).as_posix(),'sha256_fonte_tecnica':sha(primary),'regras_consultadas':['Pactos: formas, escala de ganho, vagas, benefícios, aceitação, quebra e criação','Temporários: janela de Reação, Mostrar a mão e Overtime','Aquisição de entidade por espaço, lista, criação e doma','Entrada, ciclo, retorno e destruição de entidades','Corpos mantidos, inatividade, cuidados, inconsciência e morte do invocador','Carga de entidades e combate montado','Progressão, básicas, especiais e Família Livre de entidades','Criação, ajuda, nova tentativa, reconstrução, transferência e herança'],'limite':'Leitura editorial, comparação com regras e decisões e contas selecionadas. O Escriba foi retomado do estado lido no 140. Não é teste com jogadores, simulação completa de confronto ou revisão visual do PDF final.'})
report=R/'04 - Planejamento/142-leitura-de-pactos-e-entidades.md'
report.write_text('''# Leitura de Pactos e entidades

Registro 142, 30 de outubro de 2026. A leitura contínua do capítulo 9 foi concluída com seus exemplos e registros. Os ajustes explicam classificações e estados, tornam as tabelas consultáveis e melhoram os acessos. Nenhum valor de poder, prazo ou orçamento foi alterado.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Pactos e entidades](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-09.html>) · [Alterações](apoio-leitura-142/alteracoes.json) · [Conferência](apoio-leitura-142/conferencia.json) · [Contas selecionadas](apoio-leitura-142/contas-conferidas.json).

## O que foi lido

Foram lidos por inteiro **14 arquivos**: o capítulo, onze casos e duas consultas. Eles cobrem as ideias de Pactos, Pacifismo, Liberação irregular, Promessa do arquivo, aquisição e estado de entidades, tempo e materiais, reconstrução, transferência, prova do Cão de sombra, doma do Amontoado, transporte e projeto do Vigia. As consultas são os registros de Pactos e Promessas e de aquisição e estado de entidade.

O Escriba de campo foi retomado do estado já lido por inteiro no registro 140; seu hash continua igual. Ele não é contado como uma nova leitura integral neste lote. As três fontes alteradas passaram por uma segunda leitura completa depois dos ajustes. O inventário `leitura-realizada.json` identifica os arquivos e distingue a retomada da leitura nova.

## Ajustes aplicados

| Dificuldade | Ajuste |
|---|---|
| A escala de ganhos citava Estilo, mas o parágrafo de limites só dizia que Pacto não o concede | Foi explicitado que um Pacto pode modificar um Estilo já possuído, sem conceder outro, conforme a regra publicada. |
| A finalidade do sorteio inicial de Liberação irregular estava comprimida numa frase | O capítulo explica quando sortear, quais Reações ele cobre e que esse sorteio não prepara Refluxo. |
| A conta de corpos mantidos era apenas mencionada | O capítulo apresenta a fórmula publicada e separa esse total do teto de entidades que podem atuar. A consulta de aquisição leva à explicação. |
| Construir invocações podia parecer uma instrução sem referência | O texto identifica a seção do livro de regras. |
| As tabelas dependiam do texto próximo para identificar seus valores | Cinco células de cabeçalho passaram a indicar horas de trabalho e ajustes à base da CD. As linhas numéricas não mudaram. |
| Tempo e materiais só era encontrado por meio de outra consulta | O capítulo ganhou uma ligação direta ao orçamento e às etapas de trabalho. |
| Inativo e Desligada eram usados sem uma comparação direta no capítulo | Agora distingue modo inativo, queda, ativação e retorno, preservando os limites dos trabalhos extremamente simples. |
| Nova adesão a Liberação irregular era chamada de troca de ficha | A consulta nomeia saída e nova adesão ao Pacto. Os descansos exigidos e o uso de Refluxo não mudaram. |

São **10 registros de alteração em três fontes**, com três documentos HTML atualizados. Dois cabeçalhos de tabela foram ajustados, totalizando cinco células; todos os valores, demais linhas de tabela e números da prosa foram preservados.

## Escolhas dos Pactos preservadas

Pacifismo mantém violência direta impedida, responsabilidade por morte indireta, janela de trinta dias e suspensão de três. Não foi restaurada a exigência de decisão intermediária nem de conhecer previamente a vítima. Condução pela matéria continua sendo o ganho particular escolhido, sem ataques a criaturas, percepção adicional ou aumento de dano. Calendário e saída seguem o caso completo.

Liberação irregular mantém a distribuição do d6, teto total por intervalo, possibilidade de zero e Refluxo de 25% uma vez por descanso curto ou longo. O limite inicial não prepara Refluxo; recuperação não apaga o gasto do intervalo. Manutenção, energia temporária, variação de máximo, abreviação fora de combate e encerramento continuam como escritos.

A Promessa do arquivo conserva a perda de PE e o bloqueio até reparação definida ou dispensa expressa, sem punição inventada depois. Cumprir a reparação não devolve a energia perdida. Exceção por impossibilidade involuntária e critérios de entrega continuam sendo cláusulas particulares desse acordo. O texto da Promessa e o de Pacifismo ficaram intactos neste lote.

## Entidades e conferência das contas

As formas de aquisição permanecem distintas. A lista de ritual é individual; a doma permite colaboração na luta, tem risco de exorcismo e conserva o nível de aquisição. A entrada do Cão não virou teste de fabricação. O Amontoado continua recebido com a ficha convertida e os estados preservados, sem cura ou ataque gratuito.

Foram reconferidas as tabelas de criação, reconstrução e transferência: sete referências de criação e transferência, seis passagens de reconstrução e suas retomadas. Reconstruir continua custando metade da criação da Classe nova; transferir, um oitavo com arredondamento e mínimo; cada falha, metade da operação inicial, salvo projeto detalhado previamente combinado. Ajuda conserva os requisitos e o tempo de cada participante.

As contas reproduziram os três projetos do Vigia, seus máximos de vida e Integridade nos níveis apresentados e as comparações com um corpo de criação. Foram conferidos também Overtime e Refluxo nos exemplos selecionados, as janelas de Pacifismo, as dezesseis horas de bloqueio da Promessa, limites de destruição e a conta do passageiro da Mula. Não houve mudança numérica. A reconferência não mede equilíbrio de Pactos ou de encontros nem valida todas as combinações possíveis.

Ativar, retornar, transferir e recuperar recursos continuam operações diferentes. A comparação de estados não concede tarefas ou capacidades a um corpo inativo. Inconsciência não foi tratada como morte, e herança não antecipa uma morte ainda não confirmada.

## Conferência e salvamento

A conferência reproduz os ajustes a partir das 99 cópias anteriores, compara os números e admite nas tabelas apenas as cinco células declaradas. Percorre documentos HTML, ligações, âncoras e imagens, além dos destinos Markdown. As âncoras anteriores dos três documentos alterados são preservadas. Os resultados estão em `conferencia.json`.

A edição segue nas pastas `edicao-integrada-136`. Use o gerador de `apoio-leitura-142`; não reaplique os preparadores antigos sobre as fontes vigentes. Os estados anteriores foram guardados. O manifesto é atualizado por união a partir de **5.062 entradas**, admitindo apenas três fontes, três páginas HTML e nove controles anteriores alterados. Originais, demais textos, mapas, fontes tipográficas, provas e PDF anterior permanecem preservados. Este lote tem salvamento local; o último envio ao GitHub continua sendo o registro 141.

## Próxima tarefa

**Capítulo 10, Jogar em guilda, com suas consultas e exemplos. Modelo recomendado: GPT-6.1 Sol; esforço alto.** Conferir calendário, passagem entre mestres, registros, decisões e trabalho compartilhado. Manter a guilda como foco sem obrigar seu formato numa campanha fechada.

Depois seguem a conferência final do conjunto, consultas ainda necessárias, composição do PDF completo, inspeção visual de cada página e nova inspeção após as correções. Este lote não cria outro PDF parcial nem declara inspeção do HTML em navegador. A comparação final com o livro base e os demais guias continua pendente.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-141/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=142,base_manifesto=5062,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[row['fonte'] for row in routes],html_alterados=[(E/row['pagina']).relative_to(R).as_posix() for row in routes]);save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 142,' in s:continue
 s=s.replace('**Fila vigente - registro 141,','**Fila histórica - registro 141,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 142, 30/10/2026:** capítulo 9, onze casos e duas consultas lidos; Escriba retomado do estado já lido no 140; três fontes relidas após os ajustes. [Registro e edição atual](<{url}>). Corpos mantidos, estados e consulta de projetos esclarecidos; contas selecionadas reconferidas; valores e decisões de Pactos preservados. **Próximo: capítulo 10, Jogar em guilda, e seus apoios; GPT-6.1 Sol, esforço alto.** Depois, conferência final e PDF completo com revisão visual de todas as páginas. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua do capítulo 9.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** leitura contínua do capítulo 10, Jogar em guilda, e seus apoios. Depois, conferência final do conjunto e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 142 e continuidade atualizados; 14 fontes lidas e Escriba retomado sem alteração.')

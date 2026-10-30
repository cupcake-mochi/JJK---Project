"""Registrar a revisão contínua do capítulo 7, exemplos e decisões preservadas."""
from pathlib import Path
import json,hashlib,os,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
names=['07-personagens-e-tecnicas.md','casos/27-convivencia-do-receptaculo.md','casos/30-pareceres-de-criacoes.md','casos/31-avaliar-poderes-avancados.md','casos/33-casos-especificos-de-avaliacao.md','casos/53-construir-e-evoluir-o-escriba.md','casos/89-vida-rolada-e-familia-propria.md','casos/90-reparar-personagem-de-corpo-construido.md','casos/91-restricao-corporal-e-cuidados.md','casos/93-ampliar-mesclas-e-trocar-formas.md','casos/94-compras-repetidas-e-restricoes.md','casos/95-efeitos-de-cena-e-cancelamento.md','consultas/28-ficha-de-convivencia.md','consultas/32-ficha-de-avaliacao-de-capacidade.md','consultas/92-reserva-condensada-proposta-e-comparacao.md']
changed={row['fonte'] for row in json.loads((A/'destinos-alterados.json').read_text())}
rows=[]
for name in names:
 p=T/name;rel=p.relative_to(R).as_posix()
 rows.append({'fonte':rel,'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa; segunda leitura completa depois dos ajustes.' if rel in changed else 'Leitura completa e comparação com o capítulo; sem alteração neste lote.'})
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
save(A/'leitura-realizada.json',{'registro':140,'data':'2026-10-30','fontes_lidas':rows,'fonte_tecnica':primary.relative_to(R).as_posix(),'sha256_fonte_tecnica':sha(primary),'regras_consultadas':['Receptáculo: modalidades e menores; Memória Testemunha','Kamo: Execução Ensaiada e Contingência Estudada; Fundamento Incorporado','Corpo Amaldiçoado: consciências, descanso, reparo e menores','Restrição corporal: CE4, Rede Remota, Saída Elevada, três corpos e menores','Personalizar e rever a Origem','Progressão: Classes, marcos e ajuste de saldos','Pontos, preços, tetos e devoluções','Desdobramento Técnico e Remodelar','Liberação Máxima e Técnica Máxima','Regra Própria e Talento Próprio','Aptidão Própria e Bênção Própria','Expansão: aquisição, Acerto, Efeito, abertura, duração, barreira e Rescaldo','Condicional e Restrição Própria: dificuldade e prazo de revisão'],'limite':'Leitura editorial e comparação com trechos publicados. Não é teste com jogadores, nova avaliação de equilíbrio ou revisão visual do PDF completo.'})
report=R/'04 - Planejamento/140-leitura-de-personagens-e-tecnicas.md'
report.write_text('''# Leitura de personagens e técnicas

Registro 140, 30 de outubro de 2026. O capítulo 7 foi lido junto de seus exemplos e fichas de consulta. A principal correção delimita o prazo de revisão de Restrição Própria. As demais mudanças tornam explicações e referências mais diretas. Custos, dados, saldos e tabelas dos exemplos foram preservados.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Personagens e técnicas](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-07.html>) · [Alterações](apoio-leitura-140/alteracoes.json) · [Conferência](apoio-leitura-140/conferencia.json).

## Leitura e comparação

Foram lidos por inteiro **15 arquivos**: o capítulo, onze casos e três consultas. O conjunto cobre convivência do Receptáculo, avaliação de poderes, capacidades avançadas, dúvidas de montagem, vida rolada e família Arata, reparo de Ena, cuidados de Nilo, mescla de Yara, repetição de Melhorias, Restrições e cancelamento. Inclui o Escriba de campo, para conferir o intermediário usado por Nilo e a exibição examinada no cancelamento. As consultas são convivência, avaliação de capacidade e Reserva Condensada.

As cinco fontes modificadas passaram por uma segunda leitura completa após os ajustes. As demais foram comparadas com o capítulo sem receber mudanças. O inventário `leitura-realizada.json` identifica os arquivos, seu estado final e os trechos do Livro de Regras 1.0 consultados. A leitura de partes dessa referência não é declarada como releitura integral do livro de regras.

## Correções e clareza

| Trecho | Ajuste |
|---|---|
| Revisão de Restrições no capítulo, pareceres e folha de avaliação | O prazo de três sessões de uso agora está expressamente ligado à Restrição Própria. Condicional mantém a conferência de frequência nas sessões seguintes, sem ganhar esse prazo por analogia. A folha continua disponível para outros acompanhamentos. |
| Subtítulo sobre limites de armazenamento | Passou a Reserva Condensada, identificando a habilidade consultada. A âncora antiga foi conservada. |
| Roteiro de montagem | Conta passou a Pontos, indicando o que será conferido. |
| Mudanças do Emanador | Desdobramento Técnico recebe o nome publicado e fica claro que a alteração vale para aquela conjuração. A consulta citada recebe seu título e assuntos. |
| Conta da Liberação | Pontos disponíveis, preço de Linha e acréscimo de dados aparecem em frases separadas. |
| Resistência e recarga de poderes avançados | O texto identifica o alvo que recebe dano ao passar no TR e nomeia Técnica Máxima na recarga opcional. Essa opção não foi estendida à Liberação. |
| Saída Elevada | A frase vaga sobre usos foi substituída por sua função: pontos para Melhorias de feitiços comuns da técnica de Classe 1 ou maior. |
| Abertura dos pareceres | Apresenta exemplos publicados e propostas novas sem narrar a ausência de testes durante a produção do livro. |
| Recálculo de Constituição na vida rolada | A referência leva diretamente a Ao subir de nível, onde estão as regras de ajuste do saldo. |
| Cancelamento do painel | A frase identifica Interromper fluxo como a capacidade que não destrói a imagem guardada nem desliga a entidade. |

São **14 registros de alteração em cinco fontes**, com cinco documentos HTML atualizados. Nenhuma linha de tabela mudou. A explicação de Saída Elevada passou a mencionar explicitamente a Classe 1 já prevista na regra; é uma referência numérica acrescentada à prosa, sem modificar a habilidade ou os valores das fichas.

## Decisões e exemplos preservados

A outra voz do Receptáculo continua recomendada ao mestre mediante acordo com o jogador. O jogador conserva as decisões da personagem, e uma discussão não entrega controle ou poderes adicionais. Capítulo, caso de Maia e Taru e ficha de convivência concordam. Não foi criado um medidor obrigatório de relação.

Reserva Condensada permanece como a menor publicada da Restrição corporal. Os quatro campos são definidos por personagem. **Os depósitos, tetos e retiradas numéricos descartados não foram retomados.** O caso de Nilo usa Reserva Excedente e Leitura de Reservas, sem receber Reserva Condensada por associação. Comunicação comum e Rede Remota continuam separadas.

O reparo de Ena continua com uma tentativa por corpo no descanso, repetição de Manutenção Precisa dentro dessa tentativa e distinção de Reparo Autônomo. As Classes comparadas vêm dos níveis permitidos. O corpo de personagem não foi tratado como entidade Desligada.

Foram comparadas as contas apresentadas no capítulo e nos casos: Toque e Precisão; duas Classes da mescla e Forma Fluida; dados e pontos separados da Técnica Máxima; Acerto de Galeria de Vidro e duração por turnos do dono; vida rolada e crescimento do saldo. As montagens próprias continuam identificadas como propostas, sem inclusão automática no catálogo. Esta leitura não declara equilíbrio em mesa nem apresenta nova simulação de combate.

O prazo de três sessões foi conferido na entrada Restrição Própria. Condicional prevê conferir a estimativa nas sessões seguintes. O caso de Matriz de chão já distinguia essas orientações; capítulo, pareceres e folha agora seguem a mesma distinção.

## Conferência e salvamento

A verificação reproduz as alterações a partir das 99 cópias anteriores, compara as tabelas e verifica os números da prosa. A única ocorrência numérica adicionada é a referência publicada de Classe 1 em Saída Elevada. Percorre os documentos HTML, ligações, imagens e âncoras; confere também os destinos Markdown e conserva as âncoras antigas dos cinco documentos alterados. Os resultados estão em `conferencia.json`.

A edição atual continua nas pastas `edicao-integrada-136`. O gerador vigente está em `apoio-leitura-140/GERAR-LEITURA.py`; não reaplique preparadores antigos sobre as fontes atuais. O estado anterior das fontes, dos cinco documentos de leitura e dos controles está guardado neste apoio.

O manifesto é atualizado por união a partir de **4.798 entradas**. As únicas alterações admitidas nos arquivos anteriores são cinco fontes, cinco páginas HTML e nove controles de continuidade. Fontes originais, outros capítulos, mapas, fontes tipográficas, provas e PDF integrado anterior permanecem preservados. O salvamento deste lote é local.

## Próxima tarefa

**Capítulo 8, Entre missões, com seus exemplos e folhas de consulta. Modelo recomendado: GPT-6.1 Sol; esforço alto.** Conferir dedicação por ficha, fabricação, reparos, Ofícios, recompensas e limites do treinamento. Preservar o ciclo de sete dias com 28 horas por ficha e o saldo válido somente no ciclo seguinte, sem converter possibilidades de treinamento em ganhos já aprovados.

Depois seguem capítulos 9–10, consultas ainda necessárias, composição do PDF completo e inspeção visual de todas as páginas, repetida após as correções. Este lote não cria outro PDF parcial nem declara inspeção do HTML em navegador. A comparação final com o livro base e os demais guias continua pendente.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-139/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=140,base_manifesto=4798,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[row['fonte'] for row in routes],html_alterados=[(E/row['pagina']).relative_to(R).as_posix() for row in routes])
save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 140,' in s:continue
 s=s.replace('**Fila vigente - registro 139,','**Fila histórica - registro 139,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 140, 30/10/2026:** capítulo 7, onze casos e três consultas lidos; cinco fontes relidas depois dos ajustes. [Registro e edição atual](<{url}>). Prazo de revisão de Restrição Própria delimitado, montagem e poderes avançados esclarecidos; tabelas e valores preservados. Decisões do Receptáculo e de Reserva Condensada mantidas. **Próximo: capítulo 8 e seus exemplos; GPT-6.1 Sol, esforço alto.** Depois, capítulos 9–10, consultas e PDF completo com revisão visual global. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua do capítulo 7.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** leitura contínua do capítulo 8, Entre missões, e seus exemplos. Depois, capítulos 9–10, demais consultas e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 140 e continuidade atualizados; leitura completa de 15 fontes.')
